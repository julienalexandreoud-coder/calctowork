"""Fix EN names by restoring from old git version if available, 
and fix missing i18n fields."""
import json, subprocess, sys, re
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Microsaas\obra")
CALC_DIR = ROOT / "src" / "calculators"

LANGS = ["en", "es", "de", "fr", "it", "pt"]

# ── Step 1: Extract old EN names from pre-restructure git commit ──
print("=== Step 1: Restoring EN names from old git ===")
try:
    # Get old i18n/en.json with per-calculator data
    result = subprocess.run(
        ["git", "show", "a498122:src/i18n/en.json"],
        capture_output=True, text=True, cwd=ROOT,
        encoding="utf-8", errors="replace"
    )
    if result.returncode == 0:
        old_en = json.loads(result.stdout)
        old_calcs = old_en.get("calculators", {})
        print(f"  Found {len(old_calcs)} calculator entries in old en.json")
        
        fixed_en_names = 0
        for cf in sorted(CALC_DIR.glob("*.json")):
            if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
                continue
            with open(cf, "r", encoding="utf-8") as f:
                calc = json.load(f)
            cid = calc.get("id", "")
            if not cid or cid not in old_calcs:
                continue
            
            old_name = old_calcs[cid].get("name", "")
            old_desc = old_calcs[cid].get("desc", "")
            old_seo_title = old_calcs[cid].get("seo_title", "")
            old_seo_desc = old_calcs[cid].get("seo_desc", old_calcs[cid].get("seo_description", ""))
            
            en_i18n = calc.get("i18n", {}).get("en", {})
            current_name = en_i18n.get("name", "")
            es_name = calc.get("i18n", {}).get("es", {}).get("name", "")
            slug = calc.get("slug", "")
            
            # Check if current EN name matches slug keywords or ES name
            slug_keywords = set(slug.lower().replace("-", " ").split())
            en_keywords = set(current_name.lower().split())
            common = slug_keywords & en_keywords
            
            # Also check if EN name looks like it belongs to a different calculator
            # by checking if it matches another calculator's slug
            if not common and old_name and old_name != current_name:
                # The old name is different - use it
                changed = False
                en_data = calc.setdefault("i18n", {}).setdefault("en", {})
                
                if current_name != old_name:
                    print(f"  Fixing EN name for {slug} (id={cid}): '{current_name}' -> '{old_name}'")
                    en_data["name"] = old_name
                    changed = True
                
                if old_desc and en_data.get("description", "") != old_desc:
                    en_data["desc"] = old_desc
                    en_data["description"] = old_desc
                    changed = True
                
                if old_seo_title and en_data.get("seo_title", "") != old_seo_title:
                    en_data["seo_title"] = old_seo_title
                    changed = True
                    
                if old_seo_desc:
                    en_data["seo_description"] = old_seo_desc
                    changed = True
                
                if changed:
                    fixed_en_names += 1
                    with open(cf, "w", encoding="utf-8") as f:
                        json.dump(calc, f, ensure_ascii=False, indent=2)
        
        print(f"  Fixed EN names for {fixed_en_names} calculators")
    else:
        print(f"  Could not read old git: {result.stderr}")
except Exception as e:
    print(f"  Error: {e}")

# ── Step 2: Restore old names for ALL languages (not just EN) ──
print("\n=== Step 2: Restoring ALL language names from old git ===")
all_fixed = {lang: 0 for lang in LANGS}
for lang in LANGS:
    try:
        result = subprocess.run(
            ["git", "show", f"a498122:src/i18n/{lang}.json"],
            capture_output=True, cwd=ROOT,
        )
        if result.returncode != 0:
            continue
        # Handle BOM: try utf-8-sig first, then utf-8
        raw = result.stdout
        try:
            old_i18n = json.loads(raw.decode("utf-8-sig"))
        except:
            old_i18n = json.loads(raw.decode("utf-8", errors="replace"))
        old_calcs = old_i18n.get("calculators", {})
        
        for cf in sorted(CALC_DIR.glob("*.json")):
            if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
                continue
            with open(cf, "r", encoding="utf-8") as f:
                calc = json.load(f)
            cid = calc.get("id", "")
            if not cid or cid not in old_calcs:
                continue
            
            old_entry = old_calcs[cid]
            lang_data = calc.setdefault("i18n", {}).setdefault(lang, {})
            
            changed = False
            # Restore name
            old_name = old_entry.get("name", "")
            if old_name and lang_data.get("name", "") != old_name:
                lang_data["name"] = old_name
                changed = True
            
            # Restore description
            old_desc = old_entry.get("desc", old_entry.get("description", ""))
            if old_desc and lang_data.get("description", "") != old_desc:
                lang_data["description"] = old_desc
                lang_data["desc"] = old_desc
                changed = True
            
            # Restore seo_title
            old_seo = old_entry.get("seo_title", "")
            if old_seo and lang_data.get("seo_title", "") != old_seo:
                lang_data["seo_title"] = old_seo
                changed = True
            
            # Restore seo_description
            old_seo_desc = old_entry.get("seo_desc", old_entry.get("seo_description", ""))
            if old_seo_desc and lang_data.get("seo_description", "") != old_seo_desc:
                lang_data["seo_description"] = old_seo_desc
                changed = True
            
            # Restore inputs labels
            old_inputs = old_entry.get("inputs", {})
            if old_inputs:
                for inp_id, inp_label in old_inputs.items():
                    current_labels = lang_data.setdefault("inputs", {})
                    if inp_id not in current_labels or not current_labels[inp_id]:
                        current_labels[inp_id] = inp_label
                        changed = True
            
            # Restore outputs labels
            old_outputs = old_entry.get("outputs", {})
            if old_outputs:
                for out_id, out_label in old_outputs.items():
                    current_labels = lang_data.setdefault("outputs", {})
                    if out_id not in current_labels or not current_labels[out_id]:
                        current_labels[out_id] = out_label
                        changed = True
            
            # Restore steps
            old_steps = old_entry.get("steps", [])
            if old_steps and not lang_data.get("steps"):
                lang_data["steps"] = old_steps
                changed = True
            
            # Restore mistakes
            old_mistakes = old_entry.get("mistakes", [])
            if old_mistakes and not lang_data.get("mistakes"):
                lang_data["mistakes"] = old_mistakes
                changed = True
            
            # Restore formula_display
            old_fd = old_entry.get("formula_display", "")
            if old_fd and not lang_data.get("formula_display"):
                lang_data["formula_display"] = old_fd
                changed = True
            
            # Restore result_context
            old_rc = old_entry.get("result_context", "")
            if old_rc and not lang_data.get("result_context"):
                lang_data["result_context"] = old_rc
                changed = True
            
            if changed:
                with open(cf, "w", encoding="utf-8") as f:
                    json.dump(calc, f, ensure_ascii=False, indent=2)
                all_fixed[lang] += 1
    
    except Exception as e:
        print(f"  Error processing {lang}: {e}")

for lang, count in all_fixed.items():
    print(f"  {lang}: restored data for {count} calculators")

# ── Step 3: Verify remaining issues ──
print("\n=== Step 3: Verification ===")
remaining_missing = defaultdict(list)
for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        calc = json.load(f)
    cid = calc.get("id", "")
    slug = calc.get("slug", cf.stem)
    i18n = calc.get("i18n", {})
    
    for lang in LANGS:
        lang_data = i18n.get(lang, {})
        if not lang_data:
            remaining_missing[(lang, "no_data")].append((slug, cid))
            continue
        for field in ["steps", "mistakes", "formula_display", "inputs", "name"]:
            if field not in lang_data or not lang_data.get(field):
                remaining_missing[(lang, field)].append((slug, cid))

print(f"Remaining issues after fix:")
for (lang, field), items in sorted(remaining_missing.items()):
    print(f"  [{lang}] {field}: {len(items)} calculators")
    if len(items) <= 5:
        for slug, cid in items:
            print(f"    {slug} (id={cid})")
