"""Find ALL ES content files with wrong calculator topic."""
import json, re
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')
stopwords = {'para','una','del','las','los','con','por','que','como','entre','sobre','sin','donde','más','muy','cada','todo','tipo','qué','cuál','quién','cómo','este','esta','estos','esta','fórmula','detrás','resultados','tus','funciona','cálculo','explicada','financiera','médica','física','conversión','paso'}

wrong = []
generic = []

for cdir in sorted(d.iterdir(), key=lambda x: int(x.name) if x.name.isdigit() else 9999):
    if not cdir.is_dir(): continue
    es_html = cdir / 'es.html'
    es_json = cdir / 'es.json'
    if not es_html.exists() or not es_json.exists(): continue
    
    with open(es_json, encoding='utf-8') as f:
        name = json.load(f).get('name','').lower()
    content = es_html.read_text(encoding='utf-8')
    h2 = re.search(r'<h2>(.*?)</h2>', content)
    if not h2: continue
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).lower().strip()
    
    # Get meaningful calc name words
    name_words = set()
    for w in name.split():
        w = w.strip('¿?¡!()[].,;:-«»""''')
        if len(w) > 2 and w not in stopwords and w not in ('calculadora','de','la','el','los','las','y','e','o','a','en'):
            name_words.add(w)
    
    # Get meaningful h2 words  
    h2_words = set()
    for w in h2_text.split():
        w = w.strip('¿?¡!()[].,;:-«»""''')
        if len(w) > 2 and w not in stopwords:
            h2_words.add(w)
    
    # Detect if h2 is generic template
    template_markers = ['cómo funciona el cálculo', 'cómo funciona este cálculo', 'cómo funciona la conversión',
                        'la fórmula financiera explicada', 'la fórmula médica explicada',
                        'la fórmula de física explicada', 'la fórmula explicada',
                        'la fórmula detrás de tus resultados', 'la fórmula detrás']
    is_generic = any(t in h2_text for t in template_markers)
    
    common = name_words & h2_words
    
    if not common and name_words and h2_words:
        wrong.append((cdir.name, name[:50], h2_text[:60], 'NO MATCHING KEYWORDS'))
    elif is_generic and name_words:
        generic.append((cdir.name, name[:50], h2_text[:60]))

print(f'WRONG CONTENT ({len(wrong)} files):')
print('='*80)
for cid, cname, h2t, reason in wrong:
    print(f'ID {cid}: calc="{cname}"')
    print(f'  h2="{h2t}"')
    print()

print(f'\nGENERIC TEMPLATE ({len(generic)} files):')
print('='*80)
for cid, cname, h2t in generic[:20]:
    print(f'ID {cid}: calc="{cname}" h2="{h2t}"')
if len(generic) > 20:
    print(f'  ... and {len(generic)-20} more files with generic headings')
