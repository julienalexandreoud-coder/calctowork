#!/usr/bin/env python3
"""Fix English narrative — batch 3 covering blocks 5-9 and math."""

import json, os, glob
CALC = r"C:\Microsaas\obra\src\calculators"
f = {}

def N(name, steps, mistakes, rc, fd, el): return {k:v for k,v in locals().items() if k != 'N' and v}

# ── BLOCK 5: electricidad ──
f["050"] = N("Electrical Cable Size Calculator",
    ["Calculate the load current: power in watts ÷ voltage","Choose conductor material: copper or aluminum","Apply derating factors for temperature, grouping, and installation method","Select cable size from standard tables based on calculated current","Verify voltage drop stays below 3% for lighting or 5% for power"],
    ["Using too small a cable — causes overheating and fire risk","Not applying temperature derating — cables in hot spaces carry less current","Forgetting that cable length affects voltage drop, not just load current"],
    "For a load of {potencia} W at {voltaje} V over {longitud_cable} m, the minimum copper cable cross-section is {seccion} mm².", "Current = P ÷ V; Cable size from IEC tables with derating factors", "Cable size for a 3000 W circuit, 230 V, 20 m cable run")
f["051"] = N("Voltage Drop Calculator",
    ["Calculate the percentage drop: (2 × L × I × ρ) ÷ (A × V) × 100","Where L = one-way cable length, I = current, ρ = resistivity, A = cross-section","Copper resistivity = 0.0172 Ω·mm²/m; aluminum = 0.0282","Compare result to maximum allowed: 3% for lighting, 5% for other uses","If drop exceeds limit, increase cable cross-section"],
    ["Calculating drop for the wrong voltage — 230 V vs 400 V three-phase","Not doubling the length — current travels out AND back","Using the nominal voltage instead of the actual supply voltage"],
    "The voltage drop of {caida}% over {distancia} m is within acceptable limits for this circuit type.", "Vdrop% = (2 × L × I × ρ) ÷ (A × V) × 100", "Voltage drop check for a 50 m cable carrying 16 A at 230 V")
f["053"] = N("Air Conditioner BTU Calculator",
    ["Calculate room volume: length × width × height","Base cooling: multiply room area by 500–600 BTU/m² depending on climate","Add 10% for each south-facing window","Add 600 BTU per person above 2 occupants","Add 4000 BTU if the room is a kitchen"],
    ["Buying an oversized unit — cools too fast without removing humidity","Buying an undersized unit — runs continuously and never reaches temperature","Forgetting to account for ceiling height — volume matters, not just floor area"],
    "For a room of {area} m², the recommended cooling capacity is approximately {btu_necesarios} BTU/h.", "BTU = area × 550 + window adjustments + occupancy adjustments", "AC sizing for a 25 m² bedroom with one south-facing window")
f["055"] = N("Electrical Panel Calculator",
    ["List all circuits with their breaker ratings in amps","Calculate total connected load: sum of all breaker ratings","Apply diversity factor: total connected × 0.6 for residential","Single phase: total VA = total A × 230 V","Verify panel rating exceeds calculated demand by at least 20%"],
    ["Summing breaker ratings directly — they don't all draw full load simultaneously","Not leaving spare capacity for future circuits and EV chargers","Forgetting that RCD/GFCI requirements add to the panel space needed"],
    "With a calculated demand of {carga_total} A on a {tamano_panel} A panel, you have {margen}% spare capacity.", "Demand = sum of breakers × diversity factor; Spare = (panel − demand) ÷ panel × 100", "Panel load check for a house with 10 circuits on a 100 A panel")
f["058"] = N("Grounding Rod Calculator",
    ["Soil resistivity varies: clay 20–100 Ω·m, sand 200–3000 Ω·m, rock 1000–10000 Ω·m","Single rod resistance: R = ρ ÷ (2πL) × ln(4L/d)","Where L = rod length, d = rod diameter, ρ = soil resistivity","If resistance exceeds 10 Ω, add more rods spaced at least twice the rod length apart","Multiple rods in parallel: Rtotal = R ÷ (n × 0.8) for typical installations"],
    ["Using too short a rod — 1.5–2.4 m is standard for residential","Not testing soil resistivity before installation — guessing leads to poor grounding","Placing rods too close together — they interfere rather than improving the ground"],
    "A {longitud_pica} m grounding rod in {resistividad} Ω·m soil gives approximately {resistencia} Ω of earth resistance.", "R = ρ ÷ (2πL) × ln(4L/d); Multiple rods: Rtotal ≈ R ÷ (n × 0.8)", "Ground rod calculation for clay soil with a 2 m rod")
f["059"] = N("Solar Panel Installation Calculator",
    ["Calculate daily energy consumption: sum all appliance watt-hours","Determine peak sun hours for your location (typically 3–6 hours/day)","Panel wattage needed: daily Wh ÷ peak sun hours ÷ system efficiency (0.75)","Number of panels: system wattage ÷ panel rating (typically 400–450 W)","Battery capacity (off-grid): daily Wh × autonomy days ÷ battery voltage ÷ DoD"],
    ["Overestimating peak sun hours — use actual location data, not the maximum","Forgetting system losses: inverter 5%, wiring 3%, dust 5%, temperature 10%","Undersizing the inverter — it should be 80–100% of the panel array rating"],
    "You need approximately {paneles} solar panels totaling {potencia_total} W, with {baterias} batteries for backup.", "Panels = daily Wh ÷ (sun hours × 0.75 × panel W); Batteries = daily Wh × days ÷ V ÷ 0.5", "Solar system size for 15 kWh daily consumption with 5 peak sun hours")

# ── BLOCK 6: climatizacion ──
f["061"] = N("Gas Boiler Sizing Calculator",
    ["Calculate total heat loss: area × U-values for walls, roof, floor, windows","Add ventilation heat loss: 0.33 × air changes × volume × ΔT","Total heat loss in watts = sum of fabric + ventilation losses","Convert to kW: divide by 1000","Add 10–20% for hot water demand on combi boilers"],
    ["Sizing the boiler by floor area alone — ignores insulation levels","Oversizing a modern condensing boiler — they work best at lower flow temperatures","Forgetting that a combi boiler prioritizes hot water, so size for the largest demand"],
    "For a {area} m² home, a {potencia} kW gas boiler provides adequate heating and hot water.", "Heat loss = Σ(area × U × ΔT) + ventilation loss; Boiler kW = heat loss ÷ 1000 × 1.15", "Boiler size for a 120 m² home with average insulation")
f["062"] = N("Radiator Heat Output Calculator",
    ["Calculate room heat loss from dimensions and insulation","1 m² of radiator typically outputs 500–600 W at ΔT 50°C","Required radiator area: room heat loss ÷ radiator output per m²","Consider radiator type: panel, convector, or column — each has different output","Add 10% for rooms with two external walls"],
    ["Hiding radiators behind furniture or curtains — reduces output by 20–40%","Not bleeding radiators before winter — trapped air prevents circulation","Placing the thermostat near a radiator — causes short cycling"],
    "This room needs a radiator with approximately {btu_requeridos} BTU/h ({vatios} W) heat output.", "Radiator size = room heat loss ÷ output per m²; 1 m² panel ≈ 550 W at ΔT 50", "Radiator size for a 20 m² living room with two external walls")
f["063"] = N("Underfloor Heating Calculator",
    ["Calculate floor area excluding fixed units (kitchen, bathroom cabinets)","Pipe spacing: 150 mm for high output, 200 mm for standard, 300 mm in hallways","Pipe length per m²: at 150 mm spacing ≈ 6.7 m/m²; at 200 mm ≈ 5 m/m²","Total pipe length: floor area × pipe density + 10% for manifold connections","Heat output: approximately 70–100 W/m² depending on floor covering"],
    ["Installing under thick carpet — reduces heat output by 30–50%","Not installing edge insulation — heat escapes to external walls","Running pipes too close together in small rooms — causes overheating"],
    "For {area} m² of heated floor, you need approximately {metros_tubo} m of pipe at {separacion} mm spacing.", "Pipe length = area × spacing factor × 1.10; Spacing factor = 10 ÷ spacing in cm", "Underfloor heating for a 25 m² living room with tile floor")
f["066"] = N("Ventilation Calculator",
    ["Determine room volume: length × width × height","Select air change rate: bathroom 6–8, kitchen 10–15, office 4–6, bedroom 2–4","Required airflow: room volume × air change rate in m³/h","Extract fan capacity must equal or exceed calculated airflow","For continuous ventilation, use 0.3–0.5 air changes per hour for whole house"],
    ["Under-ventilating bathrooms — leads to mold growth within months","Not providing makeup air — extract fans need fresh air inlets to work","Installing a noisy fan because it was the cheapest — choose <35 dB for bedrooms"],
    "This room needs an extract fan rated at {caudal} m³/h to achieve {renovaciones} air changes per hour.", "Airflow (m³/h) = room volume × air change rate", "Ventilation for a 15 m³ bathroom needing 8 air changes per hour")
f["069"] = N("Heat Pump Calculator",
    ["Calculate building heat loss at design temperature (typically −5°C to −10°C)","Heat pump capacity = building heat loss in kW","COP (Coefficient of Performance): typically 3–4 for air source, 4–5 for ground source","Check that existing radiators work at the lower flow temperature of a heat pump (35–45°C vs 60–70°C for boilers)","Annual electricity cost = heat demand ÷ COP × electricity price per kWh"],
    ["Replacing a boiler with the same kW heat pump — heat pumps need lower flow temps but longer run times","Not upgrading insulation before installing — heat pumps work best in well-insulated homes","Installing an air source heat pump in a noisy location — check planning regulations for noise"],
    "A {potencia} kW heat pump with COP of {cop} will provide efficient heating for your building.", "Heat pump kW = building heat loss at design temp; Running cost = demand ÷ COP × electric rate", "Heat pump sizing for a well-insulated 150 m² home")

# ── BLOCK 7: carpinteria ──
f["072"] = N("Interior Door Calculator",
    ["Measure the rough opening: width and height in mm","Standard interior doors: 726, 826, or 926 mm wide × 2040 mm high","Choose door swing direction: left or right, inward or outward","Frame kit includes: head, two jambs, stop mouldings","Hardware per door: 3 hinges, 1 handle set, 1 latch, optional door stop"],
    ["Measuring the old door instead of the rough opening — sizes change with settlement","Ordering the wrong swing direction — it is irreversible once the frame is installed","Forgetting that door frames need shimming — rough opening must be 10–15 mm larger than the frame"],
    "For an opening of {ancho} mm × {alto} mm, order a {medida_puerta} interior door with matching frame and hardware.", "Door size = rough opening − 10 mm each side; Hardware: 3 hinges + handle set per door", "Interior door sizing for a standard 826 mm bedroom door opening")
f["076"] = N("Wooden Staircase Calculator",
    ["Measure total rise: finished floor to finished floor height","Calculate number of risers: total rise ÷ desired riser height (170–190 mm)","Round riser count up, recalculate exact riser height","Calculate tread depth: use the formula 2R + T = 600–650 mm","Total run: tread depth × (number of treads − 1)"],
    ["Making risers too tall — building codes typically limit to 190 mm maximum","Not allowing for floor finishes — carpet adds 10–15 mm, tiles add 15–20 mm","Forgetting the nosing overhang — treads should overhang risers by 15–25 mm"],
    "A staircase with {escalones} steps, {contrahuella} mm risers, and {huella} mm treads gives a comfortable and code-compliant stair.", "Risers = total rise ÷ target height (round up); Tread = 630 − 2 × riser height", "Stair design for a 2.80 m floor-to-floor height")
f["073"] = N("Sliding Door Calculator",
    ["Measure the opening width and height","Sliding door panel width = opening width ÷ 2 + 50 mm overlap","Door height = opening height − 10 mm for floor clearance","Track length = opening width × 2 for bypass doors","Hardware: top-hung or bottom-rolling track, rollers, guides, handles"],
    ["Not checking if the wall has enough space for the doors to slide open","Installing the track out of level — doors will slide open or closed on their own","Forgetting the soft-close mechanism — heavy glass doors slam without it"],
    "For a {ancho} m opening, each sliding door panel should be approximately {ancho_panel} m wide.", "Panel width = (opening width ÷ 2) + 0.05; Track = opening width × 2", "Sliding door dimensions for a 2.4 m wide wardrobe opening")
f["075"] = N("Window Frame Calculator",
    ["Measure the rough opening: width × height","Frame profile: subtract 20–30 mm from opening for clearance and shimming","Glass area: frame dimensions minus profile width (typically 50–60 mm per side)","Choose frame material: aluminum = slim profile, PVC = better insulation","Add hardware: hinges or friction stays, handles, locking mechanism"],
    ["Ordering glass the same size as the frame — glass is smaller than the outer frame","Not specifying toughened glass for low windows — required by safety codes","Forgetting drainage slots in the frame — water must escape, not pool"],
    "For a {ancho} m × {alto} m window opening, the frame requires {perfil_metres} m of profile and {area_vidrio} m² of glass.", "Glass area = (width − 0.10) × (height − 0.10); Frame perimeter = 2 × (W + H)", "Window frame for a 1.5 m × 1.2 m opening")
f["077"] = N("Metal Railing Calculator",
    ["Measure total railing length including any returns","Post spacing: typically 1.2–1.5 m between posts","Number of posts: railing length ÷ spacing + 1 (for end posts)","Balusters: typically 3–4 per meter, spaced ≤100 mm apart for safety","Handrail length = railing length + 10% for joints and returns"],
    ["Exceeding 100 mm gap between balusters — a child's head could get stuck","Not anchoring end posts into the structure — simple surface mounting is insufficient","Forgetting that exterior railings need corrosion protection — galvanized or stainless steel"],
    "For {longitud} m of railing, you need {postes} posts, {balustres} balusters, and {barandal_m} m of handrail.", "Posts = length ÷ spacing + 1; Balusters = length × density per meter", "Metal railing for a 5 m balcony with 1.3 m post spacing")
f["079"] = N("Steel Structure Calculator",
    ["Define load requirements: dead load + live load + wind/snow loads","Select steel profiles: IPE, HEA, HEB for beams; HEA/HEB for columns","Calculate section modulus needed: M ÷ σallowable","Choose profile with adequate section modulus from steel tables","Check deflection limits: typically span ÷ 250 for floors, span ÷ 200 for roofs"],
    ["Using the same profile for all members — columns and beams have different requirements","Not checking lateral-torsional buckling for long unsupported beams","Forgetting connection design — the connections often govern the design, not the members"],
    "Based on the load and span, an {perfil} steel profile provides adequate strength and stiffness.", "M = wL²/8; Required Z = M ÷ fy; Deflection = 5wL⁴/(384EI) < L/250", "Steel beam selection for a 6 m span with 20 kN/m load")

# ── BLOCK 8: pintura ──
f["083"] = N("Wall Paint Calculator",
    ["Calculate total wall area: perimeter × height, minus doors and windows","Standard paint coverage: 10–12 m² per liter per coat","Most walls need 2 coats for even coverage","Litres per coat: wall area ÷ coverage rate","Total paint: litres per coat × number of coats","Add 10% for touch-ups and absorption on porous surfaces"],
    ["Measuring only one coat — almost all walls need at least two coats for opacity","Forgetting to subtract doors and windows — can be 15–25% of wall area","Using the same coverage rate for new plaster — it absorbs much more paint than old walls"],
    "For {area} m² of wall with {manos} coats, you need approximately {litros} liters of paint.", "Litres = area ÷ coverage × coats × 1.10", "Paint estimate for a 80 m² room with 2 coats")
f["084"] = N("Ceiling Paint Calculator",
    ["Calculate ceiling area: room length × width","Ceiling paint coverage: 10–12 m² per liter per coat","One coat may suffice for white over white, but two coats recommended for color changes","Litres per coat: ceiling area ÷ coverage rate","Add 10% for absorption and touch-ups","Consider ceiling paint specifically — it is thicker and spatter-resistant"],
    ["Using wall paint on ceilings — it drips more and doesn't cover as evenly","Painting without drop cloths — ceiling paint splatters","Applying too thick — causes orange-peel texture and cracking"],
    "For a {area} m² ceiling, you need approximately {litros} liters of ceiling paint.", "Litres = ceiling area ÷ 10 × 1.10", "Paint quantity for a 20 m² lounge ceiling")
f["086"] = N("Varnish Calculator",
    ["Calculate surface area: sum of all exterior wood areas","Coverage: approximately 10–14 m² per liter per coat, depending on wood porosity","Exterior wood typically needs 3 coats: primer/base coat + 2 top coats","Porous or weathered wood absorbs 20–30% more","Add 10% for brush loading and spillage"],
    ["Applying varnish in direct sunlight — dries too fast and leaves brush marks","Not sanding between coats — varnish needs mechanical adhesion between layers","Using interior varnish outdoors — lacks UV protection and weathers within months"],
    "For {area} m² of exterior wood with {manos} coats, you need approximately {litros_barniz} liters of varnish.", "Litres = area ÷ coverage × coats × 1.10", "Varnish estimate for a 30 m² wooden deck, 3 coats")
f["088"] = N("Primer Sealer Calculator",
    ["Calculate surface area to prime","Coverage: primer covers 8–12 m² per liter on porous surfaces","New drywall: use PVA primer at 10 m²/L, one coat","Previously painted: use standard primer at 12 m²/L, one coat","Raw wood: use wood primer at 8 m²/L, may need two coats","Add 15% for porous or very absorbent surfaces"],
    ["Skipping primer on new drywall — paint peels within months","Using cheap primer — good primer is cheaper than an extra coat of paint","Applying primer too thin — it needs to seal the surface, not just tint it"],
    "For {area} m² of surface, you need approximately {litros} liters of primer.", "Litres = area ÷ coverage × coats × 1.10", "Primer estimate for 120 m² of new drywall")
f["091"] = N("Wallpaper Calculator",
    ["Measure each wall height and width separately","Standard roll: 10 m long × 0.53 m wide = 5.3 m², but usable is about 4.2 m² after pattern matching","Rolls per wall = (wall width ÷ roll width, rounded up) × (wall height + pattern repeat) ÷ roll length","Total rolls = sum for all walls, rounded up to full rolls","Add 1–2 extra rolls for complex patterns and future repairs"],
    ["Calculating from room area only — wallpaper is sold by the roll, and pattern matching wastes 10–20%","Forgetting about pattern repeat — large repeats need significantly more paper","Not buying an extra roll for future repairs — different batches have slight color differences"],
    "For a room with {area} m² of wall area, order approximately {rollos} rolls of wallpaper including pattern waste.", "Rolls = Σ(ceil(wall width ÷ 0.53) × (wall height + repeat) ÷ 10)", "Wallpaper estimate for a 4 m × 3 m room with standard walls")

# ── BLOCK 9: gestion ──
f["093"] = {
    "steps": ["Enter the net amount (price before tax)","Multiply by VAT rate: net x (VAT% / 100) = VAT amount","Gross amount = net + VAT amount","To extract VAT from gross: gross / (1 + VAT%/100) = net amount","Common rates: standard 21%, reduced 10%, super-reduced 4%"],
    "mistakes": ["Applying VAT to an amount that already includes VAT — always check if prices are net or gross","Using the wrong VAT rate for the product category — not everything is standard rate","Forgetting that VAT is calculated on the total, not per item when items have different rates"],
    "result_context": "Net: {neto} EUR, VAT ({iva}%): {iva_eur} EUR, Gross total: {bruto} EUR.",
    "formula_display": "Total gross = net x (1 + VAT% / 100)",
    "example_label": "Calculate VAT on a 500 EUR net invoice at 21% rate"
}
f["095"] = N("Profit Margin Calculator",
    ["Enter your cost price (what you pay)","Enter your selling price (what you charge)","Profit = selling price − cost price","Margin % = (profit ÷ selling price) × 100","Markup % = (profit ÷ cost price) × 100"],
    ["Confusing margin with markup — a 50% markup is only a 33% margin","Not including ALL costs — overhead, shipping, labor, and fees must be included","Setting margin too low to cover returns, warranty claims, and payment processing fees"],
    "At a selling price of {precio_venta} with cost of {coste}, your profit margin is {margen}%.", "Margin = (price − cost) ÷ price × 100", "Calculate profit margin on a product costing 80€ sold at 120€")
f["096"] = N("Break Even Calculator",
    ["Enter total fixed costs (rent, salaries, insurance — regardless of sales)","Enter variable cost per unit (materials, shipping, packaging per item)","Enter selling price per unit","Contribution margin = selling price − variable cost","Break-even units = fixed costs ÷ contribution margin","Break-even revenue = break-even units × selling price"],
    ["Forgetting that fixed costs include depreciation and interest — not just obvious expenses","Assuming variable costs stay the same at higher volumes — bulk discounts change unit costs","Not recalculating after price changes — a small price cut needs a lot more volume to break even"],
    "You need to sell {punto_equilibrio} units (revenue of {ingreso_equilibrio}€) to cover all costs.", "Break-even = fixed costs ÷ (price − variable cost per unit)", "Break-even point for fixed costs of 5000€, variable 20€/unit, selling at 50€")
f["097"] = N("Labor Cost Calculator",
    ["Enter the number of workers and hours worked","Enter hourly wage rate","Calculate base labor cost: workers × hours × hourly rate","Add burden: typically 20–35% for payroll taxes, insurance, benefits","Add overhead allocation: tools, supervision, site facilities","Total labor cost = base + burden + overhead"],
    ["Using only the hourly wage — the true cost is 1.3–1.5× the wage","Not accounting for overtime rates — time-and-a-half or double time","Forgetting travel time, setup, and cleanup — these are paid hours too"],
    "The total labor cost is {coste_total}€ comprising {coste_base}€ base wages plus {coste_cargas}€ in burden and overhead.", "Total labor = workers × hours × rate × (1 + burden%)", "Labor cost for 3 workers, 40 hours each, at 18€/hour with 30% burden")
f["100"] = N("Tool ROI Calculator",
    ["Enter the purchase cost of the tool or machine","Estimate hours saved per month compared to the current method","Calculate monthly savings: hours saved × hourly rate (labor cost)","Calculate payback period: purchase cost ÷ monthly savings","ROI after 1 year = (12 × monthly savings − purchase cost) ÷ purchase cost × 100%"],
    ["Not including maintenance costs — tools need servicing, consumables, and repairs","Overestimating time saved — new tools often have a learning curve","Forgetting that the old tool still has resale value — net investment is new cost minus old sale price"],
    "This tool pays for itself in {meses_recuperacion} months and generates a {roi}% ROI in the first year.", "Payback = cost ÷ monthly savings; ROI = (annual savings − cost) ÷ cost × 100", "ROI on a 5000€ tool saving 20 hours/month at 25€/hour")

# ── MATH ──
f["200"] = N("Percentage Calculator",
    ["Enter the whole value (the 100% base)","Enter the percentage you want to calculate","Calculate: result = whole × (percentage ÷ 100)","The result shows what X% of the total equals","Reverse calculation: percentage = (part ÷ whole) × 100"],
    ["Confusing percentage points with percentage — an increase from 10% to 15% is 5 percentage points, but a 50% increase"],
    "{porcentaje}% of {total} equals {resultado}.", "Result = total × (percentage ÷ 100)", "What is 20% of 250?")
f["202"] = N("Rule of Three Calculator",
    ["Set up the proportion: if A corresponds to B, then C corresponds to X","For direct proportion: X = (B × C) ÷ A","For inverse proportion: X = (A × B) ÷ C","Enter the three known values","The calculator solves for the fourth unknown value"],
    ["Confusing direct with inverse proportion — if one goes up and the other goes down, it is inverse"],
    "If {a} corresponds to {b}, then {c} corresponds to {x}.", "X = (B × C) ÷ A (direct) or X = (A × B) ÷ C (inverse)", "If 5 kg costs 15€, how much does 8 kg cost?")
f["203"] = {
    "steps": ["Enter the original price","Enter the discount percentage","Calculate discount amount: price x (discount / 100)","Calculate final price: original price minus discount amount","Savings shown as both amount and percentage"],
    "mistakes": ["Applying a discount to an already discounted price — it compounds, not adds","Forgetting that VAT is calculated AFTER the discount is applied"],
    "result_context": "You save {ahorro} ({porcentaje}% off), paying {precio_final} instead of {precio_original}.",
    "formula_display": "Final price = original x (1 - discount% / 100)",
    "example_label": "How much is 30% off a 85€ item?"
}
f["205"] = N("Exponential Growth Calculator",
    ["Enter the initial value","Enter the growth rate as a percentage","Enter the number of time periods","Calculate final value: initial × (1 + rate%)ⁿ","The result shows exponential compounding over time"],
    ["Using simple interest when compound applies — the difference grows dramatically over many periods"],
    "Starting with {inicial} and growing at {tasa}% per period, after {periodos} periods the value is {final}.", "Final = initial × (1 + rate)ⁿ", "What does 1000€ grow to at 8% annual over 10 years?")
f["206"] = N("Logarithm Calculator",
    ["Enter the number you want the logarithm of","Choose the base (e for natural log, 10 for common log, or custom)","The logarithm answers: 'to what power must the base be raised to get this number?'","log₁₀(100) = 2 because 10² = 100","Natural log ln(e) = 1 because e¹ = e"],
    ["Confusing log base 10 with natural log — they give very different results","Taking log of zero or negative numbers — undefined in real numbers"],
    "The logarithm base {base} of {numero} equals {resultado}.", "log_b(x) = y means bʸ = x", "What is log base 2 of 64?")
f["208"] = N("Root Calculator",
    ["Enter the number (radicand)","Choose the root degree (2 = square root, 3 = cube root, etc.)","The nth root of X is the number that, when raised to power n, equals X","√25 = 5 because 5² = 25","Cube root ³√27 = 3 because 3³ = 27"],
    ["Forgetting that even roots of negative numbers are undefined in real numbers","Taking the square root twice is NOT the same as the 4th root if the number is negative"],
    "The {grado}ᵗʰ root of {radicando} is {resultado}.", "ⁿ√x = x^(1/n)", "What is the cube root of 125?")
f["221"] = N("Probability Calculator",
    ["Enter the number of favorable outcomes","Enter the total number of possible outcomes","Probability = favorable ÷ total","Result is between 0 (impossible) and 1 (certain)","Multiply by 100 for percentage probability"],
    ["Counting outcomes that are not equally likely — probability assumes fair dice, fair coins, etc.", "Adding probabilities of overlapping events without subtracting the overlap"],
    "The probability is {probabilidad} ({porcentaje}%) — {favorables} favorable outcomes out of {totales} possible.", "P = favorable outcomes ÷ total outcomes", "What is the probability of rolling a 4 or higher on a 6-sided die?")
f["222"] = N("Pythagorean Theorem Calculator",
    ["Enter the two known sides of a right triangle","To find the hypotenuse: c = √(a² + b²)","To find a leg: a = √(c² − b²)","The result is the length of the missing side","Used for distances, diagonal measurements, and construction squaring"],
    ["Applying the theorem to non-right triangles — only works when one angle is exactly 90°"],
    "In a right triangle, with {lado_a} and {lado_b} as legs, the {lado} is {resultado}.", "Hypotenuse = √(a² + b²); Leg = √(c² − b²)", "Find the diagonal of a rectangle 3 m wide and 4 m long")

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
    print(f"Updated {updated} narrative fields")

apply()
