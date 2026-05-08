"""Fix ES content: simple string replacement of English names with Spanish names."""
import json
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')
total = 0

for cdir in sorted(d.iterdir(), key=lambda x: int(x.name) if x.name.isdigit() else 9999):
    if not cdir.is_dir(): continue
    ef = cdir / 'es.html'
    jf = cdir / 'es.json'
    if not ef.exists() or not jf.exists(): continue
    
    with open(jf, encoding='utf-8') as f:
        try: es_name = json.load(f).get('name','')
        except: es_name = ''
    
    content = ef.read_text(encoding='utf-8')
    orig = content
    
    # Find bold/strong text and replace English calc names
    import re
    bold = re.search(r'<strong>([^<]+)</strong>', content)
    if bold:
        bolded = bold.group(1)
        if bolded.lower() != es_name.lower() and not any(c in bolded for c in 'áéíóúñ'):
            content = content.replace(f'<strong>{bolded}</strong>', es_name, 1)
    
    # Remove "Usa la" / "usa la" prefix before the name
    content = re.sub(r'(?i)(Usa la|usa la|Use la|use la)\s+', r'', content, count=1)
    
    # Fix "useful" and English see-also text
    content = content.replace('useful.', 'útiles.')
    content = content.replace('also find the', 'también puede encontrar la')
    content = content.replace('Also find the', 'También puede encontrar la')
    content = content.replace('you may also find the', 'también puede encontrar')
    content = content.replace('You may also find the', 'También puede encontrar')
    content = content.replace('you may also find', 'también puede encontrar')
    content = content.replace('You may also find', 'También puede encontrar')
    
    # Remove duplicate paragraphs
    paras = list(re.finditer(r'<p>(.*?)</p>', content, re.DOTALL))
    seen = set()
    for p in reversed(paras):
        clean = re.sub(r'<[^>]+>', '', p.group(1)).strip()
        if len(clean) > 60:
            if clean in seen:
                content = content[:p.start()] + content[p.end():]
            seen.add(clean)
    
    if content != orig:
        ef.write_text(content, encoding='utf-8')
        total += 1

print(f'Fixed {total} files')
