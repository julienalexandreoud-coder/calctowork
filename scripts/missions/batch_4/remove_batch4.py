import json
from pathlib import Path

p = Path(r"C:\Microsaas\obra\src\calculators\calculators.json")
with open(p, "r", encoding="utf-8") as f:
    data = json.load(f)

original = len(data["calculators"])
data["calculators"] = [c for c in data["calculators"] if not (str(c["id"]).isdigit() and int(c["id"]) >= 1050)]

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Removed {original - len(data['calculators'])} batch 4 calculators")
