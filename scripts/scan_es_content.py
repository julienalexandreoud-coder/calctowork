"""
Scan all ES content files for topic mismatches.
Reads actual content body to detect if it's about the wrong calculator.
"""
import json, re
from pathlib import Path

base = Path(r'C:\Microsaas\obra')
calcs_dir = base / 'src' / 'calculators'
es_content_dir = base / 'src' / 'content' / 'es'

# Load all calculator info
calc_info = {}
for calc_dir in sorted(calcs_dir.iterdir()):
    if not calc_dir.is_dir():
        continue
    cid = calc_dir.name
    calc_json = calc_dir / 'calc.json'
    es_json = calc_dir / 'es.json'
    if not calc_json.exists():
        continue
    
    with open(calc_json, encoding='utf-8') as f:
        calc_data = json.load(f)
    
    es_name = ''
    if es_json.exists():
        with open(es_json, encoding='utf-8') as f:
            es_i18n = json.load(f)
        es_name = es_i18n.get('name', '')
    
    inputs = [i.get('id','') for i in calc_data.get('inputs',[])]
    outputs = [o.get('id','') for o in calc_data.get('outputs',[])]
    
    calc_info[cid] = {
        'name': es_name.lower(),
        'inputs': inputs,
        'outputs': outputs,
    }

print(f'Loaded {len(calc_info)} calculator definitions')
print('Scanning ES content files...\n')

mismatches = []

for es_file in sorted(es_content_dir.glob('*.html')):
    cid = es_file.stem
    if cid not in calc_info:
        continue
    
    info = calc_info[cid]
    calc_name = info['name']
    
    content = es_file.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    first_300 = text[:300].lower()
    
    # Detect content topic based on specific keywords in the BODY
    # Key: calculator-specific terms that should NOT appear in wrong calc content
    is_pipe_content = any(w in first_300 for w in ['tubería', 'tuberia', 'dn', 'diámetro interior', 'diámetro exterior', 'espesor de pared'])
    is_calorie_content = any(w in first_300 for w in ['caloría', 'calorias', 'tdee', 'grasa corporal', 'bmi prime'])
    is_molecular_content = any(w in first_300 for w in ['peso molecular', 'masa molecular', 'molecular'])
    is_compound_interest = any(w in first_300 for w in ['interés compuesto', 'interes compuesto', 'capital inicial', 'tasa de interés'])
    is_mortgage = any(w in first_300 for w in ['hipoteca', 'pago mensual', 'plazo del préstamo'])
    is_bmi = any(w in first_300 for w in ['índice de masa corporal', 'indice de masa corporal', 'imc'])
    is_tdee = any(w in first_300 for w in ['gasto energético', 'gasto energetico', 'tdee', 'calorías diarias'])
    is_water = any(w in first_300 for w in ['agua diaria', 'consumo de agua', 'hidratación'])
    is_speed = any(w in first_300 for w in ['velocidad', 'distancia', 'tiempo'])
    
    # Now check if the content topic matches the calculator
    mismatched = False
    # Check: Is this labeled as concrete but has pipe content?
    if 'hormigón' in calc_name or 'concreto' in calc_name:
        if is_pipe_content:
            mismatches.append((cid, calc_name, 'PIPE CONTENT in CONCRETE calc', first_300[:120]))
            continue
    
    # Check: Is this labeled as BMI but has calorie content?
    if 'imc' in calc_name or 'bmi' in calc_name or 'masa corporal' in calc_name:
        if is_calorie_content and not is_bmi:
            mismatches.append((cid, calc_name, 'CALORIE CONTENT in BMI calc', first_300[:120]))
            continue
    
    # Check: Area converter has molecular weight content?
    if 'área' in calc_name or 'superficie' in calc_name:
        if is_molecular_content:
            mismatches.append((cid, calc_name, 'MOLECULAR WEIGHT in AREA calc', first_300[:120]))
            continue
    
    # Check: TDEE but has BMI content?
    if 'caloría' in calc_name and 'diaria' in calc_name:
        if is_bmi and not is_tdee:
            mismatches.append((cid, calc_name, 'BMI CONTENT in TDEE calc', first_300[:120]))
            continue
    
    # Generic check: does the content h2/heading mention the calculator name?
    h2_match = re.search(r'<h[12]>(.*?)</h[12]>', content)
    h2_text = h2_match.group(1).lower() if h2_match else ''
    
    # Extract calc name keywords (skip common words)
    name_keywords = set(w for w in calc_name.split() if len(w) > 4)
    
    if h2_text and name_keywords:
        common = name_keywords & set(h2_text.split())
        if len(common) == 0 and len(name_keywords) > 0:
            mismatches.append((cid, calc_name, f'H2 MISMATCH: h2="{h2_text[:60]}"', first_300[:120]))

print(f'Found {len(mismatches)} mismatches:\n')
for cid, calc_name, issue, snippet in sorted(mismatches, key=lambda x: int(x[0])):
    print(f'ID {cid}: calc="{calc_name[:50]}"')
    print(f'  Issue: {issue}')
    print(f'  Content starts: {snippet}')
    print()
