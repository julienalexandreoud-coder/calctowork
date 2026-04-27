import json
from pathlib import Path

schemas_file = Path("scripts/missions/batch_4/schemas.json")
with open(schemas_file, "r", encoding="utf-8") as f:
    data = json.load(f)

calculators = data["calculators"]
errors = []
seen_ids = set()
seen_slugs = set()

for c in calculators:
    cid = c["id"]
    slug = c["slug"]
    if cid in seen_ids:
        errors.append(f"Duplicate ID: {cid}")
    seen_ids.add(cid)
    if slug in seen_slugs:
        errors.append(f"Duplicate slug: {slug}")
    seen_slugs.add(slug)

    formula = c.get("formula", "")
    inputs = c.get("inputs", [])
    outputs = c.get("outputs", [])

    for i in inputs:
        if i["id"] not in formula:
            errors.append(f"{cid}: input {i['id']} not in formula")
    for o in outputs:
        if o["id"] not in formula:
            errors.append(f"{cid}: output {o['id']} not in formula")

    try:
        code = formula.replace("return ", "RESULT = ")
        compile(code, "<string>", "exec")
    except SyntaxError as e:
        errors.append(f"{cid}: syntax error in formula: {e}")

if errors:
    print("VALIDATION ERRORS:")
    for e in errors:
        print(f"  - {e}")
else:
    print(f"All {len(calculators)} calculators passed validation!")
