import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

generic_patterns = [
    'Calculate instantly with step-by-step results',
    'Calculate instantly and for free',
    'Calcula al instante con resultados paso a paso',
    'Calculez instantan',
    'Calcule instantaneamente com resultados passo a passo',
    'Sofort berechnen mit schrittweisen Ergebnissen',
    'Calcola istantaneamente con risultati dettagliati',
]

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    calcs = data['calculators']
    for cid, c in calcs.items():
        desc = c.get('seo_description', '') or c.get('seo_desc', '')
        name = c.get('name', '')
        if desc == name + '.' or desc == name:
            print(f'{lang}/{cid}: name-only: "{desc[:60]}"')
        for pat in generic_patterns:
            if pat in desc:
                print(f'{lang}/{cid}: generic: "{desc[:60]}"')
                break