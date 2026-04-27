"""Audit current SEO titles across all 6 languages."""
import json, os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    # Check title formats
    has_calculator_word = 0
    has_separator = 0
    short_titles = 0
    long_titles = 0
    
    for ci in calcs.values():
        title = ci.get('seo_title', '')
        name = ci.get('name', '')
        
        if 'Calculator' in title or 'calculator' in title.lower() or \
           'Calculadora' in title or 'Calculatrice' in title or \
           'Rechner' in title or 'Calculateur' in title or \
           'Calcolatrice' in title or 'Calcolatore' in title or \
           'Calculador' in title or 'Convertisseur' in title or \
           'Convertidor' in title or 'Conversor' in title or \
           'Umrechner' in title or 'Convertitore' in title:
            has_calculator_word += 1
        
        if ' - ' in title or ' | ' in title or ' — ' in title:
            has_separator += 1
        
        if len(title) < 30:
            short_titles += 1
        elif len(title) > 60:
            long_titles += 1
    
    print(f"\n{lang.upper()}:")
    print(f"  Total: {len(calcs)}")
    print(f"  Has 'Calculator' word: {has_calculator_word} ({has_calculator_word/len(calcs)*100:.0f}%)")
    print(f"  Has separator (- or |): {has_separator} ({has_separator/len(calcs)*100:.0f}%)")
    print(f"  Short (<30c): {short_titles}")
    print(f"  Long (>60c): {long_titles}")
    
    # Show some examples
    examples = list(calcs.items())[:5]
    for cid, ci in examples:
        title = ci.get('seo_title', '')
        name = ci.get('name', '')
        print(f"  {cid}: title='{title}' ({len(title)}c) | name='{name}'")