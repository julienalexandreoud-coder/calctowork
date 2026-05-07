"""Investigate audit issues."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"

print("=== 1. Content-relevance false positives? ===")
for slug, cid, lang, name in [
    ("a1c-estimator", "961", "en", "A1C Estimator"),
    ("agua-diaria-2", "403", "fr", "Daily Water Intake Calculator"),
]:
    with open(CALC_DIR / f"{slug}.json", "r", encoding="utf-8") as f:
        calc = json.load(f)
    lang_data = calc["i18n"].get(lang, {})
    content = lang_data.get("long_content", "")
    # Check what terms ARE in the content
    content_lower = content.lower()
    print(f"\n{slug} [{lang}] name='{name}'")
    for term in ["a1c", "hb", "water", "daily", "intake", "hidrat", "hydration", "agua"]:
        if term.lower() in content_lower:
            print(f"  found term: '{term}'")

print("\n=== 2. Duplicate DE names ===")
# Check if duplicates are actually the same name or just similar
name_map = {}
for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        calc = json.load(f)
    cid = calc.get("id", "")
    de_name = calc.get("i18n", {}).get("de", {}).get("name", "")
    if de_name:
        key = de_name.lower().strip()
        if key not in name_map:
            name_map[key] = []
        name_map[key].append((cid, calc.get("slug", ""), de_name))

dupes = {k: v for k, v in name_map.items() if len(v) > 1}
print(f"Total duplicate DE names: {len(dupes)}")
for name, entries in sorted(dupes.items())[:10]:
    print(f"  '{entries[0][2]}':")
    for cid, slug, n in entries:
        en_name = None
        with open(CALC_DIR / f"{slug}.json", "r", encoding="utf-8") as f:
            en_name = json.load(f).get("i18n", {}).get("en", {}).get("name", "")
        print(f"    ID={cid} slug={slug} en='{en_name}'")

print("\n=== 3. Missing fields scope ===")
missing_fields = {}
for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        calc = json.load(f)
    cid = calc.get("id", "")
    slug = calc.get("slug", cf.stem)
    i18n = calc.get("i18n", {})
    for lang in ["en", "es", "fr", "it", "pt", "de"]:
        lang_data = i18n.get(lang, {})
        for field in ["steps", "mistakes", "formula_display", "inputs", "name", "description"]:
            if field not in lang_data:
                key = (lang, field)
                if key not in missing_fields:
                    missing_fields[key] = []
                missing_fields[key].append((slug, cid))

for (lang, field), items in sorted(missing_fields.items()):
    print(f"  [{lang}] {field}: {len(items)} calculators missing")
