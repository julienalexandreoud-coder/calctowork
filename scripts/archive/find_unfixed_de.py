"""Find unfixed German output labels that don't match translation dict."""
import json, glob, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from fix_de_outputs import OUTPUT_TRANSLATIONS

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

unmatched = {}

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    if not de:
        continue
    outputs = de.get('outputs', {})
    for key, val in outputs.items():
        if val and val not in OUTPUT_TRANSLATIONS and val.lower() not in OUTPUT_TRANSLATIONS:
            # Check if this output looks non-German (contains English/Spanish)
            is_non_german = False
            # Check if value is different from Spanish version
            es = data.get('i18n', {}).get('es', {})
            es_outputs = es.get('outputs', {})
            es_val = es_outputs.get(key, '')
            if es_val and es_val != val:
                is_non_german = True
            
            if is_non_german or any(w in val.lower() for w in ['result', 'value', 'total', 'number', 'amount', 'calculate']):
                if val not in unmatched:
                    unmatched[val] = {'count': 0, 'es': es_val, 'file': os.path.basename(f)}
                unmatched[val]['count'] += 1

print(f"Unmatched output labels needing translation:")
print("=" * 60)
for label, info in sorted(unmatched.items(), key=lambda x: x[1]['count'], reverse=True):
    if info['es']:
        print(f"  [{info['count']}x] '{label}' (ES: '{info['es']}')")
    else:
        print(f"  [{info['count']}x] '{label}'")
