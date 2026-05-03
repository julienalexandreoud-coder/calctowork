import json, re
from collections import Counter, defaultdict

data = json.load(open('src/calculators/calculators.json', 'r', encoding='utf-8'))
calc_ids = set(c['id'] for c in data['calculators'])
calc_inputs = {c['id']: {inp['id'] for inp in c.get('inputs', [])} for c in data['calculators']}

with open('scripts/tools_config.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================
# 1. DUPLICATE SLUGS WITHIN SAME LANGUAGE
# ============================================
print("=" * 60)
print("1. DUPLICATE SLUGS WITHIN SAME LANGUAGE")
print("=" * 60)

# Extract all TOOLS slug entries with their language
tools_section = content.split("PARAMETRIC_VARIANTS = {")[0]
# Parse each tool entry's slugs
slug_pattern = r'"id":\s*"(\d+)"[^}]*?"slugs":\s*\{([^}]+)\}'
slug_lang_pairs = defaultdict(list)  # lang -> [(slug, id)]

for match in re.finditer(slug_pattern, tools_section, re.DOTALL):
    tool_id = match.group(1)
    slugs_text = match.group(2)
    for lang_match in re.finditer(r'"(es|en|fr|pt|de|it)":\s*"([^"]+)"', slugs_text):
        lang = lang_match.group(1)
        slug = lang_match.group(2)
        slug_lang_pairs[lang].append((slug, tool_id))

for lang, pairs in sorted(slug_lang_pairs.items()):
    slug_counts = Counter(slug for slug, _ in pairs)
    dups = {slug: count for slug, count in slug_counts.items() if count > 1}
    if dups:
        print(f"\n  Language: {lang}")
        for slug, count in sorted(dups.items(), key=lambda x: -x[1]):
            ids = [tid for s, tid in pairs if s == slug]
            print(f"    '{slug}' used by IDs: {ids}")

# Also check across different tool IDs that have IDENTICAL slugs in ALL languages
print("\n\n--- Tools with ALL slugs identical across all 6 languages ---")
all_identical = []
for match in re.finditer(slug_pattern, tools_section, re.DOTALL):
    tool_id = match.group(1)
    slugs_text = match.group(2)
    slug_values = re.findall(r'"(?:es|en|fr|pt|de|it)":\s*"([^"]+)"', slugs_text)
    if len(slug_values) >= 2 and len(set(slug_values)) == 1:
        all_identical.append((tool_id, slug_values[0]))

if all_identical:
    for tid, slug in all_identical[:20]:
        print(f"  ID {tid}: all slugs = '{slug}'")
    if len(all_identical) > 20:
        print(f"  ... and {len(all_identical) - 20} more")

# ============================================
# 2. PARAMETRIC VARIANTS - Missing languages in title/desc templates
# ============================================
print("\n" + "=" * 60)
print("2. PARAMETRIC VARIANTS - MISSING TRANSLATIONS")
print("=" * 60)

pv_section = content.split("PARAMETRIC_VARIANTS = {")[1]

# Find all pv entries with title_template
title_tpl_pattern = r'"(\d+)":\s*\{[^}]*?"title_template":\s*\{([^}]+)\}'
for match in re.finditer(title_tpl_pattern, pv_section, re.DOTALL):
    pv_id = match.group(1)
    tpl_text = match.group(2)
    langs = re.findall(r'"(es|en|fr|pt|de|it)":', tpl_text)
    missing = set(['es','en','fr','pt','de','it']) - set(langs)
    if missing:
        print(f"  PV {pv_id} title_template missing languages: {missing}")

# Find entries with desc_template (same check)
desc_tpl_pattern = r'"(\d+)":\s*\{[^}]*?"desc_template":\s*\{([^}]+)\}'
for match in re.finditer(desc_tpl_pattern, pv_section, re.DOTALL):
    pv_id = match.group(1)
    tpl_text = match.group(2)
    langs = re.findall(r'"(es|en|fr|pt|de|it)":', tpl_text)
    missing = set(['es','en','fr','pt','de','it']) - set(langs)
    if missing:
        print(f"  PV {pv_id} desc_template missing languages: {missing}")

# ============================================
# 3. PARAMETRIC VARIANTS - Inputs not matching calculator definition
# ============================================
print("\n" + "=" * 60)
print("3. PARAMETRIC VARIANTS - INPUT MISMATCHES")
print("=" * 60)

# Parse each PV entry manually
pv_entries_str = pv_section.strip().rstrip('}').strip()
pv_id_pattern = r'"(\d+)":\s*\{'

for match in re.finditer(pv_id_pattern, pv_section):
    pv_id = match.group(1)
    if pv_id not in calc_inputs:
        continue
    # Find the inputs dict for this pv entry
    start = match.start()
    # Find "inputs": { ... }
    inputs_match = re.search(r'"inputs":\s*\{([^}]+)\}', pv_section[start:start+2000])
    if not inputs_match:
        continue
    inputs_text = inputs_match.group(1)
    pv_input_keys = set(re.findall(r'"(\w+)":\s*\[', inputs_text))
    calc_input_set = calc_inputs.get(pv_id, set())
    not_in_calc = pv_input_keys - calc_input_set
    if not_in_calc:
        print(f"  PV {pv_id}: parametric input key(s) {not_in_calc} NOT in calculator inputs {calc_input_set}")

# ============================================
# 4. PARAMETRIC VARIANTS - Simplified entries missing url_fn, title_template, desc_template
# ============================================
print("\n" + "=" * 60)
print("4. SIMPLIFIED PV ENTRIES (1105-1119) - MISSING FIELDS")
print("=" * 60)

for pv_id in ['1105','1106','1107','1108','1109','1110','1111','1112','1113','1114','1115','1116','1117','1118','1119']:
    # Extract the entry
    pattern = f'"{pv_id}":' + r'\s*\{([^}]+)\}'
    match = re.search(pattern, pv_section)
    if match:
        entry_text = match.group(1)
        has_url_fn = 'url_fn' in entry_text
        has_title = 'title_template' in entry_text or 'title_fn' in entry_text
        has_desc = 'desc_template' in entry_text or 'desc_fn' in entry_text
        print(f"  PV {pv_id}: url_fn={has_url_fn}, title={has_title}, desc={has_desc}")

# ============================================
# 5. Duplicate PV slugs that could collide
# ============================================
print("\n" + "=" * 60)
print("5. POTENTIAL DUPLICATE CALCULATORS (same concept, different IDs)")
print("=" * 60)

duplicates = [
    ("096", "307", "Break-even"),
    ("082", "503", "Fuel cost"),
    ("400", "410", "BMI / BMR"),
    ("402", "414", "Ideal weight"),
    ("403", "434", "Water intake"),
    ("057", "929", "COP/EER"),
    ("050", "950", "Three-phase / Newton"),
    ("045", "946", "Lighting / Kinetic energy"),
    ("200", "910", "Percentage / Fraction"),
    ("203", "917", "Pythagoras / Right triangle"),
    ("202", "919", "Rectangle area"),
    ("204", "957", "Rule of three / Combinations"),
    ("300", "936", "Mortgage"),
    ("095", "939", "Profit margin"),
    ("073", "1112", "Wallpaper"),
    ("023", "1107", "Laminate flooring"),
    ("030", "1110", "Grout"),
    ("004", "1117", "Retaining wall"),
    ("014", "1115", "Drywall"),
]

for id1, id2, label in duplicates:
    print(f"  IDs {id1} & {id2}: {label} - possible duplicate calculators")

# Check for slugs that are used by multiple calculator IDs in the same language
print("\n" + "=" * 60)
print("6. SLUG COLLISIONS (same slug, different calculator ID)")
print("=" * 60)

# Re-parse more carefully per-language
for lang in ['es', 'en', 'fr', 'pt', 'de', 'it']:
    slug_map = defaultdict(list)
    for match in re.finditer(slug_pattern, tools_section, re.DOTALL):
        tool_id = match.group(1)
        slugs_text = match.group(2)
        for lang_match in re.finditer(r'"(es|en|fr|pt|de|it)":\s*"([^"]+)"', slugs_text):
            l = lang_match.group(1)
            s = lang_match.group(2)
            if l == lang:
                slug_map[s].append(tool_id)
    
    collisions = {s: ids for s, ids in slug_map.items() if len(ids) > 1}
    if collisions:
        print(f"\n  {lang.upper()} slug collisions:")
        for s, ids in sorted(collisions.items()):
            # Only show first 10 per language
            print(f"    '{s}' -> IDs: {ids}")

print("\nDone.")