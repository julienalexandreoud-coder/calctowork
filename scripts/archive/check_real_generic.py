"""Check if remaining 'padded' descriptions are actually generic or unique."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Only truly generic phrases
REAL_GENERIC = [
    'Calculate instantly with step-by-step results',
    'Calculate instantly and for free',
    'Calcula al instante con resultados paso a paso',
    'Calculez instantanement avec des resultats detailles',
    'Calcule instantaneamente com resultados passo a passo',
    'Sofort berechnen mit schrittweisen Ergebnissen',
    'Calcola istantaneamente con risultati dettagliati',
]

REAL_PHRASES = [
    'Get instant results with step-by-step explanation.',
    'Free online tool with formula and worked examples.',
    'Accurate, fast calculation with clear methodology.',
    'Enter your values and get precise results immediately.',
    'Easy-to-use calculator with formula breakdown and tips.',
    'Obten resultados al instante con explicacion paso a paso.',
    'Herramienta gratuita con formula y ejemplos resueltos.',
    'Calculo preciso y rapido con metodologia clara.',
    'Outil gratuit avec formule et exemples pratiques.',
    'Calcul precis et rapide avec methodologie claire.',
    'Ferramenta gratuita com formula e exemplos praticos.',
    'Calcule preciso e rapido com metodologia clara.',
    'Kostenloses Online-Tool mit Formel und Beispielen.',
    'Einfacher Rechner mit Formelaufschluss und Tipps.',
    'Strumento gratuito con formula ed esempi pratici.',
    'Calcolo preciso e veloce con metodologia chiara.',
]

for lang in ['es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    truly_generic = 0
    for ci in calcs.values():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        for p in REAL_PHRASES:
            if p in desc:
                truly_generic += 1
                break
    
    print(f"{lang}: truly_generic={truly_generic}/441")