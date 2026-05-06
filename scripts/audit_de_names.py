"""
Audit: Check which German calculator names/SEO fields are OK vs garbled.
"""
import json, glob, os

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
files = sorted(glob.glob(os.path.join(CALC_DIR, "*.json")))

garbled_markers = ['calcudiet', 'calcudie', 'furterminar', 'furcolocar',
                   'absonne', 'bund ', 'repristints', 'inergia',
                   'mofurrada', 'diist ', 'rechneih', 'uurrect',
                   'rderative', 'isttimation', 'bundated', 'paundmint',
                   'undear', 'percintage', 'mitsumo', 'adhistivo',
                   'incodiedo', 'imc indeich', 'colocar']

good_name = 0
bad_name = 0
good_seo = 0
bad_seo = 0
good_inputs = 0
bad_inputs = 0
good_outputs = 0
bad_outputs = 0

spanish_input_markers = ['calcular', 'ingresar', 'resultado', 'entre ']
spanish_output_markers = ['calcular', 'ingresar', 'resultado']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    de = data.get('i18n', {}).get('de', {})
    if not de:
        continue
    
    name = de.get('name', '').lower()
    seo_title = de.get('seo_title', '').lower()
    
    # Check name
    if any(m in name for m in garbled_markers):
        bad_name += 1
    else:
        good_name += 1
    
    # Check seo_title
    if any(m in seo_title for m in garbled_markers):
        bad_seo += 1
    else:
        good_seo += 1
    
    # Check inputs
    inputs = de.get('inputs', {})
    if inputs:
        input_vals = ' '.join(str(v).lower() for v in inputs.values())
        if any(m in input_vals for m in garbled_markers) or any(m in input_vals for m in spanish_input_markers):
            bad_inputs += 1
        else:
            good_inputs += 1
    
    # Check outputs
    outputs = de.get('outputs', {})
    if outputs:
        output_vals = ' '.join(str(v).lower() for v in outputs.values())
        if any(m in output_vals for m in garbled_markers) or any(m in output_vals for m in spanish_output_markers):
            bad_outputs += 1
        else:
            good_outputs += 1

print(f"Total calculators: {len(files)}")
print()
print("German name:")
print(f"  OK: {good_name}")
print(f"  BAD: {bad_name}")
print()
print("German seo_title:")
print(f"  OK: {good_seo}")
print(f"  BAD: {bad_seo}")
print()
print("German inputs:")
print(f"  OK: {good_inputs}")
print(f"  BAD: {bad_inputs}")
print()
print("German outputs:")
print(f"  OK: {good_outputs}")
print(f"  BAD: {bad_outputs}")
