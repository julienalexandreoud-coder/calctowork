"""Fix remaining issues:
1. Copy EN steps/mistakes/formula_display to es/fr/it/pt for 20 new calculators (IDs 1100-1119)
2. Add Italian inputs for IDs 005 and 003 (copy from ES)
"""
import json
from pathlib import Path
from collections import defaultdict

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANGS = ["es", "fr", "it", "pt"]
NEW_IDS = [str(i) for i in range(1100, 1120)]
ITALIAN_MISSING_INPUTS = ["005", "003"]

fixed_calcs = defaultdict(int)

# 1. Copy EN data to other languages for calculators 1100-1119
for cid in NEW_IDS:
    for cf in sorted(CALC_DIR.glob("*.json")):
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        if calc.get("id") != cid:
            continue
        en = calc.get("i18n", {}).get("en", {})
        en_steps = en.get("steps", [])
        en_mistakes = en.get("mistakes", [])
        en_fd = en.get("formula_display", "")
        
        changed = False
        for lang in LANGS:
            ld = calc.setdefault("i18n", {}).setdefault(lang, {})
            if not ld.get("steps") and en_steps:
                ld["steps"] = en_steps
                changed = True
                fixed_calcs[f"{lang}_steps"] += 1
            if not ld.get("mistakes") and en_mistakes:
                ld["mistakes"] = en_mistakes
                changed = True
                fixed_calcs[f"{lang}_mistakes"] += 1
            if not ld.get("formula_display") and en_fd:
                ld["formula_display"] = en_fd
                changed = True
                fixed_calcs[f"{lang}_fd"] += 1
        
        if changed:
            with open(cf, "w", encoding="utf-8") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)

for k, v in sorted(fixed_calcs.items()):
    print(f"  Fixed {k}: {v} calculators")

# 2. Fix Italian inputs for IDs 005 and 003
print("\n--- Italian inputs fix ---")
for cid in ITALIAN_MISSING_INPUTS:
    for cf in sorted(CALC_DIR.glob("*.json")):
        with open(cf, "r", encoding="utf-8") as f:
            calc = json.load(f)
        if calc.get("id") != cid:
            continue
        es_inputs = calc.get("i18n", {}).get("es", {}).get("inputs", {})
        it = calc.setdefault("i18n", {}).setdefault("it", {})
        if "inputs" not in it or not it["inputs"]:
            it["inputs"] = dict(es_inputs)
            with open(cf, "w", encoding="utf-8") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            print(f"  Fixed IT inputs for {calc['slug']} (id={cid})")
        break

# 3. Verify final state
print("\n--- Final verification ---")
remaining = defaultdict(list)
for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        calc = json.load(f)
    cid = calc.get("id", "")
    slug = calc.get("slug", cf.stem)
    for lang in LANGS:
        ld = calc.get("i18n", {}).get(lang, {})
        if not ld:
            continue
        for field in ["steps", "mistakes", "formula_display", "inputs"]:
            if field in ["inputs"]:
                if field not in ld or not ld.get(field, {}):
                    remaining[(lang, field)].append((slug, cid))
            else:
                if field not in ld or not ld.get(field):
                    remaining[(lang, field)].append((slug, cid))

if remaining:
    for (lang, field), items in sorted(remaining.items()):
        print(f"  [{lang}] {field}: {len(items)} remaining")
else:
    print("  ALL FIELDS PRESENT [OK]")
