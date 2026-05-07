# -*- coding: utf-8 -*-
import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Check a few files for Spanish accent coverage
files_to_check = [
    "hormigon-masa", "aceleracion", "acometida-agua",
    "calorias-diarias", "interes-compuesto", "a1c-estimator"
]

print("=== SPANISH ACCENT CHECK ===")
for name in files_to_check:
    fp = os.path.join(CALC_DIR, f"{name}.json")
    if not os.path.exists(fp):
        print(f"  {name}: NOT FOUND")
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        c = json.load(f)
    es = c.get("i18n", {}).get("es", {})

    # Check if text has proper Spanish accents
    name_text = es.get("name", "")
    seo = es.get("seo_title", "")
    desc = es.get("seo_description", "")

    # Spanish words that MUST have accents
    needs_accent = {
        "calculo": "c\u00e1lculo",
        "Calculo": "C\u00e1lculo",
        "formula": "f\u00f3rmula",
        "Formula": "F\u00f3rmula",
        "automaticamente": "autom\u00e1ticamente",
        "Automaticamente": "Autom\u00e1ticamente",
        "optimo": "\u00f3ptimo",
        "Optimo": "\u00d3ptimo",
        "diametro": "di\u00e1metro",
        "Diametro": "Di\u00e1metro",
        "segun": "seg\u00fan",
        "Segun": "Seg\u00fan",
        "simultaneo": "simult\u00e1neo",
        "Simultaneo": "Simult\u00e1neo",
        "aceleracion": "aceleraci\u00f3n",
        "Aceleracion": "Aceleraci\u00f3n",
        "gratuita": "gratuita",  # already has accent
        "Gratuita": "Gratuita",
        "facil": "f\u00e1cil",
        "Facil": "F\u00e1cil",
        "gratis": "gratis",  # no accent
    }

    issues = []
    for wrong, correct in needs_accent.items():
        if wrong in name_text or wrong in seo or wrong in desc:
            issues.append(f"{wrong}->{correct}")

    if issues:
        print(f"  {name}: MISSING ACCENTS: {issues[:5]}")
    else:
        print(f"  {name}: OK")

    # Show actual text
    print(f"    name: {name_text}")
    print(f"    seo:  {seo}")
    print(f"    desc: {desc[:100]}")
    print()
