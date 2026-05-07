"""
Sync de.json calculator entries with fixed individual calculator JSON files.
Reads fixed translations from individual files and updates de.json.
"""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
DE_JSON = r"C:\Microsaas\obra\src\i18n\de.json"

# Load current de.json
with open(DE_JSON, 'r', encoding='utf-8') as f:
    de_i18n = json.load(f)

# Build calculator translations from individual files
calc_files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

de_calcs = {}
synced = 0
no_id = 0

for f in calc_files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    
    calc_id = str(data.get('id', ''))
    if not calc_id:
        no_id += 1
        continue
    
    de = data.get('i18n', {}).get('de', {})
    if de:
        sync_fields = ['name', 'seo_title', 'seo_description', 'inputs', 'outputs']
        entry = {}
        for field in sync_fields:
            if field in de:
                entry[field] = de[field]
        de_calcs[calc_id] = entry

# Update de.json calculators section
old_calcs = de_i18n.get('calculators', {})
updated = 0

for calc_id, entry in de_calcs.items():
    if calc_id in old_calcs:
        old_entry = old_calcs[calc_id]
        # Check if anything changed
        changed = False
        for field, value in entry.items():
            if old_entry.get(field) != value:
                old_entry[field] = value
                changed = True
        if changed:
            updated += 1
    else:
        old_calcs[calc_id] = entry
        updated += 1

# Also update for any entry not in individual files
for calc_id in old_calcs:
    if calc_id not in de_calcs:
        old_calcs[calc_id] = None

de_i18n['calculators'] = old_calcs

# Write back
with open(DE_JSON, 'w', encoding='utf-8') as f:
    json.dump(de_i18n, f, ensure_ascii=False, indent=2)

print(f"Calculator entries in de.json: {len(de_calcs)}")
print(f"Updated entries: {updated}")
print(f"Files without ID: {no_id}")
print("de.json written.")
