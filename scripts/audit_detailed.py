import json
from collections import defaultdict

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

calcs = data['calculators']

# 1. Duplicate slugs - show full details
print('=== DUPLICATE SLUGS (detailed) ===')
slug_map = defaultdict(list)
for c in calcs:
    slug_map[c.get('slug','')].append(c.get('id',''))

for slug, ids in sorted(slug_map.items()):
    if len(ids) > 1:
        print(f'\n  slug="{slug}" used by IDs: {ids}')
        for cid in ids:
            c = next(x for x in calcs if x.get('id') == cid)
            block = c.get('block', '?')
            block_slug = c.get('block_slug', '?')
            formula_preview = c.get('formula','')[:60]
            print(f'    ID={cid}, block={block}, block_slug={block_slug}')

# 2. Block mapping analysis
print('\n=== BLOCK NUMBER TO SLUG MAPPING ===')
block_num_to_slug = defaultdict(set)
for c in calcs:
    block_num_to_slug[c.get('block','')].add(c.get('block_slug',''))

for bn in sorted(block_num_to_slug.keys(), key=lambda x: str(x)):
    slugs = block_num_to_slug[bn]
    print(f'  block={bn}: {slugs}')

# 3. Related calculator references - find all bad ones
print('\n=== BAD RELATED REFERENCES (detailed) ===')
all_ids = {c.get('id') for c in calcs}
bad_refs = defaultdict(list)
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    for rid in c.get('related', []):
        if rid not in all_ids:
            bad_refs[cid].append((slug, rid))

for cid, refs in sorted(bad_refs.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 9999):
    slg = refs[0][0]
    ref_ids = [r[1] for r in refs]
    print(f'  ID={cid} ({slg}) references non-existent IDs: {ref_ids}')

# 4. Formula references to non-existent inputs
print('\n=== FORMULA BAD INPUT REFERENCES ===')
import re
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    formula = c.get('formula', '')
    if not formula:
        continue
    
    input_ids = {inp.get('id') for inp in c.get('inputs', [])}
    refs = re.findall(r'inputs\.(\w+)', formula)
    bad = [r for r in refs if r not in input_ids]
    if bad:
        print(f'  ID={cid} ({slug}) formula references inputs not defined: {bad}')

# 5. Missing example inputs
print('\n=== MISSING EXAMPLE INPUTS (detailed) ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    example = c.get('example_inputs', {})
    input_ids = {inp.get('id') for inp in c.get('inputs', [])}
    if not example:
        print(f'  ID={cid} ({slug}) has NO example_inputs at all')
        continue
    missing = input_ids - set(example.keys())
    if missing:
        print(f'  ID={cid} ({slug}) example_inputs missing: {missing}')

# 6. Duplicate IDs
print('\n=== DUPLICATE IDs ===')
id_map = defaultdict(list)
for c in calcs:
    id_map[c.get('id','')].append(c.get('slug','?'))
for cid, slugs in id_map.items():
    if len(slugs) > 1:
        print(f'  ID="{cid}" used by multiple calculators: {slugs}')

# 7. Calculators with no formula
print('\n=== CALCULATORS WITH NO FORMULA ===')
for c in calcs:
    if not c.get('formula', '').strip():
        print(f'  ID={c.get("id","")} ({c.get("slug","?")}) has empty formula')

# 8. Output IDs not computed in formula
print('\n=== OUTPUT IDS NOT IN FORMULA ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    formula = c.get('formula', '')
    for out in c.get('outputs', []):
        oid = out.get('id', '')
        if oid and formula and oid not in formula:
            print(f'  ID={cid} ({slug}) output id="{oid}" not found anywhere in formula')

# 9. Select inputs without options
print('\n=== SELECT INPUTS WITHOUT OPTIONS ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    for inp in c.get('inputs', []):
        if inp.get('type') == 'select' and not inp.get('options'):
            print(f'  ID={cid} ({slug}) input "{inp.get("id","")}" is select but has no options')

# 10. Input default out of min/max range
print('\n=== INPUT DEFAULTS OUT OF RANGE ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    for inp in c.get('inputs', []):
        iid = inp.get('id', '')
        default = inp.get('default')
        min_val = inp.get('min')
        max_val = inp.get('max')
        if default is not None and min_val is not None:
            try:
                if float(default) < float(min_val):
                    print(f'  ID={cid} ({slug}) input "{iid}" default={default} < min={min_val}')
            except (ValueError, TypeError):
                pass
        if default is not None and max_val is not None:
            try:
                if float(default) > float(max_val):
                    print(f'  ID={cid} ({slug}) input "{iid}" default={default} > max={max_val}')
            except (ValueError, TypeError):
                pass
        if min_val is not None and max_val is not None:
            try:
                if float(min_val) > float(max_val):
                    print(f'  ID={cid} ({slug}) input "{iid}" min={min_val} > max={max_val}')
            except (ValueError, TypeError):
                pass