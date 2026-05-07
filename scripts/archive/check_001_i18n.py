import json

langs = ['es', 'fr', 'de', 'it', 'pt']
for lang in langs:
    i18n = json.load(open(f'src/i18n/{lang}.json', encoding='utf-8'))['calculators']
    c001 = i18n.get('001', {})
    print(lang + ':')
    print('  Name:', c001.get('name'))
    print('  Inputs:', c001.get('inputs', {}))
    print('  Outputs:', c001.get('outputs', {}))
    print()
