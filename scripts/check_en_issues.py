import json

with open(r'C:\Microsaas\obra\src\i18n\en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    calcs_def = json.load(f)

calcs = data['calculators']
calc_by_id = {c['id']: c for c in calcs_def['calculators']}

# Build formula map from calculators.json
formulas_map = {}
for c in calcs_def['calculators']:
    formulas_map[c['id']] = {
        'formula': c.get('formula', ''),
        'formula_display': c.get('formula_display', ''),
        'outputs': [o['id'] for o in c.get('outputs', [])],
        'input_ids': [i['id'] for i in c.get('inputs', [])],
    }

for cid in sorted(calcs.keys(), key=lambda x: int(x)):
    if int(cid) > 100:
        continue
    c = calcs[cid]
    
    # 1. seo_title
    title = c.get('seo_title', '')
    if len(title) < 50:
        print(f"ISSUE|{cid}|seo_title_too_short|{len(title)} chars: {title!r}")
    if len(title) > 70:
        print(f"ISSUE|{cid}|seo_title_too_long|{len(title)} chars: {title!r}")
    
    # 2. seo_desc truncation
    sd = c.get('seo_desc', '')
    if sd.endswith('and.'):
        print(f"ISSUE|{cid}|seo_desc_truncated|ends with 'and.'")
    if sd.endswith('Includes.'):
        print(f"ISSUE|{cid}|seo_desc_truncated|ends with 'Includes.'")
    if 'Calculations.' == sd[-13:]:
        print(f"ISSUE|{cid}|seo_desc_truncated|ends with 'Calculations.'")
    
    # 2b. seo_description duplicate of seo_desc
    sed = c.get('seo_description', '')
    if sed == sd and sd:
        print(f"ISSUE|{cid}|seo_description_duplicate|same as seo_desc")
    
    # 2c. desc is boilerplate
    desc = c.get('desc', '')
    if 'Free online calculator with formula, examples and step-by-step guide.' in desc:
        print(f"ISSUE|{cid}|desc_boilerplate|generic template text")
    
    # 3. formula_display mojibake
    fd_en = c.get('formula_display', '')
    if '\u00c3\u0097' in fd_en or '\u00c3' in fd_en or 'Ã' in fd_en:
        print(f"ISSUE|{cid}|formula_display_mojibake|has Ã— instead of ×")
    
    # 4. Cross-reference formula_display with calculators.json
    if cid in formulas_map:
        calc_fd = formulas_map[cid].get('formula_display', '')
        if calc_fd == 'Resultado = cÃ¡lculo segÃºn inputs' or calc_fd == 'Resultado = cálculo según inputs':
            print(f"ISSUE|{cid}|calc_formula_placeholder|calculators.json has placeholder formula: {calc_fd!r}")
        # Check if en formula uses variables not in calc outputs
        import re
        en_vars = set(re.findall(r'\{(\w+)\}', c.get('result_context', '')))
        calc_outputs = set(formulas_map[cid]['outputs'])
        missing = en_vars - calc_outputs
        if missing:
            print(f"ISSUE|{cid}|result_context_bad_vars|references non-existent outputs: {missing}")
    
    # 5. Spanish content in English i18n
    el = c.get('example_label', '')
    spanish_starts = ['Calcular ', 'calcular ', 'Calcular el ', 'Calcular la ']
    for ss in spanish_starts:
        if el.startswith(ss):
            print(f"ISSUE|{cid}|example_label_spanish|{el[:80]!r}")
            break
    
    steps = c.get('steps', [])
    if steps:
        en_count = sum(1 for s in steps if any(w in s for w in ['Calculate', 'Multiply', 'Divide', 'Apply', 'Enter', 'Convert', 'Estimate']))
        es_count = sum(1 for s in steps if any(w in s for w in ['Calcular', 'Multiplicar', 'Aplicar', 'Calcular:', 'Convertir']))
        if es_count > en_count and es_count > 0:
            print(f"ISSUE|{cid}|steps_spanish|{es_count} Spanish / {en_count} English")
    
    mistakes = c.get('mistakes', [])
    if mistakes:
        es_mistakes = sum(1 for m in mistakes if any(w in m for w in ['No ', 'Usar ', 'Omitir', 'Confundir', 'No verificar', 'No considerar', 'No prever', 'No calcular', 'No instalar', 'No colocar', 'No incluir', 'No respetar', 'No dejar', 'No usar', 'No nivelar', 'No impermeabilizar', 'No sellar', 'No humedecer', 'No comenzar']))
        if es_mistakes == len(mistakes) and es_mistakes > 0:
            print(f"ISSUE|{cid}|mistakes_all_spanish|all {es_mistakes} mistakes are in Spanish")
    
    rh = c.get('range_hints', {})
    if rh:
        spanish_words = [
            'tipic', 'minimo', 'maximo', 'segun', 'superficie',
            'longitud', 'altura', 'espesor', 'numero',
            'Dimensiones', 'Medida', 'Valor', 'Varia', 'Formatos',
        ]
        es_hints = sum(
            1 for v in rh.values()
            if any(w.lower() in v.lower() for w in spanish_words)
        )
        if es_hints > len(rh) / 2:
            print(f"ISSUE|{cid}|range_hints_spanish|{es_hints}/{len(rh)} hints in Spanish")
    
    rc = c.get('result_context', '')
    if rc and any(w in rc.lower() for w in ['se necesitan', 'se requiere', 'requiere ', 'equivalentes a', 'para una ', 'para un ', 'cada ']):
        print(f"ISSUE|{cid}|result_context_spanish|{rc[:80]!r}")
    
    # Check input_type_review reasons in Spanish
    itr = c.get('input_type_review', [])
    if itr:
        es_itr = sum(1 for r in itr if 'Correcto' in r.get('reason', '') or 'valor continuo' in r.get('reason', ''))
        if es_itr == len(itr) and es_itr > 0:
            print(f"ISSUE|{cid}|input_type_review_spanish|all {es_itr} reasons are in Spanish")
    
    # 6. Check seo_title matches calculator purpose
    name = c.get('name', '')
    if cid == '006' and 'Block' in title:
        print(f"ISSUE|{cid}|seo_title_wrong|title says 'Concrete Block' but calculator is Concrete Beam")
    if cid == '020' and 'How Many' in title:
        print(f"ISSUE|{cid}|seo_title_generic|starts with 'How Many' — could be more descriptive")
    if cid == '021' and 'How Many' in title:
        print(f"ISSUE|{cid}|seo_title_generic|starts with 'How Many' — could be more descriptive")

print("\nDone checking calculators 001-100")