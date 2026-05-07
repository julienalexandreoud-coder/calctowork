"""
FULL STRUCTURAL AUDIT of every calculator across all 6 languages.
Checks every field that appears on the live site.
"""
import json, glob, os, re
from collections import defaultdict

CALC_DIR = "src/calculators"
CONTENT_DIR = "src/content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# Spanish/garbled text indicators to detect in non-Spanish
SP_INDICATORS = {
    'de', 'el', 'la', 'los', 'las', 'del', 'un', 'una', 'por', 'para',
    'con', 'como', 'que', 'entre', 'hasta', 'desde', 'muy', 'mucho',
    'solo', 'y', 'o', 'e', 'se', 'le', 'lo', 'su', 'al', 'en', 'no',
    'es', 'son', 'tiene', 'puede', 'debe', 'hay', 'hace', 'ser', 'estar',
    'más', 'menos', 'todo', 'cada', 'otro', 'este', 'esta', 'también',
    'volumen', 'largo', 'ancho', 'altura', 'hormigón', 'cálculo', 'valor',
    'metros', 'cúbicos', 'cuadrados', 'sacos', 'arena', 'grava',
    'calcular', 'resultado', 'fórmula', 'mezcla', 'resistencia',
    'necesario', 'cimentación', 'losa', 'desperdicio', 'espesor',
    'calcular', 'calculadora', 'multiplicar', 'sumar', 'restar', 'dividir',
    'grietas', 'carga', 'causar', 'insuficiente', 'derrames', 'nivelación',
    'superficial', 'materiales', 'gratuita', 'herramienta', 'pedir',
    'medida', 'típica', 'típico', 'mínimo', 'máximo', 'ejemplo',
    'confundir', 'considerar', 'usar', 'usando', 'puede', 'debe',
    'calculo', 'calcola', 'calculado', 'calculé', 'calcolato',
    'berechnedo', 'berechnen', 'erfordert', 'richiede', 'necessite',
    'require', 'requiere', 'requer', 'nécessite',
    'estándar', 'estãodar', 'mérito', 'mériter',
}

report = defaultdict(lambda: defaultdict(list))

for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, 'r', encoding='utf-8-sig') as f:
        calc = json.load(f)
    
    cid = calc['id']
    slug = calc['slug']
    block = calc.get('block_slug', '?')
    inputs = {i['id'] for i in calc.get('inputs', [])}
    outputs = {o['id'] for o in calc.get('outputs', [])}
    i18n = calc.get('i18n', {})
    
    # Get Spanish name (source of truth for what this calculator IS)
    es_name = i18n.get('es', {}).get('name', '')
    
    for lang in LANGS:
        lang_data = i18n.get(lang, {})
        if not lang_data or not isinstance(lang_data, dict):
            report[cid][lang].append("MISSING_ENTIRE_i18n")
            continue
        
        # --- NAME check ---
        name = lang_data.get('name', '')
        if not name:
            report[cid][lang].append("EMPTY_name")
        
        # --- INPUT/OUTPUT LABELS ---
        inp_labels = lang_data.get('inputs', {})
        out_labels = lang_data.get('outputs', {})
        
        for inp_id in inputs:
            label = inp_labels.get(inp_id, '')
            if not label or len(str(label)) < 2:
                report[cid][lang].append(f"MISSING_input_label:{inp_id}")
        
        for out_id in outputs:
            label = out_labels.get(out_id, '')
            if not label or len(str(label)) < 2:
                report[cid][lang].append(f"MISSING_output_label:{out_id}")
        
        # --- SEO checks ---
        seo_title = lang_data.get('seo_title', '')
        seo_desc = lang_data.get('seo_description', '')
        if not seo_title:
            report[cid][lang].append("EMPTY_seo_title")
        elif len(seo_title) > 60:
            report[cid][lang].append("LONG_seo_title")
        if not seo_desc:
            report[cid][lang].append("EMPTY_seo_description")
        elif len(seo_desc) > 160:
            report[cid][lang].append("LONG_seo_description")
        
        # --- SPANISH TEXT in non-Spanish languages ---
        if lang != 'es':
            check_fields = ['example_label', 'result_context', 'formula_display', 'description']
            for field in check_fields:
                val = lang_data.get(field, '')
                if val and isinstance(val, str) and len(val) > 5:
                    words = set(re.findall(r'\b[a-záéíóúñü]+\b', val.lower()))
                    spanish = words & SP_INDICATORS
                    if len(spanish) >= 4:
                        report[cid][lang].append(f"SPANISH_MIX_{field}")
            
            # Check steps
            steps = lang_data.get('steps', [])
            for i, step in enumerate(steps):
                if isinstance(step, str) and len(step) > 5:
                    words = set(re.findall(r'\b[a-záéíóúñü]+\b', step.lower()))
                    spanish = words & SP_INDICATORS
                    if len(spanish) >= 3:
                        report[cid][lang].append(f"SPANISH_MIX_step_{i+1}")
                        break  # Only flag once per language
            
            # Check mistakes
            mistakes = lang_data.get('mistakes', [])
            for i, mist in enumerate(mistakes):
                if isinstance(mist, str) and len(mist) > 5:
                    words = set(re.findall(r'\b[a-záéíóúñü]+\b', mist.lower()))
                    spanish = words & SP_INDICATORS
                    if len(spanish) >= 3:
                        report[cid][lang].append(f"SPANISH_MIX_mistake_{i+1}")
                        break
            
            # Check range_hints
            hints = lang_data.get('range_hints', {})
            for hint_id, hint_text in hints.items():
                if isinstance(hint_text, str) and len(hint_text) > 5:
                    words = set(re.findall(r'\b[a-záéíóúñü]+\b', hint_text.lower()))
                    spanish = words & SP_INDICATORS
                    if len(spanish) >= 3:
                        report[cid][lang].append(f"SPANISH_MIX_hint_{hint_id}")
                        break
        
        # --- MISSING narrative fields ---
        narrative_fields = ['example_label', 'result_context', 'formula_display', 'description']
        for field in narrative_fields:
            val = lang_data.get(field, '')
            if not val or len(str(val)) < 5:
                report[cid][lang].append(f"EMPTY_{field}")

# --- CONTENT FILE CHECK ---
for lang in LANGS:
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        if "bak" in fp: continue
        with open(fp, 'r', encoding='utf-8-sig') as f:
            cid = json.load(f)['id']
        content_path = f"{CONTENT_DIR}/{lang}/{cid}.html"
        if not os.path.exists(content_path):
            report[cid][lang].append("NO_longform_content")

# ========== SUMMARY ==========
total_calcs = len(list(glob.glob(os.path.join(CALC_DIR, "*.json"))))
calcs_with_issues = len([c for c in report if any(report[c].values())])
total_issues = sum(
    len(issues) for calc_issues in report.values() 
    for issues in calc_issues.values()
)

print(f"TOTAL CALCULATORS: {total_calcs}")
print(f"WITH ISSUES: {calcs_with_issues}")
print(f"TOTAL ISSUES: {total_issues}")
print()

# Issue type breakdown
type_counts = defaultdict(int)
for calc_issues in report.values():
    for lang_issues in calc_issues.values():
        for issue in lang_issues:
            t = issue.split(':')[0] if ':' in issue else issue
            type_counts[t] += 1

print("=== ISSUE BREAKDOWN ===")
for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c}")

# Language breakdown
print("\n=== PER LANGUAGE ===")
for lang in LANGS:
    count = sum(
        len(issues.get(lang, [])) 
        for issues in report.values()
    )
    cals = sum(1 for issues in report.values() if lang in issues)
    print(f"  {lang}: {count} issues in {cals} calculators")

# Block breakdown
print("\n=== MOST AFFECTED RANGES ===")
range_counts = defaultdict(int)
for cid, calc_issues in report.items():
    for lang_issues in calc_issues.values():
        range_counts[f"{int(cid)//10*10}-{int(cid)//10*10+9}"] += len(lang_issues)
for r, c in sorted(range_counts.items(), key=lambda x: -x[1])[:15]:
    print(f"  IDs {r}: {c} issues")

# Print affected calculator IDs
print("\n=== CALCULATORS WITH ISSUES ===")
for cid in sorted(report.keys(), key=int):
    calc_issues = report[cid]
    total_c = sum(len(v) for v in calc_issues.values())
    issue_summary = []
    for lang in LANGS:
        if lang in calc_issues:
            issue_summary.append(f"{lang}:{len(calc_issues[lang])}")
    print(f"  {cid:>5} ({total_c:>3} issues)  {' | '.join(issue_summary)}")
