"""
Enhance short SEO titles across all 6 languages.
Rules:
- Titles under 30 chars → expand to 35-60 chars with benefit/keyword
- Titles 30-60 chars → keep as-is
- Titles >60 chars → truncate (already done by fix_titles.py)
- Format: "[Calculator Name] – [Benefit]" or "[Calculator Name] | [Detail]"
- Use CALC_FACTS for specificity where available
"""
import json, sys, os, re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from scripts.calc_content import CALC_FACTS, BLOCK_CATEGORY

I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
CALCS_PATH = os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators', 'calculators.json')

LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# Benefit suffixes by category and language
BENEFIT_SUFFIXES = {
    'construction': {
        'en': ['Materials & Costs', 'Fast & Free', 'Estimate Materials', 'Plan Your Build', 'Accurate Estimates'],
        'es': ['Materiales y Costos', 'Rápido y Gratis', 'Calcula Materiales', 'Planifica tu Obra'],
        'fr': ['Matériaux et Coûts', 'Rapide et Gratuit', 'Estimez les Matériaux', 'Planifiez vos Travaux'],
        'pt': ['Materiais e Custos', 'Rápido e Grátis', 'Calcule Materiais', 'Planeje sua Obra'],
        'de': ['Material & Kosten', 'Schnell & Gratis', 'Material Berechnen', 'Bauplanung'],
        'it': ['Materiali e Costi', 'Veloce e Gratuito', 'Calcola Materiali', 'Pianifica i Lavori'],
    },
    'finance': {
        'en': ['Plan Your Money', 'Fast & Accurate', 'Smart Finance Tool', 'Free Online Tool', 'Easy & Accurate'],
        'es': ['Planifica tu Dinero', 'Rápido y Preciso', 'Herramienta Financiera', 'Gratis y Fácil'],
        'fr': ['Planifiez vos Finances', 'Rapide et Précis', 'Outil Financier', 'Gratuit en Ligne'],
        'pt': ['Planeje seu Dinheiro', 'Rápido e Preciso', 'Ferramenta Financeira', 'Grátis e Fácil'],
        'de': ['Finanzen Planen', 'Schnell & Präzise', 'Finanz-Tool', 'Kostenlos Online'],
        'it': ['Pianifica i Tuoi Soldi', 'Veloce e Preciso', 'Strumento Finanziario', 'Gratis Online'],
    },
    'health': {
        'en': ['Track Your Health', 'Fast & Free', 'Monitor & Plan', 'Accurate Results', 'Health Insights'],
        'es': ['Cuida tu Salud', 'Rápido y Gratis', 'Monitorea y Planifica', 'Resultados Precisos'],
        'fr': ['Suivi Santé', 'Rapide et Gratuit', 'Surveillez et Planifiez', 'Résultats Précis'],
        'pt': ['Cuide da Saúde', 'Rápido e Grátis', 'Monitore e Planeje', 'Resultados Precisos'],
        'de': ['Gesundheit Tracken', 'Schnell & Gratis', 'Monitor & Plan', 'Präzise Ergebnisse'],
        'it': ['Monitora la Salute', 'Veloce e Gratuito', 'Risultati Precisi', 'Salute e Fitness'],
    },
    'math': {
        'en': ['Free Online Tool', 'Step-by-Step', 'Fast & Accurate', 'Easy Calculator', 'Instant Results'],
        'es': ['Herramienta Gratuita', 'Paso a Paso', 'Rápido y Preciso', 'Fácil y Gratis'],
        'fr': ['Outil Gratuit', 'Étape par Étape', 'Rapide et Précis', 'Calcul Facile'],
        'pt': ['Ferramenta Grátis', 'Passo a Passo', 'Rápido e Preciso', 'Fácil e Grátis'],
        'de': ['Kostenloses Tool', 'Schritt für Schritt', 'Schnell & Präzise', 'Einfacher Rechner'],
        'it': ['Strumento Gratuito', 'Passo dopo Passo', 'Veloce e Preciso', 'Calcolo Facile'],
    },
    'science': {
        'en': ['Free & Accurate', 'Lab & Study Tool', 'Instant Results', 'Quick Calculator', 'Learn & Calculate'],
        'es': ['Gratis y Preciso', 'Para Laboratorio', 'Resultados Instantáneos', 'Aprende y Calcula'],
        'fr': ['Gratuit et Précis', 'Outil Labo', 'Résultats Instantanés', 'Apprenez et Calculez'],
        'pt': ['Grátis e Preciso', 'Para Laboratório', 'Resultados Instantâneos', 'Aprenda e Calcule'],
        'de': ['Kostenlos & Präzise', 'Für Labor & Studium', 'Sofortergebnisse', 'Lernen & Berechnen'],
        'it': ['Gratuito e Preciso', 'Per Laboratorio', 'Risultati Istantanei', 'Impara e Calcola'],
    },
    'conversion': {
        'en': ['Convert Instantly', 'Fast & Free', 'Unit Converter', 'Easy & Accurate', 'Quick Convert'],
        'es': ['Convierte al Instante', 'Rápido y Gratis', 'Conversor de Unidades', 'Fácil y Preciso'],
        'fr': ['Convertissez Instantanément', 'Rapide et Gratuit', 'Convertisseur', 'Facile et Précis'],
        'pt': ['Converta na Hora', 'Rápido e Grátis', 'Conversor de Unidades', 'Fácil e Preciso'],
        'de': ['Schnell Umrechnen', 'Schnell & Gratis', 'Einheiten-Umrechner', 'Einfach & Präzise'],
        'it': ['Converti Subito', 'Veloce e Gratuito', 'Convertitore Unità', 'Facile e Preciso'],
    },
    'everyday': {
        'en': ['Easy & Free', 'Quick Results', 'Daily Life Tool', 'Free Calculator', 'Simple & Fast'],
        'es': ['Fácil y Gratis', 'Resultados Rápidos', 'Para el Día a Día', 'Calculadora Gratuita'],
        'fr': ['Facile et Gratuit', 'Résultats Rapides', 'Pour Quotidien', 'Calculatrice Gratuite'],
        'pt': ['Fácil e Grátis', 'Resultados Rápidos', 'Para o Dia a Dia', 'Calculadora Gratuita'],
        'de': ['Einfach & Gratis', 'Schnelle Ergebnisse', 'Für den Alltag', 'Kostenlos Online'],
        'it': ['Facile e Gratuito', 'Risultati Rapidi', 'Per Ogni Giorno', 'Calcolatrice Gratis'],
    },
    'sports': {
        'en': ['Train Smarter', 'Free & Accurate', 'Performance Tool', 'Plan & Track', 'Athletic Calculator'],
        'es': ['Entrena Mejor', 'Gratis y Preciso', 'Herramienta Deportiva', 'Planifica y Registra'],
        'fr': ['Entraînez-vous Mieux', 'Gratuit et Précis', 'Outil Performance', 'Planifiez et Suivez'],
        'pt': ['Treine Melhor', 'Grátis e Preciso', 'Ferramenta Esportiva', 'Planeje e Registre'],
        'de': ['Besser Trainieren', 'Kostenlos & Präzise', 'Leistungs-Tool', 'Planen & Tracken'],
        'it': ['Allenati Meglio', 'Gratuito e Preciso', 'Strumento Sportivo', 'Pianifica e Registra'],
    },
}

# Calculator-specific benefit suffixes for EN (override generic)
SPECIFIC_EN = {
    '940': 'NPV Calculator – Investment Returns',
    '942': 'Age Calculator – Exact Age & Days',
    '944': 'Tip Calculator – Split Bills Easily',
    '321': 'APR Calculator – Real Interest Rate',
    '428': 'RMR Calculator – Resting Metabolism',
    '1000': 'pH Calculator – Acidity & Alkalinity',
    '1001': 'pOH Calculator – Hydroxide Levels',
    '954': 'Angle Converter – Degrees & Radians',
    '320': 'CAGR Calculator – Growth Rate Tool',
    '329': 'WACC Calculator – Cost of Capital',
    '426': 'TDEE Calculator – Daily Calorie Burn',
    '429': 'METs Calculator – Activity Calories',
    '911': 'Slope Calculator – Rise Over Run',
    '928': 'Macro Calculator – Track Your Macros',
    '956': 'Energy Converter – Joules & Calories',
    '916': 'Circle Calculator – Area & Circumference',
    '920': 'Square Calculator – Area & Perimeter',
    '925': 'Sphere Calculator – Volume & Surface',
    '127': 'Torque Calculator – Force & Rotation',
    '938': 'Savings Calculator – Interest & Growth',
    '936': 'Mortgage Calculator – Monthly Payment',
    '910': 'Fraction Calculator – Add & Simplify',
    '913': 'Rounding Calculator – Nearest Value',
    '961': 'A1C Estimator – Blood Sugar Average',
    '953': 'VO2 Max Estimator – Fitness Level',
    '131': 'Natural Logarithm – ln(x) Calculator',
    '138': 'Median Calculator – Find Middle Value',
    '513': 'Screen Resolution – Display Info',
    '518': 'Typing Speed Test – WPM Results',
    '422': 'BMI Prime – Weight Ratio Tool',
    '314': 'Pension Calculator – Retirement Income',
    '412': 'Sleep Calculator – Wake Up Fresh',
    '505': 'Battery Life – Runtime Estimate',
    '506': 'Download Time – Speed Estimator',
}

CALCS_DATA = json.load(open(CALCS_PATH, 'r', encoding='utf-8'))

def get_category(calc_id):
    calc = CALCS_DATA.get(calc_id, {})
    block = str(calc.get('block', ''))
    return BLOCK_CATEGORY.get(block, BLOCK_CATEGORY.get(str(int(block)) if block.isdigit() else block, 'math'))

def get_en_uses(calc_id):
    cf = CALC_FACTS.get(calc_id, {})
    en = cf.get('en', {})
    if isinstance(en, dict):
        return en.get('u', [])
    return []

total_changed = 0

for lang in LANGS:
    fpath = os.path.join(I18N, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    calcs = data['calculators']
    changed = 0
    
    for cid, ci in calcs.items():
        title = ci.get('seo_title', '')
        
        # Only enhance titles under 30 chars OR empty
        if len(title) >= 30:
            continue
        
        # For EN, try specific overrides first
        if lang == 'en' and cid in SPECIFIC_EN:
            new_title = SPECIFIC_EN[cid]
            if new_title != title:
                ci['seo_title'] = new_title
                changed += 1
                continue
        
        # Get category and benefit
        cat = get_category(cid)
        suffixes = BENEFIT_SUFFIXES.get(cat, BENEFIT_SUFFIXES['math'])
        lang_suffixes = suffixes.get(lang, suffixes.get('en', []))
        
        # Pick a suffix based on calc ID hash for consistency
        suffix_idx = hash(cid) % len(lang_suffixes)
        suffix = lang_suffixes[suffix_idx]
        
        # Apply suffix with separator
        sep = ' – '
        new_title = f'{title}{sep}{suffix}'
        
        # Truncate if >60
        if len(new_title) > 60:
            # Try shorter separator
            shorter = f'{title} | {suffix}'
            if len(shorter) <= 60:
                new_title = shorter
            else:
                # Truncate suffix
                max_suffix_len = 60 - len(title) - 3
                if max_suffix_len > 5:
                    suffix = suffix[:max_suffix_len].rsplit(' ', 1)[0]
                    new_title = f'{title}{sep}{suffix}'
                else:
                    continue
        
        if new_title != title and 30 <= len(new_title) <= 60:
            ci['seo_title'] = new_title
            changed += 1
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    print(f'  {lang}: enhanced {changed} titles')
    total_changed += changed

print(f'\n  Total titles enhanced: {total_changed}')

# Verify
print('\n--- TITLE LENGTH DISTRIBUTION AFTER ---')
for lang in LANGS:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) < 30)
    good = sum(1 for ci in calcs.values() if 30 <= len(ci.get('seo_title', '')) <= 60)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) > 60)
    print(f'  {lang}: <30c={short}, 30-60c={good}, >60c={long}')