import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Check EN distribution
data = json.load(open(os.path.join(I18N_DIR, 'en.json'), 'r', encoding='utf-8'))
calcs = data['calculators']

buckets = {'0-80': 0, '80-120': 0, '120-155': 0, '155+': 0}
for ci in calcs.values():
    desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
    l = len(desc)
    if l <= 80: buckets['0-80'] += 1
    elif l <= 120: buckets['80-120'] += 1
    elif l <= 155: buckets['120-155'] += 1
    else: buckets['155+'] += 1

print("EN Description Length Distribution (after optimization):")
for bucket, count in buckets.items():
    print(f"  {bucket} chars: {count} calculators")

# Count how many are in the sweet spot
good = buckets['120-155']
total = sum(buckets.values())
print(f"\nIn sweet spot (120-155): {good}/{total} ({good/total*100:.1f}%)")