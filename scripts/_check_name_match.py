import json, glob, os
from difflib import SequenceMatcher

calcs = []
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = int(d['id'])
    slug = d['slug']
    es_name = d.get('i18n',{}).get('es',{}).get('name','')
    en_name = d.get('i18n',{}).get('en',{}).get('name','')
    calcs.append((cid, slug, es_name, en_name))

print(f'{"ID":>6} {"SLUG":<32} {"ES NAME (correct)":<45} {"EN NAME":<45} {"MATCH?"}')
print('='*140)

mismatches = 0
for cid, slug, es_name, en_name in sorted(calcs, key=lambda x: x[0]):
    es_words = set(es_name.lower().split())
    en_words = set(en_name.lower().split())
    common = es_words & en_words
    ratio = SequenceMatcher(None, es_name.lower(), en_name.lower()).ratio()
    
    # Check if names are about the same topic
    is_match = len(common) > 0 or ratio > 0.3
    
    if not is_match:
        mismatches += 1
        print(f'{cid:>6} {slug:<32} {es_name:<45} {en_name:<45} MISMATCH')
    elif cid <= 10 or (300 <= cid <= 310) or (500 <= cid <= 510) or (900 <= cid <= 910) or (1000 <= cid <= 1010) or (1100 <= cid <= 1110):
        status = 'OK' if ratio > 0.6 else 'WEAK'
        print(f'{cid:>6} {slug:<32} {es_name:<45} {en_name:<45} {status}')

print(f'\nTotal mismatches: {mismatches} / {len(calcs)}')
