import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.calc_content import CALC_FACTS, BLOCK_CATEGORY

I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALCS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators', 'calculators.json')

CALCS_DATA = json.load(open(CALCS_PATH, 'r', encoding='utf-8'))

# Category-based extension suffixes for DE
DE_SUFFIXES = {
    'construction': ' – Berechnen Sie Materialmengen und Kosten für Ihr Bauprojekt.',
    'finance': ' – Berechnen Sie Renditen, Zinsen und finanzielle Kennzahlen.',
    'health': ' – Ermitteln Sie wichtige Gesundheits- und Fitnesswerte.',
    'math': ' – Lösen Sie mathematische Berechnungen schnell und genau.',
    'science': ' – Berechnen Sie physikalische und chemische Größen.',
    'conversion': ' – Konvertieren Sie Einheiten schnell und präzise.',
    'everyday': ' – Praktische Berechnungen für den Alltag.',
    'sports': ' – Optimieren Sie Training und sportliche Leistung.',
}

# Category-based extension suffixes for IT
IT_SUFFIXES = {
    'construction': ' – Calcola le quantità di materiali e i costi del tuo progetto.',
    'finance': ' – Calcola rendimenti, interessi e indicatori finanziari.',
    'health': ' – Determina i valori importanti di salute e fitness.',
    'math': ' – Risolvi calcoli matematici in modo rapido e preciso.',
    'science': ' – Calcola grandezze fisiche e chimiche.',
    'conversion': ' – Converti unità in modo rapido e preciso.',
    'everyday': ' – Calcoli pratici per la vita di tutti i giorni.',
    'sports': ' – Ottimizza l\'allenamento e le prestazioni sportive.',
}

for lang in ['de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short_descs = [(cid, ci.get('seo_description', ''), len(ci.get('seo_description', ''))) 
                   for cid, ci in calcs.items() 
                   if len(ci.get('seo_description', '')) < 120]
    print(f'\n{lang}: {len(short_descs)} descriptions under 120 chars')
    
    # Show sample
    for cid, desc, l in short_descs[:5]:
        print(f'  {cid}: "{desc}" ({l}c)')

print()