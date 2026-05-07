#!/usr/bin/env python3
"""Replace remaining template Spanish articles (math, physics, health, sports, etc)."""

import json, os, glob

CALC_DIR = r"C:\Microsaas\obra\src\calculators"
CONTENT_DIR = r"C:\Microsaas\obra\src\content\es"

# All remaining template H2s to replace
TEMPLATE_H2S = [
    'La f\u00f3rmula explicada',
    'La f\u00f3rmula de f\u00edsica explicada',
    'La f\u00f3rmula m\u00e9dica explicada',
    'La f\u00f3rmula detr\u00e1s de tus resultados',
    'C\u00f3mo funciona la conversi\u00f3n',
    'C\u00f3mo funciona este c\u00e1lculo',
    'Errores Comunes',
    'Consejo Profesional',
]

def gen_article(calc):
    es = calc.get("i18n", {}).get("es", {})
    name = es.get("name", "")
    desc = es.get("desc", es.get("description", ""))
    inputs = calc.get("inputs", [])
    outputs = calc.get("outputs", [])
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

    formula = es.get("formula_display", calc.get("formula_display", ""))

    article = f"""<h2>¿Qué es la {name}?</h2>
<p>{desc}</p>

<h2>Cómo usar esta calculadora</h2>
<p>Introduce los siguientes datos:</p>
<ul>
{input_desc}
</ul>
<p>Obtendrás:</p>
<ul>
{output_desc}
</ul>

<h2>Cómo funciona el cálculo</h2>
<p>El cálculo se basa en la siguiente expresión: <code>{formula}</code></p>
<p>Los valores que introduzcas se procesan automáticamente para darte el resultado con la máxima precisión.</p>

<h2>Ejemplo paso a paso</h2>
<ol>
{steps_html}
</ol>

<h2>Errores comunes</h2>
<ul>
{mistakes_html}
</ul>

<h2>Consejos útiles</h2>
<ul>
<li>Verifica siempre que los valores introducidos estén en las unidades correctas</li>
<li>Comprueba los resultados con un segundo método si es posible</li>
<li>Guarda tus cálculos para referencia futura usando la función de exportación</li>
<li>Esta calculadora es gratuita y no requiere registro</li>
</ul>

<h2>Preguntas frecuentes</h2>
<h3>¿Es precisa esta calculadora?</h3>
<p>Sí, utiliza fórmulas estándar y precisión de cálculo completa. Los resultados son fiables para uso profesional y personal.</p>
<h3>¿Puedo usar los resultados para trabajos académicos?</h3>
<p>Sí, puedes citar esta calculadora como fuente. Te recomendamos verificar los resultados manualmente para trabajos académicos formales.</p>
<h3>¿Funciona en dispositivos móviles?</h3>
<p>Sí, la calculadora está optimizada para funcionar en cualquier dispositivo, incluyendo teléfonos y tablets.</p>
"""
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

    print(f"Updated {updated} Spanish articles")


if __name__ == "__main__":
    main()
