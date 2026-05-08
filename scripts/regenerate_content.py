#!/usr/bin/env python3
"""
Phase 4: Regenerate HTML long-form content for mismatched calculators.
Reads the list of calc IDs from scripts/mismatch_ids.txt (output of Phase 3),
then regenerates proper HTML for all 6 languages using the correct block_slug
from calc.json and the template functions in calc_content.py.

Run from project root: python scripts/regenerate_content.py [--all] [--dry-run] [--id 015]
  --all       regenerate ALL calculators (not just mismatched ones)
  --dry-run   preview without writing files
  --id NNN    regenerate only a specific calculator ID
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from calc_content import (
    HOW_TO_TITLE, FAQ_TITLE, FORMULA_TITLE,
    generate_intro, generate_how_to, generate_faq, generate_formula_explained,
)

CALC_DIR = ROOT / "src" / "calculators"
LANGS = ["en", "de", "es", "fr", "it", "pt"]
MISMATCH_IDS_FILE = ROOT / "scripts" / "mismatch_ids.txt"

# Fallback description templates when lang.json has no desc
FALLBACK_DESC = {
    "en": "Enter your values and get instant, accurate results.",
    "es": "Introduce los valores y obtén el resultado al instante.",
    "fr": "Saisissez vos valeurs pour un résultat instantané.",
    "pt": "Insira os valores e obtenha resultados instantâneos.",
    "de": "Geben Sie Ihre Werte ein und erhalten Sie sofort Ergebnisse.",
    "it": "Inserisci i valori e ottieni risultati immediati.",
}

STEP_INTRO = {
    "en": "Follow these steps to get a reliable result:",
    "es": "Sigue estos pasos para obtener un resultado fiable:",
    "fr": "Suivez ces étapes pour un résultat fiable :",
    "pt": "Siga estes passos para obter um resultado fiável:",
    "de": "Führen Sie diese Schritte aus, um ein zuverlässiges Ergebnis zu erhalten:",
    "it": "Segui questi passaggi per ottenere un risultato affidabile:",
}


def load_lang_json(calc_dir: Path, lang: str) -> dict:
    path = calc_dir / f"{lang}.json"
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_calc_json(calc_dir: Path) -> dict:
    path = calc_dir / "calc.json"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_faq_html(faqs: list[dict]) -> str:
    if not faqs:
        return ""
    items = []
    for faq in faqs:
        q = faq.get("q", "")
        a = faq.get("a", "")
        if q and a:
            items.append(
                f'<div class="faq-item">'
                f'<button class="faq-q" aria-expanded="false">{q}</button>'
                f'<div class="faq-a"><p>{a}</p></div>'
                f'</div>'
            )
    return "\n".join(items)


def build_html(calc_id: str, lang: str, calc_data: dict, lang_data: dict) -> str:
    block_slug = calc_data.get("block_slug", "")
    name = lang_data.get("name") or calc_data.get("slug", "").replace("-", " ").title()
    desc = lang_data.get("desc") or lang_data.get("seo_description") or FALLBACK_DESC.get(lang, "")

    intro = generate_intro(calc_id, lang, name, desc, block_slug)
    steps = generate_how_to(calc_id, block_slug, lang)
    formula_text = generate_formula_explained(block_slug, lang)
    faqs = generate_faq(calc_id, block_slug, lang)

    html_parts = ['<section class="long-content">']

    # Intro paragraph
    html_parts.append(f"<p>{intro}</p>")

    # How-to section
    if steps:
        how_to_title = HOW_TO_TITLE.get(lang, HOW_TO_TITLE["en"])
        step_intro = STEP_INTRO.get(lang, STEP_INTRO["en"])
        html_parts.append(f"<h2>{how_to_title}</h2>")
        html_parts.append(f"<p>{step_intro}</p>")
        html_parts.append("<ol>")
        for step in steps:
            html_parts.append(f"<li>{step}</li>")
        html_parts.append("</ol>")

    # Formula section
    if formula_text:
        formula_title = FORMULA_TITLE.get(lang, FORMULA_TITLE["en"])
        html_parts.append(f"<h2>{formula_title}</h2>")
        html_parts.append(f"<p>{formula_text}</p>")

    # FAQ section
    if faqs:
        faq_title = FAQ_TITLE.get(lang, FAQ_TITLE["en"])
        faq_html = build_faq_html(faqs)
        if faq_html:
            html_parts.append(f"<h2>{faq_title}</h2>")
            html_parts.append('<div class="faq-list">')
            html_parts.append(faq_html)
            html_parts.append("</div>")

    html_parts.append("</section>")
    return "\n".join(html_parts)


def regenerate_calculator(calc_dir: Path, dry_run: bool = False) -> int:
    """Regenerate all 6 language HTML files for a calculator. Returns count of files written."""
    calc_data = load_calc_json(calc_dir)
    if not calc_data:
        return 0

    calc_id = calc_data.get("id", calc_dir.name)
    block_slug = calc_data.get("block_slug", "")
    if not block_slug:
        print(f"  [SKIP] {calc_id}: no block_slug in calc.json")
        return 0

    written = 0
    for lang in LANGS:
        lang_data = load_lang_json(calc_dir, lang)
        html = build_html(calc_id, lang, calc_data, lang_data)
        if not html.strip():
            continue

        out_path = calc_dir / f"{lang}.html"
        if not dry_run:
            out_path.write_text(html, encoding="utf-8")
        written += 1

    return written


def get_target_ids(args: list[str]) -> list[str] | None:
    """Returns list of IDs to process, or None for all."""
    if "--all" in args:
        return None
    if "--id" in args:
        idx = args.index("--id")
        if idx + 1 < len(args):
            return [args[idx + 1].zfill(3)]
    if MISMATCH_IDS_FILE.exists():
        ids = MISMATCH_IDS_FILE.read_text(encoding="utf-8").splitlines()
        ids = [line.strip() for line in ids if line.strip()]
        return ids
    return None


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args

    if dry_run:
        print("DRY RUN — no files will be written.\n")

    target_ids = get_target_ids(args)

    if target_ids is None:
        print("Regenerating ALL calculators...")
        calc_dirs = sorted(d for d in CALC_DIR.iterdir() if d.is_dir())
    elif not target_ids:
        print(f"No IDs found in {MISMATCH_IDS_FILE}. Run Phase 3 first, or use --all.")
        sys.exit(1)
    else:
        print(f"Regenerating {len(target_ids)} mismatched calculators...")
        calc_dirs = []
        for cid in target_ids:
            cid_padded = cid.zfill(3)
            d = CALC_DIR / cid_padded
            if d.exists():
                calc_dirs.append(d)
            else:
                print(f"  [NOT FOUND] {cid_padded}")

    total_calcs = total_files = 0
    for calc_dir in calc_dirs:
        n = regenerate_calculator(calc_dir, dry_run)
        if n > 0:
            total_calcs += 1
            total_files += n
            print(f"  {'[DRY]' if dry_run else 'WRITTEN'} {calc_dir.name} — {n} files")

    label = "would write" if dry_run else "wrote"
    print(f"\nPhase 4 done. {label} {total_files} files across {total_calcs} calculators.")


if __name__ == "__main__":
    main()
