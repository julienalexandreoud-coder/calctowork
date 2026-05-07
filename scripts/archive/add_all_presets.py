"""
Add comparison_presets to all calculators that don't have them.
Uses example_inputs + input ranges to generate 5 realistic preset rows.
Adds a _label key for scenario names based on block type.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

calcs = data["calculators"]

LABELS = {
    "estructuras":   ["Small", "Medium", "Large", "Extra Large", "Industrial"],
    "mamposteria":   ["Small wall", "Medium wall", "Large wall", "Room", "House perimeter"],
    "pavimentos":    ["Small patio", "Medium patio", "Large patio", "Driveway", "Parking lot"],
    "fontaneria":    ["Small bathroom", "Medium bathroom", "Large bathroom", "Apartment", "House"],
    "electricidad":  ["Small circuit", "Medium circuit", "Large circuit", "House", "Building"],
    "climatizacion": ["Small room", "Medium room", "Large room", "Office", "Warehouse"],
    "carpinteria":   ["Small door", "Standard door", "Large door", "Window", "Bay window"],
    "pintura":       ["Small room", "Medium room", "Large room", "Office", "Hall"],
    "gestion":       ["Small project", "Medium project", "Large project", "Complex", "Mega project"],
    "salud":         ["Child", "Teen", "Adult (F)", "Adult (M)", "Elderly"],
    "finanzas":      ["Starter", "Average", "High", "Premium", "Enterprise"],
    "deportes":      ["Beginner", "Intermediate", "Advanced", "Elite", "Pro"],
    "matematicas":   ["Small scale", "Medium", "Large", "Industrial", "Theoretical"],
    "ciencia":       ["Small scale", "Medium", "Large", "Industrial", "Theoretical"],
    "quimica":       ["Small scale", "Medium", "Large", "Industrial", "Theoretical"],
    "electronica":   ["Small circuit", "Medium circuit", "Large circuit", "Board", "System"],
    "clima":         ["Light", "Moderate", "Strong", "Severe", "Extreme"],
    "utilidades":    ["Basic", "Standard", "Advanced", "Pro", "Enterprise"],
    "fotografia":    ["Small print", "Standard", "Large poster", "Banner", "Billboard"],
    "transporte":    ["City", "Suburban", "Highway", "Long haul", "International"],
    "cotidiano":     ["Small", "Medium", "Large", "Extra Large", "Maximum"],
}

def generate_presets(calc):
    example = calc.get("example_inputs", {})
    inputs = calc.get("inputs", [])
    block = calc.get("block_slug", "cotidiano")
    labels = LABELS.get(block, LABELS["cotidiano"])

    numeric_inputs = [inp for inp in inputs if inp.get("type") == "number"]
    if not numeric_inputs:
        return None

    base = {}
    for inp in numeric_inputs:
        key = inp["id"]
        val = example.get(key, inp.get("default", 1))
        try:
            base[key] = float(val)
        except (TypeError, ValueError):
            base[key] = 1.0

    # Sort by range size descending
    def range_size(inp):
        try:
            return float(inp.get("max", 1)) - float(inp.get("min", 0))
        except Exception:
            return 1
    numeric_inputs.sort(key=range_size, reverse=True)

    main_inputs = numeric_inputs[:2]
    other_inputs = numeric_inputs[2:]

    presets = []
    scales = [0.5, 0.75, 1.0, 1.5, 2.0]

    for i, scale in enumerate(scales):
        row = {"_label": labels[i] if i < len(labels) else labels[-1]}
        for inp in main_inputs:
            key = inp["id"]
            val = base[key] * scale
            minv = inp.get("min")
            maxv = inp.get("max")
            if minv is not None:
                try:
                    val = max(val, float(minv))
                except Exception:
                    pass
            if maxv is not None:
                try:
                    val = min(val, float(maxv))
                except Exception:
                    pass
            step = inp.get("step", 1)
            try:
                step = float(step)
            except Exception:
                step = 1
            if step < 1:
                val = round(val, 3)
            elif step == 1:
                val = int(round(val))
            else:
                val = round(val / step) * step
                if step >= 1:
                    val = int(round(val))
                else:
                    val = round(val, 3)
            row[key] = val
        for inp in other_inputs:
            key = inp["id"]
            row[key] = base[key]
        presets.append(row)

    return presets

updated = 0
for calc in calcs:
    if calc.get("comparison_presets"):
        continue
    presets = generate_presets(calc)
    if presets:
        calc["comparison_presets"] = presets
        updated += 1

with open(CALCS_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added comparison_presets to {updated} calculators")
