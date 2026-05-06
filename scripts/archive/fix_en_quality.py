#!/usr/bin/env python3
"""
fix_en_quality.py — Comprehensive English quality fixer for CalcToWork

Fixes:
  1. Spanish text → English in example_label, steps, mistakes, result_context, range_hints
  2. Missing desc (150 calculators)
  3. Missing seo_desc (379 calculators) 
  4. Missing rich content for IDs 1100-1119 (example_label, steps, mistakes, range_hints, result_context)
  5. Generic example_labels → specific ones
  6. Spanish input/output labels → English
  7. Syncs data between individual JSONs, calculators.json, and i18n/en.json

Usage: python scripts/fix_en_quality.py [--dry-run] [--target all|en_json|indiv_json|calc_json]
"""

import json
import os
import sys
import copy
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_EN = SRC / "i18n" / "en.json"
CALCS_DIR = SRC / "calculators"

# ── Language Detection ─────────────────────────────────────────────────────────

SPANISH_START_PATTERNS = [
    # Example labels
    r'^(Calcular?|Dimensionar|Ejemplo|Introduc[ei]|Pulsa|Interpreta|Calcula|Obten|Resultados?:|'
    r'El resultado|Este valor|La cifra|Los resultado|Medida t[ií]pica|Seg[úu]n)\b',
    # Steps
    r'^(Introduce|Pulsa|Interpreta|Calcula|Identifica|Estima|Asigna|Determina|Mide|Coloca|'
    r'Resta|Suma|Divide|Multiplica|Convierte|Proyecta|No considerar|Sobreestimar|Olvidar|'
    r'Calcular ROI|Dimensionar|Calcular volumen|Calcular el|Aseg[uú]rate|Verifica|Comprueba|'
    r'Recuerda|No olvides|Considera|Ten en cuenta|A[nñ]ade)\b',
    # Mistakes
    r'^(No considerar|Sobreestimar|Olvidar|Comparar|No tener|Usar|Medir|Confundir|'
    r'Calcular|Asumir|Utilizar|Redondear|Sumar|Restar|Ignorar|Pensar|Creer|Aplicar|'
    r'Elegir|Escoger|Mezclar|Pisar|Pintar|Apretar|Cortar|Colocar|Verter|Encender|'
    r'No utilizar|No medir|No comprobar|No verificar|No tener en cuenta)\b',
    # Range hints
    r'^(Valor entre|Valor|Medida t[ií]pica|Seg[úu]n|Entre)\b',
    # Result context
    r'^(Resultados?:|El resultado|Este valor|La cifra|Los resultado|Interpreta)\b',
]

# Spanish input/output label words (common Spanish terms used in labels)
SPANISH_LABEL_WORDS = [
    r'\b(Largo|Ancho|Alto|Volumen|Peso|Tiempo|Cantidad|N[uú]mero|Valor|Precio|Coste|'
    r'Superficie|[ÁA]rea|Longitud|Altura|Profundidad|Di[áa]metro|Radio|Temperatura|'
    r'Presi[óo]n|Velocidad|Masa|Densidad|Energ[ií]a|Potencia|Fuerza|Tensi[óo]n|'
    r'Corriente|Resistencia|Frecuencia|[ÁA]ngulo|Porcentaje|Tasa|Ratio|Factor|'
    r'Coeficiente|[ÍI]ndice|Grosor|Separaci[óo]n|Distancia|Ahorro|Beneficio|'
    r'Ganancia|P[ée]rdida|Consumo|Gasto|Necesario|Necesaria|Requerido|Resultado|'
    r'Desperdicio|Tablas|Filas|Metros lineales|Sacos|Arena|Grava|Cemento|'
    r'Hormig[óo]n|Ladrillo|Bloque|Mortero|Baldosa|Azulejo|Pintura|Barniz)\b'
]


def is_spanish(text: str, field_type: str = "general") -> bool:
    """Check if text appears to be Spanish rather than English."""
    if not text or not text.strip():
        return False
    text = text.strip()
    
    # Check against Spanish start patterns
    if field_type == "example_label":
        pattern = SPANISH_START_PATTERNS[0]
    elif field_type == "step":
        pattern = SPANISH_START_PATTERNS[1]
    elif field_type == "mistake":
        pattern = SPANISH_START_PATTERNS[2]
    elif field_type == "range_hint":
        pattern = SPANISH_START_PATTERNS[3]
    elif field_type == "result_context":
        pattern = SPANISH_START_PATTERNS[4]
    else:
        # General: check for accented characters + Spanish words
        has_spanish_accents = bool(re.search(r'[áéíóúñÁÉÍÓÚÑ]', text))
        has_spanish_words = bool(re.search(
            r'\b(calculadora|calcular|gratuito|sencillo|f[aá]cil|paso a paso|'
            r'introduce|pulsa|obt[ée]n|mide|anota|a[ñn]ade)\b', text, re.IGNORECASE))
        return has_spanish_accents or has_spanish_words
    
    return bool(re.search(pattern, text))


def is_spanish_label(label: str) -> bool:
    """Check if an input/output label is Spanish."""
    if not label:
        return False
    has_accents = bool(re.search(r'[áéíóúñÁÉÍÓÚÑ]', label))
    # Check for distinctly Spanish words (case-insensitive)
    spanish_patterns = [
        r'\b(porcentaje|cuenta|personas|distancia|potencia|valor)\b',
        r'\b(Volumen|Velocidad\s+(Sonido|Fuente|Avion|Angular)|Tiempo\s+Ejercicio|'
        r'Precio\s+(Accion|Compra)|Tasa\s+Impuesto|Coste\s+Variable|'
        r'Volumen\s+Gas|Masa\s+Solvente|Volumen\s+(Inicial|Final)|'
        r'Velocidad\s+Ms|Distancia|Potencia)\b'
    ]
    return has_accents or bool(re.search('|'.join(spanish_patterns), label, re.IGNORECASE))


# ── Content Generators ─────────────────────────────────────────────────────────

def generate_desc(calc: dict) -> str:
    """Generate a short description for a calculator."""
    name = calc.get("name", "")
    inputs = calc.get("inputs", {})
    outputs = calc.get("outputs", {})
    
    # Get input and output labels for context
    input_labels = [v for v in inputs.values() if isinstance(v, str)][:2]
    output_labels = [v for v in outputs.values() if isinstance(v, str)][:1]
    
    parts = [f"Free online {name.lower()}."]
    if input_labels:
        parts.append(f"Enter {' and '.join(input_labels).lower()} to get instant results.")
    elif output_labels:
        parts.append(f"Calculate {output_labels[0].lower()} instantly.")
    
    return " ".join(parts)


def generate_seo_desc(calc: dict) -> str:
    """Generate a short SEO description (120-155 chars)."""
    name = calc.get("name", "")
    inputs = calc.get("inputs", {})
    outputs = calc.get("outputs", {})
    
    # Use label values not keys
    input_vals = [v for v in inputs.values() if isinstance(v, str) and v.strip()][:2]
    output_vals = [v for v in outputs.values() if isinstance(v, str) and v.strip()][:2]
    
    if not input_vals:
        input_vals = list(inputs.keys())[:2]
    if not output_vals:
        output_vals = list(outputs.keys())[:2]
    
    templates = [
        f"Free {name.lower()}: calculate {', '.join(output_vals).lower()} from your {', '.join(input_vals).lower()}. Instant results, no sign-up required.",
        f"Use our free {name.lower()} to estimate {', '.join(output_vals).lower()} based on {', '.join(input_vals).lower()}. No registration needed.",
        f"Quick {name.lower()}: enter {', '.join(input_vals).lower()} and get {', '.join(output_vals).lower()} instantly. 100% free, no signup.",
    ]
    
    best = min(templates, key=lambda t: abs(len(t) - 140))
    return best[:160]


def generate_example_label(calc: dict) -> str:
    """Generate a specific example_label based on calc metadata."""
    name = calc.get("name", "Calculator")
    example_inputs = calc.get("example_inputs", {})
    
    if not example_inputs or isinstance(example_inputs, str):
        return f"Example calculation for {name} using the default values."
    
    input_labels = calc.get("inputs", {})
    parts = []
    for key, val in example_inputs.items():
        label = input_labels.get(key, key)
        if isinstance(label, dict):
            label = label.get("en", key)
        parts.append(f"{label} {val}")
    
    if parts:
        return f"Calculate {name.lower()} with {', '.join(parts)}."
    return f"Example calculation for {name} using the default values."


def generate_range_hint(field_id: str, field_config: dict) -> str:
    """Generate a range hint for an input field."""
    min_val = field_config.get("min", 0)
    max_val = field_config.get("max", 100)
    unit = field_config.get("unit", "")
    
    if unit:
        return f"Value between {min_val} and {max_val} {unit}."
    return f"Value between {min_val} and {max_val}."


def generate_result_context(calc: dict) -> str:
    """Generate a result_context string."""
    outputs = calc.get("outputs", {})
    output_labels = list(outputs.values())[:3]
    
    if output_labels:
        labels_str = ", ".join([f"{{{l}}}" if l in outputs else str(l) 
                               for l in output_labels[:3]])
        return f"Results: {labels_str}."
    return "Results shown below."


def generate_steps(calc: dict) -> List[str]:
    """Generate step-by-step instructions."""
    name = calc.get("name", "Calculator")
    inputs = calc.get("inputs", {})
    input_labels = list(inputs.values()) if isinstance(inputs, dict) else []
    block = calc.get("block_slug", "")
    
    steps = []
    
    # Step 1: Understand
    steps.append(f"Identify what you want to calculate with the {name}.")
    
    # Step 2-4: Enter values
    for i, label in enumerate(input_labels[:3]):
        if isinstance(label, str):
            steps.append(f"Enter the {label.lower()} in the input field.")
    
    if len(input_labels) > 3:
        steps.append(f"Fill in the remaining fields with your measurements.")
    
    # Last step
    steps.append(f"Click Calculate to see your result instantly.")
    
    # Ensure 5 steps
    while len(steps) < 5:
        steps.append(f"Review your result and adjust inputs as needed.")
    
    return steps[:6]


def generate_mistakes(calc: dict) -> List[str]:
    """Generate common mistakes for the calculator."""
    name = calc.get("name", "Calculator")
    block = calc.get("block_slug", "")
    
    # Generic mistakes that apply to most calculators
    mistakes = [
        f"Entering values in the wrong units — check that all measurements use the same unit system.",
        f"Forgetting to include a waste or safety margin — add 5-10% extra for real-world projects.",
        f"Using incorrect default values — verify the suggested defaults match your specific situation.",
        f"Rounding intermediate values too early — keep full precision until the final result.",
    ]
    
    return mistakes[:5]


# ── Loader ─────────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    # Read raw bytes and handle BOM
    with open(path, 'rb') as f:
        raw = f.read()
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]
    return json.loads(raw.decode('utf-8'))


def save_json(path: Path, data: dict, dry_run: bool = False):
    if dry_run:
        print(f"  [DRY RUN] Would save {path}")
        return
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Saved {path}")


def load_individual_jsons() -> Dict[str, dict]:
    """Load all individual calculator JSON files keyed by ID."""
    calcs = {}
    for fpath in CALCS_DIR.glob("*.json"):
        if fpath.name == "calculators.json":
            continue
        try:
            calc = load_json(fpath)
            calc_id = str(calc.get("id", ""))
            if calc_id:
                calc["_source_file"] = fpath.name
                calcs[calc_id] = calc
        except Exception as e:
            print(f"  WARNING: Could not load {fpath.name}: {e}")
    return calcs


# ── Sync: Individual JSON → calculators.json ──────────────────────────────────

def sync_calc_to_aggregate(calc_id: str, indiv_calc: dict, aggregate: dict):
    """Sync rich content fields from individual JSON to aggregate."""
    calc_list = aggregate.get("calculators", [])
    for agg_calc in calc_list:
        if str(agg_calc.get("id", "")) == calc_id:
            for field in ["example_label", "steps", "mistakes", "result_context", 
                         "range_hints", "formula_display", "example_inputs", "comparison_presets"]:
                if field in indiv_calc and indiv_calc[field]:
                    agg_calc[field] = indiv_calc[field]
            break


# ── Main Fix Logic ─────────────────────────────────────────────────────────────

def fix_calculator(calc_id: str, indiv_calc: dict, en_json_calc: dict, 
                   stats: dict) -> Tuple[dict, dict]:
    """Fix all English quality issues for one calculator.
    Returns (updated_indiv_calc, updated_en_json_calc)
    """
    en_calc = copy.deepcopy(en_json_calc) if en_json_calc else {}
    ind_calc = copy.deepcopy(indiv_calc) if indiv_calc else {}
    
    # Merge available data from both sources
    name = en_calc.get("name", "") or (ind_calc.get("i18n", {}).get("en", {}).get("name", ""))
    block_slug = ind_calc.get("block_slug", "")
    
    # Build a unified view of the calculator for content generation
    unified = {
        "name": name,
        "block_slug": block_slug,
        "inputs": en_calc.get("inputs", {}),
        "outputs": en_calc.get("outputs", {}),
        "example_inputs": ind_calc.get("example_inputs", {}),
    }
    
    # ── Fix 1: desc ──
    current_desc = en_calc.get("desc", "") or ""
    # Also fix generic "Calculator XXXX." descs
    is_generic_desc = bool(re.search(r'^Calculator\s+\d+\.', current_desc))
    if not current_desc or not current_desc.strip() or is_generic_desc:
        en_calc["desc"] = generate_desc(unified)
        stats["desc_fixed"] += 1
    
    # ── Fix 2: seo_desc ──
    if not en_calc.get("seo_desc") or not en_calc["seo_desc"].strip():
        en_calc["seo_desc"] = generate_seo_desc(unified)
        stats["seo_desc_fixed"] += 1
    
    # ── Fix 3: seo_description ──
    if not en_calc.get("seo_description") or not en_calc["seo_description"].strip():
        en_calc["seo_description"] = generate_seo_desc(unified)
        stats["seo_description_fixed"] += 1
    
    # ── Fix 4: example_label ──
    en_label = en_calc.get("example_label", "") or ""
    ind_label = ind_calc.get("example_label", "") if ind_calc else ""
    
    # Sync: if individual has a non-Spanish label but en.json doesn't, copy it
    if ind_label and not is_spanish(ind_label, "example_label") and (not en_label or is_spanish(en_label, "example_label")):
        en_calc["example_label"] = ind_label
        stats["example_label_fixed"] += 1
    elif not en_label or not en_label.strip():
        en_calc["example_label"] = generate_example_label(unified)
        if ind_calc:
            ind_calc["example_label"] = en_calc["example_label"]
        stats["example_label_fixed"] += 1
    elif is_spanish(en_label, "example_label"):
        en_calc["example_label"] = generate_example_label(unified)
        if ind_calc:
            ind_calc["example_label"] = en_calc["example_label"]
        stats["example_label_es_fixed"] += 1
    
    # ── Fix 5: steps ──
    en_steps = en_calc.get("steps") or []
    ind_steps = ind_calc.get("steps") if ind_calc else []
    current_steps = en_steps if (en_steps and len(en_steps) > 0) else ind_steps
    
    # Sync: if individual has steps but en.json doesn't, copy them
    if ind_steps and len(ind_steps) > 0 and (not en_steps or len(en_steps) == 0):
        en_calc["steps"] = list(ind_steps)
        stats["steps_fixed"] += 1
    elif not current_steps or len(current_steps) == 0:
        new_steps = generate_steps(unified)
        en_calc["steps"] = new_steps
        if ind_calc:
            ind_calc["steps"] = new_steps
        stats["steps_fixed"] += 1
    elif isinstance(current_steps, list) and len(current_steps) > 0:
        first_step = current_steps[0] if isinstance(current_steps[0], str) else ""
        if is_spanish(first_step, "step"):
            new_steps = generate_steps(unified)
            en_calc["steps"] = new_steps
            if ind_calc:
                ind_calc["steps"] = new_steps
            stats["steps_es_fixed"] += 1
    
    # ── Fix 6: mistakes ──
    en_mistakes = en_calc.get("mistakes") or []
    ind_mistakes = ind_calc.get("mistakes") if ind_calc else []
    current_mistakes = en_mistakes if (en_mistakes and len(en_mistakes) > 0) else ind_mistakes
    
    # Sync: if individual has mistakes but en.json doesn't, copy them
    if ind_mistakes and len(ind_mistakes) > 0 and (not en_mistakes or len(en_mistakes) == 0):
        en_calc["mistakes"] = list(ind_mistakes)
        stats["mistakes_fixed"] += 1
    elif not current_mistakes or len(current_mistakes) == 0:
        new_mistakes = generate_mistakes(unified)
        en_calc["mistakes"] = new_mistakes
        if ind_calc:
            ind_calc["mistakes"] = new_mistakes
        stats["mistakes_fixed"] += 1
    elif isinstance(current_mistakes, list) and len(current_mistakes) > 0:
        first_mistake = current_mistakes[0] if isinstance(current_mistakes[0], str) else ""
        if is_spanish(first_mistake, "mistake"):
            new_mistakes = generate_mistakes(unified)
            en_calc["mistakes"] = new_mistakes
            if ind_calc:
                ind_calc["mistakes"] = new_mistakes
            stats["mistakes_es_fixed"] += 1
    
    # ── Fix 7: range_hints ──
    if not en_calc.get("range_hints"):
        # Generate from individual calc's inputs
        hints = {}
        for inp in ind_calc.get("inputs", []):
            inp_id = inp.get("id", "")
            if inp_id:
                hints[inp_id] = generate_range_hint(inp_id, inp)
        if hints:
            en_calc["range_hints"] = hints
            stats["range_hints_fixed"] += 1
    elif isinstance(en_calc.get("range_hints"), dict):
        for key, val in en_calc["range_hints"].items():
            if isinstance(val, str) and is_spanish(val, "range_hint"):
                # Try to find matching input config
                for inp in ind_calc.get("inputs", []):
                    if inp.get("id") == key:
                        en_calc["range_hints"][key] = generate_range_hint(key, inp)
                        stats["range_hints_es_fixed"] += 1
                        break
    
    # ── Fix 8: result_context ──
    current_rc = en_calc.get("result_context", "") or ind_calc.get("result_context", "")
    if not current_rc or not current_rc.strip():
        en_calc["result_context"] = generate_result_context(unified)
        if ind_calc:
            ind_calc["result_context"] = en_calc["result_context"]
        stats["result_context_fixed"] += 1
    elif is_spanish(current_rc, "result_context"):
        en_calc["result_context"] = generate_result_context(unified)
        if ind_calc:
            ind_calc["result_context"] = en_calc["result_context"]
        stats["result_context_es_fixed"] += 1
    
    # ── Fix 9: formula_display ──
    if not en_calc.get("formula_display") and ind_calc.get("formula_display"):
        en_calc["formula_display"] = ind_calc["formula_display"]
        stats["formula_display_fixed"] += 1
    
    # ── Fix 10: Spanish input/output labels in i18n.en ──
    if "i18n" in ind_calc and "en" in ind_calc.get("i18n", {}):
        en_i18n = ind_calc["i18n"]["en"]
        for field in ["inputs", "outputs"]:
            if field in en_i18n:
                for key, val in list(en_i18n[field].items()):
                    if isinstance(val, str) and is_spanish_label(val):
                        # Try to construct English label from key
                        english = key.replace("_", " ").title()
                        en_i18n[field][key] = english
                        stats["label_es_fixed"] += 1
    
    return en_calc, ind_calc


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix English quality in CalcToWork")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files")
    parser.add_argument("--target", choices=["all", "en_json", "indiv_json", "calc_json"], 
                       default="all", help="What to fix")
    args = parser.parse_args()
    
    stats = {
        "desc_fixed": 0, "seo_desc_fixed": 0, "seo_description_fixed": 0,
        "example_label_fixed": 0, "example_label_es_fixed": 0,
        "steps_fixed": 0, "steps_es_fixed": 0,
        "mistakes_fixed": 0, "mistakes_es_fixed": 0,
        "range_hints_fixed": 0, "range_hints_es_fixed": 0,
        "result_context_fixed": 0, "result_context_es_fixed": 0,
        "formula_display_fixed": 0,
        "label_es_fixed": 0,
    }
    
    print("=" * 60)
    print("CalcToWork English Quality Fixer")
    print("=" * 60)
    
    # Load data
    print("\nLoading data...")
    en_json = load_json(I18N_EN)
    calc_agg = load_json(CALCS_FILE)
    indiv_calcs = load_individual_jsons()
    
    print(f"  i18n/en.json: {len(en_json.get('calculators', {}))} calculators")
    print(f"  calculators.json: {len(calc_agg.get('calculators', []))} calculators")
    print(f"  Individual JSONs: {len(indiv_calcs)} files")
    
    # ── Phase 1: Fix i18n/en.json using individual JSON data ──
    if args.target in ("all", "en_json"):
        print("\n-- Phase 1: Fixing i18n/en.json --")
        en_calcs = en_json.get("calculators", {})
        fixed_count = 0
        
        for calc_id, en_calc in list(en_calcs.items()):
            indiv_calc = indiv_calcs.get(calc_id, {})
            updated_en, updated_ind = fix_calculator(calc_id, indiv_calc, en_calc, stats)
            en_calcs[calc_id] = updated_en
            if calc_id in indiv_calcs:
                indiv_calcs[calc_id] = updated_ind
            fixed_count += 1
            
            if fixed_count % 50 == 0:
                print(f"  Processed {fixed_count} calculators...")
        
        en_json["calculators"] = en_calcs
        save_json(I18N_EN, en_json, args.dry_run)
        print(f"  Processed {fixed_count} calculators in total")
    
    # ── Phase 2: Sync individual JSONs ──
    if args.target in ("all", "indiv_json"):
        print("\n-- Phase 2: Syncing individual JSONs --")
        synced = 0
        en_calcs = en_json.get("calculators", {})
        
        for calc_id, indiv_calc in indiv_calcs.items():
            en_calc = en_calcs.get(calc_id, {})
            if not en_calc:
                continue
            
            # Sync example_label
            if not indiv_calc.get("example_label") and en_calc.get("example_label"):
                indiv_calc["example_label"] = en_calc["example_label"]
                synced += 1
            
            # Sync steps
            if (not indiv_calc.get("steps") or len(indiv_calc.get("steps", [])) == 0) \
               and en_calc.get("steps"):
                indiv_calc["steps"] = en_calc["steps"]
            
            # Sync mistakes
            if (not indiv_calc.get("mistakes") or len(indiv_calc.get("mistakes", [])) == 0) \
               and en_calc.get("mistakes"):
                indiv_calc["mistakes"] = en_calc["mistakes"]
            
            # Sync range_hints
            if not indiv_calc.get("range_hints") and en_calc.get("range_hints"):
                indiv_calc["range_hints"] = en_calc["range_hints"]
            
            # Sync result_context
            if not indiv_calc.get("result_context") and en_calc.get("result_context"):
                indiv_calc["result_context"] = en_calc["result_context"]
            
            # Sync formula_display
            if not indiv_calc.get("formula_display") and en_calc.get("formula_display"):
                indiv_calc["formula_display"] = en_calc["formula_display"]
            
            # Save individual JSON
            fname = indiv_calc.get("_source_file", "")
            if fname:
                # Remove internal key before saving
                clean = {k: v for k, v in indiv_calc.items() if not k.startswith("_")}
                fpath = CALCS_DIR / fname
                save_json(fpath, clean, args.dry_run)
        
        print(f"  Synced {synced} individual JSONs with example_labels")
    
    # ── Phase 3: Sync calculators.json aggregate ──
    if args.target in ("all", "calc_json"):
        print("\n-- Phase 3: Syncing calculators.json --")
        calc_list = calc_agg.get("calculators", [])
        synced = 0
        
        for agg_calc in calc_list:
            calc_id = str(agg_calc.get("id", ""))
            en_calc = en_json.get("calculators", {}).get(calc_id, {})
            indiv_calc = indiv_calcs.get(calc_id, {})
            
            if indiv_calc:
                for field in ["example_label", "steps", "mistakes", "result_context", 
                             "range_hints", "formula_display", "example_inputs", "comparison_presets"]:
                    if field in indiv_calc and indiv_calc[field]:
                        agg_calc[field] = indiv_calc[field]
                synced += 1
        
        save_json(CALCS_FILE, calc_agg, args.dry_run)
        print(f"  Synced {synced} calculators in aggregate")
    
    # ── Summary ──
    print("\n" + "=" * 60)
    print("FIX SUMMARY")
    print("=" * 60)
    total = sum(stats.values())
    for key, val in sorted(stats.items()):
        if val > 0:
            print(f"  {key}: {val}")
    print(f"  ---")
    print(f"  TOTAL FIXES: {total}")
    
    if args.dry_run:
        print("\n  *** DRY RUN — no files were modified ***")
    else:
        print("\n  Done! Run the build to verify:")
        print("    python scripts/generate_calctowork.py")


if __name__ == "__main__":
    main()
