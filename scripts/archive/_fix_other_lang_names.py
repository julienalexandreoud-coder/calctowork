"""Fix non-English names: use English fallback where clearly wrong topic."""
import json, glob

fixed = 0
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    en_name = d.get('i18n',{}).get('en',{}).get('name','')
    if not en_name:
        continue
    
    en_words = set(w.lower() for w in en_name.replace('(',' ').replace(')',' ').replace('/',' ').split())
    changed = False
    
    for lang in ['fr','pt','de','it']:
        ld = d.get('i18n',{}).get(lang,{})
        if not ld or 'name' not in ld:
            continue
        old = ld['name']
        old_words = set(w.lower() for w in old.replace('(',' ').replace(')',' ').replace('/',' ').split())
        overlap = len(en_words & old_words)
        
        # No word overlap = completely different topic = wrong name
        if overlap < 1 and old and en_name != old:
            ld['name'] = en_name
            changed = True
    
    if changed:
        with open(fp,'w',encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write('\n')
        fixed += 1

print(f'Fixed {fixed} calculators')
