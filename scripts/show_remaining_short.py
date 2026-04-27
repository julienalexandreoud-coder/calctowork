import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

for lang in ['en', 'fr', 'pt', 'de', 'it']:
    data = json.load(open(os.path.join(I18N, f'{lang}.json'), 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = [(cid, ci.get('seo_title', '')) for cid, ci in calcs.items() if len(ci.get('seo_title', '')) < 30]
    if short:
        print(f'\n=== {lang} ({len(short)} short) ===')
        for cid, t in short:
            print(f'  {cid}: "{t}" ({len(t)}c)')