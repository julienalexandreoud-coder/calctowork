import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

for lang in ['en', 'de', 'it']:
    data = json.load(open(os.path.join(I18N, f'{lang}.json'), 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = [(cid, ci.get('seo_title', '')) for cid, ci in calcs.items() if len(ci.get('seo_title', '')) < 30]
    print(f'\n=== {lang} SHORT TITLES ({len(short)}) ===')
    for cid, t in sorted(short, key=lambda x: len(x[1]))[:30]:
        print(f'  {cid}: "{t}" ({len(t)}c)')