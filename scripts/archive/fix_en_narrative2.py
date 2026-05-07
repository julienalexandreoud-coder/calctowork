#!/usr/bin/env python3
"""Fix English narrative — batch 2 covering blocks 2-9."""
import json, os, glob
CALC = r"C:\Microsaas\obra\src\calculators"
f = {}

def N(name, steps, mistakes, rc, fd, el, rh=None):
    d = {"name": name, "steps": steps, "mistakes": mistakes, "result_context": rc, "formula_display": fd, "example_label": el}
    if rh: d["range_hints"] = rh
    return d

# ── Block 2: mamposteria ──
f["011"] = N("Hollow Brick Calculator",
    ["Measure wall length and height to find total wall area","Subtract window and door openings from the total","Calculate bricks per square meter: 1 ÷ ((brick length + 1 cm joint) × (brick height + 1 cm joint))","Multiply net area by bricks per m², then add 5% for cuts and breakage","Estimate mortar volume from joint dimensions and brick count"],
    ["Forgetting to add the 1 cm mortar joint to brick dimensions — undercounts by about 15%","Ordering exactly the calculated quantity — always add 5% waste","Using the same mortar mix for hollow bricks as solid bricks"],
    "For a wall area of approximately {area} m², order about {bloques} hollow bricks and prepare {mortero_m3} m³ of mortar.", "Bricks = wall area ÷ (brick face + joint)²; Mortar = bricks × joint volume per brick", "Calculate hollow bricks for a standard interior partition wall")
f["012"] = N("Face Brick Calculator",
    ["Calculate the visible wall area (length × height)","Subtract all openings: windows, doors, vents","Face bricks per m²: 1 ÷ ((brick L + 1 cm) × (brick H + 1 cm))","Multiply by net area and add 5% for half-bricks at corners","Calculate mortar — facing brickwork uses thinner 8–10 mm joints"],
    ["Not accounting for color variation across batches — order all from the same lot","Forgetting half-bricks needed at corners, sills, and reveals","Using standard grey mortar that ruins the aesthetic of face brickwork"],
    "For a visible wall area of {area} m², you need approximately {bloques} face bricks and {mortero_m3} m³ of mortar.", "Bricks = visible area ÷ (brick + joint)² × 1.05", "Face brick estimate for an exterior feature wall")
f["013"] = N("Concrete Block Calculator",
    ["Calculate wall area from length and height","Each standard block covers roughly 0.08 m² (40×20 cm) plus joint","Divide wall area by block coverage for the base count","Add 5% for cuts around openings and corners","Calculate mortar: roughly 0.012 m³ per m² of block wall"],
    ["Forgetting that concrete blocks are heavier than bricks — check foundation load","Not accounting for bond beams and lintels over openings","Using the wrong block type — there are solid, hollow, and lightweight blocks"],
    "You need approximately {bloques} concrete blocks and {mortero_m3} m³ of mortar for this wall.", "Blocks = wall area ÷ block coverage rate; Mortar = wall area × 0.012 m³/m²", "Concrete block estimate for a standard wall")
f["014"] = N("Stone Masonry Calculator",
    ["Calculate the wall volume from length, height, and average thickness","Stone walls are about 60% stone and 40% mortar by volume","Calculate stone volume: total wall volume × 0.60","Calculate mortar volume: total wall volume × 0.40","Add 10–15% extra for irregular stone shapes"],
    ["Underestimating mortar volume — stone walls use much more mortar than brick","Not allowing for the irregular shape of rubble stone — needs extra stone","Forgetting that stone walls need deeper foundations due to weight"],
    "A stone masonry wall of approximately {volumen} m³ will require about {piedra_m3} m³ of stone and {mortero_m3} m³ of mortar.", "Stone = wall volume × 0.60; Mortar = wall volume × 0.40", "Stone quantity for a rubble stone garden wall")
f["016"] = N("Drywall Partition Calculator",
    ["Calculate wall area from length and height","Standard drywall sheets are 1.2 m × 2.4 m or 1.2 m × 3.0 m","Number of sheets: divide wall area by sheet area, round up","Studs needed: wall length in meters ÷ 0.40 m spacing, plus one per end","Screws: approximately 30 screws per sheet; joint compound: 0.5 kg per m²"],
    ["Not doubling the count for double-sided partitions — both faces need drywall","Forgetting corner beads, joint tape, and trim pieces","Using the wrong stud spacing — 40 cm for walls, 60 cm for ceilings"],
    "For a partition wall of {area} m², you need {placas} drywall sheets, {perfiles} metal studs, and {tornillos} screws.", "Sheets = total area ÷ sheet area; Studs = length ÷ 0.40 + 1", "Drywall estimate for a 4 m × 2.7 m partition wall")
f["017"] = N("Plaster Render Calculator",
    ["Calculate wall area: length × height for each wall","Determine total plaster thickness (typically 1.5–2 cm)","Volume of plaster: wall area × thickness","Cement: plaster volume ÷ mix ratio (typically 1:4 cement to sand)","Sand: cement volume × 4"],
    ["Applying plaster too thick in one coat — 1.5 cm maximum per coat","Not wetting the wall before applying — dry walls suck moisture from the plaster","Using the wrong sand grade — plaster sand should be fine, not coarse"],
    "You need approximately {cemento_sacos} cement bags and {arena_m3} m³ of sand to plaster {area} m² of wall.", "Plaster volume = area × thickness; Cement = volume ÷ 5; Sand = cement × 4", "Plaster estimate for a 30 m² wall at 2 cm thickness")
f["018"] = N("Spray Render Calculator",
    ["Calculate total wall area from all wall dimensions","Spray render is applied at 1–2 cm thickness","Base volume: wall area × thickness","Add 15–20% overspray loss for spray application","Calculate cement and sand from the mix ratio"],
    ["Not accounting for overspray — spray application loses 15–20% more than hand application","Applying on a dirty or dusty surface — causes poor adhesion","Using the same mix as hand-applied render — spray mixes need more water"],
    "With spray application, expect to use about {volumen} m³ of render including overspray allowance.", "Volume = wall area × thickness × 1.18 (overspray)", "Spray render quantity for a 100 m² wall surface")
f["020"] = N("Material Waste Factor Calculator",
    ["Enter the base quantity of material needed","Choose the appropriate waste percentage for your material type","Calculate: total quantity = base quantity × (1 + waste% / 100)","Use the total for ordering — this is the amount to buy","Typical waste factors: tiles 10%, bricks 5%, concrete 5–10%, paint 10–15%"],
    ["Using the same waste factor for all materials — different materials have very different waste rates","Applying waste factor after the calculation instead of before","Forgetting that waste factor applies to all materials, not just the primary one"],
    "With a {porcentaje}% waste factor, you need to order {total} units rather than the base {cantidad}.", "Total = base quantity × (1 + waste% ÷ 100)", "Calculate total order quantity for 100 bricks with 5% waste")
f["015"] = N("Thermal Insulation Calculator",
    ["Calculate surface area from length and width","Insulation panels are typically 1.2 m × 0.6 m or similar","Number of panels: total area ÷ panel area, rounded up","Add 5–10% for cutting around obstacles and odd shapes","For rolls: calculate linear meters from area and roll width"],
    ["Not accounting for thermal bridging around studs and joists","Using the wrong insulation thickness — check local building code requirements","Forgetting the vapor barrier on the warm side of the insulation"],
    "To insulate {area} m², you need approximately {paneles} insulation panels.", "Panels = area ÷ panel area × 1.05", "Insulation estimate for a 50 m² exterior wall")

# ── Block 3: pavimentos ──
f["021"] = N("Ceramic Floor Tile Calculator",
    ["Calculate floor area from room length and width","Tiles per m²: 1 ÷ ((tile length in m) × (tile width in m))","Multiply floor area by tiles per m² for the base count","Add 10% for cuts, breakage, and pattern matching","Calculate adhesive: approximately 3–5 kg per m² depending on trowel notch"],
    ["Not adding the 10% cutting waste — almost every room needs partial tiles at edges","Using the floor area without subtracting fixed cabinets — but not vanities","Forgetting to order matching edge trims and thresholds"],
    "For a {area} m² floor, order approximately {baldosas} ceramic tiles and {adhesivo_kg} kg of adhesive.", "Tiles = floor area ÷ (tile L × tile W) × 1.10", "Tile estimate for a 20 m² floor with 60×60 cm tiles")
f["022"] = N("Porcelain Tile Calculator",
    ["Calculate room area: length × width","Porcelain tiles per m²: 1 ÷ (tile size in m²)","Base quantity: room area × tiles per m²","Add 12–15% waste for porcelain — it's harder to cut than ceramic","Adhesive: use flexible thin-set, approximately 4–6 kg/m²"],
    ["Attempting to cut porcelain with a manual tile cutter — needs a wet saw","Not back-buttering large format tiles — causes hollow spots","Using the same grout width as ceramic — porcelain needs minimum 2–3 mm joints"],
    "For your {area} m² porcelain floor, order {baldosas} tiles and use flexible adhesive rated for porcelain.", "Tiles = area ÷ tile size × 1.12", "Porcelain tile estimate for a 15 m² bathroom floor")
f["023"] = N("Mosaic Tile Calculator",
    ["Mosaic sheets come in standard sizes, typically 30×30 cm","Calculate room area: length × width","Number of sheets: room area ÷ sheet area (0.09 m² for 30×30)","Add 10–15% waste — mosaics need more cuts around fixtures","Grout quantity is higher than standard tiles due to many small joints"],
    ["Not aligning sheet edges perfectly — mosaic pattern mismatches are very visible","Using white grout with dark mosaic — shows every imperfection","Applying too much adhesive — oozes through the mesh backing"],
    "You need approximately {hojas} mosaic sheets to cover {area} m², plus matching grout for the many small joints.", "Sheets = area ÷ sheet area × 1.12", "Mosaic tile estimate for a kitchen backsplash")
f["024"] = N("Laminate Flooring Calculator",
    ["Calculate room area from length and width","Each laminate plank covers about 0.2–0.3 m² (check pack specs)","Number of packs: room area ÷ pack coverage","Add 10% for cuts, stagger pattern, and damaged pieces","Include underlayment: same area as the room plus 5% overlap"],
    ["Not leaving expansion gap (8–12 mm) around the perimeter — floor will buckle","Forgetting the underlayment — essential for sound reduction and moisture barrier","Installing parallel to the longest wall — perpendicular looks better in narrow rooms"],
    "For a {area} m² room, you need approximately {cajas} packs of laminate flooring plus underlayment.", "Packs = area ÷ pack coverage × 1.10", "Laminate estimate for a 25 m² living room")
f["031"] = N("Wall Tile Calculator",
    ["Calculate each wall area separately: width × height","Add all wall areas together and subtract door/window openings","Tiles per m² based on tile dimensions","Add 10–15% waste for cuts around fixtures and corners","Calculate grout and adhesive quantities from total area"],
    ["Not starting with a level batten — tiles will slide on the first row","Forgetting that wall tiles need different adhesive than floor tiles","Not planning the layout — avoid thin slivers at edges"],
    "For {area} m² of wall tiling, purchase {baldosas} tiles plus suitable wall adhesive and grout.", "Tiles = total wall area ÷ tile area × 1.12", "Wall tile estimate for a 12 m² bathroom")
f["027"] = N("Tile Adhesive Calculator",
    ["Coverage depends on trowel notch size: 3 mm ≈ 1.5 kg/m², 6 mm ≈ 3 kg/m², 10 mm ≈ 5 kg/m²","Enter your total tile area","Calculate: adhesive needed = area × coverage rate per m²","Round up to the nearest full bag","Consider substrate: porous surfaces need more adhesive"],
    ["Using the wrong trowel size — large tiles need deeper notches for proper bed","Mixing too much adhesive at once — it skins over in 20–30 minutes","Not back-buttering tiles larger than 30×30 cm"],
    "For {area} m² of tiling, you need approximately {adhesivo_kg} kg of thin-set adhesive.", "Adhesive = area × coverage rate (kg/m²)", "Adhesive quantity for a 25 m² floor with 10 mm trowel")
f["028"] = N("Tile Grout Calculator",
    ["Calculate the total grout joint length from tile dimensions and area","Grout volume = joint width × joint depth × total joint length per m² × area","Adjust for tile thickness — deeper tiles need more grout","Add 10% for waste — grout is cheap but running out mid-job is frustrating","Account for grout type: epoxy grout covers less area than cement-based"],
    ["Starting grouting too soon — adhesive must cure 24 hours first","Mixing too much grout at once — it hardens in 20–30 minutes","Using unsanded grout in joints wider than 3 mm — it will crack"],
    "You need approximately {lechada_kg} kg of grout for the joints between your tiles.", "Grout = area × joint factor; Joint factor = (width+depth)/width × joint W × joint D / (tile L × tile W) × 1000", "Grout estimate for 25 m² of 60×60 cm tiles with 3 mm joints")
f["030"] = N("Marble & Granite Calculator",
    ["Calculate surface area requiring stone — countertop, floor, or wall","Standard slabs are approximately 3 m × 1.8 m but vary","Number of slabs: total area ÷ slab area, rounded up","Add 15–20% for vein matching, cutouts, and irregular shapes","Account for fabrication: sinks, edges, and backsplashes consume extra stone"],
    ["Not visiting the stone yard to select the specific slab — each one is unique","Forgetting cutouts for sinks and cooktops in the area calculation","Using standard grout on marble — acids in grout can etch the surface"],
    "Plan for approximately {losas} stone slabs to cover {area} m², including waste for vein matching and cutouts.", "Slabs = (area × 1.18) ÷ slab area, rounded up", "Marble estimate for a 4 m² kitchen countertop with cutouts")
f["033"] = N("Textured Coating Calculator",
    ["Calculate wall area: sum of all wall faces (length × height)","Choose texture thickness: fine = 1–2 mm, medium = 2–3 mm, coarse = 3–5 mm","Volume of coating: area × thickness in meters","Coverage: approximately 1.5–3 kg/m² depending on texture","Add 10% for overspray and touch-ups"],
    ["Not priming the surface first — textured coatings need a good base","Applying too thick — can crack as it dries","Not protecting adjacent surfaces from overspray during application"],
    "You need approximately {kg_total} kg of textured coating to cover {area} m² at the specified thickness.", "Coating kg = area × coverage rate × 1.10", "Textured coating quantity for 80 m² of wall area")
f["036"] = N("Glass Panel Calculator",
    ["Calculate glass area: length × width in meters","Glass weight: area × thickness in mm × 2.5 (density of glass in kg/m² per mm)","For toughened glass, add 10–20% cost premium","Check thickness requirements: 4 mm for shelves, 6 mm for small windows, 10+ mm for doors","Calculate edge polishing cost per linear meter"],
    ["Using annealed (non-toughened) glass where safety glass is required by code","Not accounting for the weight — glass is heavy and needs proper support","Ordering the exact size — glass needs 3–5 mm clearance in frames"],
    "Your glass panel weighs approximately {peso_kg} kg and requires {area} m² of {grosor} mm thick glass.", "Weight = area × thickness × 2.5; Area = L × W", "Glass estimate for a 2 m × 1 m window panel, 6 mm thick")

# ── Block 4: fontaneria ──
f["038"] = N("Copper & PEX Pipe Calculator",
    ["Measure the total pipe run length from source to fixtures","Add 10% for fittings, bends, and vertical runs","Copper: choose diameter based on fixture units (15 mm for basins, 22 mm for baths)","PEX: same sizing but needs fewer fittings due to flexibility","Calculate fittings: approximately one per 2–3 meters of pipe run plus elbows and tees"],
    ["Using undersized pipe — causes low pressure and noisy flow","Not allowing for thermal expansion — PEX expands more than copper","Forgetting isolation valves — install at each fixture for future maintenance"],
    "For a plumbing run of approximately {longitud} m, you need {tubos} lengths of pipe and {accesorios} fittings.", "Pipe = run length × 1.10; Fittings = run length ÷ 2.5", "Copper pipe estimate for a bathroom supply run")
f["039"] = N("PVC Drainage Pipe Calculator",
    ["Measure the horizontal and vertical pipe runs","Drainage pipes need a minimum slope of 1–2% (1–2 cm per meter)","Calculate total pipe length including slope adjustment","Fittings: add 15–20% to pipe length for junctions, bends, and inspection chambers","Diameter: 110 mm for soil stacks, 50 mm for basins, 40 mm for washing machines"],
    ["Not maintaining the minimum slope — causes blockages over time","Using too many bends — every 90° bend increases blockage risk","Connecting rainwater drainage to the sewer — illegal in most jurisdictions"],
    "Your drainage system needs approximately {longitud} m of PVC pipe at {diametro} mm diameter, with {accesorios} fittings.", "Pipe length = run length × 1.18; Slope check: rise ÷ run ≥ 0.01", "PVC drainage estimate for a house sewer connection")
f["040"] = N("Water Service Connection Calculator",
    ["Measure distance from the water main to the building entry point","Trench depth must be below frost line (typically 0.80–1.20 m)","Pipe diameter: based on peak flow demand (typically 25–32 mm for a house)","Add 2–3 m extra for the vertical rise at each end of the trench","Include backflow prevention, stop valve, and water meter housing"],
    ["Not checking local utility requirements — some demand specific pipe materials","Digging the trench too shallow — pipes freeze in winter","Forgetting to install tracer wire with plastic pipe for future locating"],
    "For a {distancia} m connection from the main, use {diametro} mm pipe buried at least 1 m deep.", "Trench volume = distance × 0.40 × frost depth; Pipe = distance + 3 m", "Water connection for a 15 m run from street main to house")
f["041"] = N("Water Pressure Calculator",
    ["Static pressure: height of water column ÷ 10.2 (gives pressure in bar)","Each meter of elevation = 0.098 bar of static pressure","Dynamic pressure = static pressure − friction loss in pipes","Friction loss depends on pipe diameter, length, and flow rate","Minimum recommended pressure at fixtures: 1.0–1.5 bar"],
    ["Confusing static pressure (when water is not flowing) with dynamic pressure","Not accounting for pressure loss in long pipe runs — can lose 1 bar per 100 m","Installing a booster pump without checking if the mains can supply the flow"],
    "Your static pressure is approximately {presion_estatica} bar, with estimated dynamic pressure of {presion_dinamica} bar at the fixture.", "Static pressure = height ÷ 10.2; Dynamic = static − friction loss", "Water pressure check for a house 8 m above the mains connection")
f["042"] = N("Water Heater Sizing Calculator",
    ["Calculate peak hot water demand: add up simultaneous usage","Electric: 30–50 L per person, gas: 50–80 L per person for storage","Tankless (instant): flow rate of 6–12 L/min for one shower","Recovery time: how fast the heater can reheat a full tank","Consider future usage — growing families need larger capacity"],
    ["Buying a heater that is too small — running out of hot water daily","Oversizing an electric heater — higher standby losses","Not considering the incoming cold water temperature — winter vs summer"],
    "For a household of {personas} people, a {capacidad} L water heater should meet your hot water needs.", "Capacity = people × 50 L (electric) or people × 70 L (gas)", "Water heater size for a 4-person household")
f["043"] = N("Water Tank Capacity Calculator",
    ["Calculate daily water consumption: 150 L per person is typical","Multiply by the number of reserve days (usually 2–5)","Add 20% for fire reserve if required","Tank volume: daily consumption × reserve days × 1.20","Choose tank dimensions: rectangular or cylindrical based on space"],
    ["Underestimating daily consumption — includes washing, cooking, and irrigation","Not providing adequate overflow and ventilation for the tank","Placing the tank on unstable ground — a full 5000 L tank weighs 5 tonnes"],
    "A {volumen} L tank provides enough water for {personas} people with {dias} days of reserve.", "Volume = people × 150 L × reserve days × 1.20", "Water storage for a home with 4 people and 3 days reserve")
f["047"] = N("Drain Trap Calculator",
    ["Determine the fixture type: basin, shower, bath, or floor drain","Trap diameter: basins = 32–40 mm, showers = 40–50 mm, toilets = 100 mm","Water seal depth: minimum 50 mm to prevent sewer gas entry","Calculate pipe slope from trap to stack: 2% minimum","Consider space under the fixture — some traps need more height"],
    ["Using the wrong trap type for the fixture — S-traps are banned in many codes","Not maintaining the water seal — unused floor drains dry out","Installing the trap too far from the fixture — causes siphoning of the seal"],
    "Install a {diametro} mm trap with a minimum {sello} mm water seal for this fixture.", "Trap size based on fixture type; Seal depth = 50–75 mm", "Drain trap sizing for a bathroom basin")
f["049"] = N("Pool Volume Calculator",
    ["Rectangular pool: length × width × average depth (m)","Average depth = (shallow end + deep end) ÷ 2","Circular pool: π × radius² × average depth","Irregular shape: break into rectangular sections and sum","Result in m³; multiply by 1000 for liters"],
    ["Using the maximum depth instead of average — overestimates volume","Forgetting to subtract steps, benches, and swim-outs from the volume","Not accounting for the fact that you never fill a pool to the very top"],
    "Your pool holds approximately {volumen} m³ of water — that's {litros} liters.", "Volume = L × W × avg depth; or πr² × avg depth", "Calculate water volume for an 8 m × 4 m pool, 1.2 m to 1.8 m deep")

def apply():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        if "bak" in fp or "monolithic" in fp or os.path.basename(fp) == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        cid = calc.get("id", "")
        if cid not in f: continue
        en = calc.setdefault("i18n", {}).setdefault("en", {})
        changed = False
        for k, v in f[cid].items():
            if not v: continue
            en[k] = v
            changed = True
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated}")

apply()
