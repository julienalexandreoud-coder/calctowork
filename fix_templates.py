#!/usr/bin/env python3
"""Fix template content in all calculators with generic steps/mistakes/formula_display."""
import json, re, math, random

random.seed(42)

INPUT = "src/calculators/calculators.json"

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

TEMPLATE_STEPS_FIRST = "Identificar los valores de entrada"
TEMPLATE_MISTAKES_FIRST = "No verificar las medidas antes de calcular"
TEMPLATE_FORMULA = "Resultado = cálculo según inputs"

# --- Knowledge base per block ---
BLOCK_DOMAIN = {
    "matematicas": "matemático",
    "finanzas": "financiero",
    "salud": "de salud",
    "cotidiano": "cotidiano",
    "estadistica": "estadístico",
    "ciencia": "científico",
    "conversion": "de conversión de unidades",
    "deportes": "deportivo",
    "estructuras": "de construcción",
    "mamposteria": "de construcción",
    "pavimentos": "de construcción",
    "fontaneria": "de fontanería",
    "electricidad": "eléctrico",
    "climatizacion": "de climatización",
    "carpinteria": "de carpintería",
    "pintura": "de pintura",
    "gestion": "de gestión de obra",
    "quimica": "químico",
    "electronica": "electrónico",
    "transporte": "de transporte",
    "fotografia": "fotográfico",
    "clima": "meteorológico",
    "utilidades": "informático",
    "ingenieria": "de ingeniería",
}

MISTAKE_PATTERNS = {
    "matematicas": [
        "Confundir la fórmula con la de otra figura geométrica similar",
        "Usar el radio en lugar del diámetro (o viceversa) en la fórmula",
        "No verificar que las unidades sean consistentes antes de operar",
        "Redondear resultados intermedios perdiendo precisión en el resultado final",
        "Aplicar una fórmula lineal a un problema que requiere operación cuadrática o cúbica",
        "Olvidar el orden correcto de las operaciones al calcular manualmente",
        "Confundir área con perímetro o volumen con área superficial",
        "No considerar restricciones del dominio (raíces negativas, división por cero)",
        "Usar grados en lugar de radianes en funciones trigonométricas",
        "Interpretar un resultado intermedio como el resultado final del cálculo",
    ],
    "finanzas": [
        "No comparar la TAE entre distintas ofertas antes de contratar",
        "Confundir interés simple con interés compuesto en inversiones a largo plazo",
        "Olvidar incluir comisiones y gastos en el cálculo del coste total",
        "Usar el tipo de interés nominal en lugar del efectivo (TAE)",
        "No considerar la inflación al calcular la rentabilidad real de una inversión",
        "Subestimar el impacto de los impuestos sobre el rendimiento neto",
        "Asumir que una cuota mensual baja significa un préstamo más barato",
        "No verificar si el interés es fijo o variable antes de comprometerse",
        "Calcular el IVA sobre un importe que ya lo incluye",
        "Olvidar que el plazo afecta enormemente al coste total del préstamo",
    ],
    "salud": [
        "Medir el peso con ropa y zapatos (añade 1-3 kg al resultado real)",
        "Usar unidades incorrectas: libras en lugar de kg o pulgadas en lugar de cm",
        "Interpretar el IMC como medida de grasa corporal (no distingue músculo de grasa)",
        "Comparar resultados con tablas de población general sin considerar edad o género",
        "No tener en cuenta que la hidratación y la hora del día afectan a las mediciones",
        "Usar fórmulas para adultos en niños o adolescentes",
        "Confundir frecuencia cardíaca máxima con frecuencia cardíaca de entrenamiento",
        "Asumir que todas las calorías tienen el mismo efecto metabólico",
        "No ajustar la ingesta calórica al cambiar el nivel de actividad física",
        "Autodiagnosticarse basándose solo en el resultado de una calculadora",
    ],
    "ciencia": [
        "Mezclar unidades de diferentes sistemas (métrico con imperial) sin convertir",
        "Usar la temperatura en Celsius en fórmulas que requieren Kelvin (sumar 273.15)",
        "Confundir masa (kg) con peso (N) en cálculos de física",
        "Olvidar que las constantes físicas tienen unidades específicas",
        "Aplicar una fórmula de mecánica clásica a velocidades relativistas",
        "No considerar la resistencia del aire en problemas de movimiento",
        "Usar valores de presión en unidades incorrectas (bar vs Pa vs atm)",
        "Confundir velocidad media con velocidad instantánea",
        "No verificar las condiciones de contorno de la fórmula (ej: gas ideal solo a bajas presiones)",
        "Asumir que la aceleración es constante cuando no lo es",
    ],
    "conversion": [
        "Confundir el factor de conversión (multiplicar cuando hay que dividir o viceversa)",
        "Usar el factor de conversión de una unidad similar pero incorrecta",
        "No verificar si la conversión es lineal o requiere un ajuste (ej: temperatura)",
        "Acumular errores de redondeo en conversiones encadenadas",
        "Olvidar que algunas conversiones dependen del contexto (galón US vs UK)",
    ],
    "deportes": [
        "Confundir ritmo (min/km) con velocidad (km/h)",
        "No considerar el desnivel del terreno en el cálculo de ritmo",
        "Usar el peso corporal total en lugar de la masa magra para calcular gasto calórico",
        "Olvidar que el viento y la temperatura afectan al rendimiento",
        "Comparar marcas en diferentes distancias sin ajustar por el factor de fatiga",
    ],
    "cotidiano": [
        "No considerar si la propina se calcula antes o después de impuestos",
        "Olvidar que los meses tienen diferente número de días",
        "Usar el formato de fecha incorrecto (MM/DD vs DD/MM) al introducir datos",
        "Confundir horas decimales (1.5h) con formato horas:minutos (1:30)",
        "No verificar la zona horaria al calcular diferencias de tiempo entre países",
    ],
    "estadistica": [
        "Confundir media con mediana en distribuciones asimétricas",
        "Usar la desviación estándar de la muestra (n-1) para datos de población (n)",
        "Interpretar correlación como causalidad",
        "No verificar la normalidad de los datos antes de aplicar pruebas paramétricas",
        "Seleccionar un tamaño de muestra insuficiente para detectar el efecto deseado",
    ],
    "electricidad": [
        "No calcular la sección del cable por los tres criterios: térmico, caída de tensión y cortocircuito",
        "Usar cable unipolar donde se requiere multipolar o viceversa",
        "Olvidar que la potencia trifásica incluye el factor √3",
    ],
    "fontaneria": [
        "No respetar la pendiente mínima del 2% en tuberías de saneamiento",
        "Usar tubería de pared delgada para instalaciones enterradas",
        "No instalar válvulas de corte en puntos clave de la instalación",
    ],
    "climatizacion": [
        "Sobredimensionar el equipo (provoca ciclos cortos que reducen la eficiencia)",
        "No limpiar los filtros regularmente (reduce el caudal hasta un 30%)",
        "Instalar la unidad exterior en un lugar sin ventilación adecuada",
    ],
    "quimica": [
        "Confundir masa molar (g/mol) con masa molecular (uma)",
        "Olvidar balancear la ecuación química antes de hacer cálculos estequiométricos",
        "Usar concentración en lugar de actividad en cálculos de equilibrio",
    ],
    "electronica": [
        "Confundir resistencia en serie (suma) con resistencia en paralelo (inversa de sumas de inversas)",
        "No verificar la potencia máxima que puede disipar un componente",
        "Usar el código de colores de 4 bandas para resistencias de 5 bandas",
    ],
    "transporte": [
        "Usar litros y millas sin convertir unidades (1 galón US = 3.785 L)",
        "No considerar que el consumo urbano puede ser hasta un 50% mayor que el extraurbano",
        "Olvidar que la presión de neumáticos debe medirse en frío",
    ],
    "fotografia": [
        "Confundir la distancia hiperfocal con la profundidad de campo",
        "Olvidar que el factor de recorte del sensor afecta a la profundidad de campo",
        "Usar ISO muy alto innecesariamente (introduce ruido digital)",
    ],
}

# Common mistakes for any generic domain
GENERIC_MISTAKES = [
    "Introducir valores con unidades incorrectas sin verificar la conversión",
    "Redondear resultados intermedios en lugar del resultado final",
    "No verificar que el resultado tiene sentido físico o lógico en el contexto del problema",
]

def get_domain_mistakes(block_slug):
    """Get 3 domain-specific mistakes."""
    domain = BLOCK_DOMAIN.get(block_slug, "")
    mistakes_pool = MISTAKE_PATTERNS.get(block_slug, GENERIC_MISTAKES)
    # Pick 3 diverse ones
    selected = []
    for m in mistakes_pool:
        if m not in selected:
            selected.append(m)
        if len(selected) >= 3:
            break
    if len(selected) < 3:
        selected += GENERIC_MISTAKES[:3 - len(selected)]
    return selected[:3]

def generate_steps(calc):
    """Generate 5 calculation steps based on formula and inputs."""
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    block = calc.get("block_slug", "")
    
    input_names = [inp.get("id", "") for inp in inputs]
    output_names = [out.get("id", "") for out in outputs]
    input_labels = [inp.get("label", inp.get("id", "")) for inp in inputs]
    formula_str = calc.get("formula", "")
    
    steps = []
    
    # Step 1: Identify inputs
    if len(input_names) >= 3:
        steps.append(f"Introducir los valores de {', '.join(input_labels[:-1])} y {input_labels[-1]}")
    elif len(input_names) == 2:
        steps.append(f"Introducir los valores de {input_labels[0]} y {input_labels[1]}")
    elif len(input_names) == 1:
        steps.append(f"Introducir el valor de {input_labels[0]}")
    else:
        steps.append("Identificar los valores necesarios para el cálculo")
    
    # Step 2: Check/convert units
    unit_inputs = [inp for inp in inputs if inp.get("unit_options")]
    if unit_inputs:
        ui = unit_inputs[0]
        steps.append(f"Verificar que las unidades sean correctas y convertir si es necesario ({', '.join(ui.get('unit_options', [])[:3])})")
    else:
        steps.append("Verificar que los valores introducidos están en el rango y formato correctos")
    
    # Step 3: Apply formula/core operation
    formula_display = calc.get("formula_display", "")
    if formula_display and formula_display != TEMPLATE_FORMULA:
        steps.append(f"Aplicar la fórmula: {formula_display}")
    elif len(output_names) == 1:
        steps.append(f"Realizar el cálculo para obtener {output_names[0].replace('_', ' ')}")
    elif len(output_names) >= 2:
        steps.append(f"Calcular los valores de {output_names[0].replace('_', ' ')} y {output_names[1].replace('_', ' ')}")
    else:
        steps.append("Realizar la operación matemática correspondiente")
    
    # Step 4: Verify
    unit = outputs[0].get("unit", "") if outputs else ""
    if unit:
        steps.append(f"El resultado se expresa en {unit}. Verificar que la magnitud es coherente")
    else:
        steps.append("Verificar que el resultado es coherente con los valores de entrada")
    
    # Step 5: Interpret/apply
    if block in ("salud", "deportes"):
        steps.append("Comparar el resultado con los valores de referencia para interpretar su significado")
    elif block in ("finanzas",):
        steps.append("Utilizar el resultado para tomar decisiones informadas sobre tu planificación financiera")
    elif block in ("matematicas", "estadistica"):
        steps.append("El resultado puede usarse como dato intermedio para cálculos posteriores más complejos")
    elif block in ("ciencia", "quimica", "electronica"):
        steps.append("Documentar el resultado con sus unidades para usarlo en cálculos de ingeniería posteriores")
    else:
        steps.append("Utilizar el resultado para la aplicación práctica correspondiente")
    
    return steps

def generate_formula_display(calc):
    """Generate a proper formula_display from the actual formula."""
    formula_str = calc.get("formula", "")
    if not formula_str or len(formula_str) < 5:
        return calc.get("formula_display", TEMPLATE_FORMULA)
    
    inputs = {inp["id"]: inp for inp in calc.get("inputs", [])}
    outputs = {out["id"]: out for out in calc.get("outputs", [])}
    block = calc.get("block_slug", "")
    
    # Try to derive a meaningful formula from the JavaScript formula
    formula_clean = formula_str.replace("\n", " ").strip()
    
    # Try to match common patterns
    patterns = [
        # Volume
        (r"(\w+)\s*\*\s*(\w+)\s*\*\s*(\w+)", lambda m: f"{m.group(1)} × {m.group(2)} × {m.group(3)}"),
        # Area of circle
        (r"pi\s*\*\s*(\w+)\s*\*\*\s*2", lambda m: f"π × {m.group(1)}²"),
        # Division
        (r"(\w+)\s*/\s*(\w+)", lambda m: f"{m.group(1)} ÷ {m.group(2)}"),
        # Multiplication
        (r"(\w+)\s*\*\s*(\w+)", lambda m: f"{m.group(1)} × {m.group(2)}"),
    ]
    
    # Try output-specific
    if len(outputs) == 1:
        out_id = list(outputs.keys())[0]
        out_unit = outputs[out_id].get("unit", "")
        if out_unit:
            return f"{out_id.replace('_', ' ').title()} ({out_unit}) = f({', '.join(inputs.keys())})"
        return f"{out_id.replace('_', ' ').title()} = f({', '.join(inputs.keys())})"
    
    # Fallback: try to extract from formula
    for pattern, replacer in patterns:
        match = re.search(pattern, formula_clean)
        if match:
            result = replacer(match)
            # Add output context
            if outputs:
                out_keys = list(outputs.keys())[:2]
                suffix = f" → {', '.join(out_keys)}"
                return f"{result}{suffix}"
            return result
    
    return calc.get("formula_display", TEMPLATE_FORMULA)

def generate_range_hints(calc):
    """Generate real range hints based on input types."""
    hints = {}
    for inp in calc.get("inputs", []):
        inp_id = inp.get("id", "")
        inp_type = inp.get("type", "number")
        min_v = inp.get("min", 0)
        max_v = inp.get("max", 500)
        default = inp.get("default", 0)
        unit = inp.get("unit", "")
        
        if inp_type == "select":
            options = inp.get("options", [])
            opt_strs = [str(o) if isinstance(o, str) else str(o.get("value", o.get("label", o))) for o in options[:5]]
            hints[inp_id] = f"Seleccionar entre las opciones: {', '.join(opt_strs)}"
        elif inp_type == "number":
            if default and min_v is not None and max_v is not None:
                hints[inp_id] = f"Valor típico entre {min_v} y {max_v}. Valor por defecto: {default}{' ' + unit if unit else ''}."
            elif default:
                hints[inp_id] = f"Valor por defecto: {default}{' ' + unit if unit else ''}."
            else:
                hints[inp_id] = f"Introducir un valor numérico{' en ' + unit if unit else ''}."
    
    return hints

def generate_comparison_presets(calc):
    """Generate 5 varied comparison presets."""
    inputs = calc.get("inputs", [])
    num_inputs = [inp for inp in inputs if inp.get("type") == "number"]
    
    if not num_inputs:
        return calc.get("comparison_presets", [])
    
    presets = []
    labels = ["Pequeño", "Mediano", "Grande", "Muy grande", "Extremo"]
    
    for i, label in enumerate(labels):
        preset = {"_label": label}
        multiplier = [0.5, 0.75, 1.0, 1.5, 2.5][i]
        for inp in num_inputs:
            default = inp.get("default", 1) or 1
            min_v = inp.get("min", 0) or 0
            val = max(min_v, round(default * multiplier, 2))
            preset[inp["id"]] = val
        presets.append(preset)
    
    return presets

def generate_example_label(calc):
    """Generate a descriptive example label."""
    num_inputs = [inp for inp in calc.get("inputs", []) if inp.get("type") == "number"]
    if not num_inputs:
        return calc.get("example_label", "")
    
    parts = []
    for inp in num_inputs[:3]:
        default = inp.get("default", 1)
        unit = inp.get("unit", "")
        parts.append(f"{inp.get('id', '')}={default}{' ' + unit if unit else ''}")
    
    slug = calc.get("slug", "").replace("-", " ")
    return f"Ejemplo de cálculo para {slug}: {', '.join(parts)}."

# --- Main processing ---
fixed_count = 0
for calc in data["calculators"]:
    calc_id = calc.get("id", "")
    steps = calc.get("steps", [])
    mistakes = calc.get("mistakes", [])
    formula_display = calc.get("formula_display", "")
    block_slug = calc.get("block_slug", "")
    
    needs_fix = False
    
    # Check if template steps
    if steps and steps[0] == TEMPLATE_STEPS_FIRST:
        calc["steps"] = generate_steps(calc)
        needs_fix = True
    
    # Check if template mistakes
    if mistakes and mistakes[0] == TEMPLATE_MISTAKES_FIRST:
        calc["mistakes"] = get_domain_mistakes(block_slug)
        needs_fix = True
    
    # Check if template formula_display
    if formula_display == TEMPLATE_FORMULA:
        calc["formula_display"] = generate_formula_display(calc)
        needs_fix = True
    
    # Always fix generic range_hints
    range_hints = calc.get("range_hints", {})
    if range_hints:
        has_generic = any("Valor según especificaciones" in str(v) for v in range_hints.values())
        if has_generic:
            calc["range_hints"] = generate_range_hints(calc)
            needs_fix = True
    
    # Fix generic comparison presets
    presets = calc.get("comparison_presets", [])
    has_generic_labels = any(p.get("_label", "") in ("Small scale", "Medium", "Large", "Industrial", "Theoretical") for p in presets)
    if has_generic_labels:
        calc["comparison_presets"] = generate_comparison_presets(calc)
        needs_fix = True
    
    # Fix generic example_labels
    example_label = calc.get("example_label", "")
    if example_label and ("Calcular para" in example_label and "×" in example_label):
        calc["example_label"] = generate_example_label(calc)
        needs_fix = True
    
    if needs_fix:
        fixed_count += 1

print(f"Fixed {fixed_count} calculators")

# Write output
with open(INPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done writing")
