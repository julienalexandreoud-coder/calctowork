#!/usr/bin/env python3
"""Fix all English narrative text — unique, hand-crafted for every calculator."""

import json, os, glob

CALC = r"C:\Microsaas\obra\src\calculators"

f = {}

# ============================================================
# BLOCK 1 — estructuras (15 calcs)
# ============================================================

f["001"] = {  # hormigon-masa
    "steps": [
        "Calculate the surface area: 5 m × 3 m = 15 m²",
        "Multiply by slab thickness: 15 m² × 0.20 m = 3.0 m³ of concrete",
        "Determine cement bags: 3.0 m³ × 7 bags/m³ = 21 bags (50 kg each)",
        "Calculate sand volume: 3.0 m³ × 0.65 = 1.95 m³ of sand",
        "Calculate gravel volume: 3.0 m³ × 0.90 = 2.70 m³ of gravel"
    ],
    "mistakes": [
        "Using slab thickness under 15 cm — lightweight slabs crack under load",
        "Forgetting 5–10% extra for spillage and uneven subgrade",
        "Confusing cubic meters with square meters when placing the order"
    ],
    "result_context": "For a slab measuring {largo} m × {ancho} m × {espesor} m, you need {volumen} m³ of concrete — that's {cemento_sacos} cement bags, {arena_m3} m³ of sand, and {grava_m3} m³ of gravel.",
    "formula_display": "Volume (m³) = Length × Width × Thickness",
    "example_label": "Concrete needed for a 5 m × 3 m foundation slab, 20 cm thick",
}
f["002"] = {  # hormigon-armado
    "steps": [
        "Calculate surface area: 5 m × 3 m = 15 m²",
        "Multiply by thickness: 15 m² × 0.25 m = 3.75 m³ of reinforced concrete",
        "Cement requirement: 3.75 m³ × 7 bags/m³ = 27 bags (50 kg each)",
        "Sand volume: 3.75 m³ × 0.65 = 2.44 m³",
        "Gravel volume: 3.75 m³ × 0.90 = 3.38 m³",
        "Steel rebar weight: 3.75 m³ × 100 kg/m³ = 375 kg"
    ],
    "mistakes": [
        "Using the wrong steel ratio — 80–120 kg/m³ for beams, 50–80 for slabs",
        "Placing rebar without minimum concrete cover (typically 2.5–5 cm)",
        "Not adding 5–10% waste for material loss during pouring and vibration"
    ],
    "result_context": "The beam requires {volumen} m³ of reinforced concrete with {acero_kg} kg of steel rebar, plus {cemento_sacos} cement bags, {arena_m3} m³ of sand, and {grava_m3} m³ of gravel.",
    "formula_display": "Volume = Length × Width × Thickness; Steel = Volume × ratio",
    "example_label": "Reinforced concrete for a 5 m beam, 3 m wide, 25 cm thick, with 100 kg/m³ steel",
}
f["003"] = {  # zapata-aislada
    "steps": [
        "Calculate volume per footing: 1.5 m × 1.5 m × 0.40 m = 0.90 m³",
        "Multiply by number of footings: 0.90 m³ × 4 = 3.60 m³ total",
        "Add working space for excavation: 1.7 m × 1.7 m × 0.40 m × 4 = 4.62 m³ excavated",
        "Cement: 3.60 m³ × 7 bags/m³ = 26 bags",
        "Sand: 3.60 m³ × 0.65 = 2.34 m³",
        "Gravel: 3.60 m³ × 0.90 = 3.24 m³"
    ],
    "mistakes": [
        "Undersizing the footing for the column load — verify soil bearing capacity first",
        "Not leaving 10–15 cm working space around each side for formwork",
        "Confusing isolated footings with continuous strip footings — different reinforcement patterns"
    ],
    "result_context": "For {cantidad} isolated footings each {largo} m × {ancho} m × {canto} m deep: {volumen} m³ of concrete and {excavacion} m³ of excavation.",
    "formula_display": "Volume per footing = L × W × D; Total = volume × quantity",
    "example_label": "4 isolated footings, each 1.5 m × 1.5 m × 0.40 m",
}
f["004"] = {  # muro-contencion
    "steps": [
        "Calculate average thickness: (0.40 m + 0.20 m) ÷ 2 = 0.30 m",
        "Cross-sectional area: 2.5 m × 0.30 m = 0.75 m²",
        "Concrete volume: 10 m × 0.75 m² = 7.50 m³",
        "Cement: 7.50 m³ × 7 bags/m³ = 53 bags",
        "Sand and gravel from standard mix proportions"
    ],
    "mistakes": [
        "Not using the average thickness — the wall is trapezoidal, not rectangular",
        "Forgetting drainage behind the wall — hydrostatic pressure causes failure",
        "Underestimating excavation width for formwork access on both sides"
    ],
    "result_context": "The retaining wall needs {volumen} m³ of concrete with a trapezoidal profile tapering from {espesor_base} m base to {espesor_corona} m crown.",
    "formula_display": "Avg thickness = (base + crown) ÷ 2; Volume = L × H × avg thickness",
    "example_label": "10 m long retaining wall, 2.5 m high, 0.40 m base, 0.20 m crown",
}
f["005"] = {  # pilares-hormigon
    "steps": [
        "Cross-section per column: 0.30 m × 0.30 m = 0.09 m²",
        "Volume per column: 0.09 m² × 3 m = 0.27 m³",
        "Total for 6 columns: 0.27 m³ × 6 = 1.62 m³",
        "Cement: 1.62 m³ × 7 bags/m³ = 12 bags",
        "Steel rebar: 1.62 m³ × 120 kg/m³ = 195 kg"
    ],
    "mistakes": [
        "Confusing column width with depth — both affect load capacity differently",
        "Using slab steel ratios — columns need 100–150 kg/m³ of reinforcement",
        "Not accounting for overlap between columns, beams, and footings"
    ],
    "result_context": "{cantidad} rectangular columns require {volumen} m³ of concrete and {acero_kg} kg of steel rebar.",
    "formula_display": "Volume per column = W × D × H; Total = volume × quantity",
    "example_label": "6 concrete columns, each 0.30 m × 0.30 m × 3 m",
}
f["006"] = {  # vigas-hormigon
    "steps": [
        "Cross-section per beam: 0.25 m × 0.50 m = 0.125 m²",
        "Volume per beam: 0.125 m² × 5 m = 0.625 m³",
        "Total for 4 beams: 0.625 m³ × 4 = 2.50 m³",
        "Cement: 2.50 m³ × 7 bags/m³ = 18 bags",
        "Steel rebar: 2.50 m³ × 110 kg/m³ = 275 kg"
    ],
    "mistakes": [
        "Using the wrong depth-to-span ratio — depth should be span ÷ 14 approximately",
        "Placing rebar too close to the surface — maintain minimum concrete cover",
        "Not accounting for beam-column joint reinforcement"
    ],
    "result_context": "{cantidad} rectangular beams require {volumen} m³ of concrete and {acero_kg} kg of steel rebar.",
    "formula_display": "Volume per beam = L × W × H; Total = volume × quantity",
    "example_label": "4 concrete beams, each 5 m × 0.25 m × 0.50 m",
}
f["007"] = {  # forjado-vigueta
    "steps": [
        "Floor area: 8 m × 6 m = 48 m²",
        "Gross concrete volume: 48 m² × 0.25 m = 12 m³",
        "Subtract hollow block voids (~25%): 12 m³ × 0.75 = 9 m³ net concrete",
        "Cement: 9 m³ × 7 bags/m³ = 63 bags",
        "Calculate hollow blocks based on joist spacing"
    ],
    "mistakes": [
        "Not subtracting hollow block volume — overestimates concrete by 20–30%",
        "Using incorrect joist spacing — standard is 50–70 cm center-to-center",
        "Forgetting the screed topping layer — typically adds 4–5 cm"
    ],
    "result_context": "The {largo} m × {ancho} m joist floor requires {volumen} m³ of concrete and approximately {bloques} hollow blocks.",
    "formula_display": "Area = L × W; Volume = area × thickness × (1 − void ratio)",
    "example_label": "8 m × 6 m joist floor, 25 cm thick, 60 cm joist spacing",
}
f["008"] = {  # losa-hormigon
    "steps": [
        "Slab area: 6 m × 4 m = 24 m²",
        "Base volume: 24 m² × 0.15 m = 3.60 m³",
        "Add waste factor: 3.60 m³ × 1.10 = 3.96 m³ with 10% extra",
        "Cement: 3.96 m³ × 7 bags/m³ = 28 bags",
        "Sand and gravel from standard mix ratio"
    ],
    "mistakes": [
        "Pouring on uncompacted ground — causes settlement and cracking",
        "Using too dry a mix — makes leveling and finishing difficult",
        "Skipping the damp-proof membrane under ground-bearing slabs"
    ],
    "result_context": "Your ground slab requires {volumen} m³ of concrete — {cemento_sacos} cement bags, {arena_m3} m³ sand, {grava_m3} m³ gravel.",
    "formula_display": "Volume = L × W × thickness × (1 + waste%)",
    "example_label": "6 m × 4 m ground slab, 15 cm thick, with 10% waste allowance",
}
f["009"] = {  # cimiento-corrido
    "steps": [
        "Cross-sectional area: 0.60 m × 0.50 m = 0.30 m²",
        "Concrete volume: 20 m × 0.30 m² = 6 m³",
        "Excavation (with 10 cm working space each side): 20 m × 0.80 m × 0.50 m = 8 m³",
        "Cement: 6 m³ × 7 bags/m³ = 42 bags",
        "Sand and gravel from standard proportions"
    ],
    "mistakes": [
        "Making the footing too narrow for the wall load it supports",
        "Not compacting the trench bottom before pouring — causes uneven settlement",
        "Forgetting the blinding layer — 5–10 cm of lean concrete under the footing"
    ],
    "result_context": "For {largo} m of continuous strip footing: {volumen} m³ of concrete and {excavacion} m³ of earth to remove.",
    "formula_display": "Volume = L × W × D; Excavation = L × (W + margin) × D",
    "example_label": "20 m strip foundation, 0.60 m wide, 0.50 m deep",
}
f["010"] = {  # excavacion-tierra
    "steps": [
        "In-situ volume: 10 m × 5 m × 2 m = 100 m³",
        "Apply swell factor (clay soil, 30%): 100 m³ × 1.30 = 130 m³ loose",
        "Weight estimate (1.8 t/m³): 100 m³ × 1.8 = 180 tonnes",
        "Truck loads (10 m³ per truck): 130 m³ ÷ 10 = 13 loads"
    ],
    "mistakes": [
        "Forgetting the swell factor — excavated soil occupies 20–40% more volume",
        "Not allowing for safe slope angles or shoring in deep excavations",
        "Mixing in-situ volume with loose volume when ordering haulage"
    ],
    "result_context": "The excavation yields {volumen} m³ in-situ, expanding to {volumen_esponjado} m³ after digging — about {camiones} truck loads.",
    "formula_display": "Volume = L × W × D; Loose = volume × (1 + swell%)",
    "example_label": "Foundation pit 10 m × 5 m × 2 m in clay soil with 30% swell",
}
f["1101"] = {  # sod-turf
    "steps": [
        "Lawn area: 10 m × 8 m = 80 m²",
        "Add 10% waste for cutting: 80 m² × 1.10 = 88 m²",
        "Rolls needed (0.5 m² each): 88 m² ÷ 0.5 = 176 rolls",
        "Pallets (50 rolls per pallet): 176 ÷ 50 = 4 pallets (round up)"
    ],
    "mistakes": [
        "Not adding 5–10% for cuts, odd shapes, and damaged pieces",
        "Ordering sod too early — it must be laid within 24 hours of delivery",
        "Skipping soil prep — grade, fertilize, and water the base before laying"
    ],
    "result_context": "To cover {area} m² you need approximately {rollos} rolls of sod, which equals {pallets} pallets — including waste allowance.",
    "formula_display": "Area = L × W; Rolls = area × (1 + waste%) ÷ roll size",
    "example_label": "10 m × 8 m lawn using 0.5 m² sod rolls with 10% waste",
}
f["1102"] = {  # mulch
    "steps": [
        "Bed area: 5 m × 3 m = 15 m²",
        "Convert depth: 8 cm = 0.08 m",
        "Volume needed: 15 m² × 0.08 m = 1.2 m³",
        "Bags required (50 L each): 1.2 m³ × 1000 ÷ 50 = 24 bags"
    ],
    "mistakes": [
        "Applying mulch too thick — 5–10 cm is optimal; thicker suffocates plants",
        "Piling mulch against tree trunks and stems — promotes rot",
        "Using fresh wood chips that deplete soil nitrogen as they decompose"
    ],
    "result_context": "You need {volumen} m³ of mulch — about {bolsas} bags — to cover {area} m² at the specified depth.",
    "formula_display": "Area = L × W; Volume = area × depth; Bags = volume × 1000 ÷ bag L",
    "example_label": "5 m × 3 m garden bed, 8 cm deep, using 50 L bags",
}
f["1104"] = {  # roofing-shingle
    "steps": [
        "Flat roof area: 12 m × 8 m = 96 m²",
        "Adjust for 30° pitch: 96 m² ÷ cos(30°) = 110.9 m² effective",
        "Add 10% waste for hips and valleys: 110.9 m² × 1.10 = 122 m²",
        "Bundles (3 m² per bundle): 122 m² ÷ 3 = 41 bundles"
    ],
    "mistakes": [
        "Measuring floor area instead of roof surface — pitch increases surface area",
        "Not adding waste for valleys, hips, and ridges — 10–15% extra for complex roofs",
        "Forgetting underlayment, ridge caps, and starter strips in the order"
    ],
    "result_context": "Your roof has an effective area of {area_efectiva} m² and needs approximately {paquetes} shingle bundles with waste allowance.",
    "formula_display": "Area = L × W; Effective = area ÷ cos(pitch); Bundles = effective × (1 + waste%) ÷ coverage",
    "example_label": "12 m × 8 m roof with 30° pitch and 10% waste",
}
f["1116"] = {  # concrete-steps
    "steps": [
        "Volume per step: 0.30 m × 0.18 m × 1.2 m = 0.065 m³",
        "Total for 10 steps: 0.065 m³ × 10 = 0.65 m³",
        "Add 10% waste for formwork: 0.65 m³ × 1.10 = 0.72 m³",
        "Cement: 0.72 m³ × 7 bags/m³ = 5 bags"
    ],
    "mistakes": [
        "Making risers too tall — building codes typically limit to 18 cm maximum",
        "Not sloping treads slightly (1–2%) for rainwater drainage",
        "Forgetting to include top and bottom landings in the step count"
    ],
    "result_context": "Your {escalones} concrete steps require {volumen} m³ of concrete, including waste allowance for formwork.",
    "formula_display": "Volume per step = tread × riser × width; Total = volume × steps × (1 + waste%)",
    "example_label": "10 steps, 30 cm tread, 18 cm riser, 1.2 m wide",
}
f["1119"] = {  # landscape-rock
    "steps": [
        "Coverage area: 4 m × 3 m = 12 m²",
        "Convert depth: 5 cm = 0.05 m",
        "Volume needed: 12 m² × 0.05 m = 0.6 m³",
        "Weight (gravel density 1.6 t/m³): 0.6 m³ × 1.6 = 0.96 tonnes"
    ],
    "mistakes": [
        "Spreading rock too thin — under 3 cm allows weeds to push through",
        "Skipping landscape fabric — rocks sink into soil without a barrier",
        "Using the wrong rock size — 10–20 mm is standard for decorative gravel"
    ],
    "result_context": "You need {volumen} m³ of decorative rock, weighing approximately {peso} tonnes, to cover {area} m².",
    "formula_display": "Area = L × W; Volume = area × depth; Weight = volume × density",
    "example_label": "4 m × 3 m landscaping bed, 5 cm deep, standard gravel density",
}
f["1118"] = {  # retaining-wall-calculator
}  # skip — duplicate of 004

# ============================================================
# BLOCK 2 — mamposteria (Masonry) — 13 calcs
# ============================================================

f["011"] = {  # ladrillo-hueco
    "steps": [
        "Wall area: length × height = total m²",
        "Bricks per m² = 1 ÷ ((brick length + 1 cm joint) × (brick height + 1 cm joint))",
        "Total bricks: wall area × bricks per m²",
        "Add 5% for cuts and breakage",
        "Mortar volume: (brick count × joint volume per brick) + bedding mortar"
    ],
    "mistakes": [
        "Using face dimensions without the 1 cm mortar joint — undercounts bricks",
        "Ordering exactly the calculated amount — always add 5% for breakage",
        "Forgetting that hollow bricks need different mortar consistency than solid bricks"
    ],
    "result_context": "For a wall area of {area} m², you need approximately {bloques} hollow bricks and {mortero_m3} m³ of mortar.",
    "formula_display": "Bricks = area ÷ (brick face + joint)²; Mortar = brick count × avg joint volume",
    "example_label": "Calculate hollow bricks for a 10 m × 2.5 m interior wall",
}
f["012"] = {  # ladrillo-cara-vista
    "steps": [
        "Calculate visible wall area: length × height",
        "Subtract openings for windows and doors",
        "Face bricks per m² = 1 ÷ ((brick length + 1 cm) × (brick height + 1 cm))",
        "Total bricks = net area × bricks per m² × 1.05 (waste)",
        "Mortar for facing: thinner joints (8–10 mm) require less mortar than common brickwork"
    ],
    "mistakes": [
        "Not accounting for brick color variation — order from the same batch",
        "Forgetting to factor in half-bricks at corners and openings",
        "Using standard mortar color that clashes with the face brick aesthetic"
    ],
    "result_context": "Your facing brick wall requires approximately {bloques} face bricks and {mortero_m3} m³ of colored mortar.",
    "formula_display": "Bricks = visible area ÷ (brick + joint)² × 1.05",
    "example_label": "Face brick calculation for a 12 m × 2.7 m exterior wall with two windows",
}

# Continue writing more blocks...
# This script will be continued with all 461 calculators

def apply():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        if "bak" in fp or "monolithic" in fp or os.path.basename(fp) == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        cid = calc.get("id", "")
        if cid not in f: continue
        en = calc.setdefault("i18n", {}).setdefault("en", {})
        changed = False
        for k, v in f[cid].items():
            if not v: continue
            en[k] = v
            changed = True
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated} narrative fields")

apply()
