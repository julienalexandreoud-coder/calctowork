"""Deep check: for each content file, find what calculator it ACTUALLY belongs to by comparing its H1/title to ALL calculator names."""
import json, glob, os, re
from difflib import SequenceMatcher

# Build all English calculator names
all_calcs = {}  # id -> name
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    en = d.get('i18n', {}).get('en', {})
    name = en.get('name', '')
    if name:
        all_calcs[d['id']] = name.lower()

def best_match(content_text):
    """Find best matching calculator name for this content's H1."""
    h1m = re.search(r'<h1[^>]*>(.*?)</h1>', content_text)
    if not h1m:
        return None, 0, None
    h1 = h1m.group(1).strip().lower()
    best_id = None
    best_score = 0
    for cid, name in all_calcs.items():
        score = SequenceMatcher(None, h1, name.lower()).ratio()
        # Also check first words
        h1w = ' '.join(h1.split()[:3])
        namew = ' '.join(name.lower().split()[:3])
        word_score = SequenceMatcher(None, h1w, namew).ratio()
        score = max(score, word_score)
        if score > best_score:
            best_score = score
            best_id = cid
    return best_id, best_score, h1

# Check all English content files
print(f"{'File ID':>6} {'Belongs To':>6} {'Score':>6} {'Expected':>6} {'Match?':>7} {'Content H1':.60}")
print("-" * 120)

issues = []
for fp in sorted(glob.glob('src/content/en/*.html')):
    file_id = os.path.splitext(os.path.basename(fp))[0]
    with open(fp, 'r', encoding='utf-8-sig') as f:
        text = f.read(5000)
    
    best_id, best_score, h1 = best_match(text)
    
    if best_id is None:
        issues.append((file_id, '?', 0, file_id, 'NO_H1', '(no h1 found)'))
        continue
    
    match_status = 'OK' if best_id == file_id else 'WRONG'
    if match_status == 'WRONG' and best_score > 0.5:
        issues.append((file_id, best_id, best_score, file_id, match_status, h1[:60]))
    elif match_status == 'OK' and best_score < 0.3:
        issues.append((file_id, best_id, best_score, file_id, 'LOW_CONF', h1[:60]))

mismatches = [i for i in issues if i[4] == 'WRONG']
low = [i for i in issues if i[4] == 'LOW_CONF']
noh1 = [i for i in issues if i[4] == 'NO_H1']

print(f'\nDEFINITE MISMATCHES: {len(mismatches)}')
for file_id, best_id, score, expected, status, h1 in mismatches[:40]:
    print(f'  {file_id:>6} -> {best_id:>6}  ({score:.0%})  H1: {h1}')

print(f'\nLOW CONFIDENCE (content may be too different): {len(low)}')
print(f'NO H1 FOUND: {len(noh1)}')
