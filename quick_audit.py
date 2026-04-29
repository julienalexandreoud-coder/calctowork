"""Quick audit of calculator content"""
import json
import os

# Load all calculators
calcs = json.loads(open('src/calculators/calculators.json', encoding='utf-8').read())['calculators']

# Load i18n names  
i18n = {}
with open('src/i18n/en.json', encoding='utf-8') as f:
    for cid, data in json.load(f).get('calculators', {}).items():
        i18n[cid] = data.get('name', '')

print("CALCULATOR CONTENT AUDIT\n")

needs_content = []
has_content = []

for calc in calcs:
    cid = calc['id']
    name = i18n.get(cid, '')[:40]
    block = calc.get('block_slug', '?')
    
    src_file = f'src/content/en/{cid}.html'
    
    if os.path.exists(src_file):
        content = open(src_file, encoding='utf-8').read()
        words = len(content.split())
        
        has_faq = 'faq-item' in content.lower()
        has_example = 'Example' in content
        
        if words > 800 and has_faq and has_example:
            has_content.append((cid, name, block, words))
        else:
            needs_content.append((cid, name, block, words, 'thin'))
    else:
        needs_content.append((cid, name, block, 0, 'missing'))

print(f"HAS QUALITY CONTENT: {len(has_content)}")
print(f"NEEDS CONTENT: {len(needs_content)}")
print(f"TOTAL: {len(calcs)}\n")

# Group needs_content by block
blocks = {}
for item in needs_content:
    block = item[2]
    if block not in blocks:
        blocks[block] = []
    blocks[block].append(item)

print("=" * 70)
print("CALCULATORS NEEDING CONTENT (by block)")
print("=" * 70)

for block, items in sorted(blocks.items()):
    print(f"\n[{block.upper()}] - {len(items)} calculators")
    for cid, name, _, words, status in items:
        print(f"  {cid}: {name} ({status}, {words}w)")
