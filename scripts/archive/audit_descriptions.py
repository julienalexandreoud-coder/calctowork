"""Audit current descriptions - show what they actually look like."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from calc_content import CALC_FACTS

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALC_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators')

calcs = json.load(open(os.path.join(CALC_DIR, 'calculators.json'), 'r', encoding='utf-8'))['calculators']
calc_by_id = {str(c['id']): c for c in calcs}

en = json.load(open(os.path.join(I18N_DIR, 'en.json'), 'r', encoding='utf-8'))
calcs_en = en['calculators']

# Classify descriptions
padded = []   # Has generic action phrase appended
unique = []   # Genuinely unique description
short = []    # Under 120 chars

GENERIC_PHRASES = [
    'Get instant results with step-by-step explanation.',
    'Free online tool with formula and worked examples.',
    'Accurate, fast calculation with clear methodology.',
    'Enter your values and get precise results immediately.',
    'Easy-to-use calculator with formula breakdown and tips.',
    'Obten resultados al instante',
    'Herramienta gratuita con formula',
    'Calculo preciso y rapido',
    'Introduce tus valores y obtiene',
    'Calculadora facil de usar',
    'Obtenez des resultats',
    'Outil gratuit avec formule',
    'Calcul precis et rapide',
    'Entrez vos valeurs',
    'Calcule preciso e rapido',
    'Ferramenta gratuita',
    'Insira seus valores',
    'Sofortige Ergebnisse mit',
    'Kostenloses Online-Tool',
    'Prázise, schnelle Berechnung',
    'Geben Sie Ihre Werte ein',
    'Einfacher Rechner',
    'Ottieni risultati istantanei',
    'Strumento gratuito con formula',
    'Calcolo preciso e veloce',
    'Inserisci i tuoi valori',
    'Calcolatrice facile da usare',
]

for cid, ci in sorted(calcs_en.items()):
    desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
    name = ci.get('name', '')
    
    is_padded = any(p in desc for p in GENERIC_PHRASES)
    
    if len(desc) < 120:
        short.append((cid, name, desc[:100], len(desc)))
    elif is_padded:
        padded.append((cid, name, desc[:100], len(desc)))
    else:
        unique.append((cid, name, desc[:100], len(desc)))

print(f"UNIQUE descriptions (good): {len(unique)}")
print(f"PADDED descriptions (need rewrite): {len(padded)}")
print(f"SHORT descriptions (need rewrite): {len(short)}")
print(f"TOTAL: {len(unique) + len(padded) + len(short)}")

print(f"\n--- SAMPLE PADDED (these are the problem): ---")
for cid, name, desc, l in sorted(padded, key=lambda x: x[0])[:15]:
    print(f"  {cid} ({name}): {desc}... ({l}c)")

print(f"\n--- SAMPLE SHORT: ---")
for cid, name, desc, l in sorted(short, key=lambda x: x[0])[:10]:
    print(f"  {cid} ({name}): {desc}... ({l}c)")

print(f"\n--- SAMPLE UNIQUE (these are good): ---")
for cid, name, desc, l in sorted(unique, key=lambda x: x[0])[:10]:
    print(f"  {cid} ({name}): {desc}... ({l}c)")