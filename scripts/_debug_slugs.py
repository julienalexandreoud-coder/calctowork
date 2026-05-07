import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(r'C:\Microsaas\obra\scripts')))
from tools_config import TOOL_BY_ID

# Check structure
cid = '087'
if cid in TOOL_BY_ID:
    info = TOOL_BY_ID[cid]
    print(f'Keys for {cid}: {list(info.keys())}')
    if 'slug' in info:
        print(f'slug: {info["slug"]}')
    if 'en' in info.get('slug', {}):
        print(f'en slug: {info["slug"]["en"]}')
    if 'fr' in info.get('slug', {}):
        print(f'fr slug: {info["slug"]["fr"]}')
else:
    print(f'{cid} not in TOOL_BY_ID')
    
# Check a few more
for cid in ['078', '089', '099', '090']:
    if cid in TOOL_BY_ID:
        s = TOOL_BY_ID[cid].get('slug', {})
        print(f'{cid}: en={s.get("en","N/A")}, fr={s.get("fr","N/A")}')
    else:
        print(f'{cid}: NOT FOUND')
