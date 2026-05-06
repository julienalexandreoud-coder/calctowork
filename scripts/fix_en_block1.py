#!/usr/bin/env python3
"""Fix English content for Block 1 (estructuras) calculators."""

import json

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

FIXES = {
    "001": {  # hormigon-masa.json
        "name": "Mass Concrete Volume Calculator",
        "description": "Calculate the volume of mass concrete and the materials needed — cement bags, sand, and gravel — for foundations, slabs, and footings. Includes a waste factor for ordering.",
        "seo_title": "Mass Concrete Calculator — Volume, Cement & Gravel | CalcToWork",
        "seo_description": "Calculate concrete volume and materials (cement, sand, gravel) for mass concrete foundations. Enter slab dimensions and get exact cubic meters plus bag counts. Free tool with waste factor.",
        "inputs": {"largo": "Length (m)", "ancho": "Width (m)", "espesor": "Thickness (m)"},
        "outputs": {"volumen": "Concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Multiply 5 m × 3 m = 15 m² of surface area",
            "Multiply 15 m² × 0.20 m = 3 m³ of concrete volume",
            "Calculate materials: 3 m³ × 7 bags/m³ = 21 cement bags (50 kg each)",
            "Calculate sand: 3 m³ × 0.65 = 1.95 m³ of sand",
            "Calculate gravel: 3 m³ × 0.90 = 2.70 m³ of gravel"
        ],
        "mistakes": [
            "Using insufficient slab thickness (under 15 cm) — may cause cracking under load",
            "Forgetting to add 5–10% waste for spillage and uneven ground",
            "Confusing cubic meters with square meters when ordering concrete"
        ],
        "result_context": "The calculated volume of {volumen} m³ requires {cemento_sacos} cement bags, {arena_m3} m³ of sand and {grava_m3} m³ of gravel for a standard-strength mix.",
        "formula_display": "Volume = length × width × thickness",
        "example_label": "Calculate the concrete needed for a 5 m × 3 m foundation slab with 20 cm thickness.",
        "range_hints": {"largo": "Typical range: 3–10 m for residential slabs", "ancho": "Typical range: 2–5 m for residential slabs", "espesor": "Minimum 0.15 m for light loads, 0.20–0.30 m for standard loads"},
    },
    "002": {  # hormigon-armado.json
        "name": "Reinforced Concrete Calculator",
        "description": "Calculate the volume of reinforced concrete needed for beams, columns, and structural elements. Includes cement, sand, gravel, and steel reinforcement estimates.",
        "seo_title": "Reinforced Concrete Calculator — Volume & Rebar | CalcToWork",
        "seo_description": "Calculate reinforced concrete volume and materials including steel rebar, cement bags, sand, and gravel for structural elements. Free online tool with waste factor.",
        "inputs": {"largo": "Length (m)", "ancho": "Width (m)", "espesor": "Thickness (m)", "kg_acero_m3": "Steel ratio (kg/m³)"},
        "outputs": {"volumen": "Concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)", "acero_kg": "Rebar weight (kg)"},
        "steps": [
            "Calculate surface area: 5 m × 3 m = 15 m²",
            "Calculate volume: 15 m² × 0.25 m = 3.75 m³ of reinforced concrete",
            "Calculate cement: 3.75 m³ × 7 bags/m³ = 27 cement bags (50 kg each)",
            "Calculate sand: 3.75 m³ × 0.65 = 2.44 m³",
            "Calculate steel: 3.75 m³ × 100 kg/m³ = 375 kg of rebar"
        ],
        "mistakes": [
            "Using the wrong steel ratio — 80–120 kg/m³ is typical for beams, 50–80 kg/m³ for slabs",
            "Forgetting to account for concrete cover when placing rebar",
            "Not adding 5–10% waste for material loss during pouring"
        ],
        "result_context": "The calculated volume of {volumen} m³ needs {cemento_sacos} cement bags, {arena_m3} m³ of sand, {grava_m3} m³ of gravel and {acero_kg} kg of steel rebar.",
        "formula_display": "Volume = length × width × thickness; Steel = volume × steel ratio",
        "example_label": "Calculate reinforced concrete for a 5 m × 3 m beam with 25 cm thickness and 100 kg/m³ steel ratio.",
        "range_hints": {"largo": "Range: 2–15 m for structural beams", "ancho": "Range: 0.2–1 m for beam width", "espesor": "Range: 0.2–1 m for beam height", "kg_acero_m3": "Typical: 80–120 kg/m³ for beams, 50–80 for slabs"},
    },
    "003": {  # zapata-aislada.json
        "name": "Isolated Footing Calculator",
        "description": "Calculate the concrete volume and excavation needed for isolated spread footings. Determine footing dimensions based on column load and soil bearing capacity.",
        "seo_title": "Isolated Footing Calculator — Concrete & Excavation | CalcToWork",
        "seo_description": "Calculate isolated footing dimensions, concrete volume, rebar, and excavation for column foundations. Enter column load and soil capacity. Free construction tool.",
        "inputs": {"largo": "Footing length (m)", "ancho": "Footing width (m)", "canto": "Footing depth (m)", "cantidad": "Number of footings"},
        "outputs": {"volumen": "Total concrete volume (m³)", "excavacion": "Excavation volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Calculate volume per footing: 1.5 m × 1.5 m × 0.40 m = 0.90 m³",
            "Multiply by number of footings: 0.90 m³ × 4 = 3.60 m³ total concrete",
            "Add excavation margin: 1.7 m × 1.7 m × 0.40 m × 4 = 4.62 m³ of excavation",
            "Calculate cement: 3.60 m³ × 7 bags/m³ = 26 cement bags",
            "Calculate sand and gravel using standard mix ratio"
        ],
        "mistakes": [
            "Undersizing the footing for the column load — check soil bearing capacity first",
            "Not adding excavation margin (10–15 cm around each side)",
            "Confusing isolated footings with continuous strip footings — different designs"
        ],
        "result_context": "The calculation shows {volumen} m³ of concrete and {excavacion} m³ of excavation for {cantidad} isolated footings. Includes sand, gravel, and cement quantities.",
        "formula_display": "Volume per footing = length × width × depth; Total = volume × quantity",
        "example_label": "Calculate concrete and excavation for 4 isolated footings, each 1.5 m × 1.5 m × 0.40 m.",
        "range_hints": {"largo": "Typical: 0.8–3 m depending on load", "ancho": "Typical: 0.8–3 m depending on load", "canto": "Minimum 0.30 m for light loads, 0.40–0.60 m standard", "cantidad": "Number of footings in the foundation plan"},
    },
    "004": {  # muro-contencion.json
        "name": "Retaining Wall Calculator",
        "description": "Calculate the concrete volume, rebar, and excavation required for a gravity retaining wall. Enter wall dimensions to get material quantities and excavation estimates.",
        "seo_title": "Retaining Wall Calculator — Concrete & Rebar | CalcToWork",
        "seo_description": "Calculate retaining wall concrete volume, steel rebar, excavation and formwork. Enter wall height, base and crown thickness. Free structural calculator.",
        "inputs": {"largo": "Wall length (m)", "altura": "Wall height (m)", "espesor_base": "Base thickness (m)", "espesor_corona": "Crown thickness (m)"},
        "outputs": {"volumen": "Concrete volume (m³)", "excavacion": "Excavation volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Calculate average thickness: (0.40 m + 0.20 m) ÷ 2 = 0.30 m",
            "Calculate cross-sectional area: 2.5 m × 0.30 m = 0.75 m²",
            "Calculate volume: 10 m × 0.75 m² = 7.50 m³ of concrete",
            "Calculate cement: 7.50 m³ × 7 bags/m³ = 53 cement bags",
            "Calculate sand and gravel from standard mix proportions"
        ],
        "mistakes": [
            "Not accounting for the trapezoidal shape — use average thickness, not base alone",
            "Forgetting drainage provisions behind the wall to prevent hydrostatic pressure",
            "Underestimating excavation width — need room for formwork on both sides"
        ],
        "result_context": "The retaining wall requires {volumen} m³ of concrete with a trapezoidal cross-section from {espesor_base} m base to {espesor_corona} m crown.",
        "formula_display": "Avg thickness = (base + crown) ÷ 2; Volume = length × height × avg thickness",
        "example_label": "Calculate a 10 m long retaining wall, 2.5 m high, with 0.40 m base and 0.20 m crown thickness.",
        "range_hints": {"largo": "Typical: 5–50 m for garden/landscape walls", "altura": "Typical: 0.5–4 m — walls over 1.5 m need engineering", "espesor_base": "Rule of thumb: base = height × 0.4 to 0.6", "espesor_corona": "Minimum 0.20 m; typical 0.20–0.30 m"},
    },
    "005": {  # pilares-hormigon.json
        "name": "Concrete Column Calculator",
        "description": "Calculate the concrete volume and material quantities for reinforced concrete columns. Enter column dimensions and count for accurate material estimates.",
        "seo_title": "Concrete Column Calculator — Volume & Materials | CalcToWork",
        "seo_description": "Calculate concrete volume, cement bags, sand, gravel and rebar for rectangular columns. Enter dimensions and quantity. Free structural calculator with waste factor.",
        "inputs": {"ancho": "Column width (m)", "profundidad": "Column depth (m)", "altura": "Column height (m)", "cantidad": "Number of columns"},
        "outputs": {"volumen": "Total concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)", "acero_kg": "Rebar weight (kg)"},
        "steps": [
            "Calculate cross-sectional area: 0.30 m × 0.30 m = 0.09 m²",
            "Calculate volume per column: 0.09 m² × 3 m = 0.27 m³",
            "Multiply by number of columns: 0.27 m³ × 6 = 1.62 m³ total",
            "Calculate cement: 1.62 m³ × 7 bags/m³ = 12 cement bags",
            "Calculate rebar: 1.62 m³ × 120 kg/m³ = 195 kg of steel"
        ],
        "mistakes": [
            "Confusing column width with depth — both affect load capacity differently",
            "Using the same steel ratio as slabs — columns typically need 100–150 kg/m³",
            "Not accounting for column overlap with beams and footings"
        ],
        "result_context": "The calculation gives {volumen} m³ of concrete for {cantidad} columns. Material breakdown includes cement, sand, gravel, and steel reinforcement.",
        "formula_display": "Volume per column = width × depth × height; Total = volume × quantity",
        "example_label": "Calculate concrete for 6 columns, each 0.30 m × 0.30 m × 3 m.",
        "range_hints": {"ancho": "Typical: 0.20–0.60 m for residential columns", "profundidad": "Typical: 0.20–0.60 m", "altura": "Typical: 2.5–4 m per floor", "cantidad": "Based on structural plan"},
    },
    "006": {  # vigas-hormigon.json
        "name": "Concrete Beam Calculator",
        "description": "Calculate the concrete volume and reinforcement needed for rectangular concrete beams. Enter beam dimensions and quantity for accurate material takeoffs.",
        "seo_title": "Concrete Beam Calculator — Volume & Rebar | CalcToWork",
        "seo_description": "Calculate concrete volume, cement, sand, gravel and steel rebar for rectangular beams. Enter span, width, height and quantity. Free structural estimation tool.",
        "inputs": {"largo": "Beam length (m)", "ancho": "Beam width (m)", "espesor": "Beam height (m)", "cantidad": "Number of beams"},
        "outputs": {"volumen": "Total concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)", "acero_kg": "Rebar weight (kg)"},
        "steps": [
            "Calculate cross-section: 0.25 m × 0.50 m = 0.125 m²",
            "Calculate volume per beam: 0.125 m² × 5 m = 0.625 m³",
            "Multiply by quantity: 0.625 m³ × 4 = 2.50 m³ total concrete",
            "Calculate cement: 2.50 m³ × 7 bags/m³ = 18 cement bags",
            "Calculate rebar: 2.50 m³ × 110 kg/m³ = 275 kg of steel"
        ],
        "mistakes": [
            "Using the wrong beam depth-to-span ratio — depth should be span ÷ 12 to ÷ 18",
            "Placing rebar too close to the surface — check minimum concrete cover requirements",
            "Not accounting for beam intersections with columns or other beams"
        ],
        "result_context": "The calculation shows {volumen} m³ of concrete needed for {cantidad} beams. Includes cement, sand, gravel, and steel reinforcement quantities.",
        "formula_display": "Volume per beam = length × width × height; Total = volume × quantity",
        "example_label": "Calculate concrete for 4 beams, each 5 m long, 0.25 m wide, and 0.50 m high.",
        "range_hints": {"largo": "Typical: 2–10 m for residential beams", "ancho": "Typical: 0.20–0.40 m", "espesor": "Beam depth: typically span ÷ 14 = 0.35–0.70 m", "cantidad": "Count from structural drawings"},
    },
    "007": {  # forjado-vigueta.json
        "name": "Joist Floor Slab Calculator",
        "description": "Calculate the concrete volume and materials for a joist-and-block floor system. Enter floor dimensions and joist spacing for accurate concrete and block estimates.",
        "seo_title": "Joist Floor Calculator — Concrete & Blocks | CalcToWork",
        "seo_description": "Calculate concrete volume, cement, sand, gravel and hollow blocks for joist-and-block floor slabs. Enter floor area and joist spacing. Free construction calculator.",
        "inputs": {"largo": "Floor length (m)", "ancho": "Floor width (m)", "espesor": "Slab thickness (m)", "separacion": "Joist spacing (m)"},
        "outputs": {"volumen": "Concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)", "bloques": "Hollow blocks needed"},
        "steps": [
            "Calculate floor area: 8 m × 6 m = 48 m²",
            "Calculate concrete volume: 48 m² × 0.25 m = 12 m³ total",
            "Subtract void volume from hollow blocks (≈ 25%): 12 m³ × 0.75 = 9 m³ net concrete",
            "Calculate cement: 9 m³ × 7 bags/m³ = 63 cement bags",
            "Calculate number of hollow blocks based on spacing"
        ],
        "mistakes": [
            "Not subtracting the volume occupied by hollow blocks — overestimates concrete",
            "Using incorrect joist spacing — standard is 0.50–0.70 m center-to-center",
            "Forgetting to add screed/topping layer thickness (typically 4–5 cm)"
        ],
        "result_context": "The floor slab requires {volumen} m³ of concrete and approximately {bloques} hollow blocks for a {largo} m × {ancho} m joist-and-block floor.",
        "formula_display": "Area = length × width; Volume = area × thickness; Net concrete = volume × (1 − void ratio)",
        "example_label": "Calculate joist floor materials for an 8 m × 6 m floor with 25 cm slab thickness and 0.60 m joist spacing.",
        "range_hints": {"largo": "Typical: 4–15 m for residential floors", "ancho": "Typical: 3–10 m", "espesor": "Typical: 0.20–0.30 m including screed", "separacion": "Standard joist spacing: 0.50–0.70 m"},
    },
    "008": {  # losa-hormigon.json
        "name": "Concrete Slab Calculator",
        "description": "Calculate the concrete volume and materials needed for a ground-bearing concrete slab. Enter slab dimensions for cement, sand, gravel, and water estimates.",
        "seo_title": "Concrete Slab Calculator — Volume & Materials | CalcToWork",
        "seo_description": "Calculate the exact concrete volume, cement bags, sand and gravel for ground slabs. Enter length, width and thickness. Free tool with waste factor for ordering.",
        "inputs": {"largo": "Slab length (m)", "ancho": "Slab width (m)", "espesor": "Slab thickness (m)", "desperdicio": "Waste factor (%)"},
        "outputs": {"volumen": "Concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Calculate slab area: 6 m × 4 m = 24 m²",
            "Calculate base volume: 24 m² × 0.15 m = 3.60 m³",
            "Add waste: 3.60 m³ × 1.10 = 3.96 m³ including 10% waste",
            "Calculate cement: 3.96 m³ × 7 bags/m³ = 28 cement bags",
            "Calculate sand and gravel from standard mix proportions"
        ],
        "mistakes": [
            "Pouring on uncompacted sub-base — can cause settlement cracks",
            "Using too little water in the mix — makes concrete hard to work and finish",
            "Not including a vapor barrier (DPM) under ground-bearing slabs"
        ],
        "result_context": "The slab requires {volumen} m³ of concrete. Material breakdown: {cemento_sacos} cement bags, {arena_m3} m³ of sand, and {grava_m3} m³ of gravel.",
        "formula_display": "Volume = length × width × thickness × (1 + waste%)",
        "example_label": "Calculate concrete for a 6 m × 4 m ground slab with 15 cm thickness and 10% waste.",
        "range_hints": {"largo": "Typical: 3–15 m for residential slabs", "ancho": "Typical: 2–10 m", "espesor": "Minimum 0.10 m; standard 0.15 m for residential", "desperdicio": "Typically 5–10% for ground slabs"},
    },
    "009": {  # cimiento-corrido.json
        "name": "Continuous Strip Foundation Calculator",
        "description": "Calculate the concrete volume, excavation, and materials for continuous strip footings. Enter foundation dimensions for accurate concrete and rebar estimates.",
        "seo_title": "Strip Foundation Calculator — Concrete & Excavation | CalcToWork",
        "seo_description": "Calculate strip footing concrete volume, excavation, cement, sand, gravel and rebar. Enter foundation length, width and depth. Free construction estimation tool.",
        "inputs": {"largo": "Foundation length (m)", "ancho": "Footing width (m)", "canto": "Footing depth (m)"},
        "outputs": {"volumen": "Concrete volume (m³)", "excavacion": "Excavation volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Calculate cross-sectional area: 0.60 m × 0.50 m = 0.30 m²",
            "Calculate volume: 20 m × 0.30 m² = 6 m³ of concrete",
            "Calculate excavation: 20 m × 0.80 m × 0.50 m = 8 m³ of soil",
            "Calculate cement: 6 m³ × 7 bags/m³ = 42 cement bags",
            "Calculate sand and gravel from standard mix ratio"
        ],
        "mistakes": [
            "Making the footing too narrow for the wall load — width should match load-bearing requirements",
            "Not compacting the trench bottom before pouring — causes uneven settlement",
            "Forgetting to add blinding concrete (5–10 cm lean concrete) below the footing"
        ],
        "result_context": "The strip foundation requires {volumen} m³ of concrete and {excavacion} m³ of excavation for {largo} m of continuous footing.",
        "formula_display": "Volume = length × width × depth; Excavation = length × (width + margin) × depth",
        "example_label": "Calculate a 20 m long strip footing, 0.60 m wide and 0.50 m deep.",
        "range_hints": {"largo": "Total linear meters of foundation walls", "ancho": "Typical: 0.40–0.80 m depending on wall load", "canto": "Minimum 0.40 m; typical 0.50–0.70 m"},
    },
    "010": {  # excavacion-tierra.json
        "name": "Excavation Volume Calculator",
        "description": "Calculate the volume of earth to be excavated for foundations, trenches, and basements. Enter excavation dimensions and soil type for accurate volume estimates.",
        "seo_title": "Excavation Volume Calculator — Earthworks | CalcToWork",
        "seo_description": "Calculate excavation volume in cubic meters for foundations, trenches and basements. Enter length, width, depth and swell factor. Free earthworks estimation tool.",
        "inputs": {"largo": "Excavation length (m)", "ancho": "Excavation width (m)", "profundidad": "Excavation depth (m)", "esponjamiento": "Swell factor (%)"},
        "outputs": {"volumen": "In-situ volume (m³)", "volumen_esponjado": "Loose volume (m³)", "camiones": "Truck loads needed", "peso": "Soil weight (tonnes)"},
        "steps": [
            "Calculate in-situ volume: 10 m × 5 m × 2 m = 100 m³",
            "Apply swell factor for clay: 100 m³ × 1.30 = 130 m³ loose volume",
            "Calculate weight (density ~1.8 t/m³): 100 m³ × 1.8 = 180 tonnes",
            "Calculate truck loads (10 m³ truck): 130 m³ ÷ 10 = 13 truck loads"
        ],
        "mistakes": [
            "Forgetting the swell/bulking factor — excavated soil occupies 20–40% more volume",
            "Not accounting for safe slope or shoring in deep excavations",
            "Mixing in-situ volume with loose volume when ordering trucks"
        ],
        "result_context": "The excavation volume is {volumen} m³ in-situ, expanding to {volumen_esponjado} m³ after excavation with the swell factor applied.",
        "formula_display": "Volume = length × width × depth; Loose volume = volume × (1 + swell%)",
        "example_label": "Calculate excavation for a 10 m × 5 m × 2 m foundation pit in clay soil with 30% swell.",
        "range_hints": {"largo": "Based on foundation plan dimensions", "ancho": "Add 1–2 m working space around footings", "profundidad": "Depends on frost depth and foundation type", "esponjamiento": "Clay: 25–40%, Sand: 10–15%, Rock: 40–60%"},
    },
    "1101": {  # sod-turf-calculator.json
        "name": "Sod & Turf Calculator",
        "description": "Calculate how many rolls or pallets of sod you need to cover your lawn area. Enter lawn dimensions for accurate sod estimates with waste allowance.",
        "seo_title": "Sod Calculator — Turf Rolls & Pallets | CalcToWork",
        "seo_description": "Calculate the number of sod rolls or pallets needed for your lawn. Enter area dimensions and get exact quantities with waste factor. Free landscaping calculator.",
        "inputs": {"largo": "Lawn length (m)", "ancho": "Lawn width (m)", "rollo_m2": "Roll size (m²)", "desperdicio": "Waste factor (%)"},
        "outputs": {"area": "Total lawn area (m²)", "rollos": "Sod rolls needed", "pallets": "Pallets needed", "coste": "Estimated cost"},
        "steps": [
            "Calculate lawn area: 10 m × 8 m = 80 m²",
            "Add waste factor: 80 m² × 1.10 = 88 m² including 10% waste",
            "Calculate rolls (0.5 m² each): 88 m² ÷ 0.5 = 176 sod rolls",
            "Calculate pallets (50 rolls/pallet): 176 ÷ 50 = 4 pallets (rounded up)"
        ],
        "mistakes": [
            "Not adding 5–10% waste for cutting and irregular edges",
            "Ordering too late — sod should be installed within 24 hours of delivery",
            "Forgetting to prepare the soil before laying sod (grade, fertilize, water)"
        ],
        "result_context": "For an area of {area} m² you will need approximately {rollos} sod rolls ({pallets} pallets) including waste allowance.",
        "formula_display": "Area = length × width; Rolls = area × (1 + waste%) ÷ roll_size",
        "example_label": "Calculate sod needed for a 10 m × 8 m lawn with 0.5 m² rolls and 10% waste.",
        "range_hints": {"largo": "Measure your lawn area", "ancho": "Measure your lawn area", "rollo_m2": "Standard roll: 0.5 m²; big roll: 1 m²", "desperdicio": "5–10% for cutting and irregular shapes"},
    },
    "1102": {  # mulch-calculator.json
        "name": "Mulch Calculator",
        "description": "Calculate how much mulch you need for garden beds and landscaping. Enter bed dimensions and desired mulch depth for accurate volume estimates in bags or bulk.",
        "seo_title": "Mulch Calculator — Bags & Bulk Volume | CalcToWork",
        "seo_description": "Calculate the amount of mulch needed for garden beds and landscaping. Enter area and depth to get volume in cubic meters, bags, or bulk loads. Free tool.",
        "inputs": {"largo": "Bed length (m)", "ancho": "Bed width (m)", "profundidad": "Mulch depth (cm)", "bolsa_litros": "Bag size (liters)"},
        "outputs": {"area": "Bed area (m²)", "volumen": "Mulch volume (m³)", "bolsas": "Bags needed", "coste": "Estimated cost"},
        "steps": [
            "Calculate bed area: 5 m × 3 m = 15 m²",
            "Convert depth to meters: 8 cm = 0.08 m",
            "Calculate volume: 15 m² × 0.08 m = 1.2 m³ of mulch",
            "Calculate bags (50 L each): 1.2 m³ × 1000 ÷ 50 L = 24 bags"
        ],
        "mistakes": [
            "Applying mulch too thick — 5–10 cm is ideal; thicker can suffocate plants",
            "Piling mulch against tree trunks and plant stems — causes rot",
            "Using fresh wood chips that deplete nitrogen as they decompose"
        ],
        "result_context": "You need {volumen} m³ of mulch ({bolsas} bags) to cover {area} m² at the specified depth.",
        "formula_display": "Area = length × width; Volume = area × depth; Bags = volume × 1000 ÷ bag_size",
        "example_label": "Calculate mulch for a 5 m × 3 m garden bed with 8 cm depth using 50 L bags.",
        "range_hints": {"largo": "Measure your garden bed", "ancho": "Measure your garden bed", "profundidad": "Recommended: 5–10 cm for weed suppression", "bolsa_litros": "Common sizes: 40 L, 50 L, 60 L"},
    },
    "1104": {  # roofing-shingle-calculator.json
        "name": "Roofing Shingle Calculator",
        "description": "Calculate the number of shingle bundles and squares needed for your roof. Enter roof dimensions and pitch for accurate material estimates with waste factor.",
        "seo_title": "Roofing Shingle Calculator — Bundles & Squares | CalcToWork",
        "seo_description": "Calculate roofing shingle bundles, squares, and underlayment needed for your roof. Enter dimensions and pitch. Free roofing calculator with waste factor for cutting.",
        "inputs": {"largo": "Roof length (m)", "ancho": "Roof width (m)", "inclinacion": "Roof pitch (degrees)", "desperdicio": "Waste factor (%)"},
        "outputs": {"area": "Roof area (m²)", "area_efectiva": "Effective area (m²)", "paquetes": "Shingle bundles", "coste": "Estimated cost"},
        "steps": [
            "Calculate roof area: 12 m × 8 m = 96 m²",
            "Adjust for pitch (30°): 96 m² ÷ cos(30°) = 110.9 m² effective area",
            "Add waste: 110.9 m² × 1.10 = 122 m² with 10% waste",
            "Calculate bundles (3 m²/bundle): 122 m² ÷ 3 = 41 bundles"
        ],
        "mistakes": [
            "Measuring the floor plan instead of the actual roof surface — pitch increases area",
            "Not adding waste for valleys, hips, ridges — add 10–15% for complex roofs",
            "Forgetting underlayment and ridge cap shingles in the order"
        ],
        "result_context": "The effective roof area is {area_efectiva} m², requiring approximately {paquetes} shingle bundles including waste allowance.",
        "formula_display": "Area = length × width; Effective area = area ÷ cos(pitch); Bundles = area × (1+waste%) ÷ coverage",
        "example_label": "Calculate shingles for a 12 m × 8 m roof with 30° pitch and 10% waste.",
        "range_hints": {"largo": "Measure roof dimensions", "ancho": "Measure roof dimensions", "inclinacion": "Typical: 15–45° for residential roofs", "desperdicio": "10% simple roof, 15% complex with valleys/hips"},
    },
    "1116": {  # concrete-steps-calculator.json
        "name": "Concrete Steps Calculator",
        "description": "Calculate the concrete volume and materials needed for outdoor concrete steps. Enter step dimensions, number of steps, and riser height for accurate estimates.",
        "seo_title": "Concrete Steps Calculator — Volume & Materials | CalcToWork",
        "seo_description": "Calculate concrete volume, cement, sand and gravel for outdoor steps. Enter rise, run, width and number of steps. Free construction calculator with waste factor.",
        "inputs": {"huella": "Step tread (m)", "contrahuella": "Step riser (m)", "ancho": "Step width (m)", "escalones": "Number of steps"},
        "outputs": {"volumen": "Concrete volume (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)", "grava_m3": "Gravel (m³)"},
        "steps": [
            "Calculate volume per step: 0.30 m × 0.18 m × 1.2 m = 0.065 m³",
            "Multiply by number of steps: 0.065 m³ × 10 = 0.65 m³",
            "Add waste factor: 0.65 m³ × 1.10 = 0.72 m³ with 10% waste",
            "Calculate cement: 0.72 m³ × 7 bags/m³ = 5 cement bags"
        ],
        "mistakes": [
            "Making risers too tall — building code typically limits to 18 cm maximum",
            "Not sloping the tread slightly (1–2%) for water drainage",
            "Forgetting to include a landing at the top and bottom"
        ],
        "result_context": "The steps require {volumen} m³ of concrete for {escalones} steps including waste allowance for the formwork.",
        "formula_display": "Volume per step = tread × riser × width; Total = volume × steps × (1 + waste%)",
        "example_label": "Calculate concrete for 10 steps with 30 cm tread, 18 cm riser, and 1.2 m width.",
        "range_hints": {"huella": "Standard tread: 0.28–0.35 m", "contrahuella": "Standard riser: 0.15–0.18 m (code max)", "ancho": "Minimum 0.90 m; typical 1.0–1.5 m", "escalones": "Count all steps including landings"},
    },
    "1119": {  # landscape-rock-calculator.json
        "name": "Landscape Rock Calculator",
        "description": "Calculate how much decorative rock, gravel, or stone you need for landscaping. Enter area dimensions and desired depth for accurate volume and weight estimates.",
        "seo_title": "Landscape Rock Calculator — Gravel & Stone | CalcToWork",
        "seo_description": "Calculate decorative rock, gravel or stone needed for landscaping. Enter area and depth to get volume, weight in tonnes, and coverage. Free landscaping calculator.",
        "inputs": {"largo": "Area length (m)", "ancho": "Area width (m)", "profundidad": "Rock depth (cm)", "densidad": "Rock density (t/m³)"},
        "outputs": {"area": "Coverage area (m²)", "volumen": "Rock volume (m³)", "peso": "Weight (tonnes)", "coste": "Estimated cost"},
        "steps": [
            "Calculate coverage area: 4 m × 3 m = 12 m²",
            "Convert depth to meters: 5 cm = 0.05 m",
            "Calculate volume: 12 m² × 0.05 m = 0.6 m³",
            "Calculate weight (density 1.6 t/m³): 0.6 m³ × 1.6 = 0.96 tonnes"
        ],
        "mistakes": [
            "Applying rock too thin — under 3 cm allows weeds to grow through",
            "Forgetting landscape fabric underneath to prevent weeds and sinking",
            "Using the wrong rock size — decorative gravel is typically 10–20 mm"
        ],
        "result_context": "You need {volumen} m³ of rock ({peso} tonnes) to cover {area} m² at the specified depth.",
        "formula_display": "Area = length × width; Volume = area × depth; Weight = volume × density",
        "example_label": "Calculate decorative gravel for a 4 m × 3 m bed with 5 cm depth (standard gravel density 1.6 t/m³).",
        "range_hints": {"largo": "Measure your landscaping area", "ancho": "Measure your landscaping area", "profundidad": "Recommended: 3–8 cm for decorative rock", "densidad": "Gravel: 1.5–1.7 t/m³; Limestone: 1.6; Granite: 1.7"},
    },
}


def apply_fixes():
    import os, glob

    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue

        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        cid = calc.get("id", "")
        if cid not in FIXES:
            continue

        fix = FIXES[cid]
        en = calc.setdefault("i18n", {}).setdefault("en", {})

        changed = False
        for key, value in fix.items():
            if key in en and en[key] != value:
                en[key] = value
                changed = True

        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1
            print(f"  Fixed {name} ({cid})")

    print(f"\nUpdated {updated} English calculator files in Block 1")


if __name__ == "__main__":
    apply_fixes()
