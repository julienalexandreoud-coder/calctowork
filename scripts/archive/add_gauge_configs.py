"""
Add GAUGE_CONFIGS for calculators with clearly bounded outputs.
Conservative approach: only percentage, BPM, BMI, COP, EER, and known sports scores.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
GEN_FILE = ROOT / "scripts" / "generate_calctowork.py"

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(GEN_FILE, "r", encoding="utf-8") as f:
    gen_text = f.read()

# Find GAUGE_CONFIGS
gauge_match = re.search(r'(GAUGE_CONFIGS = \{)(.*?)(\n\})', gen_text, re.DOTALL)
if not gauge_match:
    print("ERROR: GAUGE_CONFIGS not found")
    exit(1)

gauge_body = gauge_match.group(2)
existing_ids = set(re.findall(r'"(\d+)"\s*:', gauge_body))
print(f"Existing gauge configs: {len(existing_ids)}")

calcs = data["calculators"]
new_configs = []

for calc in calcs:
    cid = calc["id"]
    if cid in existing_ids:
        continue
    
    outputs = calc.get("outputs", [])
    if not outputs:
        continue
    
    first_out = outputs[0]
    unit = first_out.get("unit", "")
    out_id = first_out.get("id", "")
    block = calc.get("block_slug", "")
    
    config = None
    
    # ── Percentage outputs ──
    if unit == "%":
        label = out_id.replace("_", " ").title()
        # Finance: ROI, return, CAGR can be negative
        if block == "finanzas":
            if out_id in ("roi", "retorno", "return", "cagr", "rentabilidad"):
                config = {"min": -50, "max": 200, "label": label, "unit": "%"}
            else:
                config = {"min": 0, "max": 100, "label": label, "unit": "%"}
        # Health
        elif block == "salud":
            if out_id in ("grasa_pct", "body_fat", "grasa", "fat", "grasa_corporal"):
                config = {"min": 3, "max": 60, "label": "Fat %", "unit": "%"}
            elif out_id in ("imc", "bmi"):
                config = {"min": 10, "max": 45, "label": "BMI", "unit": "kg/m²"}
            else:
                config = {"min": 0, "max": 100, "label": label, "unit": "%"}
        # Climate / efficiency
        elif block in ("climatizacion", "electronica"):
            if out_id in ("eficiencia", "efficiency", "rendimiento"):
                config = {"min": 0, "max": 100, "label": "Effic.", "unit": "%"}
            else:
                config = {"min": 0, "max": 100, "label": label, "unit": "%"}
        # Electricidad: voltage drop
        elif block == "electricidad":
            if out_id in ("caida", "drop", "caida_tension"):
                config = {"min": 0, "max": 10, "label": "Drop", "unit": "%"}
            else:
                config = {"min": 0, "max": 100, "label": label, "unit": "%"}
        # Generic percentage
        else:
            config = {"min": 0, "max": 100, "label": label, "unit": "%"}
    
    # ── BMI (only if health block and BMI output) ──
    elif unit == "kg/m²" and block == "salud" and out_id in ("imc", "bmi"):
        config = {"min": 10, "max": 45, "label": "BMI", "unit": "kg/m²"}
    
    # ── Heart rate ──
    elif unit == "bpm" and block == "salud":
        config = {"min": 40, "max": 220, "label": "HR", "unit": "bpm"}
    
    # ── kcal (health) ──
    elif unit == "kcal" and block == "salud":
        config = {"min": 0, "max": 5000, "label": "kcal", "unit": "kcal"}
    
    # ── VO2 max ──
    elif unit == "ml/kg/min" and block == "salud":
        config = {"min": 20, "max": 80, "label": "VO₂ max", "unit": "ml/kg/min"}
    
    # ── COP / EER ──
    elif unit == "COP":
        config = {"min": 0, "max": 15, "label": "COP", "unit": "COP"}
    elif unit == "EER":
        config = {"min": 0, "max": 100, "label": "EER", "unit": "EER"}
    
    # ── Sports weights ──
    elif unit == "kg" and block == "deportes":
        config = {"min": 0, "max": 300, "label": "kg", "unit": "kg"}
    
    # ── Speed ──
    elif unit == "km/h" and block in ("ciencia", "transporte", "cotidiano"):
        config = {"min": 0, "max": 200, "label": "Speed", "unit": "km/h"}
    
    # ── L/day (hydration) ──
    elif unit == "L" and block == "salud" and out_id in ("agua", "water", "hidratacion"):
        config = {"min": 0, "max": 6, "label": "L/day", "unit": "L"}
    
    if config:
        new_configs.append((cid, config))

if not new_configs:
    print("No new gauge configs to add.")
    exit(0)

lines = []
for cid, cfg in new_configs:
    pad = " " * (20 - len(cid))
    lines.append(f'    "{cid}": {pad}{{"min": {cfg["min"]}, "max": {cfg["max"]}, "label": "{cfg["label"]}", "unit": "{cfg["unit"]}"}},')

entries_text = "\n".join(lines) + "\n"
insert_pos = gauge_match.end(2)
new_gen_text = gen_text[:insert_pos] + entries_text + gen_text[insert_pos:]

with open(GEN_FILE, "w", encoding="utf-8") as f:
    f.write(new_gen_text)

print(f"Added {len(new_configs)} gauge configs")
for cid, cfg in new_configs[:10]:
    print(f'  {cid}: {cfg}')
if len(new_configs) > 10:
    print(f'  ... and {len(new_configs)-10} more')
