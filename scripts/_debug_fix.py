"""Debug: check why the ES fix isn't working."""
import json, re
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\calculators')
ef = d / '002' / 'es.html'
jf = d / '002' / 'es.json'

with open(jf, encoding='utf-8') as f:
    es_name = json.load(f).get('name','')
print(f'Spanish name: "{es_name}"')

content = ef.read_text(encoding='utf-8')
print(f'First 200 chars: {content[:200]}')

bold = re.search(r'\*\*([^*]+)\*\*', content)
if bold:
    bolded = bold.group(1)
    print(f'Bolded text: "{bolded}"')
    print(f'Bolded lower: "{bolded.lower()}"')
    print(f'ES name lower: "{es_name.lower()}"')
    print(f'Equal? {bolded.lower() == es_name.lower()}')
    print(f'Has Spanish chars? {any(c in bolded for c in "áéíóúñ")}')
    
    # Test the replacement
    new_content = content.replace(f'**{bolded}**', es_name, 1)
    print(f'After replace: {new_content[:200]}')
