import json
from pathlib import Path

f = Path(r'C:\Microsaas\obra\src\calculators')
files = list(f.glob('*.json'))
print(f'Total calc JSON files: {len(files)}')

# Check a few files for Spanish patterns
patterns = [' típico ', ' típica ', 'ingresados', 'tepical', ' del ', ' y ', ' para ']
for fname in ['area.json', 'imc-bmi.json', 'interes-compuesto.json', 'hormigon-masa.json']:
    fp = f / fname
    if not fp.exists(): continue
    data = json.load(open(fp, encoding='utf-8'))
    i18n = data.get('i18n', {})
    for lang in ['en', 'fr', 'de', 'it', 'pt']:
        if lang not in i18n: continue
        ld = i18n[lang]
        for field in ['range_hints', 'result_context', 'example_label']:
            val = ld.get(field, '')
            if isinstance(val, str):
                for p in patterns:
                    if p in val:
                        print(f'{fname}/{lang}/{field}: found "{p}" in "{val[:80]}"')
                        break
            elif isinstance(val, dict):
                for k, v in val.items():
                    if isinstance(v, str):
                        for p in patterns:
                            if p in v:
                                print(f'{fname}/{lang}/{field}.{k}: found "{p}" in "{v[:80]}"')
                                break
