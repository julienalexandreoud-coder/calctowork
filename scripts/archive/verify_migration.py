"""Verify the migration was successful."""
import json
import os
import sys
from pathlib import Path

CALC_DIR = Path(__file__).parent.parent / "src" / "calculators"
I18N_DIR = Path(__file__).parent.parent / "src" / "i18n"
CONTENT_DIR = Path(__file__).parent.parent / "src" / "content"

# 1. Check content directory is gone
print(f"Content dir exists: {CONTENT_DIR.exists()} (should be False)")

# 2. Check i18n files no longer have calculators key
print("\n=== i18n files ===")
for lang in ["en", "es", "de", "fr", "it", "pt"]:
    try:
        with open(I18N_DIR / f"{lang}.json", "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        has_calcs = "calculators" in data
        print(f"  {lang}.json: {len(data)} keys, 'calculators' removed={not has_calcs}")
    except Exception as e:
        print(f"  {lang}.json: ERROR - {e}")

# 3. Check calculators have long_content
print("\n=== Calculator JSONs ===")
total = 0
missing_long = 0
missing_i18n = 0
example_shown = False

for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    total += 1
    try:
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
    except Exception:
        continue

    cid = calc.get("id", "")
    if not cid:
        continue

    for lang in ["en", "es", "de", "fr", "it", "pt"]:
        i18n = calc.get("i18n", {})
        lang_i18n = i18n.get(lang, {})
        if not lang_i18n:
            missing_i18n += 1
            continue
        lc = lang_i18n.get("long_content", "")
        if not lc:
            missing_long += 1
            if not example_shown:
                print(f"  Missing long_content in {cf.name} / {lang}")
                example_shown = True

print(f"  Total calculators: {total}")
print(f"  Missing i18n blocks: {missing_i18n}")
print(f"  Missing long_content: {missing_long}")

# 4. Show a sample calculator en i18n keys
if total > 0:
    for cf in sorted(CALC_DIR.glob("*.json")):
        if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
            continue
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        en = calc.get("i18n", {}).get("en", {})
        print(f"\n=== Sample: {cf.name} ===")
        print(f"  i18n.en keys: {sorted(en.keys())}")
        if "long_content" in en:
            print(f"  long_content: {len(en['long_content'])} chars")
        break

# 5. Check scripts dir is clean
scripts_dir = Path(__file__).parent
active_scripts = [f.name for f in scripts_dir.glob("*.py") 
                  if f.name not in ("__init__.py",)]
print(f"\n=== Active scripts ({len(active_scripts)}) ===")
for s in sorted(active_scripts):
    print(f"  {s}")

# 6. Check docs dir
docs_dir = Path(__file__).parent.parent / "docs"
if docs_dir.exists():
    doc_files = [f.name for f in docs_dir.iterdir() if f.is_file()]
    print(f"\n=== Docs ({len(doc_files)}) ===")
    for d in sorted(doc_files):
        print(f"  {d}")

print(f"\n{'='*40}")
print(f"Migration verification complete")
