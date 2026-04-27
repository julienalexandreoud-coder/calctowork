# -*- coding: utf-8 -*-
"""
Regenerate ALL batch content files using ContentEngineV2 (high-quality unique content).
Run: python scripts/regen_all_content_v2.py
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from content_engine_v2 import engine_v2

CONTENT_DIR = ROOT / "src" / "content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

calcs_data = load_json(ROOT / "src" / "calculators" / "calculators.json")
i18n_data = {lang: load_json(ROOT / "src" / "i18n" / f"{lang}.json") for lang in LANGS}

# Build calc objects compatible with engine_v2
def build_calc_obj(calc_json):
    cid = calc_json["id"]
    i18n = {}
    for lang in LANGS:
        c = i18n_data[lang].get("calculators", {}).get(cid, {})
        i18n[lang] = {
            "name": c.get("name", ""),
            "description": c.get("description", ""),
            "inputs": c.get("inputs", {}),
            "outputs": c.get("outputs", {}),
        }
    block = calc_json.get("block_slug", "")
    domain = calc_json.get("domain", "")
    if not domain:
        domain = {
            "matematicas": "math", "ciencia": "physics", "salud": "health",
            "finanzas": "finance", "cotidiano": "tech", "quimica": "tech",
            "electronica": "tech", "clima": "tech", "utilidades": "tech",
            "fotografia": "tech", "transporte": "tech",
        }.get(block, "math")
    return {
        "id": cid,
        "block": block,
        "domain": domain,
        "concept": calc_json.get("concept", i18n.get("en", {}).get("name", "").split("–")[0].strip()),
        "i18n": i18n,
        "latex_formula": calc_json.get("latex_formula", ""),
        "use_cases": calc_json.get("use_cases", []),
        "steps": calc_json.get("steps", []),
    }

print(f"Regenerating content for {len(calcs_data['calculators'])} calculators...")
total = 0
for calc_json in calcs_data["calculators"]:
    # Only regenerate batch calculators (IDs >= 100) or all?
    # Regenerate ALL to ensure consistent quality
    calc = build_calc_obj(calc_json)
    for lang in LANGS:
        html = engine_v2.generate(calc, lang)
        out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        total += 1

print(f"[OK] Regenerated {total} content files with ContentEngineV2.")
