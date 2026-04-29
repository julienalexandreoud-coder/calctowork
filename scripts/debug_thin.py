import re
from pathlib import Path

for lang in ['es', 'en', 'fr', 'de', 'it', 'pt']:
    pages = list(Path(f'public/{lang}').glob('*/index.html'))[:2]
    for page in pages:
        if page.parent.name in ('about','contact','privacy','terms'):
            continue
        content = page.read_text(encoding='utf-8')
        m = re.search(r'class="long-content"[^>]*>(.*?)</section>', content, re.DOTALL)
        if m:
            text = re.sub(r'<[^>]+>', ' ', m.group(1))
            words = len(text.split())
            print(f'{lang}/{page.parent.name}: {words} words')
        else:
            print(f'{lang}/{page.parent.name}: NO long-content section')
            # Check if there's any section with long-content-wrap or similar
            if 'long-content' in content:
                print('  BUT "long-content" string found in page')
            if 'long-content-wrap' in content:
                print('  "long-content-wrap" found')
