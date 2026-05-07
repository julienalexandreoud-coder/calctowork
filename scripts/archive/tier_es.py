import os, re, glob, json
from collections import Counter

CONTENT_DIR = r'C:\Microsaas\obra\src\content\es'

AI_SLOP = [
    'est\u00e1 dise\u00f1ada para ayudarte',
    'Introduce los datos solicitados y obt\u00e9n',
    'Esta herramienta financiera',
    'Verifica siempre las unidades antes de calcular',
    'Compara resultados con otras fuentes',
    'Guarda tus c\u00e1lculos para referencia futura',
    'Esta herramienta es gratuita, sin registro',
    'S\u00ed, utiliza f\u00f3rmulas est\u00e1ndar',
    'funciona en todos los dispositivos',
]

tiers = {'A': [], 'B': [], 'C': []}
for cid in sorted(os.listdir(CONTENT_DIR)):
    if not cid.endswith('.html'): continue
    path = os.path.join(CONTENT_DIR, cid)
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    slop_count = sum(1 for s in AI_SLOP if s in content)
    length = len(text)
    
    if slop_count >= 4:
        tiers['C'].append(cid.replace('.html', ''))
    elif slop_count >= 2 or length < 2000:
        tiers['B'].append(cid.replace('.html', ''))
    else:
        tiers['A'].append(cid.replace('.html', ''))

print(f'Tier A (good unique): {len(tiers["A"])}')
print(f'Tier B (mixed/short): {len(tiers["B"])}')
print(f'Tier C (AI slop): {len(tiers["C"])}')
print(f'\nTier C examples: {tiers["C"][:20]}')
print(f'\nTier B first 15: {tiers["B"][:15]}')

# Show one Tier C article fully
if tiers['C']:
    cid = tiers['C'][0]
    path = os.path.join(CONTENT_DIR, f'{cid}.html')
    with open(path, 'r', encoding='utf-8') as f:
        print(f'\n=== Tier C sample: {cid} ===')
        print(f.read()[:800])
