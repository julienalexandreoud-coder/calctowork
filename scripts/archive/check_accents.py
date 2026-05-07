# -*- coding: utf-8 -*-
import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

missing = 0
total = 0
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    total += 1
    es = c.get("i18n", {}).get("es", {})
    name = es.get("name", "")
    seo = es.get("seo_title", "")

    # Check common Spanish words missing accents
    if "Calculo " in name or "calculo" in name.lower():
        missing += 1
        if missing <= 5:
            print(f"MISSING ACCENT: {name}")

print(f"\n{missing}/{total} files have missing Spanish accents in names")

# Sample some actual text
for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))[:5]:
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    es = c.get("i18n", {}).get("es", {})
    print(f'\n--- {os.path.basename(fp)} ---')
    print(f'  name: {es.get("name", "")}')
    print(f'  seo_title: {es.get("seo_title", "")}')
    print(f'  seo_description: {es.get("seo_description", "")[:100]}')
    steps = es.get("steps", [])
    if steps:
        print(f'  steps[0]: {steps[0][:100]}')
