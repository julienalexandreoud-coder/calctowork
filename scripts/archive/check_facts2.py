import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.calc_content import CALC_FACTS

# Show the first few with 'uses' key to understand structure
for cid in ['940', '942', '944', '426', '428', '1000', '321', '320', '928', '916']:
    cf = CALC_FACTS.get(cid, {})
    en = cf.get('en', {})
    uses = en.get('u', []) if isinstance(en, dict) else []
    f = en.get('f', '') if isinstance(en, dict) else ''
    print(f'{cid}: f="{f[:80]}" uses={uses[:3]}')