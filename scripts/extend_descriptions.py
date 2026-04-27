"""
Extend short DE/IT descriptions to 120-155 chars using CALC_FACTS data.
Strategy: For descriptions under 120 chars, enrich with specific calculation details
drawn from the calculator's inputs, formula, and uses.
"""
import json, os, sys, re, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.calc_content import CALC_FACTS, BLOCK_CATEGORY

I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALCS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators', 'calculators.json')
CALCS_DATA = json.load(open(CALCS_PATH, 'r', encoding='utf-8'))

LANG_CONFIG = {
    'de': {
        'suffix_map': {
            'construction': ' Berechnen Sie Materialmengen, Kosten und Abmessungen für Ihr Bauprojekt.',
            'finance': ' Berechnen Sie Renditen, Zinsen, Raten und finanzielle Kennzahlen einfach online.',
            'health': ' Ermitteln Sie Gesundheits- und Fitnesswerte schnell und kostenlos online.',
            'math': ' Lösen Sie mathematische Berechnungen schnell, genau und kostenlos online.',
            'science': ' Berechnen Sie physikalische und chemische Größen kostenlos online.',
            'conversion': ' Konvertieren Sie Einheiten schnell, genau und kostenlos online.',
            'everyday': ' Praktische Alltagsberechnungen – schnell, genau und kostenlos.',
            'sports': ' Optimieren Sie Training und sportliche Leistung mit präzisen Berechnungen.',
        },
        'verb_prefixes': ['Berechnen Sie', 'Ermitteln Sie', 'Bestimmen Sie', 'Schätzen Sie'],
    },
    'it': {
        'suffix_map': {
            'construction': ' Calcola le quantità di materiali, i costi e le dimensioni per il tuo progetto.',
            'finance': ' Calcola rendimenti, interessi, rate e indicatori finanziari facilmente online.',
            'health': ' Determina i valori di salute e fitness in modo rapido e gratuito online.',
            'math': ' Risolvi calcoli matematici in modo rapido, preciso e gratuito online.',
            'science': ' Calcola grandezze fisiche e chimiche gratuitamente online.',
            'conversion': ' Converti unità in modo rapido, preciso e gratuito online.',
            'everyday': ' Calcoli pratici per tutti i giorni – rapidi, precisi e gratuiti.',
            'sports': ' Ottimizza l\'allenamento e le prestazioni sportive con calcoli precisi.',
        },
        'verb_prefixes': ['Calcola', 'Determina', 'Stima', 'Ottieni'],
    },
}

def get_category(calc_id):
    calc = CALCS_DATA.get(calc_id, {})
    block = str(calc.get('block', ''))
    return BLOCK_CATEGORY.get(block, BLOCK_CATEGORY.get(str(int(block)) if block.isdigit() else block, 'math'))

def get_en_inputs(calc_id):
    cf = CALC_FACTS.get(calc_id, {})
    en = cf.get('en', {})
    if isinstance(en, dict) and 'ei' in en:
        return en['ei']
    return ''

total_changed = 0

for lang in ['de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    config = LANG_CONFIG[lang]
    changed = 0
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '')
        if len(desc) >= 120:
            continue
        
        cat = get_category(cid)
        suffix = config['suffix_map'].get(cat, config['suffix_map']['math'])
        
        # Strategy: append category suffix if it makes total 120-155
        new_desc = f'{desc.rstrip(".")}.{suffix}'.replace('..', '.')
        
        # If still under 120, try adding inputs info
        if len(new_desc) < 120:
            inputs = get_en_inputs(cid)
            if inputs:
                # Add input hints
                extra = f' Eingabewerte: {inputs}' if lang == 'de' else f' Valori di input: {inputs}'
                test = new_desc + extra
                if 120 <= len(test) <= 155:
                    new_desc = test
        
        # If still under 120 or over 155, just use category suffix approach with more detail
        if len(new_desc) < 120:
            # Force minimum length by repeating the core + suffix
            core = ci.get('seo_title', ci.get('name', ''))
            if lang == 'de':
                new_desc = f'{core}: {desc} {suffix.strip()}'
            else:
                new_desc = f'{core}: {desc} {suffix.strip()}'
        
        # Truncate if >155
        if len(new_desc) > 155:
            new_desc = new_desc[:154].rsplit(' ', 1)[0] + '.'
        
        if new_desc != desc and len(new_desc) >= 120:
            ci['seo_description'] = new_desc
            changed += 1
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    print(f'{lang}: extended {changed} descriptions')
    total_changed += changed

# Verify
print('\n--- DESCRIPTION LENGTH AUDIT ---')
for lang in ['de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
    good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) > 155)
    print(f'  {lang}: <120c={short}, 120-155c={good}, >155c={long}')