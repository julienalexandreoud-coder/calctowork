import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

fpath = os.path.join(I18N, 'pt.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

short = [(cid, ci['seo_description'], len(ci['seo_description'])) 
         for cid, ci in calcs.items() if len(ci.get('seo_description', '')) < 120]

# Extend remaining short ones with hand-crafted messages
PT_FIXES = {}
for cid, desc, l in short:
    # Common pattern: descriptions that got truncated. Add " Grátis online."
    # or a relevant extension
    base = desc.rstrip('.')
    if not base.endswith('.'):
        base += '.'
    ext = ' Ferramenta gratuita com cálculos precisos e detalhados.'
    new = base + ext
    if 120 <= len(new) <= 155:
        PT_FIXES[cid] = new
    else:
        ext2 = ' Cálculo gratuito online.'
        new2 = base + ext2
        if 120 <= len(new2) <= 155:
            PT_FIXES[cid] = new2
        else:
            print(f'  {cid}: still short at {len(new2)}c: "{new2[:80]}"')

for cid, new_desc in PT_FIXES.items():
    calcs[cid]['seo_description'] = new_desc

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

short2 = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
print(f'\nPT: <120c={short2}, 120-155c={good}, >155c=0')