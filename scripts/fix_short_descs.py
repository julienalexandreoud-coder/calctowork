import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# Fix FR short description - it's missing a period/space
fpath = os.path.join(I18N, 'fr.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

# Fix 938
calcs['938']['seo_description'] = 'Calculez vos économies futures avec intérêts composés. Calculatrice facile à utiliser avec des résultats précis.'

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(f'fr/938: fixed ({len(calcs["938"]["seo_description"])}c)')

# PT: fix 25 short descriptions by extending them
fpath = os.path.join(I18N, 'pt.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

PT_EXTENSIONS = {
    '002': 'Calcule cimento, areia, brita e kg de aço para concreto armado. Cálculo preciso e gratuito para engenheiros e construtores.',
    '035': 'Calcule a potência em kW necessária para um aquecedor elétrico. Usado por profissionais e estudantes em todo o mundo.',
    '053': 'Calcule os BTU/h e kW necessários para climatizar seu ambiente. Calculadora fácil com resultados instantâneos.',
    '063': 'Calcule os metros de trilho e ferragens para instalar portas de correr. Cálculo preciso e rápido com resultados detalhados.',
    '086': 'Estime as horas de trabalho e o custo da limpeza final de obra. Usado por profissionais e estudantes em todo o mundo.',
    '093': 'Calcule ISS, retenção de imposto, total da nota e valor a receber. Usado por profissionais e estudantes em todo o mundo.',
    '914': 'Encontre o MDC e o MMC de dois ou mais números instantaneamente. Cálculo preciso e rápido com explicação passo a passo.',
    '917': 'Resolva triângulos retângulos: encontre lados, ângulos e área. Cálculo preciso e rápido com explicação detalhada.',
    '919': 'Calcule área, perímetro e diagonal de um retângulo. Calculadora fácil de usar com resultados detalhados e grátis.',
}

changed = 0
for cid, new_desc in PT_EXTENSIONS.items():
    old = calcs[cid].get('seo_description', '')
    if old != new_desc and len(new_desc) >= 120:
        calcs[cid]['seo_description'] = new_desc
        changed += 1

# For the remaining ~17 short PT descriptions, add a period and generic extension
pt_suffix = ' Usado por profissionais e estudantes em todo o Brasil.'
pt_suffix2 = ' Calculadora gratuita com resultados precisos e instantâneos.'

for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    if len(desc) < 120 and cid not in PT_EXTENSIONS:
        # Try adding suffix
        new_desc = desc.rstrip('.') + '.' + pt_suffix
        if 120 <= len(new_desc) <= 155:
            ci['seo_description'] = new_desc
            changed += 1
        else:
            new_desc = desc.rstrip('.') + '.' + pt_suffix2
            if 120 <= len(new_desc) <= 155:
                ci['seo_description'] = new_desc
                changed += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Verify
print(f'pt: fixed {changed} descriptions')

# Final audit
for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N, f'{lang}.json')
    data = json.load(open(fpath, 'r', encoding='utf-8'))
    calcs = data['calculators']
    short = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
    good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
    long = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) > 155)
    print(f'  {lang}: <120c={short}, 120-155c={good}, >155c={long}')