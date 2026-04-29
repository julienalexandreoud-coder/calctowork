import re, json

with open('scripts/calc_content.py', 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'LONG_CONTENT = {LONG_CONTENT = {'
section = content.split(marker, 1)
body = section[1].split('\ndef generate_long_content')[0]
lc_ids = set(re.findall(r'"(\d{3})"\s*:\s*\{', body))

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    calcs = json.load(f)['calculators']

all_ids = set(c['id'] for c in calcs)
missing = sorted(all_ids - lc_ids, key=lambda x: int(x))
print(f'Total calculators: {len(all_ids)}')
print(f'In LONG_CONTENT: {len(lc_ids)}')
print(f'NOT in LONG_CONTENT (template only): {len(missing)}')
for mid in missing:
    calc = next(c for c in calcs if c['id'] == mid)
    print(f'  {mid} | {calc["slug"]} | {calc["block_slug"]}')
