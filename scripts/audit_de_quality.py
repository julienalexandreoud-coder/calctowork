"""Audit German content quality across calculator JSONs and de.json."""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
DE_JSON = r"C:\Microsaas\obra\src\i18n\de.json"

# --- Part 1: Calculator JSON files ---
print("=" * 60)
print("PART 1: Calculator JSON files (i18n.de)")
print("=" * 60)

files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))
total = len(files)

spanish_marks = ['calcular', 'ingresar', 'resultado', 'valor ', 'entre ', 'porcentaje', 'número', 'años', 'meses']
garbled_marks = ['calcudiet', 'calcudie', 'f\u00fcrterminar', 'f\u00fcrcolocar',
                 'absonne', 'bund ', 'repristints', 'inerg\u00eda',
                 'mof\u00fcrrada', 'diist ', 'rechneih',
                 'uurrect', 'rderative', 'isttimation',
                 'bundated', 'paundmint', 'undear', 'percintage',
                 'mitsumo', 'adhistivo', 'incodiedo',
                 'imc indeich', 'colocar']

spanish_count = 0
garbled_count = 0
no_de = 0
ok_count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    if not de:
        no_de += 1
        continue

    # Collect all text from the German entry
    texts = []
    for key in ['name', 'seo_title', 'seo_description', 'example_label',
                'range_hints', 'steps', 'mistakes', 'input_type_review',
                'result_context', 'formula_display']:
        val = de.get(key, '')
        if isinstance(val, list):
            texts.extend([str(v) for v in val])
        elif isinstance(val, dict):
            texts.extend([str(v) for v in val.values()])
        elif isinstance(val, str):
            texts.append(val)

    # Also check inputs/outputs which are dicts
    for section in ['inputs', 'outputs']:
        sec = de.get(section, {})
        for k, v in sec.items():
            if isinstance(v, str):
                texts.append(v)

    full = ' '.join(texts).lower()

    sp = sum(1 for w in spanish_marks if w in full)
    gb = sum(1 for w in garbled_marks if w in full)

    if sp >= 2:
        spanish_count += 1
    if gb >= 1:
        garbled_count += 1

    if sp < 2 and gb == 0:
        ok_count += 1

print(f"Total calculator files: {total}")
print(f"No German i18n: {no_de}")
print(f"Spanish contamination (>=2 markers): {spanish_count}")
print(f"Garbled pseudo-German (>=1 marker): {garbled_count}")
print(f"Likely OK German: {ok_count}")
print(f"Files needing fix: {spanish_count + garbled_count}")

# --- Part 2: de.json calculator entries ---
print()
print("=" * 60)
print("PART 2: de.json calculator entries")
print("=" * 60)

with open(DE_JSON, 'r', encoding='utf-8') as f:
    de_i18n = json.load(f)

calcs = de_i18n.get('calculators', {})
print(f"Calculator entries: {len(calcs)}")

de_spanish = 0
de_no_steps = 0
de_no_example = 0

for calc_id, entry in calcs.items():
    el = entry.get('example_label', '')
    if isinstance(el, str):
        if any(w in el.lower() for w in ['calcular', 'ingresar', 'resultado', 'entre']):
            de_spanish += 1
    if not entry.get('steps'):
        de_no_steps += 1
    if not entry.get('example_label'):
        de_no_example += 1

print(f"Spanish example_label: {de_spanish}")
print(f"No steps: {de_no_steps}")
print(f"No example_label: {de_no_example}")

# --- Part 3: Content HTML stubs ---
print()
print("=" * 60)
print("PART 3: German Content HTML (src/content/de/)")
print("=" * 60)

de_content = r"C:\Microsaas\obra\src\content\de"
content_files = sorted(glob.glob(os.path.join(de_content, "*.html")))
print(f"Total content files: {len(content_files)}")

english_in_content = 0
fur_missing_umlaut = 0
metrique_accent = 0

for cf in content_files[:100]:  # Sample first 100
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read().lower()
    if 'ensure all values use a single consistent unit system' in content:
        english_in_content += 1
    if 'fur ' in content and 'f\u00fcr ' not in content:
        fur_missing_umlaut += 1
    if 'm\u00e9trische' in content:
        metrique_accent += 1

print(f"Sample (100 files):")
print(f"  English phrase: {english_in_content}")
print(f"  'fur' without umlaut: {fur_missing_umlaut}")
print(f"  'Métrische' with French accent: {metrique_accent}")

# Count unique issue patterns across all content files
all_issues = {}
for cf in content_files:
    with open(cf, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'ensure all values' in content:
        all_issues.setdefault('english_phrase', 0)
        all_issues['english_phrase'] += 1

print(f"\nAll {len(content_files)} content files:")
for k, v in all_issues.items():
    print(f"  {k}: {v}")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Calculator JSONs needing German fix: {spanish_count + garbled_count} of {total}")
print(f"de.json calc entries needing fix: {de_spanish} (Spanish example_label)")
print(f"Content HTML files with English: {all_issues.get('english_phrase', 0)}")
print(f"Templates: 'Skip to content' hardcoded in English across 4 templates")
