#!/usr/bin/env python3
"""
CalcToWork – Static Site Generator v3.0
Generates 600 HTML pages with:
  - CalcToWork branding
  - Localized SEO slugs (flat: /{lang}/{slug}/)
  - Dynamic input grouping by category (A-E)
  - Category-based wastage defaults
  - Grouped form fields with section headings
"""

import json
import shutil
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from calc_content import (
    WASTAGE_LABEL, WASTAGE_PLACEHOLDER,
    NET_LABEL, TOTAL_LABEL,
    HOW_TO_TITLE, FAQ_TITLE,
    generate_intro, generate_how_to, generate_faq,
)
from tools_config import (
    TOOLS, TOOL_BY_ID,
    classify_input,
    GROUP_LABELS, GROUP_ICONS,
    WASTAGE_DEFAULTS, SHOW_WASTAGE,
)

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("ERROR: Jinja2 not installed.")
    sys.exit(1)

# ── Paths ──────────────────────────────────────────────────────────────────────
ROOT          = Path(__file__).parent.parent
SRC           = ROOT / "src"
CALCS_FILE    = SRC / "calculators" / "calculators.json"
I18N_DIR      = SRC / "i18n"
TEMPLATES_DIR = SRC / "templates"
CSS_SRC       = SRC / "css" / "styles.css"
JS_SRC        = SRC / "js" / "calculator.js"
PUBLIC        = ROOT / "public"

# ── Config ─────────────────────────────────────────────────────────────────────
LANGS      = ["es", "en", "fr", "pt", "de", "it"]
BASE_URL   = "https://calcto.work"
BRAND      = "CalcToWork"
BUILD_DATE = date.today().isoformat()

BLOCK_ICONS = {
    "estructuras":  "🏗️",
    "mamposteria":  "🧱",
    "pavimentos":   "🪨",
    "fontaneria":   "🔧",
    "electricidad": "⚡",
    "climatizacion": "🌡️",
    "carpinteria":  "🪵",
    "pintura":      "🎨",
    "gestion":      "📊",
}

COPIED_LABEL = {
    "es": "¡Copiado!", "en": "Copied!",
    "fr": "Copié !",   "pt": "Copiado!",
    "de": "Kopiert!",  "it": "Copiato!",
}

ADSENSE_HEAD       = ""
ADSENSE_BANNER     = "<!-- AdSense banner 728×90 -->"
ADSENSE_RESPONSIVE = "<!-- AdSense responsive -->"

PLACEHOLDER_HINTS = {
    "largo": "e.g. 5.0",    "ancho": "e.g. 3.0",     "alto": "e.g. 2.5",
    "altura": "e.g. 2.5",   "espesor": "e.g. 0.20",   "espesor_base": "e.g. 0.40",
    "espesor_bloque": "e.g. 20", "espesor_corona": "e.g. 0.20",
    "longitud": "e.g. 10",  "longitud_pica": "e.g. 2.0",
    "profundidad": "e.g. 1.5", "canto": "e.g. 0.50",  "base": "e.g. 0.30",
    "area": "e.g. 25",      "area_cubierta": "e.g. 80",
    "perimetro": "e.g. 20", "diametro": "e.g. 0.025",
    "kg_acero_m3": "e.g. 100", "kg_acero_m2": "e.g. 12",
    "capas": "e.g. 2",      "rendimiento": "e.g. 12",
    "habitantes": "e.g. 4", "dotacion": "e.g. 150",   "dias": "e.g. 2",
    "potencia": "e.g. 2000","voltaje": "e.g. 230",    "longitud_cable": "e.g. 20",
    "caida_max": "e.g. 3",  "temperatura": "e.g. 35", "humedad": "e.g. 60",
    "precio_kwh": "e.g. 0.18", "horas_dia": "e.g. 8",
    "costo_m2": "e.g. 800", "imprevistos": "e.g. 10",
    "horas": "e.g. 40",     "costo_hora": "e.g. 18",  "num_operarios": "e.g. 3",
    "costo_inicial": "e.g. 15000", "valor_residual": "e.g. 1500",
    "vida_util": "e.g. 10", "valor_inicial": "e.g. 100000",
    "edad_anos": "e.g. 15", "margen": "e.g. 20",      "iva": "e.g. 21",
    "separacion": "e.g. 0.20", "num_piezas": "e.g. 5",
    "largo_baldosa": "e.g. 60","ancho_baldosa": "e.g. 60",
    "largo_azulejo": "e.g. 30","ancho_azulejo": "e.g. 30",
    "desperdicio": "e.g. 10",
    "num_ventanas": "e.g. 4","num_puertas": "e.g. 2",
    "precio_m2": "e.g. 350","precio_kg": "e.g. 1.20",
    "caudal": "e.g. 15",    "presion_entrada": "e.g. 3.5",
    "u_muros": "e.g. 0.35", "u_techo": "e.g. 0.25",
    "t_ext": "e.g. -5",     "t_int": "e.g. 20",
    "cop": "e.g. 3.5",      "lambda": "e.g. 0.035",
    "consumo_dia": "e.g. 3000", "hsp": "e.g. 4.5",    "autonomia": "e.g. 2",
    "cantidad": "e.g. 4",   "num_ladrillos": "e.g. 500",
    "numero": "e.g. 6",     "num_escalones": "e.g. 14",
    "altura_total": "e.g. 2.8",
    "manos": "e.g. 2",      "rendimiento_m2_l": "e.g. 10",
    "pasadas": "e.g. 2",    "grano_inicial": "e.g. 60",
    "num_granos": "e.g. 3",
    "coste_eur": "e.g. 5000", "precio_dia_eur": "e.g. 250",
    "precio_m2_semana": "e.g. 1.50",
    "horas_dia": "e.g. 8",  "dias_obra": "e.g. 30",
    "num_trabajadores": "e.g. 3",
    "tam_pieza_cm": "e.g. 60", "m2_por_caja": "e.g. 1.44",
    "ancho_junta_mm": "e.g. 3",
}


# ── I/O helpers ────────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_trans(raw: dict) -> dict:
    """Map i18n file keys → template-expected keys."""
    raw_calcs = raw.get("calculators", {})
    calcs_i18n = {
        cid: {
            "name":            c.get("name", ""),
            "description":     c.get("desc", c.get("description", "")),
            "seo_title":       c.get("seo_title", c.get("name", "")),
            "seo_description": c.get("seo_desc", c.get("seo_description", "")),
            "inputs":          c.get("inputs", {}),
            "outputs":         c.get("outputs", {}),
        }
        for cid, c in raw_calcs.items()
    }
    return {
        "lang":            raw.get("lang", ""),
        "lang_name":       raw.get("lang_name", ""),
        "site_name":       BRAND,
        "site_tagline":    raw.get("site_tagline", ""),
        "site_description":raw.get("site_description", ""),
        "nav_home":        raw.get("nav_home", "Home"),
        "nav_calculators": raw.get("nav_tools", raw.get("nav_calculators", "Calculators")),
        "nav_about":       raw.get("nav_about", ""),
        "footer_rights":   raw.get("footer_rights", raw.get("footer_text", "")),
        "footer_disclaimer": raw.get("footer_disclaimer", ""),
        "btn_calculate":   raw.get("calculate_btn", raw.get("btn_calculate", "Calculate")),
        "btn_reset":       raw.get("reset_btn", raw.get("btn_reset", "Reset")),
        "btn_copy":        raw.get("copy_btn", raw.get("btn_copy", "Copy results")),
        "label_results":   raw.get("result_title", raw.get("label_results", "Results")),
        "label_inputs":    raw.get("inputs_title", raw.get("label_inputs", "Inputs")),
        "label_related":   raw.get("related_tools", raw.get("label_related", "Related")),
        "error_invalid":   raw.get("error_invalid", "Invalid values."),
        "meta_suffix":     f"| {BRAND}",
        "blocks":          raw.get("block_slugs", raw.get("blocks", {})),
        "calculators":     calcs_i18n,
    }


def load_translations() -> dict:
    result = {}
    for lang in LANGS:
        raw = load_json(I18N_DIR / f"{lang}.json")
        result[lang] = normalize_trans(raw)
    return result


def load_calculators() -> list:
    data = load_json(CALCS_FILE)
    return data.get("calculators", data) if isinstance(data, dict) else data


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_assets() -> None:
    assets = [
        (CSS_SRC,              PUBLIC / "css" / "styles.css"),
        (JS_SRC,               PUBLIC / "js"  / "calculator.js"),
        (SRC / "robots.txt",   PUBLIC / "robots.txt"),
        (SRC / "favicon.svg",  PUBLIC / "favicon.svg"),
    ]
    for src, dest in assets:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    print("  [assets] Copied CSS, JS, robots.txt and favicon")


def make_env() -> "Environment":
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def build_placeholders(input_keys: list, lang: str) -> dict:
    prefix_map = {
        "es": "ej.", "en": "e.g.", "fr": "ex.",
        "pt": "ex.", "de": "z.B.", "it": "es.",
    }
    prefix = prefix_map.get(lang, "e.g.")
    result = {}
    for key in input_keys:
        hint = PLACEHOLDER_HINTS.get(key, "")
        if hint:
            hint = hint.replace("e.g.", prefix)
        result[key] = hint
    return result


def build_input_groups(input_items: list, lang: str) -> list:
    """
    Build grouped input structure for template rendering.
    input_items: list of (key, label) tuples.
    Returns: [{id, label, icon, fields: [{key, label}]}, ...]
    """
    groups_ordered = []
    groups_data: dict = {}

    for key, label in input_items:
        gid = classify_input(key)
        if gid not in groups_data:
            groups_ordered.append(gid)
            groups_data[gid] = []
        groups_data[gid].append({"key": key, "label": label})

    return [
        {
            "id": gid,
            "label": GROUP_LABELS.get(gid, {}).get(lang, gid),
            "icon": GROUP_ICONS.get(gid, ""),
            "fields": groups_data[gid],
        }
        for gid in groups_ordered
    ]


# ── Redirect helpers ──────────────────────────────────────────────────────────

def make_redirect_html(target_url: str) -> str:
    return (
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        f'<meta http-equiv="refresh" content="0;url={target_url}">'
        f'<link rel="canonical" href="{target_url}">'
        '</head><body>'
        f'<a href="{target_url}">Redirecting…</a>'
        '</body></html>'
    )


def generate_legacy_redirects(calculators: list, public: Path) -> int:
    """
    Generate redirect pages from old /lang/block_slug/slug/ → new /lang/loc_slug/
    so bookmarks and any existing links still work.
    """
    count = 0
    for lang in LANGS:
        for calc in calculators:
            cid = calc["id"]
            tool_cfg = TOOL_BY_ID.get(cid)
            if not tool_cfg:
                continue
            old_slug = calc.get("slug", "")
            block_slug = calc.get("block_slug", "")
            loc_slug = tool_cfg["slugs"].get(lang, old_slug)
            if not old_slug or not block_slug:
                continue
            # Only write redirect if old path differs from new path
            old_path = public / lang / block_slug / old_slug / "index.html"
            new_url = f"/{lang}/{loc_slug}/"
            if not old_path.exists():
                write_file(old_path, make_redirect_html(new_url))
                count += 1
    return count


# ── Main generation ────────────────────────────────────────────────────────────

def generate() -> None:
    print(f"{BRAND} v3.0 - Static Site Generator")
    print(f"  Build date : {BUILD_DATE}")
    print(f"  Languages  : {', '.join(LANGS)}")
    print(f"  Base URL   : {BASE_URL}")

    calculators  = load_calculators()
    translations = load_translations()
    env          = make_env()

    calc_by_id     = {c["id"]: c for c in calculators}
    blocks_by_slug: dict = {}
    for c in calculators:
        blocks_by_slug.setdefault(c["block_slug"], []).append(c)

    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)
    print(f"  Output dir : {PUBLIC}")
    copy_assets()

    calc_tpl    = env.get_template("calculator.html.j2")
    index_tpl   = env.get_template("index.html.j2")
    block_tpl   = env.get_template("block.html.j2")
    sitemap_tpl = env.get_template("sitemap.xml.j2")

    sitemap_entries: list = []
    page_count = 0
    warn_count = 0

    for lang in LANGS:
        t          = translations[lang]
        calcs_i18n = t["calculators"]

        # Localized slug lookup for this language: {calc_id: slug}
        calc_url_by_id = {
            calc["id"]: TOOL_BY_ID[calc["id"]]["slugs"].get(lang, calc["slug"])
            for calc in calculators
            if calc["id"] in TOOL_BY_ID
        }

        # ── Index page ────────────────────────────────────────────────────────
        index_html = index_tpl.render(
            lang=lang, t=t, all_langs=LANGS,
            blocks_by_slug=blocks_by_slug,
            calcs_i18n=calcs_i18n,
            block_icons=BLOCK_ICONS,
            brand_name=BRAND,
            site_base_url=BASE_URL,
            calc_url_by_id=calc_url_by_id,
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

        # ── Block pages ───────────────────────────────────────────────────────
        for block_slug, block_calcs in blocks_by_slug.items():
            block_name = t["blocks"].get(block_slug, block_slug)
            block_html = block_tpl.render(
                lang=lang, t=t, all_langs=LANGS,
                block_slug=block_slug, block_name=block_name,
                block_calcs=block_calcs, calcs_i18n=calcs_i18n,
                brand_name=BRAND,
                site_base_url=BASE_URL,
                calc_url_by_id=calc_url_by_id,
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

        # ── Calculator pages ──────────────────────────────────────────────────
        for calc in calculators:
            cid = calc["id"]

            ci18n = calcs_i18n.get(cid)
            if not ci18n or not ci18n.get("name"):
                warn_count += 1
                continue

            tool_cfg = TOOL_BY_ID.get(cid)
            if not tool_cfg:
                print(f"  [WARN] No tool config for calc {cid} - skipping")
                warn_count += 1
                continue

            cat = tool_cfg["cat"]
            loc_slug = tool_cfg["slugs"].get(lang, tool_cfg["slugs"].get("es", calc["slug"]))
            alt_slugs = tool_cfg["slugs"]  # {lang: slug}

            block_name = t["blocks"].get(calc["block_slug"], calc["block_slug"])

            # ── Related calculators ──────────────────────────────────────────
            related_calcs = []
            for rel_id in calc.get("related", [])[:4]:
                rel = calc_by_id.get(rel_id)
                if rel:
                    rel_tool = TOOL_BY_ID.get(rel_id, {})
                    rel_ci18n = calcs_i18n.get(rel_id, {})
                    related_calcs.append({
                        "id": rel_id,
                        "name": rel_ci18n.get("name", rel["slug"]),
                        "url_path": rel_tool.get("slugs", {}).get(lang, rel["slug"]),
                        # keep for fallback
                        "slug": rel["slug"],
                        "block_slug": rel["block_slug"],
                    })

            # ── Content ──────────────────────────────────────────────────────
            intro_text   = generate_intro(cid, lang, ci18n["name"], ci18n["description"])
            how_to_steps = generate_how_to(calc["block_slug"], lang)
            faq          = generate_faq(calc["block_slug"], lang)

            # ── Grouped inputs ───────────────────────────────────────────────
            input_items = list(ci18n["inputs"].items())
            input_keys  = [k for k, _ in input_items]
            input_groups = build_input_groups(input_items, lang)
            input_placeholders = build_placeholders(input_keys, lang)

            # ── Wastage ──────────────────────────────────────────────────────
            show_wastage   = SHOW_WASTAGE.get(cat, False)
            wastage_default = WASTAGE_DEFAULTS.get(cat, 0)

            calc_html = calc_tpl.render(
                lang=lang, t=t, all_langs=LANGS,
                calc=calc, calc_i18n=ci18n,
                block_name=block_name,
                related_calcs=related_calcs,
                brand_name=BRAND,
                site_base_url=BASE_URL,
                # URL
                calc_url_path=loc_slug,
                calc_alt_slugs=alt_slugs,
                # Content
                intro_text=intro_text,
                how_to_steps=how_to_steps,
                faq=faq,
                howto_title=HOW_TO_TITLE.get(lang, HOW_TO_TITLE["en"]),
                faq_title=FAQ_TITLE.get(lang, FAQ_TITLE["en"]),
                # Inputs
                input_groups=input_groups,
                input_placeholders=input_placeholders,
                # Wastage
                show_wastage=show_wastage,
                wastage_default=wastage_default,
                wastage_label=WASTAGE_LABEL.get(lang, WASTAGE_LABEL["en"]),
                wastage_placeholder=WASTAGE_PLACEHOLDER.get(lang, "e.g. 10"),
                net_label=NET_LABEL.get(lang, NET_LABEL["en"]),
                total_label=TOTAL_LABEL.get(lang, TOTAL_LABEL["en"]),
                copied_label=COPIED_LABEL.get(lang, "Copied!"),
                # AdSense
                adsense_head=ADSENSE_HEAD,
                adsense_banner=ADSENSE_BANNER,
                adsense_responsive=ADSENSE_RESPONSIVE,
            )

            out_path = PUBLIC / lang / loc_slug / "index.html"
            write_file(out_path, calc_html)
            page_count += 1

            sitemap_entries.append({
                "loc": f"{BASE_URL}/{lang}/{loc_slug}/",
                "priority": "0.7",
                "alternates": [
                    {"lang": al, "href": f"{BASE_URL}/{al}/{tool_cfg['slugs'].get(al, loc_slug)}/"}
                    for al in LANGS
                ],
            })

    # ── Sitemap ───────────────────────────────────────────────────────────────
    sitemap_xml = sitemap_tpl.render(sitemap_entries=sitemap_entries, build_date=BUILD_DATE)
    write_file(PUBLIC / "sitemap.xml", sitemap_xml)

    # ── Root redirect ─────────────────────────────────────────────────────────
    write_file(PUBLIC / "index.html", (
        '<!DOCTYPE html><html><head>'
        '<meta charset="UTF-8">'
        f'<meta http-equiv="refresh" content="0;url=/es/">'
        f'<link rel="canonical" href="{BASE_URL}/es/">'
        f'</head><body><a href="/es/">{BRAND}</a></body></html>'
    ))

    # ── Legacy redirects (/lang/block_slug/slug/ → /lang/loc_slug/) ──────────
    redirect_count = generate_legacy_redirects(calculators, PUBLIC)

    print(f"\n[OK] Generated {page_count} pages")
    print(f"[OK] Redirects: {redirect_count} legacy URL redirects")
    if warn_count:
        print(f"[WARN] {warn_count} missing translations skipped")
    print(f"[OK] Sitemap : {len(sitemap_entries)} URLs")
    print(f"[OK] Output  : {PUBLIC}")
    print(f"\nDeploy with:  firebase deploy --only hosting")


if __name__ == "__main__":
    generate()
