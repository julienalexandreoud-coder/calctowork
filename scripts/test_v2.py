import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from calc_content import build_article_v2, CALC_FACTS

# Test with a few different calculator categories
test_ids = ["001", "200", "300", "400", "700", "900"]
calcs = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))['calculators']
calc_lookup = {str(c['id']): c for c in calcs}

for cid in test_ids:
    if cid in CALC_FACTS:
        facts = CALC_FACTS[cid]
        calc_name = ""
        if cid in calc_lookup:
            calc_name_en = calc_lookup[cid]
            # get name from i18n
            en = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
            calc_name = en['calculators'].get(cid, {}).get('name', '')
        
        article = build_article_v2(cid, facts, 'en', calc_name=calc_name)
        word_count = len(article.split())
        print(f"\n=== ID {cid}: {calc_name} ===")
        print(f"Words: ~{word_count}, Chars: {len(article)}")
        # Show first 200 chars
        print(article[:200] + "...")
    else:
        print(f"\n=== ID {cid}: No CALC_FACTS ===")