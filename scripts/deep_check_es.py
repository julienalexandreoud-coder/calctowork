"""Deep check: read ES content files and compare to calculator definition."""
import json, re
from pathlib import Path

base = Path(r'C:\Microsaas\obra')
calcs_dir = base / 'src' / 'calculators'
content_dir = base / 'src' / 'content' / 'es'

# Check specific IDs that were known to have wrong content before
check_ids = ['001', '004', '015', '028', '043', '078', '087', '100', '200', '300', '400', '401', '402', '410', '500', '600', '700', '800', '804', '900', '951', '1000', '1028', '1050', '1104']

print('Deep checking ES content files...\n')
for cid in check_ids:
    es_file = content_dir / f'{cid}.html'
    calc_dir = calcs_dir / cid
    if not es_file.exists() or not calc_dir.exists():
        continue
    
    # Get calculator name and description from ES
    es_json = calc_dir / 'es.json'
    calc_json = calc_dir / 'calc.json'
    
    calc_name = ''
    calc_desc = ''
    formula = ''
    if es_json.exists():
        with open(es_json, encoding='utf-8') as f:
            i18n = json.load(f)
        calc_name = i18n.get('name', '')
        calc_desc = i18n.get('description', '')
    
    inputs = []
    outputs = []
    if calc_json.exists():
        with open(calc_json, encoding='utf-8') as f:
            cd = json.load(f)
        inputs = [i.get('id','') for i in cd.get('inputs',[])]
        outputs = [o.get('id','') for o in cd.get('outputs',[])]
    
    # Read ES content body
    content = es_file.read_text(encoding='utf-8')
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Check if content body mentions calculator-specific terms
    body = text[:500].lower()
    calc_words = set(w.lower() for w in calc_name.split() if len(w) > 3)
    
    # Strong indicators of content being about a DIFFERENT calculator
    wrong_indicators = []
    
    if 'tubería' in body and 'hormigón' in calc_name:
        wrong_indicators.append('pipe content in concrete calc')
    if 'interés compuesto' in body and 'hipoteca' in calc_name:
        wrong_indicators.append('compound interest in mortgage')
    if 'caloría' in body and 'imc' in calc_name:
        wrong_indicators.append('calorie content in BMI calc')
    if 'peso molecular' in body and 'área' in calc_name:
        wrong_indicators.append('molecular weight in area calc')
    if 'propina' in body and 'edad' in calc_name:
        wrong_indicators.append('tip content in age calc')
    
    # Check first h2
    h2 = re.search(r'<h[12]>(.*?)</h[12]>', content)
    h2_text = h2.group(1) if h2 else '(no h2)'
    
    status = 'WRONG' if wrong_indicators else 'OK'
    if wrong_indicators:
        print(f'ID {cid}: {calc_name[:50]}')
        print(f'  Content h2: {h2_text[:80]}')
        for w in wrong_indicators:
            print(f'  ISSUE: {w}')
        print(f'  Body start: {body[:150]}')
        print()
