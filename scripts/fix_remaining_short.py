import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

MANUAL_FIXES = {
    'en': {
        '422': 'BMI Prime Calculator – Weight Ratio',
        '1071': 'pH Calculator – Acidity & Alkalinity',
    },
    'fr': {
        '422': 'IMC Prime – Ratio de Poids',
        '130': 'Calculateur de Logarithme – Toute Base',
        '133': 'Calculateur de Factorielle – Rapide',
        '134': 'Calculateur de Permutations – N!',
        '136': 'Calculateur d\'Écart-Type – Statistiques',
        '137': 'Calculateur de Variance – Statistiques',
        '138': 'Calculateur de Médiane – Valeur Centrale',
        '139': 'Calculateur de Quartiles – Q1 Q2 Q3',
        '142': 'Loi de Snell – Réfraction Calculateur',
        '147': 'Circuit RL – Impédance & Réactance',
        '148': 'Circuit RC – Impédance & Réactance',
        '430': 'Calculateur de Poids Cible – Objectif',
        '517': 'Latence Ping – Test Vitesse Réseau',
        '520': 'Coût SMS – Calculateur de Budget',
    },
    'pt': {
        '422': 'IMC Prime – Razão de Peso',
        '130': 'Calculadora de Logaritmo – Qualquer Base',
        '133': 'Calculadora de Fatorial – Rápida',
        '136': 'Calculadora de Desvio Padrão – Estatísticas',
        '137': 'Calculadora de Variância – Estatísticas',
        '138': 'Calculadora de Mediana – Valor Central',
        '139': 'Calculadora de Quartis – Q1 Q2 Q3',
        '142': 'Lei de Snell – Refração Calculadora',
        '339': 'CAGR Mensal – Taxa de Crescimento',
        '430': 'Calculadora de Peso Alvo – Objetivo',
        '520': 'Custo de SMS – Calculadora de Orçamento',
    },
    'de': {
        '422': 'BMI Prime – Gewichtsverhältnis',
        '133': 'Fakultät-Rechner – Schnell & Präzise',
        '137': 'Varianz-Rechner – Statistik Tool',
        '138': 'Median-Rechner – Zentralwert Finden',
        '139': 'Quartile-Rechner – Q1 Q2 Q3',
        '428': 'Ruheumsatz-Rechner – Grundumsatz',
        '519': 'Lesezeit-Rechner – Text & Geschwindigkeit',
    },
    'it': {
        '422': 'BMI Prime – Rapporto di Peso',
        '130': 'Calcolatore Logaritmo – Qualsiasi Base',
        '137': 'Calcolatore Varianza – Statistiche',
        '138': 'Calcolatore Mediana – Valore Centrale',
        '139': 'Calcolatore Quartili – Q1 Q2 Q3',
        '426': 'TDEE Calcolatore – Calorie Giornaliere',
        '517': 'Latenza Ping – Test Velocità Rete',
        '520': 'Costo SMS – Calcolatore Budget',
    },
}

for lang, fixes in MANUAL_FIXES.items():
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    changed = 0
    for cid, new_title in fixes.items():
        old = calcs[cid].get('seo_title', '')
        if old != new_title:
            calcs[cid]['seo_title'] = new_title
            changed += 1
            print(f'  {lang}/{cid}: "{old}" → "{new_title}" ({len(new_title)}c)')
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'  {lang}: fixed {changed} titles')

# Verify
print('\n--- FINAL TITLE LENGTH DISTRIBUTION ---')
for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) < 30)
    good = sum(1 for ci in calcs.values() if 30 <= len(ci.get('seo_title', '')) <= 60)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) > 60)
    print(f'  {lang}: <30c={short}, 30-60c={good}, >60c={long}')