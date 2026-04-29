"""Full content audit - categorize all calculators"""
import json
import os

calcs = json.loads(open('src/calculators/calculators.json', encoding='utf-8').read())['calculators']

i18n = {}
with open('src/i18n/en.json', encoding='utf-8') as f:
    for cid, data in json.load(f).get('calculators', {}).items():
        i18n[cid] = data.get('name', '')

missing = []
thin = []
complete = []

for calc in calcs:
    cid = calc['id']
    name = i18n.get(cid, '')
    block = calc.get('block_slug', '?')
    slug = calc.get('slug', '')
    
    src_file = f'src/content/en/{cid}.html'
    
    if not os.path.exists(src_file):
        missing.append({'id': cid, 'name': name, 'block': block, 'slug': slug})
    else:
        content = open(src_file, encoding='utf-8').read()
        words = len(content.split())
        has_faq = 'faq-item' in content.lower()
        has_example = 'Example' in content
        has_steps = '<ol>' in content or '<li>' in content
        
        if words > 1000 and has_faq and has_example and has_steps:
            complete.append({'id': cid, 'name': name, 'block': block, 'slug': slug, 'words': words})
        else:
            thin.append({'id': cid, 'name': name, 'block': block, 'slug': slug, 'words': words})

# Save results
with open('audit_missing.json', 'w', encoding='utf-8') as f:
    json.dump(missing, f, indent=2, ensure_ascii=False)

with open('audit_thin.json', 'w', encoding='utf-8') as f:
    json.dump(thin, f, indent=2, ensure_ascii=False)

with open('audit_complete.json', 'w', encoding='utf-8') as f:
    json.dump(complete, f, indent=2, ensure_ascii=False)

print(f"MISSING (no content): {len(missing)}")
print(f"THIN (needs expansion): {len(thin)}")
print(f"COMPLETE (good): {len(complete)}")
print(f"\nFiles saved: audit_missing.json, audit_thin.json, audit_complete.json")

# Show first 10 of each
print("\n--- MISSING (first 10) ---")
for c in missing[:10]:
    print(f"  {c['id']}: {c['name'][:45]} ({c['block']})")

print("\n--- THIN (first 10) ---")
for c in thin[:10]:
    print(f"  {c['id']}: {c['name'][:45]} ({c['block']}) - {c['words']}w")
