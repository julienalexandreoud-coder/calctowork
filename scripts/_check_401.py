"""Check 401.html across all languages for content mismatch."""
from pathlib import Path
from bs4 import BeautifulSoup
d = Path(r'C:\Microsaas\obra\src\content')
for lang in ['en','es','fr','de','it','pt']:
    f = d / lang / '401.html'
    if f.exists():
        s = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
        h2 = s.find('h2')
        h1 = s.find('h1')
        txt = s.get_text(strip=True)
        topic = h2.get_text(strip=True)[:80] if h2 else (h1.get_text(strip=True)[:80] if h1 else 'N/A')
        print(f'{lang}: {len(txt)} chars - "{topic}"')
