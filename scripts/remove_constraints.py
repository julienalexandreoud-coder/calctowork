import json

with open('src/calculators/calculators.json', encoding='utf-8') as f:
    data = json.load(f)

total_inputs = 0
removed = 0

for calc in data['calculators']:
    for inp in calc.get('inputs', []):
        total_inputs += 1
        for key in ('min', 'max', 'step'):
            if key in inp:
                del inp[key]
                removed += 1

with open('src/calculators/calculators.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Processed {len(data["calculators"])} calculators')
print(f'Total inputs: {total_inputs}')
print(f'Constraints removed: {removed}')
