from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')

for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
    ld = d / lang
    if not ld.exists():
        print(f'{lang}: MISSING')
        continue
    
    total = len(list(ld.glob('*.html')))
    template = 0
    missing = 0
    ref_lang = 'en'
    
    for ef in sorted((d / ref_lang).glob('*.html')):
        tf = ld / ef.name
        if not tf.exists():
            missing += 1
            continue
        en_txt = len(BeautifulSoup(ef.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
        if en_txt > 600:
            tr_txt = len(BeautifulSoup(tf.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
            if tr_txt / en_txt < 0.4:
                template += 1
    
    real = total - template - missing
    print(f'{lang}: {total} files, {real} real content, {template} template, {missing} missing')
