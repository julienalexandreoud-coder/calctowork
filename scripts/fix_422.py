import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Check remaining short titles
for lang in ['fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = [(cid, ci.get('seo_title', '')) for cid, ci in calcs.items() if len(ci.get('seo_title', '')) < 30]
    print(f'{lang}: {short}')