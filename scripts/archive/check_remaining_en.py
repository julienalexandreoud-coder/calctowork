"""Fix remaining issues: copy EN steps/mistakes to other langs, fix IT inputs."""
import json
from pathlib import Path
from collections import defaultdict

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")
LANGS = ["es", "fr", "it", "pt"]

# Check which calculators have EN data available
missing_en = []
for cid in [str(i) for i in range(1100, 1120)] + ["005", "003"]:
    for cf in sorted(CALC_DIR.glob("*.json")):
        with open(cf, "r", encoding="utf-8") as f:
            c = json.load(f)
        if c.get("id") == cid:
            en = c.get("i18n", {}).get("en", {})
            has_steps = bool(en.get("steps"))
            has_mistakes = bool(en.get("mistakes"))
            has_fd = bool(en.get("formula_display"))
            if not (has_steps and has_mistakes and has_fd):
                missing_en.append((cid, c["slug"], has_steps, has_mistakes, has_fd))
            break

print("EN also missing fields for:")
for cid, slug, st, ms, fd in missing_en:
    print(f"  {cid} {slug}: steps={st} mistakes={ms} formula_display={fd}")
