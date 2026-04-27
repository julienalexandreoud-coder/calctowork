import json
data = json.load(open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'r', encoding='utf-8'))
calcs = data['calculators']
has = sum(1 for c in calcs if c.get('related'))
total = len(calcs)
print(f'{has}/{total} calculators have related links')

# Show a sample with related
for c in calcs:
    if c.get('related'):
        print(f"  {c.get('id','?')}: related={c['related']}")
        break

# Show first calc id
print(f"  First calc id: {calcs[0]['id']}")
print(f"  Second calc id: {calcs[1]['id']}")