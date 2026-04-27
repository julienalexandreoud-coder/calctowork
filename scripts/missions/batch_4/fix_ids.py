import json, shutil
from pathlib import Path

ROOT = Path(r"C:\Microsaas\obra")
SCHEMAS = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"
I18N_DIR = ROOT / "src" / "i18n"
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
CONTENT_DIR = ROOT / "src" / "content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# Fix schemas: IDs to strings, i18n keys without calc_ prefix
with open(SCHEMAS, "r", encoding="utf-8") as f:
    data = json.load(f)

for c in data["calculators"]:
    c["id"] = str(c["id"])
    # i18n was removed earlier, but if it exists fix keys
    if "i18n" in c:
        for lang in c["i18n"]:
            c["i18n"][lang] = c["i18n"][lang]

with open(SCHEMAS, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Fix i18n files: change calc_1050 to 1050
for lang in LANGS:
    p = I18N_DIR / f"{lang}.json"
    with open(p, "r", encoding="utf-8") as f:
        i18n = json.load(f)
    calc_keys = i18n.get("calculators", {})
    keys_to_fix = [k for k in calc_keys if k.startswith("calc_")]
    for k in keys_to_fix:
        new_key = k.replace("calc_", "")
        calc_keys[new_key] = calc_keys.pop(k)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(i18n, f, indent=2, ensure_ascii=False)
    print(f"Fixed {lang}.json, renamed {len(keys_to_fix)} keys")

# Fix calculators.json: IDs must be strings
with open(CALCS_FILE, "r", encoding="utf-8") as f:
    calcs = json.load(f)

for c in calcs["calculators"]:
    c["id"] = str(c["id"])

# Remove any batch 4 calculators that were already merged (they might be broken)
original = len(calcs["calculators"])
calcs["calculators"] = [c for c in calcs["calculators"] if not (c["id"].isdigit() and int(c["id"]) >= 1050 and "block_slug" not in c)]
# Also re-merge batch 4 properly later
with open(CALCS_FILE, "w", encoding="utf-8") as f:
    json.dump(calcs, f, indent=2, ensure_ascii=False)
print(f"Fixed calculators.json, {original} → {len(calcs['calculators'])}")

print("All fixed")
