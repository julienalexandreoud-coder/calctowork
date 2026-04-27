import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

generic_patterns = [
    'Calculate instantly with step-by-step results',
    'Calculate instantly and for free',
    'Calcula al instante',
    'Calculez instantan',
    'Calcule instantaneamente',
    'Sofort berechnen',
    'Calcola istantaneamente',
]

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    calcs = data['calculators']
    generic_count = 0
    for cid, c in calcs.items():
        desc = c.get('seo_description', '') or c.get('seo_desc', '')
        for pat in generic_patterns:
            if pat in desc:
                generic_count += 1
                break
    print(f'{lang}: {generic_count} generic descriptions')

# Also check for descriptions that are just the name + "."
for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    calcs = data['calculators']
    name_only = 0
    for cid, c in calcs.items():
        desc = c.get('seo_description', '') or c.get('seo_desc', '')
        name = c.get('name', '')
        if desc == name + '.' or desc == name:
            name_only += 1
    if name_only > 0:
        print(f'{lang}: {name_only} name-only descriptions')