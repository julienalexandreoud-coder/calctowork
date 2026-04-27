"""Analyze description lengths and create an SEO optimization plan."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

calcs = json.load(open(os.path.join(CALC_DIR, 'calculators.json'), 'r', encoding='utf-8'))['calculators']
calc_by_id = {str(c['id']): c for c in calcs}

# Distribution of EN description lengths
en_data = json.load(open(os.path.join(I18N_DIR, 'en.json'), 'r', encoding='utf-8'))
calcs_en = en_data['calculators']

buckets = {'0-50': 0, '50-80': 0, '80-120': 0, '120-155': 0, '155-200': 0, '200+': 0}
examples_per_bucket = {'0-50': [], '50-80': [], '80-120': [], '120-155': [], '155-200': [], '200+': []}

for cid, ci in calcs_en.items():
    desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
    l = len(desc)
    if l <= 50:
        buckets['0-50'] += 1
        examples_per_bucket['0-50'].append((cid, desc[:80], l))
    elif l <= 80:
        buckets['50-80'] += 1
        examples_per_bucket['50-80'].append((cid, desc[:80], l))
    elif l <= 120:
        buckets['80-120'] += 1
        examples_per_bucket['80-120'].append((cid, desc[:80], l))
    elif l <= 155:
        buckets['120-155'] += 1
        examples_per_bucket['120-155'].append((cid, desc[:80], l))
    elif l <= 200:
        buckets['155-200'] += 1
        examples_per_bucket['155-200'].append((cid, desc[:80], l))
    else:
        buckets['200+'] += 1
        examples_per_bucket['200+'].append((cid, desc[:80], l))

print("EN Description Length Distribution:")
print("-" * 40)
for bucket, count in buckets.items():
    print(f"  {bucket} chars: {count} calculators")
    for cid, desc, l in examples_per_bucket[bucket][:2]:
        print(f"    {cid}: ({l}c) {desc}...")

# Check titles
print("\nEN Title Length Distribution:")
title_buckets = {'0-30': 0, '30-50': 0, '50-60': 0, '60-70': 0, '70+': 0}
for cid, ci in calcs_en.items():
    title = ci.get('seo_title', '')
    l = len(title)
    if l <= 30: title_buckets['0-30'] += 1
    elif l <= 50: title_buckets['30-50'] += 1
    elif l <= 60: title_buckets['50-60'] += 1
    elif l <= 70: title_buckets['60-70'] += 1
    else: title_buckets['70+'] += 1

for bucket, count in title_buckets.items():
    print(f"  {bucket} chars: {count} calculators")

# Also check how many have "Calculator" in the title (potential keyword stuffing)
calc_in_title = sum(1 for ci in calcs_en.values() if 'Calculator' in ci.get('seo_title', '') or 'calculator' in ci.get('seo_title', '').lower())
print(f"\nTitles containing 'Calculator': {calc_in_title} / {len(calcs_en)}")