import json

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

batch4 = [c for c in data['calculators'] if int(c['id']) >= 1050]

print('Batch 4 Tools (50 new calculators):')
print('=' * 60)
for c in batch4[:15]:
    slug = c['slug']
    block = c.get('block_slug', c.get('block', ''))
    cid = c['id']
    print(f"  ES: https://calctowork.web.app/es/{slug}/")
    print(f"  EN: https://calctowork.web.app/en/{slug}/")
    print(f"  Block: {block} | ID: {cid}")
    print()
print(f'... and {len(batch4) - 15} more')
