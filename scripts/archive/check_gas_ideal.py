import json
d = json.load(open(r'C:\Microsaas\obra\src\calculators\gas-ideal.json', encoding='utf-8'))
de = d['i18n']['de']
for k in ['example_label','range_hints','steps','mistakes','input_type_review','formula_display','result_context']:
    v = de.get(k)
    if v is not None:
        print(f'{k}: type={type(v).__name__}, len={len(str(v))}, value={repr(v)[:120]}')
    else:
        print(f'{k}: None')
