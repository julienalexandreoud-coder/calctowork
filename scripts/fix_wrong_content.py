"""Fix specific files that have wrong content (pre-existing mismatched translations)."""
import sys, time, re
from pathlib import Path
from bs4 import BeautifulSoup
import requests

CONTENT_DIR = Path(r'C:\Microsaas\obra\src\content')
SEP = ' |||BRK||| '
MAX_CHUNK = 3500

# Specific files to fix: (target_lang, filename)
FILES_TO_FIX = [
    ('fr', '302.html'),   # FR 302 is Compound Interest instead of Project Planning
    ('fr', '951.html'),   # FR 951 is Unit Conversion instead of 1RM
    ('de', '951.html'),   # DE 951 is Unit Conversion
    ('pt', '951.html'),   # PT 951 is Unit Conversion
    ('es', '951.html'),   # ES 951 only has 53% content
]

def translate(text, source='en', target='es'):
    params = {'client': 'gtx', 'sl': source, 'tl': target, 'dt': 't', 'q': text}
    r = requests.get('https://translate.googleapis.com/translate_a/single', params=params, timeout=30)
    r.raise_for_status()
    return ''.join(item[0] for item in r.json()[0] if item[0])

def translate_file(en_file, target_lang, dest_file):
    html = en_file.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    if not soup.find('section', class_='long-content'):
        return False
    
    texts = []
    for tag in soup.find_all(True):
        if tag.name in ('script','style','code','pre','a'):
            continue
        for c in list(tag.children):
            if c.name is None and isinstance(c, str):
                t = c.strip()
                if len(t) >= 10 and t[0] not in '<{[':
                    texts.append((tag, c, t))
    
    if not texts:
        return False
    
    origs = [x[2] for x in texts]
    batches = []
    cur, cur_len = [], 0
    for t in origs:
        add = len(SEP) if cur else 0
        if cur_len + add + len(t) > MAX_CHUNK and cur:
            batches.append(cur)
            cur, cur_len = [t], len(t)
        else:
            cur.append(t)
            cur_len += add + len(t)
    if cur:
        batches.append(cur)
    
    translated = []
    for b in batches:
        result = translate(SEP.join(b), 'en', target_lang)
        parts = result.split(SEP)
        while len(parts) < len(b):
            parts.append('')
        translated.extend(parts[:len(b)])
        time.sleep(0.15)
    
    for (tag, child, _), new_t in zip(texts, translated):
        nt = new_t.strip()
        if nt:
            child.replace_with(nt)
    
    dest_file.write_text(str(soup), encoding='utf-8')
    return True

print('Fixing specific files with wrong content...')
ok = 0
for lang, fname in FILES_TO_FIX:
    en_file = CONTENT_DIR / 'en' / fname
    dest_file = CONTENT_DIR / lang / fname
    try:
        translate_file(en_file, lang, dest_file)
        ok += 1
        print(f'  Fixed {lang}/{fname}')
    except Exception as e:
        print(f'  ERR {lang}/{fname}: {e}')

print(f'\nFixed {ok}/{len(FILES_TO_FIX)} files')

# Verify the fixes
print('\nVerification:')
verify = [
    ('fr', '302.html', 'Projet'),
    ('fr', '951.html', 'Répétition'),
    ('de', '951.html', 'Wiederholung'),
    ('pt', '951.html', 'Repetição'),
    ('es', '951.html', 'Repetición'),
]
for lang, fname, keyword in verify:
    content = (CONTENT_DIR / lang / fname).read_text(encoding='utf-8')
    has_keyword = keyword.lower() in content.lower()
    print(f'  {lang}/{fname}: {"OK" if has_keyword else "STILL WRONG"} (checked for "{keyword}")')
