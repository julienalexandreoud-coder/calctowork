"""Proper content audit: check content-calculator topic match via keywords."""
import json, glob, os, re

# Get all real calculator IDs and their key terms
calc_info = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    en = d.get('i18n', {}).get('en', {})
    es = d.get('i18n', {}).get('es', {})
    desc = ' '.join([
        en.get('name', ''), en.get('description', ''), en.get('desc', ''),
        ' '.join(en.get('inputs', {}).values()),
        ' '.join(en.get('outputs', {}).values()),
    ]).lower()
    calc_info[d['id']] = {
        'slug': d['slug'],
        'name': en.get('name', ''),
        'keywords': set(re.findall(r'[a-z]{4,}', desc))
    }

# Check each language's content
print(f'Real calculators: {len(calc_info)}')
print()

for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    content_dir = f'src/content/{lang}'
    if not os.path.isdir(content_dir):
        continue
    
    exists_ok = 0      # content file for real calculator, match looks good
    exists_bad = 0     # content file for real calculator, but topic mismatch
    no_calc = 0        # content file for non-existent calculator
    missing_content = 0  # real calculator has no content file
    
    content_ids = set()
    for fp in sorted(glob.glob(f'{content_dir}/*.html')):
        cid = os.path.splitext(os.path.basename(fp))[0]
        content_ids.add(cid)
        
        if cid not in calc_info:
            no_calc += 1
            continue
        
        # Read content and extract key terms from first 2000 chars
        with open(fp, 'r', encoding='utf-8-sig') as f:
            text = f.read(2000)
        # Remove HTML
        text = re.sub(r'<[^>]+>', ' ', text)
        content_words = set(re.findall(r'[a-z]{4,}', text.lower()))
        
        # Compare keyword overlap
        target = calc_info[cid]['keywords']
        overlap = len(content_words & target)
        total = len(target)
        
        if total > 0 and overlap >= max(1, total * 0.1):
            exists_ok += 1
        elif total > 0:
            exists_bad += 1
            if exists_bad <= 5:
                print(f'  BAD {lang}/{cid} ({calc_info[cid]["name"]}): overlap {overlap}/{total} keywords')
        else:
            exists_ok += 1  # no keywords to compare
    
    missing_content = len(calc_info) - len(content_ids & set(calc_info.keys()))
    
    total = exists_ok + exists_bad + no_calc
    print(f'{lang}: {total} files | OK:{exists_ok} BAD:{exists_bad} NO_CALC:{no_calc} | Missing content for {missing_content} calcs')
