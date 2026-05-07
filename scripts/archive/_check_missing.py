from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')
missing = ['402','403','200','201','203','210','500','501','700','800','802','600','900']

# Check each language for these files
for mid in missing:
    f_en = d / 'en' / f'{mid}.html'
    en_txt = BeautifulSoup(f_en.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True) if f_en.exists() else 0
    print(f'\n{mid}.html: EN={len(en_txt)} chars')
    
    for lang in ['es', 'fr', 'de', 'it', 'pt']:
        f = d / lang / f'{mid}.html'
        if f.exists():
            txt = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True)
            ratio = len(txt) / en_txt * 100 if en_txt > 0 else 0
            h2 = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').find('h2')
            h2_text = h2.get_text(strip=True)[:50] if h2 else 'N/A'
            status = 'REAL' if ratio > 40 else 'TEMPLATE'
            print(f'  {lang}: {len(txt)} chars ({ratio:.0f}%) [{status}] h2={h2_text}')
        else:
            print(f'  {lang}: MISSING')
