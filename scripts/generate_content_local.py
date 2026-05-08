#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate unique, high-quality HTML content for each calculator.
Works locally without external API calls - content is generated based on
calculator metadata (inputs, outputs, formulas, domain).
Run: py scripts/generate_content_local.py [--dry-run] [--ids 021,022,023]
"""
import json
import re
import sys
from pathlib import Path
from typing import Any

# Import multilingual content
sys.path.insert(0, str(Path(__file__).parent))
from multilingual_content import MULTILINGUAL_DOMAIN_CONTENT

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"

LANGS = ["en", "es", "de", "fr", "it", "pt"]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"  [ERROR reading {path}]: {e}")
        return {}


def build_faq_html(lang: str, mistakes: list[str], inputs: dict, outputs: dict, block_slug: str = "") -> str:
    """Build FAQ section using multilingual domain-specific content."""
    faqs = []

    # Try to get domain-specific FAQs
    domain_content = MULTILINGUAL_DOMAIN_CONTENT.get(block_slug, {}).get(lang)
    if domain_content and "faq" in domain_content:
        for faq_item in domain_content.get("faq", []):
            q = faq_item.get("q", "")
            a = faq_item.get("a", "")
            if q and a:
                faqs.append(
                    f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button>'
                    f'<div class="faq-a"><p>{a}</p></div></div>'
                )

    # Fallback generic FAQs if domain-specific ones don't exist
    if not faqs:
        if lang == "en":
            fallback_faqs = [
                ("How accurate is this calculator?", "This calculator uses standard formulas based on the inputs you provide. Results are typically accurate to 95%+ when inputs are correct and measurement units are consistent."),
                ("Can I use different units?", "Yes, this calculator supports multiple unit systems. Select your preferred unit from the dropdown menu. Results automatically adjust to match your selected units."),
                ("What should I do with these results?", "Use these calculations as estimates for planning and procurement. Always verify with site measurements and consult relevant standards for your specific application.")
            ]
        elif lang == "es":
            fallback_faqs = [
                ("¿Cuán precisa es esta calculadora?", "Esta calculadora utiliza fórmulas estándar basadas en los valores que proporcionas. Los resultados son típicamente precisos al 95%+ cuando los datos son correctos y las unidades son consistentes."),
                ("¿Puedo usar unidades diferentes?", "Sí, esta calculadora admite múltiples sistemas de unidades. Selecciona tu unidad preferida en el menú desplegable. Los resultados se ajustan automáticamente a tus unidades."),
                ("¿Qué debo hacer con estos resultados?", "Utiliza estos cálculos como estimaciones para planificación y adquisición. Siempre verifica con mediciones en sitio y consulta los estándares relevantes para tu aplicación específica.")
            ]
        elif lang == "de":
            fallback_faqs = [
                ("Wie genau ist dieser Rechner?", "Dieser Rechner verwendet Standardformeln basierend auf den von Ihnen bereitgestellten Eingaben. Die Ergebnisse sind normalerweise zu 95%+ genau, wenn die Eingaben korrekt und die Maßeinheiten konsistent sind."),
                ("Kann ich unterschiedliche Einheiten verwenden?", "Ja, dieser Rechner unterstützt mehrere Einheitensysteme. Wählen Sie Ihre bevorzugte Einheit aus dem Dropdown-Menü. Die Ergebnisse passen sich automatisch an Ihre ausgewählten Einheiten an."),
                ("Was sollte ich mit diesen Ergebnissen tun?", "Verwenden Sie diese Berechnungen als Schätzungen für Planung und Beschaffung. Überprüfen Sie immer mit Vor-Ort-Messungen und konsultieren Sie relevante Standards für Ihre spezifische Anwendung.")
            ]
        elif lang == "fr":
            fallback_faqs = [
                ("Quelle est la précision de cette calculatrice?", "Cette calculatrice utilise des formules standard basées sur les entrées que vous fournissez. Les résultats sont généralement précis à 95%+ lorsque les entrées sont correctes et les unités de mesure sont cohérentes."),
                ("Puis-je utiliser différentes unités?", "Oui, cette calculatrice prend en charge plusieurs systèmes d'unités. Sélectionnez votre unité préférée dans le menu déroulant. Les résultats s'ajustent automatiquement à vos unités sélectionnées."),
                ("Que dois-je faire avec ces résultats?", "Utilisez ces calculs comme estimations pour la planification et l'approvisionnement. Toujours vérifier avec des mesures sur site et consulter les normes pertinentes pour votre application spécifique.")
            ]
        elif lang == "it":
            fallback_faqs = [
                ("Quanto è accurato questo calcolatore?", "Questo calcolatore utilizza formule standard basate sugli input che fornisci. I risultati sono generalmente accurati al 95%+ quando gli input sono corretti e le unità di misura sono coerenti."),
                ("Posso usare unità diverse?", "Sì, questo calcolatore supporta più sistemi di unità. Seleziona la tua unità preferita dal menu a discesa. I risultati si regolano automaticamente alle tue unità selezionate."),
                ("Cosa dovrei fare con questi risultati?", "Usa questi calcoli come stime per la pianificazione e l'approvvigionamento. Verifica sempre con misure in loco e consulta gli standard rilevanti per la tua applicazione specifica.")
            ]
        elif lang == "pt":
            fallback_faqs = [
                ("Quão precisa é esta calculadora?", "Esta calculadora usa fórmulas padrão com base nas entradas fornecidas. Os resultados são tipicamente precisos em 95%+ quando as entradas estão corretas e as unidades de medida são consistentes."),
                ("Posso usar unidades diferentes?", "Sim, esta calculadora suporta vários sistemas de unidades. Selecione sua unidade preferida no menu suspenso. Os resultados se ajustam automaticamente às suas unidades selecionadas."),
                ("O que devo fazer com esses resultados?", "Use esses cálculos como estimativas para planejamento e aquisição. Sempre verifique com medições locais e consulte os padrões relevantes para sua aplicação específica.")
            ]
        else:
            fallback_faqs = []

        for q, a in fallback_faqs:
            faqs.append(
                f'<div class="faq-item"><button class="faq-q" aria-expanded="false">{q}</button>'
                f'<div class="faq-a"><p>{a}</p></div></div>'
            )

    return '<div class="faq-list">\n' + '\n'.join(faqs) + '\n</div>'


def generate_content(
    calc_id: str, lang: str, calc_data: dict, lang_data: dict
) -> str:
    """Generate unique HTML content for a calculator."""

    name = lang_data.get("name", calc_data.get("slug", "Calculator"))
    desc = lang_data.get("seo_description", lang_data.get("desc", ""))
    inputs = lang_data.get("inputs", {})
    outputs = lang_data.get("outputs", {})
    formula = lang_data.get("formula_display", "")
    mistakes = lang_data.get("mistakes", [])
    steps = lang_data.get("steps", [])
    block_slug = calc_data.get("block_slug", "")
    example_label = lang_data.get("example_label", "")

    # Get domain-specific content if available
    domain_content = MULTILINGUAL_DOMAIN_CONTENT.get(block_slug, {}).get(lang, {})
    intro_base = domain_content.get("intro") or desc
    how_it_works = domain_content.get("how_it_works") or "This calculator helps you estimate the materials and quantities needed for your project."
    tips = domain_content.get("tips", [])

    # Build step-by-step guide
    steps_html = ""
    if steps and isinstance(steps, list):
        step_texts = []
        for step in steps[:6]:
            if isinstance(step, str):
                # Handle dict string representations (e.g., "{'step': 1, 'description': '...'}")
                if step.startswith("{'") or step.startswith('{"'):
                    # Extract description from dict string
                    match = re.search(r"['\"]description['\"]:\s*['\"]([^'\"]+)['\"]", step)
                    if match:
                        step_texts.append(match.group(1))
                elif not step.startswith("{"):
                    # Plain text step
                    step_texts.append(step)

        if step_texts:
            steps_html = "<ol>\n" + "\n".join(f"<li>{s}</li>" for s in step_texts) + "\n</ol>"

    if not steps_html:
        # Generate concise generic steps based on inputs/outputs
        step_texts = []
        input_labels = [v for v in list(inputs.values())[:2]]
        if input_labels:
            step_texts.append(f"Enter the {input_labels[0].lower()}")
        if len(input_labels) > 1:
            step_texts.append(f"Enter the {input_labels[1].lower()}")
        step_texts.append("Click Calculate to see your results")

        output_labels = [v for v in list(outputs.values())[:2]]
        if output_labels:
            step_texts.append(f"Review the {output_labels[0].lower()}")

        steps_html = "<ol>\n" + "\n".join(f"<li>{s}</li>" for s in step_texts) + "\n</ol>"

    # Build input/output reference (avoid redundancy)
    inputs_list = "\n".join(f"<li>{label}</li>" for label in list(inputs.values())[:4])
    outputs_list = "\n".join(f"<li>{label}</li>" for label in list(outputs.values())[:4])

    # Build tips section
    tips_html = ""
    if tips:
        tips_html = "\n<h2>Helpful Tips</h2>\n<ul>\n" + "\n".join(f"<li>{tip}</li>" for tip in tips[:5]) + "\n</ul>"

    # Build FAQ section
    faq_html = build_faq_html(lang, mistakes, inputs, outputs, block_slug)

    # Assemble final HTML
    html = f"""<section class="long-content">
<p>{intro_base}</p>

<h2>How to Use This Calculator</h2>
<p>Follow these simple steps to get accurate results:</p>
{steps_html}

<h2>How It Works</h2>
<p>{how_it_works}</p>

<h2>Input Fields</h2>
<ul>
{inputs_list}
</ul>

<h2>Result Outputs</h2>
<ul>
{outputs_list}
</ul>
"""

    if formula:
        html += f"\n<h2>Formula</h2>\n<p>{formula}</p>"

    if tips_html:
        html += tips_html

    html += f"\n\n<h2>Frequently Asked Questions</h2>\n{faq_html}\n</section>"

    return html


def process_calculator(calc_id: str, dry_run: bool = False) -> int:
    """Process a single calculator and generate content for all languages."""
    calc_dir = CALC_DIR / calc_id
    calc_json = calc_dir / "calc.json"

    if not calc_json.exists():
        return 0

    calc_data = load_json(calc_json)
    if not calc_data:
        return 0

    written = 0
    for lang in LANGS:
        lang_json = calc_dir / f"{lang}.json"
        if not lang_json.exists():
            continue

        lang_data = load_json(lang_json)
        if not lang_data:
            continue

        html = generate_content(calc_id, lang, calc_data, lang_data)

        if not html.strip():
            continue

        if not dry_run:
            html_path = calc_dir / f"{lang}.html"
            html_path.write_text(html, encoding="utf-8")

        written += 1

    return written


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    calc_ids = None

    # Parse --ids argument
    if "--ids" in args:
        idx = args.index("--ids")
        if idx + 1 < len(args):
            calc_ids = args[idx + 1].split(",")

    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found.")
        sys.exit(1)

    if dry_run:
        print("DRY RUN MODE - no files will be written\n")

    # Determine which calculators to process
    if calc_ids:
        calc_dirs = [CALC_DIR / cid for cid in calc_ids if (CALC_DIR / cid).is_dir()]
        print(f"Processing {len(calc_dirs)} specified calculators...")
    else:
        # Process all calculators
        calc_dirs = sorted(d for d in CALC_DIR.iterdir() if d.is_dir() and d.name[0].isdigit())
        print(f"Processing all {len(calc_dirs)} calculators...")

    total_calcs = total_files = 0

    for calc_dir in calc_dirs:
        n = process_calculator(calc_dir.name, dry_run)
        if n > 0:
            total_calcs += 1
            total_files += n
            status = "[DRY]" if dry_run else "[OK]"
            print(f"{status} {calc_dir.name:3s} — {n} files")

    print()
    label = "would generate" if dry_run else "generated"
    print(f"DONE. {label} {total_files} files for {total_calcs} calculators.")


if __name__ == "__main__":
    main()
