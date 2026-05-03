import json
from collections import defaultdict

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

calcs = data['calculators']

# Block field type inconsistency
print('=== BLOCK FIELD TYPE INCONSISTENCY ===')
block_types = defaultdict(int)
for c in calcs:
    b = c.get('block', '')
    btype = type(b).__name__
    block_types[btype] += 1
print(f'  Number types: {block_types.get("int", 0)}')
print(f'  String types: {block_types.get("str", 0)}')

string_blocks = [(c.get('id'), c.get('slug'), c.get('block'), c.get('block_slug')) for c in calcs if isinstance(c.get('block', ''), str)]
print(f'\n  Calculators with string block (should be int?): {len(string_blocks)}')
for cid, slug, block, bslug in string_blocks[:20]:
    print(f'    ID={cid} ({slug}) block="{block}" block_slug="{bslug}"')

# Check for calculators where block != numeric mapping
print('\n=== CALCULATORS WHERE block AND block_slug DONT MATCH EXPECTED PATTERN ===')
# The main categories seem to use numeric blocks 1-18
# The 1000+ series use string block = block_slug
# Let's see what the "correct" block->slug mapping should be
known_mapping = {}
for c in calcs:
    bn = c.get('block', '')
    bs = c.get('block_slug', '')
    if isinstance(bn, int) and 1 <= bn <= 18:
        if bn not in known_mapping:
            known_mapping[bn] = set()
        known_mapping[bn].add(bs)

print('  Expected block->slug mapping:')
for bn in sorted(known_mapping.keys()):
    slugs = known_mapping[bn]
    if len(slugs) > 1:
        print(f'    block {bn}: MULTIPLE SLUGS = {slugs}  *** INCONSISTENT ***')
    else:
        print(f'    block {bn}: {list(slugs)[0]}')

# Check for select inputs
print('\n=== SELECT INPUTS ANALYSIS ===')
select_count = 0
for c in calcs:
    for inp in c.get('inputs', []):
        if inp.get('type') == 'select':
            select_count += 1
            opts = inp.get('options', [])
            if not opts:
                print(f'  ID={c.get("id")} input "{inp.get("id","")}" is select with NO options')
            elif len(opts) < 2:
                print(f'  ID={c.get("id")} input "{inp.get("id","")}" is select with only {len(opts)} options: {opts}')
print(f'  Total select inputs: {select_count}')

# Check for empty formulas or formula syntax issues
print('\n=== FORMULA SYNTAX CHECKS ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    formula = c.get('formula', '')
    
    # Check for potential JS errors
    if 'undefined' in formula and '!=' not in formula and '!==' not in formula:
        # Using undefined as value rather than comparison
        pass  # Many formulas use undefined checks, skip this

    # Check for remaining template patterns
    if '{{' in formula or '}}' in formula:
        print(f'  ID={cid} ({slug}) formula contains unreplaced template: {{ }}')
    
    if 'TODO' in formula or 'FIXME' in formula:
        print(f'  ID={cid} ({slug}) formula contains TODO/FIXME')
    
    # Check formula doesn't reference output IDs that don't exist
    outputs = c.get('outputs', [])
    output_ids = {o.get('id') for o in outputs}
    input_ids = {i.get('id') for i in c.get('inputs', [])}

# Check for calculators with no highlight on any output
print('\n=== CALCULATORS WITH NO HIGHLIGHTED OUTPUT ===')
for c in calcs:
    outputs = c.get('outputs', [])
    has_highlight = any(o.get('highlight') for o in outputs)
    if not has_highlight:
        print(f'  ID={c.get("id")} ({c.get("slug","")}) - no output has highlight=true')

# Check for calculators with multiple highlighted outputs
print('\n=== CALCULATORS WITH MULTIPLE HIGHLIGHTED OUTPUTS ===')
for c in calcs:
    outputs = c.get('outputs', [])
    highlights = [o.get('id','') for o in outputs if o.get('highlight')]
    if len(highlights) > 1:
        print(f'  ID={c.get("id")} ({c.get("slug","")}) - multiple highlights: {highlights}')

# Check input unit_options consistency
print('\n=== UNIT OPTIONS WITHOUT UNIT ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    for inp in c.get('inputs', []):
        has_unit_options = bool(inp.get('unit_options'))
        has_unit = bool(inp.get('unit', ''))
        if has_unit_options and not has_unit:
            print(f'  ID={cid} ({slug}) input "{inp.get("id","")}" has unit_options but no unit')

# Check for mojibake in all string fields
print('\n=== MOJIBAKE (DOUBLE-ENCODED UTF-8) ===')
for c in calcs:
    cid = c.get('id', '')
    slug = c.get('slug', '')
    for field in ['formula_display', 'example_label', 'result_context']:
        val = c.get(field, '')
        if 'Ã' in val:
            print(f'  ID={cid} ({slug}) {field}: {val[:80]}...')
    for out in c.get('outputs', []):
        u = out.get('unit', '')
        if 'Ã' in u:
            print(f'  ID={cid} ({slug}) output unit: {u}')
    for inp in c.get('inputs', []):
        for field in ['unit']:
            u = inp.get(field, '')
            if 'Ã' in u:
                print(f'  ID={cid} ({slug}) input unit: {u}')

# Check IDs with leading zeros
print('\n=== ID FORMAT ISSUES ===')
for c in calcs:
    cid = c.get('id', '')
    if not cid.isdigit():
        print(f'  ID="{cid}" ({c.get("slug","")}) is not numeric')

# Check for inputs with duplicate IDs within same calculator
print('\n=== DUPLICATE INPUT IDS WITHIN CALCULATOR ===')
for c in calcs:
    input_ids = [i.get('id','') for i in c.get('inputs', [])]
    if len(input_ids) != len(set(input_ids)):
        dupes = [x for x in input_ids if input_ids.count(x) > 1]
        print(f'  ID={c.get("id")} ({c.get("slug","")}) has duplicate input ids: {set(dupes)}')

# Check for outputs with duplicate IDs within same calculator
print('\n=== DUPLICATE OUTPUT IDS WITHIN CALCULATOR ===')
for c in calcs:
    output_ids = [o.get('id','') for o in c.get('outputs', [])]
    if len(output_ids) != len(set(output_ids)):
        dupes = [x for x in output_ids if output_ids.count(x) > 1]
        print(f'  ID={c.get("id")} ({c.get("slug","")}) has duplicate output ids: {set(dupes)}')