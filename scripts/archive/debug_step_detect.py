import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

f = open(r'C:\Microsaas\obra\src\i18n\en.json', 'r', encoding='utf-8')
en = json.load(f)

c = en['calculators']['100']
print(f'Has steps: {"steps" in c}')
print(f'Steps type: {type(c.get("steps"))}')
print(f'Steps len: {len(c.get("steps", []))}')

step_pat = re.compile(
    r'^(Introduce|Pulsa|Interpreta|Calcula\b|Identifica|Estima|Asigna|Determina|'
    r'Mide|Coloca|Resta\b|Suma\b|Divide\b|Multiplica|Convierte|Proyecta|'
    r'No considerar|Sobreestimar|Olvidar|Calcular ROI|Dimensionar|'
    r'Calcular volumen|Calcular el|Aseg\u00fArate|Verifica|Comprueba|'
    r'Recuerda|No olvides|Considera|Ten en cuenta|A\u00f1ade)\b'
)

for i, step in enumerate(c['steps']):
    m = step_pat.search(step)
    print(f'  Step {i}: match={bool(m)}  text="{step[:60]}"')

print(f'\nAlso checking ID 100 steps in check format:')
# What the check_spanish_accuracy.py does:
field_type = 'step'
pattern = step_pat
value = c.get(field_type)
print(f'  value exists: {bool(value)}')
if value:
    items = value if isinstance(value, list) else [value]
    print(f'  items count: {len(items)}')
    for item in items:
        if isinstance(item, str) and item.strip():
            result = pattern.search(item)
            print(f'  search result: {bool(result)}')
            if result:
                print(f'  ACCENT: {bool(re.search(r"[áéíóúñÁÉÍÓÚÑ]", item))}')
