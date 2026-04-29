import json
import re
from pathlib import Path

# Load calculators
calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']

print("=== TESTING FORMULA EXECUTION ===")
errors = 0
success = 0

for calc in calcs[:50]:  # Test first 50
    cid = calc['id']
    formula = calc.get('formula', '')
    inputs = calc.get('inputs', [])
    example_inputs = calc.get('example_inputs', {})
    
    if not formula:
        print(f"[{cid}] No formula")
        errors += 1
        continue
    
    # Build test inputs from example or defaults
    test_inputs = {}
    for inp in inputs:
        iid = inp['id']
        if iid in example_inputs:
            test_inputs[iid] = example_inputs[iid]
        else:
            # Use default or a sensible value
            test_inputs[iid] = inp.get('default', 1)
    
    # Execute formula in a safe environment
    env = {"inputs": test_inputs, "Math": __import__('math')}
    try:
        exec(formula, env)
        if 'error' in env.get('result', {}):
            print(f"[{cid}] Formula returned error: {env['result']}")
            errors += 1
        else:
            success += 1
    except Exception as e:
        print(f"[{cid}] Formula execution error: {e}")
        errors += 1

print(f"\nSuccess: {success}, Errors: {errors}")
