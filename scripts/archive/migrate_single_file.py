#!/usr/bin/env python3
"""
Migration script: merge content HTML files into calculator JSON i18n blocks,
remove dead `calculators` key from i18n JSON, delete content/ directory,
and update the generator.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"
CONTENT_DIR = ROOT / "src" / "content"
I18N_DIR = ROOT / "src" / "i18n"
GENERATOR = ROOT / "scripts" / "generate_calctowork.py"
LANGS = ["en", "es", "de", "fr", "it", "pt"]

# ── Step 1: Merge content/{lang}/{id}.html into calculator JSON i18n ──
print("=== Step 1: Merging content files into calculator JSONs ===")
calc_files = sorted(CALC_DIR.glob("*.json"))
merged = 0
missing_content = 0

for cf in calc_files:
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        calc = json.load(f)
    cid = calc.get("id", "")
    if not cid:
        continue
    changed = False
    for lang in LANGS:
        content_file = CONTENT_DIR / lang / f"{cid}.html"
        if content_file.exists():
            content_html = content_file.read_text(encoding="utf-8")
            if "i18n" not in calc:
                calc["i18n"] = {}
            if lang not in calc["i18n"]:
                calc["i18n"][lang] = {}
            calc["i18n"][lang]["long_content"] = content_html
            changed = True
            merged += 1
        else:
            missing_content += 1
    if changed:
        with open(cf, "w", encoding="utf-8") as f:
            json.dump(calc, f, ensure_ascii=False, indent=2)

print(f"  Merged {merged} content files across {len(calc_files)} calculators")
print(f"  Missing content: {missing_content}")

# ── Step 2: Remove `calculators` key from i18n JSON files ──
print("\n=== Step 2: Removing dead `calculators` key from i18n JSONs ===")
for lang in LANGS:
    path = I18N_DIR / f"{lang}.json"
    with open(path, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if "calculators" in data:
        calc_count = len(data["calculators"])
        del data["calculators"]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"  {lang}.json: removed calculators key ({calc_count} entries)")
    else:
        print(f"  {lang}.json: no calculators key found")

# ── Step 3: Delete content/ directory ──
print("\n=== Step 3: Deleting content/ directory ===")
if CONTENT_DIR.exists():
    shutil.rmtree(CONTENT_DIR)
    print("  Deleted src/content/")

# ── Step 4: Update generator to read long_content from calc JSON i18n ──
print("\n=== Step 4: Updating generator ===")
gen_content = GENERATOR.read_text(encoding="utf-8")

# Replace the content file reading block
old_content_block = """            content_file = CONTENT_DIR / lang / f"{cid}.html"
            has_long_content = content_file.exists()
            if has_long_content:
                long_content_raw = content_file.read_text(encoding="utf-8")
            else:
                long_content_raw = generate_long_content(cid, lang, calc_name=ci18n["name"])"""

new_content_block = """            # Read long_content from calculator JSON i18n block
            calc_long = calc.get("i18n", {}).get(lang, {}).get("long_content", "")
            if calc_long:
                long_content_raw = calc_long
            else:
                long_content_raw = generate_long_content(cid, lang, calc_name=ci18n["name"])"""

if old_content_block in gen_content:
    gen_content = gen_content.replace(old_content_block, new_content_block)
    GENERATOR.write_text(gen_content, encoding="utf-8")
    print("  Updated generate_calctowork.py to read long_content from calc JSON")
else:
    print("  WARN: Could not find content block in generator (may already be updated)")
    # Show nearby context
    idx = gen_content.find("long_content")
    if idx >= 0:
        print(f"  Found at position {idx}, surrounding text:")
        print(gen_content[max(0,idx-100):idx+200])

# ── Step 5: Update .gitignore ──
print("\n=== Step 5: Updating .gitignore ===")
gitignore = ROOT / ".gitignore"
content = gitignore.read_text(encoding="utf-8")
if "src/content/" not in content:
    with open(gitignore, "a", encoding="utf-8") as f:
        f.write("\nsrc/content/\n")
    print("  Added src/content/ to .gitignore")

print("\n=== Migration complete ===")
