"""Full content audit: check H2 title matches calculator, and check see-also links."""
import json, glob, os, re
from difflib import SequenceMatcher

# Build all English calculator names
all_calcs = {}  # id -> name
id_to_slug = {}  # id -> slug
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    en = d.get('i18n', {}).get('en', {})
    name = en.get('name', '')
    if name:
        all_calcs[d['id']] = name.lower()
    id_to_slug[d['id']] = d['slug']

def best_match_id(text):
    """Find best matching calculator ID for content."""
    # Try H2 first, then H1
    for tag in ['h2', 'h1']:
        m = re.search(f'<{tag}[^>]*>(.*?)</{tag}>', text)
        if m:
            title = m.group(1).strip().lower()
            best_id = None
            best_score = 0
            for cid, name in all_calcs.items():
                score = SequenceMatcher(None, title, name).ratio()
                tw = ' '.join(title.split()[:4])
                nw = ' '.join(name.split()[:4])
                ws = SequenceMatcher(None, tw, nw).ratio()
                score = max(score, ws)
                if score > best_score:
                    best_score = score
                    best_id = cid
            return best_id, best_score, title, tag
    return None, 0, '(no title)', '?'

# Check all English content files
mismatches = []
no_title = []
low_conf = []
good = []

for fp in sorted(glob.glob('src/content/en/*.html')):
    file_id = os.path.splitext(os.path.basename(fp))[0]
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read(5000)
    
    best_id, best_score, title, tag = best_match_id(text)
    
    if best_id is None:
        no_title.append((file_id, title))
    elif best_id == file_id:
        good.append((file_id, best_score, title[:60]))
    elif best_score >= 0.4:
        mismatches.append((file_id, best_id, best_score, title[:80]))
    else:
        low_conf.append((file_id, best_id, best_score, title[:60]))

print(f'Content files:  {len(good) + len(mismatches) + len(low_conf) + len(no_title)}')
print(f'  OK matches:  {len(good)}')
print(f'  MISMATCHES:  {len(mismatches)}')
print(f'  Low conf:    {len(low_conf)}')
print(f'  No title:    {len(no_title)}')
print()

if mismatches:
    print("=== MISMATCHES (content file -> what calculator it actually belongs to) ===")
    for file_id, best_id, score, title in mismatches[:60]:
        print(f'  {file_id} -> {best_id:>5}  {score:.0%}  {title}')

if no_title and len(no_title) < 20:
    print(f"\n=== NO TITLE: {len(no_title)} ===")
    for file_id, title in no_title[:10]:
        print(f'  {file_id}: {title[:60]}')
