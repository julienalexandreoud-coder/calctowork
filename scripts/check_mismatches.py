import json

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
i18n = json.load(open('src/i18n/en.json', encoding='utf-8'))['calculators']

mismatches = ['022', '029', '031', '032', '040', '045', '067', '072', '077']
for cid in mismatches:
    c = [x for x in calcs if x['id'] == cid][0]
    ci18n = i18n.get(cid, {})
    calc_inputs = {inp['id'] for inp in c.get('inputs', []) if 'id' in inp}
    i18n_inputs = set(ci18n.get('inputs', {}).keys())
    print(cid, c['slug'])
    print('  calc inputs:', calc_inputs)
    print('  i18n inputs:', i18n_inputs)
    print('  missing in calc:', i18n_inputs - calc_inputs)
    print('  missing in i18n:', calc_inputs - i18n_inputs)
    print()
