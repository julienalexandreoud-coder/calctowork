#!/usr/bin/env python3
"""Generate clean Spanish articles - 100% data-driven, zero hardcoded prose, per-calculator unique."""

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
    formula = es.get("formula_display", "")
    seo_desc = es.get("seo_description", "")
    related = calc.get("related", [])

    # Build input descriptions from real data
    input_rows = ""
    for inp in inputs:
        label = es.get("inputs", {}).get(inp["id"], inp["id"])
        unit = inp.get("unit", "")
        unit_text = f" en {unit}" if unit and unit not in ("", "none", "-") else ""
        default = inp.get("default", "")
        default_text = f" (valor por defecto: {default})" if default != "" and default is not None else ""
        input_rows += f"<li><strong>{label}</strong>{unit_text}{default_text}</li>\n"

    # Build output descriptions
    output_rows = ""
    for out in outputs:
        label = es.get("outputs", {}).get(out["id"], out["id"])
        unit = out.get("unit", "")
        unit_text = f" en {unit}" if unit and unit not in ("", "none", "-") else ""
        output_rows += f"<li><strong>{label}</strong>{unit_text}</li>\n"

    # Build steps with numbers
    steps_rows = ""
    if steps:
        for i, s in enumerate(steps, 1):
            steps_rows += f"<li>{s}</li>\n"

    # Build mistakes
    mistakes_rows = ""
    if mistakes:
        for m in mistakes[:5]:
            mistakes_rows += f"<li>{m}</li>\n"

    # Build example from real example_inputs
    example_text = ""
    if example:
        lines = []
        for inp in inputs:
            vid = inp["id"]
            if vid in example:
                unit = inp.get("unit", "")
                label = es.get("inputs", {}).get(vid, vid)
                val = example[vid]
                lines.append(f"{label}: <strong>{val} {unit}</strong>".strip())
        if lines:
            example_text = "<p>Ejemplo de uso: " + ", ".join(lines) + ".</p>"

    # Build related
    related_text = ""
    if related:
        related_text = "<p>Calculadoras relacionadas:"
        for rid in related[:6]:
            related_text += f" #{rid}"
        related_text += "</p>"

    # Formula explanation
    formula_text = ""
    if formula:
        formula_text = f"<p>F\u00f3rmula: <code>{formula}</code></p>"

    body = ""
    if desc:
        body += f"<p>{desc}</p>\n"
    if seo_desc:
        body += f"<p>{seo_desc}</p>\n"
    
    if input_rows:
        body += f"<h2>Datos de entrada</h2>\n<ul>\n{input_rows}</ul>\n"
    if output_rows:
        body += f"<h2>Resultados</h2>\n<ul>\n{output_rows}</ul>\n"
    if formula_text:
        body += formula_text
    if example_text:
        body += example_text
    if steps_rows:
        body += f"<h2>Desglose del c\u00e1lculo</h2>\n<ol>\n{steps_rows}</ol>\n"
    if mistakes_rows:
        body += f"<h2>Errores frecuentes</h2>\n<ul>\n{mistakes_rows}</ul>\n"
    if related_text:
        body += related_text

    return body


def main():
    import re
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

        # Find the first H2 — keep everything before it (wrapper HTML)
        match = re.search(r'<h2>', content)
        if not match:
            continue
        prefix = content[:match.start()]

        try:
            body = make_article(calc)
        except Exception as e:
            print(f"  ERROR {cid}: {e}")
            continue

        new_content = prefix + body
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1

    print(f"Updated {updated} articles with pure data-driven content")


if __name__ == "__main__":
    main()
