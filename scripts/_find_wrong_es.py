"""Find ES content files where h2 doesn't match calculator name."""
import json, re
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')
stopwords = {'una','una','del','las','los','con','por','que','para','como','entre','sobre','para','con','sin','entre','donde','más','muy','cada','todo','tipo','cómo','qué','cuál','quién','dónde','cuándo'}

for cdir in sorted(d.iterdir()):
    if not cdir.is_dir(): continue
    
    es_file = cdir / 'es.html'
    es_json = cdir / 'es.json'
    if not es_file.exists() or not es_json.exists(): continue
    
    with open(es_json, encoding='utf-8') as f:
        try:
            name = json.load(f).get('name','').lower()
        except:
            continue
    
    if not name: continue
    
    content = es_file.read_text(encoding='utf-8')
    h2 = re.search(r'<h2>(.*?)</h2>', content)
    if not h2: continue
    h2_text = re.sub(r'<[^>]+>', '', h2.group(1)).lower().strip()
    
    # Get meaningful words from name (exclude stopwords and 'calculadora')
    name_words = set()
    for w in name.split():
        w = w.strip('¿?¡!()[].,;:-')
        if len(w) > 2 and w not in stopwords and w != 'calculadora' and w != 'de' and w != 'la':
            name_words.add(w)
    
    # Get meaningful words from h2
    h2_words = set()
    for w in h2_text.split():
        w = w.strip('¿?¡!()[].,;:-')
        if len(w) > 2 and w not in stopwords:
            h2_words.add(w)
    
    common = name_words & h2_words
    
    if not common and name_words and h2_words:
        print(f'{cdir.name}: calc=\"{name[:60]}\"')
        print(f'  h2=\"{h2_text[:80]}\"')
        print(f'  name_words={name_words}, h2_words={h2_words}')
        print()
