#!/usr/bin/env python3
"""Final deep audit - simulate each calculator formula with default inputs."""

import json, os, glob
import subprocess, sys

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

# Use Node.js to eval JS formulas safely
NODE = r"C:\Program Files\nodejs\node.exe"

errors = []

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
    example = calc.get("example_inputs", {})
    
    if not formula or not inputs or not outputs:
        continue

    # Build test input values from example_inputs or defaults
    input_vals = {}
    for i in inputs:
        iid = i.get("id", "")
        if iid in example:
            input_vals[iid] = str(example[iid])
        elif "default" in i:
            input_vals[iid] = str(i["default"])

    if not input_vals:
        continue

    # Build Node.js test script
    js_inputs = json.dumps(input_vals)
    js_code = f"""
const inputs = {js_inputs};
const formula = `{formula}`;
try {{
    const result = (function() {{
        const fn = new Function('inputs', formula);
        return fn(inputs);
    }})();
    const out = JSON.stringify(result || {{}});
    console.log(out);
}} catch(e) {{
    console.log('ERROR:' + e.message);
}}
"""

    try:
        result = subprocess.run(
            [NODE, "-e", js_code],
            capture_output=True, text=True, timeout=10,
            cwd=CALC_DIR,
        )
        output = result.stdout.strip()
        stderr = result.stderr.strip()
        
        if stderr:
            errors.append((f"{cid} {name}", f"Node stderr: {stderr[:120]}"))
            continue
        
        if output.startswith("ERROR:"):
            errors.append((f"{cid} {name}", f"Runtime: {output}"))
            continue
        
        if not output:
            errors.append((f"{cid} {name}", "Empty output - formula returned nothing"))
            continue
        
        # Parse result
        result_obj = json.loads(output)
        
        if "error" in result_obj and result_obj.get("error"):
            errors.append((f"{cid} {name}", f"Formula returned error object"))
            continue
        
        # Check result has reasonable values
        output_ids = {o.get("id","") for o in outputs}
        for oid in output_ids:
            if oid in result_obj:
                val = result_obj[oid]
                if val is None:
                    errors.append((f"{cid} {name}", f"Output '{oid}' is None"))
                elif isinstance(val, (int, float)):
                    import math
                    if math.isnan(val):
                        errors.append((f"{cid} {name}", f"Output '{oid}' is NaN"))
                    elif math.isinf(val):
                        errors.append((f"{cid} {name}", f"Output '{oid}' is Infinity"))

    except subprocess.TimeoutExpired:
        errors.append((f"{cid} {name}", "TIMEOUT - formula hung"))
    except Exception as e:
        errors.append((f"{cid} {name}", f"Python error: {e}"))
        break


print(f"=== FORMULA RUNTIME CHECK ===")
print(f"Total tested: {len(os.listdir(CALC_DIR))}")
print(f"Errors: {len(errors)}")
for e in errors:
    print(f"  [FAIL] {e[0]}: {e[1]}")

if not errors:
    print("\nALL FORMULAS VALID - no runtime errors!")
