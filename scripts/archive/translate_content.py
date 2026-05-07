#!/usr/bin/env python3
"""Translate EN HTML content to FR, DE, IT, PT via Google Translate API."""
import sys, time, re
from pathlib import Path
from bs4 import BeautifulSoup
import requests

CONTENT_DIR = Path(r'C:\Microsaas\obra\src\content')
EN_DIR = CONTENT_DIR / 'en'
SEP = ' |||BRK||| '
MAX_CHUNK = 3500

def translate(text, source='en', target='fr'):
    params = {'client': 'gtx', 'sl': source, 'tl': target, 'dt': 't', 'q': text}
    r = requests.get('https://translate.googleapis.com/translate_a/single', params=params, timeout=30)
    r.raise_for_status()
    return ''.join(item[0] for item in r.json()[0] if item[0])

def get_texts(soup):
    result = []
    for tag in soup.find_all(True):
        if tag.name in ('script','style','code','pre','a'):
            continue
        for c in list(tag.children):
            if c.name is None and isinstance(c, str):
                t = c.strip()
                if len(t) >= 10 and t[0] not in '<{[':
                    result.append((tag, c, t))
    return result

def needs_xlate(tr_file, en_len):
    if not tr_file.exists():
        return True
    if en_len < 600:
        return False
    tr = BeautifulSoup(tr_file.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True)
    return len(tr) / en_len < 0.4

def run():
    files = sorted(EN_DIR.glob('*.html'))
    print(f'Total: {len(files)} EN files')

    for lang in ['fr','de','it','pt']:
        td = CONTENT_DIR / lang
        td.mkdir(parents=True, exist_ok=True)
        ok = sk = err = 0
        t0 = time.time()

        print(f'\n=== {lang.upper()} ===')
        for i, ef in enumerate(files):
            tf = td / ef.name
            html = ef.read_text(encoding='utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            en_len = len(soup.get_text(strip=True))
            if not needs_xlate(tf, en_len):
                continue
            if not soup.find('section', class_='long-content'):
                sk += 1
                continue

            tx = get_texts(soup)
            if not tx:
                sk += 1
                continue

            origs = [x[2] for x in tx]
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

            try:
                translated = []
                for b in batches:
                    result = translate(SEP.join(b), 'en', lang)
                    parts = result.split(SEP)
                    # Handle cases where split count doesn't match
                    while len(parts) < len(b):
                        parts.append('')
                    translated.extend(parts[:len(b)])
                    time.sleep(0.15)

                for (tag, child, _), new_t in zip(tx, translated):
                    nt = new_t.strip()
                    if nt:
                        child.replace_with(nt)

                tf.write_text(str(soup), encoding='utf-8')
                ok += 1
                elapsed = time.time() - t0
                print(f'  [{i+1}/{len(files)}] {ef.name} ({elapsed:.0f}s, {ok/elapsed*60:.1f}/min)')

            except Exception as e:
                print(f'  ERR {ef.name}: {e}', file=sys.stderr)
                err += 1
                time.sleep(2)

        e = time.time() - t0
        print(f'\n{lang}: {ok} ok, {sk} skip, {err} err in {e:.0f}s')

if __name__ == '__main__':
    run()
