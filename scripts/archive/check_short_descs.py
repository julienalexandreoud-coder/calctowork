import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Check short ones
for lang in ['fr', 'pt']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = [(cid, ci.get('seo_description', ''), len(ci.get('seo_description', ''))) 
             for cid, ci in calcs.items() if len(ci.get('seo_description', '')) < 120]
    print(f'\n{lang}: {len(short)} short descriptions')
    for cid, desc, l in short[:10]:
        print(f'  {cid}: "{desc[:80]}..." ({l}c)')