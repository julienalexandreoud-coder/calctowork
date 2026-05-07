"""Cross-check: for each calculator, read the formula + inputs/outputs to determine what it ACTUALLY does, then verify name matches."""
import json, glob

# Read a few key calculators to understand patterns
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = int(d['id'])
    if cid <= 15 or (300 <= cid <= 340) or (500 <= cid <= 522) or cid in (910,911,912,913,914,915,916,1000,1001,1002,1100,1101,1102):
        slug = d['slug']
        formula = d.get('formula','')
        inputs = [(i['id'],i.get('unit','')) for i in d.get('inputs',[])]
        outputs = [(o['id'],o.get('unit','')) for o in d.get('outputs',[])]
        es_name = d.get('i18n',{}).get('es',{}).get('name','')
        en_name = d.get('i18n',{}).get('en',{}).get('name','')
        
        # Extract key formula terms
        import re
        returns = re.findall(r'return\s*\{([^}]+)\}', formula)
        calculates = returns[0] if returns else '?'
        
        print(f'\n=== {cid} [{slug}] ===')
        print(f'  ES name: {es_name}')
        print(f'  EN name: {en_name}')
        print(f'  Inputs:  {inputs[:5]}')
        print(f'  Outputs: {outputs[:5]}')
        print(f'  Formula calculates: {calculates[:120]}')
