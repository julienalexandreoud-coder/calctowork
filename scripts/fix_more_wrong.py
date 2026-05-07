"""Fix 401.html (FR/DE/IT/PT have TDEE instead of BMI Prime) and 410.html (template content)."""
import sys, time, re
from pathlib import Path
from bs4 import BeautifulSoup
import requests

d = Path(r'C:\Microsaas\obra\src\content')
SEP = ' |||BRK||| '

FILES_TO_FIX = [
    ('fr', '401.html'), ('de', '401.html'), ('it', '401.html'), ('pt', '401.html'),
    ('fr', '410.html'), ('de', '410.html'), ('it', '410.html'), ('pt', '410.html'),
]

def translate(text, source='en', target='es'):
    params = {'client': 'gtx', 'sl': source, 'tl': target, 'dt': 't', 'q': text}
    r = requests.get('https://translate.googleapis.com/translate_a/single', params=params, timeout=30)
    r.raise_for_status()
    return ''.join(item[0] for item in r.json()[0] if item[0])

for lang, fname in FILES_TO_FIX:
    en_f = d / 'en' / fname
    dest = d / lang / fname
    html = en_f.read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    texts = []
    for tag in soup.find_all(True):
        if tag.name in ('script','style','code','pre','a'): continue
        for c in list(tag.children):
            if c.name is None and isinstance(c, str):
                t = c.strip()
                if len(t) >= 10 and t[0] not in '<{[':
                    texts.append((tag, c, t))
    
    origs = [x[2] for x in texts]
    batches, cur, cur_len = [], [], 0
    for t in origs:
        add = len(SEP) if cur else 0
        if cur_len + add + len(t) > 3500 and cur:
            batches.append(cur); cur, cur_len = [t], len(t)
        else:
            cur.append(t); cur_len += add + len(t)
    if cur: batches.append(cur)
    
    translated = []
    for b in batches:
        result = translate(SEP.join(b), 'en', lang)
        parts = result.split(SEP)
        while len(parts) < len(b): parts.append('')
        translated.extend(parts[:len(b)])
        time.sleep(0.15)
    
    for (tag, child, _), new_t in zip(texts, translated):
        nt = new_t.strip()
        if nt: child.replace_with(nt)
    
    dest.write_text(str(soup), encoding='utf-8')
    print(f'Fixed {lang}/{fname}')

print('\nDone!')
