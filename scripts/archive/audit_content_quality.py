import re
from pathlib import Path

for lang in ['en', 'es', 'fr', 'de', 'it', 'pt']:
    content_dir = Path(f'src/content/{lang}')
    if not content_dir.exists():
        continue
    templated = 0
    good = 0
    for f in content_dir.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        if 'class="formula-section"' in content or '<h1>' in content:
            templated += 1
        else:
            good += 1
    print(f'{lang}: {good} good, {templated} templated')
