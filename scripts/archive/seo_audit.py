"""Audit current SEO titles and descriptions across all 441 calculators in all 6 languages."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

calcs = json.load(open(os.path.join(CALC_DIR, 'calculators.json'), 'r', encoding='utf-8'))['calculators']
calc_by_id = {str(c['id']): c for c in calcs}

issues = {'short_desc': [], 'short_title': [], 'generic_desc': [], 'generic_title': [], 'no_formula_in_title': []}

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs_i18n = data['calculators']
    
    for cid, ci in calcs_i18n.items():
        seo_title = ci.get('seo_title', '')
        seo_desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        name = ci.get('name', '')
        
        # Check title length
        if len(seo_title) < 30:
            issues['short_title'].append(f'{lang}/{cid}: title="{seo_title}" ({len(seo_title)} chars)')
        
        # Check description length  
        if len(seo_desc) < 80:
            issues['short_desc'].append(f'{lang}/{cid}: desc="{seo_desc[:80]}..." ({len(seo_desc)} chars)')
        
        # Check for generic patterns
        generic_patterns = [
            'Calculate instantly',
            'Free online',
            'Online calculator',
            'Calcula al instante',
            'Calculez instantan',
            'Calcule instantaneamente',
            'Sofort berechnen',
            'Calcola istantaneamente',
        ]
        for pat in generic_patterns:
            if pat in seo_desc:
                issues['generic_desc'].append(f'{lang}/{cid}')
                break
        
        # Check if title is just the name
        if seo_title == name or seo_title == name + ' - CalcToWork':
            issues['generic_title'].append(f'{lang}/{cid}')

print("=" * 60)
print("SEO AUDIT REPORT")
print("=" * 60)

print(f"\nTotal calculators: {len(calcs)}")
print(f"Languages: {', '.join(LANGS)}")

print(f"\n--- SHORT TITLES (<30 chars): {len(issues['short_title'])} ---")
for item in issues['short_title'][:10]:
    print(f"  {item}")
if len(issues['short_title']) > 10:
    print(f"  ... and {len(issues['short_title']) - 10} more")

print(f"\n--- SHORT DESCRIPTIONS (<80 chars): {len(issues['short_desc'])} ---")
for item in issues['short_desc'][:10]:
    print(f"  {item}")
if len(issues['short_desc']) > 10:
    print(f"  ... and {len(issues['short_desc']) - 10} more")

print(f"\n--- GENERIC DESCRIPTIONS: {len(set(issues['generic_desc']))} ---")
unique_generic = set(issues['generic_desc'])
print(f"  Total unique calc/lang combos with generic descriptions: {len(unique_generic)}")

print(f"\n--- GENERIC TITLES (just name): {len(issues['generic_title'])} ---")
for item in issues['generic_title'][:10]:
    print(f"  {item}")
if len(issues['generic_title']) > 10:
    print(f"  ... and {len(issues['generic_title']) - 10} more")

# Show some example good titles/descriptions
print(f"\n--- EXAMPLE GOOD ENTRIES ---")
for lang in ['en']:
    data = json.load(open(os.path.join(I18N_DIR, f'{lang}.json'), 'r', encoding='utf-8'))
    calcs_i18n = data['calculators']
    good = []
    for cid, ci in sorted(calcs_i18n.items()):
        title = ci.get('seo_title', '')
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        if 40 < len(title) < 70 and 100 < len(desc) < 160:
            good.append((cid, title, desc))
            if len(good) >= 5:
                break
    for cid, title, desc in good:
        print(f"  {cid}: title='{title}' ({len(title)} chars)")
        print(f"         desc='{desc[:100]}...' ({len(desc)} chars)")