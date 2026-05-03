import json, sys

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
i18n = json.load(open('src/i18n/en.json', encoding='utf-8'))['calculators']

broken = []
for c in calcs:
    cid = c['id']
    ci18n = i18n.get(cid, {})
    inputs = c.get('inputs', [])
    outputs = c.get('outputs', [])
    
    issues = []
    
    calc_input_ids = {inp['id'] for inp in inputs if 'id' in inp}
    i18n_input_ids = set(ci18n.get('inputs', {}).keys())
    
    if calc_input_ids and i18n_input_ids:
        missing_in_i18n = calc_input_ids - i18n_input_ids
        missing_in_calc = i18n_input_ids - calc_input_ids
        if missing_in_i18n:
            issues.append(f'i18n missing: {missing_in_i18n}')
        if missing_in_calc:
            issues.append(f'calc missing: {missing_in_calc}')
    
    # outputs can be list of strings or list of dicts
    calc_output_ids = set()
    for o in outputs:
        if isinstance(o, str):
            calc_output_ids.add(o)
        elif isinstance(o, dict):
            calc_output_ids.add(o.get('id', o.get('name', str(o))))
    
    i18n_output_ids = set(ci18n.get('outputs', {}).keys())
    if calc_output_ids and i18n_output_ids:
        missing_out_i18n = calc_output_ids - i18n_output_ids
        if missing_out_i18n:
            issues.append(f'output i18n missing: {missing_out_i18n}')
    
    if issues:
        broken.append((cid, c['slug'], issues))

print(f'Calculators with issues: {len(broken)}')
for cid, slug, issues in broken[:30]:
    print(f'  {cid} {slug}: {issues}')
if len(broken) > 30:
    print('...')
    for cid, slug, issues in broken[-10:]:
        print(f'  {cid} {slug}: {issues}')
