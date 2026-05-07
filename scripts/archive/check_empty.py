import json, glob, os
calc_dir = r"C:\Microsaas\obra\src\calculators"
empty_outs = 0
empty_inputs = 0
for f in sorted(glob.glob(os.path.join(calc_dir, "*.json"))):
    d = json.load(open(f, encoding='utf-8'))
    de = d.get('i18n', {}).get('de', {})
    if not de.get('outputs'):
        empty_outs += 1
        if empty_outs <= 3:
            print(f"  Empty outputs: {os.path.basename(f)}")
    if not de.get('inputs'):
        empty_inputs += 1
        if empty_inputs <= 3:
            print(f"  Empty inputs: {os.path.basename(f)}")
print(f"Empty outputs: {empty_outs}")
print(f"Empty inputs: {empty_inputs}")
