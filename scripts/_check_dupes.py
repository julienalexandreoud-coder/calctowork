from pathlib import Path
import re

d = Path(r'C:\Microsaas\obra\src\content')
pattern = r'(<div\s+class="related-calculators">.*?</div>)'

for lang_dir in d.iterdir():
    if not lang_dir.is_dir():
        continue
    found = 0
    for f in lang_dir.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if len(matches) > 1:
            found += 1
    
    total = len(list(lang_dir.glob('*.html')))
    print(f'{lang_dir.name}: {found}/{total} files with duplicate sections')
