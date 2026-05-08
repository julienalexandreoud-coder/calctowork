"""Check if ES content files match their EN counterparts."""
from pathlib import Path
import re

d = Path(r'C:\Microsaas\obra\src\content')

checks = ['001', '004', '015', '028', '043', '078', '087', '100', '200', '300', '400', '401', '500', '600', '700', '800', '804', '900', '951', '1008']

print('Comparing ES vs EN content first 300 chars:\n')
for cid in checks:
    en = d / 'en' / f'{cid}.html'
    es = d / 'es' / f'{cid}.html'
    if not en.exists() or not es.exists():
        continue
    
    en_t = re.sub(r'<[^>]+>', ' ', en.read_text(encoding='utf-8'))[:300]
    es_t = re.sub(r'<[^>]+>', ' ', es.read_text(encoding='utf-8'))[:300]
    
    # Check if ES is a translation of EN by looking for key domain terms
    en_terms = set(w.lower() for w in en_t.split() if len(w) > 4)
    es_terms = set(w.lower() for w in es_t.split() if len(w) > 4)
    common = en_terms & es_terms
    
    en_h2 = re.search(r'<h2>(.*?)</h2>', en.read_text(encoding='utf-8'))
    es_h2 = re.search(r'<h2>(.*?)</h2>', es.read_text(encoding='utf-8'))
    en_h2_t = en_h2.group(1).strip() if en_h2 else 'N/A'
    es_h2_t = es_h2.group(1).strip() if es_h2 else 'N/A'
    
    # Check if ES text contains English words (suggests translation issues)
    english_words = ['the', 'and', 'for', 'with', 'from', 'that', 'this', 'calculate', 'calculator', 'your', 'their', 'these']
    eng_in_es = [w for w in english_words if w in es_t.lower().split()]
    
    status = 'OK'
    notes = []
    if eng_in_es:
        status = 'ENGLISH IN ES'
        notes.append(f'EN words: {eng_in_es[:3]}')
    
    print(f'ID {cid}: [{status}]')
    print(f'  EN h2: {en_h2_t[:70]}')
    print(f'  ES h2: {es_h2_t[:70]}')
    if notes:
        for n in notes:
            print(f'  {n}')
    print()
