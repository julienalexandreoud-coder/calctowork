import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

FIXES = {
    'fr': {'422': "Calculateur IMC Prime – Ratio Poids"},
    'pt': {'422': "Calculadora IMC Prime – Razão Peso"},
    'de': {'139': "Quartile-Rechner – Q1 bis Q3 Bestimmen"},
    'it': {'422': "Calcolatore BMI Prime – Rapporto Peso"},
}

for lang, fixes in FIXES.items():
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    for cid, new_title in fixes.items():
        calcs[cid]['seo_title'] = new_title
        print(f'{lang}/{cid}: "{new_title}" ({len(new_title)}c)')
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

# Verify
print('\n--- FINAL CHECK ---')
for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) < 30)
    good = sum(1 for ci in calcs.values() if 30 <= len(ci.get('seo_title', '')) <= 60)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) > 60)
    print(f'  {lang}: <30c={short}, 30-60c={good}, >60c={long}')