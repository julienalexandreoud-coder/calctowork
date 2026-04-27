# -*- coding: utf-8 -*-
"""
Batch 4 Auditor — Runs checks on schemas, content, and i18n.
Produces audit_report.json for the orchestrator.
"""
import json, re, hashlib
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Microsaas\obra")
SCHEMAS = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"
CONTENT_DIR = ROOT / "src" / "content"
I18N_DIR = ROOT / "src" / "i18n"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

with open(SCHEMAS, "r", encoding="utf-8") as f:
    schemas = json.load(f)

issues = []
duplicate_fingerprints = []
paragraph_hashes = defaultdict(list)
adsense_score = 100

# 1. Schema checks
for c in schemas["calculators"]:
    cid = c["id"]
    formula = c.get("formula", "")
    inputs = c.get("inputs", [])
    outputs = c.get("outputs", [])

    for i in inputs:
        if i["id"] not in formula:
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "critical", "category": "math", "message": f"input '{i['id']}' not in formula", "fix_hint": "Add input to formula or remove input"})
    for o in outputs:
        if o["id"] not in formula:
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "critical", "category": "math", "message": f"output '{o['id']}' not in formula", "fix_hint": "Add output to formula or remove output"})

    for i in inputs:
        if i.get("unit") in {"m", "kg", "L", "m²", "m³", "m/s", "km/h", "Pa", "bar", "psi", "N", "J", "W", "V", "A", "Ω", "Hz", "°C", "°F", "K", "s", "min", "h"} and not i.get("unit_options") and not i.get("unit_category"):
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "medium", "category": "inputs", "message": f"input '{i['id']}' has unit '{i['unit']}' but no unit_options/unit_category", "fix_hint": "Add unit_options and unit_category"})

    i18n = c.get("i18n", {})
    for lang in LANGS:
        if lang not in i18n or not i18n[lang].get("name") or not i18n[lang].get("description"):
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "high", "category": "i18n", "message": f"missing i18n for {lang}", "fix_hint": "Add complete i18n for language"})

    if not c.get("seo_title") and not i18n.get("es", {}).get("seo_title"):
        issues.append({"calc_id": cid, "slug": c["slug"], "severity": "medium", "category": "seo", "message": "missing seo_title", "fix_hint": "Add seo_title under 60 chars"})

# 2. Content checks
for c in schemas["calculators"]:
    cid = c["id"]
    for lang in LANGS:
        content_path = CONTENT_DIR / lang / f"{cid}.html"
        if not content_path.exists():
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "high", "category": "content", "message": f"missing content for {lang}", "fix_hint": f"Generate content at {content_path}"})
            adsense_score -= 2
            continue
        text = content_path.read_text(encoding="utf-8")
        words = len(text.split())
        if words < 200:
            issues.append({"calc_id": cid, "slug": c["slug"], "severity": "medium", "category": "content", "message": f"content too short ({words} words) for {lang}", "fix_hint": "Expand content to at least 400 words"})
            adsense_score -= 1

        # Check for generic boilerplate
        generic_phrases = ["Below, we explain", "This calculator is useful for", "Below we explain"]
        for phrase in generic_phrases:
            if phrase in text:
                issues.append({"calc_id": cid, "slug": c["slug"], "severity": "medium", "category": "content", "message": f"generic phrase found: '{phrase}' in {lang}", "fix_hint": "Rewrite with concept-specific text"})
                adsense_score -= 1

        # Paragraph fingerprinting for duplicates
        for p in re.findall(r'<p>(.*?)</p>', text, re.DOTALL):
            p_clean = re.sub(r'<.*?>', '', p).strip()
            if len(p_clean) > 50:
                h = hashlib.md5(p_clean.encode()).hexdigest()
                paragraph_hashes[h].append((cid, lang, p_clean[:80]))

# Find duplicate paragraphs across different calculators
for h, occurrences in paragraph_hashes.items():
    cids = set(o[0] for o in occurrences)
    if len(cids) > 1:
        duplicate_fingerprints.append({
            "hash": h,
            "calculators": sorted(cids),
            "snippet": occurrences[0][2]
        })
        adsense_score -= 2
        for cid in cids:
            issues.append({"calc_id": cid, "slug": "", "severity": "medium", "category": "content", "message": f"duplicate paragraph found across calculators", "fix_hint": "Rewrite content to be unique"})

# 3. Summary
critical = sum(1 for i in issues if i["severity"] == "critical")
high = sum(1 for i in issues if i["severity"] == "high")
medium = sum(1 for i in issues if i["severity"] == "medium")
low = sum(1 for i in issues if i["severity"] == "low")

passed = critical == 0 and high == 0 and adsense_score >= 85

report = {
    "batch_id": "batch_4",
    "audited_at": "2026-04-27T15:35:00",
    "summary": {"total_calculators": len(schemas["calculators"]), "critical": critical, "high": high, "medium": medium, "low": low},
    "issues": issues,
    "duplicate_content_fingerprints": duplicate_fingerprints,
    "adsense_score": max(0, adsense_score),
    "pass": passed
}

out = ROOT / "scripts" / "missions" / "batch_4" / "audit_report.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Audit complete: {critical} critical, {high} high, {medium} medium, {low} low")
print(f"AdSense score: {report['adsense_score']}, Pass: {passed}")
print(f"Report saved to {out}")
