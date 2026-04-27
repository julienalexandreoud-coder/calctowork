"""
Fix remaining generic SEO titles across all 6 language files.
Replaces "– Formula, Calculation & Examples | CalcToWork" pattern
and other generic suffixes with unique, keyword-rich titles.
"""

import json
import os

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# SEO title templates per language
TITLE_SUFFIX = {
    "en": "– Free Online Calculator",
    "es": "– Calculadora Online Gratuita",
    "fr": "– Calculatrice Gratuite en Ligne",
    "pt": "– Calculadora Online Gratuita",
    "de": "– Kostenloser Online-Rechner",
    "it": "– Calcolatrice Online Gratuita",
}

# Patterns to replace
GENERIC_PATTERNS = [
    " – Formula, Calculation & Examples | CalcToWork",
    " – Fórmula, Cálculo y Ejemplos | CalcToWork",
    " – Formule, Calcul et Exemples | CalcToWork",
    " – Fórmula, Cálculo e Exemplos | CalcToWork",
    " – Formel, Berechnung & Beispiele | CalcToWork",
    " – Formula, Calcolo ed Esempi | CalcToWork",
    " | CalcToWork",
]


def fix_generic_titles():
    """Fix generic SEO titles across all languages."""
    for lang in LANGS:
        fpath = os.path.join(I18N_DIR, f'{lang}.json')
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        calcs = data['calculators']
        changed = 0
        
        for calc_id, entry in calcs.items():
            seo_title = entry.get('seo_title', '')
            name = entry.get('name', '')
            seo_desc = entry.get('seo_description', entry.get('seo_desc', ''))
            
            # Check for generic patterns
            is_generic = False
            clean_name = name
            
            for pattern in GENERIC_PATTERNS:
                if pattern in seo_title:
                    clean_name = seo_title.replace(pattern, '').strip()
                    is_generic = True
                    break
            
            # Also catch "X - Free Online Calculator" (batch 4 style)
            if ' - Free Online Calculator' in seo_title:
                clean_name = seo_title.replace(' - Free Online Calculator', '').strip()
                is_generic = True
            
            # Also catch lazy "Name | CalcToWork" (batch 5 style)
            if seo_title == name + ' | CalcToWork':
                is_generic = True
            
            if is_generic:
                # Create unique, keyword-rich title
                new_title = clean_name + ' ' + TITLE_SUFFIX[lang]
                entry['seo_title'] = new_title
                
                # Also fix seo_description if it's the generic template
                desc_template_suffixes = {
                    "en": "Calculate instantly and for free with CalcToWork.",
                    "es": "Calcula al instante y gratis con CalcToWork.",
                    "fr": "Calculez instantanément et gratuitement avec CalcToWork.",
                    "pt": "Calcule instantaneamente e grátis com CalcToWork.",
                    "de": "Sofort kostenlos berechnen mit CalcToWork.",
                    "it": "Calcola istantaneamente e gratuitamente con CalcToWork.",
                }
                
                # Check if description is just the generic template
                desc_suffix = desc_template_suffixes.get(lang, desc_template_suffixes['en'])
                if seo_desc.endswith(desc_suffix) or seo_desc == name + '.':
                    # Create a better description
                    desc_prefix = clean_name + '.'
                    if lang == 'en':
                        entry['seo_description'] = f"{clean_name}. Calculate instantly with step-by-step results. Free online tool by CalcToWork."
                    elif lang == 'es':
                        entry['seo_description'] = f"{clean_name}. Calcula al instante con resultados paso a paso. Herramienta gratuita de CalcToWork."
                    elif lang == 'fr':
                        entry['seo_description'] = f"{clean_name}. Calculez instantanément avec des résultats détaillés. Outil gratuit par CalcToWork."
                    elif lang == 'pt':
                        entry['seo_description'] = f"{clean_name}. Calcule instantaneamente com resultados passo a passo. Ferramenta gratuita da CalcToWork."
                    elif lang == 'de':
                        entry['seo_description'] = f"{clean_name}. Sofort berechnen mit schrittweisen Ergebnissen. Kostenloses Online-Tool von CalcToWork."
                    elif lang == 'it':
                        entry['seo_description'] = f"{clean_name}. Calcola istantaneamente con risultati dettagliati. Strumento gratuito di CalcToWork."
                    entry['seo_desc'] = entry['seo_description']
                
                changed += 1
        
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')
        
        print(f'  Fixed {changed} generic titles in {lang}.json')


if __name__ == '__main__':
    print('Fixing generic SEO titles...')
    fix_generic_titles()
    print('Done!')