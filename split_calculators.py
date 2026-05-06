#!/usr/bin/env python3
"""Split monolithic calculators.json and i18n into individual files per calculator."""
import json
import os
import shutil

BASE = r"C:\Microsaas\obra"
SRC = os.path.join(BASE, "src")
CALCS_FILE = os.path.join(SRC, "calculators", "calculators.json")
I18N_DIR = os.path.join(SRC, "i18n")
OUTPUT_DIR = os.path.join(SRC, "calculators")
BACKUP_FILE = CALCS_FILE + ".monolithic_backup"

# 1. Load calculators
with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
calculators = data.get("calculators", data) if isinstance(data, dict) else data
print(f"Loaded {len(calculators)} calculators")

# 2. Load i18n per language
LANGUAGES = ["es", "en", "fr", "pt", "de", "it"]
i18n_data = {}
for lang in LANGUAGES:
    path = os.path.join(I18N_DIR, f"{lang}.json")
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    # Extract calculator entries
    if "calculators" in raw:
        i18n_data[lang] = raw["calculators"]
    else:
        i18n_data[lang] = {}
    print(f"  {lang}: {len(i18n_data[lang])} calculator entries loaded")

# 3. Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 4. For each calculator, create individual file
EXCLUDE_TOP_FIELDS = {"id", "slug", "block", "block_slug", "inputs", "outputs",
                       "formula", "related", "example_inputs", "example_label",
                       "range_hints", "result_context", 
                       "result_context_en", "result_context_fr", "result_context_pt",
                       "result_context_de", "result_context_it",
                       "formula_display", "steps", "mistakes",
                       "comparison_presets", "diagram", "standard", "trust_note",
                       "buying_units", "input_type_review", "i18n", "units",
                       "tableHeaders"}

for calc in calculators:
    calc_id = calc.get("id")
    slug = calc.get("slug", f"calc-{calc_id}")
    
    # Build individual file: top-level = calc definition, i18n = translations
    indiv = {}
    for key, value in calc.items():
        indiv[key] = value
    
    # Merge i18n from centralized files (for blocks 1-18 calcs)
    has_inline_i18n = "i18n" in calc and isinstance(calc.get("i18n"), dict)
    
    if not has_inline_i18n:
        # Create i18n structure from centralized files
        indiv["i18n"] = {}
        for lang in LANGUAGES:
            calc_i18n = i18n_data.get(lang, {}).get(calc_id, {})
            if calc_i18n and isinstance(calc_i18n, dict):
                indiv["i18n"][lang] = calc_i18n
    
    # Write file
    filename = f"{slug}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(indiv, f, ensure_ascii=False, indent=2)
    
    if (int(calc_id) if calc_id.isdigit() else 0) % 50 == 0:
        print(f"  ... wrote {calc_id} {slug}")

# 5. Backup the original monolithic file
shutil.copy2(CALCS_FILE, BACKUP_FILE)
print(f"\nBacked up to {BACKUP_FILE}")

# 6. Count output
count = len([f for f in os.listdir(OUTPUT_DIR) if f.endswith(".json") and f != "calculators.json"])
print(f"Created {count} individual calculator files in {OUTPUT_DIR}")
print("Done!")
