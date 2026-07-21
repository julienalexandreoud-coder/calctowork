#!/usr/bin/env python3
"""
Fix broken content files (wrong-article, wrong-language) by translating the
correct sibling-language article via the project's own callAI Cloud Function
(DeepSeek backend — keys stay server-side).

Work list = union of:
  A) audit/truly_wrong.json      — file contains a different calc's article
  B) WRONG_LANG rows from audit/uniqueness_report.csv

For each broken (calc, lang):
  1. Pick best clean sibling article (prefer es, then en, then fr/de/it/pt)
     — clean = not flagged wrong-article, not WRONG_LANG, not THIN, >= 700 words
  2. Prompt callAI to produce a UNIQUE, localized adaptation (not literal
     translation): localized examples/units, natural phrasing, 900-1400 words
  3. Validate: target language detected, calc name present, length OK,
     no <h1>/formula-section markers, jaccard vs source < 0.92
  4. Write file only if valid; everything logged to audit/fix_log.jsonl

Usage:
  python scripts/fix_content.py --pilot 3          # dry-run on 3 files, print results
  python scripts/fix_content.py --apply            # fix all broken files
  python scripts/fix_content.py --apply --only 1107/en,052/de
"""
import argparse
import concurrent.futures as cf
import csv
import html as htmllib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC = ROOT / "src" / "calculators"
AUDIT = ROOT / "audit"
CALL_AI = "https://us-central1-calctowork.cloudfunctions.net/callAI"
LANGS = ["es", "en", "fr", "de", "it", "pt"]
LANG_NAME = {"es": "Spanish", "en": "English", "fr": "French", "de": "German", "it": "Italian", "pt": "Portuguese"}
LOCALE_HINT = {
    "es": "Spain (metric units, euros, Spanish building conventions)",
    "en": "international English (metric units with common imperial equivalents)",
    "fr": "France (metric units, euros, French conventions)",
    "de": "Germany (metric units, euros, German conventions)",
    "it": "Italy (metric units, euros, Italian conventions)",
    "pt": "Portugal (metric units, euros, Portuguese conventions)",
}
STOPWORDS = {
    "en": {"the", "and", "of", "to", "in", "is", "for", "with", "you", "are", "this", "that", "how", "your", "can"},
    "es": {"el", "la", "de", "que", "y", "en", "los", "las", "para", "con", "una", "como", "esto", "del", "por"},
    "fr": {"le", "la", "de", "et", "les", "des", "pour", "avec", "une", "dans", "est", "que", "vous", "comment", "du"},
    "de": {"der", "die", "und", "das", "mit", "für", "ein", "eine", "ist", "wie", "den", "dem", "von", "zu", "sie"},
    "it": {"il", "la", "di", "e", "che", "per", "con", "una", "del", "della", "come", "questo", "sono", "nel", "un"},
    "pt": {"o", "a", "de", "e", "que", "para", "com", "uma", "do", "da", "como", "este", "são", "no", "um"},
}
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
WORD_RE = re.compile(r"[a-zà-ÿüöäßñç']+")

LOG = AUDIT / "fix_log.jsonl"


def norm_text(raw: str) -> str:
    t = TAG_RE.sub(" ", raw)
    return WS_RE.sub(" ", htmllib.unescape(t)).strip().lower()


def detect_lang(text: str) -> str:
    words = set(WORD_RE.findall(text))
    scores = {l: len(words & sw) for l, sw in STOPWORDS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "?"


def shingles(text: str, n: int = 6) -> set:
    ws = WORD_RE.findall(text)
    return {hash(tuple(ws[i:i + n])) for i in range(max(1, len(ws) - n + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def log_entry(rec: dict) -> None:
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load_worklist() -> dict:
    """Return {(calc, lang): reason} for all broken files."""
    work = {}
    tw = json.load((AUDIT / "truly_wrong.json").open(encoding="utf-8"))
    for w in tw:
        work[(w["calc"], w["lang"])] = "WRONG_ARTICLE"
    with (AUDIT / "uniqueness_report.csv").open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if "WRONG_LANG" in row["issues"]:
                work.setdefault((row["calc_id"], row["lang"]), "WRONG_LANG")
    return work


def load_flagged_sets():
    wrong_pairs = set()
    tw = json.load((AUDIT / "truly_wrong.json").open(encoding="utf-8"))
    for w in tw:
        wrong_pairs.add((w["calc"], w["lang"]))
    wrong_lang, thin = set(), set()
    with (AUDIT / "uniqueness_report.csv").open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if "WRONG_LANG" in row["issues"]:
                wrong_lang.add((row["calc_id"], row["lang"]))
            if "THIN" in row["issues"]:
                thin.add((row["calc_id"], row["lang"]))
    return wrong_pairs, wrong_lang, thin


def calc_meta(calc_id: str, lang: str) -> dict:
    out = {"name": "", "desc": ""}
    jf = CALC / calc_id / f"{lang}.json"
    if jf.exists():
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
            out["name"] = d.get("name", "")
            out["desc"] = d.get("desc", d.get("description", ""))
        except Exception:
            pass
    cf = CALC / calc_id / "calc.json"
    if cf.exists():
        try:
            d = json.loads(cf.read_text(encoding="utf-8"))
            out["formula"] = d.get("formula_display", d.get("formula", ""))[:400]
            ins = d.get("inputs", [])
            out["inputs"] = ", ".join(i.get("id", "") for i in ins[:8]) if isinstance(ins, list) else ""
        except Exception:
            pass
    return out


def pick_source(calc_id: str, target_lang: str, wrong_pairs, wrong_lang, thin):
    """Tier 1: clean sibling, >=700 words, correct language, unflagged."""
    for lang in LANGS:
        if lang == target_lang:
            continue
        if (calc_id, lang) in wrong_pairs or (calc_id, lang) in wrong_lang or (calc_id, lang) in thin:
            continue
        f = CALC / calc_id / f"{lang}.html"
        if not f.exists():
            continue
        raw = f.read_text(encoding="utf-8")
        words = len(norm_text(raw).split())
        if words >= 700 and detect_lang(norm_text(raw)) == lang:
            return lang, raw, words
    return None, None, 0


def pick_source_relaxed(calc_id: str, target_lang: str, wrong_pairs, wrong_lang):
    """Tier 2: topically-correct sibling (en/es preferred), >=400 words.
    May be thin — the prompt will ask to expand it."""
    for lang in ("en", "es", "fr", "de", "it", "pt"):
        if lang == target_lang:
            continue
        if (calc_id, lang) in wrong_pairs or (calc_id, lang) in wrong_lang:
            continue
        f = CALC / calc_id / f"{lang}.html"
        if not f.exists():
            continue
        raw = f.read_text(encoding="utf-8")
        text = norm_text(raw)
        if len(text.split()) >= 400 and detect_lang(text) == lang:
            return lang, raw, len(text.split())
    return None, None, 0


PROMPT_TMPL = """You are adapting a calculator article for a {target_lang_name} audience.

SOURCE ARTICLE ({src_lang_name}) for the calculator "{calc_name}":
---BEGIN SOURCE---
{source_html}
---END SOURCE---

Write a NEW article in {target_lang_name} for the same calculator "{calc_name}".
Hard requirements:
- Language: 100% natural {target_lang_name} — no sentences left in the source language.
- This is a LOCALIZATION, not a literal translation: rephrase freely, adapt examples to {locale_hint}, use different numbers in examples than the source.
- Structure: HTML fragment with 4-6 <h2> sections. Sections should cover: what the calculator does and when to use it; the formula explained variable by variable; 2 worked examples with concrete numbers; common mistakes; a short FAQ (2-3 questions with answers as <h3>+<p> or a list).
- Start directly with a <p> introduction that mentions "{calc_name}" naturally in the first two sentences.
- Allowed tags only: <h2>, <h3>, <p>, <ul>, <li>, <ol>, <strong>, <em>, <table>, <tr>, <th>, <td>. NO <h1>. No CSS classes. No markdown. No ``` fences.
- Length: 900-1400 words.
- Do NOT copy whole sentences from the source; every sentence must be freshly written in {target_lang_name}.
- Output ONLY the HTML fragment, nothing else."""


FRESH_PROMPT_TMPL = """Write a complete SEO article in {target_lang_name} for the calculator "{calc_name}".

Calculator details:
- Name: {calc_name}
- What it does: {calc_desc}
- Formula: {formula}
- Input fields: {inputs}
- Audience locale: {locale_hint}

Hard requirements:
- Language: 100% natural {target_lang_name}.
- Structure: HTML fragment with 4-6 <h2> sections covering: what the calculator does and when to use it; the formula explained variable by variable; 2 worked examples with concrete numbers; common mistakes; a short FAQ (2-3 questions with answers).
- Start directly with a <p> introduction that mentions "{calc_name}" naturally in the first two sentences.
- Allowed tags only: <h2>, <h3>, <p>, <ul>, <li>, <ol>, <strong>, <em>, <table>, <tr>, <th>, <td>. NO <h1>. No CSS classes. No markdown. No ``` fences.
- Length: 900-1400 words.
- Output ONLY the HTML fragment, nothing else."""

EXPAND_NOTE = """
IMPORTANT: the source is SHORT. Keep the facts, but EXPAND to 900-1400 words: add a second worked example, add common mistakes, add the FAQ — all freshly written in {target_lang_name}."""


def call_ai(prompt: str, retries: int = 2) -> str:
    body = json.dumps({"messages": [{"role": "user", "content": prompt}], "maxTokens": 6000}).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(CALL_AI, data=body, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=110) as resp:
                data = json.loads(resp.read().decode())
            return data.get("text", "")
        except Exception as e:
            if attempt == retries:
                raise
            time.sleep(3 * (attempt + 1))
    return ""


def clean_ai_html(text: str) -> str:
    t = text.strip()
    t = re.sub(r"^```(?:html)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    return t.strip()


def validate(html_out: str, calc_id: str, lang: str, meta: dict, src_shingles: set):
    """Return list of failure reasons (empty = pass)."""
    fails = []
    text = norm_text(html_out)
    words = len(text.split())
    if words < 650:
        fails.append(f"short({words}w)")
    if words > 2200:
        fails.append(f"long({words}w)")
    dl = detect_lang(text)
    if dl != lang:
        fails.append(f"lang={dl}")
    if re.search(r"<h1[\s>]", html_out, re.I):
        fails.append("has_h1")
    if "formula-section" in html_out:
        fails.append("tpl_class")
    name_keys = [w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", meta.get("name", ""))][:4]
    if name_keys and not any(k in text for k in name_keys):
        fails.append("name_absent")
    if src_shingles:
        j = jaccard(shingles(text), src_shingles)
        if j > 0.92:
            fails.append(f"too_similar_to_source({j:.2f})")
    return fails


def process(item, wrong_pairs, wrong_lang, thin, apply: bool):
    calc_id, lang, reason = item
    meta = calc_meta(calc_id, lang)
    src_lang, src_html, src_words = pick_source(calc_id, lang, wrong_pairs, wrong_lang, thin)
    rec = {"calc": calc_id, "lang": lang, "reason": reason, "src": src_lang, "status": ""}
    if src_html:
        prompt = PROMPT_TMPL.format(
            target_lang_name=LANG_NAME[lang], src_lang_name=LANG_NAME[src_lang],
            calc_name=meta["name"] or calc_id, locale_hint=LOCALE_HINT[lang],
            source_html=src_html[:14000])
        src_sh = shingles(norm_text(src_html))
    else:
        # Tier 2: thin but topically-correct sibling — expand it
        src_lang, src_html, src_words = pick_source_relaxed(calc_id, lang, wrong_pairs, wrong_lang)
        if src_html:
            prompt = PROMPT_TMPL.format(
                target_lang_name=LANG_NAME[lang], src_lang_name=LANG_NAME[src_lang],
                calc_name=meta["name"] or calc_id, locale_hint=LOCALE_HINT[lang],
                source_html=src_html[:12000]) + EXPAND_NOTE.format(target_lang_name=LANG_NAME[lang])
            src_sh = shingles(norm_text(src_html))
        else:
            # Tier 3: no sibling at all — generate fresh from metadata
            if not meta.get("name"):
                rec["status"] = "SKIP:no_metadata"
                return rec
            prompt = FRESH_PROMPT_TMPL.format(
                target_lang_name=LANG_NAME[lang], calc_name=meta["name"],
                calc_desc=meta.get("desc", ""), formula=meta.get("formula", ""),
                inputs=meta.get("inputs", ""), locale_hint=LOCALE_HINT[lang])
            src_sh = None
            rec["src"] = "fresh"
    if not apply:
        rec["status"] = "DRY"
        rec["prompt_chars"] = len(prompt)
        return rec
    try:
        out = clean_ai_html(call_ai(prompt))
    except Exception as e:
        rec["status"] = f"ERROR:{e.__class__.__name__}"
        return rec
    fails = validate(out, calc_id, lang, meta, src_sh)
    if fails:
        rec["status"] = "INVALID:" + ",".join(fails)
        rec["out_words"] = len(norm_text(out).split())
        return rec
    target = CALC / calc_id / f"{lang}.html"
    target.write_text(out, encoding="utf-8")
    rec["status"] = "FIXED"
    rec["out_words"] = len(norm_text(out).split())
    return rec


def process_fresh(item, apply: bool):
    """Rewrite a templated file from metadata only (forced uniqueness)."""
    calc_id, lang, reason = item
    meta = calc_meta(calc_id, lang)
    rec = {"calc": calc_id, "lang": lang, "reason": reason, "src": "fresh", "status": ""}
    if not meta.get("name"):
        rec["status"] = "SKIP:no_metadata"
        return rec
    prompt = FRESH_PROMPT_TMPL.format(
        target_lang_name=LANG_NAME[lang], calc_name=meta["name"],
        calc_desc=meta.get("desc", ""), formula=meta.get("formula", ""),
        inputs=meta.get("inputs", ""), locale_hint=LOCALE_HINT[lang])
    if not apply:
        rec["status"] = "DRY"
        return rec
    try:
        out = clean_ai_html(call_ai(prompt))
    except Exception as e:
        rec["status"] = f"ERROR:{e.__class__.__name__}"
        return rec
    fails = validate(out, calc_id, lang, meta, None)
    if fails:
        rec["status"] = "INVALID:" + ",".join(fails)
        rec["out_words"] = len(norm_text(out).split())
        return rec
    (CALC / calc_id / f"{lang}.html").write_text(out, encoding="utf-8")
    rec["status"] = "FIXED"
    rec["out_words"] = len(norm_text(out).split())
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", type=int, default=0)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--boilerplate", action="store_true",
                    help="Rewrite files >=70%% boilerplate (audit/boilerplate.json) fresh from metadata")
    args = ap.parse_args()

    if args.boilerplate:
        bp = json.load((AUDIT / "boilerplate.json").open(encoding="utf-8"))
        items = []
        for key, ratio in bp.items():
            if ratio >= 0.70:
                cid, lang = key.split("/")
                items.append((cid, lang, f"BOILERPLATE_{ratio:.0%}"))
        items.sort()
        # Resume: skip already fixed
        if LOG.exists():
            latest = {}
            for line in LOG.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    r = json.loads(line)
                    latest[(r["calc"], r["lang"])] = (r.get("status", ""), r.get("reason", ""))
            before = len(items)
            items = [i for i in items if not (latest.get((i[0], i[1]), ("", ""))[0] == "FIXED"
                                              and latest.get((i[0], i[1]), ("", ""))[1].startswith("BOILERPLATE"))]
            if before != len(items):
                print(f"Resume: skipping {before - len(items)} already-FIXED files")
        if args.only:
            wanted = {tuple(x.split("/")) for x in args.only.split(",")}
            items = [i for i in items if (i[0], i[1]) in wanted]
        if args.pilot:
            items = items[: args.pilot]
        print(f"Boilerplate rewrite list: {len(items)} files ({'APPLY' if args.apply else 'DRY-RUN'})")
        done = 0
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(process_fresh, it, args.apply): it for it in items}
            for fut in cf.as_completed(futs):
                rec = fut.result()
                log_entry(rec)
                done += 1
                if done % 25 == 0 or done == len(items):
                    print(f"[{done}/{len(items)}] last: {rec['calc']}/{rec['lang']}: {rec['status']}", flush=True)
        return

    work = load_worklist()
    wrong_pairs, wrong_lang, thin = load_flagged_sets()
    items = [(c, l, r) for (c, l), r in sorted(work.items())]
    # Resume: skip files already FIXED in a previous run
    if LOG.exists():
        latest = {}
        for line in LOG.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                latest[(r["calc"], r["lang"])] = r.get("status", "")
        before = len(items)
        items = [i for i in items if latest.get((i[0], i[1])) != "FIXED"]
        if before != len(items):
            print(f"Resume: skipping {before - len(items)} already-FIXED files")
    if args.only:
        wanted = {tuple(x.split("/")) for x in args.only.split(",")}
        items = [i for i in items if (i[0], i[1]) in wanted]
    if args.pilot:
        items = items[: args.pilot]

    print(f"Work list: {len(items)} files ({'APPLY' if args.apply else 'DRY-RUN'})")
    done = 0
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process, it, wrong_pairs, wrong_lang, thin, args.apply): it for it in items}
        for fut in cf.as_completed(futs):
            rec = fut.result()
            log_entry(rec)
            done += 1
            print(f"[{done}/{len(items)}] {rec['calc']}/{rec['lang']} ({rec['reason']}): {rec['status']}")


if __name__ == "__main__":
    sys.exit(main())
