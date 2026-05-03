import json, re

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
i18n = json.load(open('src/i18n/en.json', encoding='utf-8'))['calculators']

broken = []
for c in calcs:
    cid = c['id']
    ci18n = i18n.get(cid, {})
    inputs = c.get('inputs', [])
    formula = c.get('formula', '')
    
    issues = []
    
    calc_input_ids = {inp['id'] for inp in inputs if 'id' in inp}
    
    # Check formula references inputs that exist
    if formula:
        # Find all inputs.XXX or inputs['XXX'] or inputs["XXX"] patterns
        refs = set()
        for m in re.finditer(r'inputs\.(\w+)', formula):
            refs.add(m.group(1))
        for m in re.finditer(r"inputs\['([^']+)'\]", formula):
            refs.add(m.group(1))
        for m in re.finditer(r'inputs\["([^"]+)"\]', formula):
            refs.add(m.group(1))
        
        missing_refs = refs - calc_input_ids
        if missing_refs:
            issues.append(f'formula refs missing inputs: {missing_refs}')
    
    # Check for empty formula
    if not formula or not formula.strip():
        issues.append('empty formula')
    
    if issues:
        broken.append((cid, c['slug'], issues))

print(f'Calculators with formula issues: {len(broken)}')
for cid, slug, issues in broken[:30]:
    print(f'  {cid} {slug}: {issues}')
if len(broken) > 30:
    print('...')
    for cid, slug, issues in broken[-10:]:
        print(f'  {cid} {slug}: {issues}')
