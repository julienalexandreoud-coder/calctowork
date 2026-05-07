import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Fix FR 938 - make it 120+
fpath = os.path.join(I18N, 'fr.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']
old = calcs['938']['seo_description']
new = 'Calculez vos économies futures avec intérêts composés. Simulateur gratuit avec résultats détaillés pour planifier votre épargne.'
calcs['938']['seo_description'] = new
print(f'fr/938: {len(new)}c')
with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# PT: check remaining short descriptions
fpath = os.path.join(I18N, 'pt.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

short = [(cid, ci['seo_description'], len(ci['seo_description'])) 
         for cid, ci in calcs.items() if len(ci.get('seo_description', '')) < 120]
print(f'\nPT short descriptions ({len(short)}):')

# Many PT descriptions seem to have missing period between sentences like "word1word2.Cálculo"
# Let me check and fix patterns like missing spaces after periods
changed = 0
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    if len(desc) < 120:
        # Fix missing period/space patterns
        import re
        fixed = re.sub(r'([a-z])([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜ])', r'\1. \2', desc)
        fixed = re.sub(r'([a-z])Cálculo', r'\1. Cálculo', desc)
        fixed = re.sub(r'([a-z])Calculadora', r'\1. Calculadora', desc)
        fixed = re.sub(r'([a-z])Usado', r'\1. Usado', desc)
        fixed = re.sub(r'([a-z])Estime', r'\1. Estime', desc)
        fixed = re.sub(r'([a-z])Resultado', r'\1. Resultado', desc)
        
        if fixed != desc and 120 <= len(fixed) <= 155:
            ci['seo_description'] = fixed
            changed += 1
        elif len(desc) < 110:
            # Add period + extension if very short  
            ext = ' Calculadora gratuita com resultados precisos e instantâneos.'
            new_desc = desc.rstrip('.') + '.' + ext if not desc.endswith('.') else desc + ext
            if 120 <= len(new_desc) <= 155:
                ci['seo_description'] = new_desc
                changed += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(f'pt: fixed {changed}')

# Final check
short = [(cid, ci['seo_description'], len(ci['seo_description'])) 
         for cid, ci in calcs.items() if len(ci.get('seo_description', '')) < 120]
print(f'PT remaining short: {len(short)}')
for cid, desc, l in short[:5]:
    print(f'  {cid}: "{desc[:80]}" ({l}c)')