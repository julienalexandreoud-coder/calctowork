"""Rewrite the 17 thin content files (1103-1119) with rich, specific HTML."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "src" / "content" / "en"
CALCS_JSON = ROOT / "src" / "calculators" / "calculators.json"
I18N_EN = ROOT / "src" / "i18n" / "en.json"

data = json.loads(CALCS_JSON.read_text(encoding="utf-8"))
calcs_by_id = {c["id"]: c for c in data["calculators"]}
i18n = json.loads(I18N_EN.read_text(encoding="utf-8"))
calcs_i18n = i18n.get("calculators", {})

# Rich content per calc: (intro, use_cases, pro_tip, faqs[5])
CONTENT = {
    "1103": {
        "name": "Fence Picket Calculator",
        "intro": "Planning a fence project without doing the math first is one of the costliest mistakes in DIY construction. Buy too few pickets and the project stalls; buy too many and you waste money on lumber that sits in your garage. The Fence Picket Calculator eliminates that guesswork — enter your fence length, picket width, gap size, and post spacing, and instantly get the exact number of pickets and posts you need, including recommended waste allowance.",
        "who": "homeowners installing privacy fences, contractors bidding fence jobs, and landscapers specifying materials for clients",
        "example": "A 30-metre backyard fence using 9 cm wide pickets with a 1 cm gap and posts every 2.4 m needs <strong>273 pickets</strong> and <strong>14 posts</strong>.",
        "tip": "Add 5–10% to the picket count for cuts, warped boards, and future repairs. Cedar and pressure-treated pine are the most common choices — cedar is naturally rot-resistant, pine needs treatment but costs less.",
        "faqs": [
            ("How do I calculate pickets per section?", "Divide the post spacing by the sum of picket width plus gap. For a 2.4 m section with 9 cm pickets and 1 cm gaps: 240 ÷ (9+1) = 24 pickets per section."),
            ("What gap should I leave between fence pickets?", "A 1–2 cm gap is standard for privacy fences. Larger gaps (3–5 cm) give a more open, decorative look and allow more airflow, which helps prevent wood rot."),
            ("How many fence posts do I need?", "Posts go at each end and every 1.8–2.4 m in between. The formula is: (fence length ÷ post spacing) + 1, rounded up. A 30 m fence with 2.4 m spacing needs 14 posts."),
            ("Does the calculator account for corner posts?", "Yes — corner posts are counted in the total. Add one extra post for every 90-degree corner in your fence layout, then add gate posts in pairs (one per gate side)."),
            ("What is the standard height for a privacy fence?", "1.8 m (6 feet) is the most common privacy fence height in residential areas. Check your local council or HOA rules before building — many have maximum height limits."),
        ],
    },
    "1104": {
        "name": "Roofing Shingle Calculator",
        "intro": "Ordering the wrong amount of roofing shingles is an expensive mistake — shingles are sold in bundles and squares, and prices vary widely. Too few and the job stops mid-roof; too many and you're paying for materials you'll never use. The Roofing Shingle Calculator accounts for your roof's actual pitch using the pitch factor formula, so you get an accurate bundle count for sloped roofs of any angle.",
        "who": "homeowners re-roofing a house, roofers estimating material costs, and contractors preparing bids",
        "example": "A roof that is 12 m long × 8 m wide with a 6/12 pitch has a pitch factor of 1.118, giving an actual area of 107 m². That requires approximately <strong>35 bundles</strong> (3 bundles per square, where 1 square = 9.29 m²).",
        "tip": "Always order 10–15% extra for waste, ridge caps, hips, and valleys. Shingles from the same production run have matching colour — mixing runs can cause visible colour differences.",
        "faqs": [
            ("What is a roofing square?", "A roofing square equals 100 square feet (about 9.29 m²). Most shingles come 3 bundles per square, though premium architectural shingles may need 4 bundles per square."),
            ("How does roof pitch affect material quantities?", "Steeper roofs have more actual surface area than their footprint suggests. A 12/12 pitch (45°) requires 41% more shingles than a flat area of the same floor dimensions."),
            ("What is the pitch factor and how is it calculated?", "Pitch factor = √(1 + (pitch/12)²). For a 6/12 pitch: √(1 + 0.25) = 1.118. Multiply your floor area by this factor to get actual roof surface area."),
            ("Do I need to include the overhang in my measurements?", "Yes — measure the full roof surface including any eave overhang, not just the building footprint. Overhangs typically add 15–30 cm per side."),
            ("How long do asphalt shingles last?", "Standard 3-tab shingles last 20–25 years. Architectural (dimensional) shingles last 30–50 years. Metal roofing can exceed 50 years. Lifespan depends on climate, ventilation, and installation quality."),
        ],
    },
    "1105": {
        "name": "Insulation Batt Calculator",
        "intro": "Proper insulation is one of the highest-ROI home improvements you can make — the right amount can cut heating and cooling bills by 20–30%. But calculating how many insulation rolls or batts you need for walls, floors, or ceilings requires knowing the stud spacing, roll dimensions, and the 10% waste factor that most guides forget to mention. This calculator handles all of it automatically.",
        "who": "homeowners insulating a new build or retrofit, builders specifying insulation for a project, and energy auditors calculating upgrade requirements",
        "example": "A 15 m × 2.4 m wall section with 600 mm stud spacing using rolls that are 600 mm wide × 2.4 m long requires <strong>28 rolls</strong> including the 10% waste allowance.",
        "tip": "Match the insulation width to your stud spacing exactly — 400 mm batts for 400 mm centres, 600 mm for 600 mm centres. Batts that are too narrow leave cold gaps; too wide and they compress, reducing R-value.",
        "faqs": [
            ("What R-value do I need?", "R-value requirements depend on your climate zone and building element. As a guide: walls typically need R2.0–R2.5, ceilings R3.5–R6.0, and underfloor R1.5–R2.5 in temperate climates. Cold climates need higher values."),
            ("What is the difference between batts and rolls?", "Batts are pre-cut to standard lengths (usually 1.2 m or 2.4 m) for easy installation between studs. Rolls are continuous and can be cut to length — better for irregular spaces and large open areas like attics."),
            ("Why add a 10% waste factor?", "Insulation must be cut around electrical outlets, pipes, and structural members. Off-cuts from windows and doors also generate waste. 10% is the industry standard; add 15% for complex layouts."),
            ("Can I double up insulation layers for more R-value?", "Yes — stacking two layers of R2.0 gives R4.0. In ceilings, you can lay a second layer perpendicular to the first to also eliminate thermal bridging at the joists."),
            ("How do I insulate around electrical boxes?", "Split the batt behind the box so it fills the wall cavity on both sides. Never compress insulation tightly behind a box — it creates a fire risk. Some codes require specific fire-rated insulation around recessed lights."),
        ],
    },
    "1106": {
        "name": "Carpet Calculator",
        "intro": "Carpet is sold by the linear metre from a roll of fixed width — usually 3.66 m or 4 m — which means you need to think about the room layout, not just the floor area. An irregular room or a carpet with a pattern repeat can significantly increase waste. This calculator converts your room dimensions and carpet roll width into the exact linear metres you need to order, including a seam adjustment factor.",
        "who": "homeowners replacing carpet, interior designers specifying flooring, and carpet retailers quoting jobs",
        "example": "A 5 m × 4 m room carpeted with a 4 m wide roll requires <strong>5.5 linear metres</strong> (with no pattern repeat). Adding a 30 cm pattern repeat increases this to about 6.1 linear metres.",
        "tip": "Always run carpet pile in the same direction throughout a room — rotating it creates visible shading differences. For L-shaped rooms, calculate each section separately and combine the totals.",
        "faqs": [
            ("Why is carpet sold in linear metres, not square metres?", "Carpet comes off a roll of fixed width. The supplier cuts you a length of that roll. The linear metre price multiplied by the roll width gives the effective price per square metre."),
            ("What carpet roll widths are available?", "The most common widths are 3.66 m (12 ft) and 4.57 m (15 ft) in the US/UK, and 4 m in metric markets. Some ranges come in 5 m rolls for large rooms."),
            ("How does pattern repeat affect carpet quantity?", "With a pattern repeat of 30 cm, each strip must be aligned to the pattern before cutting, adding waste. The longer the pattern repeat, the more waste. Plain or textured carpets have zero repeat."),
            ("Can I lay carpet over underlay?", "Yes — underlay is recommended under all broadloom carpet. It extends carpet life, improves comfort and insulation, and reduces noise. Calculate underlay area the same way as carpet area."),
            ("How much extra carpet should I order?", "Standard advice is 10% extra for seams, cuts, and future repairs. In rooms with many angles or alcoves, add 15%. Always save off-cuts for patch repairs."),
        ],
    },
    "1107": {
        "name": "Laminate Flooring Calculator",
        "intro": "Laminate flooring is sold in boxes containing a set number of planks — and once you start a job, finding an extra box from the same batch to match colour and texture is never guaranteed. This calculator tells you exactly how many planks and boxes you need for your room, applying the standard 10% waste factor for cuts, offcuts at walls, and future replacements.",
        "who": "DIY homeowners laying laminate, flooring contractors quoting jobs, and interior designers specifying materials",
        "example": "A 4 m × 3.5 m room using planks that are 1.2 m × 19 cm (8 planks/box) requires approximately <strong>22 boxes</strong> with 10% waste included.",
        "tip": "Acclimate laminate planks in the room for 48–72 hours before installation. This lets them expand or contract to the room's humidity and prevents buckling or gaps after laying.",
        "faqs": [
            ("Which direction should I lay laminate flooring?", "Laying planks parallel to the longest wall makes rooms look larger. Running them toward the main light source (a window) also looks most natural. Avoid running perpendicular to the main view."),
            ("What expansion gap do I need?", "Leave a 10–12 mm expansion gap around all walls, door frames, and fixed objects. This allows the floor to expand and contract with temperature and humidity changes. Cover the gap with skirting board."),
            ("Why add 10% waste?", "Cuts at walls, angles, and door frames produce off-cuts that are unusable. The last row often needs ripping to width. 10% is standard; add 15% for diagonal installation which creates more waste."),
            ("Can laminate flooring be laid over existing tiles or vinyl?", "Yes, if the existing floor is level (< 3 mm variation over 1.8 m), firm, and dry. Lay underlay on top. Very uneven floors must be levelled first with self-levelling compound."),
            ("How do I calculate for an L-shaped room?", "Split the L-shape into two rectangles, calculate each separately, then add the totals. Don't just calculate the bounding rectangle — you'll significantly overestimate material."),
        ],
    },
    "1108": {
        "name": "Countertop Calculator",
        "intro": "Countertop materials are priced per square metre and cut to size — getting the measurement wrong means either a costly gap or an expensive re-cut. This calculator computes the surface area of your countertops, optional backsplash, and subtracts cutouts for sinks and cooktops so you get an accurate quote-ready area in square metres.",
        "who": "kitchen renovators, stone fabricators quoting benchtops, and joinery companies estimating material costs",
        "example": "A kitchen with 4.5 m of counter at 60 cm depth, a 0.6 m backsplash height, and one 0.4 × 0.8 m sink cutout has a total surface area of <strong>3.38 m²</strong> of countertop plus <strong>2.7 m²</strong> of backsplash.",
        "tip": "Engineered stone (quartz) and granite are priced differently — get quotes in 'slab' pricing versus 'per m²'. For island benches, check whether the price includes waterfall edges, which add significant area.",
        "faqs": [
            ("What is the standard depth for kitchen countertops?", "600 mm (60 cm) is the standard depth for kitchen base cabinets and countertops in most countries. Bathroom vanities are typically 450–500 mm deep."),
            ("How is a countertop cutout calculated?", "Measure the external dimensions of the sink or cooktop and subtract that rectangle from the total counter area. This calculator does that automatically when you enter cutout dimensions."),
            ("What thickness of stone countertop should I use?", "20 mm (2 cm) is standard for laminate and quartz. 30 mm (3 cm) gives a more premium look and is common for granite. Thicker slabs are heavier and require stronger cabinet support."),
            ("Do I need a template made before ordering stone?", "Yes — for stone countertops, fabricators almost always create a physical or digital template on-site after cabinets are installed. Never order cut stone from measurements taken before cabinets are in place."),
            ("How much overhang should a breakfast bar have?", "A standard breakfast bar overhang is 250–300 mm for seating. This requires support underneath (corbels or brackets) if the overhang exceeds 150–200 mm for stone slabs."),
        ],
    },
    "1109": {
        "name": "Backsplash Tile Calculator",
        "intro": "A kitchen or bathroom backsplash is one of the most visible tiling jobs in a home — and one of the most material-intensive per square metre because of all the cuts around outlets, windows, and appliances. This calculator accounts for those openings and adds a 10% waste factor so your material order comes out right the first time.",
        "who": "homeowners tiling a kitchen or bathroom, tile setters quoting backsplash jobs, and interior designers specifying finishes",
        "example": "A 3.6 m kitchen backsplash that is 0.5 m high with one 0.3 × 0.3 m window opening and 15 cm × 15 cm tiles (12/box) needs <strong>8 boxes</strong> with waste included.",
        "tip": "Start tiling from the centre of the visible wall and work outward — this ensures cut tiles are symmetrical on both sides and the full tiles are at eye level.",
        "faqs": [
            ("What size tiles work best for a backsplash?", "Small mosaic tiles (5–7.5 cm) are classic and handle curves well. Medium subway tiles (7.5 × 15 cm) are very popular for kitchens. Large format tiles (30 cm+) create a modern look but require more precise walls and generate more cut waste."),
            ("How do I measure a backsplash with windows and outlets?", "Measure the full wall area (length × height), then subtract each opening. This gives the net tile area. The calculator does this automatically with the 'window openings' field."),
            ("What grout joint width should I use for backsplash tiles?", "2–3 mm joints are standard for subway tiles. Mosaic tiles on mesh backing have 2 mm joints pre-set. Larger tiles can use 3–5 mm joints. Rectified tiles can go as tight as 1 mm."),
            ("Do I need waterproof tile adhesive behind a kitchen backsplash?", "A standard cement-based tile adhesive is fine for kitchen backsplashes since they are not continuously wet. Bathrooms and shower areas need waterproof membrane systems behind the tiles."),
            ("How long does a backsplash tile job take?", "A standard kitchen backsplash (3–4 m) takes 1 day to tile and 24 hours for adhesive to cure, then another hour to grout. Total: 2 days from start to grouting, 3–4 days before use."),
        ],
    },
    "1110": {
        "name": "Grout Calculator",
        "intro": "Running out of grout mid-job means stopping to buy more — and the new batch may not match perfectly. The grout calculation formula accounts for tile size, joint width, tile thickness, and grout density to give you an accurate weight of grout powder needed in kilograms, ready to take to the hardware store.",
        "who": "tilers, DIY homeowners, and tile contractors calculating material quantities",
        "example": "A 20 m² floor of 30 × 30 cm tiles with 3 mm joints and 8 mm tile thickness requires approximately <strong>4.2 kg of grout</strong> powder.",
        "tip": "Epoxy grout is harder to work with but is stain-proof and chemical-resistant — ideal for kitchens and pool areas. Standard cement grout is easier for beginners but needs sealing annually in wet areas.",
        "faqs": [
            ("How is grout quantity calculated?", "The formula is: Grout (kg/m²) = 2 × (tile_L + tile_W) / (tile_L × tile_W) × joint_width × tile_thickness × grout_density. It accounts for the total joint volume per square metre."),
            ("What grout density should I use?", "Cement-based grout powder has a density of approximately 1.6–1.7 kg/litre. Epoxy grout systems vary — check the product data sheet. The calculator uses 1.6 as default."),
            ("Should I seal grout after installation?", "Yes — cement grout is porous and will stain without sealing. Apply a penetrating grout sealer 24–48 hours after installation. Re-seal annually in high-traffic or wet areas. Epoxy grout does not need sealing."),
            ("How long should I wait before grouting tiles?", "Wait at least 24 hours after tiling (48 hours for large format tiles) to allow the adhesive to cure. Walking on tiles before the adhesive is set can cause tiles to shift and joints to open up."),
            ("Can I mix different grout colours in one area?", "No — mixing grout colours creates an inconsistent look and different batches of the same colour can vary. Buy all the grout you need from the same production batch."),
        ],
    },
    "1111": {
        "name": "Paint Coverage Calculator",
        "intro": "A common DIY mistake is buying paint by guessing — either running short halfway through the second coat or ending up with cans you'll never use. This calculator measures the paintable wall area, subtracts doors and windows, and divides by your paint's coverage rate per litre to give you an exact purchase quantity by number of coats.",
        "who": "homeowners painting a room, professional painters quoting jobs, and property managers budgeting for interior refreshes",
        "example": "A 5 m × 4 m room with 2.7 m ceilings, 2 coats, one door, and two windows has about 43 m² of paintable surface. At 12 m²/litre coverage: <strong>3.6 litres</strong> needed, so buy <strong>two 2-litre tins</strong>.",
        "tip": "Dark colours and reds typically need 3 coats for full coverage, not 2. If you are painting dark over light or changing colour dramatically, use a tinted primer first — it reduces the number of topcoats needed.",
        "faqs": [
            ("What is standard paint coverage per litre?", "Most interior wall paints cover 10–14 m² per litre per coat. Quality paints are often at the higher end (13–16 m²/L). Exterior paints cover 8–12 m²/L. Primers typically cover 8–12 m²/L. Always check your specific product's data sheet."),
            ("Do I need to subtract doors and windows from my paint calculation?", "Yes — a standard door is about 1.8 m² and a window 1.5 m². This calculator lets you enter the number of each and deducts them automatically. Skipping this step overestimates paint by 10–20% in a typical room."),
            ("How many coats of paint should I apply?", "Two coats are standard for most interior repaint jobs. New plasterboard or a drastic colour change may need 3 coats. One coat is sufficient only for touch-ups or very similar colour-on-colour."),
            ("Should I paint walls or ceiling first?", "Always paint the ceiling first, then walls from top to bottom. This way any drips or spatters on the wall get covered when you paint the wall. Paint skirting boards last."),
            ("How do I calculate paint for a room with vaulted ceilings?", "For a triangular vault, add (0.5 × width × height of triangle) to the rectangular wall area below. For a curved vault, measure the arc length and multiply by the room length."),
        ],
    },
    "1112": {
        "name": "Wallpaper Calculator",
        "intro": "Wallpaper is one of the trickiest materials to estimate because pattern repeats create a lot of waste — a 60 cm repeat can add 20–30% to your material needs. This calculator converts your room dimensions and roll specs into the exact number of rolls to buy, accounting for both pattern repeat and the number of usable strips per roll.",
        "who": "homeowners wallpapering a room, interior designers specifying feature walls, and decorators quoting renovation jobs",
        "example": "A room with 14 m of wallpaperable perimeter, 2.5 m walls, using rolls that are 10 m long × 0.52 m wide with a 64 cm pattern repeat needs <strong>11 rolls</strong>.",
        "tip": "Buy all rolls from the same batch number — the number printed on the label. Different batches can have subtle colour differences that are invisible in-store but obvious on the wall.",
        "faqs": [
            ("How do I calculate wallpaper for a room with a pattern repeat?", "Each strip must be cut so the pattern aligns at eye level. This wastes the top or bottom of each strip. The usable length per strip = roll_length ÷ (ceiling_height + pattern_repeat). The calculator does this automatically."),
            ("What is a full drop versus half drop wallpaper pattern?", "A straight (full) drop means every strip starts at the same point in the pattern. A half drop means alternate strips are offset by half the repeat height. Half drop patterns generate more waste and need more rolls."),
            ("How wide are standard wallpaper rolls?", "Standard UK/European rolls are 52–53 cm wide. US rolls are typically 68 cm wide. Some designers offer 70–90 cm wide rolls. Always measure and enter the actual roll width — do not assume."),
            ("Can I wallpaper over existing wallpaper?", "Not recommended. Old wallpaper may bubble or peel when new paste is applied, and the added weight can cause both layers to fall. Strip the old paper first for best results."),
            ("How long does wallpaper paste need to soak?", "Most paste manufacturers recommend 3–5 minutes of soaking time on the pasted strip before hanging. Thicker wallpapers or those printed on non-woven backing may need longer. Over-soaking causes stretching."),
        ],
    },
    "1113": {
        "name": "Crown Molding Calculator",
        "intro": "Crown molding runs along the ceiling perimeter of a room, and ordering the right linear metres is critical — molding is sold in fixed lengths (typically 2.4 m or 3.6 m) and joins are visible if you use short off-cuts. This calculator computes the room perimeter, adds 10% for angled cuts and waste, and tells you how many lengths to buy.",
        "who": "homeowners installing crown molding, finish carpenters quoting trim jobs, and interior designers specifying millwork",
        "example": "A 5 m × 4 m room with 90-degree corners requires 18 m of molding perimeter. Adding 10% waste gives 19.8 m — so buy <strong>9 lengths</strong> of 2.4 m molding (21.6 m total).",
        "tip": "Use a compound mitre saw for crown molding corners — the dual-angle cuts are difficult to do accurately with a standard mitre box. For large rooms, use longer molding lengths to minimise joins.",
        "faqs": [
            ("How do I cut crown molding corners?", "Crown molding corners require compound mitre cuts — typically 45° mitre and 33.9° bevel for 90-degree inside/outside corners. A dedicated crown molding mitre setting on your saw makes this easier. Test cuts on scrap before cutting good stock."),
            ("What is the waste allowance for crown molding?", "10% is standard for rooms with 90-degree corners. Add 15–20% if the room has many corners or bay windows, since each corner requires angled cuts that waste material."),
            ("Should crown molding be nailed to studs or the top plate?", "Crown molding should be nailed at 45 degrees into both the ceiling and wall — hitting studs and ceiling joists where possible. Use a stud finder first. Finish nails (50–65 mm) with a nail gun give the cleanest result."),
            ("How do I fill gaps between crown molding and the wall?", "Use paintable latex caulk, not silicone. Apply a thin bead along the top and bottom edges, smooth with a damp finger, and paint after it dries. Small gaps (< 3 mm) are expected and easily caulked."),
            ("Can crown molding be installed on vaulted ceilings?", "Yes, but it requires raking crown molding that runs at the slope of the ceiling, not horizontal. The calculations are more complex. For dramatic vaults, consider cove molding which is more forgiving to install."),
        ],
    },
    "1114": {
        "name": "Baseboard Calculator",
        "intro": "Baseboards (skirting boards) run along every wall at floor level — calculating the right linear metres means measuring the full room perimeter, subtracting door openings, and adding waste for mitre cuts at corners. Get it wrong and you'll have visible joins or run short mid-room.",
        "who": "homeowners finishing a renovation, carpenters quoting trim work, and builders specifying finish materials",
        "example": "A 5 m × 4 m room with two 0.9 m door openings needs (18 - 1.8) × 1.05 = <strong>17 linear metres</strong> of baseboard allowing for waste.",
        "tip": "For painted baseboards, MDF is cheaper and machines perfectly. For stained or clear-coated wood, use solid timber or finger-jointed pine. Always prime MDF cut ends — they absorb paint and swell if left unprimed.",
        "faqs": [
            ("How do I measure baseboard for a room?", "Measure the perimeter of each wall, subtract all door openings (measure between door jambs), then add 5–10% for mitre cuts at corners and waste. This calculator does all of that automatically."),
            ("What height baseboard should I use?", "70–90 mm is standard for rooms with 2.4 m ceilings. Use taller baseboards (100–140 mm) in rooms with higher ceilings to maintain visual proportion. Very tall ceilings (3 m+) can use 150 mm or taller profiles."),
            ("Should baseboard be installed before or after flooring?", "Hard flooring (tile, timber, laminate) should be installed first, then baseboard on top to cover the expansion gap. Carpet is typically laid after baseboard, with the carpet tucked under the board."),
            ("How do I deal with out-of-square corners?", "Most corners are not exactly 90 degrees. Use an angle finder or digital protractor to measure the actual angle, then divide by 2 for each mitre cut. Small gaps can be filled with caulk and painted."),
            ("Can I use flexible baseboard for curved walls?", "Yes — thin MDF baseboard (6–9 mm) can be bent around gentle curves with a heat gun or by scoring the back. For tight curves, use purpose-made flexible trim or build up the curve with multiple layers of thin strips."),
        ],
    },
    "1115": {
        "name": "Drywall Calculator",
        "intro": "Drywall (plasterboard) is sold in standard sheet sizes — most commonly 1.2 m × 2.4 m — and cutting around doors, windows, and electrical boxes creates significant waste. This calculator divides your total wall and ceiling area by sheet size and adds an 8% waste factor to give you the exact sheet count to order.",
        "who": "homeowners adding or replacing drywall, builders framing interior walls, and renovation contractors estimating material costs",
        "example": "A room with 60 m² of walls and ceiling using standard 1.2 × 2.4 m sheets requires 60 ÷ 2.88 = 20.8 sheets × 1.08 waste = <strong>23 sheets</strong>.",
        "tip": "Hang drywall horizontally (long edge perpendicular to studs) for stronger walls with fewer butt joints. Butt joints are harder to finish than tapered edge joints — minimise them.",
        "faqs": [
            ("What thickness drywall should I use?", "12.5 mm (1/2 inch) is standard for most interior walls and ceilings. Use 16 mm (5/8 inch) for fire-rated assemblies and ceilings with 600 mm joist spacing. 9.5 mm is used for curved walls."),
            ("How do I calculate drywall for a ceiling?", "Calculate ceiling area separately from walls. For a flat ceiling, it's simply length × width. Vaulted ceilings require calculating the slope surface area using the pitch factor (same as roofing)."),
            ("Why add 8% waste factor for drywall?", "Cuts around doors, windows, outlets, and switches create off-cuts that are often too small to reuse. 8% is standard for simple rectangular rooms; complex rooms with many openings may need 10–12%."),
            ("Do I need moisture-resistant drywall in bathrooms?", "Yes — use green board (moisture-resistant) or cement board behind tile in wet areas. Standard drywall absorbs moisture and will deteriorate behind tiles. Cement board is required in shower and tub surrounds by most building codes."),
            ("How long does drywall compound take to dry between coats?", "Each coat of joint compound needs 24 hours to dry in normal conditions (20°C, 50% humidity). Speed up drying with fans and heat, or use setting-type compound which chemically hardens in 20–45 minutes regardless of humidity."),
        ],
    },
    "1116": {
        "name": "Concrete Steps Calculator",
        "intro": "Building concrete steps is a precision task — the ratio of riser height to tread depth determines safety and comfort. The classic rule is that 2 × riser + tread = 630 mm (the comfortable stride). This calculator works out how many steps fit your total rise and run, checks the riser-to-tread ratio, and calculates the concrete volume needed to pour them.",
        "who": "homeowners building entrance steps, landscapers constructing garden stairs, and contractors forming concrete stairways",
        "example": "A 1.05 m total rise with 0.175 m risers, 1.2 m step width, and 0.28 m treads needs <strong>6 steps</strong> and approximately <strong>0.35 m³ of concrete</strong>.",
        "tip": "The ideal riser height for outdoor steps is 150–175 mm. Risers below 100 mm create trip hazards (too easy to miss). Risers above 200 mm are tiring to climb. Always use a comfortable riser height and let the tread depth follow from the 630 mm rule.",
        "faqs": [
            ("What is the ideal riser-to-tread ratio for steps?", "The standard formula is: 2 × riser + tread = 630 mm. For a 175 mm riser: tread = 630 - 350 = 280 mm. For outdoor steps, treads are often wider (300–350 mm) for comfort."),
            ("How do I calculate the number of steps for a given rise?", "Divide the total rise by the desired riser height and round to the nearest whole number. Then recalculate the actual riser = total rise ÷ number of steps. All risers must be equal — unequal risers are a trip hazard."),
            ("How much concrete do I need for steps?", "The volume is approximately: number_of_steps × width × riser × tread / 2. This treats each step as a wedge. Add 10% for waste and formwork overfill. The calculator does this automatically."),
            ("Do concrete steps need reinforcement?", "Yes — steps wider than 1 m or with more than 3 risers should be reinforced with rebar or mesh. This prevents cracking from ground movement. Use 10 mm rebar on a 200 mm grid."),
            ("How long before I can walk on new concrete steps?", "Concrete reaches walking strength in 24–48 hours, but continues to cure for 28 days. Avoid heavy loads (vehicles, furniture) for at least 7 days. Keep new concrete moist for the first 3–7 days to improve strength."),
        ],
    },
    "1117": {
        "name": "Retaining Wall Calculator",
        "intro": "Retaining walls hold back soil on sloped sites — and building one without enough drainage or structural blocks leads to wall failure and costly repair. This calculator computes the total number of concrete blocks needed for your wall dimensions, plus the volume of drainage gravel to place behind the wall for water management.",
        "who": "homeowners landscaping a sloped yard, landscapers building garden retaining walls, and civil engineers specifying low-height retaining structures",
        "example": "A 6 m long × 0.9 m high retaining wall using 400 mm × 200 mm blocks needs approximately <strong>68 blocks</strong> plus <strong>1.08 m³ of drainage gravel</strong> behind it.",
        "tip": "Every retaining wall needs drainage — a perforated pipe at the base wrapped in geofabric, backfilled with 200–300 mm of 20 mm aggregate. Without it, water pressure will push the wall over within a few years.",
        "faqs": [
            ("How high can a retaining wall be without engineering?", "Most councils allow retaining walls up to 600–900 mm high without engineering certification. Walls above 1 m typically require a structural engineer's design and council approval. Always check local regulations."),
            ("What is the best block type for a retaining wall?", "Concrete segmental retaining wall blocks (SRW blocks) are the most common for DIY. They interlock without mortar and are designed for retaining walls. Sizes typically range from 200 × 100 × 200 mm to 450 × 200 × 250 mm."),
            ("How much batter (lean) should a retaining wall have?", "A batter of 1:10 (10 mm per 100 mm of height) is standard for segmental block walls. This lean-back improves stability by shifting the wall's centre of gravity toward the retained soil."),
            ("What type of gravel do I use behind a retaining wall?", "Use clean 20 mm crushed rock or gravel (no fines). Fines compact and retain water, defeating the purpose. The drainage layer should be at least 300 mm wide, wrapped in geofabric to prevent soil ingress."),
            ("How many courses of blocks per metre of wall height?", "This depends on block height. 200 mm blocks give 5 courses per metre, 100 mm blocks give 10 courses per metre. Calculate: height (mm) ÷ block height (mm) = number of courses."),
        ],
    },
    "1118": {
        "name": "Paver Calculator",
        "intro": "Pavers are sold individually or by the pallet, and the laying pattern significantly affects how many you need — a herringbone or 45-degree diagonal pattern creates more cut waste than a simple running bond. This calculator computes pavers needed for your area, applies a pattern waste factor, and calculates the gravel base volume required for a stable installation.",
        "who": "homeowners laying a patio or driveway, landscapers quoting paving jobs, and concrete suppliers calculating pallet orders",
        "example": "A 4 m × 3 m patio using 200 × 100 mm pavers in herringbone pattern (5% extra waste) needs approximately <strong>660 pavers</strong> and <strong>3.24 m³ of compacted base material</strong>.",
        "tip": "Always compact the sub-base in layers of no more than 100 mm using a plate compactor. A paver surface is only as good as the base underneath — rushing the compaction is the #1 cause of sunken, uneven paving.",
        "faqs": [
            ("What depth of base material do I need under pavers?", "For pedestrian patios: 100 mm compacted gravel + 30 mm bedding sand. For driveways: 150–200 mm compacted gravel + 30 mm bedding sand. The calculator uses a 150 mm base depth by default."),
            ("What is the waste factor for different paving patterns?", "Running bond (standard): 5% waste. Herringbone (45°): 10–15% waste. Diagonal (45°): 15–20% waste. Complex patterns with multiple sizes: 15–20% waste. The calculator applies pattern-specific factors."),
            ("Do pavers need to be sealed?", "Sealing is optional but recommended — it reduces staining, enhances colour, and inhibits weed growth in joints. Apply penetrating sealer 28 days after installation. Reapply every 3–5 years."),
            ("How much does a pallet of pavers cover?", "A standard pallet covers 10–15 m² depending on paver size and thickness. 200 × 100 × 50 mm concrete pavers typically pack 500–600 per pallet. Always confirm coverage with your supplier."),
            ("Can I lay pavers over an existing concrete slab?", "Yes — if the slab is level and structurally sound. Use a 30 mm layer of bedding sand or polymer-modified mortar. This raises the finished paving level, so check door clearances and step heights first."),
        ],
    },
    "1119": {
        "name": "Landscape Rock Calculator",
        "intro": "Landscape rocks and decorative gravel are sold by weight (tonnes) or volume (m³) depending on the supplier. Ordering by eye always leads to either bare patches or a leftover pile. This calculator converts your area dimensions and desired depth into the exact tonnes or cubic metres to order, using the density of the specific rock type you choose.",
        "who": "homeowners landscaping garden beds, landscapers quoting rock supply jobs, and garden centres estimating delivery volumes",
        "example": "A 8 m × 3 m garden bed with 80 mm depth of river pebbles (density 1.5 t/m³) requires 1.92 m³ of rock, or approximately <strong>2.9 tonnes</strong> to order.",
        "tip": "Always order 10% extra — rocks settle over time and you'll need top-ups. Specify the exact product name and grade when ordering, since density varies significantly between rock types (crushed granite 1.6 t/m³ vs river pebbles 1.45 t/m³).",
        "faqs": [
            ("How deep should landscape rock be?", "For weed suppression: 75–100 mm minimum. For decorative effect: 50–75 mm. For pathways: 50 mm. For drainage: 150–200 mm. Deeper layers are more effective at blocking weeds but require significantly more material."),
            ("What is the density of common landscape rocks?", "Crushed granite: 1.6 t/m³. River pebbles: 1.45–1.5 t/m³. Basalt: 1.6–1.7 t/m³. Decomposed granite (DG): 1.4 t/m³. Limestone: 1.5–1.6 t/m³. Use the correct density for your material to get an accurate weight."),
            ("Should I use landscape fabric under decorative rock?", "Yes — install woven geofabric before laying rock. It allows water through while blocking weed growth. Avoid plastic sheeting which prevents drainage and kills plant roots. Pin the fabric at edges before covering with rock."),
            ("How do I convert between tonnes and cubic metres for rock?", "Volume (m³) × density (t/m³) = weight (tonnes). For river pebbles at 1.5 t/m³: 2 m³ × 1.5 = 3 tonnes. Suppliers often quote in one unit — ask for both so you can compare quotes from different suppliers."),
            ("How much area does one tonne of landscape rock cover?", "One tonne of river pebbles covers approximately 10–12 m² at 50 mm depth, or 5–6 m² at 100 mm depth. For crushed granite, one tonne covers 8–10 m² at 50 mm. Always calculate volume first, then convert to tonnes."),
        ],
    },
}


def build_html(cid: str, calc: dict, ci: dict, content: dict) -> str:
    name = content["name"]
    intro = content["intro"]
    example = content["example"]
    tip = content["tip"]
    faqs = content["faqs"]

    inputs = calc.get("inputs", [])
    input_labels = ci.get("inputs", {})
    steps = calc.get("steps", [])
    mistakes = calc.get("mistakes", [])
    formula = calc.get("formula_display", "")
    formula = formula.replace("×", "×").replace("÷", "÷").replace("√", "√")

    how_items = ""
    for inp in inputs:
        label = input_labels.get(inp["id"], inp["id"])
        how_items += f"<li>Enter your <strong>{label}</strong>.</li>\n    "

    steps_html = ""
    for i, step in enumerate(steps, 1):
        steps_html += f"<li>{step}</li>\n    "

    mistakes_html = ""
    for m in mistakes:
        mistakes_html += f"<li>{m}</li>\n    "

    faq_html = ""
    for q, a in faqs:
        faq_html += f"""  <div class="faq-item">
    <div class="faq-q">{q}</div>
    <div class="faq-a"><p>{a}</p></div>
  </div>\n"""

    return f"""<section class="long-content">
  <h2>What is the {name}?</h2>
  <p>{intro}</p>

  <h2>Who Uses This Calculator?</h2>
  <p>This tool is used by {content['who']}.</p>

  <h2>How to Use the {name}</h2>
  <ol>
    {how_items}<li>Click <strong>Calculate</strong> to see your results instantly.</li>
  </ol>

  <h2>Formula</h2>
  <p>The calculator uses the following formula:</p>
  <pre class="formula-block">{formula}</pre>

  <h2>Worked Example</h2>
  <p>{example}</p>

  {f'<h2>Step-by-Step Calculation</h2><ol>' + chr(10).join(f"<li>{s}</li>" for s in steps) + "</ol>" if steps else ""}

  {f'<h2>Common Mistakes to Avoid</h2><ul>' + chr(10).join(f"<li>{m}</li>" for m in mistakes) + "</ul>" if mistakes else ""}

  <div class="pro-tip">
    <strong>Pro Tip:</strong> {tip}
  </div>

  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">
{faq_html}  </div>
</section>"""


updated = 0
for cid, content in CONTENT.items():
    calc = calcs_by_id.get(cid, {})
    ci = calcs_i18n.get(cid, {})
    if not calc:
        print(f"  [SKIP] calc {cid} not found")
        continue
    html = build_html(cid, calc, ci, content)
    out_path = CONTENT_DIR / f"{cid}.html"
    out_path.write_text(html, encoding="utf-8")
    size = len(html.encode("utf-8"))
    print(f"  [OK] {cid} {content['name']} -> {size:,} bytes")
    updated += 1

print(f"\n[DONE] Rewrote {updated} content files")
