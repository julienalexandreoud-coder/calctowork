"""Add comparison_presets to the 10 calcs that don't have them yet."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_JSON = ROOT / "src" / "calculators" / "calculators.json"

data = json.loads(CALCS_JSON.read_text(encoding="utf-8"))
calcs = data["calculators"]

PRESETS = {
    # Statistics — common datasets
    "136": [  # desviacion-estandar
        {"_label": "Test scores", "values": "72,85,90,68,95,78,83,91,76,88"},
        {"_label": "Daily temps (°C)", "values": "18,21,23,19,25,22,20,24,17,26"},
        {"_label": "Sample dataset", "values": "2,4,4,4,5,5,7,9"},
        {"_label": "Heights (cm)", "values": "165,170,172,168,175,180,163,171"},
        {"_label": "Weights (kg)", "values": "60,65,72,58,80,68,75,63"},
    ],
    "137": [  # varianza
        {"_label": "Test scores", "values": "72,85,90,68,95,78,83,91,76,88"},
        {"_label": "Daily temps (°C)", "values": "18,21,23,19,25,22,20,24,17,26"},
        {"_label": "Sample dataset", "values": "2,4,4,4,5,5,7,9"},
        {"_label": "Heights (cm)", "values": "165,170,172,168,175,180,163,171"},
        {"_label": "Weights (kg)", "values": "60,65,72,58,80,68,75,63"},
    ],
    "138": [  # mediana
        {"_label": "Odd count", "values": "3,7,12,5,9,1,15"},
        {"_label": "Even count", "values": "4,8,2,10,6,14"},
        {"_label": "Test scores", "values": "55,62,70,78,82,88,91,95"},
        {"_label": "Sample dataset", "values": "1,3,5,7,9"},
        {"_label": "Salaries (k)", "values": "32,35,38,40,42,45,48,55,65,90"},
    ],
    "139": [  # cuartiles
        {"_label": "10 values", "values": "1,2,3,4,5,6,7,8,9,10"},
        {"_label": "Test scores", "values": "50,55,60,65,70,75,80,85,90,95,100"},
        {"_label": "Ages", "values": "22,25,28,31,34,37,40,43,46,49,52"},
        {"_label": "Salaries (k)", "values": "28,32,35,38,40,42,45,48,52,58,65,75"},
        {"_label": "Heights (cm)", "values": "155,160,163,165,168,170,172,175,178,182,185"},
    ],
    # Hex color converter — common web colors
    "1038": [
        {"_label": "Pure red", "hex": "#FF0000"},
        {"_label": "Pure blue", "hex": "#0000FF"},
        {"_label": "Brand orange", "hex": "#F97316"},
        {"_label": "Dark navy", "hex": "#1E3A5F"},
        {"_label": "Forest green", "hex": "#22C55E"},
    ],
    # Molar mass — common molecules
    "1070": [
        {"_label": "Water (H₂O)", "formula_quimica": "18"},
        {"_label": "CO₂", "formula_quimica": "44"},
        {"_label": "NaCl (salt)", "formula_quimica": "58.44"},
        {"_label": "Glucose (C₆H₁₂O₆)", "formula_quimica": "180"},
        {"_label": "Ethanol (C₂H₅OH)", "formula_quimica": "46"},
    ],
    # Character counter — sample texts
    "1091": [
        {"_label": "Short sentence", "texto": "The quick brown fox jumps over the lazy dog."},
        {"_label": "Tweet length", "texto": "Just shipped a new feature that makes our users 3x more productive. Excited to share the details soon! #buildinpublic"},
        {"_label": "SMS limit", "texto": "Hi! Your appointment is confirmed for tomorrow at 10am. Please reply YES to confirm or call us to reschedule."},
        {"_label": "Paragraph", "texto": "Calculating the right amount of materials for a construction project saves time and money. Whether you are working with concrete, tiles, or paint, accurate quantities prevent costly over-orders and frustrating shortages."},
        {"_label": "Spanish text", "texto": "Hola mundo, esta es una prueba de conteo de caracteres en español."},
    ],
}

updated = 0
for calc in calcs:
    cid = calc["id"]
    if cid in PRESETS and not calc.get("comparison_presets"):
        calc["comparison_presets"] = PRESETS[cid]
        updated += 1
        print(f"  [OK] {cid} {calc.get('slug','')} -> {len(PRESETS[cid])} presets")

data["calculators"] = calcs
CALCS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\n[DONE] Added presets to {updated} calcs")
