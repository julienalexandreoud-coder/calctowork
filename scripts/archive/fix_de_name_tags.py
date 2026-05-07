"""Remove (EN) and (ES) tags from German calculator names."""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

fixed = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    
    de = data.get('i18n', {}).get('de', {})
    name = de.get('name', '')
    seo_title = de.get('seo_title', '')
    
    modified = False
    
    if ' (EN)' in name:
        de['name'] = name.replace(' (EN)', '')
        modified = True
    if ' (EN)' in seo_title:
        de['seo_title'] = seo_title.replace(' (EN)', '')
        modified = True
    if ' (ES)' in name:
        de['name'] = name.replace(' (ES)', '')
        modified = True
    if ' (ES)' in seo_title:
        de['seo_title'] = seo_title.replace(' (ES)', '')
        modified = True
    
    if modified:
        data['i18n']['de'] = de
        with open(f, 'w', encoding='utf-8') as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        fixed += 1
        print(f"  FIXED: {os.path.basename(f)}")

print(f"\nFixed: {fixed}")
