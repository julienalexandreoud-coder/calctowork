"""Fix remaining BRK artifacts and check oversized files."""
import re
from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')

# Fix BRK artifacts
for lang, fname in [('es','064.html'),('fr','1000.html'),('fr','138.html'),('fr','601.html'),('pt','1084.html')]:
    f = d / lang / fname
    if f.exists():
        c = f.read_text(encoding='utf-8')
        c = re.sub(r'\s*\|\|\|BRK\|\|\|\s*', ' ', c)
        c = c.replace('|||BRK|||', '')
        f.write_text(c, encoding='utf-8')
        print(f'Fixed BRK in {lang}/{fname}')

# Check oversized files
for lang, fname in [('fr','401.html'),('fr','1101.html'),('it','401.html')]:
    f = d / lang / fname
    en_f = d / 'en' / fname
    if f.exists() and en_f.exists():
        en_t = len(BeautifulSoup(en_f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
        tr_t = len(BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
        print(f'{lang}/{fname}: EN={en_t}, LANG={tr_t}, ratio={tr_t/en_t:.0%}')
        # Check for duplicated content
        tr_text = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').get_text()
        if tr_text.count('.') > en_t / 100:
            print(f'  Possible duplication detected')
