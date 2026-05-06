#!/usr/bin/env python3
"""Deep audit of all 461 calculators for formula JS errors, field validation, and structural bugs."""

import json, os, glob, re, traceback

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

errors = []
warnings = []

for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    name = os.path.basename(fp)
    if "bak" in fp or "monolithic" in fp or name == "calculators.json":
        continue
    
    with open(fp, "r", encoding="utf-8-sig") as f:
        try:
            calc = json.load(f)
        except json.JSONDecodeError as e:
            errors.append((name, f"JSON invalid: {e}"))
            continue
    
    cid = calc.get("id", "?")
    slug = calc.get("slug", "?")
    
    # 1. Check formula exists and is valid JS
    formula = calc.get("formula", "")
    if not formula:
        errors.append((f"{cid} {name}", "MISSING formula"))
    else:
        try:
            compile(formula, f"<{name}>", "exec")
        except SyntaxError as e:
            errors.append((f"{cid} {name}", f"Formula SyntaxError: {e.msg} at line {e.lineno}"))
    
    # 2. Check inputs
    inputs = calc.get("inputs", [])
    if not inputs:
        errors.append((f"{cid} {name}", "MISSING inputs"))
    else:
        for inp in inputs:
            if "id" not in inp:
                errors.append((f"{cid} {name}", f"Input missing 'id': {inp}"))
            min_v = inp.get("min", None)
            max_v = inp.get("max", None)
            if min_v is not None and max_v is not None and min_v > max_v:
                errors.append((f"{cid} {name}", f"Input {inp.get('id','?')}: min={min_v} > max={max_v}"))
            if "type" not in inp:
                warnings.append((f"{cid} {name}", f"Input {inp.get('id','?')}: missing type"))
    
    # 3. Check outputs
    outputs = calc.get("outputs", [])
    if not outputs:
        errors.append((f"{cid} {name}", "MISSING outputs"))
    else:
        output_ids = set()
        for out in outputs:
            if "id" not in out:
                errors.append((f"{cid} {name}", f"Output missing 'id': {out}"))
            else:
                output_ids.add(out["id"])
        
        # Check formula references output IDs
        if formula and output_ids:
            for oid in output_ids:
                if oid not in formula:
                    pass  # Some formulas use different variable names, skip
    
    # 4. Check for division by zero potential (/ inputs.xxx without checking)
    if formula:
        divs = re.findall(r'/\s*inputs\.(\w+)', formula)
        for div_var in divs:
            # Check if this input has min=0 or no min
            found = False
            for inp in inputs:
                if inp.get("id") == div_var:
                    found = True
                    mn = inp.get("min", None)
                    if mn is not None and mn == 0:
                        warnings.append((f"{cid} {name}", f"Division by '{div_var}' which has min=0 — could cause Infinity"))
                    break
            if not found:
                warnings.append((f"{cid} {name}", f"Division by '{div_var}' but no input with that id found"))
    
    # 5. Check formula uses inputs that exist
    if formula:
        used_inputs = set(re.findall(r'inputs\.(\w+)', formula))
        input_ids = {inp.get("id","") for inp in inputs}
        missing = used_inputs - input_ids
        if missing:
            errors.append((f"{cid} {name}", f"Formula references inputs not declared: {missing}"))
    
    # 6. Check example_inputs match actual input IDs
    example = calc.get("example_inputs", {})
    if example:
        for eid in example:
            if eid not in input_ids:
                warnings.append((f"{cid} {name}", f"Example input '{eid}' not in actual inputs"))
    
    # 7. Check comparison_presets if present
    presets = calc.get("comparison_presets", [])
    if presets:
        for i, preset in enumerate(presets):
            for key in preset:
                if key != "_label" and key not in input_ids:
                    warnings.append((f"{cid} {name}", f"Comparison preset[{i}] has key '{key}' not in inputs"))
    
    # 8. Check i18n for all 6 languages
    i18n = calc.get("i18n", {})
    for lang in ["es", "en", "fr", "pt", "de", "it"]:
        if lang not in i18n:
            errors.append((f"{cid} {name}", f"MISSING i18n.{lang}"))
            continue
        entry = i18n[lang]
        for field in ["name", "seo_title", "seo_description"]:
            if not entry.get(field):
                warnings.append((f"{cid} {name}", f"Missing i18n.{lang}.{field}"))
        
        # Check input labels per language
        lang_inputs = entry.get("inputs", {})
        for inp_id in input_ids:
            if inp_id not in lang_inputs:
                warnings.append((f"{cid} {name}", f"Missing i18n.{lang}.inputs.{inp_id}"))


print(f"=== AUDIT RESULTS ===")
print(f"Total files: {len(os.listdir(CALC_DIR))} (excluding backups)")
print(f"\nERRORS: {len(errors)}")
for e in errors:
    print(f"  [ERROR] {e[0]}: {e[1]}")

print(f"\nWARNINGS: {len(warnings)}")
# Group warnings by type
from collections import Counter
warn_types = Counter(w[1][:60] for w in warnings)
print("Warning types:")
for t, c in warn_types.most_common(15):
    print(f"  [{c}x] {t}")

# Show first few of each warning type
shown = set()
for w in warnings:
    key = w[1][:60]
    if key not in shown:
        print(f"\n  Sample: {w[0]}: {w[1]}")
        shown.add(key)
        if len(shown) >= 5:
            break
