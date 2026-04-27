import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from calc_content import build_article_v2, CALC_FACTS

calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
calc_lookup = {str(c['id']): c for c in calcs}
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))

# Get a sample from different categories
categories = {}
for cid, facts in CALC_FACTS.items():
    block = calc_lookup.get(cid, {}).get('block', 0)
    if block not in categories:
        categories[block] = cid

print(f"Total CALC_FACTS: {len(CALC_FACTS)}")
print(f"Categories sampled: {categories}")

for block, cid in sorted(categories.items()):
    facts = CALC_FACTS[cid]
    calc_name = en['calculators'].get(cid, {}).get('name', '')
    article = build_article_v2(cid, facts, 'en', calc_name=calc_name)
    word_count = len(article.split())
    print(f"\nBlock {block} (id={cid}): {calc_name}")
    print(f"  Words: ~{word_count}")
    print(f"  First H2: {article.split('</h2>')[0].split('<h2>')[-1]}")