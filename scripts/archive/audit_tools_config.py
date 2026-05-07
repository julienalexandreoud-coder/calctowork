import json, re
from collections import Counter

data = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))
calc_ids = set(c['id'] for c in data['calculators'])

with open('scripts/tools_config.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract TOOLS ids
tools_ids = re.findall(r'"id":\s*"(\d+)"', content)
tools_ids_set = set(tools_ids)
print(f'Total tools_config IDs: {len(tools_ids_set)}')

# Extract PARAMETRIC_VARIANTS keys (lines after "PARAMETRIC_VARIANTS = {")
pv_section = content.split("PARAMETRIC_VARIANTS = {")[1] if "PARAMETRIC_VARIANTS = {" in content else ""
pv_keys = re.findall(r'^\s+"(\d+)":\s*\{', pv_section, re.MULTILINE)
pv_keys_set = set(pv_keys)
print(f'Total parametric variant keys: {len(pv_keys_set)}')

# Check TOOLS IDs not in calculators.json
missing_from_calc = tools_ids_set - calc_ids
print(f'\nTOOLS IDs not in calculators.json ({len(missing_from_calc)}):')
for id in sorted(missing_from_calc, key=int):
    print(f'  {id}')

# Check calc IDs not in TOOLS
missing_from_tools = calc_ids - tools_ids_set
print(f'\nCalc IDs not in TOOLS ({len(missing_from_tools)}):')
for id in sorted(missing_from_tools, key=int):
    print(f'  {id}')

# Check PV keys not in calculators.json
missing_pv_from_calc = pv_keys_set - calc_ids
print(f'\nParametric variant keys not in calculators.json ({len(missing_pv_from_calc)}):')
for id in sorted(missing_pv_from_calc, key=int):
    print(f'  {id}')

# Check for duplicate IDs in TOOLS list
id_counts = Counter(tools_ids)
duplicates = {id: count for id, count in id_counts.items() if count > 1}
print(f'\nDuplicate TOOLS IDs: {duplicates}')

# Check for duplicate slugs within same language
slug_entries = re.findall(r'"(?:es|en|fr|pt|de|it)":\s*"([^"]+)"', content)
# Only check from TOOLS list section, not PV
tools_section = content.split("PARAMETRIC_VARIANTS = {")[0]
slug_entries_tools = re.findall(r'"(?:es|en|fr|pt|de|it)":\s*"([^"]+)"', tools_section)
slug_counts = Counter(slug_entries_tools)
slug_dups = {slug: count for slug, count in slug_counts.items() if count > 1}
print(f'\nDuplicate slugs in TOOLS ({len(slug_dups)}):')
for slug, count in sorted(slug_dups.items(), key=lambda x: -x[1]):
    print(f'  {slug}: {count} occurrences')

# Check for missing 6-language translations in slugs
tools_entries = re.findall(r'"id":\s*"\d+".*?"slugs":\s*\{([^}]+)\}', tools_section, re.DOTALL)
missing_langs = []
for i, entry in enumerate(tools_entries):
    lang_entries = re.findall(r'"(es|en|fr|pt|de|it)":', entry)
    missing = set(['es','en','fr','pt','de','it']) - set(lang_entries)
    if missing:
        # Find the ID
        id_match = re.search(r'"id":\s*"(\d+)"', tools_section.split('"slugs"')[i+1] if i+1 < len(tools_section.split('"slugs"')) else '')
        missing_langs.append((i, missing))

# Check 910-962 batch for missing translations
batch_start = content.find('"910"')
batch_end = content.find('"110"')
if batch_start > 0 and batch_end > 0:
    batch_text = content[batch_start:batch_end]
    batch_entries = re.findall(r'"id":\s*"(\d+)".*?"slugs":\s*\{([^}]+)\}', batch_text, re.DOTALL)
    for tool_id, slugs_text in batch_entries:
        langs = re.findall(r'"(es|en|fr|pt|de|it)":', slugs_text)
        missing = set(['es','en','fr','pt','de','it']) - set(langs)
        if missing:
            print(f'  ID {tool_id}: missing languages {missing}')
        # Check if all slug values are identical (not localized)
        slug_values = re.findall(r'"(?:es|en|fr|pt|de|it)":\s*"([^"]+)"', slugs_text)
        if len(set(slug_values)) == 1 and len(slug_values) >= 2:
            print(f'  ID {tool_id}: ALL SLUGS IDENTICAL - not localized: {slug_values[0]}')

# Check parametric variant slug collisions
print('\n--- Checking parametric variant URL collisions ---')
# Extract all url_fn lambdas
pv_url_fns = re.findall(r'"(\d+)":\s*\{[^}]*"url_fn":\s*lambda\s+p:\s*([^\n]+)', pv_section, re.DOTALL)
# Can't easily eval, skip this

# Check parametric variant input keys match calculator inputs
print('\n--- Checking parametric variant input keys vs calculator inputs ---')
calc_inputs = {c['id']: {inp['id'] for inp in c.get('inputs', [])} for c in data['calculators']}

# Parse PV entries more carefully
pv_entries_raw = re.findall(r'^\s+"(\d+)":\s*\{(.*?)\n\s+\},?', pv_section, re.MULTILINE)
for pv_id, pv_body in pv_entries_raw[:5]:  # Just check first 5
    input_keys = re.findall(r'"(\w+)":\s*\[', pv_body)
    if pv_id in calc_inputs:
        calc_inp = calc_inputs[pv_id]
        pv_inputs = set(input_keys)
        not_in_calc = pv_inputs - calc_inp
        if not_in_calc:
            print(f'  PV {pv_id}: parametric inputs {not_in_calc} not in calculator inputs {calc_inp}')

# Check for all PV entries
for pv_id, pv_body in pv_entries_raw:
    input_keys = re.findall(r'"(\w+)":\s*\[', pv_body)
    if pv_id in calc_inputs:
        calc_inp = calc_inputs[pv_id]
        pv_inputs = set(input_keys)
        not_in_calc = pv_inputs - calc_inp
        if not_in_calc:
            print(f'  PV {pv_id}: parametric inputs {not_in_calc} NOT in calculator inputs')

# Check for empty slugs
empty_slugs = re.findall(r'"(es|en|fr|pt|de|it)":\s*""', content)
if empty_slugs:
    print(f'\nEmpty slug values found: {len(empty_slugs)}')

# Check all slugs are valid URLs (no spaces, special chars)
bad_slugs = re.findall(r'"(?:es|en|fr|pt|de|it)":\s*"([^"]*[\s!@#$%^&*()+={}\[\]|\\;:\'",<>?][^"]*)"', content)
if bad_slugs:
    print(f'\nSlugs with invalid URL characters: {bad_slugs[:10]}')