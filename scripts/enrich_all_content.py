"""
Rewrite thin content files (< 80 lines) for all calculators.
Uses steps, mistakes, formula_display, result_context, example_inputs from calculators.json.
Generates matching files for all 6 language directories.
"""
import json
import pathlib
import html as htmllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
I18N_DIR = ROOT / "src" / "i18n"
CONTENT_DIR = ROOT / "src" / "content"
LANGS = ["es", "en", "fr", "de", "it", "pt"]

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
calcs = {c["id"]: c for c in data["calculators"]}

def esc(s: str) -> str:
    return htmllib.escape(str(s))

FAQ_TEMPLATES = {
    "es": [
        ("¿Es gratis esta calculadora?", "Sí, todas las calculadoras de CalcToWork son completamente gratuitas."),
        ("¿Puedo usar los resultados para trabajo profesional?", "Los resultados son estimaciones. Siempre verifique con un profesional cualificado para decisiones críticas."),
    ],
    "en": [
        ("Is this calculator free?", "Yes, all CalcToWork calculators are completely free to use."),
        ("Can I use the results for professional work?", "Results are estimates. Always verify with a qualified professional for critical decisions."),
    ],
    "fr": [
        ("Cette calculatrice est-elle gratuite ?", "Oui, toutes les calculatrices CalcToWork sont entièrement gratuites."),
        ("Puis-je utiliser les résultats pour un travail professionnel ?", "Les résultats sont des estimations. Vérifiez toujours avec un professionnel qualifié pour les décisions critiques."),
    ],
    "de": [
        ("Ist dieser Rechner kostenlos?", "Ja, alle CalcToWork-Rechner sind völlig kostenlos."),
        ("Kann ich die Ergebnisse für professionelle Arbeit verwenden?", "Die Ergebnisse sind Schätzungen. Überprüfen Sie für kritische Entscheidungen immer mit einem Fachmann."),
    ],
    "it": [
        ("Questa calcolatrice è gratuita?", "Sì, tutte le calcolatrici di CalcToWork sono completamente gratuite."),
        ("Posso usare i risultati per lavoro professionale?", "I risultati sono stime. Verifica sempre con un professionista qualificato per decisioni critiche."),
    ],
    "pt": [
        ("Esta calculadora é gratuita?", "Sim, todas as calculadoras do CalcToWork são completamente gratuitas."),
        ("Posso usar os resultados para trabalho profissional?", "Os resultados são estimativas. Sempre verifique com um profissional qualificado para decisões críticas."),
    ],
}

def build_html(cid: str, calc: dict, ci18n: dict, lang: str) -> str:
    name = ci18n.get("name", f"Calculator {cid}")
    intro = f"The {name} is a free online calculator that helps you compute results quickly and accurately."
    if lang == "es":
        intro = f"La {name} es una calculadora online gratuita que le ayuda a obtener resultados rápidos y precisos."
    elif lang == "fr":
        intro = f"Le {name} est un calculateur en ligne gratuit qui vous aide à obtenir des résultats rapides et précis."
    elif lang == "de":
        intro = f"Der {name} ist ein kostenloser Online-Rechner, der Ihnen hilft, schnell und genau Ergebnisse zu berechnen."
    elif lang == "it":
        intro = f"Il {name} è un calcolatore online gratuito che ti aiuta a ottenere risultati rapidi e precisi."
    elif lang == "pt":
        intro = f"O {name} é uma calculadora online gratuita que o ajuda a obter resultados rápidos e precisos."

    steps = calc.get("steps", [])
    mistakes = calc.get("mistakes", [])
    formula = calc.get("formula_display", "")
    example = calc.get("example_inputs", {})
    result_ctx = calc.get("result_context", "")
    inputs_i18n = ci18n.get("inputs", {})
    input_names = list(inputs_i18n.keys())

    lines = ['<section class="long-content">']
    lines.append(f'  <h2>What is the {esc(name)}?</h2>')
    lines.append(f'  <p>{esc(intro)}</p>')

    lines.append(f'\n  <h2>How to Use This Calculator</h2>')
    lines.append(f'  <ol>')
    for k in input_names:
        label = inputs_i18n.get(k, k)
        lines.append(f'    <li>Enter your <strong>{esc(label)}</strong>.</li>')
    lines.append(f'    <li>Click <strong>Calculate</strong> to see instant results.</li>')
    lines.append(f'  </ol>')

    if formula:
        lines.append(f'\n  <h2>Formula</h2>')
        lines.append(f'  <p>The calculator uses this formula:</p>')
        lines.append(f'  <pre class="formula-block">{esc(formula)}</pre>')

    if steps:
        lines.append(f'\n  <h2>Worked Example</h2>')
        if example:
            ex_vals = ", ".join(f"{k} = {v}" for k, v in example.items())
            lines.append(f'  <p>Using typical values ({esc(ex_vals)}):</p>')
        lines.append(f'  <ol>')
        for s in steps:
            lines.append(f'    <li>{esc(s)}</li>')
        lines.append(f'  </ol>')
        if result_ctx:
            lines.append(f'  <p><strong>Result summary:</strong> {esc(result_ctx)}</p>')

    if mistakes:
        lines.append(f'\n  <h2>Common Mistakes to Avoid</h2>')
        lines.append(f'  <ul>')
        for m in mistakes:
            lines.append(f'    <li>{esc(m)}</li>')
        lines.append(f'  </ul>')

    faqs = FAQ_TEMPLATES.get(lang, FAQ_TEMPLATES["en"])
    lines.append(f'\n  <h2>Frequently Asked Questions</h2>')
    lines.append(f'  <div class="faq-list">')
    for q, a in faqs:
        lines.append(f'    <div class="faq-item">')
        lines.append(f'      <button class="faq-q" aria-expanded="false">{esc(q)}</button>')
        lines.append(f'      <div class="faq-a"><p>{esc(a)}</p></div>')
        lines.append(f'    </div>')
    lines.append(f'  </div>')

    lines.append(f'</section>')
    return "\n".join(lines)

updated = 0
for lang in LANGS:
    i18n = json.loads((I18N_DIR / f"{lang}.json").read_text(encoding="utf-8"))
    calcs_i18n = i18n.get("calculators", {})
    content_dir = CONTENT_DIR / lang
    for fpath in content_dir.glob("*.html"):
        text = fpath.read_text(encoding="utf-8")
        lines_count = len(text.splitlines())
        if lines_count >= 80:
            continue
        cid = fpath.stem
        calc = calcs.get(cid)
        ci18n = calcs_i18n.get(cid, {})
        if not calc:
            print(f"  [SKIP] {lang}/{cid}.html — calc not found")
            continue
        html = build_html(cid, calc, ci18n, lang)
        fpath.write_text(html, encoding="utf-8")
        updated += 1
        print(f"  [OK] {lang}/{cid}.html -> {len(html):,} bytes")

print(f"\n[DONE] Rewrote {updated} content files")
