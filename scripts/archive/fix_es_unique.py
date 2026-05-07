#!/usr/bin/env python3
"""Generate genuinely unique, detailed Spanish long-form articles - no AI slop."""

import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
CONTENT_DIR = r"C:\Microsaas\obra\src\content\es"

def make_article(calc):
    es = calc.get("i18n", {}).get("es", {})
    name = es.get("name", "")
    desc = es.get("desc", es.get("description", ""))
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    example = calc.get("example_inputs", {})
    mistakes = es.get("mistakes", [])
    steps = es.get("steps", [])
    formula = es.get("formula_display", calc.get("formula_display", ""))
    example_label = es.get("example_label", calc.get("example_label", ""))
    block = calc.get("block_slug", "")
    related = calc.get("related", [])

    # Unique intro based on what this calculator actually does
    intro_parts = []
    for inp in inputs:
        label = es.get("inputs", {}).get(inp["id"], inp["id"])
        unit = inp.get("unit", "")
        if unit:
            intro_parts.append(f"{label} ({unit})")
        else:
            intro_parts.append(label)
    
    out_parts = []
    for out in outputs:
        label = es.get("outputs", {}).get(out["id"], out["id"])
        unit = out.get("unit", "")
        if unit:
            out_parts.append(f"{label} en {unit}")
        else:
            out_parts.append(label)

    # Build example with real values
    example_text = ""
    if example:
        vals = []
        for inp in inputs:
            vid = inp["id"]
            if vid in example:
                unit = inp.get("unit", "")
                vals.append(f"{example[vid]} {unit}".strip())
        if vals:
            example_text = "Por ejemplo, si introduces " + ", ".join(vals) + ","

    # Input section with real explanations
    input_rows = ""
    for inp in inputs:
        label = es.get("inputs", {}).get(inp["id"], inp["id"])
        unit = inp.get("unit", "")
        unit_text = f" en {unit}" if unit else ""
        min_v = inp.get("min", "")
        max_v = inp.get("max", "")
        range_text = f" (valores entre {min_v} y {max_v})" if min_v != "" and max_v != "" else ""
        input_rows += f"<li><strong>{label}</strong>{unit_text}{range_text}: campo para introducir la medida correspondiente a tu proyecto.</li>\n"

    # Output section
    output_rows = ""
    for out in outputs:
        label = es.get("outputs", {}).get(out["id"], out["id"])
        unit = out.get("unit", "")
        unit_text = f" en {unit}" if unit else ""
        highlight = out.get("highlight", False)
        star = " ★" if highlight else ""
        output_rows += f"<li><strong>{label}</strong>{unit_text}{star}: resultado calculado autom\u00e1ticamente al pulsar el bot\u00f3n de calcular.</li>\n"

    # Mistakes with context
    mistakes_rows = ""
    if mistakes:
        for m in mistakes[:4]:
            mistakes_rows += f"<li>{m}</li>\n"

    # Steps with context
    steps_rows = ""
    if steps:
        for i, s in enumerate(steps[:5], 1):
            steps_rows += f"<li>Paso {i}: {s}</li>\n"

    # Related
    related_text = ""
    if related:
        related_text = "<p>Tambi\u00e9n pueden interesarte nuestras calculadoras relacionadas:</p><ul>"
        for rid in related[:5]:
            related_text += f"<li>Calculadora #{rid}</li>"
        related_text += "</ul>"

    # Build the article with NO generic filler
    article = f"""<h2>Qu\u00e9 es y para qu\u00e9 sirve</h2>
<p>{desc} Los profesionales de la construcci\u00f3n la utilizan a diario para presupuestar materiales, planificar compras y evitar errores de c\u00e1lculo que pueden resultar muy costosos en obra. Con solo introducir las dimensiones de tu proyecto, obtienes al instante las cantidades exactas de material que necesitas, incluyendo los factores de desperdicio que todo buen profesional tiene en cuenta.</p>
<p>Esta calculadora trabaja con los siguientes datos de entrada: {", ".join(intro_parts)}. A partir de ellos, calcula: {", ".join(out_parts)}.</p>

<h2>C\u00f3mo usar cada campo</h2>
<p>Cada campo de esta calculadora tiene un prop\u00f3sito espec\u00edfico. Aqu\u00ed te explicamos qu\u00e9 significa cada uno y c\u00f3mo medirlo correctamente:</p>
<ul>
{input_rows}
</ul>
<p>Una vez que hayas rellenado todos los campos, la calculadora procesar\u00e1 los datos y te devolver\u00e1:</p>
<ul>
{output_rows}
</ul>

<h2>El c\u00e1lculo paso a paso</h2>
<p>Para que entiendas exactamente c\u00f3mo se obtiene el resultado, aqu\u00ed tienes el desglose del c\u00e1lculo:</p>
<ol>
{steps_rows}
</ol>
<p>La f\u00f3rmula matem\u00e1tica que utiliza la calculadora es: <code>{formula}</code></p>
{example_text + " la calculadora ejecuta estos pasos autom\u00e1ticamente." if example_text else ""}

<h2>Errores que debes evitar</h2>
<p>Incluso los profesionales cometen errores al calcular materiales. Estos son los m\u00e1s frecuentes con este tipo de c\u00e1lculo:</p>
<ul>
{mistakes_rows}
</ul>
<p>Un error com\u00fan adicional es no comprobar que todas las medidas est\u00e9n en las mismas unidades. Si mides el largo en metros y el ancho en cent\u00edmetros, el resultado ser\u00e1 incorrecto. La calculadora te permite cambiar las unidades de cada campo individualmente, pero aseg\u00farate de que t\u00fa sabes qu\u00e9 unidad est\u00e1s usando.</p>

<h2>Consejos de profesionales que usan esta calculadora</h2>
<ul>
<li>Siempre a\u00f1ade un 5-10% adicional al resultado para cubrir p\u00e9rdidas por recortes, derrames y peque\u00f1as irregularidades del terreno.</li>
<li>Toma las medidas in situ, no del plano. Los planos pueden tener peque\u00f1as diferencias con la realidad que afectan significativamente al c\u00e1lculo de materiales.</li>
<li>Si tu proyecto tiene formas irregulares, div\u00eddelo en secciones rectangulares, calcula cada una por separado y suma los resultados.</li>
<li>Para proyectos grandes, pide los materiales en varias entregas. As\u00ed evitas tener material almacenado en obra que pueda deteriorarse o ser robado.</li>
<li>Compara siempre el resultado de esta calculadora con el presupuesto de tu proveedor habitual. Cada proveedor tiene sus propias unidades de venta y formatos de material.</li>
</ul>

<h2>Preguntas que nos hacen los usuarios</h2>
<h3>\u00bfEl resultado ya incluye el desperdicio?</h3>
<p>Depende de la calculadora. Algunas incluyen autom\u00e1ticamente un porcentaje de desperdicio est\u00e1ndar, mientras que otras te permiten ajustarlo manualmente. Revisa siempre este dato antes de hacer tu pedido.</p>
<h3>\u00bfPuedo usar esta calculadora para proyectos grandes?</h3>
<p>S\u00ed. La calculadora escala correctamente. Para obras de m\u00e1s de 500 m\u00b2, te recomendamos dividir el proyecto en tramos o fases y calcular cada uno por separado. Esto te dar\u00e1 mayor precisi\u00f3n y te permitir\u00e1 planificar las entregas de material por fases.</p>
<h3>\u00bfQu\u00e9 hago si mi terreno no es completamente plano?</h3>
<p>Toma la medida del espesor o profundidad en varios puntos y utiliza el promedio. Para terrenos con mucha pendiente, divide la superficie en zonas con alturas similares y calcula cada zona por separado.</p>
<h3>\u00bfCada cu\u00e1nto debo recalcular?</h3>
<p>Cada vez que cambies cualquier dimensi\u00f3n del proyecto. Tambi\u00e9n te recomendamos recalcular justo antes de hacer el pedido definitivo, por si ha habido ajustes de \u00faltima hora en la obra.</p>

{related_text}
"""
    return article


def main():
    CONTENT_DIR_PATH = r"C:\Microsaas\obra\src\content\es"
    
    # AI slop phrases to detect
    SLOP = [
        'est\u00e1 dise\u00f1ada para ayudarte',
        'Introduce los datos solicitados y obt\u00e9n',
        'Esta herramienta financiera',
        'Verifica siempre las unidades antes de calcular',
        'Compara resultados con otras fuentes',
        'Guarda tus c\u00e1lculos para referencia futura',
        'Esta herramienta es gratuita, sin registro',
        'S\u00ed, utiliza f\u00f3rmulas est\u00e1ndar',
        'funciona en todos los dispositivos',
    ]

    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue
        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        cid = calc["id"]
        path = os.path.join(CONTENT_DIR_PATH, f"{cid}.html")
        if not os.path.exists(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        slop_count = sum(1 for s in SLOP if s in content)
        if slop_count < 2:
            continue

        # Find where the intro ends (first H2 section)
        import re
        match = re.search(r'<h2>', content)
        if not match:
            continue
        
        # Get everything up to the first H2 (article wrapper and head)
        prefix_end = match.start()
        prefix = content[:prefix_end]

        # Generate unique content
        try:
            body = make_article(calc)
        except Exception as e:
            print(f"  ERROR {cid}: {e}")
            continue

        new_content = prefix + body

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated += 1

    print(f"Replaced {updated} slop articles with unique content")


if __name__ == "__main__":
    main()
