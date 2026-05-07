from pathlib import Path
import re

d = Path(r'C:\Microsaas\obra\src\content')

# Count actual <öl> occurrences across all DE files
de_count = 0
for f in (d / 'de').glob('*.html'):
    content = f.read_text(encoding='utf-8')
    if '<öl>' in content or '<\xc3\xb6l>' in content:
        de_count += 1

print(f'DE files with <öl>: {de_count}')

# Check what the fix script actually changed
# Look at the fix script pattern to see what was matched
sample = open(list((d / 'en').glob('*.html'))[0], encoding='utf-8').read()
patterns = [
    r'class="faq-item\s+',
    r'class="faq-item<',
    r'class="faq-item>',
    r'<öl>',
    r'class="faq-ap>',
]
for p in patterns:
    print(f'Pattern "{p}": found in sample={bool(re.search(p, sample))}')
