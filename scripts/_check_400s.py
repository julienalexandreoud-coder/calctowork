"""Check all languages for 400 and 401 content mismatch."""
from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')

# Check all 400-level files for mismatch
check_files = ['400.html','401.html','402.html','403.html','410.html','411.html']
for fname in check_files:
    en_f = d / 'en' / fname
    if not en_f.exists(): continue
    en_t = len(BeautifulSoup(en_f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
    en_h2 = BeautifulSoup(en_f.read_text(encoding='utf-8'), 'html.parser').find('h2')
    en_h2_t = en_h2.get_text(strip=True)[:60] if en_h2 else 'N/A'
    
    print(f'\n{fname}: EN={en_t}chars h2="{en_h2_t}"')
    for lang in ['es','fr','de','it','pt']:
        f = d / lang / fname
        if f.exists():
            s = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
            txt = s.get_text(strip=True)
            h2 = s.find('h2')
            ratio = len(txt) / en_t * 100
            h2_t = h2.get_text(strip=True)[:60] if h2 else 'N/A'
            match = 'OK' if abs(ratio-100) < 60 else 'MISMATCH'
            print(f'  {lang}: {len(txt)}chars ({ratio:.0f}%) h2="{h2_t}" [{match}]')
