import re, json
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\content\en')
i18n = json.load(open(r'C:\Microsaas\obra\src\i18n\en.json', encoding='utf-8'))
calcs = i18n.get('calculators', {})

link_texts = {}
for f in d.glob('*.html'):
    content = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<a href="/en/ohms-law/">([^<]+)</a>', content):
        t = m.group(1)
        link_texts[t] = link_texts.get(t, 0) + 1

print('Broken link texts and their calculator matches:')
for text, count in sorted(link_texts.items(), key=lambda x: -x[1]):
    found = None
    text_lower = text.lower().strip()
    for cid, data in calcs.items():
        n = data.get('name', '').lower().strip()
        if text_lower == n or (len(text_lower) > 5 and (text_lower in n or n in text_lower)):
            found = f'{cid}: {data["name"]}'
            break
    match_str = f'MATCH: {found}' if found else 'NO MATCH'
    print(f'  [{count}x] "{text}" -> {match_str}')
