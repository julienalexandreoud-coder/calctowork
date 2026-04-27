# -*- coding: utf-8 -*-
"""
Generate content for Batch 4 calculators using ContentEngineV2.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from content_engine_v2 import engine_v2

CONTENT_DIR = ROOT / "src" / "content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]
SCHEMAS_FILE = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

schemas = load_json(SCHEMAS_FILE)

def build_calc_obj(calc_json):
    block = calc_json.get("block", "")
    domain = {
        "matematicas": "math", "ciencia": "physics", "salud": "health",
        "finanzas": "finance", "cotidiano": "tech", "quimica": "tech",
        "electronica": "tech", "clima": "physics", "utilidades": "tech",
        "fotografia": "tech", "transporte": "tech", "ingenieria": "tech",
        "deportes": "health",
    }.get(block, "math")
    i18n = calc_json.get("i18n", {})
    return {
        "id": calc_json["id"],
        "block": block,
        "domain": domain,
        "concept": i18n.get("en", {}).get("name", "").split("–")[0].strip(),
        "i18n": i18n,
        "latex_formula": "",
        "use_cases": [],
        "steps": [],
    }

print(f"Generating content for {len(schemas['calculators'])} calculators...")
total = 0
for calc_json in schemas["calculators"]:
    calc = build_calc_obj(calc_json)
    for lang in LANGS:
        html = engine_v2.generate(calc, lang)
        out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        total += 1

print(f"[OK] Generated {total} content files with ContentEngineV2.")
