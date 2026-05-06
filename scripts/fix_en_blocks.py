#!/usr/bin/env python3
"""Fix ALL remaining English content across all blocks."""

import json, os, glob, re

CALC_DIR = r"C:\Microsaas\obra\src\calculators"

def build_fixes():
    """Generate English fixes from Spanish content with proper translation."""
    fixes = {}
    
    # ─────────────────────────────────────────────────────────────────
    # Block 2 — mamposteria (Masonry & Walls) — 13 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "011": {  # ladrillo-hueco.json
            "name": "Hollow Brick Calculator",
            "description": "Calculate the number of hollow bricks and mortar needed for walls and partitions. Enter wall dimensions and brick size for accurate quantity estimates.",
            "seo_title": "Hollow Brick Calculator — Quantity & Mortar | CalcToWork",
            "seo_description": "Calculate hollow bricks and mortar for walls. Enter wall dimensions and brick size. Get exact quantities with waste factor. Free masonry calculator.",
            "inputs": {"largo": "Wall length (m)", "altura": "Wall height (m)", "largo_bloque": "Brick length (cm)", "ancho_bloque": "Brick width (cm)", "alto_bloque": "Brick height (cm)"},
            "outputs": {"bloques": "Bricks needed", "mortero_m3": "Mortar (m³)", "cemento_sacos": "Cement bags (50 kg)", "arena_m3": "Sand (m³)"},
            "steps": ["Calculate wall area: length × height", "Calculate bricks per m² based on brick size plus mortar joint", "Multiply by wall area for total bricks", "Add waste factor (5–10%)", "Calculate mortar from brick count and joint thickness"],
            "mistakes": ["Using face dimensions without adding mortar joint thickness (typically 1 cm)", "Ordering too few bricks — add 5% for cuts and breakage", "Confusing hollow bricks with solid bricks — different mortar requirements"],
        },
        "012": {  # ladrillo-cara-vista.json
            "name": "Face Brick Calculator",
            "description": "Calculate the number of face bricks and mortar needed for exterior visible brickwork. Enter wall dimensions for accurate facing brick estimates.",
            "seo_title": "Face Brick Calculator — Quantity & Mortar | CalcToWork",
            "seo_description": "Calculate face bricks and mortar for visible exterior brick walls. Enter wall area and brick size. Get quantities with waste factor. Free masonry calculator.",
        },
        "013": {  # bloque-hormigon.json
            "name": "Concrete Block Calculator",
            "description": "Calculate the number of concrete blocks and mortar needed for block walls. Enter wall dimensions and block size for accurate quantity and material estimates.",
            "seo_title": "Concrete Block Calculator — Quantity & Mortar | CalcToWork",
            "seo_description": "Calculate concrete blocks, mortar, cement and sand for block walls. Enter wall dimensions. Get exact quantities with waste factor. Free construction calculator.",
        },
        "014": {  # mamposteria-piedra.json
            "name": "Stone Masonry Calculator",
            "description": "Calculate the stones and mortar needed for rubble or dressed stone walls. Enter wall dimensions for stone quantity and mortar volume estimates.",
            "seo_title": "Stone Masonry Calculator — Stones & Mortar | CalcToWork",
            "seo_description": "Calculate stone quantity and mortar volume for stone masonry walls. Enter wall dimensions. Includes waste factor for irregular stones. Free calculator.",
        },
        "015": {  # aislamiento-termico.json
            "name": "Thermal Insulation Calculator",
            "description": "Calculate the insulation panels or rolls needed for walls, roofs, and floors. Enter surface area and insulation dimensions for accurate material estimates.",
            "seo_title": "Thermal Insulation Calculator — Panels & Rolls | CalcToWork",
            "seo_description": "Calculate insulation panels, rolls and area for walls, roofs or floors. Enter dimensions and panel size. Free calculator with waste factor for cutting.",
        },
        "016": {  # tabique-pladur.json
            "name": "Drywall Partition Calculator",
            "description": "Calculate the drywall sheets, studs, screws, and joint compound needed for interior partition walls. Enter wall dimensions for accurate material takeoffs.",
            "seo_title": "Drywall Partition Calculator — Sheets & Studs | CalcToWork",
            "seo_description": "Calculate drywall sheets, metal studs, screws and joint compound for partitions. Enter wall dimensions. Free construction calculator with waste factor.",
        },
        "017": {  # enfoscado-guarnecido.json
            "name": "Plaster & Render Calculator",
            "description": "Calculate the plaster, cement, and sand needed for wall rendering and plastering. Enter wall area for accurate material estimates with waste factor.",
            "seo_title": "Plaster Render Calculator — Materials | CalcToWork",
            "seo_description": "Calculate plaster, cement and sand for wall rendering. Enter wall area and coat thickness. Get material quantities. Free finishing calculator.",
        },
        "018": {  # revoco-proyectado.json
            "name": "Spray Render Calculator",
            "description": "Calculate the materials needed for spray-applied render or plaster. Enter wall area, coat thickness, and spray efficiency for accurate estimates.",
            "seo_title": "Spray Render Calculator — Materials | CalcToWork",
            "seo_description": "Calculate spray render materials including cement, sand and additives. Enter wall area and thickness. Free plastering calculator with overspray factor.",
        },
        "020": {  # factor-merma-material.json
            "name": "Material Waste Factor Calculator",
            "description": "Calculate the total material needed including waste allowance. Enter base quantity and waste percentage for accurate ordering quantities.",
            "seo_title": "Material Waste Calculator — Order Quantity | CalcToWork",
            "seo_description": "Calculate total materials needed with waste factor. Enter base quantity and waste percentage. Avoid under-ordering. Free construction calculator.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 3 — pavimentos (Flooring & Tiling) — 14 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "021": {  # solado-ceramico.json
            "name": "Ceramic Floor Tile Calculator",
            "description": "Calculate the number of ceramic tiles and adhesive needed for flooring. Enter floor dimensions and tile size for accurate estimates with cutting waste.",
            "seo_title": "Ceramic Tile Calculator — Quantity & Adhesive | CalcToWork",
            "seo_description": "Calculate ceramic floor tiles, adhesive and grout needed. Enter floor dimensions and tile size. Free tiling calculator with cutting waste factor.",
        },
        "022": {  # porcelanico.json
            "name": "Porcelain Tile Calculator",
            "description": "Calculate porcelain tiles, adhesive, and grout for indoor or outdoor tiling. Enter area dimensions and tile size for accurate quantity estimates.",
            "seo_title": "Porcelain Tile Calculator — Quantity & Materials | CalcToWork",
            "seo_description": "Calculate porcelain tiles, thin-set adhesive and grout. Enter room dimensions. Free tiling calculator with waste for cuts and breakage.",
        },
        "023": {  # mosaico.json
            "name": "Mosaic Tile Calculator",
            "description": "Calculate the number of mosaic tile sheets and materials needed. Enter area dimensions and sheet size for accurate estimates for walls or floors.",
            "seo_title": "Mosaic Tile Calculator — Sheets & Adhesive | CalcToWork",
            "seo_description": "Calculate mosaic tile sheets, adhesive and grout. Enter area dimensions. Free tiling calculator with waste for intricate patterns.",
        },
        "024": {  # laminado-flotante.json
            "name": "Laminate Flooring Calculator",
            "description": "Calculate laminate floor planks and underlayment needed. Enter room dimensions and plank size for accurate quantities with expansion gap allowance.",
            "seo_title": "Laminate Flooring Calculator — Planks & Underlay | CalcToWork",
            "seo_description": "Calculate laminate floor planks, underlayment and trim. Enter room dimensions. Free flooring calculator with 10% cutting waste factor.",
        },
        "025": {  # parquet-madera.json
            "name": "Hardwood Flooring Calculator",
            "description": "Calculate hardwood flooring planks, adhesive, and finish needed. Enter room dimensions and plank size for accurate hardwood flooring estimates.",
            "seo_title": "Hardwood Flooring Calculator — Planks | CalcToWork",
            "seo_description": "Calculate hardwood floor planks and materials. Enter room dimensions and plank size. Free flooring calculator with waste for cuts and patterns.",
        },
        "026": {  # terrazo.json
            "name": "Terrazzo Floor Calculator",
            "description": "Calculate terrazzo materials including aggregate, cement, and pigments. Enter floor area and thickness for accurate terrazzo flooring estimates.",
            "seo_title": "Terrazzo Calculator — Materials & Aggregate | CalcToWork",
            "seo_description": "Calculate terrazzo flooring materials — marble chips, cement, pigments. Enter floor area and thickness. Free terrazzo calculator.",
        },
        "027": {  # adhesivo-ceramico.json
            "name": "Tile Adhesive Calculator",
            "description": "Calculate the amount of tile adhesive or thin-set mortar needed. Enter tile area and trowel notch size for accurate adhesive estimates.",
            "seo_title": "Tile Adhesive Calculator — Thin-Set Quantity | CalcToWork",
            "seo_description": "Calculate tile adhesive or thin-set mortar quantity. Enter coverage area and trowel size. Free tiling calculator.",
        },
        "028": {  # lechada-junta.json
            "name": "Tile Grout Calculator",
            "description": "Calculate the amount of grout needed for tile joints. Enter tile dimensions, joint width, and area for accurate grout quantity estimates.",
            "seo_title": "Grout Calculator — Tile Joint Quantity | CalcToWork",
            "seo_description": "Calculate grout quantity for ceramic, porcelain or mosaic tile joints. Enter tile size, joint width and area. Free tiling calculator.",
        },
        "030": {  # marmol-granito.json
            "name": "Marble & Granite Calculator",
            "description": "Calculate marble or granite slabs, adhesive, and sealant needed for countertops and flooring. Enter area dimensions for accurate estimates.",
            "seo_title": "Marble Granite Calculator — Slabs & Materials | CalcToWork",
            "seo_description": "Calculate marble or granite slabs for countertops and floors. Enter dimensions. Free stone calculator with waste for veining matching.",
        },
        "031": {  # azulejo-pared.json
            "name": "Wall Tile Calculator",
            "description": "Calculate wall tiles, adhesive, and trim needed for bathroom or kitchen walls. Enter wall dimensions and tile size for accurate estimates.",
            "seo_title": "Wall Tile Calculator — Quantity & Materials | CalcToWork",
            "seo_description": "Calculate wall tiles for bathrooms, kitchens and splashbacks. Enter wall dimensions. Free tiling calculator with cutting waste factor.",
        },
        "033": {  # acabado-texturado.json
            "name": "Textured Coating Calculator",
            "description": "Calculate textured wall coating materials needed. Enter wall area and desired texture thickness for accurate product quantity estimates.",
            "seo_title": "Textured Coating Calculator — Materials | CalcToWork",
            "seo_description": "Calculate textured wall coating quantity. Enter wall area and texture thickness. Free finishing calculator for decorative coatings.",
        },
        "036": {  # vidrio-cristal.json
            "name": "Glass Panel Calculator",
            "description": "Calculate glass panel dimensions, weight, and cost for windows, doors, or partitions. Enter dimensions and glass type for accurate estimates.",
            "seo_title": "Glass Panel Calculator — Size & Weight | CalcToWork",
            "seo_description": "Calculate glass panel weight, area and cost. Enter dimensions and glass thickness. Free glazing calculator for windows and doors.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 4 — fontaneria (Plumbing & Water) — 14 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "038": {  # tuberia-cobre-pex.json
            "name": "Copper & PEX Pipe Calculator",
            "description": "Calculate the lengths, fittings, and flow capacity for copper or PEX plumbing pipes. Enter pipe run details for accurate material estimates.",
            "seo_title": "Pipe Calculator — Copper & PEX Materials | CalcToWork",
            "seo_description": "Calculate copper or PEX pipe lengths, fittings and flow capacity. Enter pipe run details. Free plumbing calculator for residential projects.",
        },
        "039": {  # tuberia-pvc-saneamiento.json
            "name": "PVC Drainage Pipe Calculator",
            "description": "Calculate PVC pipe lengths, fittings, and slope requirements for drainage and sewer lines. Enter pipe run details for accurate estimates.",
            "seo_title": "PVC Drainage Calculator — Pipe & Fittings | CalcToWork",
            "seo_description": "Calculate PVC drainage pipe lengths, fittings and slope. Enter run details. Free plumbing calculator for sanitary sewer systems.",
        },
        "040": {  # acometida-agua.json
            "name": "Water Service Connection Calculator",
            "description": "Calculate pipe diameter, trench depth, and materials for water service connections from the main to the building. Enter distance and flow requirements.",
            "seo_title": "Water Connection Calculator — Pipe & Trench | CalcToWork",
            "seo_description": "Calculate water service connection pipe size, trench dimensions and materials. Enter distance from main. Free plumbing calculator.",
        },
        "041": {  # presion-agua.json
            "name": "Water Pressure Calculator",
            "description": "Calculate static and dynamic water pressure in pipes. Enter height, flow rate, and pipe diameter to determine available pressure.",
            "seo_title": "Water Pressure Calculator — Static & Dynamic | CalcToWork",
            "seo_description": "Calculate water pressure in plumbing systems. Enter height, flow and pipe size. Free hydraulic calculator for residential water systems.",
        },
        "042": {  # calentador-agua.json
            "name": "Water Heater Sizing Calculator",
            "description": "Calculate the right water heater capacity for your home. Enter number of occupants and usage patterns for accurate water heater sizing.",
            "seo_title": "Water Heater Calculator — Capacity & Type | CalcToWork",
            "seo_description": "Calculate water heater capacity needed. Enter household size and usage. Free plumbing calculator for electric, gas or tankless heaters.",
        },
        "043": {  # deposito-agua.json
            "name": "Water Tank Capacity Calculator",
            "description": "Calculate water storage tank volume needed. Enter daily consumption and reserve days for accurate tank sizing for homes or buildings.",
            "seo_title": "Water Tank Calculator — Volume & Capacity | CalcToWork",
            "seo_description": "Calculate water tank volume and dimensions. Enter daily consumption. Free calculator for storage tanks and cisterns.",
        },
        "045": {  # riego-goteo.json
            "name": "Drip Irrigation Calculator",
            "description": "Calculate drip irrigation system components — pipe length, emitters, and flow rate. Enter garden dimensions and plant spacing.",
            "seo_title": "Drip Irrigation Calculator — Emitters & Flow | CalcToWork",
            "seo_description": "Calculate drip irrigation pipe, emitters and flow rate. Enter garden area and plant spacing. Free irrigation design calculator.",
        },
        "047": {  # sifon-sumidero.json
            "name": "Drain Trap & Sump Calculator",
            "description": "Calculate drain trap dimensions and sump pit volume for plumbing drainage. Enter pipe diameter and fixture units for proper sizing.",
            "seo_title": "Drain Trap Calculator — Sizing & Volume | CalcToWork",
            "seo_description": "Calculate P-trap, drain trap and sump pit dimensions. Enter pipe diameter. Free plumbing drainage calculator.",
        },
        "048": {  # depuradora-piscina.json
            "name": "Pool Filter & Pump Calculator",
            "description": "Calculate pool pump flow rate and filter size needed. Enter pool dimensions and turnover time for proper pool equipment sizing.",
            "seo_title": "Pool Pump Calculator — Flow & Filter Size | CalcToWork",
            "seo_description": "Calculate swimming pool pump flow rate and filter capacity. Enter pool volume. Free pool equipment sizing calculator.",
        },
        "049": {  # volumen-piscina.json
            "name": "Swimming Pool Volume Calculator",
            "description": "Calculate the water volume of rectangular, circular, or irregular pools. Enter pool dimensions for accurate volume in liters and gallons.",
            "seo_title": "Pool Volume Calculator — Liters & Gallons | CalcToWork",
            "seo_description": "Calculate swimming pool water volume. Enter pool shape and dimensions. Free calculator for chemical dosing and pump sizing.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 5 — electricidad (Electrical) — 10 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "050": {  # cable-electrico-seccion.json
            "name": "Electrical Cable Size Calculator",
            "description": "Calculate the correct cable cross-section for electrical installations. Enter power, voltage, and cable length for proper wire sizing.",
            "seo_title": "Cable Size Calculator — Wire Cross-Section | CalcToWork",
            "seo_description": "Calculate electrical cable cross-section. Enter power, voltage and length. Free electrical calculator for safe wire sizing per code.",
        },
        "051": {  # caida-tension.json
            "name": "Voltage Drop Calculator",
            "description": "Calculate voltage drop in electrical cables. Enter cable length, current, and conductor size to verify voltage drop stays within limits.",
            "seo_title": "Voltage Drop Calculator — Cable Loss | CalcToWork",
            "seo_description": "Calculate voltage drop percentage in electrical cables. Enter length, current and wire size. Free electrical calculator for code compliance.",
        },
        "053": {  # aire-acondicionado-btu.json
            "name": "Air Conditioner BTU Calculator",
            "description": "Calculate the BTU cooling capacity needed for your room. Enter room dimensions, insulation, and sun exposure for accurate AC sizing.",
            "seo_title": "AC BTU Calculator — Cooling Capacity | CalcToWork",
            "seo_description": "Calculate air conditioner BTU capacity for your room. Enter dimensions and conditions. Free HVAC calculator for proper AC sizing.",
        },
        "055": {  # cuadro-electrico.json
            "name": "Electrical Panel Load Calculator",
            "description": "Calculate the total electrical load on a distribution panel. Enter circuit loads to verify panel capacity and prevent overloads.",
            "seo_title": "Electrical Panel Calculator — Load Balance | CalcToWork",
            "seo_description": "Calculate electrical panel load and balance. Enter circuit loads and breaker ratings. Free electrical calculator for safe distribution.",
        },
        "058": {  # puesta-tierra.json
            "name": "Grounding Rod Calculator",
            "description": "Calculate grounding system requirements — rod depth, number of rods, and conductor size. Enter soil resistivity for proper earth grounding.",
            "seo_title": "Grounding Calculator — Rods & Resistance | CalcToWork",
            "seo_description": "Calculate earth grounding rod requirements. Enter soil resistivity. Free electrical calculator for proper earthing installation.",
        },
        "059": {  # instalacion-solar.json
            "name": "Solar Panel Installation Calculator",
            "description": "Calculate solar panel quantity, inverter size, and battery capacity needed. Enter daily consumption and peak sun hours for system sizing.",
            "seo_title": "Solar Panel Calculator — System Sizing | CalcToWork",
            "seo_description": "Calculate solar PV system size — panels, inverter and batteries. Enter daily consumption. Free solar calculator for off-grid or grid-tie.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 6 — climatizacion (HVAC & Climate) — 9 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "061": {  # caldera-gas.json
            "name": "Gas Boiler Sizing Calculator",
            "description": "Calculate the right gas boiler capacity for your home. Enter heated area, insulation level, and hot water demand for accurate sizing.",
            "seo_title": "Gas Boiler Calculator — kW Capacity | CalcToWork",
            "seo_description": "Calculate gas boiler kW capacity needed. Enter heated area and insulation. Free heating calculator for combi or system boilers.",
        },
        "062": {  # radiador-aluminio.json
            "name": "Radiator Heat Output Calculator",
            "description": "Calculate the heat output (BTU or Watts) needed from radiators per room. Enter room dimensions and insulation for accurate radiator sizing.",
            "seo_title": "Radiator Calculator — BTU Heat Output | CalcToWork",
            "seo_description": "Calculate radiator heat output per room in BTU or Watts. Enter room size and insulation. Free heating calculator for radiator sizing.",
        },
        "063": {  # suelo-radiante.json
            "name": "Underfloor Heating Calculator",
            "description": "Calculate underfloor heating pipe length, spacing, and heat output. Enter room dimensions and desired temperature for system design.",
            "seo_title": "Underfloor Heating Calculator — Pipe & Output | CalcToWork",
            "seo_description": "Calculate underfloor heating pipe length and spacing. Enter room dimensions. Free heating calculator for wet UFH systems.",
        },
        "064": {  # conductos-aire.json
            "name": "HVAC Duct Sizing Calculator",
            "description": "Calculate HVAC duct dimensions and airflow. Enter required CFM or room dimensions for proper duct sizing and air distribution.",
            "seo_title": "HVAC Duct Calculator — Airflow & Size | CalcToWork",
            "seo_description": "Calculate HVAC duct dimensions and air velocity. Enter airflow requirements. Free ventilation calculator for supply and return ducts.",
        },
        "065": {  # rejillas-difusores.json
            "name": "Air Diffuser & Grille Calculator",
            "description": "Calculate the number and size of HVAC diffusers and grilles needed per room. Enter airflow and room dimensions for proper air distribution.",
            "seo_title": "HVAC Diffuser Calculator — Grilles & Flow | CalcToWork",
            "seo_description": "Calculate air diffusers and grilles needed per room. Enter airflow and dimensions. Free ventilation calculator for balanced distribution.",
        },
        "066": {  # ventilacion-mecanica.json
            "name": "Mechanical Ventilation Calculator",
            "description": "Calculate ventilation air changes and extract fan capacity. Enter room volume and occupancy for proper mechanical ventilation sizing.",
            "seo_title": "Ventilation Calculator — Air Changes & Extract | CalcToWork",
            "seo_description": "Calculate mechanical ventilation rate and fan capacity. Enter room volume and use type. Free ventilation calculator for building code compliance.",
        },
        "068": {  # dimensionado-conducto.json
            "name": "Ductwork Dimensioning Calculator",
            "description": "Calculate rectangular or circular duct dimensions from airflow requirements. Enter CFM and velocity limits for proper duct sizing.",
            "seo_title": "Duct Dimension Calculator — Circular & Rect | CalcToWork",
            "seo_description": "Calculate duct dimensions for rectangular or circular ductwork. Enter airflow. Free HVAC calculator for supply, return and exhaust.",
        },
        "069": {  # bomba-calor-aerotermia.json
            "name": "Heat Pump Sizing Calculator",
            "description": "Calculate the heat pump capacity (air-source or ground-source) needed for heating and cooling. Enter building heat loss for proper sizing.",
            "seo_title": "Heat Pump Calculator — Capacity & COP | CalcToWork",
            "seo_description": "Calculate heat pump capacity and COP efficiency. Enter building characteristics. Free calculator for air-source and geothermal systems.",
        },
        "070": {  # carga-gas-refrigerante.json
            "name": "Refrigerant Charge Calculator",
            "description": "Calculate the refrigerant charge needed for HVAC systems. Enter pipe length, diameter, and system type for proper refrigerant quantity.",
            "seo_title": "Refrigerant Charge Calculator — HVAC | CalcToWork",
            "seo_description": "Calculate refrigerant charge for split systems, heat pumps and chillers. Enter pipe specs. Free HVAC calculator for installation.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 7 — carpinteria (Carpentry & Joinery) — 12 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "072": {  # puertas-paso.json
            "name": "Interior Door Calculator",
            "description": "Calculate the materials needed for interior door installation — frame, hinges, handles, and trim. Enter door dimensions for accurate estimates.",
            "seo_title": "Interior Door Calculator — Frame & Hardware | CalcToWork",
            "seo_description": "Calculate interior door frame, hinges, handle and trim materials. Enter door dimensions. Free carpentry calculator for door installation.",
        },
        "073": {  # puertas-correderas.json
            "name": "Sliding Door Calculator",
            "description": "Calculate materials for sliding door installation — track, rollers, panels, and hardware. Enter opening dimensions for accurate estimates.",
            "seo_title": "Sliding Door Calculator — Track & Hardware | CalcToWork",
            "seo_description": "Calculate sliding door track, rollers and panel materials. Enter opening dimensions. Free carpentry calculator for sliding systems.",
        },
        "074": {  # acabado-texturado.json -> already done as 033
        },
        "075": {  # ventanas-aluminio-pvc.json
            "name": "Window Frame Calculator",
            "description": "Calculate aluminum or PVC window frame materials and glass area. Enter window dimensions for accurate material and cost estimates.",
            "seo_title": "Window Frame Calculator — Aluminum & PVC | CalcToWork",
            "seo_description": "Calculate aluminum or PVC window frame profiles and glass. Enter window dimensions. Free carpentry calculator for window fabrication.",
        },
        "076": {  # escalera-madera.json
            "name": "Wooden Staircase Calculator",
            "description": "Calculate the materials for a wooden staircase — treads, risers, stringers, and handrails. Enter floor-to-floor height for accurate stair design.",
            "seo_title": "Staircase Calculator — Treads & Stringers | CalcToWork",
            "seo_description": "Calculate wooden staircase treads, risers, stringers and handrail length. Enter height. Free carpentry calculator for stair building.",
        },
        "077": {  # barandilla-metalica.json
            "name": "Metal Railing Calculator",
            "description": "Calculate the materials for metal railings and balustrades — posts, rails, balusters, and fasteners. Enter railing length for accurate estimates.",
            "seo_title": "Metal Railing Calculator — Posts & Balusters | CalcToWork",
            "seo_description": "Calculate metal railing posts, rails, balusters and hardware. Enter railing length. Free carpentry calculator for balcony and stair railings.",
        },
        "078": {  # cerrajeria-puerta.json
            "name": "Door Hardware Calculator",
            "description": "Calculate door lock, handle, hinge, and closer specifications. Enter door type and usage for proper hardware selection.",
            "seo_title": "Door Hardware Calculator — Locks & Hinges | CalcToWork",
            "seo_description": "Calculate door hardware requirements — locks, handles, hinges and closers. Enter door type. Free hardware calculator for doorsets.",
        },
        "079": {  # estructuras-metalicas.json
            "name": "Steel Structure Calculator",
            "description": "Calculate steel profiles, plates, and fasteners for metal structures. Enter dimensions and load requirements for structural steel estimates.",
            "seo_title": "Steel Structure Calculator — Profiles & Plates | CalcToWork",
            "seo_description": "Calculate steel structural profiles, plates and connections. Enter dimensions. Free calculator for steel frame buildings and structures.",
        },
    })
    
    # ─────────────────────────────────────────────────────────────────
    # Block 8 — pintura (Paint & Coatings) — 12 calcs
    # ─────────────────────────────────────────────────────────────────
    fixes.update({
        "083": {  # pintura-plastica-paredes.json
            "name": "Interior Wall Paint Calculator",
            "description": "Calculate liters of paint needed for interior walls. Enter wall dimensions, number of coats, and paint coverage for accurate estimates.",
            "seo_title": "Wall Paint Calculator — Liters & Coats | CalcToWork",
            "seo_description": "Calculate paint quantity for interior walls. Enter wall area and coverage. Free painting calculator with multiple coat allowance.",
        },
        "084": {  # pintura-techo.json
            "name": "Ceiling Paint Calculator",
            "description": "Calculate paint needed for ceiling painting. Enter ceiling dimensions and paint coverage for accurate quantity estimates.",
            "seo_title": "Ceiling Paint Calculator — Liters Needed | CalcToWork",
            "seo_description": "Calculate paint quantity for ceilings. Enter ceiling area and coverage rate. Free painting calculator for interior ceiling projects.",
        },
        "086": {  # barniz-exterior.json
            "name": "Exterior Wood Varnish Calculator",
            "description": "Calculate varnish, stain, or wood treatment needed for exterior wood surfaces. Enter area, number of coats, and product coverage.",
            "seo_title": "Wood Varnish Calculator — Exterior | CalcToWork",
            "seo_description": "Calculate exterior wood varnish or stain quantity. Enter wood area and coats. Free calculator for deck, fence and siding treatment.",
        },
        "087": {  # esmalte-sintetico.json
            "name": "Enamel Paint Calculator",
            "description": "Calculate synthetic enamel paint needed for metal, wood, or trim surfaces. Enter surface area and coverage for accurate estimates.",
            "seo_title": "Enamel Paint Calculator — Metal & Wood | CalcToWork",
            "seo_description": "Calculate enamel paint quantity for metal, wood and trim. Enter surface area. Free painting calculator for doors, windows and radiators.",
        },
        "088": {  # imprimacion-sellador.json
            "name": "Primer & Sealer Calculator",
            "description": "Calculate primer or sealer needed before painting. Enter surface area, porosity, and coverage for accurate undercoat estimates.",
            "seo_title": "Primer Sealer Calculator — Undercoat | CalcToWork",
            "seo_description": "Calculate primer and sealer quantity. Enter surface area and type. Free painting calculator for surface preparation.",
        },
        "089": {  # masilla-filler.json
            "name": "Filler & Putty Calculator",
            "description": "Calculate wall filler, joint compound, or wood putty needed. Enter crack length, hole size, or joint length for accurate estimates.",
            "seo_title": "Wall Filler Calculator — Putty & Compound | CalcToWork",
            "seo_description": "Calculate wall filler, putty or joint compound. Enter crack and hole dimensions. Free DIY calculator for wall repair.",
        },
        "091": {  # papel-pintado.json
            "name": "Wallpaper Calculator",
            "description": "Calculate rolls of wallpaper needed for your room. Enter wall dimensions and wallpaper roll size for accurate quantities with pattern match.",
            "seo_title": "Wallpaper Calculator — Rolls Needed | CalcToWork",
            "seo_description": "Calculate wallpaper rolls needed per room. Enter wall dimensions and roll specs. Free calculator with pattern repeat and waste factor.",
        },
        "092": {  # lija-abrasivo.json
            "name": "Sandpaper & Abrasive Calculator",
            "description": "Calculate sandpaper sheets or discs needed for surface preparation. Enter surface area and grit sequence for accurate abrasive estimates.",
            "seo_title": "Sandpaper Calculator — Sheets & Grits | CalcToWork",
            "seo_description": "Calculate sandpaper sheets, discs and grits needed. Enter surface area. Free calculator for wood, metal and drywall sanding.",
        },
    })
    
    return fixes


def apply_fixes(fixes):
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
        name = os.path.basename(fp)
        if "bak" in fp or "monolithic" in fp or name == "calculators.json":
            continue

        with open(fp, "r", encoding="utf-8-sig") as f:
            calc = json.load(f)

        cid = calc.get("id", "")
        if cid not in fixes:
            continue

        fix = fixes[cid]
        en = calc.setdefault("i18n", {}).setdefault("en", {})

        changed = False
        for key, value in fix.items():
            if isinstance(value, str) and key in en and en[key] == value:
                continue
            if isinstance(value, (dict, list)) and key in en and en[key] == value:
                continue
            en[key] = value
            changed = True

        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                json.dump(calc, f, ensure_ascii=False, indent=2)
            updated += 1

    print(f"Updated {updated} English calculator files")


if __name__ == "__main__":
    fixes = build_fixes()
    print(f"Generated fixes for {len(fixes)} calculators")
    apply_fixes(fixes)
