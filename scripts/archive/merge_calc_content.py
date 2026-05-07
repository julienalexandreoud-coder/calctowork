"""
Merge human-written SEO content files from kith-temp\calc-content
into src/content/{lang}/{id}.html in the obra project.

Only copies files for calculator IDs that exist in calculators.json.
"""
import json
import re
from pathlib import Path
from collections import Counter

# ── paths ─────────────────────────────────────────────────────────────────────
KITH_CONTENT = Path(r"C:\Users\julie\kith-temp\calc-content")
OBRA_ROOT    = Path(r"C:\Microsaas\obra")
CONTENT_DIR  = OBRA_ROOT / "src" / "content"
CALCS_JSON   = OBRA_ROOT / "src" / "calculators" / "calculators.json"

# ── load valid calculator IDs ─────────────────────────────────────────────────
with open(CALCS_JSON, "r", encoding="utf-8") as f:
    calcs = json.load(f)["calculators"]
valid_ids = {c["id"] for c in calcs}
print(f"Valid calculator IDs in obra project: {len(valid_ids)}")

# ── pattern: 001-hormigon-masa-en.html ────────────────────────────────────────
pattern = re.compile(r"^(\d+)-.+-(en|es)\.html$")

# ── scan kith-temp files ──────────────────────────────────────────────────────
to_merge = []  # (calc_id, lang, content)
skip_no_match = 0
skip_bad_id = 0

for fpath in sorted(KITH_CONTENT.glob("*.html")):
    m = pattern.match(fpath.name)
    if not m:
        skip_no_match += 1
        continue
    calc_id = m.group(1).zfill(3)
    lang = m.group(2)
    if calc_id not in valid_ids:
        skip_bad_id += 1
        continue
    to_merge.append((calc_id, lang, fpath.read_text(encoding="utf-8")))

lang_counts = Counter(l for _, l, _ in to_merge)
print(f"Mergeable files: {len(to_merge)} ({dict(lang_counts)})")
print(f"Skipped: {skip_no_match} bad pattern, {skip_bad_id} unknown ID")

# ── write to src/content/{lang}/{id}.html ─────────────────────────────────────
new_files = 0
updated = 0
skipped = 0

for calc_id, lang, content in to_merge:
    out_path = CONTENT_DIR / lang / f"{calc_id}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists():
        if out_path.read_text(encoding="utf-8").strip() == content.strip():
            skipped += 1
            continue
        updated += 1
        action = "Updated"
    else:
        new_files += 1
        action = "Created"

    out_path.write_text(content, encoding="utf-8")
    print(f"  {action} {lang}/{calc_id}.html")

print(f"\n{'='*60}")
print(f"Summary: {new_files} new, {updated} updated, {skipped} identical (skipped)")

# ── final state ───────────────────────────────────────────────────────────────
print(f"\nFinal state of src/content/:")
for lang_dir in sorted(CONTENT_DIR.iterdir()):
    if lang_dir.is_dir():
        n = len(list(lang_dir.glob("*.html")))
        print(f"  {lang_dir.name}: {n} files")
