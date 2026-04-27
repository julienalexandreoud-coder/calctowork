"""
Patch calculators.json:
1. Add unit_options/unit_category to 20 key calcs (conversion, health, sports, science)
2. Update formulas for conversion calcs so they work with unit-normalized inputs
3. Update BMI and mortgage formulas for richer output (amortization table, peso_min/peso_max)
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"

with open(CALCS_FILE, encoding="utf-8") as f:
    data = json.load(f)

calcs = data["calculators"]
by_id = {c["id"]: c for c in calcs}

def set_input_units(calc, input_id, unit_options, unit_category, unit_default):
    for inp in calc.get("inputs", []):
        if inp["id"] == input_id:
            inp["unit_options"] = unit_options
            inp["unit_category"] = unit_category
            inp["unit_default"] = unit_default
            return True
    return False

# ── 1. CONVERSION CALCS — add unit selector to the main input ──────────────────

# 800 longitud — input valor_m expects meters; length base=m
c = by_id["800"]
set_input_units(c, "valor_m", ["m","cm","mm","km","ft","in","yd","mi"], "length", "m")

# 801 peso — input valor_kg expects kg; mass base=kg
c = by_id["801"]
set_input_units(c, "valor_kg", ["kg","g","lb","oz","t"], "mass", "kg")

# 802 temperatura — input celsius expects °C; need temp_c
c = by_id["802"]
set_input_units(c, "celsius", ["°C","°F","K"], "temp_c", "°C")

# 803 volumen — input valor_l expects liters; need volume_L
c = by_id["803"]
set_input_units(c, "valor_l", ["L","mL","m³","cm³","ft³","gal(us)","gal(uk)"], "volume_L", "L")

# 804 area — input valor_m2 expects m²; area base=m²
c = by_id["804"]
set_input_units(c, "valor_m2", ["m²","cm²","mm²","km²","ft²","in²","ha","ac"], "area", "m²")
# Fix: update formula to use 'm²' key consistently
c["formula"] = ("var m2=parseFloat(inputs.valor_m2)||0;"
                "return{cm2:+(m2*10000).toFixed(2),mm2:+(m2*1e6).toFixed(0),"
                "km2:+(m2/1e6).toFixed(10),ft2:+(m2*10.7639).toFixed(4),"
                "in2:+(m2*1550.0031).toFixed(2),ha:+(m2/10000).toFixed(6),"
                "ac:+(m2/4046.86).toFixed(6)};")

# 805 velocidad-unidades — input valor_kmh expects km/h; need speed_kmh
c = by_id["805"]
set_input_units(c, "valor_kmh", ["km/h","m/s","mph","knot","ft/s"], "speed_kmh", "km/h")

# 806 datos-digitales — input valor_mb expects MB; need digital_MB
c = by_id["806"]
set_input_units(c, "valor_mb", ["MB","KB","GB","TB"], "digital_MB", "MB")

# 807 presion-unidades — input valor_atm expects atm; need pressure_atm
c = by_id["807"]
set_input_units(c, "valor_atm", ["atm","Pa","kPa","bar","psi","mmHg","torr"], "pressure_atm", "atm")

# 808 tiempo-unidades — input valor_h expects hours; need time_h
c = by_id["808"]
set_input_units(c, "valor_h", ["h","min","s","d","wk"], "time_h", "h")

# 809 energia-unidades — input valor_j expects J; energy base=J
c = by_id["809"]
set_input_units(c, "valor_j", ["J","kJ","kWh","kcal","BTU"], "energy", "J")

# ── 2. HEALTH CALCS — weight kg↔lb, height cm↔in ────────────────────────────

for cid in ["400","401","402","403","410","411","412","413","414"]:
    c = by_id.get(cid)
    if not c:
        continue
    set_input_units(c, "peso_kg", ["kg","lb"], "mass", "kg")
    set_input_units(c, "altura_cm", ["cm","m","ft","in"], "length_cm", "cm")

# ── 3. SPORTS CALCS — weight kg↔lb, distance km↔mi ──────────────────────────

for cid in ["900","901","905","908","909"]:
    c = by_id.get(cid)
    if not c:
        continue
    set_input_units(c, "peso_kg", ["kg","lb"], "mass", "kg")
    set_input_units(c, "distancia_km", ["km","mi","m"], "length_km", "km")

# ── 4. SCIENCE CALCS — mass and distance units ──────────────────────────────

for cid in ["700","701","702","703","704","705","706"]:
    c = by_id.get(cid)
    if not c:
        continue
    set_input_units(c, "masa", ["kg","g","lb","t"], "mass", "kg")
    set_input_units(c, "masa_kg", ["kg","g","lb","t"], "mass", "kg")
    set_input_units(c, "distancia", ["m","cm","km","ft","mi"], "length", "m")
    set_input_units(c, "altura", ["m","cm","ft","in"], "length", "m")

# ── 5. RICH FORMULA: BMI — add peso_min, peso_max outputs ────────────────────
c = by_id["400"]
c["formula"] = (
    "var P=parseFloat(inputs.peso_kg)||0,H=parseFloat(inputs.altura_cm)||0;"
    "if(!P||!H||H<50)return{error:true};"
    "var h=H/100,imc=+(P/(h*h)).toFixed(1),cat,cat_en;"
    "if(imc<18.5){cat='Bajo peso';cat_en='Underweight';}"
    "else if(imc<25){cat='Normal';cat_en='Healthy';}"
    "else if(imc<30){cat='Sobrepeso';cat_en='Overweight';}"
    "else if(imc<35){cat='Obesidad I';cat_en='Obese I';}"
    "else{cat='Obesidad II+';cat_en='Obese II+';}"
    "var pmin=+(18.5*h*h).toFixed(1),pmax=+(24.9*h*h).toFixed(1);"
    "return{imc:imc,categoria:cat,peso_saludable_min:pmin,peso_saludable_max:pmax};"
)
# Update outputs to add the two new fields
c["outputs"] = [
    {"id":"imc","unit":"kg/m²","highlight":True},
    {"id":"categoria","unit":""},
    {"id":"peso_saludable_min","unit":"kg"},
    {"id":"peso_saludable_max","unit":"kg"},
]

# ── 6. RICH FORMULA: Hipoteca — add amortization table ───────────────────────
c = by_id["300"]
c["formula"] = (
    "var P=parseFloat(inputs.precio_vivienda)||0,E=parseFloat(inputs.entrada_pct)||20,"
    "R=parseFloat(inputs.interes_anual_pct)||0,N=parseFloat(inputs.plazo_anos)||0;"
    "if(!P||!R||!N)return{error:true};"
    "var principal=+(P*(1-E/100)).toFixed(2),r=R/100/12,n=N*12;"
    "var cuota=r?principal*(r*Math.pow(1+r,n))/(Math.pow(1+r,n)-1):principal/n;"
    "var total=+(cuota*n).toFixed(2),intereses=+(total-principal).toFixed(2);"
    "var tbl=[],bal=principal;"
    "for(var i=1;i<=N;i++){"
    "  var int_yr=+(bal*R/100).toFixed(2);"
    "  var pri_yr=+(Math.min(cuota*12-int_yr,bal)).toFixed(2);"
    "  bal=+(Math.max(bal-pri_yr,0)).toFixed(2);"
    "  tbl.push({year:i,interest:int_yr,principal:pri_yr,balance:bal});"
    "}"
    "return{cuota_mensual:+cuota.toFixed(2),principal_eur:+principal.toFixed(0),"
    "total_intereses:intereses,total_pagado:total,table:tbl};"
)
# Add table headers config
c["tableHeaders"] = ["year","interest","principal","balance"]

# ── 7. RICH FORMULA: Interés Compuesto — add year-by-year table ──────────────
c = by_id["302"]
c["formula"] = (
    "var P=parseFloat(inputs.capital_inicial)||0,"
    "r=parseFloat(inputs.tasa_anual_pct)||0,"
    "n=parseFloat(inputs.anos)||0,"
    "ap=parseFloat(inputs.aportacion_anual)||0;"
    "if(!P||!r||!n)return{error:true};"
    "var rate=r/100,bal=P,tbl=[];"
    "for(var i=1;i<=n;i++){"
    "  var int_yr=+(bal*rate).toFixed(2);"
    "  bal=+(bal+int_yr+ap).toFixed(2);"
    "  tbl.push({year:i,interest:int_yr,balance:bal});"
    "}"
    "var total_int=+(bal-P-ap*n).toFixed(2);"
    "return{capital_final:+bal.toFixed(2),total_intereses:total_int,table:tbl};"
)
c["tableHeaders"] = ["year","interest","balance"]

# ── Write back ────────────────────────────────────────────────────────────────
data["calculators"] = calcs
out = json.dumps(data, ensure_ascii=False, indent=2)
with open(CALCS_FILE, "w", encoding="utf-8", newline="\n") as f:
    f.write(out)
print(f"[OK] calculators.json patched ({len(calcs)} calcs)")

# Check how many now have unit_options
count = sum(
    1 for c in calcs
    for inp in c.get("inputs", [])
    if inp.get("unit_options")
)
print(f"[OK] {count} inputs now have unit switching enabled")
