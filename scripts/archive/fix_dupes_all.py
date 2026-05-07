"""Remove duplicate calculator sections across ALL languages."""
from pathlib import Path
import re

d = Path(r'C:\Microsaas\obra\src\content')
count = 0

for lang_dir in d.iterdir():
    if not lang_dir.is_dir():
        continue
    for f in lang_dir.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        # Find duplicate related-calculators divs
        pattern = r'(<div\s+class="related-calculators">.*?</div>)'
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if len(matches) > 1:
            # Keep the first, remove subsequent duplicates
            first_end = matches[0].end()
            for m in reversed(matches[1:]):
                content = content[:m.start()] + content[m.end():]
                count += 1
            f.write_text(content, encoding='utf-8')
            print(f'  Fixed {lang_dir.name}/{f.name}')

print(f'Total duplicate divs removed: {count}')
