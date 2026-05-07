"""
Add mistakes field to all calculators that don't have at least 2.
Generates context-aware mistakes based on inputs, units, ranges, and block type.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

calcs = data["calculators"]

BLOCK_MISTAKES = {
    "estructuras": [
        "Not adding a 5–10% waste buffer for cuts and spillage",
        "Using the nominal dimension instead of the actual finished size",
        "Confusing metres with centimetres in input fields",
    ],
    "mamposteria": [
        "Not accounting for mortar joint thickness in quantity estimates",
        "Forgetting to add waste for broken or cut pieces",
        "Entering wall dimensions in centimetres instead of metres",
    ],
    "pavimentos": [
        "Not allowing for expansion joints in large areas",
        "Ordering exact area without waste for cuts and breakages",
        "Using indoor tiles for outdoor applications",
    ],
    "fontaneria": [
        "Ignoring pipe slope requirements for drainage",
        "Mixing up pipe diameter and radius in calculations",
        "Not accounting for pressure loss over long pipe runs",
    ],
    "electricidad": [
        "Ignoring voltage drop over long cable runs",
        "Using the wrong cable gauge for the current load",
        "Forgetting to include a safety margin for circuit breakers",
    ],
    "climatizacion": [
        "Oversizing or undersizing the unit for the space",
        "Ignoring insulation quality in heat-load calculations",
        "Not accounting for solar gain through windows",
    ],
    "carpinteria": [
        "Not allowing for timber shrinkage or expansion",
        "Using nominal sizes instead of finished dimensions",
        "Forgetting to include hinge and hardware clearances",
    ],
    "pintura": [
        "Calculating for one coat when two are needed",
        "Ignoring texture and porosity of the surface",
        "Not subtracting doors and windows from wall area",
    ],
    "gestion": [
        "Using outdated unit costs in estimates",
        "Ignoring overhead and profit margins",
        "Not updating calculations when scope changes",
    ],
    "salud": [
        "Entering weight in pounds but selecting kilograms",
        "Confusing height in centimetres with metres",
        "Not adjusting for activity level or medical conditions",
    ],
    "finanzas": [
        "Confusing annual and monthly interest rates",
        "Forgetting to include taxes or fees in totals",
        "Using simple interest when compound interest applies",
    ],
    "deportes": [
        "Using estimated weight instead of actual measured weight",
        "Ignoring rest time between sets in calorie estimates",
        "Entering distance in kilometres but selecting miles",
    ],
    "matematicas": [
        "Forgetting to check the domain of the function",
        "Mixing up radians and degrees for angle inputs",
        "Rounding intermediate results too aggressively",
    ],
    "ciencia": [
        "Using incorrect units for physical constants",
        "Ignoring significant figures in measurements",
        "Mixing up mass and weight in calculations",
    ],
    "quimica": [
        "Confusing molarity with molality",
        "Using the wrong molecular weight for a compound",
        "Ignoring temperature effects on reaction rates",
    ],
    "electronica": [
        "Ignoring component tolerances in circuit design",
        "Mixing up peak and RMS voltage values",
        "Forgetting to derate power dissipation at high temperatures",
    ],
    "clima": [
        "Using local time instead of UTC for solar calculations",
        "Ignoring altitude effects on temperature and pressure",
        "Using averages instead of extremes for design loads",
    ],
    "utilidades": [
        "Entering file size in MB but selecting GB",
        "Ignoring compression ratios in storage estimates",
        "Mixing up bits and bytes in bandwidth calculations",
    ],
    "fotografia": [
        "Ignoring crop factor when calculating focal length",
        "Using print DPI instead of sensor resolution",
        "Forgetting to account for aspect ratio differences",
    ],
    "transporte": [
        "Ignoring traffic and weather delays in time estimates",
        "Using average speed instead of realistic road speeds",
        "Not accounting for fuel stops on long journeys",
    ],
    "cotidiano": [
        "Entering incorrect units for the requested measurement",
        "Not double-checking the calculation before using it",
        "Rounding intermediate results too aggressively",
    ],
}

def generate_mistakes(calc):
    block = calc.get("block_slug", "cotidiano")
    inputs = calc.get("inputs", [])
    mistakes = []

    # Unit-confusion mistakes
    for inp in inputs:
        if inp.get("type") != "number":
            continue
        unit = inp.get("unit", "")
        key = inp["id"]
        if unit in ("m", "m²", "m³"):
            mistakes.append(f"Entering {key} in centimetres or millimetres instead of metres")
        elif unit in ("cm", "cm²"):
            mistakes.append(f"Entering {key} in metres instead of centimetres")
        elif unit == "mm":
            mistakes.append(f"Entering {key} in centimetres instead of millimetres")
        elif unit == "kg":
            mistakes.append(f"Confusing kilograms with grams or pounds for {key}")
        elif unit == "%":
            mistakes.append(f"Entering {key} as a decimal (0.05) instead of a percentage (5)")
        elif unit in ("km", "km/h"):
            mistakes.append(f"Confusing kilometres with miles for {key}")
        elif unit == "L":
            mistakes.append(f"Confusing litres with gallons or millilitres for {key}")

    # Range mistakes
    for inp in inputs:
        if inp.get("type") != "number":
            continue
        minv = inp.get("min")
        maxv = inp.get("max")
        key = inp["id"]
        if minv is not None and maxv is not None:
            try:
                mistakes.append(f"Using a {key} outside the realistic range of {minv}–{maxv}")
            except Exception:
                pass

    # Block-specific generic mistakes
    generic = BLOCK_MISTAKES.get(block, BLOCK_MISTAKES["cotidiano"])
    mistakes.extend(generic)

    # Deduplicate
    seen = set()
    unique = []
    for m in mistakes:
        low = m.lower()
        if low not in seen:
            seen.add(low)
            unique.append(m)

    return unique[:3]

updated = 0
for calc in calcs:
    existing = calc.get("mistakes", [])
    if len(existing) >= 2:
        continue
    calc["mistakes"] = generate_mistakes(calc)
    updated += 1

with open(CALCS_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added mistakes to {updated} calculators")
