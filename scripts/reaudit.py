"""Quick re-audit to check remaining issues."""
import re
from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')
LANGS = ['en','es','fr','de','it','pt']

# Check remaining English headers
HEADERS = ['Pro Tip','Pro Tips','FAQs','Frequently Asked Questions','Related Calculators','Related Calculator','Real-World Examples','Real-World Example','Common Mistakes to Avoid','Common Mistakes']
for lang in LANGS:
    ld = d / lang
    remaining = 0
    for f in ld.glob('*.html'):
        c = f.read_text(encoding='utf-8')
        for h in HEADERS:
            if re.search(rf'<h[1-6]>{re.escape(h)}</h[1-6]>', c):
                remaining += 1
                break
    print(f'{lang}: {remaining} files with English headers')

# Check BRK artifacts
print()
for lang in LANGS:
    ld = d / lang
    count = 0
    for f in ld.glob('*.html'):
        c = f.read_text(encoding='utf-8')
        if 'BRK' in c:
            count += 1
            if count <= 3:
                print(f'  BRK in {lang}/{f.name}')
    print(f'{lang}: {count} files with BRK artifacts')

# Check for %0/0 content ratio (potential corruption)
print()
for lang in ['es','fr','de','it','pt']:
    ld = d / lang
    issues = 0
    for f in ld.glob('*.html'):
        en_f = d / 'en' / f.name
        if not en_f.exists(): continue
        en_t = len(BeautifulSoup(en_f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
        if en_t < 500: continue
        tr_t = len(BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
        ratio = tr_t / en_t
        if ratio < 0.3 or ratio > 2.5:
            issues += 1
            if issues <= 5:
                print(f'  RATIO {lang}/{f.name}: {ratio:.0%}')
    print(f'{lang}: {issues} files with bad content ratio')
