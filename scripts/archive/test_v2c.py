import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from calc_content import build_article_v2, CALC_FACTS

calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
calc_lookup = {str(c['id']): c for c in calcs}
en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))

categories = {}
for cid, facts in CALC_FACTS.items():
    block = calc_lookup.get(cid, {}).get('block', 0)
    block_str = str(block)
    if block_str not in categories:
        categories[block_str] = cid

from calc_content import BLOCK_CATEGORY

for block_str in sorted(categories.keys()):
    cid = categories[block_str]
    facts = CALC_FACTS[cid]
    calc_name = en['calculators'].get(cid, {}).get('name', '')
    article = build_article_v2(cid, facts, 'en', calc_name=calc_name)
    word_count = len(article.split())
    cat = BLOCK_CATEGORY.get(int(block_str) if block_str.isdigit() else block_str, "unknown")
    first_h2 = article.split('</h2>')[0].split('<h2>')[-1] if '<h2>' in article else "N/A"
    print(f"Block {block_str} (cat={cat}) id={cid}: {calc_name[:30]} | {word_count} words | H2: {first_h2}")