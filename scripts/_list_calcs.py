import json, glob, os

calcs = []
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    cid = int(d['id'])
    slug = d['slug']
    block = d.get('block_slug', '?')
    en_name = d.get('i18n', {}).get('en', {}).get('name', 'N/A')
    es_name = d.get('i18n', {}).get('es', {}).get('name', 'N/A')
    
    has_content = []
    for lang in ['es', 'en', 'fr', 'pt', 'de', 'it']:
        if os.path.exists(f'src/content/{lang}/{d["id"]}.html'):
            has_content.append(lang.upper())
        else:
            has_content.append('--')
    
    calcs.append((cid, slug, block, en_name[:55], has_content))

calcs.sort(key=lambda x: x[0])
print(f'{"ID":>5} {"SLUG":<35} {"BLOCK":<16} {"EN NAME":<55} {"CONTENT":<22}')
print('=' * 140)
for cid, slug, block, en_name, content in calcs:
    content_str = ' '.join(content)
    print(f'{cid:>5} {slug:<35} {block:<16} {en_name:<55} {content_str}')
print(f'\nTotal: {len(calcs)} calculators')
