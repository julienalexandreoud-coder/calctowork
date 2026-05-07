import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.calc_content import CALC_FACTS

ids = list(CALC_FACTS.keys())[:10]
for cid in ids:
    cf = CALC_FACTS[cid]
    en = cf.get('en', {})
    if isinstance(en, dict):
        print(f'{cid}: {list(en.keys())[:10]}')
        for k in list(en.keys())[:5]:
            val = str(en[k])[:100]
            print(f'  {k}: {val}')
    else:
        print(f'{cid}: {str(en)[:100]}')