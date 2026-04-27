"""
Optimize SEO titles for CTR. Rules:
- EN: 35-55 characters, format: "[Benefit keyword] - [What it does]" or "[What it does] Calculator"
- Other languages: 35-55 characters, same structure translated
- Remove "Formula and Calculator Online - Free Online Calculator" junk
- Google's sweet spot is 50-60 chars
"""
import json, os, re

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# Patterns to strip from titles (generic SEO junk)
JUNK_PATTERNS = [
    r'\s*[–-]\s*Formula and Calculator Online\s*[–-]\s*Free Online Calculator\s*$',
    r'\s*[–-]\s*Formule et Calcul en Ligne\s*[–-]\s*Calculatrice Gratuite en Ligne\s*$',
    r'\s*[–-]\s*Formula e Calcolo Online\s*[–-]\s*Calcolatrice Online Gratuita\s*$',
    r'\s*[–-]\s*Formel und Rechner Online\s*[–-]\s*Kostenloser Online-Rechner\s*$',
    r'\s*[–-]\s*Fórmula e Cálculo Online\s*[–-]\s*Calculadora Online Gratuita\s*$',
    r'\s*[–-]\s*F.rmula e C.lculo Online\s*[.-]\s*Calculadora .+\s*$',
    r'\s*[–-]\s*Formul.+\s*$',
    r'\s*[–-]\s*Formula .+\s*$',
    r'\s*[–-]\s*F.rmula .+\s*$',
    r'[\|–-]\s*CalcToWork\s*$',
    r'\s+[|–-]\s+Free Online Calculator\s*$',
    r'\s+[|–-]\s+Online Calculator\s*$',
    r'\s+[|–-]\s+Gratuit\s*$',
    r'\s+[|–-]\s+Gratuite\s*$',
    r'\s+[|–-]\s+Gratis\s*$',
    r'\s+[|–-]\s+Kostenlos\s*$',
]

# Specific junk endings per language (these are exact phrases to remove from the end)
JUNK_ENDINGS_ES = [
    ' – Fórmula y Cálculo Online – Calculadora Gratuita',
    ' – Fórmula y Cálculo Online',
    ' | Calculadora Online Gratuita',
    ' – Calculadora Gratuita',
    ' – Cálculo Online',
    ' – Calculadora Online',
]
JUNK_ENDINGS_FR = [
    ' – Formule et Calcul en Ligne – Calculatrice Gratuite en Ligne',
    ' – Formule et Calcul en Ligne',
    ' | Calculatrice Gratuite en Ligne',
    ' – Calculatrice Gratuite',
    ' – Calcul en Ligne',
    ' – Calculatrice Online',
]
JUNK_ENDINGS_PT = [
    ' – Fórmula e Cálculo Online – Calculadora Online Gratuita',
    ' – Fórmula e Cálculo Online',
    ' | Calculadora Online Gratuita',
    ' – Calculadora Online Gratuita',
    ' – Cálculo Online',
    ' – Calculadora Online',
]
JUNK_ENDINGS_DE = [
    ' – Formel und Rechner Online – Kostenloser Online-Rechner',
    ' – Formel und Rechner Online',
    ' | Kostenloser Online-Rechner',
    ' – Kostenloser Rechner',
    ' – Online Rechner',
    ' – Rechner Online',
]
JUNK_ENDINGS_IT = [
    ' – Formula e Calcolo Online – Calcolatrice Online Gratuita',
    ' – Formula e Calcolo Online',
    ' | Calcolatrice Online Gratuita',
    ' – Calcolatrice Online Gratuita',
    ' – Calcolo Online',
    ' – Calcolatrice Online',
]

ALL_JUNK = {
    'en': JUNK_ENDINGS_ES[:0],  # EN is already clean
    'es': JUNK_ENDINGS_ES,
    'fr': JUNK_ENDINGS_FR,
    'pt': JUNK_ENDINGS_PT,
    'de': JUNK_ENDINGS_DE,
    'it': JUNK_ENDINGS_IT,
}

total_changed = 0

for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = 0
    calcs = data['calculators']
    
    for cid, ci in calcs.items():
        title = ci.get('seo_title', '')
        new_title = title
        
        # Remove junk endings
        for junk in ALL_JUNK.get(lang, []):
            if junk in new_title:
                new_title = new_title.replace(junk, '').strip()
        
        # Also try regex patterns
        for pattern in JUNK_PATTERNS:
            new_title = re.sub(pattern, '', new_title).strip()
        
        # Remove trailing separators
        new_title = re.sub(r'\s*[|–-]\s*$', '', new_title)
        
        # Remove trailing "CalcToWork"
        new_title = re.sub(r'\s+[|–-]\s*CalcToWork\s*$', '', new_title)
        
        # Clean up multiple spaces
        new_title = re.sub(r'\s{2,}', ' ', new_title)
        new_title = new_title.strip()
        
        # Truncate to 60 chars max if still too long
        if len(new_title) > 60:
            # Find last space before 60
            truncated = new_title[:59]
            last_space = truncated.rfind(' ')
            if last_space > 30:
                new_title = truncated[:last_space]
        
        if new_title != title:
            ci['seo_title'] = new_title
            changed += 1
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    print(f"  {lang}: cleaned {changed} titles")
    total_changed += changed

print(f"\n  Total titles cleaned: {total_changed}")

# Now verify title lengths
print("\n--- TITLE LENGTH DISTRIBUTION ---")
for lang in LANGS:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) < 30)
    good = sum(1 for ci in calcs.values() if 30 <= len(ci.get('seo_title', '')) <= 60)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_title', '')) > 60)
    
    print(f"  {lang}: <30c={short}, 30-60c={good}, >60c={long}")