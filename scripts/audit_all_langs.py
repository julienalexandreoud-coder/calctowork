"""Check Spanish content files for mismatches."""
import json, glob, os, re
from difflib import SequenceMatcher

all_calcs = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    es = d.get('i18n', {}).get('es', {})
    name = es.get('name', '')
    if name:
        all_calcs[d['id']] = name.lower()

def best_match_id(text):
    for tag in ['h2', 'h1']:
        m = re.search(f'<{tag}[^>]*>(.*?)</{tag}>', text)
        if m:
            title = m.group(1).strip().lower()
            best_id, best_score = None, 0
            for cid, name in all_calcs.items():
                score = SequenceMatcher(None, title, name).ratio()
                tw = ' '.join(title.split()[:4])
                nw = ' '.join(name.split()[:4])
                ws = SequenceMatcher(None, tw, nw).ratio()
                score = max(score, ws)
                if score > best_score:
                    best_score = score
                    best_id = cid
            return best_id, best_score, title[:80]
    return None, 0, '(no title)'

langs = {}
for lang in ['es', 'fr', 'pt', 'de', 'it']:
    content_dir = f'src/content/{lang}'
    if not os.path.isdir(content_dir):
        continue
    ok = 0
    bad = 0
    notitle = 0
    for fp in sorted(glob.glob(f'{content_dir}/*.html')):
        file_id = os.path.splitext(os.path.basename(fp))[0]
        with open(fp, 'r', encoding='utf-8-sig') as f:
            text = f.read(5000)
        best_id, score, title = best_match_id(text)
        if best_id is None:
            notitle += 1
        elif best_id == file_id:
            ok += 1
        else:
            bad += 1
    langs[lang] = (ok, bad, notitle)
    total = ok + bad + notitle
    print(f'{lang}: {total} files -> {ok} OK, {bad} WRONG, {notitle} no-title ({bad/total*100:.0f}% bad)')

print(f'\nTotal across languages: {sum(v[0]+v[1]+v[2] for v in langs.values())}')
