"""Check and fix the see-also link regex that might have broken links."""
from pathlib import Path
import re

d = Path(r'C:\Microsaas\obra\src\content')

# Check what the see-also links look like now
for lang in ['fr', 'de']:
    f = d / lang / '097.html'
    if f.exists():
        content = f.read_text(encoding='utf-8')
        see_also = re.search(r'<p class="see-also">.*?</p>', content, re.DOTALL)
        if see_also:
            print(f'{lang}/097.html see-also:')
            print(f'  {see_also.group(0)[:200]}')
            print()
