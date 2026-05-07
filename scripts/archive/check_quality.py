"""Check the quality of rewritten descriptions and fix remaining issues."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

GENERIC_PHRASES = [
    'Get instant results with step-by-step explanation.',
    'Free online tool with formula and worked examples.',
    'Accurate, fast calculation with clear methodology.',
    'Enter your values and get precise results immediately.',
    'Easy-to-use calculator with formula breakdown and tips.',
    'Obten resultados al instante',
    'Herramienta gratuita con formula',
    'Calculo preciso y rapido',
    'Calculadora facil de usar',
    'Obtenez des resultats',
    'Outil gratuit avec formule',
    'Calcul precis et rapide',
    'Calcule preciso e rapido',
    'Ferramenta gratuita',
    'Sofortige Ergebnisse mit',
    'Kostenloses Online-Tool',
    'Prázise, schnelle Berechnung',
    'Einfacher Rechner',
    'Ottieni risultati istantanei',
    'Strumento gratuito con formula',
    'Calcolo preciso e veloce',
]

for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    still_padded = 0
    too_short = 0
    good = 0
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        is_padded = any(p in desc for p in GENERIC_PHRASES)
        
        if is_padded:
            still_padded += 1
        elif len(desc) < 120:
            too_short += 1
        else:
            good += 1
    
    print(f"{lang}: good={good}, still_padded={still_padded}, too_short={too_short}, total={good+still_padded+too_short}")