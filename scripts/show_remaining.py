"""Identify remaining generic patterns in non-EN descriptions."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Broader detection of generic/calculated descriptions
GENERIC_PATTERNS = [
    'Calculate instantly with step-by-step results',
    'Calculate instantly and for free',
    'Calcula al instante con resultados paso a paso',
    'Calculez instantanement avec des resultats detailles',
    'Calcule instantaneamente com resultados passo a passo',
    'Sofort berechnen mit schrittweisen Ergebnissen',
    'Calcola istantaneamente con risultati dettagliati',
    # Previous template phrases
    'Obten resultados al instante',
    'Herramienta gratuita con formula',
    'Calculo preciso y rapido',
    'Outil gratuit avec formule',
    'Calcul precis et rapide',
    'Calcule preciso e rapido',
    'Ferramenta gratuita',
    'Sofortige Ergebnisse',
    'Kostenloses Online-Tool',
    'Einfacher Rechner',
    'Ottieni risultati istantanei',
    'Strumento gratuito con formula',
    'Calcolo preciso e veloce',
    # Additional patterns
    ' para ',   # "for category" pattern from previous script
    ' pour ',
    ' fur ',
    ' per ',
    ' para ',
    'Incluye',
    'With waste',
    'Inclut',
    'Include',
]

for lang in ['es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    # Find descriptions with generic patterns
    remaining_generic = []
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        # Check for "for category." pattern
        if ' para construc' in desc or ' para mamposter' in desc or ' para pavim' in desc or \
           ' para fontan' in desc or ' para electr' in desc or ' para climat' in desc or \
           ' para carpint' in desc or ' para pintura' in desc or ' para gestion' in desc or \
           ' para matemat' in desc or ' para finan' in desc or ' para salud' in desc or \
           ' para cotid' in desc or ' para estadist' in desc or ' para cienc' in desc or \
           ' para conver' in desc or ' para deport' in desc or ' para ingenier' in desc or \
           ' para quim' in desc or ' para electr' in desc or ' para transp' in desc or \
           ' para fotogra' in desc or ' para clima' in desc or ' para utilid' in desc or \
           " pour construct" in desc or " pour mac" in desc or " pour revet" in desc or \
           " pour plomb" in desc or " pour electr" in desc or " pour climat" in desc or \
           " pour menuis" in desc or " pour peint" in desc or " pour gest" in desc or \
           " pour math" in desc or " pour finan" in desc or " pour sant" in desc or \
           " pour quoti" in desc or " pour stati" in desc or " pour scien" in desc or \
           " pour conver" in desc or " pour sport" in desc or " pour in" in desc or \
           " fur Bau" in desc or " fur Mauer" in desc or " fur Boden" in desc or \
           " fur Sanit" in desc or " fur Elektri" in desc or " fur Klima" in desc or \
           " fur Zimmer" in desc or " fur Maler" in desc or " fur Gesch" in desc or \
           " fur Math" in desc or " fur Finanz" in desc or " fur Gesund" in desc or \
           " fur Allt" in desc or " fur Stati" in desc or " fur Wiss" in desc or \
           " fur Umrec" in desc or " fur Sport" in desc or " fur Inge" in desc or \
           " fur Chemie" in desc or " fur Elek" in desc or " fur Trans" in desc or \
           " fur Foto" in desc or " fur Wissen" in desc or " fur Hilf" in desc or \
           " per costru" in desc or " per murat" in desc or " per pavim" in desc or \
           " per idrau" in desc or " per elettr" in desc or " per climat" in desc or \
           " per carpe" in desc or " per pittu" in desc or " per gesti" in desc or \
           " per matema" in desc or " per finan" in desc or " per salute" in desc or \
           " per quoti" in desc or " per stati" in desc or " per scien" in desc or \
           " per conver" in desc or " per sport" in desc or " per ingeg" in desc or \
           " per chim" in desc or " per elettr" in desc or " per tras" in desc or \
           " per foto" in desc or " per met" in desc or " per util" in desc or \
           " para construc" in desc:  # PT uses "para"
            remaining_generic.append((cid, desc[:120], len(desc)))
    
    print(f"\n{lang}: {len(remaining_generic)} 'for category' descriptions")
    for cid, desc, l in remaining_generic[:3]:
        print(f"  {cid}: {desc}... ({l}c)")