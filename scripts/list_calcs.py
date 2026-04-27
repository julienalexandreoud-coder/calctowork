import json
d = json.load(open('src/i18n/en.json', 'r', encoding='utf-8'))
calcs = d['calculators']
for k in sorted(calcs):
    if k.startswith(('105', '106', '107', '108', '109')):
        print(f"{k}: {calcs[k]['name']}")