import json
from pathlib import Path

ROOT = Path(r"C:\Microsaas\obra")
SCHEMAS = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"
I18N_DIR = ROOT / "src" / "i18n"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

with open(SCHEMAS, "r", encoding="utf-8") as f:
    data = json.load(f)

# Generate minimal i18n for each calculator
for c in data["calculators"]:
    cid = c["id"]
    slug = c["slug"]
    block = c.get("block", "")
    inputs = c.get("inputs", [])
    outputs = c.get("outputs", [])
    
    # Base Spanish names
    name_es = slug.replace("-", " ").title()
    desc_es = f"Calculadora de {name_es}"
    
    i18n = {}
    for lang in LANGS:
        if lang == "es":
            i18n[lang] = {
                "name": name_es,
                "description": desc_es,
                "seo_title": f"{name_es} | CalcToWork",
                "seo_desc": desc_es,
                "inputs": {i["id"]: i["id"].replace("_", " ").title() for i in inputs},
                "outputs": {o["id"]: o["id"].replace("_", " ").title() for o in outputs},
            }
        else:
            i18n[lang] = {
                "name": name_es,
                "description": desc_es,
                "seo_title": f"{name_es} | CalcToWork",
                "seo_desc": desc_es,
                "inputs": {i["id"]: i["id"].replace("_", " ").title() for i in inputs},
                "outputs": {o["id"]: o["id"].replace("_", " ").title() for o in outputs},
            }
    
    c["i18n"] = i18n

with open(SCHEMAS, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added i18n to {len(data['calculators'])} calculators in schemas.json")
