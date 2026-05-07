import json
from pathlib import Path

CALCS_FILE = Path(r"C:\Microsaas\obra\src\calculators\calculators.json")

with open(CALCS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Unit mapping: unit -> (unit_options list, unit_category)
UNIT_MAP = {
    "m":    (["m", "cm", "mm", "ft", "in"], "length"),
    "m²":   (["m²", "ft²"], "area"),
    "m³":   (["m³", "ft³"], "volume"),
    "kg":   (["kg", "g", "lb"], "mass"),
    "kg/m³":(["kg/m³", "g/cm³", "lb/ft³"], "density"),
    "kg/m²":(["kg/m²", "g/m²", "lb/ft²"], "density"),
    "cm":   (["cm", "m", "mm", "in", "ft"], "length"),
    "mm":   (["mm", "cm", "m", "in"], "length"),
    "L":    (["L", "mL", "gal"], "volume"),
    "L/min":(["L/min", "gal/min"], "flow"),
    "L/s":  (["L/s", "m³/h", "gal/min"], "flow"),
    "bar":  (["bar", "psi", "atm"], "pressure"),
    "°C":   (["°C", "°F", "K"], "temperature"),
    "W":    (["W", "kW"], "power"),
    "Wh":   (["Wh", "kWh"], "energy"),
    "Wh/day":(["Wh/day", "kWh/day"], "energy"),
    "kN/m²":(["kN/m²", "kg/m²", "lb/ft²"], "pressure"),
    "%":    (["%"], "ratio"),
    "sacos 50kg": (["sacos 50kg"], "count"),
    "sacos 25kg": (["sacos 25kg"], "count"),
    "ud":   (["ud"], "count"),
    "tramos": (["tramos"], "count"),
    "camiones": (["camiones"], "count"),
    "m.l.": (["m.l."], "length"),
    "m²/caja": (["m²/caja"], "area"),
    "hojas": (["hojas"], "count"),
    "manos": (["manos"], "count"),
    "litros": (["litros", "L"], "volume"),
    "rollos": (["rollos"], "count"),
    "factor": (["factor"], "ratio"),
    "°":    (["°"], "angle"),
    "h":    (["h", "min"], "time"),
    "A":    (["A", "mA"], "current"),
    "kW":   (["kW", "W"], "power"),
    "V":    (["V", "kV"], "voltage"),
    "m/s":  (["m/s", "km/h", "ft/s"], "speed"),
    "km":   (["km", "m", "mi"], "length"),
    "yr":   (["yr", "mo"], "time"),
    "N":    (["N", "kN", "lbf"], "force"),
    "s":    (["s", "min", "h"], "time"),
    "min":  (["min", "s", "h"], "time"),
    "deg":  (["deg", "rad"], "angle"),
    "J":    (["J", "kJ", "cal"], "energy"),
}

# Special per-input-id overrides
ID_UNIT_MAP = {
    "espesor_cm": (["cm", "m", "mm", "in"], "length"),
    "espesor_mm": (["mm", "cm", "m", "in"], "length"),
    "tam_pieza_cm": (["cm", "m", "mm", "in"], "length"),
    "ancho_junta_mm": (["mm", "cm"], "length"),
    "grosor_pieza_mm": (["mm", "cm"], "length"),
    "pendiente_pct": (["%"], "ratio"),
    "m2_por_caja": (["m²/caja"], "area"),
    "piezas_por_caja": (["piezas/caja"], "count"),
    "dotacion": (["L/persona·día"], "flow"),
    "habitantes": (["habitantes"], "count"),
    "dias": (["días"], "time"),
    "temperatura": (["°C", "°F", "K"], "temperature"),
    "humedad": (["%"], "ratio"),
    "potencia": (["W", "kW"], "power"),
    "voltaje": (["V", "kV"], "voltage"),
    "longitud_cable": (["m", "cm", "mm", "ft"], "length"),
    "caida_max": (["%"], "ratio"),
    "precio_kwh": (["€/kWh", "$/kWh"], "price"),
    "horas_dia": (["h"], "time"),
    "costo_m2": (["€/m²", "$/m²"], "price"),
    "imprevistos": (["%"], "ratio"),
    "horas": (["h"], "time"),
    "costo_hora": (["€/h", "$/h"], "price"),
    "num_operarios": (["operarios"], "count"),
    "costo_inicial": (["€", "$"], "currency"),
    "valor_residual": (["€", "$"], "currency"),
    "vida_util": (["años"], "time"),
    "valor_inicial": (["€", "$"], "currency"),
    "edad_anos": (["años"], "time"),
    "margen": (["%"], "ratio"),
    "iva": (["%"], "ratio"),
    "separacion": (["m", "cm"], "length"),
    "num_piezas": (["piezas"], "count"),
    "largo_baldosa": (["cm", "m", "mm"], "length"),
    "ancho_baldosa": (["cm", "m", "mm"], "length"),
    "largo_azulejo": (["cm", "m", "mm"], "length"),
    "ancho_azulejo": (["cm", "m", "mm"], "length"),
    "desperdicio": (["%"], "ratio"),
    "precio_m2": (["€/m²", "$/m²"], "price"),
    "precio_kg": (["€/kg", "$/kg"], "price"),
    "caudal": (["L/min", "L/s", "m³/h", "gal/min"], "flow"),
    "presion_entrada": (["bar", "psi", "atm"], "pressure"),
    "u_muros": (["W/m²K"], "thermal"),
    "u_techo": (["W/m²K"], "thermal"),
    "t_ext": (["°C", "°F", "K"], "temperature"),
    "t_int": (["°C", "°F", "K"], "temperature"),
    "cop": (["COP"], "ratio"),
    "lambda": (["W/m·K"], "thermal"),
    "consumo_dia": (["Wh/day", "kWh/day"], "energy"),
    "hsp": (["h/day"], "time"),
    "autonomia": (["days"], "time"),
    "cantidad": (["ud"], "count"),
    "num_ladrillos": (["uds"], "count"),
    "numero": (["ud"], "count"),
    "num_escalones": (["steps"], "count"),
    "altura_total": (["m", "cm", "ft"], "length"),
    "manos": (["coats"], "count"),
    "rendimiento_m2_l": (["m²/L"], "yield"),
    "pasadas": (["passes"], "count"),
    "grano_inicial": (["grit"], "count"),
    "num_granos": (["grits"], "count"),
    "coste_eur": (["€", "$"], "currency"),
    "precio_dia_eur": (["€/day", "$/day"], "price"),
    "precio_m2_semana": (["€/m²/wk", "$/m²/wk"], "price"),
    "horas_dia": (["h/day"], "time"),
    "dias_obra": (["days"], "time"),
    "num_trabajadores": (["workers"], "count"),
    "tam_pieza_cm": (["cm", "m", "mm", "in"], "length"),
    "m2_por_caja": (["m²/box"], "area"),
    "ancho_junta_mm": (["mm", "cm"], "length"),
    "desperdicio_merma": (["%"], "ratio"),
}

fixed_count = 0
for calc in data["calculators"]:
    cid = calc["id"]
    for inp in calc.get("inputs", []):
        iid = inp.get("id", "")
        unit = inp.get("unit", "")
        if not unit:
            continue
        if inp.get("unit_options") or inp.get("unit_category"):
            continue
        # Check ID override first
        if iid in ID_UNIT_MAP:
            opts, cat = ID_UNIT_MAP[iid]
            inp["unit_options"] = opts
            inp["unit_category"] = cat
            fixed_count += 1
            continue
        # Check unit mapping
        if unit in UNIT_MAP:
            opts, cat = UNIT_MAP[unit]
            inp["unit_options"] = opts
            inp["unit_category"] = cat
            fixed_count += 1
            continue
        # Special handling for compound units
        if unit == "kg/m³":
            inp["unit_options"] = ["kg/m³", "g/cm³", "lb/ft³"]
            inp["unit_category"] = "density"
            fixed_count += 1

with open(CALCS_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Fixed {fixed_count} inputs across original calculators.")
