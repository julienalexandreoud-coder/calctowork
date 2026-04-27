import json, re
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Microsaas\obra")
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
I18N_DIR = ROOT / "src" / "i18n"
PUBLIC_DIR = ROOT / "public"

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    calcs_data = json.load(f)

calculators = calcs_data["calculators"]
all_ids = {c["id"] for c in calculators}
slugs = {c["id"]: c["slug"] for c in calculators}
calc_by_id = {c["id"]: c for c in calculators}

issues = defaultdict(list)

def add(issue_type, calc_id, detail):
    issues[issue_type].append((calc_id, slugs.get(calc_id, calc_id), detail))

# Determine which calculators have external i18n
has_external_i18n = set()
for c in calculators:
    for lang_file in I18N_DIR.glob("*.json"):
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        calc_keys = data.get("calculators", {})
        if c["id"] in calc_keys or c["slug"] in calc_keys or f"calc_{c['id']}" in calc_keys:
            has_external_i18n.add(c["id"])
            break

# Construction blocks that should show wastage
construction_blocks = {
    "estructuras", "mamposteria", "pavimentos",
    "fontaneria", "electricidad", "climatizacion",
    "carpinteria", "pintura", "gestion",
}

# ═══════════════════════════════════════════════════════════════════════════════
# 1. JSON STRUCTURAL AUDIT
# ═══════════════════════════════════════════════════════════════════════════════

for c in calculators:
    cid = c["id"]
    inputs = c.get("inputs", [])
    outputs = c.get("outputs", [])
    formula = c.get("formula", "")
    related = c.get("related", [])

    inp_ids = [i["id"] for i in inputs]
    out_ids = [o["id"] for o in outputs]

    seen_inp = set()
    for iid in inp_ids:
        if iid in seen_inp:
            add("duplicate_input_id", cid, f"input '{iid}' duplicated")
        seen_inp.add(iid)

    seen_out = set()
    for oid in out_ids:
        if oid in seen_out:
            add("duplicate_output_id", cid, f"output '{oid}' duplicated")
        seen_out.add(oid)

    for i in inputs:
        iid = i["id"]
        if iid not in formula:
            add("input_unused_in_formula", cid, f"input '{iid}' not referenced in formula")

    for o in outputs:
        oid = o["id"]
        if oid not in formula:
            add("output_missing_from_formula", cid, f"output '{oid}' not returned in formula")

    for rid in related:
        if rid not in all_ids:
            add("broken_related_link", cid, f"related '{rid}' does not exist")

    for i in inputs:
        iid = i["id"]
        itype = i.get("type", "")
        if iid in ("gender", "sexo", "sex") and itype != "select":
            add("broken_input_type", cid, f"'{iid}' should be select, is {itype}")
        if iid == "raid" and itype != "select":
            add("broken_input_type", cid, f"'{iid}' should be select, is {itype}")
        if iid in ("activity", "activity_factor", "factor_actividad") and itype == "number":
            if cid not in ("417", "434"):
                add("broken_input_type", cid, f"'{iid}' is number; should be select with labels")

    convertible_units = {"m","cm","mm","ft","in","km","mi","m²","m2","ft2","ft²","m³","m3","ft3","ft³","kg","g","lb","oz","L","mL","gal","L/min","m/s","km/h","mph","ft/s","knots","N","lbf","kN","Pa","bar","psi","atm","J","kJ","cal","kcal","Wh","kWh","W","kW","hp","V","kV","mV","A","mA","Hz","kHz","MHz","GHz","s","min","h","day","yr","K","°C","°F","deg","rad","GB","TB","MB","kbps","Mbps","Gbps","kg/m³","g/cm³","lb/ft³","kg/m²","g/m²"}
    for i in inputs:
        u = i.get("unit", "")
        if u in convertible_units and not i.get("unit_options") and not i.get("unit_category"):
            add("missing_unit_toggle", cid, f"input '{i['id']}' has unit '{u}' but no unit_options/unit_category")

    if cid not in has_external_i18n:
        i18n = c.get("i18n", {})
        for lang in ["es","en","fr","pt","de","it"]:
            if lang not in i18n:
                add("missing_i18n_lang", cid, f"missing i18n for {lang}")
                continue
            calc_i18n = i18n[lang]
            inp_labels = calc_i18n.get("inputs", {})
            out_labels = calc_i18n.get("outputs", {})
            for i in inputs:
                if i["id"] not in inp_labels:
                    add("missing_input_translation", cid, f"input '{i['id']}' missing translation in {lang}")
            for o in outputs:
                if o["id"] not in out_labels:
                    add("missing_output_translation", cid, f"output '{o['id']}' missing translation in {lang}")

    for lang, calc_i18n in c.get("i18n", {}).items():
        if isinstance(calc_i18n, dict):
            for k, v in calc_i18n.items():
                if isinstance(v, str) and v.strip() == "":
                    add("empty_i18n_string", cid, f"i18n[{lang}].{k} is empty")
                if isinstance(v, dict):
                    for sk, sv in v.items():
                        if isinstance(sv, str) and sv.strip() == "":
                            add("empty_i18n_string", cid, f"i18n[{lang}].{k}.{sk} is empty")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. HTML AUDIT (sample 800 files) - using calc mapping from slug
# ═══════════════════════════════════════════════════════════════════════════════

# Build slug -> calc_id mapping for all languages
slug_to_cid = {}
for c in calculators:
    cid = c["id"]
    # Map base slug
    slug_to_cid[c["slug"]] = cid
    # We can't easily map localized slugs without tools_config, but base slug is in path

html_files = sorted(PUBLIC_DIR.rglob("*.html"))[:800]
print(f"Scanning {len(html_files)} HTML files...")

for html_path in html_files:
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        continue
    rel = str(html_path.relative_to(PUBLIC_DIR))
    low = content.lower()

    # Determine calc_id from URL path (e.g., de/absoluter-wert/ or de/absoluter-wert/10m/)
    parts = rel.replace("\\", "/").split("/")
    base_slug = parts[1] if len(parts) >= 2 else ""
    cid = slug_to_cid.get(base_slug)

    if '<meta name="description" content="">' in content:
        add("empty_meta_description", rel, "Empty meta description")

    if '<link rel="canonical"' not in content:
        add("missing_canonical", rel, "No canonical tag")

    # FAQ sections
    faq_sections = re.findall(r'<section[^>]*class="[^"]*faq-section[^"]*"[^>]*>', low)
    faq_lists = re.findall(r'<div[^>]*class="[^"]*faq-list[^"]*"[^>]*>', low)
    faq_count = len(faq_sections) + len([fl for fl in faq_lists if 'faq-section' not in fl])
    if faq_count >= 2:
        add("duplicate_faq", rel, f"Found {faq_count} FAQ sections")

    # Wastage - only flag if actual input is rendered on non-construction calc
    # Skip parametric variants (paths with >2 segments)
    path_segments = rel.replace("\\", "/").rstrip("/").split("/")
    is_parametric = len(path_segments) > 2
    if not is_parametric and re.search(r'<input[^>]*name="desperdicio_merma"', content):
        if cid and calc_by_id.get(cid, {}).get("block_slug", "") not in construction_blocks:
            add("wastage_on_wrong_block", rel, "Wastage input rendered on non-construction calc")
        elif not cid:
            add("wastage_on_wrong_block", rel, "Wastage input on unknown calc")

    # Empty placeholder on actual input fields (skip parametric variants)
    if not is_parametric:
        input_tags = re.findall(r'<input[^>]*>', content, re.S)
        for inp in input_tags:
            if 'placeholder=""' in inp and 'id="input-desperdicio_merma"' not in inp:
                add("empty_placeholder", rel, f"Input has empty placeholder: {inp[:80]}")

    # Untranslated result placeholder on non-EN pages
    if "/en/" not in rel:
        m = re.search(r'<div class="result-placeholder">(.*?)</div>', content)
        if m and "Enter values and press Calculate" in m.group(1):
            add("untranslated_placeholder", rel, "English result placeholder on non-EN page")

    if "Technical Parameters" in content or "Parámetros técnicos" in content:
        if cid and calc_by_id.get(cid, {}).get("block_slug", "") not in construction_blocks:
            add("generic_group_label", rel, "'Technical Parameters' on non-construction calc")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. I18N FILE AUDIT
# ═══════════════════════════════════════════════════════════════════════════════

meta_keys = {"blocks","block_slugs","block_descriptions","calculators","table_headers","nav","footer","common","errors","share","seo","home","categories","result_placeholder"}
for i18n_file in I18N_DIR.glob("*.json"):
    lang = i18n_file.stem
    with open(i18n_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for key, val in data.items():
        if key in meta_keys:
            continue
        if isinstance(val, dict):
            if val.get("seo_desc", "") == "":
                add("empty_seo_desc_in_i18n", lang, f"key '{key}' empty seo_desc")
            if val.get("seo_title", "") == "":
                add("empty_seo_title_in_i18n", lang, f"key '{key}' empty seo_title")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*80)
print("CALCTOWORK COMPREHENSIVE AUDIT REPORT (CLEANED v3)")
print("="*80 + "\n")

total_issues = 0
for issue_type, items in sorted(issues.items(), key=lambda x: -len(x[1])):
    count = len(items)
    total_issues += count
    print(f"\n{issue_type.upper().replace('_', ' ')} ({count})")
    print("-" * 60)
    for item in items[:25]:
        print(f"  • [{item[0]}] {item[1]} — {item[2]}")
    if len(items) > 25:
        print(f"  ... and {len(items)-25} more")

print(f"\n{'='*80}")
print(f"TOTAL ISSUES FOUND: {total_issues}")
print(f"{'='*80}")

report_path = ROOT / "audit_report_v3.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("CALCTOWORK COMPREHENSIVE AUDIT REPORT (CLEANED v3)\n")
    f.write("="*80 + "\n\n")
    for issue_type, items in sorted(issues.items(), key=lambda x: -len(x[1])):
        f.write(f"\n{issue_type.upper().replace('_', ' ')} ({len(items)})\n")
        f.write("-" * 60 + "\n")
        for item in items:
            f.write(f"  • [{item[0]}] {item[1]} — {item[2]}\n")
    f.write(f"\nTOTAL ISSUES: {total_issues}\n")
print(f"Full report saved to: {report_path}")
