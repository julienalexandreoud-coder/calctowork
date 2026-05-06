# -*- coding: utf-8 -*-
"""Deep Portuguese audit — check labels, narrative, uniqueness."""
import json, os, glob
from collections import Counter

CALC = r'C:\Microsaas\obra\src\calculators'

# 1. Check input/output labels matching Spanish
label_matches = Counter()
total_labels = 0
match_labels = 0
for fp in sorted(glob.glob(os.path.join(CALC, '*.json'))):
    if 'bak' in fp or 'monolithic' in fp: continue
    with open(fp, 'r', encoding='utf-8-sig') as f: calc = json.load(f)
    pt = calc.get('i18n', {}).get('pt', {})
    es = calc.get('i18n', {}).get('es', {})
    for io in ['inputs', 'outputs']:
        pt_io = pt.get(io, {})
        es_io = es.get(io, {})
        for k, v in pt_io.items():
            if not isinstance(v, str): continue
            total_labels += 1
            es_v = es_io.get(k, '')
            if v == es_v and v and any(c.isalpha() for c in v):
                match_labels += 1
                label_matches[v] += 1

print(f"=== INPUT/OUTPUT LABELS ===")
print(f"{match_labels}/{total_labels} PT labels still match ES")
print("Top ES-matching labels:")
for label, count in label_matches.most_common(15):
    print(f"  '{label}': {count}")

# 2. Check for clearly non-Portuguese Spanish words in narrative
print(f"\n=== NARRATIVE SPANISH WORDS ===")
BAD = ['Obtener', 'obtener', 'herramienta', 'herramientas', 'hormigon', 'hormig\u00f3n',
       'seg\u00fan', 'segun', 'donde', 'Donde', 'desperdicio', 'Desperdicio', 'merma', 'Merma']
issues = 0
word_found = Counter()
for fp in sorted(glob.glob(os.path.join(CALC, '*.json'))):
    if 'bak' in fp or 'monolithic' in fp: continue
    with open(fp, 'r', encoding='utf-8-sig') as f: calc = json.load(f)
    pt = calc.get('i18n', {}).get('pt', {})
    allt = ''
    for field in ['steps', 'mistakes']:
        val = pt.get(field, [])
        if isinstance(val, list):
            for s in val: allt += str(s) + ' '
    for field in ['result_context', 'example_label', 'formula_display']:
        v = pt.get(field, '')
        if isinstance(v, str): allt += v + ' '
    found = [p for p in BAD if p in allt]
    if found:
        issues += 1
        for p in found: word_found[p] += 1

print(f"{issues}/461 files have non-PT Spanish words")
for w, c in word_found.most_common(10):
    print(f"  '{w}': {c}")

# 3. Sample 5 files — check PT quality for all fields
print(f"\n=== SAMPLE QUALITY CHECK ===")
samples = ['hormigon-masa', 'calorias-diarias', 'interes-compuesto', 'ley-ohm', 'aceleracion']
for name in samples:
    fp = os.path.join(CALC, f'{name}.json')
    if not os.path.exists(fp):
        print(f"  {name}: NOT FOUND")
        continue
    with open(fp, 'r', encoding='utf-8-sig') as f: calc = json.load(f)
    pt = calc.get('i18n', {}).get('pt', {})
    print(f"\n  {name} (id={calc['id']})")
    print(f"    name: {pt.get('name', '?')}")
    print(f"    desc: {pt.get('description', '?')[:100]}")
    print(f"    inputs: {dict(list(pt.get('inputs', {}).items())[:3])}")
    print(f"    outputs: {pt.get('outputs', {})}")
    steps = pt.get('steps', [])
    if steps: print(f"    steps[0]: {str(steps[0])[:120]}")
    rc = pt.get('result_context', '')
    if rc: print(f"    result: {rc[:120]}")
