#!/usr/bin/env python3
"""Continue unfinished translations for IT and PT."""
import sys, time
from pathlib import Path
from bs4 import BeautifulSoup
import requests

d = Path(r'C:\Microsaas\obra\src\content')

def is_real(tr_file, en_text_len):
    """Check if target file has real (not template) content."""
    if not tr_file.exists():
        return False
    if en_text_len < 600:
        return True
    soup = BeautifulSoup(tr_file.read_text(encoding='utf-8'), 'html.parser')
    h2 = soup.find('h2')
    if h2 and h2.get_text(strip=True).startswith('Come funziona'):
        return False
    txt = len(soup.get_text(strip=True))
    return txt / en_text_len >= 0.4

for lang in ['it', 'pt']:
    td = d / lang
    td.mkdir(parents=True, exist_ok=True)
    ok = err = 0
    t0 = time.time()

    print(f'\n=== {lang.upper()} ===')
    for i, ef in enumerate(sorted((d / 'en').glob('*.html'))):
        tf = td / ef.name
        html = ef.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        en_txt = len(soup.get_text(strip=True))
        if is_real(tf, en_txt):
            continue
        if not soup.find('section', class_='long-content'):
            continue

        texts = []
        for tag in soup.find_all(True):
            if tag.name in ('script','style','code','pre','a'): continue
            for c in list(tag.children):
                if c.name is None and isinstance(c, str):
                    t = c.strip()
                    if len(t) >= 10 and t[0] not in '<{[':
                        texts.append((tag, c, t))
        if not texts:
            continue

        origs = [x[2] for x in texts]
        sep = ' |||BRK||| '
        batches, cur, cur_len = [], [], 0
        for t in origs:
            add = len(sep) if cur else 0
            if cur_len + add + len(t) > 3500 and cur:
                batches.append(cur)
                cur, cur_len = [t], len(t)
            else:
                cur.append(t)
                cur_len += add + len(t)
        if cur:
            batches.append(cur)

        translated = []
        try:
            for b in batches:
                params = {'client':'gtx','sl':'en','tl':lang,'dt':'t','q':sep.join(b)}
                r = requests.get('https://translate.googleapis.com/translate_a/single', params=params, timeout=30)
                result = ''.join(item[0] for item in r.json()[0] if item[0])
                parts = result.split(sep)
                while len(parts) < len(b):
                    parts.append('')
                translated.extend(parts[:len(b)])
                time.sleep(0.15)

            for (tag, child, _), new_t in zip(texts, translated):
                nt = new_t.strip()
                if nt:
                    child.replace_with(nt)

            tf.write_text(str(soup), encoding='utf-8')
            ok += 1
            if ok % 20 == 0:
                elapsed = time.time() - t0
                print(f'  {lang}: {ok} done ({ok/elapsed*60:.1f}/min)')

        except Exception as e:
            print(f'  ERR {ef.name}: {e}', file=sys.stderr)
            err += 1
            time.sleep(5)

    elapsed = time.time() - t0
    print(f'{lang}: {ok} done, {err} err in {elapsed:.0f}s')
