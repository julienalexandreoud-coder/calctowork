#!/usr/bin/env python3
"""
Content uniqueness audit for CalcToWork.

Data model (2026-07): src/calculators/{id}/{lang}.html  — one article per calc per lang.
Detects, per language and cross-calculator:
  1. EXACT_DUP      — identical normalized text under different calculator IDs
  2. TEMPLATE_GROUP — articles sharing the same H2 skeleton AND same opening
                      (rigid template indicator from docs/TODO.md)
  3. NEAR_DUP       — high Jaccard similarity on word 6-shingles (>= 0.65),
                      computed only within candidate buckets (fast)
  4. THIN           — < 600 words of body text
  5. TPL_MARKERS    — contains <h1> tag or 'formula-section' class (template indicators)
  6. WRONG_LANG     — body stopword profile doesn't match the file's language

Output: audit/uniqueness_report.csv  (one row per file, worst severity)
        audit/uniqueness_summary.txt (aggregate stats + worst offenders)

Usage:  python scripts/audit_uniqueness.py
"""
import csv
import hashlib
import html
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"
AUDIT_DIR = ROOT / "audit"
LANGS = ["en", "es", "fr", "de", "it", "pt"]

THIN_WORDS = 600
NEAR_DUP_THRESHOLD = 0.65

STOPWORDS = {
    "en": {"the", "and", "of", "to", "in", "is", "for", "with", "you", "are", "this", "that", "how", "your", "can"},
    "es": {"el", "la", "de", "que", "y", "en", "los", "las", "para", "con", "una", "como", "esto", "del", "por"},
    "fr": {"le", "la", "de", "et", "les", "des", "pour", "avec", "une", "dans", "est", "que", "vous", "comment", "du"},
    "de": {"der", "die", "und", "das", "mit", "für", "ein", "eine", "ist", "wie", "den", "dem", "von", "zu", "sie"},
    "it": {"il", "la", "di", "e", "che", "per", "con", "una", "del", "della", "come", "questo", "sono", "nel", "un"},
    "pt": {"o", "a", "de", "e", "que", "para", "com", "uma", "do", "da", "como", "este", "são", "no", "um"},
}

TAG_RE = re.compile(r"<[^>]+>")
H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.IGNORECASE | re.DOTALL)
H1_RE = re.compile(r"<h1[\s>]", re.IGNORECASE)
WS_RE = re.compile(r"\s+")
WORD_RE = re.compile(r"[a-zà-ÿüöäßñç']+")


def normalize_text(raw_html: str) -> str:
    text = TAG_RE.sub(" ", raw_html)
    text = html.unescape(text).lower()
    return WS_RE.sub(" ", text).strip()


def shingles(text: str, n: int = 6) -> set:
    words = WORD_RE.findall(text)
    if len(words) < n:
        return {tuple(words)} if words else set()
    return {hash(tuple(words[i:i + n])) for i in range(len(words) - n + 1)}


def detect_lang(text: str) -> str:
    words = set(WORD_RE.findall(text))
    scores = {lang: len(words & sw) for lang, sw in STOPWORDS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "?"


def h2_skeleton(raw_html: str) -> str:
    heads = [WS_RE.sub(" ", TAG_RE.sub("", h)).strip().lower() for h in H2_RE.findall(raw_html)]
    return "|".join(heads)


def main() -> None:
    AUDIT_DIR.mkdir(exist_ok=True)
    files = sorted(CALC_DIR.glob("*/[a-z][a-z].html"))
    print(f"Auditing {len(files)} content files...")

    rows = []  # per-file record
    by_lang = defaultdict(list)

    for f in files:
        calc_id = f.parent.name
        lang = f.stem
        raw = f.read_text(encoding="utf-8", errors="replace")
        text = normalize_text(raw)
        words = text.split()
        rec = {
            "calc_id": calc_id,
            "lang": lang,
            "path": str(f.relative_to(ROOT)),
            "words": len(words),
            "hash": hashlib.md5(text.encode()).hexdigest(),
            "open300": hashlib.md5(text[:300].encode()).hexdigest(),
            "skeleton": h2_skeleton(raw),
            "has_h1": bool(H1_RE.search(raw)),
            "has_formula_section": "formula-section" in raw,
            "detected_lang": detect_lang(text),
            "shingles": shingles(text),
        }
        rows.append(rec)
        by_lang[lang].append(rec)

    issues = defaultdict(list)  # (calc_id, lang) -> list of (severity, detail)

    # 1. Exact duplicates (same normalized text, different calc, same lang)
    hash_groups = defaultdict(list)
    for r in rows:
        hash_groups[(r["lang"], r["hash"])].append(r)
    for (lang, h), group in hash_groups.items():
        if len(group) > 1:
            ids = sorted(g["calc_id"] for g in group)
            for g in group:
                issues[(g["calc_id"], lang)].append(("EXACT_DUP", f"identical to {','.join(i for i in ids if i != g['calc_id'])}"))

    # 2. Template groups: same H2 skeleton + same opening, different calcs, same lang
    tpl_groups = defaultdict(list)
    for r in rows:
        if r["skeleton"]:
            tpl_groups[(r["lang"], r["skeleton"], r["open300"])].append(r)
    for (lang, skel, op), group in tpl_groups.items():
        if len(group) > 1:
            ids = sorted(g["calc_id"] for g in group)
            for g in group:
                issues[(g["calc_id"], lang)].append(("TEMPLATE_GROUP", f"{len(group)} calcs share skeleton+opening: {','.join(ids[:8])}"))

    # 3. Near-duplicates: candidate pairs share same opening bucket OR same skeleton;
    #    compare Jaccard only within buckets to keep it O(n)ish.
    cand_groups = defaultdict(list)
    for lang, recs in by_lang.items():
        for r in recs:
            cand_groups[(lang, "open", r["open300"])].append(r)
            if r["skeleton"]:
                cand_groups[(lang, "skel", r["skeleton"])].append(r)
    compared = set()
    for (lang, kind, key), group in cand_groups.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                pair = tuple(sorted([(a["calc_id"], lang), (b["calc_id"], lang)]))
                if pair in compared:
                    continue
                compared.add(pair)
                sa, sb = a["shingles"], b["shingles"]
                if not sa or not sb:
                    continue
                j = len(sa & sb) / len(sa | sb)
                if j >= NEAR_DUP_THRESHOLD and (("NEAR_DUP", "") not in [x for x in issues[(a["calc_id"], lang)] if x[0] == "NEAR_DUP"]):
                    detail = f"jaccard={j:.2f} with {b['calc_id']}"
                    issues[(a["calc_id"], lang)].append(("NEAR_DUP", detail))
                    issues[(b["calc_id"], lang)].append(("NEAR_DUP", f"jaccard={j:.2f} with {a['calc_id']}"))

    # 4-6. Per-file checks
    for r in rows:
        key = (r["calc_id"], r["lang"])
        if r["words"] < THIN_WORDS:
            issues[key].append(("THIN", f"{r['words']} words"))
        if r["has_h1"]:
            issues[key].append(("TPL_MARKERS", "contains <h1>"))
        if r["has_formula_section"]:
            issues[key].append(("TPL_MARKERS", "contains formula-section class"))
        if r["detected_lang"] != "?" and r["detected_lang"] != r["lang"] and r["words"] > 200:
            issues[key].append(("WRONG_LANG", f"detected={r['detected_lang']}"))

    # ---- Write CSV ----
    severity_rank = {"EXACT_DUP": 5, "NEAR_DUP": 4, "TEMPLATE_GROUP": 3, "WRONG_LANG": 2, "THIN": 1, "TPL_MARKERS": 1}
    csv_path = AUDIT_DIR / "uniqueness_report.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["calc_id", "lang", "worst_severity", "issues", "words", "detected_lang", "path"])
        for r in sorted(rows, key=lambda x: (x["lang"], x["calc_id"])):
            iss = issues.get((r["calc_id"], r["lang"]), [])
            if not iss:
                continue
            worst = max(iss, key=lambda x: severity_rank.get(x[0], 0))[0]
            w.writerow([r["calc_id"], r["lang"], worst, " ; ".join(f"{s}: {d}" for s, d in iss),
                        r["words"], r["detected_lang"], r["path"]])

    # ---- Summary ----
    lines = ["=" * 60, "CONTENT UNIQUENESS AUDIT — SUMMARY", "=" * 60, f"Files audited: {len(rows)}"]
    per_lang_counts = {lang: len(recs) for lang, recs in sorted(by_lang.items())}
    lines.append(f"Per language: {per_lang_counts}")
    lines.append("")
    sev_counts = defaultdict(int)
    for key, iss in issues.items():
        worst = max(iss, key=lambda x: severity_rank.get(x[0], 0))[0]
        sev_counts[worst] += 1
    for sev in ["EXACT_DUP", "NEAR_DUP", "TEMPLATE_GROUP", "WRONG_LANG", "THIN", "TPL_MARKERS"]:
        lines.append(f"  {sev:15s}: {sev_counts.get(sev, 0)} files")
    clean = len(rows) - len(issues)
    lines.append(f"\n  CLEAN          : {clean} files ({100*clean/max(len(rows),1):.1f}%)")
    lines.append(f"  FLAGGED        : {len(issues)} files ({100*len(issues)/max(len(rows),1):.1f}%)")

    # Breakdown per language of worst severities
    lines.append("\nPer-language breakdown of flagged files:")
    for lang in LANGS:
        lang_issues = {k: v for k, v in issues.items() if k[1] == lang}
        counts = defaultdict(int)
        for k, iss in lang_issues.items():
            worst = max(iss, key=lambda x: severity_rank.get(x[0], 0))[0]
            counts[worst] += 1
        total_lang = per_lang_counts.get(lang, 0)
        lines.append(f"  {lang}: {len(lang_issues)}/{total_lang} flagged — " +
                     ", ".join(f"{s}={c}" for s, c in sorted(counts.items())))

    summary_path = AUDIT_DIR / "uniqueness_summary.txt"
    summary = "\n".join(lines)
    summary_path.write_text(summary, encoding="utf-8")
    print(summary)
    print(f"\nCSV: {csv_path}\nSummary: {summary_path}")


if __name__ == "__main__":
    sys.exit(main())
