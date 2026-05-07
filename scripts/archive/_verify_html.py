from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')

# Verify HTML validity of a few fixed files
files_to_check = [
    d / 'en' / '951.html',
    d / 'en' / '097.html',
    d / 'de' / '001.html',
    d / 'fr' / '097.html',
]

for f in files_to_check:
    content = f.read_text(encoding='utf-8')
    try:
        soup = BeautifulSoup(content, 'html.parser')
        errors = []
        
        # Check for unclosed tags
        if '<öl>' in content:
            errors.append('has <öl>')
        if '</öl>' in content:
            errors.append('has </öl>')
        if 'class="faq-item>' in content:
            errors.append('missing quote in faq-item')
        if 'faq-ap' in content:
            errors.append('has faq-ap instead of faq-a')
        
        status = 'OK' if not errors else f'ISSUES: {", ".join(errors)}'
        print(f'{f.parent.name}/{f.name}: {status}')
    except Exception as e:
        print(f'{f.parent.name}/{f.name}: PARSE ERROR: {e}')
