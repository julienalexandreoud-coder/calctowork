from pathlib import Path
import json
i18n = json.load(open(r'C:\Microsaas\obra\src\i18n\en.json'))
for cid, data in i18n.get('calculators',{}).items():
    name = data.get('name','')
    if 'area' in name.lower() and 'converter' in name.lower():
        print(f'{cid}: {name}')
    if 'molecular' in name.lower():
        print(f'{cid}: {name} (HAS MOLECULAR!)')
