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

# Find the closing ] of TOOLS list
# The TOOLS list ends before PARAMETRIC_VARIANTS
tools_end = content.find('PARAMETRIC_VARIANTS')
if tools_end == -1:
    print('Could not find PARAMETRIC_VARIANTS')
    exit(1)

# Find the last ] before PARAMETRIC_VARIANTS
insert_pos = content.rfind(']', 0, tools_end)
if insert_pos == -1:
    print('Could not find closing bracket')
    exit(1)

lines = []
for c in new_calcs:
    cid = c['id']
    slug = c['slug']
    block = c.get('block_slug', '')
    cat = block_to_cat.get(block, 'A')
    slugs = json.dumps({'es': slug, 'en': slug, 'fr': slug, 'pt': slug, 'de': slug, 'it': slug}, ensure_ascii=False)
    lines.append(f'    {{"id": "{cid}", "cat": "{cat}", "block": "{block}", "slugs": {slugs}}},')

# Insert before the closing ]
new_content = content[:insert_pos] + '\n    # ── NEW CALCULATORS ──\n' + '\n'.join(lines) + '\n' + content[insert_pos:]

with open('scripts/tools_config.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Added', len(lines), 'entries')
