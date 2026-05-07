"""
Add Batch 4 calculators to tools_config.py TOOLS array.
"""
import json, re
from pathlib import Path

ROOT = Path(r"C:\Microsaas\obra")
SCHEMAS = ROOT / "scripts" / "missions" / "batch_4" / "schemas.json"
TOOLS_FILE = ROOT / "scripts" / "tools_config.py"

with open(SCHEMAS, "r", encoding="utf-8") as f:
    data = json.load(f)

new_entries = []
for c in data["calculators"]:
    slug = c["slug"]
    block = c.get("block", "")
    new_entries.append(f'''    {{"id": "{c['id']}", "cat": "E", "block": "{block}", "slugs": {{
        "es": "{slug}",
        "en": "{slug}",
        "fr": "{slug}",
        "pt": "{slug}",
        "de": "{slug}",
        "it": "{slug}",
    }}}},''')

# Insert before the closing ] of TOOLS
text = TOOLS_FILE.read_text(encoding="utf-8")
insert_text = "    # ── BATCH 4 (1050-1099) ─────────────────────────────────────────────\n" + "\n".join(new_entries) + "\n"

# Find the line with ]
lines = text.splitlines()
insert_idx = None
for i, line in enumerate(lines):
    if line.strip() == "]":
        insert_idx = i
        break

if insert_idx is not None:
    lines.insert(insert_idx, insert_text.rstrip())
    TOOLS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Added {len(new_entries)} tools to tools_config.py")
else:
    print("Could not find insertion point")
