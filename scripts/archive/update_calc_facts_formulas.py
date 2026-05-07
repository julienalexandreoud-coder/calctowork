"""
Update CALC_FACTS for all newly added calculators (356 entries) to use
localized calculator names instead of slug-based formulas.
Reads the i18n files to get proper localized names and descriptions.
"""

import json
import os
import sys
import importlib

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')
LANGS = ['en', 'es', 'fr', 'pt', 'de', 'it']

# Formula templates per language - maps output description patterns to formula text
FORMULA_TEMPLATES = {
    "en": {"prefix": "", "template": "{name} = {inputs}", "result": "Result: {outputs}"},
    "es": {"prefix": "", "template": "{name} = {inputs}", "result": "Resultado: {outputs}"},
    "fr": {"prefix": "", "template": "{name} = {inputs}", "result": "Résultat : {outputs}"},
    "pt": {"prefix": "", "template": "{name} = {inputs}", "result": "Resultado: {outputs}"},
    "de": {"prefix": "", "template": "{name} = {inputs}", "result": "Ergebnis: {outputs}"},
    "it": {"prefix": "", "template": "{name} = {inputs}", "result": "Risultato: {outputs}"},
}

# Output description templates
RESULT_TEMPLATES = {
    "en": "Calculated from {n} inputs",
    "es": "Calculado a partir de {n} entradas",
    "fr": "Calculé à partir de {n} entrées",
    "pt": "Calculado a partir de {n} entradas",
    "de": "Berechnet aus {n} Eingaben",
    "it": "Calcolato da {n} input",
}


def update_calc_facts():
    """Update CALC_FACTS formulas with proper localized names."""
    # Load i18n data
    i18n_data = {}
    for lang in LANGS:
        with open(os.path.join(I18N_DIR, f'{lang}.json'), 'r', encoding='utf-8') as f:
            i18n_data[lang] = json.load(f)['calculators']
    
    # Load calculator definitions
    with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'calculators', 'calculators.json'), 'r', encoding='utf-8') as f:
        calcs = json.load(f)['calculators']
    
    # Load existing LONG_CONTENT IDs (we don't touch those)
    sys.path.insert(0, os.path.dirname(__file__))
    from calc_content import LONG_CONTENT
    existing_long = set(LONG_CONTENT.keys())
    
    # Now update the calc_content.py file
    calc_content_path = os.path.join(os.path.dirname(__file__), 'calc_content.py')
    with open(calc_content_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated = 0
    for calc in calcs:
        calc_id = str(calc['id'])
        if calc_id in existing_long:
            continue  # Don't touch LONG_CONTENT entries
        
        # Get localized names and descriptions
        for lang in LANGS:
            calc_i18n = i18n_data.get(lang, {}).get(calc_id, {})
            if not calc_i18n:
                continue
            
            name = calc_i18n.get('name', calc.get('slug', '').replace('-', ' ').title())
            desc = calc_i18n.get('desc', calc_i18n.get('description', ''))
            
            # Get input/output names
            inputs = calc.get('inputs', [])
            outputs = calc.get('outputs', [])
            
            input_names = []
            if isinstance(inputs, list):
                for inp in inputs[:4]:
                    i18n_inputs = calc_i18n.get('inputs', {})
                    label = i18n_inputs.get(inp['id'], inp['id'].replace('_', ' ').title()) if isinstance(i18n_inputs, dict) else inp['id']
                    input_names.append(label)
            elif isinstance(inputs, dict):
                for key in list(inputs.keys())[:4]:
                    input_names.append(inputs[key] if isinstance(inputs[key], str) else key)
            
            output_names = []
            if isinstance(outputs, list):
                for out in outputs[:3]:
                    i18n_outputs = calc_i18n.get('outputs', {})
                    label = i18n_outputs.get(out['id'], out['id'].replace('_', ' ').title()) if isinstance(i18n_outputs, dict) else out['id']
                    output_names.append(label)
            elif isinstance(outputs, dict):
                for key in list(outputs.keys())[:3]:
                    output_names.append(outputs[key] if isinstance(outputs[key], str) else key)
            
            # Build formula string
            if input_names:
                formula = f"{name} = f({', '.join(input_names)})"
            else:
                formula = name
            
            # Build example input
            default_vals = []
            if isinstance(inputs, list):
                for inp in inputs[:4]:
                    val = inp.get('default', 10)
                    unit = inp.get('unit', '')
                    if unit:
                        default_vals.append(f"{val} {unit}")
                    else:
                        default_vals.append(str(val))
            ei = "; ".join(default_vals) if default_vals else "enter values"
            
            # Build example output
            n_inputs = len(inputs) if isinstance(inputs, (list, dict)) else 0
            eo = RESULT_TEMPLATES[lang].format(n=n_inputs)
            if output_names:
                eo = ", ".join(output_names[:3])
            
            # Now we need to update the CALC_FACTS dict in the file
            # We'll do this by building a replacement pattern
            # The entry format in the file is: "calc_id": { "lang": { "f": "...", ... } }
            
            updated += 1
    
    # Instead of regex, let's just re-import and rewrite
    # Actually, the simplest approach: reload calc_content, modify in memory, and write back
    import importlib
    from calc_content import CALC_FACTS
    
    for calc in calcs:
        calc_id = str(calc['id'])
        if calc_id in existing_long:
            continue
        if calc_id not in CALC_FACTS:
            continue
        
        for lang in LANGS:
            calc_i18n = i18n_data.get(lang, {}).get(calc_id, {})
            if not calc_i18n:
                continue
            
            name = calc_i18n.get('name', calc.get('slug', '').replace('-', ' ').title())
            inputs = calc.get('inputs', [])
            outputs = calc.get('outputs', [])
            
            input_names = []
            if isinstance(inputs, list):
                i18n_inputs = calc_i18n.get('inputs', {})
                for inp in inputs[:4]:
                    if isinstance(i18n_inputs, dict):
                        label = i18n_inputs.get(inp['id'], inp['id'].replace('_', ' ').title())
                    else:
                        label = inp['id'].replace('_', ' ').title()
                    input_names.append(label)
            elif isinstance(inputs, dict):
                for key in list(inputs.keys())[:4]:
                    input_names.append(inputs[key] if isinstance(inputs[key], str) else key)
            
            output_labels = []
            if isinstance(outputs, list):
                i18n_outputs = calc_i18n.get('outputs', {})
                for out in outputs[:3]:
                    if isinstance(i18n_outputs, dict):
                        label = i18n_outputs.get(out['id'], out['id'].replace('_', ' ').title())
                    else:
                        label = out['id'].replace('_', ' ').title()
                    output_labels.append(label)
            elif isinstance(outputs, dict):
                for key in list(outputs.keys())[:3]:
                    output_labels.append(outputs[key] if isinstance(outputs[key], str) else key)
            
            # Build formula
            if input_names:
                formula = f"{name} = f({', '.join(input_names)})"
            else:
                formula = name
            
            # Build example input
            default_vals = []
            if isinstance(inputs, list):
                for inp in inputs[:4]:
                    val = inp.get('default', 10)
                    unit = inp.get('unit', '')
                    if unit:
                        default_vals.append(f"{val} {unit}")
                    else:
                        default_vals.append(str(val))
            ei = "; ".join(default_vals) if default_vals else "enter values"
            
            # Build example output
            eo = ", ".join(output_labels) if output_labels else RESULT_TEMPLATES[lang].format(n=len(input_names))
            
            # Update the facts
            if lang in CALC_FACTS[calc_id]:
                CALC_FACTS[calc_id][lang]['f'] = formula
                CALC_FACTS[calc_id][lang]['ei'] = ei
                CALC_FACTS[calc_id][lang]['eo'] = eo
    
    print(f"Updated {updated} CALC_FACTS entries with localized names")
    
    # Now write back to the file
    # We need to replace the CALC_FACTS dict in calc_content.py
    # Find the start and end markers
    start_marker = 'CALC_FACTS = {'
    end_pattern = '}'
    
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("ERROR: Could not find CALC_FACTS in file")
        return
    
    # Build the new CALC_FACTS content
    facts_str = json.dumps(CALC_FACTS, ensure_ascii=False, indent=4)
    # Convert to Python dict syntax (more compact)
    # Actually just use json format since that's valid Python
    
    # Find the end of CALC_FACTS by matching braces
    brace_count = 0
    in_dict = False
    end_pos = -1
    for i in range(start_pos, len(content)):
        if content[i] == '{':
            brace_count += 1
            in_dict = True
        elif content[i] == '}':
            brace_count -= 1
            if in_dict and brace_count == 0:
                end_pos = i + 1
                break
    
    if end_pos == -1:
        print("ERROR: Could not find end of CALC_FACTS")
        return
    
    new_content = content[:start_pos] + f"CALC_FACTS = {facts_str}" + content[end_pos:]
    
    with open(calc_content_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Written updated CALC_FACTS to calc_content.py")


if __name__ == '__main__':
    update_calc_facts()