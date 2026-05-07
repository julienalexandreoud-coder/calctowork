#!/usr/bin/env python3
"""Replace template finance articles with unique per-calculator content."""

import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
CONTENT_DIR = r"C:\Microsaas\obra\src\content\es"

TEMPLATE_H2S = [
    'La f\u00f3rmula financiera explicada',
    'Aplicaciones pr\u00e1cticas para tu dinero',
    'C\u00f3mo leer el resultado financiero',
    'C\u00f3mo funcionan las f\u00f3rmulas financieras',
]

def gen_article(calc):
    es = calc.get("i18n", {}).get("es", {})
    name = es.get("name", "")
    desc = es.get("desc", es.get("description", ""))
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
    example = calc.get("example_inputs", {})
    mistakes = es.get("mistakes", [])
    steps = es.get("steps", [])

    input_desc = ""
    for inp in inputs[:6]:
        label = es.get("inputs", {}).get(inp["id"], inp["id"])
        input_desc += f"<li><strong>{label}</strong></li>\n"

    output_desc = ""
    for out in outputs[:6]:
        label = es.get("outputs", {}).get(out["id"], out["id"])
        output_desc += f"<li><strong>{label}</strong></li>\n"

    mistakes_html = ""
    if mistakes:
        for m in mistakes[:4]:
            mistakes_html += f"<li>{m}</li>\n"

    steps_html = ""
    if steps:
        for s in steps[:5]:
            steps_html += f"<li>{s}</li>\n"

    article = f"""<h2>¿Qué es la {name}?</h2>
<p>{desc}</p>
<p>Esta herramienta financiera está diseñada para ayudarte a tomar decisiones informadas sobre tu dinero. Introduce los datos solicitados y obtén resultados inmediatos que te permitirán planificar tus finanzas con confianza.</p>

<h2>Cómo usar esta calculadora financiera</h2>
<p>Completa los siguientes campos con tus datos:</p>
<ul>
{input_desc}
</ul>
<p>La calculadora te devolverá:</p>
<ul>
{output_desc}
</ul>

<h2>Ejemplo práctico de cálculo</h2>
<ol>
{steps_html}
</ol>

<h2>Errores comunes al calcular</h2>
<ul>
{mistakes_html}
</ul>

<h2>Consejos para mejorar tus finanzas</h2>
<ul>
<li>Compara siempre varias opciones antes de tomar una decisión financiera importante</li>
<li>Revisa los resultados periódicamente — las condiciones del mercado cambian</li>
<li>Utiliza esta calculadora para simular diferentes escenarios (optimista, realista, pesimista)</li>
<li>Los resultados son estimaciones — consulta con un asesor financiero para decisiones importantes</li>
<li>Ten en cuenta la inflación al planificar a largo plazo</li>
</ul>

<h2>Preguntas frecuentes</h2>
<h3>¿Qué tasa de interés debo usar?</h3>
<p>Utiliza la tasa anual nominal (TIN) de tu producto financiero. Si tienes la TAE, la calculadora la convierte automáticamente.</p>
<h3>¿Los cálculos incluyen impuestos?</h3>
<p>Los resultados muestran valores antes de impuestos. Para cálculos con impuestos incluidos, utiliza nuestra calculadora de IVA.</p>
<h3>¿Puedo guardar mis resultados?</h3>
<p>Puedes descargar un PDF con tus resultados usando la función de exportación al final de la página.</p>
<h3>¿Son precisos los resultados para préstamos reales?</h3>
<p>Sí, los cálculos siguen las fórmulas financieras estándar utilizadas por bancos y entidades financieras. Las pequeñas diferencias con tu entidad pueden deberse a comisiones o seguros adicionales.</p>
"""

    example_label = es.get("example_label", "")
    if example_label:
        article += f"\n<p><em>Ejemplo: {example_label}</em></p>\n"

    return article


def main():
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

        score = sum(1 for h2 in TEMPLATE_H2S if h2 in content)
        if score < 2:
            continue

        first_template_pos = min(
            (content.find(h2) for h2 in TEMPLATE_H2S if h2 in content),
            default=-1,
        )
        if first_template_pos < 0:
            continue

        prefix = content[:first_template_pos]

        try:
            new_body = gen_article(calc)
        except Exception as e:
            print(f"  ERROR {cid}: {e}")
            continue

        new_content = prefix + new_body
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1

    print(f"Updated {updated} Spanish finance articles")


if __name__ == "__main__":
    main()
