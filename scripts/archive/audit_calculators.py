import json
import re
from collections import defaultdict

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

calcs = data['calculators']
print(f"Total calculators: {len(calcs)}")

# Check a few to understand schema
sample_keys = set()
for c in calcs[:10]:
    sample_keys.update(c.keys())
print(f"All keys across calculators: {sample_keys}")

# Check for input keys
sample_input_keys = set()
for c in calcs[:5]:
    for inp in c.get('inputs', []):
        sample_input_keys.update(inp.keys())
print(f"Input keys: {sample_input_keys}")

sample_output_keys = set()
for c in calcs[:5]:
    for out in c.get('outputs', []):
        sample_output_keys.update(out.keys())
print(f"Output keys: {sample_output_keys}")

issues = defaultdict(list)

# =========================================================
# 1. DUPLICATE IDs
# =========================================================
id_counts = defaultdict(list)
for c in calcs:
    cid = c.get('id', '')
    id_counts[cid].append(c.get('slug', 'no-slug'))

for cid, slugs in id_counts.items():
    if len(slugs) > 1:
        issues['DUPLICATE_ID'].append(f"id='{cid}' appears {len(slugs)} times: slugs={slugs}")

# =========================================================
# 2. MISSING REQUIRED FIELDS (based on actual schema)
# =========================================================
required_fields = ['id', 'slug', 'block', 'block_slug', 'inputs', 'formula', 'outputs']
for c in calcs:
    cid = c.get('id', '<no-id>')
    for field in required_fields:
        if field not in c:
            issues['MISSING_FIELD'].append(f"Calculator '{cid}' ({c.get('slug','?')}) missing field '{field}'")

    # Check for empty strings in important fields
    if c.get('slug', '') == '':
        issues['EMPTY_VALUE'].append(f"Calculator '{cid}' has empty slug")
    if c.get('formula', '') == '':
        issues['EMPTY_VALUE'].append(f"Calculator '{cid}' ({c.get('slug','?')}) has empty formula")
    if not c.get('inputs', []):
        issues['EMPTY_INPUTS'].append(f"Calculator '{cid}' ({c.get('slug','?')}) has empty inputs")
    if not c.get('outputs', []):
        issues['EMPTY_OUTPUTS'].append(f"Calculator '{cid}' ({c.get('slug','?')}) has empty outputs")

# =========================================================
# 3. PLACEHOLDER / TODO VALUES
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    for key, val in c.items():
        if isinstance(val, str):
            vl = val.strip().upper()
            if vl in ('TODO', 'FIXME', 'XXX', 'TBD', 'PLACEHOLDER', 'TEMP', 'TEST', 'N/A', 'HACK'):
                issues['PLACEHOLDER'].append(f"Calculator '{cid}' ({slug}) field '{key}' = '{val}'")
            elif vl == '':
                issues['EMPTY_VALUE'].append(f"Calculator '{cid}' ({slug}) field '{key}' is empty string")

# =========================================================
# 4. FORMULA ISSUES - check vars referenced but not in inputs/outputs
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    formula = c.get('formula', '')
    if not formula:
        continue

    input_ids = set()
    for inp in c.get('inputs', []):
        iid = inp.get('id', '')
        if iid:
            input_ids.add(iid)

    output_ids = set()
    for out in c.get('outputs', []):
        oid = out.get('id', '')
        if oid:
            output_ids.add(oid)

    # Extract tokens from formula that look like property access: inputs.xxx
    input_refs = set(re.findall(r'inputs\.(\w+)', formula))
    # Also check for direct variable assignments: var xxx= or xxx =
    assigned_vars = set(re.findall(r'(?:var|let|const)\s+(\w+)', formula))
    # Also check for object property shorthand in returns: {xxx, yyy}
    returned_vars = set(re.findall(r'\{([^}]+)\}', formula))
    returned_ids = set()
    for rv in returned_vars:
        for item in rv.split(','):
            item = item.strip()
            # Handle key: value pairs
            if ':' in item:
                key = item.split(':')[0].strip()
                # Skip numeric keys or expressions
                if re.match(r'^[a-zA-Z_]\w*$', key):
                    returned_ids.add(key)
            else:
                if re.match(r'^[a-zA-Z_]\w*$', item):
                    returned_ids.add(item)

    # Check that input_refs exist in inputs
    for ref in input_refs:
        if ref not in input_ids and ref not in output_ids:
            issues['FORMULA_BAD_INPUT_REF'].append(f"Calculator '{cid}' ({slug}) formula references inputs.{ref} but no input with id='{ref}'")

    # Check that output ids are actually computed in the formula
    for oid in output_ids:
        if oid not in returned_ids and oid not in assigned_vars and f'{oid}:' not in formula and f'{oid} :' not in formula:
            # More lenient check - just see if the var name appears anywhere in formula
            if oid not in formula:
                issues['FORMULA_MISSING_OUTPUT'].append(f"Calculator '{cid}' ({slug}) output id='{oid}' not found in formula")

# =========================================================
# 5. INCONSISTENT CATEGORIES (block/block_slug)
# =========================================================
block_map = defaultdict(set)
for c in calcs:
    block = c.get('block', '')
    block_slug = c.get('block_slug', '')
    block_map[block_slug].add(block)
    block_map[f"__block__{block}"].add(block_slug)

# Find blocks with multiple block numbers or slugs
slug_to_block = defaultdict(set)
block_to_slug = defaultdict(set)
for c in calcs:
    b = c.get('block', '')
    bs = c.get('block_slug', '')
    slug_to_block[bs].add(b)
    block_to_slug[b].add(bs)

for bs, blocks in slug_to_block.items():
    if len(blocks) > 1:
        issues['INCONSISTENT_BLOCK'].append(f"block_slug='{bs}' maps to multiple block numbers: {blocks}")

for b, slugs in block_to_slug.items():
    if len(slugs) > 1:
        issues['INCONSISTENT_BLOCK'].append(f"block={b} maps to multiple block_slugs: {slugs}")

# =========================================================
# 6. INPUT FIELD ISSUES
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    for inp in c.get('inputs', []):
        iid = inp.get('id', '<unnamed>')
        itype = inp.get('type', 'number')

        # Missing id
        if not inp.get('id'):
            issues['INPUT_MISSING_ID'].append(f"Calculator '{cid}' ({slug}) input missing 'id'")

        # Select type without options
        if itype == 'select':
            opts = inp.get('options', [])
            if not opts:
                issues['INPUT_SELECT_NO_OPTIONS'].append(f"Calculator '{cid}' ({slug}) input '{iid}' is select but has no options")
            elif len(opts) < 2:
                issues['INPUT_SELECT_FEW_OPTIONS'].append(f"Calculator '{cid}' ({slug}) input '{iid}' is select with only {len(opts)} option(s)")

        # Number type checks
        if itype in ('number', 'range', 'float'):
            default = inp.get('default')
            min_val = inp.get('min')
            max_val = inp.get('max')

            # Default out of range
            if default is not None and min_val is not None:
                try:
                    if float(default) < float(min_val):
                        issues['INPUT_DEFAULT_BELOW_MIN'].append(f"Calculator '{cid}' ({slug}) input '{iid}' default={default} < min={min_val}")
                except (ValueError, TypeError):
                    pass

            if default is not None and max_val is not None:
                try:
                    if float(default) > float(max_val):
                        issues['INPUT_DEFAULT_ABOVE_MAX'].append(f"Calculator '{cid}' ({slug}) input '{iid}' default={default} > max={max_val}")
                except (ValueError, TypeError):
                    pass

            # Min > max
            if min_val is not None and max_val is not None:
                try:
                    if float(min_val) > float(max_val):
                        issues['INPUT_MIN_GREATER_MAX'].append(f"Calculator '{cid}' ({slug}) input '{iid}' min={min_val} > max={max_val}")
                except (ValueError, TypeError):
                    pass

            # Non-numeric step
            step = inp.get('step')
            if step is not None:
                if isinstance(step, str):
                    try:
                        float(step)
                    except ValueError:
                        issues['INPUT_STEP_NON_NUMERIC'].append(f"Calculator '{cid}' ({slug}) input '{iid}' step='{step}' is non-numeric string")

            # Non-numeric default
            if default is not None and isinstance(default, str):
                try:
                    float(default)
                except ValueError:
                    issues['INPUT_DEFAULT_NON_NUMERIC'].append(f"Calculator '{cid}' ({slug}) input '{iid}' default='{default}' is non-numeric string for type '{itype}'")

        # Missing unit for measurement inputs
        if itype == 'number' and not inp.get('unit') and not inp.get('unit_category'):
            # Some numeric inputs are dimensionless - only flag if this looks like it should have a unit
            pass  # Will check separately

# =========================================================
# 7. OUTPUT FIELD ISSUES
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    for out in c.get('outputs', []):
        oid = out.get('id', '<unnamed>')

        if not out.get('id'):
            issues['OUTPUT_MISSING_ID'].append(f"Calculator '{cid}' ({slug}) output missing 'id'")

        # Check for encoding issues in unit
        unit = out.get('unit', '')
        if unit and ('\ufffd' in unit or '\u00ef' in unit or '' in unit):
            issues['OUTPUT_ENCODING_ISSUE'].append(f"Calculator '{cid}' ({slug}) output '{oid}' unit='{unit}' has encoding issues")

        # Empty unit (most outputs should have units)
        if not unit and out.get('type') != 'text':
            issues['OUTPUT_MISSING_UNIT'].append(f"Calculator '{cid}' ({slug}) output '{oid}' has no unit")

# =========================================================
# 8. EXAMPLE_INPUTS ISSUES
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    example = c.get('example_inputs', {})
    input_ids = {inp.get('id') for inp in c.get('inputs', [])}

    if not example:
        issues['MISSING_EXAMPLE'].append(f"Calculator '{cid}' ({slug}) has no example_inputs")
    else:
        # Check example references non-existent inputs
        for key in example:
            if key not in input_ids:
                issues['EXAMPLE_BAD_REF'].append(f"Calculator '{cid}' ({slug}) example_inputs references '{key}' but no input with that id")

        # Check inputs not covered by example
        for iid in input_ids:
            if iid not in example:
                issues['EXAMPLE_MISSING_INPUT'].append(f"Calculator '{cid}' ({slug}) example_inputs missing input '{iid}'")

# =========================================================
# 9. RELATED CALCULATOR REFERENCES
# =========================================================
all_ids = {c.get('id') for c in calcs}
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    related = c.get('related', [])
    for rid in related:
        if rid not in all_ids:
            issues['RELATED_BAD_REF'].append(f"Calculator '{cid}' ({slug}) references non-existent calculator id='{rid}'")

    # Self-reference check
    if cid in related:
        issues['RELATED_SELF_REF'].append(f"Calculator '{cid}' ({slug}) references itself in related")

# =========================================================
# 10. ENCODING ISSUES IN STRING FIELDS
# =========================================================
for c in calcs:
    cid = c.get('id', '<no-id>')
    slug = c.get('slug', '')
    for field in ['formula_display', 'example_label', 'result_context']:
        val = c.get(field, '')
        if val and ('\ufffd' in val or '' in val):
            issues['ENCODING_ISSUE'].append(f"Calculator '{cid}' ({slug}) field '{field}' has encoding issues")

# =========================================================
# 11. DUPLICATE SLUGS
# =========================================================
slug_counts = defaultdict(list)
for c in calcs:
    s = c.get('slug', '')
    slug_counts[s].append(c.get('id', ''))

for s, ids in slug_counts.items():
    if len(ids) > 1:
        issues['DUPLICATE_SLUG'].append(f"slug='{s}' used by calculators: {ids}")

# =========================================================
# 12. CALCULATOR ID FORMAT CHECK
# =========================================================
for c in calcs:
    cid = c.get('id', '')
    if not re.match(r'^\d{3}$', cid):
        issues['ID_FORMAT'].append(f"Calculator id='{cid}' ({c.get('slug','')}) doesn't match 3-digit format")

# =========================================================
# 13. BLOCK/SLUG CONSISTENCY
# =========================================================
# Check sequential numbering
prev_id = 0
for c in calcs:
    cid = c.get('id', '')
    try:
        num = int(cid)
        if num != prev_id + 1:
            issues['ID_GAP'].append(f"ID gap: expected {prev_id+1}, got {num}")
        prev_id = num
    except ValueError:
        pass

# =========================================================
# PRINT RESULTS
# =========================================================
print("\n" + "="*80)
print("AUDIT RESULTS")
print("="*80)

total = 0
for cat in sorted(issues.keys()):
    cat_issues = issues[cat]
    total += len(cat_issues)
    print(f"\n--- {cat} ({len(cat_issues)} issues) ---")
    for iss in cat_issues[:30]:
        print(f"  {iss}")
    if len(cat_issues) > 30:
        print(f"  ... and {len(cat_issues) - 30} more")

print(f"\n{'='*80}")
print(f"TOTAL ISSUES: {total}")