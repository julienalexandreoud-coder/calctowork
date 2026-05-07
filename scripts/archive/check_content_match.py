"""Check if long-form content matches the correct calculator."""
import json, glob, os, re

calc_names = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    en = d.get('i18n', {}).get('en', {})
    calc_names[d['id']] = en.get('name', '') or en.get('seo_title', '')

mismatches = []
match_count = 0
no_h1 = 0

for fp in sorted(glob.glob('src/content/en/*.html')):
    cid = os.path.splitext(os.path.basename(fp))[0]
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read(3000)
    h1m = re.search(r'<h1>(.*?)</h1>', text)
    if not h1m:
        no_h1 += 1
        continue
    h1 = h1m.group(1)
    expected = calc_names.get(cid, '')
    if not expected:
        continue
    
    h1_words = set(w.lower() for w in re.findall(r'\w+', h1)[:4])
    exp_words = set(w.lower() for w in re.findall(r'\w+', expected)[:4])
    overlap = len(h1_words & exp_words)
    
    if overlap > 0:
        match_count += 1
    else:
        mismatches.append((cid, expected[:80], h1[:80]))

total = len(list(glob.glob('src/content/en/*.html')))
print(f'English content files: {total}')
print(f'Good matches: {match_count}')
print(f'No H1 found: {no_h1}')
print(f'MISMATCHES: {len(mismatches)}')
print()
for cid, expected, h1 in mismatches:
    print(f'  ID {cid}:')
    print(f'    Expected: {expected}')
    print(f'    Got H1:   {h1}')
