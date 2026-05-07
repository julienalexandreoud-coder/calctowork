"""Comprehensive English content audit: flag ALL potential mismatches."""
import json, glob, os, re
from difflib import SequenceMatcher

calc_info = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    en = d.get('i18n', {}).get('en', {})
    name = en.get('name', '')
    desc = en.get('desc', '') or en.get('description', '')
    calc_info[d['id']] = {
        'name': name,
        'desc': desc,
        'slug': d['slug']
    }

# For each English content file, check if the content topic matches
flagged = []
for fp in sorted(glob.glob('src/content/en/*.html')):
    cid = os.path.splitext(os.path.basename(fp))[0]
    if cid not in calc_info:
        continue
    
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read(5000)
    
    # Extract content topic title
    h1m = re.search(r'<h1>(.*?)</h1>', text)
    h2m = re.search(r'<h2>(.*?)</h2>', text)
    title = (h1m.group(1) if h1m else '') or (h2m.group(1) if h2m else '')
    
    calc_name = calc_info[cid]['name']
    
    # Compare title to calculator name
    name_match = SequenceMatcher(None, title.lower(), calc_name.lower()).ratio()
    
    # Also check first paragraph for topic relevance
    pm = re.search(r'<p>(.*?)</p>', text)
    first_p = pm.group(1) if pm else ''
    first_p = re.sub(r'<[^>]+>', '', first_p)
    
    # Look for keyword match
    calc_words = set(re.findall(r'\b[a-z]{5,}\b', calc_name.lower() + ' ' + calc_info[cid]['desc'].lower()))
    content_words = set(re.findall(r'\b[a-z]{5,}\b', first_p.lower()))
    keyword_overlap = len(calc_words & content_words)
    keyword_total = len(calc_words)
    
    # Flag if name match is poor AND keyword overlap is low
    if name_match < 0.3 and keyword_overlap <= max(1, keyword_total * 0.15) and keyword_total > 0:
        flagged.append((cid, calc_name[:50], title[:60], f'{keyword_overlap}/{keyword_total} keywords'))

print(f'English content files: {len(list(glob.glob("src/content/en/*.html")))}')
print(f'Real calculators: {len(calc_info)}')
print(f'Flagged mismatches: {len(flagged)}')
print()
for cid, name, title, kw in flagged:
    print(f'  {cid:>5} | {name}')
    print(f'         | Content: {title}')
    print(f'         | {kw}')
    print()
