#!/usr/bin/env python3
"""Remove broken German machine translations from calculator files.
The Spanish steps/mistakes are quality content — showing them on German pages
as-is is better than garbled machine translation."""
import json, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

fixed = 0
for filename in sorted(os.listdir(CALC_DIR)):
    if not filename.endswith(".json") or "backup" in filename or "monolithic" in filename:
        continue
    if filename == "calculators.json":
        continue
    
    filepath = os.path.join(CALC_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        calc = json.load(f)
    
    de_data = calc.get("i18n", {}).get("de", {})
    if not isinstance(de_data, dict):
        continue
    
    # Remove broken machine translations
    removed = False
    if "steps" in de_data and any("verwendern" in s.lower() or "vodern" in s.lower() for s in de_data["steps"]):
        del de_data["steps"]
        removed = True
    if "mistakes" in de_data and any("berücksichtigen loders" in m.lower() for m in de_data.get("mistakes", [])):
        del de_data["mistakes"]
        removed = True
    if "example_label" in de_data and any(w in str(de_data.get("example_label","")) for w in ["vodern", "loder", "todertal", "espedoderr"]):
        del de_data["example_label"]
        removed = True
    # Also remove if they're still mostly Spanish
    if "steps" in de_data:
        spanish_words = sum(1 for s in de_data["steps"] for w in [" para ", " del ", " de ", " las ", " los "])
        if spanish_words > 2:
            del de_data["steps"]
            removed = True
    
    if removed:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(calc, f, ensure_ascii=False, indent=2)
        fixed += 1

print(f"Cleaned {fixed} calculators — German pages will show original Spanish content for steps/mistakes")
