import json

# Read the calculators.json file
with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fields to extract (keep example_inputs as-is, translate the other 7 fields)
fields_to_extract = ['example_label', 'range_hints', 'result_context', 'formula_display', 'steps', 'mistakes', 'input_type_review']

# Since the source text is already in Spanish, we just extract it
output = []

for calc in data['calculators']:
    extracted = {
        'id': calc['id'],
        'slug': calc['slug'],
        'example_inputs': calc.get('example_inputs', {})
    }
    
    for field in fields_to_extract:
        extracted[field] = calc.get(field)
    
    output.append(extracted)

# Save to i18n_es.json with UTF-8 encoding (no BOM)
with open(r'C:\Microsaas\obra\i18n_es.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(output)} calculators to i18n_es.json")
