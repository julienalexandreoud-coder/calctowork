"""Sample German names/inputs/outputs from first 10 calculators."""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))[:10]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    print(f"--- {os.path.basename(f)} ---")
    print(f"  name: {de.get('name', 'N/A')}")
    print(f"  seo_title: {de.get('seo_title', 'N/A')}")
    inputs = de.get('inputs', {})
    print(f"  inputs: {dict(list(inputs.items())[:5])}")
    outputs = de.get('outputs', {})
    print(f"  outputs: {dict(list(outputs.items())[:5])}")
    print()
