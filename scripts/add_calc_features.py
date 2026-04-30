"""Add comparison_presets, standard, diagram, buying_units to top calculators."""
import json
from pathlib import Path
import math

ROOT = Path(__file__).parent.parent
CALC_PATH = ROOT / "src" / "calculators" / "calculators.json"

# Fields to add per calculator id
ADDITIONS = {
    # ── Concrete slab (hormigon-masa) ──────────────────────────────────────────
    "001": {
        "diagram": "slab",
        "standard": "EN 206 / ACI 318",
        "trust_note": "Concrete density 2,400 kg/m³",
        "comparison_presets": [
            {"largo": 3, "ancho": 3, "espesor": 0.10},
            {"largo": 4, "ancho": 4, "espesor": 0.10},
            {"largo": 5, "ancho": 5, "espesor": 0.12},
            {"largo": 6, "ancho": 4, "espesor": 0.15},
            {"largo": 10, "ancho": 5, "espesor": 0.15},
            {"largo": 10, "ancho": 10, "espesor": 0.20},
        ],
        "buying_units": {
            "volumen": [
                {"label": "Bags 25 kg", "factor": 10.0, "round": "ceil", "unit": "bags"},
                {"label": "Ready-mix truck (6 m³)", "factor": 0.167, "round": "ceil", "unit": "trucks"},
            ]
        },
    },
    # ── Reinforced concrete (hormigon-armado) ──────────────────────────────────
    "002": {
        "diagram": "slab",
        "standard": "EN 1992-1-1 (Eurocode 2) / ACI 318",
        "trust_note": "Concrete density 2,400 kg/m³",
        "comparison_presets": [
            {"largo": 3, "ancho": 3, "espesor": 0.15, "kg_acero_m3": 80},
            {"largo": 4, "ancho": 4, "espesor": 0.15, "kg_acero_m3": 100},
            {"largo": 5, "ancho": 5, "espesor": 0.20, "kg_acero_m3": 120},
            {"largo": 6, "ancho": 4, "espesor": 0.20, "kg_acero_m3": 120},
            {"largo": 10, "ancho": 5, "espesor": 0.20, "kg_acero_m3": 100},
        ],
    },
    # ── Isolated footing (zapata-aislada) ─────────────────────────────────────
    "003": {
        "diagram": "slab",
        "standard": "EN 1997-1 / ACI 336",
        "comparison_presets": [
            {"largo": 0.8, "ancho": 0.8, "canto": 0.40, "cantidad": 4},
            {"largo": 1.0, "ancho": 1.0, "canto": 0.50, "cantidad": 6},
            {"largo": 1.2, "ancho": 1.2, "canto": 0.60, "cantidad": 8},
            {"largo": 1.5, "ancho": 1.5, "canto": 0.60, "cantidad": 10},
        ],
    },
    # ── Strip footing (cimiento-corrido) ──────────────────────────────────────
    "009": {
        "diagram": "wall",
        "standard": "EN 1997-1",
        "comparison_presets": [
            {"longitud": 10, "ancho": 0.40, "profundidad": 0.50},
            {"longitud": 20, "ancho": 0.50, "profundidad": 0.60},
            {"longitud": 30, "ancho": 0.50, "profundidad": 0.70},
            {"longitud": 40, "ancho": 0.60, "profundidad": 0.80},
        ],
    },
    # ── Brick wall (ladrillo-hueco) ────────────────────────────────────────────
    "011": {
        "diagram": "wall",
        "standard": "EN 1996-1-1 (Eurocode 6)",
        "comparison_presets": [
            {"largo": 5, "alto": 2.5, "descontar_huecos": 0},
            {"largo": 8, "alto": 2.5, "descontar_huecos": 0},
            {"largo": 10, "alto": 2.7, "descontar_huecos": 2},
            {"largo": 15, "alto": 2.7, "descontar_huecos": 4},
            {"largo": 20, "alto": 3.0, "descontar_huecos": 6},
        ],
    },
    # ── Concrete block (bloque-hormigon) ──────────────────────────────────────
    "013": {
        "diagram": "wall",
        "standard": "EN 1996-1-1",
        "comparison_presets": [
            {"largo": 5, "alto": 2.5, "descontar_huecos": 0},
            {"largo": 8, "alto": 2.5, "descontar_huecos": 0},
            {"largo": 10, "alto": 2.7, "descontar_huecos": 2},
            {"largo": 15, "alto": 3.0, "descontar_huecos": 4},
        ],
    },
    # ── Cement mortar (mortero-cemento) ───────────────────────────────────────
    "017": {
        "diagram": "wall",
        "standard": "EN 998-2",
        "comparison_presets": [
            {"area": 5, "espesor_cm": 1, "dosificacion": "1:3"},
            {"area": 10, "espesor_cm": 1.5, "dosificacion": "1:4"},
            {"area": 20, "espesor_cm": 2, "dosificacion": "1:4"},
            {"area": 30, "espesor_cm": 2, "dosificacion": "1:5"},
        ],
    },
}

data = json.loads(CALC_PATH.read_text(encoding="utf-8"))
updated = 0
for calc in data["calculators"]:
    cid = calc.get("id", "")
    if cid in ADDITIONS:
        for key, val in ADDITIONS[cid].items():
            calc[key] = val
        updated += 1

CALC_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated {updated} calculators with comparison_presets, standard, diagram, buying_units")
