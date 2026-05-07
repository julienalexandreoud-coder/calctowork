from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')
missing = ['402','403','200','201','203','210','500','501','700','800','802','600','900']

for mid in missing:
    f_en = d / 'en' / f'{mid}.html'
    en_txt = len(BeautifulSoup(f_en.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
    print(f'{mid}.html: EN={en_txt} chars')
    
    for lang in ['es', 'fr', 'de', 'it', 'pt']:
        f = d / lang / f'{mid}.html'
        if f.exists():
            txt = len(BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
            ratio = txt / en_txt * 100
            status = 'REAL' if ratio > 40 else 'TEMPLATE'
            print(f'  {lang}: {txt} chars ({ratio:.0f}%) [{status}]')
        else:
            print(f'  {lang}: MISSING')
