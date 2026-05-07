"""Investigate wrong content in translated files."""
from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')
files = ['302.html', '951.html']

for fname in files:
    print(f'\n=== {fname} ===')
    
    # Check EN
    en_file = d / 'en' / fname
    en_txt = BeautifulSoup(en_file.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True)
    en_h1 = BeautifulSoup(en_file.read_text(encoding='utf-8'), 'html.parser').find('h1')
    en_h2 = BeautifulSoup(en_file.read_text(encoding='utf-8'), 'html.parser').find('h2')
    print(f'EN ({len(en_txt)} chars): h1="{en_h1.get_text(strip=True) if en_h1 else "N/A"}"')
    print(f'  First h2: "{en_h2.get_text(strip=True) if en_h2 else "N/A"}"')
    print(f'  First 200 chars: {en_txt[:200]}')
    
    for lang in ['fr', 'de', 'it', 'pt', 'es']:
        lf = d / lang / fname
        if lf.exists():
            txt = BeautifulSoup(lf.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True)
            h1 = BeautifulSoup(lf.read_text(encoding='utf-8'), 'html.parser').find('h1')
            h2 = BeautifulSoup(lf.read_text(encoding='utf-8'), 'html.parser').find('h2')
            ratio = len(txt) / len(en_txt) * 100
            h1_text = h1.get_text(strip=True) if h1 else "N/A"
            h2_text = h2.get_text(strip=True)[:80] if h2 else "N/A"
            match = 'OK' if (abs(ratio - 100) < 60) else 'WRONG CONTENT'
            print(f'  {lang} ({len(txt)} chars, {ratio:.0f}%): h1="{h1_text}"')
            print(f'    h2="{h2_text}" [{match}]')
