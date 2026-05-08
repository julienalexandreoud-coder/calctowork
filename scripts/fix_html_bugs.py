#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive HTML bug fixer for all calculator content files.
Fixes:
  1. English section headings in non-English files
  2. English placeholder in "How It Works" section
  3. Encoding artifacts (mmÂ², â†', etc.)
  4. Typo "Calculatete" -> "Calculate" / language equivalent
Run: py scripts/fix_html_bugs.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALC_DIR = ROOT / "src" / "calculators"

# -----------------------------------------------------------------
# Section heading translations
# -----------------------------------------------------------------
HEADINGS = {
    "es": {
        "How to Use This Calculator":    "Cómo usar esta calculadora",
        "Follow these simple steps to get accurate results:":
                                         "Sigue estos pasos para obtener resultados precisos:",
        "How It Works":                  "Cómo funciona",
        "Input Fields":                  "Campos de entrada",
        "Result Outputs":                "Resultados",
        "Helpful Tips":                  "Consejos útiles",
        "Frequently Asked Questions":    "Preguntas frecuentes",
        "Formula":                       "Fórmula",
    },
    "de": {
        "How to Use This Calculator":    "So verwenden Sie diesen Rechner",
        "Follow these simple steps to get accurate results:":
                                         "Folgen Sie diesen Schritten für genaue Ergebnisse:",
        "How It Works":                  "Wie es funktioniert",
        "Input Fields":                  "Eingabefelder",
        "Result Outputs":                "Ergebnisse",
        "Helpful Tips":                  "Hilfreiche Tipps",
        "Frequently Asked Questions":    "Häufig gestellte Fragen",
        "Formula":                       "Formel",
    },
    "fr": {
        "How to Use This Calculator":    "Comment utiliser cette calculatrice",
        "Follow these simple steps to get accurate results:":
                                         "Suivez ces étapes simples pour obtenir des résultats précis :",
        "How It Works":                  "Comment ça fonctionne",
        "Input Fields":                  "Champs de saisie",
        "Result Outputs":                "Résultats",
        "Helpful Tips":                  "Conseils utiles",
        "Frequently Asked Questions":    "Foire aux questions",
        "Formula":                       "Formule",
    },
    "it": {
        "How to Use This Calculator":    "Come usare questo calcolatore",
        "Follow these simple steps to get accurate results:":
                                         "Segui questi semplici passaggi per ottenere risultati precisi:",
        "How It Works":                  "Come funziona",
        "Input Fields":                  "Campi di input",
        "Result Outputs":                "Risultati",
        "Helpful Tips":                  "Suggerimenti utili",
        "Frequently Asked Questions":    "Domande frequenti",
        "Formula":                       "Formula",
    },
    "pt": {
        "How to Use This Calculator":    "Como usar esta calculadora",
        "Follow these simple steps to get accurate results:":
                                         "Siga estes passos simples para obter resultados precisos:",
        "How It Works":                  "Como funciona",
        "Input Fields":                  "Campos de entrada",
        "Result Outputs":                "Resultados",
        "Helpful Tips":                  "Dicas úteis",
        "Frequently Asked Questions":    "Perguntas frequentes",
        "Formula":                       "Fórmula",
    },
}

# -----------------------------------------------------------------
# Generic placeholder replacement - "How It Works" body text
# -----------------------------------------------------------------
GENERIC_PLACEHOLDER = "This calculator helps you estimate the materials and quantities needed for your project."

PLACEHOLDER_TRANSLATIONS = {
    "es": "Esta calculadora te ayuda a estimar los materiales y cantidades necesarios para tu proyecto.",
    "de": "Dieser Rechner hilft Ihnen, die Materialien und Mengen für Ihr Projekt zu berechnen.",
    "fr": "Cette calculatrice vous aide à estimer les matériaux et quantités nécessaires pour votre projet.",
    "it": "Questo calcolatore ti aiuta a stimare i materiali e le quantità necessari per il tuo progetto.",
    "pt": "Esta calculadora ajuda você a estimar os materiais e quantidades necessários para o seu projeto.",
}

# -----------------------------------------------------------------
# Encoding artifact fixes (HTML-entity-like corruption)
# -----------------------------------------------------------------
ENCODING_FIXES = [
    ("mmÂ²", "mm²"),
    ("mÂ²",  "m²"),
    ("â†'",   "→"),
    ("âˆ'",   "−"),
    ("Â°",   "°"),
    ("Â´",   "´"),
    ("Ã©",   "é"),
    ("Ã¨",   "è"),
    ("Ã ",   "à"),
    ("Ã¹",   "ù"),
    ("Ã¼",   "ü"),
    ("Ã¶",   "ö"),
    ("Ã¤",   "ä"),
    ("Ã±",   "ñ"),
    ("Ã­",   "í"),
    ("Ã³",   "ó"),
    ("Ãº",   "ú"),
    ("Ã¡",   "á"),
    ("Ã‡",   "Ç"),
    ("Ã§",   "ç"),
]

# -----------------------------------------------------------------
# Typo fix (in English source steps that leak into other langs)
# -----------------------------------------------------------------
TYPO_FIXES = {
    "en": [("Calculatete", "Calculate")],
    "es": [("Calculatete", "Calcular"), ("Calculatete", "Calcular")],
    "de": [("Calculatete", "Berechnen"), ("Calculatete", "Berechnen")],
    "fr": [("Calculatete", "Calculer"), ("Calculatete", "Calculer")],
    "it": [("Calculatete", "Calcolare"), ("Calculatete", "Calcolare")],
    "pt": [("Calculatete", "Calcular"), ("Calculatete", "Calcular")],
}


def fix_html(content: str, lang: str) -> str:
    changed = False

    # 1. Fix section headings
    if lang in HEADINGS:
        for en_heading, translated in HEADINGS[lang].items():
            # Match <h2>English heading</h2>
            pattern = re.compile(
                r"(<h2>)" + re.escape(en_heading) + r"(</h2>)",
                re.IGNORECASE
            )
            new_content = pattern.sub(r"\g<1>" + translated + r"\g<2>", content)
            if new_content != content:
                content = new_content
                changed = True

            # Also match the standalone paragraph "Follow these simple steps..." outside h2
            if "Follow these simple steps to get accurate results:" in en_heading:
                p_pattern = re.compile(
                    r"(<p>)" + re.escape(en_heading) + r"(</p>)",
                    re.IGNORECASE
                )
                translated_p = HEADINGS[lang].get(en_heading, en_heading)
                new_content = p_pattern.sub(r"\g<1>" + translated_p + r"\g<2>", content)
                if new_content != content:
                    content = new_content
                    changed = True

    # 2. Fix generic English placeholder in How It Works
    if lang in PLACEHOLDER_TRANSLATIONS and GENERIC_PLACEHOLDER in content:
        content = content.replace(GENERIC_PLACEHOLDER, PLACEHOLDER_TRANSLATIONS[lang])
        changed = True

    # 3. Fix encoding artifacts
    for bad, good in ENCODING_FIXES:
        if bad in content:
            content = content.replace(bad, good)
            changed = True

    # 4. Fix typos
    for bad, good in TYPO_FIXES.get(lang, []):
        if bad in content:
            content = content.replace(bad, good)
            changed = True

    return content


def process_file(path: Path, lang: str, dry_run: bool) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            original = path.read_text(encoding="utf-8-sig")
        except Exception:
            return False

    fixed = fix_html(original, lang)
    if fixed == original:
        return False

    if not dry_run:
        path.write_text(fixed, encoding="utf-8")
    return True


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args

    if not CALC_DIR.exists():
        print(f"ERROR: {CALC_DIR} not found.")
        sys.exit(1)

    if dry_run:
        print("DRY RUN MODE — no files written\n")

    total = changed_files = 0
    by_lang: dict[str, int] = {}

    for calc_dir in sorted(CALC_DIR.iterdir()):
        if not calc_dir.is_dir():
            continue
        for lang in ["en", "es", "de", "fr", "it", "pt"]:
            html_path = calc_dir / f"{lang}.html"
            if not html_path.exists():
                continue
            total += 1
            if process_file(html_path, lang, dry_run):
                changed_files += 1
                by_lang[lang] = by_lang.get(lang, 0) + 1

    print(f"Checked {total} files.")
    print(f"Fixed {changed_files} files:")
    for lang, count in sorted(by_lang.items()):
        print(f"  {lang}: {count}")


if __name__ == "__main__":
    main()
