#!/usr/bin/env python3
"""
Fix CTR Issues - Update meta descriptions for zero-CTR queries
Based on GSC data analysis
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
I18N_DIR = ROOT / "src" / "i18n"
CONTENT_DIR = ROOT / "src" / "content"

# Zero-CTR queries from GSC that need meta description fixes
# Format: (query_pattern, calc_id, new_seo_title, new_seo_description)
FIXES = {
    # TILE CALCULATOR - 46 impressions, pos 83, 0% CTR
    "en": {
        "027": {
            "seo_title": "Tile Calculator – Calculate Tiles Needed for Floor/Wall",
            "seo_desc": "Free tile calculator: calculate exactly how many tiles you need for floors, walls, or showers. Includes waste factor. Get instant results in m² or sq ft."
        },
        "wall-tile": {
            "seo_title": "Wall Tile Calculator – Bathroom & Kitchen Tiling",
            "seo_desc": "Calculate wall tiles for bathroom, kitchen or shower. Enter wall dimensions and tile size. Includes adhesive and grout estimates. Free online tool."
        }
    },
    # COP/EER CALCULATOR - 157 impressions, pos 45, 0% CTR
    "en": {
        "057": {
            "seo_title": "COP & EER Calculator – HVAC Efficiency Calculator",
            "seo_desc": "Calculate COP (Coefficient of Performance) and EER (Energy Efficiency Ratio) for HVAC systems. Convert EER to COP instantly. Free HVAC efficiency tool."
        }
    },
    # BMR CALCULATOR - 128 impressions, pos 5.94, 0% CTR (already page 1!)
    "en": {
        "427": {
            "seo_title": "BMR Calculator – Mifflin-St Jeor Equation (Accurate)",
            "seo_desc": "Calculate your Basal Metabolic Rate using the Mifflin-St Jeor equation. Most accurate BMR formula for weight loss or muscle gain. Free calculator."
        }
    },
    # CONCRETE BLOCK CALCULATOR - 59 impressions, pos 69
    "en": {
        "006": {
            "seo_title": "Concrete Block Calculator – CMU Quantity Calculator",
            "seo_desc": "Calculate how many concrete blocks (CMU) you need for walls. Enter wall dimensions and block size. Includes mortar and waste factor. Free tool."
        }
    },
    # ESPANOL - Pladur calculator (already has clicks, improve further)
    "es": {
        "014": {
            "seo_title": "Calculadora de Pladur – Materiales para Tabiques",
            "seo_desc": "Calcula los materiales de pladur necesarios para tabiques y falsos techos. Incluye placas, perfiles, tornillos y aislante. Herramienta gratuita."
        },
        "059": {
            "seo_title": "Calculadora de Rejillas y Difusores – HVAC",
            "seo_desc": "Dimensiona rejillas y difusores de aire acondicionado. Calcula el número necesario según el caudal de aire y tamaño de la habitación."
        },
        "008": {
            "seo_title": "Calculadora de Losa de Hormigón – Cimentación",
            "seo_desc": "Calcula el hormigón y acero necesario para losas de cimentación. Incluye encofrado y mallazo. Resultados en m³ y kg. Herramienta gratuita."
        }
    }
}

# Load and update i18n files
for lang, fixes in FIXES.items():
    i18n_file = I18N_DIR / f"{lang}.json"
    if not i18n_file.exists():
        print(f"[SKIP] {i18n_file} not found")
        continue
    
    with open(i18n_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    for calc_id, updates in fixes.items():
        # Try to find the calculator in i18n
        if calc_id in data.get('calculators', {}):
            calc = data['calculators'][calc_id]
            if 'seo_title' in updates:
                calc['seo_title'] = updates['seo_title']
                updated += 1
            if 'seo_desc' in updates:
                calc['seo_description'] = updates['seo_desc']
                calc['seo_desc'] = updates['seo_desc']  # Also update alias
                updated += 1
        else:
            # Try to find by slug match
            found = False
            for cid, calc in data.get('calculators', {}).items():
                if calc_id.lower() in cid.lower() or calc_id.lower() in calc.get('name', '').lower():
                    if 'seo_title' in updates:
                        calc['seo_title'] = updates['seo_title']
                        updated += 1
                    if 'seo_desc' in updates:
                        calc['seo_description'] = updates['seo_desc']
                        calc['seo_desc'] = updates['seo_desc']
                        updated += 1
                    found = True
                    break
            if not found:
                print(f"  [WARN] Calc {calc_id} not found in {lang}.json")
    
    if updated > 0:
        with open(i18n_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] {lang}.json: Updated {updated} fields")
    else:
        print(f"[WARN] {lang}.json: No updates made")

print("\n[INFO] Run build to apply changes: python scripts/generate_calctowork.py")
