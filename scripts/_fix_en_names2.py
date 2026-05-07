"""Fix MORE English names based on actual function."""
import json, glob

FIXES = {
    # Construction - shifted
    "013": "Concrete Beam Calculator",
    "016": "Spray Render Calculator",
    "018": "Plaster & Render Calculator",
    "020": "Tile Roof Calculator",
    "023": "Floating Laminate Floor Calculator",
    "024": "Wood Parquet Calculator",
    "035": "Water Heater Calculator",
    "037": "Aluminum Radiator Calculator",
    "040": "Water Service Connection Calculator",
    "042": "Floor Drain & Trap Calculator",
    "045": "Lumen Lighting Calculator",
    "046": "Light Points per Room Calculator",
    "049": "Battery Storage Calculator",
    "050": "Three-Phase Power Calculator",
    "052": "Monthly Electricity Cost Calculator",
    "053": "Air Conditioner BTU Calculator",
    "056": "Heat Pump (Aerothermal) Calculator",
    "058": "Duct Sizing Calculator",
    "059": "Grille & Diffuser Calculator",
    "061": "Aluminum/PVC Window Calculator",
    "064": "Wooden Staircase Calculator",
    "067": "Metal Door Hardware Calculator",
    "069": "Wall Paint Calculator",
    "071": "Synthetic Enamel Calculator",
    "075": "Primer & Sealer Calculator",
    "078": "Renovation Budget Calculator",
    "079": "Hourly Rate Calculator",
    "083": "Travel Allowance Calculator",
    "084": "Container Rental Calculator",
    "085": "Scaffolding Rental Calculator",
    "087": "Liability Insurance Calculator",
    "088": "PPE Equipment Calculator",
    "089": "Site Signage Calculator",
    "090": "Daily Productivity Calculator",
    "096": "Break-Even Point Calculator",
    "097": "Site Water Calculator",
    "101": "Pool Volume Calculator",
    "102": "Garden Soil Calculator",
    "103": "Fence Posts Calculator",
    "110": "Absolute Value Calculator",
    "111": "Arithmetic Series Sum",
    "112": "Geometric Series Sum",
    "113": "Complex Number Modulus",
    "114": "2x2 Matrix Determinant",
    "118": "Quadratic Derivative",
    "120": "Projectile Motion Calculator",
    "121": "Centripetal Force Calculator",
    "125": "Wave Speed Calculator",
    "129": "Fluid Pressure Calculator",
    "136": "Standard Deviation Calculator",
    "142": "Snell's Law Calculator",
    "145": "Thermal Expansion Calculator",
    "149": "Ideal Gas Law Calculator",
    "201": "Percentage Change Calculator",
    "213": "Cylinder Volume Calculator",
    "214": "Powers & Exponents Calculator",
}

fixed = 0
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    if cid in FIXES:
        old_name = d.get('i18n',{}).get('en',{}).get('name','')
        new_name = FIXES[cid]
        if old_name != new_name:
            d['i18n']['en']['name'] = new_name
            with open(fp,'w',encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                f.write('\n')
            fixed += 1
            print(f'  {cid}: "{old_name[:50]}" -> "{new_name}"')

print(f'\nFixed {fixed} more English names')
