"""Re-translate all remaining template files across non-EN languages."""
import sys, time, re
from pathlib import Path
from bs4 import BeautifulSoup
import requests

d = Path(r'C:\Microsaas\obra\src\content')
SEP = ' |||BRK||| '

TEMPLATE_H2 = {
    'es': ['Cómo funciona el cálculo', 'Datos de entrada', 'Resultados'],
    'fr': ['Comment fonctionne le calcul', 'La formule', 'La formule financiere', 'Exemple de calcul'],
    'de': ['So funktioniert die Berechnung', 'Die Formel', 'Die finanzmathematische', 'Schritt-für-Schritt'],
    'it': ['Come funziona il calcolo', 'La formula', 'Esempio di calcolo'],
    'pt': ['Como funciona o cálculo', 'A formula', 'Exemplo de cálculo'],
}

def translate(text, target):
    params = {'client':'gtx','sl':'en','tl':target,'dt':'t','q':text}
    r = requests.get('https://translate.googleapis.com/translate_a/single', params=params, timeout=30)
    r.raise_for_status()
    return ''.join(item[0] for item in r.json()[0] if item[0])

total = 0
for lang, markers in TEMPLATE_H2.items():
    ld = d / lang
    if not ld.exists(): continue
    n = 0
    for f in sorted(ld.glob('*.html')):
        en_f = d / 'en' / f.name
        if not en_f.exists(): continue
        
        # Check if template
        s = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
        h2 = s.find('h2')
        if not h2: continue
        h2t = h2.get_text(strip=True)
        is_template = any(m.lower() in h2t.lower() for m in markers)
        if not is_template: continue
        
        # Translate
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
        if not texts: continue
        
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
        try:
            for b in batches:
                result = translate(SEP.join(b), lang)
                parts = result.split(SEP)
                while len(parts) < len(b): parts.append('')
                translated.extend(parts[:len(b)])
                time.sleep(0.15)
            for (tag, child, _), new_t in zip(texts, translated):
                nt = new_t.strip()
                if nt: child.replace_with(nt)
            f.write_text(str(soup), encoding='utf-8')
            n += 1
            if n % 20 == 0: print(f'  {lang}: {n} done')
        except Exception as e:
            print(f'  ERR {lang}/{f.name}: {e}')
            time.sleep(3)
    
    total += n
    print(f'{lang}: {n} files fixed')

print(f'\nTotal: {total} template files re-translated')
