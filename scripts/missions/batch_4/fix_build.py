import json
from pathlib import Path

ROOT = Path(r"C:\Microsaas\obra")
SCHEMAS = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"
I18N_DIR = ROOT / "src" / "i18n"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# Fix schemas: add block_slug, remove group and i18n from calc objects
with open(SCHEMAS, "r", encoding="utf-8") as f:
    data = json.load(f)

for c in data["calculators"]:
    c["block_slug"] = c.get("block", "")
    c.pop("group", None)
    c.pop("i18n", None)

with open(SCHEMAS, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Remove batch 4 entries from i18n files
for lang in LANGS:
    p = I18N_DIR / f"{lang}.json"
    with open(p, "r", encoding="utf-8") as f:
        i18n = json.load(f)
    calc_keys = i18n.get("calculators", {})
    keys_to_remove = [k for k in calc_keys if k.startswith("calc_10")]
    for k in keys_to_remove:
        del calc_keys[k]
    with open(p, "w", encoding="utf-8") as f:
        json.dump(i18n, f, indent=2, ensure_ascii=False)
    print(f"Cleaned {lang}.json, removed {len(keys_to_remove)} keys")

print("Fixed schemas and i18n")
