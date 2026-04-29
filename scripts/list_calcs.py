import sys, json
sys.path.insert(0, r'C:\Microsaas\obra\scripts')
from tools_config import TOOLS

en_data = json.load(open(r'C:\Microsaas\obra\src\i18n\en.json', 'r', encoding='utf-8'))
calcs_data = json.load(open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8'))['calculators']

existing = {'001','008','300','301','302','304','305','400','401','410','412','422','426','928','936','938','940','942','953','1000'}

# Get names from en.json calculator translations
for c in calcs_data:
    cid = c['id']
    if cid not in existing:
        name_key = f"calc_{cid}_name"
        name = en_data.get(name_key, '?')
        print(f"{cid:>5}  {c['block_slug']:20s}  {name}")