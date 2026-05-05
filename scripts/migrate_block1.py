#!/usr/bin/env python3
"""
migrate_block1.py - Update 22 specific calculators in calculators.json
Run: C:/Users/julie/AppData/Local/Programs/Python/Python314/python.exe scripts/migrate_block1.py
"""

import json
import sys
import os
from copy import deepcopy

INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "calculators", "calculators.json")
INPUT_PATH = os.path.abspath(INPUT_PATH)

TARGET_IDS = [
    "001", "002", "003", "004", "005", "006", "007", "008", "009", "010",
    "1101", "1102", "1104", "1116", "1119",
    "415", "425", "144", "1024", "1029", "1030", "1039",
]

# ---------------------------------------------------------------------------
#  Per-calculator update functions.  Each receives the full calculator dict
#  and mutates it in place.
# ---------------------------------------------------------------------------

def _ensure_field(calc, key, value):
    """Add key=value only if key does not already exist."""
    if key not in calc:
        calc[key] = value


def _update_field(calc, key, value):
    """Set or overwrite key=value."""
    calc[key] = value


# ============================== BLOCK 1 =====================================

def update_001(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "tags", ["concrete", "slab", "foundation", "cement", "construction", "materials"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "volumen", "min": 0, "max": 50,
        "zones": [
            {"min": 0, "max": 1, "label": "Small pour", "color": "#4CAF50"},
            {"min": 1, "max": 5, "label": "Medium pour", "color": "#FF9800"},
            {"min": 5, "max": 50, "label": "Large pour", "color": "#F44336"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "faqs", [
        {"question": "What concrete density does this calculator use?",
         "answer": "This calculator uses standard normal-weight concrete at 2400 kg/m\u00b3 (150 lb/ft\u00b3). For lightweight concrete, multiply the volume result by your specific density."},
        {"question": "How many 25 kg bags of cement do I need per cubic metre?",
         "answer": "A standard 1:2:3 mix (cement:sand:gravel) requires approximately 7 bags of 50 kg cement per m\u00b3, or about 14 bags of 25 kg. The calculator shows 50 kg bag equivalents."},
        {"question": "Does the calculator account for waste and spillage?",
         "answer": "The calculator shows net material quantities. Add 10% for form losses, spillage, and uneven ground. The safety margin input lets you adjust this."},
        {"question": "What's the difference between C25 and C30 concrete?",
         "answer": "C25 has 25 MPa compressive strength (typical for residential slabs and driveways). C30 has 30 MPa (used for structural columns, beams, and industrial floors). This calculator assumes a standard 1:2:3 mix ratio."},
        {"question": "How thick should a residential concrete slab be?",
         "answer": "Garage floors and patios: 100-150 mm (4-6 inches). Driveways: 150-200 mm (6-8 inches). Interior floor slabs on grade: 100-125 mm (4-5 inches). Always follow local building codes."},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Typical 3\u201310 m for residential slabs",
        "ancho": "Typical 3\u201310 m for residential slabs",
        "espesor": "100\u2013200 mm for garage/patio slabs, 150\u2013300 mm for industrial",
    })
    _update_field(calc, "comparison_presets", [
        {"_label": "Small shed base 3\u00d73m", "largo": 3, "ancho": 3, "espesor": 0.1},
        {"_label": "Garden patio 4\u00d74m", "largo": 4, "ancho": 4, "espesor": 0.1},
        {"_label": "Single garage floor 5\u00d75m", "largo": 5, "ancho": 5, "espesor": 0.12},
        {"_label": "Double garage slab 6\u00d74m", "largo": 6, "ancho": 4, "espesor": 0.15},
        {"_label": "Residential driveway 10\u00d75m", "largo": 10, "ancho": 5, "espesor": 0.15},
        {"_label": "Warehouse floor 10\u00d710m", "largo": 10, "ancho": 10, "espesor": 0.2},
    ])
    _update_field(calc, "related", ["002", "003", "008", "009", "010", "1104", "1116"])


def update_002(calc):
    # Fix buying_units: current key is "bloques" — replace with "volumen"
    _update_field(calc, "buying_units", {
        "volumen": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "wastage_pct", 12)
    _ensure_field(calc, "tags", ["reinforced-concrete", "rebar", "slab", "construction", "structural", "cement"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "acero_kg", "min": 0, "max": 5000,
        "zones": [
            {"min": 0, "max": 200, "label": "Light reinforcement", "color": "#4CAF50"},
            {"min": 200, "max": 1000, "label": "Standard", "color": "#FF9800"},
            {"min": 1000, "max": 5000, "label": "Heavy duty", "color": "#F44336"},
        ],
        "unit": "kg",
    })
    _ensure_field(calc, "faqs", [
        {"question": "How much steel reinforcement does concrete need?",
         "answer": "Typical residential slabs use 80-120 kg of steel per m\u00b3 of concrete. Columns and beams use 150-200 kg/m\u00b3. This calculator uses 120 kg/m\u00b3 as standard."},
        {"question": "What grade of rebar should I use?",
         "answer": "For most residential projects, Grade 60 (420 MPa) rebar is standard. High-rise and industrial structures may require Grade 75 or 80. Always check structural drawings for specifications."},
        {"question": "Does rebar spacing affect the quantity?",
         "answer": "Yes. Tighter spacing (e.g. 150 mm vs 300 mm centres) roughly doubles the steel weight. This calculator uses an average reinforcement ratio. Consult your structural engineer for exact spacing."},
        {"question": "Can I use fiber-reinforced concrete instead of rebar?",
         "answer": "For slabs on grade and non-structural applications, steel fiber or macro-synthetic fiber reinforcement can replace welded wire mesh. For structural elements like beams and columns, traditional rebar is required by most building codes."},
        {"question": "What concrete mix ratio should I use?",
         "answer": "Standard reinforced concrete uses a 1:2:3 mix (cement:sand:gravel) with a water-cement ratio of 0.45-0.50. For harsh environments, use 1:1.5:3 with 0.40 water-cement ratio."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small garden path 5\u00d71m", "largo": 5, "ancho": 1, "espesor": 0.1, "cuantia": 80},
        {"_label": "Patio slab 4\u00d74m", "largo": 4, "ancho": 4, "espesor": 0.12, "cuantia": 100},
        {"_label": "Driveway 8\u00d74m", "largo": 8, "ancho": 4, "espesor": 0.15, "cuantia": 100},
        {"_label": "Garage floor 6\u00d75m", "largo": 6, "ancho": 5, "espesor": 0.15, "cuantia": 120},
        {"_label": "Industrial floor 12\u00d78m", "largo": 12, "ancho": 8, "espesor": 0.2, "cuantia": 120},
        {"_label": "Bridge deck section 20\u00d710m", "largo": 20, "ancho": 10, "espesor": 0.3, "cuantia": 150},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Span length, typically 3\u201320 m",
        "ancho": "Width, typically 1\u201315 m",
        "espesor": "Slab depth 100\u2013300 mm per EN 1992-1-1",
        "cuantia": "Steel ratio 80\u2013200 kg/m\u00b3 (higher for columns/beams)",
    })
    _update_field(calc, "related", ["001", "003", "005", "006", "008", "009"])


def update_003(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "trust_note", "Density 2400 kg/m\u00b3, reinforcement 120 kg/m\u00b3 for footings")
    _ensure_field(calc, "tags", ["footing", "foundation", "concrete", "rebar", "excavation", "structural"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "vol_total", "min": 0, "max": 20,
        "zones": [
            {"min": 0, "max": 1, "label": "Small footing", "color": "#4CAF50"},
            {"min": 1, "max": 5, "label": "Standard", "color": "#2196F3"},
            {"min": 5, "max": 20, "label": "Large footing", "color": "#FF9800"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "buying_units", {
        "vol_total": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What size footing do I need for my column?",
         "answer": "Footing size depends on column load and soil bearing capacity. As a rule of thumb, a residential column carrying a typical 2-storey load needs a 1.0-1.5m square footing. Always get a geotechnical report."},
        {"question": "How deep should footings be?",
         "answer": "Footings must reach below the frost line (600-1200mm depending on climate). Structural depth (canto) is typically 400-800mm for residential footings, increasing for heavier loads or poor soil."},
        {"question": "Do I need reinforcement in footings?",
         "answer": "Yes. Even small isolated footings need reinforcement top and bottom to resist bending moments. Typical ratio is 80-120 kg/m\u00b3. Use a mesh or bar grid at 150-200mm spacing."},
        {"question": "What concrete strength for footings?",
         "answer": "Use minimum C25/30 concrete (25 MPa cylinder / 30 MPa cube strength). For aggressive soil conditions (sulfates, chlorides), use C30/37 or higher with sulfate-resisting cement."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small column footing 1.0\u00d71.0m", "largo": 1.0, "ancho": 1.0, "canto": 0.4, "cantidad": 4},
        {"_label": "Standard footing 1.5\u00d71.5m", "largo": 1.5, "ancho": 1.5, "canto": 0.5, "cantidad": 6},
        {"_label": "Two-storey column 2.0\u00d72.0m", "largo": 2.0, "ancho": 2.0, "canto": 0.6, "cantidad": 4},
        {"_label": "Large residential 1.8\u00d71.8m", "largo": 1.8, "ancho": 1.8, "canto": 0.7, "cantidad": 8},
        {"_label": "Industrial footing 2.5\u00d72.5m", "largo": 2.5, "ancho": 2.5, "canto": 1.0, "cantidad": 6},
    ])
    _update_field(calc, "related", ["001", "002", "005", "009", "010", "1116"])


def update_004(calc):
    _update_field(calc, "steps", [
        "Measure the wall's total length in metres",
        "Determine the retained height (from foundation to top of wall)",
        "Input base thickness (typically 0.3\u00d7 retained height for cantilever walls)",
        "Calculate and add 10% for construction waste and form losses",
        "Order concrete in 0.5 m\u00b3 increments above the calculated volume",
    ])
    _update_field(calc, "mistakes", [
        "Underestimating base width (should be 0.3-0.6\u00d7 wall height for cantilever walls)",
        "Forgetting the drainage system behind the wall",
        "Not accounting for surcharge loads from adjacent structures",
    ])
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "EN 1997-1 / ACI 318-19 (retaining structures)")
    _ensure_field(calc, "trust_note", "For walls > 1.2m, structural engineering review is required by most building codes")
    _ensure_field(calc, "tags", ["retaining-wall", "concrete", "foundation", "earth-retention", "structural", "garden-wall"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "wall")
    _ensure_field(calc, "gauge_config", {
        "output_key": "vol_muro", "min": 0, "max": 50,
        "zones": [
            {"min": 0, "max": 3, "label": "Garden wall", "color": "#4CAF50"},
            {"min": 3, "max": 15, "label": "Medium wall", "color": "#FF9800"},
            {"min": 15, "max": 50, "label": "Major structure", "color": "#F44336"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "buying_units", {
        "vol_muro": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "How thick should a retaining wall be?",
         "answer": "For gravity walls, base width should be 0.5-0.7\u00d7 the height. For cantilever walls, stem thickness at base = height/12, base slab thickness = height/10. Walls over 1.2m need engineered design per EN 1997-1."},
        {"question": "Do I need drainage behind a retaining wall?",
         "answer": "Yes. Without drainage, hydrostatic pressure can double the lateral force on the wall. Install a perforated drain pipe at the base, surrounded by free-draining gravel, with weep holes every 1.5-2m."},
        {"question": "What concrete strength for retaining walls?",
         "answer": "Use minimum C30/37 concrete. For walls exposed to de-icing salts or marine environments, use C35/45 with air entrainment. Water-cement ratio should not exceed 0.50."},
        {"question": "Do I need a building permit for a retaining wall?",
         "answer": "In most jurisdictions, walls over 1.0-1.2m require a permit and structural engineer's design. Check local building codes. Walls under 1m for garden landscaping are typically exempt."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Garden wall 5m\u00d71m", "largo": 5, "altura": 1.0, "espesor_base": 0.3, "espesor_corona": 0.2},
        {"_label": "Low terrace wall 8m\u00d71.5m", "largo": 8, "altura": 1.5, "espesor_base": 0.4, "espesor_corona": 0.25},
        {"_label": "Residential wall 10m\u00d72m", "largo": 10, "altura": 2.0, "espesor_base": 0.5, "espesor_corona": 0.3},
        {"_label": "Sloped garden 12m\u00d72.5m", "largo": 12, "altura": 2.5, "espesor_base": 0.7, "espesor_corona": 0.35},
        {"_label": "Commercial wall 15m\u00d73m", "largo": 15, "altura": 3.0, "espesor_base": 1.0, "espesor_corona": 0.4},
        {"_label": "Road embankment 20m\u00d74m", "largo": 20, "altura": 4.0, "espesor_base": 1.5, "espesor_corona": 0.5},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Wall length 3\u201330 m",
        "altura": "Retained height 0.5\u20136.0 m (engineering required >1.2m)",
        "espesor_base": "Base thickness, typically 0.3\u20130.6\u00d7 wall height",
        "espesor_corona": "Top/corona thickness, minimum 200 mm",
    })
    _update_field(calc, "related", ["001", "003", "005", "009", "010", "1116"])


def update_005(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "EN 1992-1-1 / ACI 318-19 (column design)")
    _ensure_field(calc, "trust_note", "Reinforcement ratio 160 kg/m\u00b3 for columns")
    _ensure_field(calc, "tags", ["columns", "concrete", "structural", "rebar", "vertical-elements", "construction"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "column")
    _ensure_field(calc, "gauge_config", {
        "output_key": "vol_total", "min": 0, "max": 10,
        "zones": [
            {"min": 0, "max": 0.5, "label": "Small column", "color": "#4CAF50"},
            {"min": 0.5, "max": 2, "label": "Standard", "color": "#2196F3"},
            {"min": 2, "max": 10, "label": "Large column", "color": "#FF9800"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "buying_units", {
        "vol_total": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is the minimum column size for a residential building?",
         "answer": "Minimum column size for single-storey residential is 230\u00d7230 mm (9\u00d79 inches). For two-storey, use 300\u00d7300 mm minimum. Columns should not be smaller than 200mm in any dimension per ACI 318."},
        {"question": "How much steel reinforcement do columns need?",
         "answer": "Columns typically require 1-4% steel by cross-sectional area (160-200 kg/m\u00b3). Minimum is 1% per ACI 318. Use 4 bars minimum, tied with stirrups at spacing \u2264 16\u00d7 bar diameter."},
        {"question": "What concrete strength for columns?",
         "answer": "Use minimum C25/30 for residential columns. Mid-rise buildings typically use C30/37 to C40/50. High-rise structures use C50/60 or higher."},
        {"question": "How do I calculate column formwork area?",
         "answer": "Formwork area = perimeter \u00d7 height \u00d7 number of columns. For a 300\u00d7300mm column, perimeter = 1.2m. Add 10% for overlaps and bracing."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small porch posts 25\u00d725cm", "ancho": 0.25, "profundidad": 0.25, "altura": 2.5, "cantidad": 2},
        {"_label": "Residential columns 30\u00d730cm", "ancho": 0.30, "profundidad": 0.30, "altura": 3.0, "cantidad": 6},
        {"_label": "Two-storey house 35\u00d735cm", "ancho": 0.35, "profundidad": 0.35, "altura": 3.0, "cantidad": 8},
        {"_label": "Commercial building 40\u00d740cm", "ancho": 0.40, "profundidad": 0.40, "altura": 3.5, "cantidad": 12},
        {"_label": "Multi-storey 50\u00d750cm", "ancho": 0.50, "profundidad": 0.50, "altura": 3.5, "cantidad": 16},
    ])
    _update_field(calc, "range_hints", {
        "ancho": "Column width 200\u2013600 mm",
        "profundidad": "Column depth 200\u2013600 mm",
        "altura": "Storey height, typically 2.5\u20134.0 m",
        "cantidad": "Number of identical columns in structure",
    })
    _update_field(calc, "related", ["002", "003", "006", "008", "009", "1116"])


def update_006(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "EN 1992-1-1 / ACI 318-19 (beam design)")
    _ensure_field(calc, "trust_note", "Reinforcement ratio 150 kg/m\u00b3 for beams")
    _ensure_field(calc, "tags", ["beams", "concrete", "structural", "rebar", "horizontal-elements", "construction"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "beam")
    _ensure_field(calc, "gauge_config", {
        "output_key": "acero_kg", "min": 0, "max": 3000,
        "zones": [
            {"min": 0, "max": 200, "label": "Light beam", "color": "#4CAF50"},
            {"min": 200, "max": 800, "label": "Standard", "color": "#2196F3"},
            {"min": 800, "max": 3000, "label": "Heavy beam", "color": "#F44336"},
        ],
        "unit": "kg",
    })
    _ensure_field(calc, "buying_units", {
        "vol_total": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What size beam do I need for a given span?",
         "answer": "As a rule of thumb, beam depth = span/12 to span/15 for simply supported beams, and span/18 to span/21 for continuous beams. A 6m span typically needs a 400-500mm deep beam."},
        {"question": "How is beam reinforcement calculated?",
         "answer": "Beams need bottom (tension) bars, top (compression) bars, and shear stirrups. Bottom steel area \u2248 0.5-1.5% of cross-section. This calculator uses an average of 150 kg/m\u00b3."},
        {"question": "What is effective depth vs total depth?",
         "answer": "Effective depth (d) is the distance from the compression face to the centroid of tension reinforcement. Total depth (h) = effective depth + cover + half bar diameter. Minimum cover is 25-40mm depending on exposure."},
        {"question": "Do beams and slabs use the same concrete mix?",
         "answer": "They can, but beams often use a slightly higher strength concrete than slabs (C30/37 vs C25/30) because beams carry more load. The slump (workability) should be 75-100mm for pump placement."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Lintel beam 2m span", "ancho": 0.2, "canto": 0.2, "longitud": 2.0, "cantidad": 3},
        {"_label": "Floor beam 4m span", "ancho": 0.25, "canto": 0.35, "longitud": 4.0, "cantidad": 4},
        {"_label": "Main beam 5m span", "ancho": 0.3, "canto": 0.45, "longitud": 5.0, "cantidad": 5},
        {"_label": "Large beam 6m span", "ancho": 0.3, "canto": 0.5, "longitud": 6.0, "cantidad": 6},
        {"_label": "Transfer beam 8m span", "ancho": 0.4, "canto": 0.7, "longitud": 8.0, "cantidad": 2},
    ])
    _update_field(calc, "range_hints", {
        "ancho": "Beam width 150\u2013500 mm",
        "canto": "Beam depth, typically span/12 to span/15",
        "longitud": "Beam span 2\u201312 m",
        "cantidad": "Number of identical beams",
    })
    _update_field(calc, "related", ["002", "003", "005", "008", "007", "009"])


def update_007(calc):
    _update_field(calc, "formula_display",
                  "N_viguetas = ceil(largo / intereje); Vol_hormig\u00f3n = largo \u00d7 ancho \u00d7 0.05 + N_viguetas \u00d7 0.01 \u00d7 ancho")
    _update_field(calc, "steps", [
        "Measure the floor span length and width in metres",
        "Determine joist spacing (intereje) \u2014 standard is 0.70m for 70cm joist blocks",
        "Count joists: divide span length by spacing and round up",
        "Calculate concrete topping: area \u00d7 0.05m (5cm minimum topping)",
        "Add 10% to concrete volume for construction tolerances and spillage",
    ])
    _update_field(calc, "mistakes", [
        "Forgetting the 5cm minimum concrete topping over joists",
        "Not accounting for end bearing (joists must sit 10-15cm on walls)",
        "Using wrong intereje spacing (60, 70, or 80cm depending on block type)",
    ])
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "EN 15037-1 (precast concrete joist floors)")
    _ensure_field(calc, "trust_note", "Concrete topping minimum 50mm per EN 15037-1")
    _ensure_field(calc, "tags", ["floor", "joist", "beam-block", "concrete", "structural", "slab"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "slab")
    _ensure_field(calc, "buying_units", {
        "vol_hormigon": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is a joist-and-block floor system?",
         "answer": "It consists of pre-stressed concrete joists (viguetas) placed at regular spacing, with hollow blocks (bovedillas) between them, topped with a 5cm cast-in-place concrete compression layer. Common in Mediterranean and Latin American construction."},
        {"question": "What spacing should I use between joists?",
         "answer": "Standard spacing is 0.70m (70cm) for typical hollow blocks. Some systems use 0.60m or 0.80m spacing. Always match the intereje to your block manufacturer's specifications."},
        {"question": "How thick should the concrete topping be?",
         "answer": "Minimum 50mm (5cm) per EN 15037-1. For floors supporting partition walls or with spans over 5m, increase to 60-80mm. Always include welded wire mesh in the topping."},
        {"question": "Do I need propping during construction?",
         "answer": "Yes. Joists need temporary mid-span propping until the topping concrete reaches 70% of design strength (typically 7 days at 20\u00b0C). Props should remain for minimum 14 days."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small room 4\u00d73m, 70cm", "largo": 4, "ancho": 3, "intereje": 0.7},
        {"_label": "Bedroom 5\u00d74m, 70cm", "largo": 5, "ancho": 4, "intereje": 0.7},
        {"_label": "Living room 6\u00d75m, 70cm", "largo": 6, "ancho": 5, "intereje": 0.7},
        {"_label": "Open plan 8\u00d76m, 60cm", "largo": 8, "ancho": 6, "intereje": 0.6},
        {"_label": "Commercial floor 10\u00d78m, 70cm", "largo": 10, "ancho": 8, "intereje": 0.7},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Floor span 3\u201315 m (one direction)",
        "ancho": "Floor width 2\u201312 m",
        "intereje": "Joist spacing 0.60\u20130.80m depending on block type",
    })
    _update_field(calc, "related", ["002", "006", "008", "001", "009", "1104"])


def update_008(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "EN 206-1 / ACI 318-19")
    _ensure_field(calc, "trust_note", "For slabs on grade, include 50mm sand blinding layer beneath")
    _ensure_field(calc, "tags", ["concrete", "slab", "floor", "ground-slab", "construction", "materials"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "slab")
    _ensure_field(calc, "gauge_config", {
        "output_key": "volumen", "min": 0, "max": 100,
        "zones": [
            {"min": 0, "max": 3, "label": "Small slab", "color": "#4CAF50"},
            {"min": 3, "max": 15, "label": "Standard slab", "color": "#FF9800"},
            {"min": 15, "max": 100, "label": "Industrial slab", "color": "#F44336"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "buying_units", {
        "volumen": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "How thick should a concrete slab on grade be?",
         "answer": "Residential floors: 100mm. Garage floors: 125-150mm. Light industrial: 150mm. For heavy industrial with forklift traffic: 175-200mm with reinforcement. Always place on 50mm sand blinding and DPM."},
        {"question": "Do I need reinforcement mesh in a slab?",
         "answer": "For residential slabs, A142 or A193 mesh is standard. For garage floors, use A252 mesh. Position mesh in the top third of the slab (typically 40-50mm cover). Fiber reinforcement is an acceptable alternative for residential use."},
        {"question": "What concrete mix for a floor slab?",
         "answer": "Use C25/30 with 75-100mm slump for pump placement. For garages exposed to de-icing salts, use C30/37 with air entrainment (4-6%). Water-cement ratio \u2264 0.55 for durability."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Garden shed base 3\u00d72m", "largo": 3, "ancho": 2, "espesor": 0.1},
        {"_label": "Small patio 4\u00d73m", "largo": 4, "ancho": 3, "espesor": 0.1},
        {"_label": "Single garage 6\u00d74m", "largo": 6, "ancho": 4, "espesor": 0.15},
        {"_label": "Double garage 6\u00d76m", "largo": 6, "ancho": 6, "espesor": 0.15},
        {"_label": "Small warehouse 12\u00d78m", "largo": 12, "ancho": 8, "espesor": 0.2},
        {"_label": "Industrial floor 20\u00d715m", "largo": 20, "ancho": 15, "espesor": 0.2},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Length 3\u201330 m",
        "ancho": "Width 2\u201320 m",
        "espesor": "100\u2013200 mm for residential, 150\u2013300 mm industrial",
    })
    _update_field(calc, "related", ["001", "002", "007", "009", "1116", "1104"])


def update_009(calc):
    _update_field(calc, "formula_display", "Volumen = largo \u00d7 ancho \u00d7 profundidad")
    _update_field(calc, "steps", [
        "Mark out the foundation trench lines with string and pegs",
        "Measure the total trench length by adding all wall lengths",
        "Determine trench width (typically 600mm for 2-storey, 450mm for single-storey)",
        "Input trench depth to reach below frost line (600-1200mm depending on climate)",
        "Add 10% to the calculated volume for uneven trench bottom and spillage",
    ])
    _update_field(calc, "mistakes", [
        "Forgetting to overlap trench corners in the length measurement",
        "Not accounting for steps in the foundation where ground slopes",
        "Using trench width less than 450mm (minimum for concrete placement access)",
    ])
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "trust_note", "Minimum trench width 450mm for concrete placement access")
    _ensure_field(calc, "tags", ["strip-foundation", "trench-fill", "concrete", "footing", "foundation", "structural"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "volumen", "min": 0, "max": 30,
        "zones": [
            {"min": 0, "max": 3, "label": "Small foundation", "color": "#4CAF50"},
            {"min": 3, "max": 10, "label": "Standard house", "color": "#2196F3"},
            {"min": 10, "max": 30, "label": "Large building", "color": "#FF9800"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "buying_units", {
        "volumen": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What width should a strip foundation be?",
         "answer": "Single-storey residential: 450-500mm. Two-storey: 600mm. Three-storey: 750mm+. Width is determined by wall load divided by soil bearing capacity. Always get a soil investigation for values below 100 kN/m\u00b2."},
        {"question": "How deep should strip foundations be?",
         "answer": "Minimum 600mm for single-storey, 750-900mm for two-storey in temperate climates. Must extend below the frost line (varies by region, 600-1200mm). In clay soils, depth may need to reach below the zone of seasonal moisture variation."},
        {"question": "Do strip footings need reinforcement?",
         "answer": "Plain concrete strip footings are acceptable for low-rise residential on good ground. However, reinforcement is recommended where there are trees, mining, or variable ground. Use longitudinal bars with minimum 0.15% steel area."},
        {"question": "What concrete mix for strip foundations?",
         "answer": "Use ST2 or ST3 (C20/25 to C25/30) for most residential foundations. For aggressive ground conditions (sulfate class DS-2 or higher), use sulfate-resisting cement with C30/37 minimum."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small extension 15m run", "largo": 15, "ancho": 0.45, "profundidad": 0.6},
        {"_label": "Single-storey house 30m", "largo": 30, "ancho": 0.5, "profundidad": 0.7},
        {"_label": "Two-storey house 40m", "largo": 40, "ancho": 0.6, "profundidad": 0.8},
        {"_label": "Large bungalow 50m", "largo": 50, "ancho": 0.6, "profundidad": 0.9},
        {"_label": "Commercial building 80m", "largo": 80, "ancho": 0.75, "profundidad": 1.0},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Total trench length 5\u2013150 m",
        "ancho": "Trench width 0.45\u20131.0 m (depends on wall load)",
        "profundidad": "Trench depth 0.6\u20131.5 m (below frost line)",
    })
    _update_field(calc, "related", ["001", "002", "003", "008", "010", "004"])


def update_010(calc):
    _update_field(calc, "formula_display",
                  "Volumen = largo \u00d7 ancho \u00d7 profundidad; Vol_esponjado = Volumen \u00d7 (1 + esponjamiento/100)")
    _update_field(calc, "steps", [
        "Measure the excavation area length and width at ground level",
        "Determine the dig depth from existing ground level to formation level",
        "Select the swell/bulking factor for your soil type (clay: 30-40%, sand: 10-15%, rock: 50-60%)",
        "Calculate the loose volume (the volume you'll actually truck away)",
        "Add 5% for over-excavation and irregularities",
    ])
    _update_field(calc, "mistakes", [
        "Applying the same swell factor to all soil types",
        "Measuring plan area only and forgetting depth",
        "Not allowing for working space around foundations (add 600mm each side)",
    ])
    _ensure_field(calc, "wastage_pct", 5)
    _ensure_field(calc, "standard", "EN 1997-2 (Eurocode 7 - ground investigation and testing)")
    _ensure_field(calc, "trust_note",
                  "Bulking/swell factor depends on soil type: clay 30-40%, sand 10-15%, rock 50-60%")
    _ensure_field(calc, "tags", ["excavation", "earthwork", "soil", "bulking", "construction", "site-prep"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "diagram", "excavation")
    _ensure_field(calc, "buying_units", {
        "volumen": [
            {"label": "Truck loads (8 m\u00b3)", "factor": 0.125, "round": "ceil", "unit": "trucks"},
            {"label": "Skip (6 yd\u00b3 \u2248 4.6 m\u00b3)", "factor": 0.217, "round": "ceil", "unit": "skips"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is the bulking/swell factor?",
         "answer": "When soil is excavated, it expands in volume because air fills the voids between particles. The bulking factor is the percentage increase from in-situ (bank) volume to loose volume. Clay swells 30-40%, sand 10-15%, gravel 5-10%, rock 50-60%."},
        {"question": "How do I calculate how many truckloads of spoil I need to remove?",
         "answer": "Calculate the bank volume (l\u00d7w\u00d7d), then multiply by (1 + swell%/100) to get loose volume. Divide loose volume by your truck capacity (typically 8 m\u00b3 per load). The calculator does this automatically."},
        {"question": "How much working space do I need around foundations?",
         "answer": "Add 600mm minimum on each side of foundation trenches for worker access. For deeper excavations (>1.5m), you may need benching or shoring, which significantly increases the excavation volume."},
        {"question": "What safety precautions for excavations?",
         "answer": "Any excavation deeper than 1.2m (4ft) requires shoring, benching, or battering per OSHA/EN regulations. Keep spoil at least 1m from the edge. Never enter an unsupported trench deeper than 1.2m. Always use trench boxes for deep excavations."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Garden trench 5\u00d70.5\u00d71m", "largo": 5, "ancho": 0.5, "profundidad": 1.0, "esponjamiento": 20},
        {"_label": "Foundation trench 20\u00d70.6\u00d71.2m", "largo": 20, "ancho": 0.6, "profundidad": 1.2, "esponjamiento": 25},
        {"_label": "Basement dig 10\u00d78\u00d72.5m", "largo": 10, "ancho": 8.0, "profundidad": 2.5, "esponjamiento": 30},
        {"_label": "Pool excavation 12\u00d76\u00d72m", "largo": 12, "ancho": 6.0, "profundidad": 2.0, "esponjamiento": 25},
        {"_label": "Road cut 50\u00d73\u00d71m", "largo": 50, "ancho": 3.0, "profundidad": 1.0, "esponjamiento": 15},
    ])
    _update_field(calc, "range_hints", {
        "largo": "Excavation length 1\u2013200 m",
        "ancho": "Excavation width 0.3\u201330 m (add 0.6m working space each side)",
        "profundidad": "Dig depth 0.3\u201310 m (shoring required >1.2m)",
        "esponjamiento": "Swell %: clay 30-40%, sand 10-15%, rock 50-60%",
    })
    _update_field(calc, "related", ["001", "003", "004", "009", "008", "1116"])


# ========================= 1100s  ===========================================

def update_1101(calc):
    _ensure_field(calc, "wastage_pct", 5)
    _ensure_field(calc, "standard", "TPI (Turfgrass Producers International) standards")
    _ensure_field(calc, "trust_note", "Add 5-10% for cutting waste on curved areas")
    _ensure_field(calc, "tags", ["sod", "turf", "lawn", "landscaping", "garden", "grass"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "faqs", [
        {"question": "How do I measure irregularly shaped lawns?",
         "answer": "Divide the lawn into rectangles, triangles, and circles. Calculate each area separately and sum them. For curved areas, measure the longest length and average width, then add 10% extra to be safe."},
        {"question": "What's the difference between sod and seeding?",
         "answer": "Sod gives instant lawn and can be laid any time during the growing season. Seeding costs about 75% less but takes 8-12 weeks to establish and can only be done in spring or autumn. Sod also reduces erosion immediately on slopes."},
        {"question": "How soon can I walk on new sod?",
         "answer": "Keep foot traffic off new sod for 2-3 weeks. Water daily for the first 2 weeks (keep soil moist 100-150mm deep). First mowing at 3-4 weeks when grass reaches 75-100mm. Full root establishment takes 4-6 weeks."},
        {"question": "How many rolls of sod do I need?",
         "answer": "Standard sod rolls cover 0.6m\u00b2 (2ft \u00d7 3.25ft or 0.6m \u00d7 1m). Divide your lawn area in m\u00b2 by 0.6 to get the number of rolls. The calculator does this automatically and adds a waste allowance for cutting."},
    ])
    _update_field(calc, "range_hints", {
        "total_area_m2": "Lawn area 5\u2013500 m\u00b2 (measure length \u00d7 width for rectangle)",
        "roll_area_m2": "Standard sod roll covers 0.6 m\u00b2 (0.6m \u00d7 1.0m)",
    })
    _update_field(calc, "related", ["1102", "1119", "010", "001"])


def update_1102(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "ANSI A300 (Part 2) - Tree Care Operations")
    _ensure_field(calc, "trust_note",
                  "Mulch compacts by ~20% after rain; factor this into your depth calculation")
    _ensure_field(calc, "tags", ["mulch", "landscaping", "garden", "bark", "soil-cover", "bed"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "volume_m3", "min": 0, "max": 10,
        "zones": [
            {"min": 0, "max": 0.5, "label": "Small bed", "color": "#4CAF50"},
            {"min": 0.5, "max": 3, "label": "Medium garden", "color": "#FF9800"},
            {"min": 3, "max": 10, "label": "Large landscape", "color": "#F44336"},
        ],
        "unit": "m\u00b3",
    })
    _ensure_field(calc, "faqs", [
        {"question": "How deep should mulch be applied?",
         "answer": "50-75mm (2-3 inches) is ideal for most garden beds. Less than 50mm won't suppress weeds, and more than 100mm can suffocate plant roots and create a barrier to water infiltration. Around trees, keep mulch 100-150mm away from the trunk."},
        {"question": "How often should I replace mulch?",
         "answer": "Organic mulch (bark, wood chips) breaks down in 1-2 years and should be topped up annually. Inorganic mulch (gravel, stone) needs replenishing every 3-5 years. Check depth in spring and top up to maintain 50-75mm."},
        {"question": "Does mulch color affect performance?",
         "answer": "Dyed mulches (black, red, brown) perform the same as natural mulch but may fade within 6-12 months. The dye is typically non-toxic iron oxide or carbon-based. Natural bark mulch weathers to a grey colour over time."},
    ])
    _update_field(calc, "range_hints", {
        "length_m": "Bed length 1\u201350 m",
        "width_m": "Bed width 1\u201330 m",
        "depth_cm": "Depth 5\u201310 cm (2-4 inches) for effective weed suppression",
    })
    _update_field(calc, "related", ["1101", "1119", "001"])


def update_1104(calc):
    _ensure_field(calc, "wastage_pct", 15)
    _ensure_field(calc, "standard", "ASTM D3462 (asphalt shingles)")
    _ensure_field(calc, "trust_note",
                  "Order one extra bundle for every 10 for cuts, ridge caps, and starter strips")
    _ensure_field(calc, "tags", ["roofing", "shingles", "asphalt", "roof", "construction", "materials"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "waste_percent", "min": 5, "max": 25,
        "zones": [
            {"min": 5, "max": 10, "label": "Simple roof", "color": "#4CAF50"},
            {"min": 10, "max": 15, "label": "Standard", "color": "#FF9800"},
            {"min": 15, "max": 25, "label": "Complex roof", "color": "#F44336"},
        ],
        "unit": "%",
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is a roofing square?",
         "answer": "A roofing square equals 100 square feet (9.29 m\u00b2) of roof area. Shingles are sold in bundles, with 3 bundles typically covering 1 square. This calculator converts your m\u00b2 roof area into squares and bundles automatically."},
        {"question": "How much overlap should I allow for shingles?",
         "answer": "Standard three-tab shingles require 50% overlap (double coverage). Architectural/laminated shingles have built-in overlap. Ridge caps and starter strips add 10-15% to material requirements. The waste factor in the calculator covers this."},
        {"question": "Can I install new shingles over old ones?",
         "answer": "Building codes typically allow one overlay (reroofing over existing shingles) if the existing roof has only one layer. Two layers maximum total. However, a full tear-off allows inspection of the decking and is recommended for best results."},
        {"question": "What roof pitch adds the most waste?",
         "answer": "Roof pitch affects waste because steeper roofs require more overlap and have more safety-related handling waste. Add 5% for 4/12 pitch, 10% for 8/12, and 15%+ for 12/12 or steeper. Complex roofs with hips, valleys, and dormers require 15-20% extra."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small shed 8\u00d75m, 4/12", "roof_length": 8, "roof_width": 5, "roof_pitch": 4, "shingles_per_bundle": 33},
        {"_label": "Single garage 6\u00d76m, 6/12", "roof_length": 6, "roof_width": 6, "roof_pitch": 6, "shingles_per_bundle": 33},
        {"_label": "Standard house 12\u00d79m, 8/12", "roof_length": 12, "roof_width": 9, "roof_pitch": 8, "shingles_per_bundle": 33},
        {"_label": "Large home 15\u00d710m, 8/12", "roof_length": 15, "roof_width": 10, "roof_pitch": 8, "shingles_per_bundle": 33},
        {"_label": "Steep roof 10\u00d78m, 12/12", "roof_length": 10, "roof_width": 8, "roof_pitch": 12, "shingles_per_bundle": 33},
    ])
    _update_field(calc, "related", ["001", "008", "1102", "1116"])


def update_1116(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "ACI 315 / EN 1992-1-1")
    _ensure_field(calc, "trust_note", "For steps, add 10% for riser and tread irregularities in formwork")
    _ensure_field(calc, "tags", ["steps", "stairs", "concrete", "outdoor", "landscaping", "construction"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "buying_units", {
        "concrete_m3": [
            {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
            {"label": "Ready-mix truck (6 m\u00b3)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is the ideal riser and tread for outdoor steps?",
         "answer": "For comfortable outdoor steps, use risers 150-175mm and treads 280-350mm. The 'rule of 600' states that 2\u00d7 riser + tread should equal 600-630mm. For garden steps, 150mm risers with 350mm treads give a relaxed, safe stride."},
        {"question": "Do outdoor concrete steps need a foundation?",
         "answer": "Yes. Concrete steps need a minimum 150mm compacted hardcore base with 100mm concrete pad beneath the bottom step. In freezing climates, the foundation must extend below the frost line. Without a proper base, steps will settle and crack."},
        {"question": "How do I calculate the number of steps?",
         "answer": "Divide total rise (ground to door height) by your chosen riser height (typically 150-175mm). Round to the nearest whole number. The calculator does this automatically and adjusts the tread depth accordingly."},
        {"question": "What concrete mix for outdoor steps?",
         "answer": "Use C30/37 with air entrainment (4-6%) for freeze-thaw resistance. The mix should be stiff enough to hold the riser face but workable enough to finish. Slump should be 50-75mm. Avoid adding water on site \u2014 it weakens the surface."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small porch 2 steps", "total_rise": 0.35, "desired_riser": 0.175, "step_width": 1.2},
        {"_label": "Front entrance 3 steps", "total_rise": 0.55, "desired_riser": 0.18, "step_width": 1.5},
        {"_label": "Deck access 4 steps", "total_rise": 0.75, "desired_riser": 0.175, "step_width": 1.8},
        {"_label": "Garden terrace 5 steps", "total_rise": 0.9, "desired_riser": 0.18, "step_width": 2.0},
        {"_label": "Long garden 7 steps", "total_rise": 1.2, "desired_riser": 0.17, "step_width": 1.5},
    ])
    _update_field(calc, "range_hints", {
        "total_rise": "Total height from ground to finished floor level, 0.3\u20133.0 m",
        "desired_riser": "Riser height 150\u2013200 mm (150\u2013175 mm for comfortable outdoor steps)",
        "step_width": "Step width 0.8\u20133.0 m",
    })
    _update_field(calc, "related", ["001", "005", "008", "1104", "010"])


def update_1119(calc):
    _ensure_field(calc, "wastage_pct", 10)
    _ensure_field(calc, "standard", "ASTM D448 (standard sizes of aggregate)")
    _ensure_field(calc, "trust_note",
                  "Landscape rock compacts by ~5% after installation; order slightly more than calculated")
    _ensure_field(calc, "tags", ["gravel", "landscape-rock", "decorative-stone", "garden", "hardscape", "aggregate"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "tonnes_needed", "min": 0, "max": 20,
        "zones": [
            {"min": 0, "max": 1, "label": "Small feature", "color": "#4CAF50"},
            {"min": 1, "max": 5, "label": "Medium area", "color": "#FF9800"},
            {"min": 5, "max": 20, "label": "Large project", "color": "#F44336"},
        ],
        "unit": "t",
    })
    _ensure_field(calc, "buying_units", {
        "tonnes_needed": [
            {"label": "Bulk bag (800 kg)", "factor": 1.25, "round": "ceil", "unit": "bulk bags"},
            {"label": "25 kg bags", "factor": 40.0, "round": "ceil", "unit": "small bags"},
        ]
    })
    _ensure_field(calc, "faqs", [
        {"question": "How deep should landscape rock be?",
         "answer": "For ground cover: 50-75mm (2-3 inches). For driveways: 100-150mm (4-6 inches) on a compacted sub-base. For paths: 75mm (3 inches). Deeper than 100mm rarely provides additional benefit and wastes material."},
        {"question": "What size rock should I use?",
         "answer": "10-20mm gravel for paths and general ground cover. 20-40mm for driveways (locks together better). 40-100mm cobbles for decorative borders and dry creek beds. Use angular stone for driveways (locks together); rounded for decorative areas."},
        {"question": "Do I need landscape fabric under the rock?",
         "answer": "Yes. A geotextile membrane prevents the stone from mixing with the soil below, stops weeds, and maintains drainage. Overlap fabric joints by 300mm. Use a heavy-duty 100g/m\u00b2 or greater woven membrane, not thin plastic sheeting."},
        {"question": "How do I convert between tonnes and cubic metres?",
         "answer": "Landscape rock density varies: limestone gravel is ~1.6 t/m\u00b3, granite ~1.7 t/m\u00b3, sandstone ~1.5 t/m\u00b3. The calculator uses 1.6 t/m\u00b3 as standard. Multiply m\u00b3 by density to get tonnes."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small flower bed 3\u00d72m", "length": 3, "width": 2, "depth": 0.05, "rock_type": 1},
        {"_label": "Garden path 8\u00d71m", "length": 8, "width": 1, "depth": 0.075, "rock_type": 2},
        {"_label": "Decorative area 6\u00d74m", "length": 6, "width": 4, "depth": 0.05, "rock_type": 1},
        {"_label": "Driveway 12\u00d73m", "length": 12, "width": 3, "depth": 0.12, "rock_type": 2},
        {"_label": "Large landscape 10\u00d78m", "length": 10, "width": 8, "depth": 0.06, "rock_type": 1},
    ])
    _update_field(calc, "range_hints", {
        "length": "Area length 1\u201330 m",
        "width": "Area width 0.5\u201315 m",
        "depth": "Desired rock depth 50\u2013150 mm",
        "rock_type": "1 = Decorative gravel (1.5 t/m\u00b3), 2 = Crushed stone (1.7 t/m\u00b3)",
    })
    _update_field(calc, "related", ["1101", "1102", "010", "001"])


# =========================  SALUD  =========================================

def update_415(calc):
    _update_field(calc, "formula_display",
                  "Boer formula: LBM (male) = 0.407\u00d7W + 0.267\u00d7H \u2212 19.2; LBM (female) = 0.252\u00d7W + 0.473\u00d7H \u2212 48.3")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard",
                  "Boer equation (Boer P, 1984, 'Estimated lean body mass as an index for normalization of body fluid volumes in humans')")
    _ensure_field(calc, "trust_note",
                  "The Boer formula is most accurate for adults with BMI 18.5-35. For athletes with very low body fat, the result may overestimate LBM slightly")
    _ensure_field(calc, "tags", ["lean-body-mass", "body-composition", "health", "fitness", "boer-formula", "weight"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "lbm", "min": 30, "max": 120,
        "zones": [
            {"min": 30, "max": 45, "label": "Below average", "color": "#FF9800"},
            {"min": 45, "max": 65, "label": "Average", "color": "#4CAF50"},
            {"min": 65, "max": 80, "label": "Athletic", "color": "#2196F3"},
            {"min": 80, "max": 120, "label": "Elite", "color": "#9C27B0"},
        ],
        "unit": "kg",
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is lean body mass?",
         "answer": "Lean body mass (LBM) is your total body weight minus your fat mass. It includes muscle, bone, organs, water, and connective tissue. Knowing your LBM helps calculate protein requirements, basal metabolic rate, and drug dosing more accurately than total weight."},
        {"question": "How accurate is the Boer formula?",
         "answer": "The Boer formula has a standard error of approximately \u00b12-3 kg compared to DEXA scans in the general population. It's more accurate than BMI-based estimates but less accurate than skinfold measurements or bioelectrical impedance for individuals."},
        {"question": "How do I use LBM to calculate protein needs?",
         "answer": "Multiply your LBM in kg by 1.6-2.2 for daily protein grams needed for muscle gain. For maintenance, use 1.2-1.6 g per kg of LBM. These values are based on lean mass, not total body weight."},
        {"question": "What's a good lean body mass for my height?",
         "answer": "For men, LBM typically ranges from 50-70 kg for average build, 70-80 kg for athletic, 80+ kg for bodybuilders. For women, 35-48 kg is average, 48-55 kg athletic. LBM naturally decreases with age after 30 by about 3-5% per decade."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Small female", "weight": 50, "height": 155, "gender": "female"},
        {"_label": "Average female", "weight": 65, "height": 165, "gender": "female"},
        {"_label": "Average male", "weight": 78, "height": 175, "gender": "male"},
        {"_label": "Athletic male", "weight": 85, "height": 180, "gender": "male"},
        {"_label": "Tall male", "weight": 95, "height": 190, "gender": "male"},
    ])
    _update_field(calc, "range_hints", {
        "weight": "Body weight 35\u2013200 kg",
        "height": "Height 100\u2013250 cm",
        "gender": "Male or female (different formulas apply)",
    })
    _update_field(calc, "related", ["425", "410", "411", "426"])


def update_425(calc):
    _update_field(calc, "formula_display",
                  "Navy method: BFP% (male) = 495/(1.0324 \u2212 0.19077\u00d7log10(waist\u2212neck) + 0.15456\u00d7log10(height)) \u2212 450")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "U.S. Navy circumference method (Hodgdon JA, Beckett MB, 1984)")
    _ensure_field(calc, "trust_note",
                  "The Navy method has ~3% error margin compared to DEXA. Accuracy depends on precise neck and waist measurements")
    _ensure_field(calc, "tags", ["body-fat", "navy-method", "health", "fitness", "body-composition", "military"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "bfp", "min": 2, "max": 50,
        "zones": [
            {"min": 2, "max": 5, "label": "Essential fat", "color": "#F44336"},
            {"min": 5, "max": 13, "label": "Athletic", "color": "#4CAF50"},
            {"min": 13, "max": 20, "label": "Fitness", "color": "#2196F3"},
            {"min": 20, "max": 28, "label": "Acceptable", "color": "#FF9800"},
            {"min": 28, "max": 50, "label": "Above average", "color": "#F44336"},
        ],
        "unit": "%",
    })
    _ensure_field(calc, "faqs", [
        {"question": "How do I measure my neck and waist correctly?",
         "answer": "Neck: measure just below the larynx (Adam's apple) with the tape perpendicular to the neck axis. Waist (men): measure at navel level. Waist (women): measure at the narrowest point. Keep the tape snug but not compressing the skin. Take 3 measurements and average."},
        {"question": "How accurate is the Navy body fat method?",
         "answer": "The Navy method has a standard error of ~3% body fat compared to DEXA. It tends to underestimate body fat in very lean individuals and overestimate in very obese individuals. It's most accurate for people in the 10-30% body fat range."},
        {"question": "What is a healthy body fat percentage?",
         "answer": "For men: essential fat 2-5%, athletic 6-13%, fitness 14-17%, acceptable 18-25%, above 25% is overweight. For women: essential 10-13%, athletic 14-20%, fitness 21-24%, acceptable 25-31%, above 31% is overweight."},
        {"question": "Why does the Navy use this method?",
         "answer": "The circumference method is quick, requires only a tape measure, and can be administered to thousands of personnel without specialized equipment. It was developed by the Naval Health Research Center in 1984 and remains the official method for U.S. military body composition assessment."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Lean female athlete", "waist": 68, "neck": 32, "height": 168, "gender": "female"},
        {"_label": "Active female", "waist": 75, "neck": 33, "height": 163, "gender": "female"},
        {"_label": "Fit male", "waist": 82, "neck": 40, "height": 178, "gender": "male"},
        {"_label": "Average male", "waist": 94, "neck": 41, "height": 175, "gender": "male"},
        {"_label": "Overweight male", "waist": 108, "neck": 43, "height": 180, "gender": "male"},
    ])
    _update_field(calc, "range_hints", {
        "waist": "Waist circumference at navel level, 60\u2013150 cm",
        "neck": "Neck circumference below larynx, 25\u201355 cm",
        "height": "Height 100\u2013250 cm",
        "gender": "Male or female (different equations apply)",
    })
    _update_field(calc, "related", ["415", "410", "413", "426", "416"])


# =========================  CIENCIA  ========================================

def update_144(calc):
    _update_field(calc, "formula_display", "F = q \u00d7 v \u00d7 B \u00d7 sin(\u03b8)")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "Lorentz force law")
    _ensure_field(calc, "trust_note",
                  "This calculator uses the Lorentz force equation for a single point charge in a uniform magnetic field")
    _ensure_field(calc, "tags", ["magnetic-force", "lorentz", "physics", "electromagnetism", "charge", "field"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "faqs", [
        {"question": "What is the Lorentz force?",
         "answer": "The Lorentz force is the force on a charged particle moving through electric and magnetic fields. For a magnetic field only, F = qvB sin(\u03b8), where \u03b8 is the angle between velocity and the magnetic field. The force is perpendicular to both v and B."},
        {"question": "When is the magnetic force zero?",
         "answer": "The magnetic force is zero when: (1) the particle has no charge (q = 0), (2) the particle is stationary (v = 0), (3) there is no magnetic field (B = 0), or (4) the velocity is parallel to the magnetic field (\u03b8 = 0\u00b0 or 180\u00b0, so sin(\u03b8) = 0)."},
        {"question": "What units is the force in?",
         "answer": "The calculator outputs force in newtons (N). If you input charge in \u00b5C, convert to coulombs first (1 \u00b5C = 10\u207b\u2076 C). A force of 1 N on a single particle is enormous in particle physics \u2014 typical forces on electrons in lab fields are ~10\u207b\u00b9\u00b3 N."},
        {"question": "What is the right-hand rule?",
         "answer": "For a positive charge: point fingers in direction of v, curl towards B, thumb shows the direction of F. For a negative charge, the force direction is reversed. This calculator gives the magnitude |F|; direction depends on the sign of q."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Electron in lab field", "q": 0.000001, "v": 1000, "B": 0.5, "theta": 90},
        {"_label": "Proton in MRI field", "q": 0.00001, "v": 5000, "B": 1.5, "theta": 90},
        {"_label": "Particle in cyclotron", "q": 0.001, "v": 10000, "B": 2.0, "theta": 45},
        {"_label": "Cosmic ray in Earth's field", "q": 0.0001, "v": 50000, "B": 0.00005, "theta": 60},
        {"_label": "Ion in mass spectrometer", "q": 0.000005, "v": 2000, "B": 0.8, "theta": 90},
    ])
    _update_field(calc, "range_hints", {
        "q": "Charge 0.01\u201310 \u00b5C (microcoulombs)",
        "v": "Velocity 1\u2013100000 m/s",
        "B": "Magnetic field strength 0.001\u20135 T",
        "theta": "Angle between v and B, 0\u201390\u00b0",
    })
    _update_field(calc, "related", ["143", "141", "148", "122"])


# =========================  CLIMA  =========================================

def update_1024(calc):
    _update_field(calc, "formula_display", "AQI = PM2.5 \u00d7 4.17 (simplified linear approximation)")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "US EPA AQI breakpoints (simplified linear approximation)")
    _ensure_field(calc, "trust_note",
                  "This simplified calculator uses linear interpolation. The official EPA AQI uses piecewise linear functions with specific breakpoints for each pollutant")
    _ensure_field(calc, "tags", ["aqi", "air-quality", "pollution", "pm25", "health", "environment"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "aqi", "min": 0, "max": 500,
        "zones": [
            {"min": 0, "max": 50, "label": "Good", "color": "#4CAF50"},
            {"min": 50, "max": 100, "label": "Moderate", "color": "#FFEB3B"},
            {"min": 100, "max": 150, "label": "Sensitive", "color": "#FF9800"},
            {"min": 150, "max": 200, "label": "Unhealthy", "color": "#F44336"},
            {"min": 200, "max": 300, "label": "Very Unhealthy", "color": "#9C27B0"},
            {"min": 300, "max": 500, "label": "Hazardous", "color": "#800000"},
        ],
        "unit": "",
    })
    _ensure_field(calc, "faqs", [
        {"question": "What does the Air Quality Index number mean?",
         "answer": "0-50 Good (green): air quality is satisfactory. 51-100 Moderate (yellow): acceptable but may affect sensitive people. 101-150 Unhealthy for Sensitive Groups (orange). 151-200 Unhealthy (red): everyone may feel effects. 201-300 Very Unhealthy (purple): health alert. 301-500 Hazardous (maroon): emergency conditions."},
        {"question": "How is AQI calculated from PM2.5?",
         "answer": "The EPA uses a piecewise linear function that maps PM2.5 concentrations to AQI values. This simplified calculator uses a linear approximation of AQI = PM2.5 \u00d7 4.17. The official calculation has different slopes for different concentration ranges."},
        {"question": "What PM2.5 level is safe?",
         "answer": "The WHO guideline is an annual average of 5 \u00b5g/m\u00b3 and a 24-hour average of 15 \u00b5g/m\u00b3. The US EPA standard is an annual average of 12 \u00b5g/m\u00b3 and a 24-hour limit of 35 \u00b5g/m\u00b3. Levels above these indicate increased health risk."},
        {"question": "What are the health effects of high AQI?",
         "answer": "PM2.5 particles penetrate deep into lungs and can enter the bloodstream. Short-term exposure causes eye/throat irritation, coughing, and shortness of breath. Long-term exposure increases risk of heart disease, lung cancer, asthma, and premature death."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Clean rural air", "pm25": 6},
        {"_label": "Typical suburban", "pm25": 12},
        {"_label": "Urban background", "pm25": 20},
        {"_label": "Traffic pollution", "pm25": 35},
        {"_label": "Wildfire smoke", "pm25": 80},
        {"_label": "Severe smog event", "pm25": 150},
    ])
    _update_field(calc, "range_hints", {
        "pm25": "PM2.5 concentration 0\u2013500 \u00b5g/m\u00b3",
    })
    _update_field(calc, "related", ["1029", "103", "927"])


def update_1029(calc):
    _update_field(calc, "formula_display",
                  "ET = 0.0023 \u00d7 (T + 17.8) \u00d7 \u221aRH \u00d7 v (simplified empirical formula)")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "Simplified Penman-Monteith approximation")
    _ensure_field(calc, "trust_note",
                  "This simplified formula gives approximate daily ET. For agricultural planning, use the full FAO Penman-Monteith equation with solar radiation data")
    _ensure_field(calc, "tags", ["evapotranspiration", "water-loss", "agriculture", "irrigation", "climate", "crop"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "faqs", [
        {"question": "What is evapotranspiration?",
         "answer": "Evapotranspiration (ET) is the combined water loss from soil evaporation and plant transpiration. It's measured in mm/day and is critical for irrigation scheduling. A typical reference ET value is 3-8 mm/day in summer for temperate climates."},
        {"question": "How do I use ET for irrigation scheduling?",
         "answer": "Multiply the reference ET by a crop coefficient (Kc) to get actual crop water use. For lawns, Kc \u2248 0.7-0.8. Water your lawn when cumulative ET exceeds 25-30mm. This prevents both overwatering and drought stress."},
        {"question": "What factors affect evapotranspiration most?",
         "answer": "Temperature (higher = more ET), humidity (lower = more ET), wind speed (higher = more ET), and solar radiation (more sun = more ET). On a hot, dry, windy day, ET can be 3-4\u00d7 higher than on a cool, humid, calm day."},
        {"question": "Why does this calculator not include solar radiation?",
         "answer": "The 0.0023 coefficient is calibrated for average mid-latitude solar radiation. The full FAO Penman-Monteith equation requires net radiation data that most users don't have. This simplified formula gives reasonable estimates for most locations within \u00b120%."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Cool spring morning", "temp": 12, "rh": 75, "wind": 2.0},
        {"_label": "Mild afternoon", "temp": 20, "rh": 55, "wind": 3.0},
        {"_label": "Warm summer day", "temp": 28, "rh": 40, "wind": 4.0},
        {"_label": "Hot dry wind", "temp": 35, "rh": 20, "wind": 6.0},
        {"_label": "Desert conditions", "temp": 42, "rh": 10, "wind": 8.0},
    ])
    _update_field(calc, "range_hints", {
        "temp": "Air temperature 0\u201350 \u00b0C",
        "rh": "Relative humidity 10\u2013100 %",
        "wind": "Wind speed 0\u201320 m/s",
    })
    _update_field(calc, "related", ["1024", "103", "125"])


# =========================  UTILIDADES  =====================================

def update_1030(calc):
    _update_field(calc, "formula_display",
                  "DOY = sum of days in preceding months + day of current month")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "ISO 8601 ordinal date format")
    _ensure_field(calc, "trust_note",
                  "Non-leap year calculation. For leap years, add 1 to result for dates after 29 February")
    _ensure_field(calc, "tags", ["day-of-year", "julian-date", "ordinal-date", "calendar", "utility", "date"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "faqs", [
        {"question": "What is the day of the year?",
         "answer": "The day of the year (DOY) is the ordinal number of a day within a calendar year, from 1 to 365 (or 366 in leap years). January 1st is DOY 1, and December 31st is DOY 365. It's used in astronomy, agriculture, hydrology, and scientific data logging."},
        {"question": "Is this the same as Julian date?",
         "answer": "In common usage, 'Julian date' often refers to the day-of-year number (e.g., 'Julian day 100' = 10 April). However, in astronomy, Julian Date (JD) is a continuous count of days since 4713 BC, which is different. This calculator gives the ordinal day number."},
        {"question": "Does this calculator account for leap years?",
         "answer": "No \u2014 this calculator assumes a non-leap year (February has 28 days). For leap years, add 1 to the result for any date after February 29. Leap years are years divisible by 4, except century years not divisible by 400."},
        {"question": "What is this used for?",
         "answer": "Day-of-year numbers are used in: calculating growing degree days in agriculture, hydrological water year calculations (which often start on October 1 = DOY 274), satellite orbit tracking, and fiscal year day counting in accounting."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "New Year's Day", "month": 1, "day": 1},
        {"_label": "Spring equinox", "month": 3, "day": 20},
        {"_label": "Mid-year (Jul 1)", "month": 7, "day": 1},
        {"_label": "Autumn equinox", "month": 9, "day": 22},
        {"_label": "Christmas Day", "month": 12, "day": 25},
    ])
    _update_field(calc, "range_hints", {
        "month": "Month number 1\u201312",
        "day": "Day of month 1\u201331 (validated by month)",
    })
    _update_field(calc, "related", ["932", "423"])


# =========================  FOTOGRAFIA  =====================================

def update_1039(calc):
    _update_field(calc, "formula_display",
                  "EV = log\u2082(aperture\u00b2 / (1/shutter_speed)) \u2212 log\u2082(ISO/100)")
    _ensure_field(calc, "wastage_pct", 0)
    _ensure_field(calc, "standard", "APEX (Additive System of Photographic Exposure) standard, ISO 2720")
    _ensure_field(calc, "trust_note",
                  "Exposure Value 0 corresponds to f/1.0 at 1 second at ISO 100. Each +1 EV doubles the light; each \u22121 EV halves it")
    _ensure_field(calc, "tags", ["exposure", "photography", "EV", "aperture", "shutter-speed", "ISO"])
    _ensure_field(calc, "date_modified", "2025-01-01")
    _ensure_field(calc, "gauge_config", {
        "output_key": "ev", "min": -5, "max": 20,
        "zones": [
            {"min": -5, "max": 0, "label": "Very dark (night)", "color": "#1A237E"},
            {"min": 0, "max": 5, "label": "Low light", "color": "#455A64"},
            {"min": 5, "max": 10, "label": "Indoor/daylight", "color": "#2196F3"},
            {"min": 10, "max": 14, "label": "Bright daylight", "color": "#4CAF50"},
            {"min": 14, "max": 20, "label": "Very bright (snow/beach)", "color": "#FFEB3B"},
        ],
        "unit": "EV",
    })
    _ensure_field(calc, "faqs", [
        {"question": "What is Exposure Value (EV)?",
         "answer": "Exposure Value is a number that represents a combination of aperture and shutter speed that gives the same exposure. EV 0 = f/1.0 at 1 second at ISO 100. Each increase of 1 EV represents half the light (darker) or double the shutter speed. It's used to compare lighting conditions."},
        {"question": "How do I use EV in practice?",
         "answer": "If your light meter reads EV 12 at ISO 100, you can use f/8 at 1/125s, f/5.6 at 1/250s, or f/11 at 1/60s \u2014 all give the same exposure. EV helps you trade aperture for shutter speed while maintaining correct exposure."},
        {"question": "What EV corresponds to different lighting conditions?",
         "answer": "Candlelight: EV 2-3. Home interior: EV 5-7. Overcast day: EV 11-13. Sunny day: EV 14-15. Bright snow/beach: EV 16-17. Night street: EV 3-5. Sports stadium: EV 8-10. Full moon: EV -2 to -3."},
        {"question": "Why does ISO affect EV?",
         "answer": "EV is defined at ISO 100. If you set ISO 400, the sensor is 4\u00d7 more sensitive (2 stops), so a scene that measures EV 10 at ISO 100 becomes effectively EV 12 (brighter) at ISO 400. The calculator subtracts the ISO adjustment to give the standard EV."},
    ])
    _update_field(calc, "comparison_presets", [
        {"_label": "Night street scene", "aperture": 2.8, "shutter": 30, "iso": 800},
        {"_label": "Indoor room", "aperture": 4.0, "shutter": 60, "iso": 400},
        {"_label": "Overcast day", "aperture": 5.6, "shutter": 125, "iso": 100},
        {"_label": "Bright sunlight", "aperture": 8.0, "shutter": 500, "iso": 100},
        {"_label": "Snow/beach scene", "aperture": 11.0, "shutter": 1000, "iso": 100},
    ])
    _update_field(calc, "range_hints", {
        "aperture": "Aperture f/1.0 to f/32",
        "shutter": "Shutter speed 1/8000 to 30 seconds",
        "iso": "ISO sensitivity 50\u201325600",
    })
    _update_field(calc, "related", ["104", "107", "706"])


# =========================  DISPATCH TABLE  =================================

UPDATERS = {
    "001": update_001,   "002": update_002,   "003": update_003,
    "004": update_004,   "005": update_005,   "006": update_006,
    "007": update_007,   "008": update_008,   "009": update_009,
    "010": update_010,
    "1101": update_1101, "1102": update_1102, "1104": update_1104,
    "1116": update_1116, "1119": update_1119,
    "415": update_415,   "425": update_425,
    "144": update_144,
    "1024": update_1024, "1029": update_1029,
    "1030": update_1030, "1039": update_1039,
}


def main():
    # 1. Read input
    print(f"Reading {INPUT_PATH} ...")
    if not os.path.exists(INPUT_PATH):
        sys.exit(f"ERROR: File not found: {INPUT_PATH}")

    with open(INPUT_PATH, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    calculators = data.get("calculators")
    if not isinstance(calculators, list):
        sys.exit("ERROR: Expected 'calculators' to be a list.")

    # Build index
    by_id = {}
    for idx, calc in enumerate(calculators):
        cid = calc.get("id")
        if cid:
            by_id[cid] = idx

    # 2. Apply updates
    updated_count = 0
    missing_ids = []
    for target_id in TARGET_IDS:
        if target_id not in by_id:
            missing_ids.append(target_id)
            continue
        idx = by_id[target_id]
        calc = calculators[idx]
        updater = UPDATERS.get(target_id)
        if updater:
            updater(calc)
            updated_count += 1
            print(f"  Updated {target_id} ({calc.get('slug', '?')})")
        else:
            print(f"  SKIP {target_id} — no updater defined")

    if missing_ids:
        print(f"\nWARNING: {len(missing_ids)} IDs not found in source: {missing_ids}")

    # 3. Basic validation
    print(f"\nRunning validation...")
    errors = []
    for target_id in TARGET_IDS:
        if target_id in by_id:
            calc = calculators[by_id[target_id]]
            # Check buying_units keys match output IDs
            bu = calc.get("buying_units", {})
            outputs = {o["id"] for o in calc.get("outputs", [])}
            for key in bu:
                if key not in outputs:
                    errors.append(f"  {target_id}: buying_units key '{key}' not in outputs {outputs}")
            # Check comparison_presets have _label
            presets = calc.get("comparison_presets", [])
            for i, p in enumerate(presets):
                if "_label" not in p:
                    errors.append(f"  {target_id}: comparison_preset[{i}] missing _label")

    if errors:
        print("WARNINGS:")
        for e in errors:
            print(e)
    else:
        print("  All validations passed.")

    # 4. Write output
    print(f"\nWriting {INPUT_PATH} ...")
    with open(INPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"\nDone. Updated {updated_count} of {len(TARGET_IDS)} calculators.")
    print(f"Total calculators in file: {len(calculators)}")


if __name__ == "__main__":
    main()
