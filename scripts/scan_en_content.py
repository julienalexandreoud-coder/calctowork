"""Scan ALL English content files for WRONG CALCULATOR content."""
import json, re
from pathlib import Path

base = Path(r'C:\Microsaas\obra')
calcs_dir = base / 'src' / 'calculators'
en_content_dir = base / 'src' / 'content' / 'en'

# Build keyword signatures for each calculator
# What keywords SHOULD be in the content vs what should NOT
calc_signatures = {}

for calc_dir in sorted(calcs_dir.iterdir()):
    if not calc_dir.is_dir():
        continue
    cid = calc_dir.name
    
    calc_json = calc_dir / 'calc.json'
    en_json = calc_dir / 'en.json'
    if not calc_json.exists():
        continue
    
    with open(calc_json, encoding='utf-8') as f:
        cd = json.load(f)
    
    calc_name = ''
    if en_json.exists():
        with open(en_json, encoding='utf-8') as f:
            i18n = json.load(f)
        calc_name = i18n.get('name', '').lower()
    
    inputs = [i.get('id', '') for i in cd.get('inputs', [])]
    formula = cd.get('formula', '')
    
    calc_signatures[cid] = {
        'name': calc_name,
        'inputs': inputs,
        'formula': formula,
    }

# Now check each EN content file
print('Checking EN content for wrong calculator content...\n')
wrong = []
unclear = []

for en_file in sorted(en_content_dir.glob('*.html')):
    cid = en_file.stem
    if cid not in calc_signatures:
        continue
    
    info = calc_signatures[cid]
    calc_name = info['name']
    formula = info['formula']
    
    content = en_file.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    body = text.lower()
    first_500 = body[:500]
    
    # STRONG wrong indicators based on actual formula/topic
    # Check each calculator against formulas that don't belong
    is_concrete = any(w in calc_name for w in ['concrete', 'cement', 'slab', 'footing', 'beam', 'column', 'foundation'])
    is_finance = any(w in calc_name for w in ['loan', 'mortgage', 'interest', 'savings', 'salary', 'tax', 'vat', 'investment', 'retirement', 'roi', 'break-even', 'profit', 'budget', 'insurance', 'cagr', 'apr', 'annuity', 'wacc', 'sharpe', 'dividend'])
    is_health = any(w in calc_name for w in ['bmi', 'calorie', 'tdee', 'bmr', 'body fat', 'heart rate', 'sleep', 'water intake', 'ideal weight', 'pregnancy', 'protein', 'fiber'])
    is_math = any(w in calc_name for w in ['percentage', 'fraction', 'geometry', 'algebra', 'logarithm', 'factorial', 'exponent', 'pythagorean', 'circle', 'triangle', 'area', 'volume'])
    is_conversion = any(w in calc_name for w in ['converter', 'conversion'])
    is_physics = any(w in calc_name for w in ['speed', 'force', 'energy', 'density', 'pressure', 'acceleration', 'newton', 'kinetic', 'potential', 'work'])
    is_everyday = any(w in calc_name for w in ['tip', 'age', 'date', 'fuel', 'battery', 'download', 'screen', 'password', 'typing'])
    
    issues = []
    
    # Detailed checks
    if is_concrete:
        if 'pipe' in body and 'concrete' in calc_name:
            issues.append(f'PIPE content in concrete calc')
        if 'dn600' in body or 'dn' in body:
            issues.append('PIPE DIMENSIONS in concrete')
    
    if is_finance:
        if 'bmi' in body and 'body mass' in body and 'loan' in calc_name:
            issues.append('BMI content in finance calc')
        if 'concrete' in body and 'mortgage' in calc_name:
            issues.append('Concrete content in finance calc')
    
    if is_health:
        if 'mortgage' in body and 'bmi' in calc_name:
            issues.append('Mortgage content in health calc')
        if 'interest' in body and 'calorie' in calc_name:
            issues.append('Interest content in calorie calc')
    
    if is_conversion:
        if 'molecular' in body and 'area' in calc_name:
            issues.append('Molecular weight in converter')
        if 'bmi' in body and 'converter' in calc_name:
            issues.append('BMI content in converter')
    
    if is_math:
        if 'loan' in body and 'percentage' in calc_name:
            issues.append('Loan content in math calc')
    
    if is_physics:
        if 'loan' in body or 'mortgage' in body or 'interest' in body:
            issues.append('Finance content in physics calc')
    
    if is_everyday:
        if 'beam' in body and 'tip' in calc_name:
            issues.append('Construction content in everyday calc')
        if 'concrete' in body and ('age' in calc_name or 'date' in calc_name):
            issues.append('Concrete content in age/date calc')
    
    if issues:
        wrong.append((cid, calc_name, issues, first_500[:100]))

print(f'Found {len(wrong)} files with likely wrong content:\n')
for cid, name, issues, snippet in sorted(wrong, key=lambda x: int(x[0])):
    print(f'ID {cid}: "{name[:60]}"')
    for i in issues:
        print(f'  {i}')
    print(f'  Starts with: {snippet}')
    print()
