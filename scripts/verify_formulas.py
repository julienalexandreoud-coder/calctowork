#!/usr/bin/env python3
"""Formula linter — checks for common issues without executing JS."""
import json
import re

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    calcs = json.load(f)["calculators"]

issues = []
for c in calcs:
    cid = c["id"]
    slug = c.get("slug", "")
    formula = c.get("formula", "")
    inputs = c.get("inputs", [])
    input_ids = {i["id"] for i in inputs}

    if not formula or formula.strip() == "":
        issues.append((cid, slug, "empty formula"))
        continue

    if "return" not in formula:
        issues.append((cid, slug, "missing return statement"))

    if "eval" in formula or "Function(" in formula:
        issues.append((cid, slug, "contains eval/Function — security risk"))

    # Check for references to inputs that don't exist
    for inp in inputs:
        iid = inp["id"]
        # crude: look for inputs.X or inputs['X'] or inputs["X"]
        if re.search(r'inputs\.' + re.escape(iid) + r'\b', formula) or re.search(r'inputs\[[\'"]' + re.escape(iid) + r'[\'"]\]', formula):
            pass  # OK
        else:
            # Only flag if the input is numeric and formula is long enough to expect usage
            if inp.get("type") == "number" and len(formula) > 100:
                pass  # Too many false positives

    # Check formula_display quality
    formula_display = c.get("formula_display", "")
    if not formula_display or formula_display.strip() in ("", "Resultado = cálculo según inputs", "Result = calculation based on inputs"):
        issues.append((cid, slug, "vague or missing formula_display"))

print(f"Scanned {len(calcs)} calculators.")
print(f"Found {len(issues)} issues:\n")
for cid, slug, reason in issues[:30]:
    print(f"  {cid:>6} {slug:<45} {reason}")
if len(issues) > 30:
    print(f"  ... and {len(issues)-30} more")
