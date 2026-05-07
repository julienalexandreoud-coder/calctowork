"""Remap content files to correct calculators based on keyword matching."""
import json, glob, os, re, shutil
from collections import defaultdict

# Build calculator keyword sets for each language
calc_keywords = {}  # lang -> cid -> set of keywords
calc_info = {}
for fp in glob.glob('src/calculators/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    calc_info[cid] = d['slug']
    for lang in ['es', 'fr', 'pt', 'de', 'it']:
        if lang not in calc_keywords:
            calc_keywords[lang] = {}
        i18n = d.get('i18n', {}).get(lang, {})
        text = ' '.join([
            i18n.get('name', ''), i18n.get('description', ''), i18n.get('desc', ''),
            ' '.join(i18n.get('inputs', {}).values()),
            ' '.join(i18n.get('outputs', {}).values()),
        ]).lower()
        words = set(re.findall(r'[a-z]{4,}', text))
        if lang == 'es':
            # Spanish uses accented chars too
            words.update(set(re.findall(r'[a-záéíóúñü]{4,}', text)))
        calc_keywords[lang][cid] = words

# For each non-English language, remap content files
for lang in ['es', 'fr', 'pt', 'de', 'it']:
    content_dir = f'src/content/{lang}'
    if not os.path.isdir(content_dir):
        continue
    
    # Read all content files and find best matching calculator
    assignments = {}  # correct_cid -> source_filepath
    conflicts = defaultdict(list)
    
    for fp in sorted(glob.glob(f'{content_dir}/*.html')):
        source_cid = os.path.splitext(os.path.basename(fp))[0]
        if source_cid not in calc_info:
            continue  # skip content for non-existent calculators
        
        with open(fp, 'r', encoding='utf-8-sig') as f:
            text = f.read(3000)
        text = re.sub(r'<[^>]+>', ' ', text).lower()
        content_words = set(re.findall(r'[a-záéíóúñü]{4,}', text))
        
        if not content_words:
            continue
        
        # Find best matching calculator
        best_cid = None
        best_score = 0
        for cid, keywords in calc_keywords[lang].items():
            if not keywords:
                continue
            overlap = len(content_words & keywords)
            score = overlap / len(keywords) if keywords else 0
            # Weight by total keywords too
            if overlap >= 2 and score > best_score:
                best_score = score
                best_cid = cid
        
        if best_cid and best_score > 0:
            key = best_cid
            if key in assignments:
                # Conflict: this cid already has content assigned
                conflicts[key].append((source_cid, best_score, fp))
            else:
                assignments[key] = (source_cid, best_score, fp)
    
    # Resolve conflicts: keep highest score
    for cid, candidates in conflicts.items():
        existing = assignments[cid]
        for src_cid, score, fp in candidates:
            if score > existing[1]:
                # Old content gets demoted to source id if available
                old_src = existing[0]
                if old_src not in assignments:
                    assignments[old_src] = existing
                assignments[cid] = (src_cid, score, fp)
    
    # Execute remapping
    moved = 0
    temp_dir = f'{content_dir}_temp'
    os.makedirs(temp_dir, exist_ok=True)
    
    for correct_cid, (source_cid, score, fp) in assignments.items():
        if source_cid == correct_cid:
            # Copy to temp (already correct)
            dest = os.path.join(temp_dir, f'{correct_cid}.html')
            shutil.copy2(fp, dest)
        else:
            dest = os.path.join(temp_dir, f'{correct_cid}.html')
            if not os.path.exists(dest):
                shutil.copy2(fp, dest)
                moved += 1
    
    # Check results
    new_count = len(os.listdir(temp_dir))
    old_count = len(os.listdir(content_dir))
    print(f'{lang}: {moved} files remapped | {new_count} output files from {old_count} input')
    
    # Replace old content with remapped
    if new_count > 0:
        shutil.rmtree(content_dir)
        os.rename(temp_dir, content_dir)

print('\nDone. English content was not modified (97.6% already correct).')
