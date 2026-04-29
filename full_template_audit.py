"""Full audit: template vs unique content across ALL calculators"""
import json
import os
import re

calcs = json.loads(open('src/calculators/calculators.json', encoding='utf-8').read())['calculators']

template_phrases = [
    'the formula behind this calculation',
    'understanding how the result is derived',
    'this calculator is particularly useful',
    'ensure all values use a single consistent unit',
    'results are mathematically exact',
    'final accuracy depends on the precision',
    'enter your values:',
    'the calculator applies the standard formula',
]

i18n = {}
with open('src/i18n/en.json', encoding='utf-8') as f:
    for cid, data in json.load(f).get('calculators', {}).items():
        i18n[cid] = data.get('name', '')

unique_content = []
templated_content = []
mixed_content = []

for calc in calcs:
    cid = calc['id']
    name = i18n.get(cid, '')
    block = calc.get('block_slug', '?')
    
    f = f'src/content/en/{cid}.html'
    if not os.path.exists(f):
        continue
    
    content = open(f, encoding='utf-8').read()
    words = len(content.split())
    
    # Count template phrases
    template_count = sum(1 for phrase in template_phrases if phrase.lower() in content.lower())
    
    # Count specific numbers with units
    specific_nums = len(re.findall(r'\d+\.?\d*\s*(?:lbs?|kg|cm|inches?|mph|km/h|calories?|years?|months?)', content.lower()))
    
    # Has real examples?
    has_examples = bool(re.search(r'example.*?:.*?\d+', content.lower()))
    
    # Classify
    if template_count >= 4:
        templated_content.append({'id': cid, 'name': name, 'block': block, 'words': words, 'templates': template_count})
    elif specific_nums >= 10 and has_examples:
        unique_content.append({'id': cid, 'name': name, 'block': block, 'words': words, 'examples': specific_nums})
    else:
        mixed_content.append({'id': cid, 'name': name, 'block': block, 'words': words, 'templates': template_count})

print("=" * 70)
print("TEMPLATE vs UNIQUE CONTENT - FULL AUDIT")
print("=" * 70)
print(f"\nUNIQUE CONTENT (real examples, specific numbers): {len(unique_content)}")
print(f"MIXED (some template, some substance): {len(mixed_content)}")
print(f"TEMPLATED (generic filler phrases): {len(templated_content)}")
print(f"TOTAL WITH CONTENT: {len(unique_content) + len(mixed_content) + len(templated_content)}")

print("\n" + "=" * 70)
print("TEMPLATED CONTENT BY CATEGORY (needs rewrite)")
print("=" * 70)

blocks = {}
for c in templated_content:
    b = c['block']
    if b not in blocks:
        blocks[b] = []
    blocks[b].append(c)

total_templated = 0
for block, items in sorted(blocks.items(), key=lambda x: -len(x[1])):
    print(f"\n[{block.upper()}] - {len(items)} templated calculators")
    for c in items[:10]:
        print(f"  {c['id']}: {c['name'][:45]} ({c['words']}w, {c['templates']} template phrases)")
    if len(items) > 10:
        print(f"  ... and {len(items)-10} more")
    total_templated += len(items)

print(f"\n\nTOTAL TEMPLATED: {total_templated} calculators need complete rewrite")

print("\n" + "=" * 70)
print("SAMPLE OF UNIQUE CONTENT (for reference)")
print("=" * 70)
for c in unique_content[:10]:
    print(f"  {c['id']}: {c['name'][:45]} ({c['words']}w, {c.get('examples',0)} specific examples)")
