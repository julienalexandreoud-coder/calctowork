import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['es', 'fr', 'pt', 'de', 'it']

generic_patterns = [
    'Calculate instantly with step-by-step results',
    'Calculate instantly and for free',
    'Calcula al instante con resultados paso a paso',
    'Calculez instantan',
    'Calcule instantaneamente',
    'Sofort berechnen mit schrittweisen',
    'Calcola istantaneamente con risultati dettagliati',
]

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    calcs = data['calculators']
    generic_ids = []
    for cid, c in calcs.items():
        desc = c.get('seo_description', '') or c.get('seo_desc', '')
        for pat in generic_patterns:
            if pat in desc:
                generic_ids.append(cid)
                break
    print(f'{lang}: {len(generic_ids)} generic')
    if generic_ids:
        for cid in generic_ids[:3]:
            print(f'  {cid}: {calcs[cid].get("seo_description","")[:80]}')