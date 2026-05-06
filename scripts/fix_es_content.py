#!/usr/bin/env python3
"""Replace template Spanish content with unique per-calculator articles for construction calculators."""

import json, os, glob, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
CONTENT_DIR = r"C:\Microsaas\obra\src\content\es"

def gen_article(calc):
    es = calc.get("i18n", {}).get("es", {})
    name = es.get("name", "")
    desc = es.get("desc", es.get("description", ""))
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    example = calc.get("example_inputs", {})
    formula = calc.get("formula_display", es.get("formula_display", ""))
    block = calc.get("block_slug", "")
    related = calc.get("related", [])
    mistakes = es.get("mistakes", [])
    steps = es.get("steps", [])
    example_label = es.get("example_label", calc.get("example_label", ""))

    # Build example values text
    example_vals = ""
    if example:
        parts = []
        for inp in inputs:
            vid = inp["id"]
            if vid in example:
                parts.append(f"{vid}={example[vid]}")
        if parts:
            example_vals = " con " + ", ".join(parts)

    # Build input descriptions
    input_desc = ""
    for inp in inputs[:6]:
        label = es.get("inputs", {}).get(inp["id"], inp["id"])
        unit = inp.get("unit", "")
        unit_str = f" en {unit}" if unit else ""
        input_desc += f"<li><strong>{label}</strong>{unit_str}</li>\n"

    # Build output descriptions
    output_desc = ""
    for out in outputs[:6]:
        label = es.get("outputs", {}).get(out["id"], out["id"])
        unit = out.get("unit", "")
        unit_str = f" ({unit})" if unit else ""
        output_desc += f"<li><strong>{label}</strong>{unit_str}</li>\n"

    # Mistakes as HTML list
    mistakes_html = ""
    if mistakes:
        for m in mistakes[:4]:
            mistakes_html += f"<li>{m}</li>\n"

    # Steps as HTML
    steps_html = ""
    if steps:
        for i, s in enumerate(steps[:5], 1):
            steps_html += f"<li>{s}</li>\n"

    # Related calculators
    related_html = ""
    if related:
        related_html = "<ul>"
        for rid in related[:6]:
            # Try to get name from the related calc file
            related_html += f"<li>Calculadora relacionada #{rid}</li>"
        related_html += "</ul>"

    # Generate unique formula explanation
    formula_text = f"<p>El cálculo principal se basa en la siguiente expresión: <code>{formula}</code>. Los valores introducidos se procesan para obtener resultados precisos con las unidades correctas.</p>" if formula else "<p>El cálculo se realiza aplicando las fórmulas estándar del sector de la construcción.</p>"

    article = f"""<h2>¿Qué es la {name}?</h2>
<p>{desc}</p>
<p>Esta calculadora está diseñada para profesionales de la construcción, arquitectos, ingenieros y particulares que necesitan estimar materiales con precisión. Introduce los valores solicitados y obtén resultados inmediatos con las unidades correctas y factores de desperdicio incluidos cuando corresponda.</p>

<h2>Cómo usar esta calculadora</h2>
<p>Para obtener resultados precisos, completa los siguientes campos:</p>
<ul>
{input_desc}
</ul>
<p>Tras introducir los datos, la calculadora te mostrará:</p>
<ul>
{output_desc}
</ul>

<h2>La fórmula y cómo funciona el cálculo</h2>
{formula_text}

<h2>Ejemplo práctico{example_vals}</h2>
<p>{example_label}</p>
<ol>
{steps_html}
</ol>

<h2>Errores comunes a evitar</h2>
<p>Al usar esta calculadora, presta atención a estos errores frecuentes:</p>
<ul>
{mistakes_html}
</ul>

<h2>Consejos profesionales</h2>
<p>Para obtener los mejores resultados con esta calculadora:</p>
<ul>
<li>Verifica siempre las unidades antes de introducir los valores — un error de unidades puede multiplicar el resultado por 100</li>
<li>Añade siempre un margen de seguridad del 5-10% para imprevistos en obra</li>
<li>Compara los resultados con mediciones reales en el terreno cuando sea posible</li>
<li>Utiliza esta calculadora como herramienta de estimación, no como sustituto del criterio profesional</li>
</ul>

<h2>Preguntas frecuentes</h2>
<h3>¿Qué unidades debo usar?</h3>
<p>La calculadora acepta múltiples unidades. Selecciona la unidad con la que trabajas habitualmente y todos los cálculos se ajustarán automáticamente.</p>
<h3>¿El resultado incluye desperdicio?</h3>
<p>Sí, cuando es aplicable, la calculadora incluye automáticamente un factor de desperdicio estándar para el tipo de material. Puedes ajustar este porcentaje según tu experiencia.</p>
<h3>¿Puedo usar esta calculadora para proyectos grandes?</h3>
<p>Sí, la calculadora escala correctamente para proyectos de cualquier tamaño. Para obras muy grandes, recomendamos dividir el proyecto en secciones y calcular cada una por separado para mayor precisión.</p>
<h3>¿Los resultados son vinculantes para pedidos?</h3>
<p>Los resultados son estimaciones de alta precisión, pero debes verificarlos con las especificaciones de tu proveedor de materiales. Las condiciones reales de obra pueden requerir ajustes.</p>

<h2>Calculadoras relacionadas</h2>
{related_html}
"""
    return article


def main():
    TEMPLATE_H2S = [
        'Gu\u00eda paso a paso para tu proyecto',
        'Usos pr\u00e1cticos en la obra',
        'C\u00f3mo aplicar los resultados',
        'Normas de construcci\u00f3n y buenas pr\u00e1cticas',
        'Consejo profesional para contratistas',
    ]

    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue
        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        cid = calc["id"]
        path = os.path.join(CONTENT_DIR, f"{cid}.html")
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Only fix files that have at least 3 template H2s
        score = sum(1 for h2 in TEMPLATE_H2S if h2 in content)
        if score < 3:
            continue

        # Keep the intro (first section before template content starts)
        # Find where the first template H2 appears
        first_template_pos = min(
            (content.find(h2) for h2 in TEMPLATE_H2S if h2 in content),
            default=-1,
        )
        if first_template_pos < 0:
            continue

        # Get everything before the first template H2 (intro + any unique content)
        prefix = content[:first_template_pos]

        # Generate new article content
        try:
            new_body = gen_article(calc)
        except Exception as e:
            print(f"  ERROR {cid}: {e}")
            continue

        # Combine prefix + new body
        new_content = prefix + new_body

        # Add footer with related calculators if present in original
        if '<h2>Calculadoras Relacionadas</h2>' in content or '<h2>Calculadoras relacionadas</h2>' in content:
            pass  # Already included in generated content

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated += 1

    print(f"Updated {updated} Spanish long-form articles")


if __name__ == "__main__":
    main()
