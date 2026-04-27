import json

calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
blocks = {}
for c in calcs:
    bid = c.get('block', 'unknown')
    bslug = c.get('block_slug', 'unknown')
    if bid not in blocks:
        blocks[bid] = {'slug': bslug, 'count': 0, 'examples': []}
    blocks[bid]['count'] += 1
    if len(blocks[bid]['examples']) < 2:
        blocks[bid]['examples'].append(c.get('id', ''))

for k, v in sorted(blocks.items(), key=lambda x: str(x[0])):
    print(f'{k} ({v["slug"]}): {v["count"]} calcs - examples: {v["examples"]}')