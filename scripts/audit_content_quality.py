#!/usr/bin/env python3
"""
Audit: check every calculator has quality content in all 6 languages,
IDs are consistent across languages, and content is relevant to the calculator.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"
LANGS = ["en", "es", "de", "fr", "it", "pt"]

REPORT = []

def log(msg):
    REPORT.append(msg)
    print(msg)

def check_lang_coverage():
    """Check every calculator has i18n + long_content for all 6 languages."""
    log("\n=== 1. Language Coverage ===")
    ok = 0
    missing_any = 0
    partial = 0
    missing_detail = []

    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)

        cid = calc.get("id", "")
        slug = calc.get("slug", cf.stem)
        i18n = calc.get("i18n", {})

        missing = []
        for lang in LANGS:
            lang_data = i18n.get(lang, {})
            if not lang_data:
                missing.append(f"{lang}:no_data")
            elif not lang_data.get("long_content", "").strip():
                missing.append(f"{lang}:no_content")
            elif len(lang_data.get("long_content", "")) < 500:
                missing.append(f"{lang}:too_short({len(lang_data.get('long_content',''))})")

        if not missing:
            ok += 1
        elif any("no_data" in m for m in missing):
            missing_any += 1
            missing_detail.append((slug, cid, missing))
        else:
            partial += 1
            if len(missing_detail) < 20:
                missing_detail.append((slug, cid, missing))

    log(f"  Full coverage (all 6 langs): {ok}/{ok+missing_any+partial}")
    log(f"  Missing entire language blocks: {missing_any}")
    log(f"  Missing or short content: {partial}")
    for slug, cid, issues in missing_detail[:10]:
        log(f"    {slug} (id={cid}): {issues}")
    return ok, missing_any, partial


def check_id_consistency():
    """Verify all calculator IDs are present in every language's i18n."""
    log("\n=== 2. ID Consistency Across Languages ===")
    ids_by_lang = defaultdict(set)
    calc_names = {}

    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        cid = calc.get("id", "")
        if not cid:
            continue
        i18n = calc.get("i18n", {})
        for lang in LANGS:
            if lang in i18n and i18n[lang]:
                ids_by_lang[lang].add(cid)
        calc_names[cid] = {
            lang: i18n.get(lang, {}).get("name", "") for lang in LANGS
        }

    # Check all language ID sets are identical
    base_set = ids_by_lang.get("en", set())
    mismatches = []
    for lang in LANGS:
        if lang == "en":
            continue
        diff = base_set - ids_by_lang[lang]
        if diff:
            mismatches.append((lang, "missing", sorted(diff)[:10]))
        extra = ids_by_lang[lang] - base_set
        if extra:
            mismatches.append((lang, "extra", sorted(extra)[:10]))

    if mismatches:
        log(f"  ID MISMATCHES FOUND:")
        for lang, kind, ids in mismatches:
            log(f"    {lang}: {kind} {ids}")
    else:
        log(f"  All 6 languages have the same {len(base_set)} calculator IDs [OK]")

    # Check for duplicate names (different calculators with same name in a language)
    log("\n  Checking for duplicate names across calculators...")
    name_to_ids = defaultdict(list)
    for cid, names in calc_names.items():
        for lang, name in names.items():
            if name:
                name_to_ids[(lang, name.lower().strip())].append(cid)

    dupes = {k: v for k, v in name_to_ids.items() if len(v) > 1}
    if dupes:
        log(f"  Found {len(dupes)} duplicate names:")
        for (lang, name), ids in sorted(dupes.items())[:10]:
            log(f"    {lang}: '{name}' used by IDs {ids}")
    else:
        log(f"  No duplicate names found [OK]")
    
    return len(base_set)


def check_content_relevance():
    """Check content includes the calculator name (basic relevance check)."""
    log("\n=== 3. Content Relevance Check ===")

    irrelevant = []
    short_content = []
    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        cid = calc.get("id", "")
        slug = calc.get("slug", cf.stem)
        i18n = calc.get("i18n", {})

        for lang in LANGS:
            lang_data = i18n.get(lang, {})
            content = lang_data.get("long_content", "")
            name = lang_data.get("name", "")
            desc = lang_data.get("description", "")

            if not content.strip():
                continue

            # Check content mentions the calculator name or key terms
            content_lower = content.lower()
            name_words = re.findall(r'\w+', name.lower())
            key_terms = [w for w in name_words if len(w) > 3]

            found = any(term in content_lower for term in key_terms) if key_terms else True
            if not found:
                irrelevant.append((slug, cid, lang, name[:40]))

            # Check minimum content length
            if len(content) < 1000:
                short_content.append((slug, cid, lang, len(content)))

    if irrelevant:
        log(f"  Calculators where content doesn't mention the calculator name:")
        for slug, cid, lang, name in irrelevant[:15]:
            log(f"    {slug} (id={cid}) [{lang}]: name='{name}' not found in content")
    else:
        log(f"  All content mentions the calculator name [OK]")

    if short_content:
        log(f"\n  Suspiciously short content (<1000 chars):")
        for slug, cid, lang, length in sorted(short_content, key=lambda x: x[3])[:15]:
            log(f"    {slug} (id={cid}) [{lang}]: {length} chars")
    else:
        log(f"  No suspiciously short content [OK]")


def check_spanish_source():
    """Verify Spanish (source lang) has content and all IDs."""
    log("\n=== 4. Spanish (Source Language) Health ===")
    es_count = 0
    es_no_content = 0
    es_short = 0
    
    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        cid = calc.get("id", "")
        i18n = calc.get("i18n", {})
        es = i18n.get("es", {})
        if es:
            es_count += 1
            content = es.get("long_content", "")
            if not content.strip():
                es_no_content += 1
            elif len(content) < 1000:
                es_short += 1
    
    log(f"  Spanish calculators with i18n: {es_count}")
    log(f"  Missing content: {es_no_content}")
    log(f"  Short content (<1000): {es_short}")


def check_translation_gaps():
    """Flag content where all languages have identical content (suggests no translation)."""
    log("\n=== 5. Translation Quality (Content Similarity) ===")
    identical_across_langs = 0
    
    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        cid = calc.get("id", "")
        i18n = calc.get("i18n", {})

        contents = []
        for lang in LANGS:
            lang_data = i18n.get(lang, {})
            content = lang_data.get("long_content", "")
            if content.strip():
                # Normalize: strip whitespace, lowercase first 200 chars
                sig = content.strip()[:200].lower()
                contents.append((lang, sig))
        
        if len(contents) >= 6:
            first_sig = contents[0][1]
            all_same = all(sig == first_sig for _, sig in contents)
            if all_same:
                identical_across_langs += 1
                if identical_across_langs <= 5:
                    name = calc.get("slug", cid)
                    log(f"    {name} (id={cid}): ALL 6 languages have identical content (untranslated?)")
    
    if identical_across_langs:
        log(f"  Total calculators with identical content across all 6 langs: {identical_across_langs}")
    else:
        log(f"  All calculators have distinct content per language [OK]")


def check_formula_i18n_gaps():
    """Check that if a field has i18n in one language, it has it in all."""
    log("\n=== 6. i18n Field Completeness ===")
    field_gaps = defaultdict(list)

    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        slug = calc.get("slug", cf.stem)
        cid = calc.get("id", "")
        i18n = calc.get("i18n", {})

        # Check steps
        for lang in LANGS:
            lang_data = i18n.get(lang, {})
            if not lang_data:
                continue
            # Check that all field types present
            for field in ["name", "description", "seo_title", "seo_description",
                          "inputs", "outputs", "steps", "mistakes", "formula_display"]:
                if field not in lang_data:
                    field_gaps[(lang, field)].append((slug, cid))

    for (lang, field), calcs in sorted(field_gaps.items()):
        log(f"  [{lang}] missing '{field}' in {len(calcs)} calculators:")
        for slug, cid in calcs[:5]:
            log(f"    {slug} (id={cid})")
        if len(calcs) > 5:
            log(f"    ... and {len(calcs)-5} more")


if __name__ == "__main__":
    total = len([cf for cf in CALC_DIR.glob("*.json") 
                 if cf.name not in ("calculators.json", "monolithic.json", "backup.json")])
    log(f"Auditing {total} calculators across {len(LANGS)} languages\n")
    
    check_lang_coverage()
    n_ids = check_id_consistency()
    check_content_relevance()
    check_spanish_source()
    check_translation_gaps()
    check_formula_i18n_gaps()

    log(f"\n{'='*50}")
    log(f"Audit complete. {total} calculators checked.")
