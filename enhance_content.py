#!/usr/bin/env python3
"""Enhance calculator content quality to match Phase 0 standards."""
import json, re, os

INPUT = os.path.join(os.path.dirname(__file__) or ".", "src/calculators/calculators.json")

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---- Domain-specific presets labels ----
PRESET_LABELS = {
    "matematicas": {
        "area": ["Triangulo 3m lado", "Cuadrado 5m lado", "Pentagono 6m lado", "Hexagono 8m lado", "Octogono 10m lado"],
        "volumen": ["Cubo pequeno", "Prisma rectangular", "Cilindro estandar", "Esfera grande", "Tanque industrial"],
        "porcentaje": ["Descuento tienda", "Incremento salarial", "Margen comercial", "Poblacion", "Macroeconomico"],
        "general": ["Caso basico", "Caso tipico", "Caso medio", "Caso avanzado", "Caso extremo"],
    },
    "finanzas": {
        "general": ["Perfil conservador", "Familia tipo", "Inversor moderado", "Inversor agresivo", "Gran patrimonio"],
    },
    "salud": {
        "general": ["Perfil sedentario", "Actividad ligera", "Actividad moderada", "Deportista", "Atleta elite"],
    },
    "deportes": {
        "general": ["Principiante", "Aficionado", "Intermedio", "Avanzado", "Profesional"],
    },
    "cotidiano": {
        "general": ["Escenario minimo", "Uso habitual", "Uso frecuente", "Uso intensivo", "Caso maximo"],
    },
    "estadistica": {
        "general": ["Muestra pequena", "Datos uniformes", "Datos dispersos", "Muestra grande", "Valores atipicos"],
    },
    "ciencia": {
        "general": ["Escala laboratorio", "Uso domestico", "Aplicacion industrial", "Ingenieria civil", "Escala cientifica"],
    },
    "conversion": {
        "general": ["Conversion minima", "Uso cotidiano", "Uso profesional", "Ingenieria", "Escala industrial"],
    },
}

def get_preset_labels(slug, block_slug, inputs):
    block_presets = PRESET_LABELS.get(block_slug, {}).get("general", ["Caso 1", "Caso 2", "Caso 3", "Caso 4", "Caso 5"])
    # Try to find more specific labels based on slug keywords
    for keyword, labels in PRESET_LABELS.get(block_slug, {}).items():
        if keyword != "general" and keyword in slug.lower():
            return labels
    return block_presets

def generate_improved_presets(calc):
    inputs = calc.get("inputs", [])
    num_inputs = [inp for inp in inputs if inp.get("type") == "number"]
    slug = calc.get("slug", "")
    block = calc.get("block_slug", "")
    
    labels = get_preset_labels(slug, block, inputs)
    presets = []
    
    multipliers = [0.4, 0.7, 1.0, 1.5, 2.5]
    for i, (label, mult) in enumerate(zip(labels, multipliers)):
        preset = {"_label": label}
        for inp in num_inputs:
            default = inp.get("default", 1) or 1
            min_v = inp.get("min", 0) or 0
            max_v = inp.get("max", 1000) or 1000
            val = round(default * mult, 2)
            # If select input, pick different options
            if inp.get("type") == "select":
                options = inp.get("options", ["opcion"])
                if isinstance(options[0], dict):
                    options = [o.get("value", o.get("label", "")) for o in options]
                preset[inp["id"]] = options[min(i, len(options)-1)]
            else:
                preset[inp["id"]] = max(float(min_v), min(float(max_v), val))
        presets.append(preset)
    return presets

def generate_improved_example_label(calc):
    slug = calc.get("slug", "").replace("-", " ")
    inputs = calc.get("inputs", [])
    num_inputs = [inp for inp in inputs if inp.get("type") == "number"]
    
    if not num_inputs:
        return f"Ejemplo de calculo para {slug}"
    
    parts = []
    for inp in num_inputs[:4]:
        default = inp.get("default", 1)
        unit = inp.get("unit", "")
        parts.append(f"{default}{unit}")
    
    return f"Ejemplo para {slug}: valores {', '.join(parts)}"

def generate_improved_range_hints(calc):
    hints = {}
    for inp in calc.get("inputs", []):
        inp_id = inp.get("id", "")
        inp_type = inp.get("type", "number")
        default = inp.get("default", 1)
        unit = inp.get("unit", "")
        min_v = inp.get("min", 0)
        max_v = inp.get("max", 500)
        
        if inp_type == "select":
            options = inp.get("options", [])
            opt_strs = [str(o) if isinstance(o, str) else str(o.get("value", str(o))) for o in options]
            hints[inp_id] = f"Opciones disponibles: {', '.join(opt_strs[:6])}"
        elif inp_type == "number":
            if unit:
                hints[inp_id] = f"Introduce el valor de {inp_id.replace('_', ' ')} ({unit}). Valor sugerido: {default}"
            else:
                hints[inp_id] = f"Introduce el valor de {inp_id.replace('_', ' ')}. Valor sugerido: {default}"
    
    return hints

# ---- Process all calculators ----
fixed = 0
for calc in data["calculators"]:
    calc_id = calc.get("id", "")
    slug = calc.get("slug", "")
    block = calc.get("block_slug", "")
    
    needs_fix = False
    
    # Fix generic comparison preset labels
    presets = calc.get("comparison_presets", [])
    if presets:
        generic_labels = ["Small scale", "Medium", "Large", "Industrial", "Theoretical",
                         "Pequeño", "Mediano", "Grande", "Muy grande", "Extremo",
                         "Caso 1", "Caso 2", "Caso 3", "Caso 4", "Caso 5"]
        has_generic = any(p.get("_label", "") in generic_labels for p in presets)
        if has_generic:
            calc["comparison_presets"] = generate_improved_presets(calc)
            needs_fix = True
    
    # Fix weak example labels
    example_label = calc.get("example_label", "")
    is_weak = (
        (example_label.startswith("Calcular para") and "×" in example_label) or
        example_label.startswith("Ejemplo de calculo para") or
        "Ejemplo de c" in example_label
    )
    # Also fix "Calcular para 1." patterns
    if is_weak or example_label == "Calcular para 1." or example_label == "":
        calc["example_label"] = generate_improved_example_label(calc)
        needs_fix = True
    
    # Fix range hints that show huge defaults
    range_hints = calc.get("range_hints", {})
    if range_hints:
        has_bad = any("1000000000000" in str(v) for v in range_hints.values())
        has_intro = any("Introduce el valor de" not in str(v) and "Seleccionar" not in str(v) and "Opciones" not in str(v) for v in range_hints.values())
        if has_bad:
            calc["range_hints"] = generate_improved_range_hints(calc)
            needs_fix = True
    
    if needs_fix:
        fixed += 1

print(f"Enhanced {fixed} calculators")

with open(INPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done")
