"""Show sample padded descriptions in non-EN languages to understand what needs fixing."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

GENERIC_PHRASES = [
    'Obten resultados al instante',
    'Herramienta gratuita con formula',
    'Calculo preciso y rapido',
    'Introduce tus valores y obtiene',
    'Calculadora facil de usar',
    'Obtenez des resultats',
    'Outil gratuit avec formule',
    'Calcul precis et rapide',
    'Entrez vos valeurs',
    'Calcule precise et rapide',
    'Calcule preciso e rapido',
    'Ferramenta gratuita',
    'Insira seus valores',
    'Sofortige Ergebnisse mit',
    'Kostenloses Online-Tool',
    'Einfacher Rechner',
    'Geben Sie Ihre Werte ein',
    'Ottieni risultati istantanei',
    'Strumento gratuito con formula',
    'Calcolo preciso e veloce',
    'Inserisci i tuoi valori',
    'Calcolatrice facile da usare',
    'Calcula al instante con resultados',
    'Calculez instantanement avec des resultats',
    'Calcule instantaneamente com resultados',
    'Sofort berechnen mit schrittweisen Ergebnissen',
    'Calcola istantaneamente con risultati dettagliati',
]

for lang in ['es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    padded = []
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        is_padded = any(p in desc for p in GENERIC_PHRASES)
        if is_padded:
            padded.append((cid, ci.get('name', ''), desc[:120], len(desc)))
    
    print(f"\n=== {lang.upper()}: {len(padded)} padded ===")
    for cid, name, desc, l in sorted(padded, key=lambda x: x[0])[:5]:
        print(f"  {cid} ({name}): {desc}... ({l}c)")