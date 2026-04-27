import json
import re

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
calcs = data.get('calculators', data)

new_calcs = [c for c in calcs if int(c['id']) >= 910]
print('Found', len(new_calcs), 'new calculators')

block_to_cat = {
    'matematicas': 'A', 'salud': 'B', 'finanzas': 'C',
    'cotidiano': 'D', 'ciencia': 'E', 'deportes': 'B',
    'conversion': 'A', 'estadistica': 'A',
}

with open('scripts/tools_config.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the TOOLS list end
last_match = None
for m in re.finditer(r'\{\s*"id":\s*"\d+"[^}]+\}\s*,?', content):
    last_match = m

if not last_match:
    print('Could not find TOOLS list')
    exit(1)

insert_pos = last_match.end()

lines = []
for c in new_calcs:
    cid = c['id']
    slug = c['slug']
    block = c.get('block_slug', '')
    cat = block_to_cat.get(block, 'A')
    slugs = json.dumps({'es': slug, 'en': slug, 'fr': slug, 'pt': slug, 'de': slug, 'it': slug}, ensure_ascii=False)
    lines.append(f'    {{"id": "{cid}", "cat": "{cat}", "block": "{block}", "slugs": {slugs}}},')

new_content = content[:insert_pos] + '\n' + '\n'.join(lines) + '\n' + content[insert_pos:]

with open('scripts/tools_config.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Added', len(lines), 'entries')
