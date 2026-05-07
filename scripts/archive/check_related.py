import json
data = json.load(open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'r', encoding='utf-8'))
if isinstance(data, dict):
    calcs = data.values()
elif isinstance(data, list):
    calcs = data

has = sum(1 for c in calcs if c.get('related'))
total = len(list(calcs))
print(f'{has}/{total} calculators have related links')

# Show a sample with related
for c in (data.values() if isinstance(data, dict) else data):
    if c.get('related'):
        print(f"  {c.get('id','?')}: related={c['related']}")
        break