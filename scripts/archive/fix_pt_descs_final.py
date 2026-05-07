"""
Clean approach: Read PT descriptions that are under 120 chars, and extend them properly.
No regex fixes — just append appropriate extensions.
"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
I18N = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

# First, revert the regex damage - reload from git or fix known broken patterns
fpath = os.path.join(I18N, 'pt.json')
data = json.load(open(fpath, 'r', encoding='utf-8'))
calcs = data['calculators']

# Fix broken patterns from previous regex
import re
fixes_applied = 0
for cid, ci in calcs.items():
    desc = ci.get('seo_description', '')
    # Fix "k. W" -> "kW"
    new = desc.replace('k. W', 'kW')
    # Fix ". IMC" -> " IMC" 
    new = new.replace('. IMC', ' IMC')
    # Fix ". VO" -> " VO"
    new = new.replace('. VO', ' VO')
    # Fix ". Pr" -> " Pr"  
    new = new.replace('. Pr', ' Pr')
    # Fix ". Cr" -> " Cr"
    new = new.replace('. Cr', ' Cr')
    # Fix ". MDC" -> " MDC"
    new = new.replace('. MDC', ' MDC')
    # Fix ". MMC" -> " MMC"
    new = new.replace('. MMC', ' MMC')
    # Fix ". Z" -> " Z"
    new = new.replace('. Z', ' Z')
    # Fix ". Doppler" -> " Doppler"
    new = new.replace('. Doppler', ' Doppler')
    # Fix "de. A1C" -> "de A1C"
    new = new.replace('de. A1C', 'de A1C')
    # Remove double periods
    new = new.replace('..', '.')
    # Fix missing spaces after periods if not acronym
    new = re.sub(r'\.([A-Z][a-z])', r'. \1', new)
    # Fix "sua. taxa" etc
    new = re.sub(r'([a-z])\. ([a-z])', r'\1 \2', new)
    
    if new != desc:
        ci['seo_description'] = new
        fixes_applied += 1

print(f'Fixed {fixes_applied} broken patterns')

# Now extend descriptions that are still under 120 chars
# Use HAND-WRITTEN extensions for the remaining short ones
PT_HANDWRITTEN = {
    '035': 'Calcule a potência em kW necessária para um aquecedor elétrico. Ferramenta gratuita usada por profissionais e estudantes.',
    '053': 'Calcule os BTU/h e kW necessários para climatizar seu ambiente. Calculadora fácil com resultados rápidos e precisos.',
    '086': 'Estime as horas de trabalho e o custo da limpeza final de obra. Usado por profissionais e estudantes em todo o mundo.',
    '914': 'Encontre o MDC e o MMC de dois ou mais números instantaneamente. Cálculo preciso e rápido com explicação passo a passo.',
    '917': 'Resolva triângulos retângulos: encontre lados, ângulos e área. Cálculo preciso e rápido com explicação detalhada e gratuita.',
    '919': 'Calcule área, perímetro e diagonal de um retângulo. Calculadora fácil de usar com resultados detalhados e precisos online.',
    '921': 'Calcule a área do trapézio a partir das duas bases e da altura. Calculadora fácil com resultados instantâneos e precisos.',
    '925': 'Calcule volume, área superficial e circunferência de uma esfera. Cálculo preciso e rápido com fórmulas detalhadas.',
    '931': 'Calcule seu índice cintura-altura, melhor preditor de risco que o IMC. Cálculo preciso e rápido com explicação detalhada.',
    '934': 'Converta seu salário anual em taxa horária, mensal e semanal. Cálculo preciso e gratuito com resultados detalhados.',
    '935': 'Converta sua taxa horária em salário anual, mensal e semanal. Calculadora fácil com resultados detalhados e gratuitos.',
    '936': 'Calcule as parcelas mensais da hipoteca, juros totais e amortização. Cálculo preciso e gratuito com gráfico detalhado.',
    '938': 'Calcule suas economias futuras com juros compostos. Calculadora fácil de usar com gráficos e resultados detalhados.',
    '953': 'Estime seu VO₂ máximo a partir de um tempo de corrida recente. Calculadora fácil e gratuita com resultados precisos.',
    '957': 'Calcule permutações e combinações (nPr e nCr) para qualquer n e k. Usado por profissionais e estudantes em todo o mundo.',
    '958': 'Calcule o escore Z e encontre o percentil correspondente. Calculadora fácil e gratuita com resultados rápidos e precisos.',
    '959': 'Calcule o tamanho de amostra mínimo para sua pesquisa. Calculadora fácil com resultados detalhados e precisos online.',
    '961': 'Estime sua A1C a partir dos níveis médios de glicose no sangue. Calculadora fácil e gratuita com resultados precisos e rápidos.',
    '1056': 'Calcule a mudança de frequência observada pelo efeito Doppler. Usado por profissionais e estudantes em todo o mundo.',
    '1069': 'Calcule seu ponto de equilíbrio em unidades e receitas. Usado por profissionais e estudantes em todo o mundo.',
    '1080': 'Calcule o consumo de combustível em L/100km, MPG ou km/L. Usado por profissionais e estudantes em todo o mundo.',
    '1084': 'Calcule o tempo de voo com vento contrário ou favorável. Calculadora fácil e gratuita com resultados precisos e rápidos.',
}

for cid, new_desc in PT_HANDWRITTEN.items():
    if cid in calcs:
        calcs[cid]['seo_description'] = new_desc

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# Verify
short = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) < 120)
good = sum(1 for ci in calcs.values() if 120 <= len(ci.get('seo_description', '')) <= 155)
long = sum(1 for ci in calcs.values() if len(ci.get('seo_description', '')) > 155)
print(f'\nPT final: <120c={short}, 120-155c={good}, >155c={long}')

# Spot check
for cid in ['914', '917', '053']:
    print(f'  {cid}: "{calcs[cid]["seo_description"][:80]}..." ({len(calcs[cid]["seo_description"])}c)')