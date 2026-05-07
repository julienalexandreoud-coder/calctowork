"""
Add missing calculators (1100-1119) to TOOLS in tools_config.py.
Inserts before the closing ] of the TOOLS list.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
TOOLS_FILE = ROOT / "scripts" / "tools_config.py"

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = __import__("json").load(f)

with open(TOOLS_FILE, "r", encoding="utf-8") as f:
    tools_text = f.read()

# Extract existing IDs from TOOLS
existing_ids = set(re.findall(r'"id"\s*:\s*"(\d+)"', tools_text))

missing = [c for c in data["calculators"] if c["id"] not in existing_ids]
print(f"Missing from TOOLS: {len(missing)} calculators")

BLOCK_CAT = {
    "estructuras": "C", "mamposteria": "C", "pavimentos": "A",
    "fontaneria": "D", "electricidad": "D", "climatizacion": "D",
    "carpinteria": "C", "pintura": "B", "gestion": "E",
    "matematicas": "E", "ciencia": "D", "salud": "D",
    "finanzas": "E", "cotidiano": "E", "quimica": "D",
    "electronica": "D", "clima": "D", "utilidades": "E",
    "fotografia": "E", "transporte": "E", "deportes": "E",
}

# Collect all existing slugs to avoid collisions
existing_slugs = set(re.findall(r'"(?:es|en|fr|pt|de|it)"\s*:\s*"([^"]+)"', tools_text))

new_tools = []
for calc in missing:
    cid = calc["id"]
    block = calc.get("block_slug", "cotidiano")
    base_slug = calc.get("slug", f"calc-{cid}")
    
    slug = base_slug
    counter = 1
    while slug in existing_slugs:
        slug = f"{base_slug}-{block}"
        if slug in existing_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
    existing_slugs.add(slug)
    
    cat = BLOCK_CAT.get(block, "C")
    new_tools.append({
        "id": cid,
        "cat": cat,
        "block": block,
        "slug": slug,
    })
    print(f"  {cid}: {slug} (block={block}, cat={cat})")

if not new_tools:
    print("Nothing to add.")
    exit(0)

# Build entries text
entries_text = ""
for tool in new_tools:
    entries_text += f'    {{"id": "{tool["id"]}", "cat": "{tool["cat"]}", "block": "{tool["block"]}", "slugs": {{\n'
    for lang in ["es", "en", "fr", "pt", "de", "it"]:
        entries_text += f'        "{lang}": "{tool["slug"]}",\n'
    entries_text = entries_text.rstrip(",\n") + "\n"
    entries_text += "    }},\n"

# Find the exact end of TOOLS list: the line with just ]
lines = tools_text.splitlines(keepends=True)
insert_idx = None
for i, line in enumerate(lines):
    if line.strip() == "]" and i > 0 and "TOOLS" in tools_text[:sum(len(l) for l in lines[:i+1])]:
        # Make sure this is the TOOLS closing bracket, not another list
        # Simple heuristic: it's before TOOL_BY_ID
        if "TOOL_BY_ID" in "".join(lines[i:]):
            insert_idx = i
            break

if insert_idx is None:
    # Fallback: find the last ] before TOOL_BY_ID
    tool_by_id_pos = tools_text.find("TOOL_BY_ID")
    if tool_by_id_pos == -1:
        print("ERROR: Could not find TOOL_BY_ID")
        exit(1)
    # Find the last ] before TOOL_BY_ID
    insert_idx = tools_text.rfind("]", 0, tool_by_id_pos)
    if insert_idx == -1:
        print("ERROR: Could not find ] before TOOL_BY_ID")
        exit(1)
    new_tools_text = tools_text[:insert_idx] + entries_text + tools_text[insert_idx:]
else:
    new_tools_text = "".join(lines[:insert_idx]) + entries_text + "".join(lines[insert_idx:])

with open(TOOLS_FILE, "w", encoding="utf-8") as f:
    f.write(new_tools_text)

print(f"\nAdded {len(new_tools)} entries to TOOLS")
