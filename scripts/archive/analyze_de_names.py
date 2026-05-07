"""Analyze DE name issues and check old git version."""
import json, subprocess, sys
from pathlib import Path

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")

# Check specific questionable DE names
print("=== DE names that look wrong ===")
suspect_ids = ["703", "704", "073", "101", "1106", "1108", "1109", "1112", "1113", "1114", "1116"]
for cid in suspect_ids:
    for cf in sorted(CALC_DIR.glob("*.json")):
        with open(cf, "r", encoding="utf-8") as f:
            c = json.load(f)
        if c.get("id") == cid:
            en = c.get("i18n",{}).get("en",{}).get("name","")
            de = c.get("i18n",{}).get("de",{}).get("name","")
            print(f'ID {cid:>4} slug={c["slug"]:40s} en={en:40s} de={de}')

# Check old git version for the EN -> DE mapping
print("\n=== Checking old git for DE names comparison ===")
try:
    # Show the old i18n/de.json calculators key to compare DE names
    result = subprocess.run(
        ["git", "show", "a498122:src/i18n/de.json"],
        capture_output=True, text=True, cwd=r"C:\Microsaas\obra"
    )
    if result.returncode == 0:
        old_de = json.loads(result.stdout)
        calcs = old_de.get("calculators", {})
        print(f"Old de.json had {len(calcs)} calculators")
        # Check the suspect IDs
        for cid in suspect_ids:
            if cid in calcs:
                old_name = calcs[cid].get("name", "")
                if old_name:
                    print(f"  ID {cid}: old DE name = '{old_name}'")
    else:
        print("Could not read old git version:", result.stderr)
except Exception as e:
    print(f"Error: {e}")
