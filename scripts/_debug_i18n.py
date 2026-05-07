import json
i18n = json.load(open(r'C:\Microsaas\obra\src\i18n\en.json', encoding='utf-8'))
print('Keys:', list(i18n.keys()))
calcs = i18n.get('calculators', {})
print(f'Calculator count: {len(calcs)}')
if calcs:
    sample = list(calcs.keys())[0]
    print(f'Sample: {sample} -> {calcs[sample].get("name", "N/A")}')

# Check if "Liability Insurance Estimator" is in there
for cid, data in calcs.items():
    if 'liability' in data.get('name', '').lower():
        print(f'Found: {cid} -> {data["name"]}')

# Check name_to_id building
name_to_id = {}
for cid, data in calcs.items():
    name = data.get('name', '').lower().strip()
    if name:
        name_to_id[name] = cid

test_names = [
    "Liability Insurance Estimator",
    "Construction Signage Calculator",
    "Renovation Budget Calculator",
]

for n in test_names:
    found = name_to_id.get(n.lower().strip())
    print(f'"{n}" -> {found}')
