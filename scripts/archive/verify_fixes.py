import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Microsaas\obra\src\i18n\en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

for cid in ['100', '1100', '1115', '929', '400', '944']:
    c = en['calculators'][cid]
    name = c.get('name', 'NONE')
    desc = c.get('desc', 'NONE') or 'NONE'
    seo = c.get('seo_desc', 'NONE') or 'NONE'
    label = c.get('example_label', 'NONE') or 'NONE'
    s = c.get('steps') or []
    m = c.get('mistakes') or []
    print(f'=== ID {cid}: {name} ===')
    print(f'  desc: {desc[:80]}')
    print(f'  seo_desc: {seo[:80]}')
    print(f'  label: {label[:80]}')
    print(f'  steps: {len(s)}, mistakes: {len(m)}')
    if s:
        print(f'    step0: {s[0][:70]}')
    if m:
        print(f'    mistake0: {m[0][:70]}')
    print()
