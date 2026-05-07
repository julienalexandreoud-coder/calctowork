import json
with open(r'C:\Microsaas\obra\src\i18n\en.json', encoding='utf-8') as f:
    i18n = json.load(f)
for cid, data in i18n.get('calculators',{}).items():
    name = data.get('name','')
    if 'area' in name.lower() and 'converter' in name.lower():
        print(f'{cid}: {name}')
    if 'molecular' in name.lower():
        print(f'{cid}: {name} (HAS MOLECULAR!)')
    if 'molecular' in data.get('seo_title','').lower():
        print(f'{cid} seo_title: {data["seo_title"]}')
