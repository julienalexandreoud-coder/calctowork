"""
Rewrites thin content files for calcs 1100-1119 with rich, specific HTML.
Uses steps, mistakes, formula_display, result_context, example_inputs from calculators.json.
"""
import json, pathlib, html as htmllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
I18N_FILE  = ROOT / "src" / "i18n" / "en.json"
CONTENT_DIR = ROOT / "src" / "content" / "en"

data  = json.loads(CALCS_FILE.read_text(encoding="utf-8"))
i18n  = json.loads(I18N_FILE.read_text(encoding="utf-8"))
calcs = {c["id"]: c for c in data["calculators"]}
calcs_i18n = i18n.get("calculators", {})

def esc(s: str) -> str:
    return htmllib.escape(str(s))

# Specific content overrides per calculator
CONTENT = {
    "1100": {
        "intro": """The Decking Calculator estimates how many deck boards you need for any timber deck — covering board count, row count, total linear metres, and percentage waste. Whether you're building a garden deck, pool surround, or balcony, enter your dimensions and get exact material quantities before you visit the timber yard.""",
        "what_it_calculates": "deck area in m², number of boards, number of rows, total linear metres of timber, and waste percentage from end cuts.",
        "faqs": [
            ("What gap should I leave between deck boards?", "A 6 mm gap (0.6 cm) is standard for softwood decking to allow for water drainage and seasonal expansion. Hardwood can use a tighter 3–5 mm gap. Never use zero gap — boards swell when wet and will buckle."),
            ("How much extra decking should I order?", "The calculator includes a waste factor automatically. For a simple rectangular deck, 5–8% waste is typical. Add 10–15% if you're running boards at 45° (diagonal layout), which generates significantly more offcuts."),
            ("What board width is most common?", "90 mm, 120 mm, and 140 mm are the most common nominal widths. Always use the finished (actual) width, not the nominal size — a '140 mm' board is typically 135 mm after planing."),
            ("Hardwood vs softwood: does it affect the calculation?", "The count is the same, but hardwood boards are denser and heavier. Allow for thermal movement gaps: hardwood expands less than softwood, so you can reduce the gap slightly to 3–4 mm."),
            ("Do I need to include joists in this calculation?", "No — this calculator covers deck boards only. Joist spacing (typically 400–600 mm centres) depends on board thickness: 19 mm boards need 400 mm centres, 25 mm boards can span 600 mm.")
        ]
    },
    "1101": {
        "intro": """The Sod / Turf Calculator tells you exactly how many sod rolls you need to cover a lawn area. It accounts for the roll dimensions you're purchasing and automatically adds 5% for waste from cuts along edges and irregular shapes.""",
        "what_it_calculates": "total lawn area in m², number of rolls needed, rolls with waste allowance, and coverage per roll.",
        "faqs": [
            ("What are standard sod roll sizes?", "The most common UK and European size is 0.6 m × 2 m (1.2 m² per roll). US rolls are typically 2 ft × 5 ft or 16 in × 24 in. Enter your supplier's exact dimensions into the calculator."),
            ("When is the best time to lay sod?", "Spring and early autumn are ideal — soil temperatures are mild, moisture is available, and grass roots establish before extreme heat or frost. Avoid laying in midsummer heat or frozen ground."),
            ("How long does sod need to be watered after laying?", "Water immediately after laying and keep the soil moist (not waterlogged) for the first 2–3 weeks. Reduce watering once roots have knitted into the soil — test by gently tugging a corner."),
            ("Should I add extra for an irregular lawn shape?", "The calculator adds 5% waste by default. For highly irregular shapes with many curves and cutouts (L-shapes, circles), increase waste to 10–15% manually by multiplying your calculated rolls by 1.10–1.15."),
            ("Can sod be laid over existing grass?", "No — existing grass and weeds must be removed first, otherwise the new turf will struggle to root. Kill weeds, remove old turf with a turf cutter or spade, then level and firm the soil before laying.")
        ]
    },
    "1102": {
        "intro": """The Mulch Calculator computes how many bags of mulch you need to cover garden beds, paths, or play areas to a specified depth. Enter your area dimensions and mulch depth in centimetres, choose your bag size, and get the exact bag count — no guessing at the garden centre.""",
        "what_it_calculates": "area in m², volume in m³, number of bags needed, and volume in cubic yards.",
        "faqs": [
            ("How deep should I apply mulch?", "5–8 cm (2–3 inches) is the standard for weed suppression and moisture retention. Less than 5 cm lets weeds through; more than 10 cm can suffocate plant roots and invite pests. Keep mulch away from plant stems and tree trunks."),
            ("What type of mulch is best?", "Wood chip mulch is best for paths and tree bases. Bark mulch suits ornamental beds. Straw or compost mulch is ideal around vegetables. Rubber mulch lasts longest but doesn't improve soil. Choose based on appearance and whether you want it to break down and feed the soil."),
            ("How much does a cubic metre of mulch weigh?", "It depends on type: wood chip mulch ≈ 400–500 kg/m³; bark mulch ≈ 300–400 kg/m³; gravel mulch ≈ 1,400–1,600 kg/m³. A standard 50 L bag of bark mulch weighs about 15–20 kg."),
            ("Do I need to remove old mulch before adding new?", "If the old mulch is less than 5 cm deep and not compacted, top it up. If it's thick, matted, or harbouring mould, remove the old layer first to prevent nitrogen depletion as it decomposes."),
            ("Does mulch colour affect performance?", "Colour is cosmetic only. Dark mulches absorb more heat (can be too hot for sensitive plants in summer) while light-coloured mulch reflects heat. All organic mulch degrades and must be topped up annually or bi-annually.")
        ]
    },
    "1103": {
        "intro": """The Fence Picket Calculator determines how many pickets, posts, and rails you need for any length of wooden fence. Enter your fence length, picket dimensions, gap between pickets, and post spacing to get an accurate materials list before visiting the lumber yard.""",
        "what_it_calculates": "total pickets needed, number of posts, number of rails, and total linear metres of timber.",
        "faqs": [
            ("What is the standard gap between fence pickets?", "20 mm (2 cm) is the most common gap for a privacy fence. Decorative and pool fences often use gaps of 50–100 mm. Picket-style (spaced) fences typically use gaps equal to the picket width. Enter your preferred gap into the calculator."),
            ("How deep should fence posts be set?", "As a rule: bury at least one-third of the post length. For a 1.8 m fence, use 2.4 m posts set 600 mm into the ground. In soft or wet soil, increase burial depth or use concrete footings."),
            ("Should I use 2 or 3 rails?", "2 rails are standard for fences up to 1.2 m high. 3 rails are recommended for fences over 1.5 m. The calculator assumes 2 rails per span — adjust manually if you need 3."),
            ("How do I account for a gate?", "Subtract the gate opening width from your fence length before calculating. A standard gate is 0.9 m wide (single) or 1.8 m wide (double). Add the gate frame separately."),
            ("What type of wood is best for outdoor fencing?", "Pressure-treated pine is the most economical choice. Cedar and redwood are naturally rot-resistant but more expensive. Always coat cut ends with preservative, especially post bottoms.")
        ]
    },
    "1104": {
        "intro": """The Roofing Shingle Calculator works out how many bundles of shingles you need based on your roof's footprint dimensions and pitch. It automatically applies the pitch correction factor to convert your floor-level measurements to actual sloped roof area — the step most DIYers skip.""",
        "what_it_calculates": "actual roof area in m², number of roofing squares (1 square = 9.29 m²), bundles needed, and waste percentage.",
        "faqs": [
            ("What is a 'roofing square'?", "A roofing square is 100 square feet (9.29 m²) of roof surface area — it's the standard unit for ordering shingles in North America. Most shingles come in bundles of 33, and 3 bundles cover 1 square."),
            ("How does roof pitch affect shingle quantity?", "The steeper the pitch, the more actual surface area there is versus the floor footprint. A 4/12 pitch needs about 5% more material than a flat roof; an 8/12 pitch needs 20% more. The calculator applies this correction automatically."),
            ("How much waste should I add?", "The calculator adds 10% by default. For roofs with valleys, hips, skylights, or chimneys, add 15–20%. Waste comes from cutting shingles around penetrations and at ridge lines."),
            ("How many shingles are in a bundle?", "Standard 3-tab shingles: 33 per bundle. Architectural/laminate shingles: 20–26 per bundle depending on brand. Enter your actual bundle size into the calculator for accurate results."),
            ("Can I use this calculator for metal or tile roofing?", "The area calculation is universal. However, metal roofing is ordered by the panel or square metre, and clay/concrete tiles have their own coverage rates. Divide your calculated area by the coverage per panel or tile.")
        ]
    },
    "1105": {
        "intro": """The Insulation Batt Calculator determines how many rolls of insulation you need to fill wall or ceiling cavities between studs. Enter your wall dimensions, stud spacing, and roll size to get an accurate roll count — preventing both costly over-ordering and mid-project supply shortages.""",
        "what_it_calculates": "total wall area in m², number of rolls needed, coverage per roll, and total linear metres.",
        "faqs": [
            ("What width insulation do I need for my wall?", "Standard stud spacings are 400 mm (16 in) or 600 mm (24 in) on centre. Insulation batts are manufactured to fit snugly: 380 mm wide for 400 mm studs, 570 mm wide for 600 mm studs. Always match batt width to your actual stud spacing."),
            ("What R-value do I need?", "R-value requirements depend on climate and building location (wall, floor, or roof). Typical European requirements: R-2 to R-4 for walls, R-4 to R-8 for roofs. Higher R-value batts are thicker and require deeper stud cavities."),
            ("Do I need a vapour barrier?", "In most climates, a vapour retarder on the warm side of the insulation is recommended to prevent moisture migration into the wall cavity. Check local building regulations."),
            ("How do I insulate around windows and doors?", "Cut batts to fit and compress them gently into the gap around framing. Use spray foam for small gaps and irregular shapes. Do not compress batts aggressively — compression reduces their R-value."),
            ("Can insulation batts go on top of existing insulation?", "Yes, for attic top-up. Lay new rolls perpendicular to the existing ones to bridge gaps and increase thermal resistance. Do not use faced batts on top of existing insulation — the facing can trap moisture.")
        ]
    },
    "1106": {
        "intro": """The Carpet Calculator estimates how many linear metres of carpet you need to purchase from a roll of a given width. Unlike simple area calculators, it accounts for the roll width constraint — meaning you may need more carpet than the room area suggests when the room is wider than the roll.""",
        "what_it_calculates": "room area in m², square yards, linear metres needed from the roll, and waste percentage.",
        "faqs": [
            ("Why do I need more than the room area in linear metres?", "Carpet comes on rolls of fixed width (typically 3.66 m / 12 ft). If your room is 4 m wide, you must use a length of carpet that covers the full 4 m — you can't join two strips side by side without a visible seam. The excess from the narrower dimension is waste."),
            ("What carpet roll widths are available?", "Standard widths are 3.66 m (12 ft) in the US/UK, and 4 m in Europe. Wider rolls reduce seaming needs but increase waste in smaller rooms. Some specialty carpets come in 2 m or 5 m widths."),
            ("How do I handle pattern matching?", "Each strip must be cut to align the pattern, wasting the excess from the top of each drop. A 64 cm repeat in a room requiring 10 strips wastes up to 6.4 m of carpet. The calculator accounts for this with the pattern repeat input."),
            ("Does carpet direction matter?", "Yes — cut pile carpets must all face the same direction or they will look different shades in raking light. Always run strips in the same direction and confirm with your installer."),
            ("Can I calculate carpet for stairs?", "Use a separate calculation for stairs: measure one tread + one riser + 5 cm for fitting per step, multiply by number of steps, then divide by carpet width to get linear metres.")
        ]
    },
    "1107": {
        "intro": """The Laminate Flooring Calculator tells you exactly how many planks and boxes of laminate you need for a room. It computes the room area, applies a 10% waste factor for cuts and offcuts, and divides by the planks-per-box count to give you a direct trip to the shop with the right quantity.""",
        "what_it_calculates": "room area in m², total planks needed, boxes to purchase, and waste percentage.",
        "faqs": [
            ("Why is 10% waste added?", "The last plank in each row must be cut to length. The offcut starts the next row only if it's longer than 30 cm; otherwise it's wasted. Additionally, door frames and obstacles require cuts. Diagonal layouts waste 15–20% due to angle cuts."),
            ("How do I measure a room with alcoves or recesses?", "Break the floor into rectangles, calculate each, and add them together. Include the full area under door frames (laminate runs under the door stop, not up to it)."),
            ("Do I need underlay?", "Yes — laminate flooring requires an underlay for acoustic dampening, moisture protection, and subfloor levelling. Underlay comes in rolls (typically 15–20 m²/roll) and is ordered separately."),
            ("How many planks are in a box?", "It varies by plank size and brand. Typical packs contain 6–10 planks covering 1.5–2.5 m². Always enter your specific pack size into the calculator — don't guess."),
            ("Can I reuse leftover planks from a previous job?", "Only if they're from the same production batch (check the batch number on the box). Different batches can have slight colour or thickness variations that will be visible at the join.")
        ]
    },
    "1108": {
        "intro": """The Countertop Calculator estimates the slab area needed for kitchen or bathroom countertops, including the backsplash. Enter your counter length, depth, backsplash height, and number of sink or hob cutouts to get the net slab area and an estimated material cost.""",
        "what_it_calculates": "counter surface area in m², total linear metres, backsplash area in m², and estimated cost.",
        "faqs": [
            ("What is the standard countertop depth?", "600 mm (60 cm) is the most common depth for kitchen worktops to align with standard base cabinets. Bathroom vanity tops are typically 450–500 mm deep. Island countertops can extend to 900 mm–1200 mm for seating overhangs."),
            ("How much overhang should I allow for seating?", "A standard breakfast bar overhang is 250–300 mm. Knee clearance of at least 200 mm from the cabinet face is needed for comfortable seating. Overhangs greater than 300 mm require a structural support bracket."),
            ("What slab size do stone fabricators work with?", "Standard granite and quartz slabs are 3000 × 1400 mm or 3200 × 1600 mm. Large kitchens may need two slabs — the join should be planned at a natural break such as a corner. Confirm slab size with your fabricator before finalising the design."),
            ("How many cutouts can one slab accommodate?", "Most fabricators can make 2–3 cutouts per slab (sink, hob, tap hole). Cutouts weaken the slab, so each needs a minimum of 100 mm from the slab edge. Complex cutouts increase fabrication time and cost."),
            ("What is the difference between slab area and running metres?", "Running metres (linear metres) measures the length of counter edge — used for pricing edge profiles and upstands. Slab area (m²) is used for material cost. Both are shown in the results.")
        ]
    },
    "1109": {
        "intro": """The Backsplash Tile Calculator works out how many tiles and boxes you need for a kitchen or bathroom backsplash wall. Enter the wall dimensions, tile size in centimetres, and any window openings to get an accurate order — including the 10% waste typically needed for cuts around outlets and edges.""",
        "what_it_calculates": "wall area in m², total tiles needed, boxes to purchase, and waste percentage.",
        "faqs": [
            ("What tile size is most common for backsplashes?", "Subway tiles (7.5 × 15 cm or 10 × 20 cm) are the classic choice. Large format tiles (30 × 60 cm) are increasingly popular — they have fewer grout lines and look more contemporary. Mosaic tiles (2.5 × 2.5 cm sheets) require significantly more grout and cutting time."),
            ("How many tiles are in a box?", "It varies enormously: a box of 10×20 cm subway tiles might contain 50 tiles covering 1 m², while 60×30 cm tiles might be 8 per box covering 1.44 m². Always check the coverage stated on the box label."),
            ("Should I account for outlet cutouts?", "Yes — each electrical outlet or switch plate requires a tile cut. The calculator's 'window openings' field subtracts rectangular areas, but add 5% extra manually for individual outlet cuts."),
            ("What's the difference between wall tile and floor tile?", "Wall tiles are thinner and lighter (not rated for foot traffic). They should not be used on floors. Floor tiles can be used on walls but are heavier and may require stronger adhesive."),
            ("How high should a kitchen backsplash be?", "Standard backsplash height is from the countertop to the bottom of the upper cabinets — typically 45–60 cm. Full-height backsplashes from counter to ceiling are increasingly popular and easier to clean.")
        ]
    },
    "1110": {
        "intro": """The Grout Calculator computes the kilograms of grout needed for any tiled area based on tile dimensions and joint width. It's far more accurate than guessing from tile count — because grout quantity depends on joint width and tile thickness, not just area. Get the right number of bags before you mix anything.""",
        "what_it_calculates": "grout required in kg, 5 kg bags needed, 10 kg bags needed, and coverage per kg.",
        "faqs": [
            ("What width grout joint should I use?", "Less than 3 mm: use unsanded (non-sanded) grout. 3–12 mm: use sanded grout. Over 12 mm: use epoxy or specialty grout. Wall tiles: 2–3 mm joint typical. Floor tiles: 3–5 mm for indoor, 5–10 mm for outdoor pavers."),
            ("How long does grout last?", "Standard cement grout: 5–10 years before needing re-grouting in wet areas. Epoxy grout: 20+ years, highly stain-resistant. Coloured grout fades faster in areas with UV exposure."),
            ("What is epoxy grout and when should I use it?", "Epoxy grout uses a two-part resin system instead of cement. It's stain-proof, waterproof, and chemical-resistant — ideal for commercial kitchens, showers, and pool surrounds. It's more expensive and harder to apply correctly."),
            ("How do I seal grout?", "Allow grout to cure for at least 72 hours. Apply a penetrating sealer with a brush or roller, let it soak in for 5–10 minutes, then wipe off the excess. Reseal annually in wet areas (showers, around sinks)."),
            ("Can I tile over existing grout?", "Only if the existing tiles and grout are fully bonded, level, and clean. Remove loose or crumbling grout first. You cannot apply new tiles directly over old grout lines — the new tile will sit proud and the bond will be weak.")
        ]
    },
    "1111": {
        "intro": """The Paint Coverage Calculator tells you exactly how many litres of paint you need for any room — accounting for the number of coats, doors and windows to skip, and the coverage rate of your chosen paint type. Stop guessing at the paint shop and stop mid-job trips to buy more.""",
        "what_it_calculates": "paintable wall area in m², litres needed, gallons needed, and number of 5L cans to buy.",
        "faqs": [
            ("How many m² does a litre of paint cover?", "Standard emulsion: 10–12 m² per litre. Masonry paint: 5–8 m² per litre (porous surfaces absorb more). Gloss or satinwood: 12–16 m² per litre. Check your specific tin — coverage rates vary by brand and finish."),
            ("How many coats do I need?", "Two coats are standard for most repaints. Three coats are needed when: painting over a dark colour with a lighter shade, covering fresh plaster (the first coat seals, the second covers), or using heavily diluted paint."),
            ("Should I include the ceiling in this calculation?", "This calculator is for walls only. Calculate the ceiling separately: it's simply length × width. Ceiling paint has a higher coverage rate than wall paint — typically 10–14 m²/L."),
            ("What is the difference between a primer and an undercoat?", "A primer penetrates and seals the surface (used on bare wood, new plaster, or stained surfaces). An undercoat provides opacity and adhesion before the topcoat. Many modern paints are 'primer and undercoat in one', suitable for repaints over sound surfaces."),
            ("How do I measure an irregular room?", "Measure all walls individually (length × height), add them together, then subtract door and window areas. For sloped ceilings in loft rooms, measure the sloped wall area using the actual sloped length, not the horizontal projection.")
        ]
    },
    "1112": {
        "intro": """The Wallpaper Calculator works out how many rolls of wallpaper you need for a room, correctly accounting for the usable number of drops (strips) per roll after matching the pattern repeat. This is the step where most people underestimate — pattern repeat can waste an entire strip per roll.""",
        "what_it_calculates": "total wall area in m², rolls needed, strips per roll, and waste percentage.",
        "faqs": [
            ("What is a pattern repeat and why does it matter?", "A pattern repeat is the vertical distance before the pattern repeats. When hanging multiple strips, each new strip must be cut to align with the previous strip's pattern — the excess is waste. A 64 cm repeat in a 2.5 m room means only 3 usable strips per 10 m roll instead of 4."),
            ("What is a standard wallpaper roll size?", "Most European rolls are 10 m long × 530 mm (53 cm) wide. US rolls are typically 27 ft (8.2 m) long × 20.5 in (52 cm) wide. Always enter your specific roll size — it varies significantly by brand."),
            ("Should I buy extra rolls?", "Always buy 1–2 extra rolls from the same batch (batch number is on the label). Colours can vary between batches, and if you need to patch damage later, you need an exact match. Unused rolls can often be returned."),
            ("How do I hang wallpaper correctly?", "Hang from a true vertical plumb line 1 roll-width from the focal wall (usually opposite the window or door). Work away from natural light to disguise joins. Use appropriate adhesive for your paper weight (heavy papers need stronger paste)."),
            ("Can I wallpaper over existing wallpaper?", "Generally no — the added weight can cause both layers to peel. Existing paper should be stripped. Exception: if the existing paper is firmly bonded smooth lining paper, some decorators hang directly over it.")
        ]
    },
    "1113": {
        "intro": """The Crown Moulding Calculator computes how many linear metres and pieces of crown moulding you need for a room. It measures the room perimeter, adds 10% for mitre waste, and divides by the standard moulding length to give you an exact piece count for the lumber yard.""",
        "what_it_calculates": "room perimeter in m, linear metres needed with waste, pieces needed, and corner pieces required.",
        "faqs": [
            ("How much extra should I add for mitre cuts?", "The calculator adds 10% as a default. For rooms with many inside corners (L-shaped rooms, bay windows), consider 12–15%. Each inside corner wastes a small amount from both joining pieces."),
            ("What is the difference between crown and cove moulding?", "Crown moulding has a complex spring-angle profile that projects away from the wall and ceiling surface. Cove moulding is a simpler concave curve that sits flat against the wall and ceiling junction. Crown is more dramatic and requires more skill to cut accurately."),
            ("How do I cut crown moulding corners?", "Crown corners use compound mitre cuts: the saw blade tilts to match the spring angle, and the fence angle matches the wall angle. Most walls meet at 90°, requiring 45° cuts. Use a crown stop jig or a compound mitre saw set to the manufacturer's spring angle specification."),
            ("Can I paint crown moulding before or after installation?", "Both approaches work. Pre-painting saves masking effort but requires touching up nail holes and caulked gaps after installation. Many professionals install first, caulk all gaps, then paint — this gives the cleanest finish."),
            ("What nails or adhesive should I use?", "Use 50–65 mm finish nails for structural attachment, driving into the top plate and the wall studs or blocking. Construction adhesive on the back of the moulding reduces the number of nails needed and helps with ceiling contact.")
        ]
    },
    "1114": {
        "intro": """The Baseboard Calculator tells you how many linear metres and individual boards you need for skirting boards around any room. It subtracts door openings from the perimeter, adds 5% for cuts, and divides by the board length you're purchasing.""",
        "what_it_calculates": "net room perimeter in m, linear metres needed with waste, boards to purchase, and return pieces.",
        "faqs": [
            ("How tall should baseboards be?", "Standard baseboard height is 70–90 mm for rooms with 2.4 m ceilings. For rooms with high ceilings (2.7 m+), 100–150 mm looks proportional. Taller baseboards are more expensive but dramatically improve the finished look of a room."),
            ("Do I need to include inside corners in the waste estimate?", "Yes — inside corners require a coped joint (one piece cut at a profile angle to sit against the other). This wastes 50–100 mm per inside corner. The 5% waste factor covers this for typical rooms with 4 corners."),
            ("What is the difference between MDF and solid wood baseboard?", "MDF (medium-density fibreboard) is cheaper, takes paint perfectly, and won't split or warp. It cannot be stained (use solid wood for a stained finish). MDF is the professional's choice for painted rooms."),
            ("Do I need to remove old baseboards before tiling or flooring?", "Yes for flooring — new floor goes in first, then baseboards are installed on top to cover the expansion gap. Yes for tile — tiles should go under the baseboard, not be cut to the baseboard face."),
            ("How do I attach baseboards without a nail gun?", "Construction adhesive plus 2–3 finish nails per board is the reliable method. Apply adhesive to the back, nail at each stud location, then fill nail holes and caulk the top gap before painting.")
        ]
    },
    "1115": {
        "intro": """The Drywall Calculator estimates how many sheets of drywall (plasterboard) you need for a wall or ceiling, along with the joint compound (mud) and tape quantities. It applies an 8% waste factor for cuts around outlets, windows, and edges.""",
        "what_it_calculates": "wall area in m², sheets needed, joint compound in kg, tape in metres, and screw count.",
        "faqs": [
            ("What size drywall sheet should I use?", "Standard sheets are 1200 × 2400 mm (2.88 m²) or 1200 × 3000 mm (3.6 m²). For walls exactly 2.4 m high, vertical 2400 mm sheets are standard. For ceilings, 2400 mm or 3000 mm sheets run perpendicular to the joists."),
            ("What thickness drywall should I use?", "9.5 mm (3/8 in): ceilings only, curved surfaces. 12.5 mm (1/2 in): standard wall application — the most common. 15.9 mm (5/8 in): fire-rated walls, soundproofing. Two layers of 12.5 mm provide a fire-rated assembly."),
            ("How many screws per sheet?", "Approximately 32 screws per sheet for a standard wall application: screws every 300 mm along studs at 600 mm centres. The calculator estimates 11 screws/m² as a guide figure."),
            ("What joint compound (mud) do I need?", "All-purpose compound is suitable for the full taping process. Pre-mixed tubs are easier to use; powder compounds require mixing and have longer shelf life. Plan for 0.4–0.6 kg per m² of finished drywall for all coats combined."),
            ("Can drywall be used in bathrooms?", "Standard drywall absorbs moisture — use moisture-resistant (green board) or cement board (Hardiebacker) behind tiles and in wet areas. Standard drywall can be used for bathroom ceilings if properly ventilated and painted with moisture-resistant paint.")
        ]
    },
    "1116": {
        "intro": """The Concrete Steps Calculator designs a safe, proportioned staircase from your total rise and run dimensions. It computes the number of steps, individual riser and tread measurements, stringer length, and the concrete volume needed — ensuring your steps meet the 2R+T=63 cm ergonomic rule.""",
        "what_it_calculates": "number of steps, tread depth in cm, stringer length in m, and concrete volume in m³.",
        "faqs": [
            ("What is the ergonomic rule for step proportions?", "The standard comfort formula is 2 × riser + tread = 63 cm (the Blondel formula). Typical comfortable risers are 15–18 cm with treads of 27–33 cm. Steps steeper than 20 cm riser feel ladder-like; treads shallower than 25 cm feel dangerous."),
            ("How much concrete do I need for 5 steps?", "The concrete volume is roughly half the prismatic volume of the staircase block. For 5 steps of 1.2 m width, 18 cm rise, and 36 cm tread: approximately 0.2–0.3 m³ — about half a ready-mix truck. Add 15% for waste and formwork variations."),
            ("Do I need rebar in concrete steps?", "Yes for steps over 1 m wide or more than 3 steps: use 10 mm rebar at 200 mm centres, tied at intersections. Unreinforced steps crack and chip at the front nose. For small garden steps (2–3 steps, narrow width), plain concrete may suffice."),
            ("How long should concrete steps cure before use?", "Foot traffic: 24–48 hours at minimum. Vehicle load: 7 days. Full strength: 28 days. Keep concrete moist for the first 7 days to prevent surface cracking — cover with plastic sheeting or wet hessian."),
            ("What is the minimum tread width for outdoor steps?", "600 mm is the absolute minimum for single-person use. 900 mm is comfortable for one person with bags. 1200 mm allows two people to pass. Public steps and building codes typically require 1500 mm minimum.")
        ]
    },
    "1117": {
        "intro": """The Retaining Wall Calculator determines how many blocks you need and how much drainage gravel to order for a segmental concrete block retaining wall. It also estimates the required base depth and drainage pipe length — the structural elements that determine whether your wall stays standing.""",
        "what_it_calculates": "number of blocks, gravel in tonnes, recommended base depth in cm, and drainage pipe length in m.",
        "faqs": [
            ("How deep does the base course need to be buried?", "As a rule: bury one block deep for every 1 m of exposed wall height, minimum one full block course. For a 0.9 m wall, bury one 20 cm course = 20 cm below grade. This prevents toe failure and frost heaving."),
            ("When is a retaining wall considered a structural wall requiring engineering?", "Most building codes require a structural engineer's design for walls over 1.0–1.2 m in exposed height, walls retaining sloped soil (surcharge), or walls near buildings, roads, or other structures. Always check local regulations."),
            ("What drainage goes behind a retaining wall?", "Install a 100 mm perforated drain pipe at the base of the wall, wrapped in geotextile fabric, set in 200–300 mm of clean crushed drainage gravel (10–20 mm size). Extend the pipe to daylight at each end of the wall. Without drainage, water pressure builds and topples the wall."),
            ("What is the batter (tilt) of a retaining wall?", "Segmental retaining walls are designed with a slight rearward lean (batter) of typically 12–25 mm per course (setback). This counteracts lateral soil pressure and gives the wall structural stability. Always follow the block manufacturer's recommended setback."),
            ("Can I plant on top of a retaining wall?", "Yes, if the wall is designed for the additional surcharge load. Wet soil is heavier than dry soil — a fully saturated 300 mm planting bed adds 480 kg/m² of pressure. Trees near walls create root pressure over time.")
        ]
    },
    "1118": {
        "intro": """The Paver Calculator estimates how many paving stones you need for any outdoor area, along with the gravel base and bedding sand quantities. Getting the base right is as important as the pavers themselves — a properly compacted base prevents settling, cracking, and drainage problems for years.""",
        "what_it_calculates": "paved area in m², pavers needed, base gravel in tonnes, and bedding sand in kg.",
        "faqs": [
            ("What thickness gravel base do I need?", "Minimum 100 mm (10 cm) for pedestrian areas. 150–200 mm for driveways. The gravel must be compacted in 100 mm lifts with a plate compactor — do not compact more than 100 mm at once or the bottom won't be reached."),
            ("How thick is the sand bedding layer?", "30 mm (3 cm) of coarse bedding sand over the compacted gravel base is standard. After compacting the pavers, the sand will compact to approximately 25 mm. Do not use fine or silty sand — it washes away; use sharp angular grit sand."),
            ("What paver pattern should I choose?", "Running bond (offset rows): easy to lay, recommended for beginners. Herringbone (45° or 90°): structurally strongest, recommended for driveways. Random stack: easiest but weakest pattern. Herringbone patterns require ~10% more material for edge cuts."),
            ("How do I cut pavers?", "Angle grinder with a diamond blade for straight cuts. Wet-cut table saw for precise straight cuts in quantity. Hire a block splitter for straight cuts in natural stone. Always wear eye protection and a dust mask."),
            ("Do I need edge restraints?", "Yes — without edge restraints, the outer pavers will gradually shift outward and the pattern will open up. Use concrete haunching, metal or plastic edging, or a soldier course set in mortar around the perimeter.")
        ]
    },
    "1119": {
        "intro": """The Landscape Rock Calculator determines how many tonnes of decorative rock, crushed stone, or gravel you need for a garden bed, path, or drainage area. Different rock types have different densities — the calculator converts your volume into tonnes for when you order by weight from the quarry or landscape supplier.""",
        "what_it_calculates": "area in m², volume in m³, tonnes needed, and volume in cubic yards.",
        "faqs": [
            ("How deep should decorative rock be applied?", "50–80 mm (5–8 cm) is the minimum for effective weed suppression. Less than 5 cm and weeds push through or are visible through the gaps. More than 10 cm is wasteful unless you need drainage depth. Install landscape fabric underneath for best weed control."),
            ("What rock type is best for drainage?", "20–40 mm clean (washed) crushed stone or pea gravel allows water to percolate freely and won't pack down. Avoid crusher run (crushed stone with fines) for drainage — it compacts and blocks water flow. Use it for base layers only."),
            ("How much does a tonne of gravel cover?", "At 80 mm depth: approximately 0.65–0.75 m² per tonne for standard crushed limestone. At 50 mm depth: approximately 1.0–1.2 m² per tonne. The exact coverage depends on rock density and void space."),
            ("Can I install rock over existing grass?", "Remove all grass and weeds first — grass will grow through decorative rock within one season. Use a chemical weed killer, wait 2 weeks, then scalp the lawn, compact the soil, lay landscape fabric, and apply rock."),
            ("What is the difference between gravel, crushed stone, and pea gravel?", "Gravel: naturally rounded, washed. Crushed stone: angular, produced by crushing quarried rock — better for driveways as it interlocks. Pea gravel: small (8–12 mm) rounded stones — comfortable for bare feet, good for play areas. River rock: large (50–200 mm) polished stones — decorative only.")
        ]
    },
}

def build_html(cid: str, calc: dict, ci18n: dict, content: dict) -> str:
    name = ci18n.get("name", f"Calculator {cid}")
    slug = calc.get("slug", cid)
    intro = content["intro"]
    what = content.get("what_it_calculates", "")
    steps = calc.get("steps", [])
    mistakes = calc.get("mistakes", [])
    formula = calc.get("formula_display", "")
    example = calc.get("example_inputs", {})
    result_ctx = calc.get("result_context", "")
    faqs = content.get("faqs", [])

    lines = [f'<section class="long-content">']
    lines.append(f'  <h2>What is the {esc(name)}?</h2>')
    lines.append(f'  <p>{esc(intro)}</p>')
    if what:
        lines.append(f'  <p>It calculates: {esc(what)}</p>')

    # How to use
    inputs_i18n = ci18n.get("inputs", {})
    input_names = list(inputs_i18n.keys())
    lines.append(f'\n  <h2>How to Use This Calculator</h2>')
    lines.append(f'  <ol>')
    for k in input_names:
        label = inputs_i18n.get(k, k)
        lines.append(f'    <li>Enter your <strong>{esc(label)}</strong>.</li>')
    lines.append(f'    <li>Click <strong>Calculate</strong> to see instant results.</li>')
    lines.append(f'  </ol>')

    # Formula
    if formula:
        lines.append(f'\n  <h2>Formula</h2>')
        lines.append(f'  <p>The calculator uses this formula:</p>')
        lines.append(f'  <pre class="formula-block">{esc(formula)}</pre>')

    # Worked example
    if steps:
        lines.append(f'\n  <h2>Worked Example</h2>')
        if example:
            ex_vals = ", ".join(f"{k} = {v}" for k, v in example.items())
            lines.append(f'  <p>Using typical values ({esc(ex_vals)}):</p>')
        lines.append(f'  <ol>')
        for s in steps:
            lines.append(f'    <li>{esc(s)}</li>')
        lines.append(f'  </ol>')
        if result_ctx:
            lines.append(f'  <p><strong>Result summary:</strong> {esc(result_ctx)}</p>')

    # Common mistakes
    if mistakes:
        lines.append(f'\n  <h2>Common Mistakes to Avoid</h2>')
        lines.append(f'  <ul>')
        for m in mistakes:
            lines.append(f'    <li>{esc(m)}</li>')
        lines.append(f'  </ul>')

    # FAQs
    if faqs:
        lines.append(f'\n  <h2>Frequently Asked Questions</h2>')
        lines.append(f'  <div class="faq-list">')
        for q, a in faqs:
            lines.append(f'    <div class="faq-item">')
            lines.append(f'      <button class="faq-q" aria-expanded="false">{esc(q)}</button>')
            lines.append(f'      <div class="faq-ap"><p>{esc(a)}</p></div>')
            lines.append(f'    </div>')
        lines.append(f'  </div>')

    lines.append(f'</section>')
    return "\n".join(lines)


updated = 0
for cid, content in CONTENT.items():
    calc = calcs.get(cid)
    ci18n = calcs_i18n.get(cid, {})
    if not calc:
        print(f"  [SKIP] calc {cid} not found")
        continue
    html = build_html(cid, calc, ci18n, content)
    out_path = CONTENT_DIR / f"{cid}.html"
    out_path.write_text(html, encoding="utf-8")
    size = len(html.encode("utf-8"))
    print(f"  [OK] {cid} -> {size:,} bytes")
    updated += 1

print(f"\n[DONE] Rewrote {updated} content files")
