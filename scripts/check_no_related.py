import json
data = json.load(open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'r', encoding='utf-8'))
calcs = data['calculators']

no_related = [c for c in calcs if not c.get('related')]
print(f'{len(no_related)} calculators without related links:')
for c in no_related[:20]:
    print(f"  {c['id']}: {c.get('slug','?')} (block={c.get('block')})")