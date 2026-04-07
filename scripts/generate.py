#!/usr/bin/env python3
"""
ObraCalc – Static site generator
Generates 600 calculator pages + block pages + index pages + sitemap
"""

import json
import os
import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
CALCS_FILE = SRC / "calculators" / "calculators.json"
I18N_DIR = SRC / "i18n"
TEMPLATES_DIR = SRC / "templates"
CSS_SRC = SRC / "css" / "styles.css"
JS_SRC = SRC / "js" / "calculator.js"
PUBLIC = ROOT / "public"

# ── Config ───────────────────────────────────────────────────────────────────
LANGS = ["es", "en", "fr", "pt", "de", "it"]
BASE_URL = "https://obracalc.com"
BUILD_DATE = date.today().isoformat()

# Block icons (emoji) keyed by block_slug
BLOCK_ICONS = {
    "estructuras":  "🏗️",
    "mamposteria":  "🧱",
    "pavimentos":   "🪨",
    "fontaneria":   "🔧",
    "electricidad": "⚡",
    "climatizacion":"🌡️",
    "carpinteria":  "🪵",
    "pintura":      "🎨",
    "gestion":      "📊",
}

# ── AdSense placeholders (replace with real ad code) ─────────────────────────
ADSENSE_HEAD = ""
# ADSENSE_HEAD = """<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>"""

ADSENSE_BANNER = "<!-- AdSense banner 728×90 -->"
ADSENSE_RESPONSIVE = "<!-- AdSense responsive -->"

# ── Load data ────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_trans(raw: dict) -> dict:
    """Normalize i18n file keys to what the templates expect."""
    raw_calcs = raw.get("calculators", {})
    calcs_i18n = {
        cid: {
            "name": c.get("name", ""),
            "description": c.get("desc", c.get("description", "")),
            "seo_title": c.get("seo_title", c.get("name", "")),
            "seo_description": c.get("seo_desc", c.get("seo_description", "")),
            "inputs": c.get("inputs", {}),
            "outputs": c.get("outputs", {}),
        }
        for cid, c in raw_calcs.items()
    }
    return {
        "lang": raw.get("lang", ""),
        "lang_name": raw.get("lang_name", ""),
        "site_name": raw.get("site_name", "ObraCalc"),
        "site_tagline": raw.get("site_tagline", ""),
        "site_description": raw.get("site_description", ""),
        "nav_home": raw.get("nav_home", "Home"),
        "nav_calculators": raw.get("nav_tools", raw.get("nav_calculators", "Calculators")),
        "nav_about": raw.get("nav_about", ""),
        "footer_rights": raw.get("footer_rights", raw.get("footer_text", "")),
        "footer_disclaimer": raw.get("footer_disclaimer", ""),
        "btn_calculate": raw.get("calculate_btn", raw.get("btn_calculate", "Calculate")),
        "btn_reset": raw.get("reset_btn", raw.get("btn_reset", "Reset")),
        "btn_copy": raw.get("copy_btn", raw.get("btn_copy", "Copy results")),
        "label_results": raw.get("result_title", raw.get("label_results", "Results")),
        "label_inputs": raw.get("inputs_title", raw.get("label_inputs", "Inputs")),
        "label_related": raw.get("related_tools", raw.get("label_related", "Related")),
        "error_invalid": raw.get("error_invalid", "Invalid values."),
        "meta_suffix": raw.get("meta_suffix", "| ObraCalc"),
        # blocks keyed by block_slug
        "blocks": raw.get("block_slugs", raw.get("blocks", {})),
        "calculators": calcs_i18n,
    }


def load_translations():
    trans = {}
    for lang in LANGS:
        path = I18N_DIR / f"{lang}.json"
        raw = load_json(path)
        trans[lang] = normalize_trans(raw)
    return trans


def load_calculators():
    data = load_json(CALCS_FILE)
    # Support both a plain list and {"calculators": [...]}
    if isinstance(data, list):
        return data
    return data.get("calculators", data)


# ── Jinja2 environment ────────────────────────────────────────────────────────

def make_env():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


# ── Output helpers ────────────────────────────────────────────────────────────

def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ── Copy static assets ────────────────────────────────────────────────────────

def copy_assets():
    css_dest = PUBLIC / "css" / "styles.css"
    js_dest = PUBLIC / "js" / "calculator.js"
    css_dest.parent.mkdir(parents=True, exist_ok=True)
    js_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(CSS_SRC, css_dest)
    shutil.copy2(JS_SRC, js_dest)
    print(f"  [assets] Copied CSS and JS")


# ── Main generation ───────────────────────────────────────────────────────────

def generate():
    print("ObraCalc – Static Site Generator")
    print(f"  Build date : {BUILD_DATE}")
    print(f"  Languages  : {', '.join(LANGS)}")

    # Load data
    calculators = load_calculators()
    translations = load_translations()
    env = make_env()

    # Build lookup structures
    calc_by_id = {c["id"]: c for c in calculators}

    blocks_by_slug = {}  # block_slug → [calc, ...]
    for c in calculators:
        bs = c["block_slug"]
        blocks_by_slug.setdefault(bs, []).append(c)

    # Clear and recreate public
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    print(f"  Output dir : {PUBLIC}")

    copy_assets()

    # Templates
    calc_tpl = env.get_template("calculator.html.j2")
    index_tpl = env.get_template("index.html.j2")
    block_tpl = env.get_template("block.html.j2")
    sitemap_tpl = env.get_template("sitemap.xml.j2")

    sitemap_entries = []
    page_count = 0

    for lang in LANGS:
        t = translations[lang]
        calcs_i18n = t["calculators"]  # id → {name, description, inputs, outputs, ...}

        # ── Index page ──────────────────────────────────────────────────────
        index_html = index_tpl.render(
            lang=lang,
            t=t,
            all_langs=LANGS,
            blocks_by_slug=blocks_by_slug,
            calcs_i18n=calcs_i18n,
            block_icons=BLOCK_ICONS,
            adsense_head=ADSENSE_HEAD,
            adsense_banner=ADSENSE_BANNER,
            adsense_responsive=ADSENSE_RESPONSIVE,
        )
        write_file(PUBLIC / lang / "index.html", index_html)
        page_count += 1

        sitemap_entries.append({
            "loc": f"{BASE_URL}/{lang}/",
            "priority": "1.0",
            "alternates": [{"lang": al, "href": f"{BASE_URL}/{al}/"} for al in LANGS],
        })

        # ── Block pages ─────────────────────────────────────────────────────
        for block_slug, block_calcs in blocks_by_slug.items():
            block_name = t["blocks"].get(block_slug, block_slug)
            block_html = block_tpl.render(
                lang=lang,
                t=t,
                all_langs=LANGS,
                block_slug=block_slug,
                block_name=block_name,
                block_calcs=block_calcs,
                calcs_i18n=calcs_i18n,
                adsense_head=ADSENSE_HEAD,
                adsense_banner=ADSENSE_BANNER,
                adsense_responsive=ADSENSE_RESPONSIVE,
            )
            write_file(PUBLIC / lang / block_slug / "index.html", block_html)
            page_count += 1

            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{block_slug}/",
                "priority": "0.8",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{block_slug}/"} for al in LANGS
                ],
            })

        # ── Calculator pages ─────────────────────────────────────────────────
        for calc in calculators:
            cid = calc["id"]
            ci18n = calcs_i18n.get(cid, {})
            if not ci18n:
                print(f"  [WARN] Missing i18n for calc {cid} in lang {lang}")
                continue

            block_name = t["blocks"].get(calc["block_slug"], calc["block_slug"])

            # Resolve related calculators
            related_calcs = []
            for rel_id in calc.get("related", [])[:4]:
                rel = calc_by_id.get(rel_id)
                if rel:
                    rel_i18n = calcs_i18n.get(rel_id, {})
                    related_calcs.append({
                        "id": rel_id,
                        "slug": rel["slug"],
                        "block_slug": rel["block_slug"],
                        "name": rel_i18n.get("name", rel["slug"]),
                    })

            calc_html = calc_tpl.render(
                lang=lang,
                t=t,
                all_langs=LANGS,
                calc=calc,
                calc_i18n=ci18n,
                block_name=block_name,
                related_calcs=related_calcs,
                adsense_head=ADSENSE_HEAD,
                adsense_banner=ADSENSE_BANNER,
                adsense_responsive=ADSENSE_RESPONSIVE,
            )

            out_path = PUBLIC / lang / calc["block_slug"] / calc["slug"] / "index.html"
            write_file(out_path, calc_html)
            page_count += 1

            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{calc['block_slug']}/{calc['slug']}/",
                "priority": "0.7",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{calc['block_slug']}/{calc['slug']}/"}
                    for al in LANGS
                ],
            })

    # ── Sitemap ──────────────────────────────────────────────────────────────
    sitemap_xml = sitemap_tpl.render(
        sitemap_entries=sitemap_entries,
        build_date=BUILD_DATE,
    )
    write_file(PUBLIC / "sitemap.xml", sitemap_xml)

    # ── Root redirect to default language ────────────────────────────────────
    root_index = (
        '<!DOCTYPE html><html><head>'
        '<meta charset="UTF-8">'
        '<meta http-equiv="refresh" content="0;url=/es/">'
        '<link rel="canonical" href="https://obracalc.com/es/">'
        '</head><body>'
        '<a href="/es/">ObraCalc</a>'
        '</body></html>'
    )
    write_file(PUBLIC / "index.html", root_index)

    print(f"\n[OK] Generated {page_count} pages")
    print(f"[OK] Sitemap: {len(sitemap_entries)} URLs")
    print(f"[OK] Output: {PUBLIC}")
    print("\nDeploy with:  firebase deploy")


if __name__ == "__main__":
    generate()
