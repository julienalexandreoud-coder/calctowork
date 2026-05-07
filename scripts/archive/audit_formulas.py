#!/usr/bin/env python3
"""Real JS formula audit - check braces, parens, field validation."""

import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

errors = []
warnings = []

for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    name = os.path.basename(fp)
    if "bak" in fp or "monolithic" in fp or name == "calculators.json":
        continue

    with open(fp, "r", encoding="utf-8-sig") as f:
        calc = json.load(f)

    cid = calc.get("id", "?")
    formula = calc.get("formula", "")
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    input_ids = {i.get("id", "") for i in inputs}
    output_ids = {o.get("id", "") for o in outputs}

    # 1. Mismatched braces/parens
    if formula:
        opens = formula.count("{") - formula.count("}")
        if opens != 0:
            errors.append((f"{cid} {name}", f"Mismatched braces: {'+' if opens>0 else ''}{opens}"))
        parens = formula.count("(") - formula.count(")")
        if parens != 0:
            errors.append((f"{cid} {name}", f"Mismatched parens: {'+' if parens>0 else ''}{parens}"))

    # 2. Missing formula
    if not formula:
        errors.append((f"{cid} {name}", "MISSING formula"))

    # 3. Missing inputs/outputs
    if not inputs:
        errors.append((f"{cid} {name}", "MISSING inputs"))
    if not outputs:
        errors.append((f"{cid} {name}", "MISSING outputs"))

    # 4. Input min > max
    for i in inputs:
        mn = i.get("min")
        mx = i.get("max")
        if mn is not None and mx is not None and mn > mx:
            errors.append((f"{cid} {name}", f"Input '{i['id']}' min={mn} > max={mx}"))

    # 5. Formula uses undefined inputs
    if formula:
        import re
        used = set(re.findall(r'inputs\.(\w+)', formula))
        missing_inputs = used - input_ids
        if missing_inputs:
            errors.append((f"{cid} {name}", f"Formula uses undeclared inputs: {missing_inputs}"))

print(f"ERRORS: {len(errors)}")
for e in errors:
    print(f"  {e[0]}: {e[1]}")

print(f"\nWARNINGS: {len(warnings)}")
for w in warnings[:20]:
    print(f"  {w[0]}: {w[1]}")
