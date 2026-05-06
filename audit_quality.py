#!/usr/bin/env python3
"""Audit calculator quality across all dimensions."""
import json, os, re
from pathlib import Path
from collections import Counter

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# Load all calculators
calcs = {}
for f in sorted(CALC_DIR.glob("*.json")):
    if f.name in ("calculators.json",) or "backup" in f.name or "monolithic" in f.name:
        continue
    try:
        with open(f, encoding="utf-8") as fh:
            calc = json.load(fh)
        calcs[calc["id"]] = calc
    except Exception as e:
        print(f"ERROR loading {f.name}: {e}")

print(f"Loaded {len(calcs)} calculators\n")

# ---- Audit dimensions ----

# 1. i18n completeness per language
i18n_present = {lang: 0 for lang in LANGS}
i18n_missing_name = {lang: 0 for lang in LANGS}
total = len(calcs)

for cid, calc in calcs.items():
    i18n = calc.get("i18n", {})
    for lang in LANGS:
        if lang in i18n and i18n[lang]:
            i18n_present[lang] += 1
            if not i18n[lang].get("name"):
                i18n_missing_name[lang] += 1

print("=== i18n COMPLETENESS ===")
for lang in LANGS:
    pct = i18n_present[lang] / total * 100
    missing = total - i18n_present[lang]
    no_name = i18n_missing_name[lang]
    print(f"  {lang}: {i18n_present[lang]}/{total} have i18n ({pct:.0f}%)  missing_names={no_name}  absent={missing}")

# 2. Language contamination detection
# Count calculators where German is actually French/Spanish
SPANISH_MARKERS = re.compile(r'\b(Calcula|Calcular|Calculadora|Resultado|según|medidas|Introduce|Valor)\b', re.IGNORECASE)
FRENCH_MARKERS = re.compile(r'\b(Calculez|Calculateur|Calcul)\b', re.IGNORECASE)
ENGLISH_MARKERS = re.compile(r'\b(Calculat(e|or))\b', re.IGNORECASE)
GERMAN_MARKERS = re.compile(r'\b(Berechnen|Rechner|Kostenlos|Geben|Wert|Ergebnis)\b', re.IGNORECASE)

lang_contamination = {lang: Counter() for lang in LANGS}
for cid, calc in calcs.items():
    i18n = calc.get("i18n", {})
    for lang in LANGS:
        if lang not in i18n or not i18n[lang]:
            continue
        name = i18n[lang].get("name", "")
        if lang != "es" and SPANISH_MARKERS.search(name):
            lang_contamination[lang]["spanish"] += 1
        if lang != "fr" and FRENCH_MARKERS.search(name):
            lang_contamination[lang]["french"] += 1
        if lang != "en" and ENGLISH_MARKERS.search(name):
            lang_contamination[lang]["english"] += 1
        if lang == "de" and not GERMAN_MARKERS.search(name) and name:
            lang_contamination[lang]["non_german_name"] += 1

print("\n=== LANGUAGE CONTAMINATION ===")
for lang in LANGS:
    cont = lang_contamination[lang]
    if cont:
        print(f"  {lang}: {dict(cont)}")

# 3. Content quality - templates
TEMPLATE_STEP = "Identificar los valores de entrada"
TEMPLATE_MISTAKE = "No verificar las medidas antes de calcular"
TEMPLATE_FORMULA = "Resultado = cálculo según inputs"

template_steps = 0
template_mistakes = 0
template_formula = 0
for cid, calc in calcs.items():
    steps = calc.get("steps", [])
    mistakes = calc.get("mistakes", [])
    fd = calc.get("formula_display", "")
    if steps and steps[0] == TEMPLATE_STEP:
        template_steps += 1
    if mistakes and mistakes[0] == TEMPLATE_MISTAKE:
        template_mistakes += 1
    if fd == TEMPLATE_FORMULA:
        template_formula += 1

print(f"\n=== TEMPLATE CONTENT ===")
print(f"  Template steps: {template_steps}/{total}")
print(f"  Template mistakes: {template_mistakes}/{total}")
print(f"  Template formula_display: {template_formula}/{total}")

# 4. SEO description quality
empty_seo = {lang: 0 for lang in LANGS}
duplicate_seo = {lang: 0 for lang in LANGS}
for cid, calc in calcs.items():
    i18n = calc.get("i18n", {})
    for lang in LANGS:
        if lang not in i18n or not i18n[lang]:
            empty_seo[lang] += 1  # counted as absent
            continue
        seo = i18n[lang].get("seo_description", i18n[lang].get("seo_desc", ""))
        if not seo or len(seo) < 10:
            empty_seo[lang] += 1
        # Check if seo_desc == seo_description (duplicate)
        if i18n[lang].get("seo_desc") and i18n[lang].get("seo_description"):
            if i18n[lang]["seo_desc"] == i18n[lang]["seo_description"]:
                duplicate_seo[lang] += 1

print(f"\n=== SEO DESCRIPTION ===")
for lang in LANGS:
    print(f"  {lang}: empty/short={empty_seo[lang]}  duplicate_seo_&_desc={duplicate_seo[lang]}")

# 5. Comparison presets quality
generic_presets = 0
no_presets = 0
for cid, calc in calcs.items():
    presets = calc.get("comparison_presets", [])
    if not presets:
        no_presets += 1
        continue
    labels = [p.get("_label", "") for p in presets]
    if any(l in ("Pequeño", "Mediano", "Grande", "Muy grande", "Extremo",
                 "Small scale", "Medium", "Large", "Industrial", "Theoretical",
                 "Caso basico", "Caso tipico", "Caso medio", "Caso avanzado", "Caso extremo")
           for l in labels):
        generic_presets += 1

print(f"\n=== COMPARISON PRESETS ===")
print(f"  Generic labels: {generic_presets}/{total}")
print(f"  Missing entirely: {no_presets}/{total}")

# 6. Range hints quality
generic_hints = 0
for cid, calc in calcs.items():
    hints = calc.get("range_hints", {})
    has_generic = any("Valor según especificaciones" in str(v) or 
                      "Introduce el valor de" in str(v) or
                      "Introduce la valeur" in str(v)
                      for v in hints.values())
    if has_generic or not hints:
        generic_hints += 1

print(f"\n=== RANGE HINTS ===")
print(f"  Generic or missing: {generic_hints}/{total}")

# 7. Block distribution
blocks = Counter()
for cid, calc in calcs.items():
    blocks[calc.get("block_slug", "unknown")] += 1

print(f"\n=== CALCULATOR DISTRIBUTION ===")
print(f"  Total blocks: {len(blocks)}")
print(f"  Total calcs: {total}")

# 8. Enrichment fields
has_standard = sum(1 for c in calcs.values() if c.get("standard"))
has_trust = sum(1 for c in calcs.values() if c.get("trust_note"))
has_diagram = sum(1 for c in calcs.values() if c.get("diagram"))
has_buying = sum(1 for c in calcs.values() if c.get("buying_units"))

print(f"\n=== ENRICHMENT FIELDS ===")
print(f"  standard: {has_standard}/{total}")
print(f"  trust_note: {has_trust}/{total}")
print(f"  diagram: {has_diagram}/{total}")
print(f"  buying_units: {has_buying}/{total}")

# 9. Input/Output label translation completeness
missing_input_labels = {lang: 0 for lang in LANGS}
missing_output_labels = {lang: 0 for lang in LANGS}
for cid, calc in calcs.items():
    i18n = calc.get("i18n", {})
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    input_ids = {inp["id"] for inp in inputs}
    output_ids = {out["id"] for out in outputs}
    
    for lang in LANGS:
        if lang not in i18n or not i18n[lang]:
            missing_input_labels[lang] += len(input_ids)
            missing_output_labels[lang] += len(output_ids)
            continue
        i18n_inputs = set(i18n[lang].get("inputs", {}).keys())
        i18n_outputs = set(i18n[lang].get("outputs", {}).keys())
        missing_input_labels[lang] += len(input_ids - i18n_inputs)
        missing_output_labels[lang] += len(output_ids - i18n_outputs)

print(f"\n=== INPUT/OUTPUT LABELS ===")
for lang in LANGS:
    print(f"  {lang}: missing_input_labels={missing_input_labels[lang]}  missing_output_labels={missing_output_labels[lang]}")

print("\n=== AUDIT COMPLETE ===")
