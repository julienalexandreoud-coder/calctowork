"""
Fix PT descriptions that have missing period+space between sentences.
Pattern: lowercase followed by uppercase without period+space.
Then extend any descriptions still under 120 chars.
"""
import json, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

fpath = os.path.join(I18N, 'pt.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

changed = 0
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    if len(desc) >= 120:
        continue
    
    # Fix missing period between sentences: "wordWord" -> "word. Word"
    fixed = re.sub(r'([a-zãâáàéêíïóõúü])\s*([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜ])', r'\1. \2', desc)
    # Also fix "wordCalc" pattern (missing space+period)
    fixed = re.sub(r'([a-zà-ü])((?:Calculadora|Cálculo|Estime|Usado|Resultado|Encontre|Resolva|Calcule|Simule|Determine|Obtenha|Converta))', r'\1. \2', fixed)
    # Fix missing space after period: "word.another" -> "word. another"
    fixed = re.sub(r'\.(\S)', r'. \1', fixed)
    # Fix double spaces
    fixed = re.sub(r'  +', ' ', fixed)
    
    if fixed != desc:
        ci['seo_description'] = fixed
        changed += 1
        print(f'  {cid}: {len(desc)}c -> {len(fixed)}c: "{fixed[:80]}..."')

print(f'\nFixed {changed} descriptions')

# Now check remaining short ones
short = [(cid, ci['seo_description'], len(ci['seo_description'])) 
         for cid, ci in calcs.items() if len(ci.get('seo_description', '')) < 120]
print(f'Remaining short: {len(short)}')

# Extend remaining short descriptions
PT_EXT = {
    0: ' Calculadora gratuita com resultados precisos e instantâneos.',
    1: ' Usado por profissionais e estudantes em todo o Brasil.',
    2: ' Ferramenta online gratuita com cálculos detalhados passo a passo.',
}

ext_idx = 0
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    if len(desc) < 120:
        ext = PT_EXT[ext_idx % len(PT_EXT)]
        new_desc = desc.rstrip('.') + '.' + ext
        if 120 <= len(new_desc) <= 155:
            ci['seo_description'] = new_desc
            ext_idx += 1
        else:
            # Try shorter extension
            short_ext = ' Gratuito online com resultados precisos.'
            new_desc = desc.rstrip('.') + '.' + short_ext
            if 120 <= len(new_desc) <= 155:
                ci['seo_description'] = new_desc
                ext_idx += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Final audit
short = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
long = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) > 155)
print(f'\nPT final: <120c={short}, 120-155c={good}, >155c={long}')

# Also check all other langs
for lang in ['en', 'es', 'fr', 'de', 'it']:
    fpath2 = os.path.join(I18N, f'{lang}.json')
    data2 = json.load(open(fpath2, 'r', encoding='utf-8'))
    calcs2 = data2['calculators']
    s = sum(1 for ci in calcs2.values() if len(ci.get('seo_description', '')) < 120)
    g = sum(1 for ci in calcs2.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
    l = sum(1 for ci in calcs2.values() if len(ci.get('seo_description', '')) > 155)
    print(f'  {lang}: <120c={s}, 120-155c={g}, >155c={l}')