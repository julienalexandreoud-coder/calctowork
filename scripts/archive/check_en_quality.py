import re
from pathlib import Path

templated = []
good = []
for f in Path('src/content/en').glob('*.html'):
    content = f.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    words = len(text.split())
    if 'class="formula-section"' in content or '<h1>' in content:
        templated.append((f.stem, words))
    else:
        good.append((f.stem, words))

print(f'Templated: {len(templated)}, avg: {sum(w for _,w in templated)/max(len(templated),1):.0f}w')
print(f'Good: {len(good)}, avg: {sum(w for _,w in good)/max(len(good),1):.0f}w')
print('Thinnest templated:', sorted(templated, key=lambda x: x[1])[:10])
