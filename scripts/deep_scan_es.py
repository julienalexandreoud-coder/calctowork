"""Practical deep scan of ES content for real issues."""
import json, re
from collections import Counter
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')

issues_by_type = {
    'too_short': [],
    'first_para_mismatch': [],
    'english_words': [],
    'duplicate_paras': [],
    'eng_link_text': [],
}

for cdir in sorted(d.iterdir(), key=lambda x: int(x.name) if x.name.isdigit() else 9999):
    if not cdir.is_dir(): continue
    cid = cdir.name
    ef = cdir / 'es.html'
    jf = cdir / 'es.json'
    cf = cdir / 'calc.json'
    if not ef.exists() or not jf.exists():
        continue
    
    with open(jf, encoding='utf-8') as f:
        try: calc_name = json.load(f).get('name','').lower()
        except: calc_name = ''
    
    content = ef.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Too short
    if len(text) < 500:
        issues_by_type['too_short'].append((cid, calc_name[:40], len(text)))
        continue
    
    # First para mismatch
    fp = re.search(r'<p>(.*?)</p>', content)
    if fp:
        fp_t = re.sub(r'<[^>]+>', '', fp.group(1)).lower()
        name_words = set(w for w in calc_name.split() if len(w) > 3 and w not in ('calculadora','para','una','del','las','los','con','por','que','como','entre','sobre','sin'))
        fp_words = set(w for w in fp_t.split() if len(w) > 3 and w not in ('calculadora','para','una','del','las','los','con','por','que','como','entre','sobre','sin'))
        common = name_words & fp_words
        if not common and name_words and fp_words:
            issues_by_type['first_para_mismatch'].append((cid, calc_name[:40], fp_t[:80]))
    
    # English words
    eng = [w for w in ['your','their','also','find','useful','may','calculate','calculator','the','and','for','with','from','that','this'] 
           if re.search(r'\b' + w + r'\b', text.lower())]
    # Filter: 'the','and','for','with','from' are common in mixed-language content, ignore unless in see-also
    real_eng = [w for w in eng if w in ('your','their','also','find','useful','may')]
    if real_eng:
        issues_by_type['english_words'].append((cid, calc_name[:40], real_eng))
    
    # Duplicate paragraphs
    paras = re.findall(r'<p>(.*?)</p>', content, re.DOTALL)
    pts = [re.sub(r'<[^>]+>', '', p).strip() for p in paras if len(p) > 50]
    dupes = [p for p,c in Counter(pts).items() if c > 1]
    if dupes:
        issues_by_type['duplicate_paras'].append((cid, calc_name[:40], len(dupes)))
    
    # English link text in see-also
    sa = re.search(r'<p class="see-also">(.*?)</p>', content, re.DOTALL)
    if sa:
        for m in re.finditer(r'>([^<]+)<', sa.group(1)):
            t = m.group(1).strip()
            if t and not any(c in t.lower() for c in 'áéíóúñ') and ' ' in t and t[0].isupper():
                if not any(w in t.lower() for w in ['calculadora','convertir','calcular','índice','máxima']):
                    issues_by_type['eng_link_text'].append((cid, t[:50]))
                    break

print('='*80)
for issue_type, items in issues_by_type.items():
    print(f'\n{issue_type.upper()}: {len(items)} files')
    if items:
        for item in items[:15]:
            print(f'  {item}')
        if len(items) > 15:
            print(f'  ... and {len(items)-15} more')

print('\n\nRECOMMENDED FIXES:')
for cid, cname, reason in issues_by_type['first_para_mismatch'][:10]:
    print(f'  ID {cid}: {cname} -> first paragraph topic wrong')
