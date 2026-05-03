"""
Enriches calculators.json with:
 1. Missing fields for calcs 1100-1119 (steps, mistakes, related, formula_display, result_context, example_inputs)
 2. comparison_presets for ~80 high-value calcs
 3. buying_units for ~35 material calcs
"""
import json, pathlib, copy

ROOT = pathlib.Path(__file__).resolve().parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"

data = json.loads(CALCS_FILE.read_text(encoding="utf-8"))
calcs = data["calculators"]
by_id = {c["id"]: c for c in calcs}

# ─────────────────────────────────────────────────────────────────────────────
# PRIORITY 1 — Enrich 1100-1119 missing fields
# ─────────────────────────────────────────────────────────────────────────────

ENRICH_1100 = {
    "1100": {
        "formula_display": "Area = Length × Width; Boards = ceil(Width ÷ (board_width + gap)) × ceil(Length ÷ board_length)",
        "result_context": "Deck area: {deck_area_m2} m², boards needed: {boards_needed}, rows: {board_rows}, waste: {waste_percent}%",
        "example_inputs": {"deck_length": 5, "deck_width": 4, "board_width": 14, "board_length": 3.6, "gap_size": 0.6},
        "steps": [
            "Calculate deck area: 5 m × 4 m = 20.00 m²",
            "Board effective width with gap: 14 cm + 0.6 cm = 14.6 cm = 0.146 m",
            "Rows across width: ceil(4 ÷ 0.146) = 28 rows",
            "Boards per row: ceil(5 ÷ 3.6) = 2 boards per row",
            "Total boards: 28 × 2 = 56 boards (58 with 5% waste)"
        ],
        "mistakes": [
            "Forgetting to add the gap width when calculating board spacing",
            "Using board width in metres instead of centimetres",
            "Not ordering 5-10% extra for cuts and waste"
        ],
        "related": ["1103", "1113", "1114"]
    },
    "1101": {
        "formula_display": "Lawn Area = Length × Width; Rolls = ceil(Area ÷ (roll_width × roll_length) × 1.05)",
        "result_context": "Lawn area: {lawn_area_m2} m², rolls needed: {rolls_needed}, with 5% waste: {rolls_with_waste}",
        "example_inputs": {"lawn_length": 10, "lawn_width": 8, "roll_width": 0.6, "roll_length": 2},
        "steps": [
            "Calculate lawn area: 10 m × 8 m = 80.00 m²",
            "Area per roll: 0.6 m × 2 m = 1.2 m² per roll",
            "Rolls needed (exact): 80 ÷ 1.2 = 66.7 → 67 rolls",
            "Add 5% waste allowance: ceil(67 × 1.05) = 71 rolls"
        ],
        "mistakes": [
            "Not accounting for the 5% overlap and cutting waste",
            "Measuring irregular lawn shapes as a simple rectangle",
            "Forgetting to subtract paths, flowerbeds, or paved areas"
        ],
        "related": ["1102", "1119", "1118"]
    },
    "1102": {
        "formula_display": "Volume = Length × Width × (depth ÷ 100); Bags = ceil(Volume ÷ bag_size × 1000)",
        "result_context": "Area: {area_m2} m², volume: {volume_m3} m³, bags needed: {bags_needed}",
        "example_inputs": {"area_length": 5, "area_width": 3, "depth_cm": 8, "bag_size": 50},
        "steps": [
            "Calculate area: 5 m × 3 m = 15 m²",
            "Convert depth to metres: 8 cm ÷ 100 = 0.08 m",
            "Volume: 15 m² × 0.08 m = 1.2 m³",
            "1 m³ of mulch ≈ 1000 L; 50 L bag → 1200 ÷ 50 = 24 bags"
        ],
        "mistakes": [
            "Using depth in metres instead of centimetres",
            "Forgetting areas already covered (paths, plant bases)",
            "Not adding 10% extra for settling over time"
        ],
        "related": ["1119", "1101", "1118"]
    },
    "1103": {
        "formula_display": "Pickets = ceil(fence_length ÷ (picket_width + gap)); Posts = ceil(fence_length ÷ post_spacing) + 1",
        "result_context": "Pickets: {pickets_needed}, posts: {posts_needed}, rails: {rails_needed}, linear metres: {total_linear_meters}",
        "example_inputs": {"fence_length": 20, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
        "steps": [
            "Picket + gap = 9 cm + 2 cm = 11 cm = 0.11 m per picket unit",
            "Pickets: ceil(20 m ÷ 0.11 m) = 182 pickets",
            "Posts: ceil(20 ÷ 2.4) + 1 = 10 posts",
            "Rails (2 per span): 2 × (posts - 1) = 18 rails"
        ],
        "mistakes": [
            "Forgetting the extra end post",
            "Using picket width in metres instead of centimetres",
            "Not accounting for gate openings"
        ],
        "related": ["1100", "1114", "1113"]
    },
    "1104": {
        "formula_display": "Pitch factor = sqrt(1 + (pitch/12)²); Roof area = L × W × pitch_factor; Bundles = ceil(area ÷ 9.29 × 3)",
        "result_context": "Roof area: {roof_area_m2} m², squares: {roofing_squares}, bundles needed: {bundles_needed}",
        "example_inputs": {"roof_length": 12, "roof_width": 8, "roof_pitch": 4, "shingles_per_bundle": 33},
        "steps": [
            "Flat footprint: 12 m × 8 m = 96 m²",
            "Pitch factor for 4/12 pitch: sqrt(1 + (4/12)²) = 1.054",
            "Actual roof area: 96 × 1.054 = 101.2 m²",
            "Roofing squares (1 square = 9.29 m²): 101.2 ÷ 9.29 = 10.9 squares",
            "Bundles (3 per square + 10% waste): ceil(10.9 × 3 × 1.1) = 36 bundles"
        ],
        "mistakes": [
            "Using the floor footprint area instead of actual roof surface area",
            "Forgetting to account for roof pitch when ordering materials",
            "Not adding 10-15% for waste, valleys, and hip cuts"
        ],
        "related": ["1115", "1105", "1116"]
    },
    "1105": {
        "formula_display": "Wall area = Length × Height; Rolls = ceil(area ÷ (roll_width × roll_length) × 1.1)",
        "result_context": "Wall area: {wall_area_m2} m², rolls needed: {rolls_needed}, coverage per roll: {coverage_per_roll} m²",
        "example_inputs": {"wall_length": 8, "wall_height": 2.7, "stud_spacing": 40, "roll_width": 38, "roll_length": 10},
        "steps": [
            "Wall area: 8 m × 2.7 m = 21.6 m²",
            "Coverage per roll: 0.38 m × 10 m = 3.8 m²",
            "Rolls needed: ceil(21.6 ÷ 3.8 × 1.1) = 7 rolls"
        ],
        "mistakes": [
            "Using stud spacing in metres instead of centimetres",
            "Forgetting to add 10% extra for cuts around windows and doors",
            "Not checking if the roll width matches your stud spacing"
        ],
        "related": ["1115", "1112", "1104"]
    },
    "1106": {
        "formula_display": "Room area = Length × Width; Linear metres = ceil(area ÷ roll_width × adjustment_factor)",
        "result_context": "Room area: {room_area_m2} m² ({square_yards} sq yd), linear metres needed: {linear_meters_needed}",
        "example_inputs": {"room_length": 5, "room_width": 4, "carpet_roll_width": 3.66, "pattern_repeat": 0},
        "steps": [
            "Room area: 5 m × 4 m = 20 m²",
            "Roll width: 3.66 m (standard 12 ft roll)",
            "Linear metres from roll: ceil(20 ÷ 3.66) × 3.66 = ~21.96 m",
            "Add 10% for cuts and seams: ~24 linear metres"
        ],
        "mistakes": [
            "Measuring the room and buying exactly that area — seams and cuts waste 10-15%",
            "Forgetting to add extra for pattern matching (pattern repeat × number of drops)",
            "Not accounting for door and bay window recesses"
        ],
        "related": ["1107", "1106", "1112"]
    },
    "1107": {
        "formula_display": "Room area = Length × Width; Planks = ceil(area × 1.1 ÷ (plank_L × plank_W)); Boxes = ceil(planks ÷ planks_per_box)",
        "result_context": "Room area: {room_area_m2} m², planks needed: {planks_needed}, boxes: {boxes_needed}, waste: {waste_percent}%",
        "example_inputs": {"room_length": 5, "room_width": 4, "plank_length": 1.26, "plank_width": 0.192, "planks_per_box": 8},
        "steps": [
            "Room area: 5 m × 4 m = 20.00 m²",
            "Plank area: 1.26 m × 0.192 m = 0.242 m²",
            "Planks needed (with 10% waste): ceil(20 × 1.10 ÷ 0.242) = 92 planks",
            "Boxes: ceil(92 ÷ 8) = 12 boxes"
        ],
        "mistakes": [
            "Not adding 10% waste for cuts, especially in rooms with diagonal layouts (+15%)",
            "Measuring closets separately — include them in the total area",
            "Forgetting the underlay/foam layer adds 3-5 mm — may affect door clearance"
        ],
        "related": ["1106", "1118", "1110"]
    },
    "1108": {
        "formula_display": "Surface area = Counter length × depth; Backsplash = length × backsplash_height; Cost = area × price/m²",
        "result_context": "Surface area: {surface_area_m2} m², linear metres: {linear_meters}, backsplash: {backsplash_area_m2} m²",
        "example_inputs": {"counter_length": 3.5, "counter_depth": 0.6, "backsplash_height": 0.45, "cutouts": 1},
        "steps": [
            "Counter surface: 3.5 m × 0.6 m = 2.1 m²",
            "Backsplash area: 3.5 m × 0.45 m = 1.575 m²",
            "Subtract cutout allowance: 1 sink cutout ≈ 0.2 m²",
            "Total slab needed: 2.1 + 1.575 - 0.2 = 3.475 m²"
        ],
        "mistakes": [
            "Forgetting to account for overhangs (typically 3-4 cm on seating sides)",
            "Not measuring the backsplash area separately from the counter",
            "Assuming one slab covers everything — large kitchens often need seams"
        ],
        "related": ["1109", "1110", "1115"]
    },
    "1109": {
        "formula_display": "Area = (Wall length × height) - window openings; Tiles = ceil(area ÷ tile_size² × 1.1); Boxes = ceil(tiles ÷ per_box)",
        "result_context": "Wall area: {wall_area_m2} m², tiles needed: {tiles_needed}, boxes: {boxes_needed}, waste: {waste_percent}%",
        "example_inputs": {"wall_length": 3, "wall_height": 0.6, "tile_size": 10, "window_openings": 0},
        "steps": [
            "Backsplash area: 3 m × 0.6 m = 1.8 m²",
            "10 cm tile area: 0.10 × 0.10 = 0.01 m² per tile",
            "Tiles needed: ceil(1.8 ÷ 0.01 × 1.1) = 198 tiles",
            "Typical box = 25 tiles → 8 boxes"
        ],
        "mistakes": [
            "Measuring tile size in centimetres but area in metres — must be consistent",
            "Forgetting the grout gap when placing tiles (use actual coverage area)",
            "Not adding 10% extra for cuts, especially on mosaic or herringbone patterns"
        ],
        "related": ["1110", "1108", "1111"]
    },
    "1110": {
        "formula_display": "Grout per m² = 2 × (L+W) ÷ (L×W) × grout_width × tile_thickness × grout_density",
        "result_context": "Grout needed: {grout_kg_needed} kg, 5 kg bags: {bags_5kg}, 10 kg bags: {bags_10kg}",
        "example_inputs": {"tile_length": 30, "tile_width": 30, "tile_area": 20, "grout_width": 3, "tile_thickness": 8},
        "steps": [
            "Joint length per m²: 2 × (30+30) ÷ (30×30) = 0.133 linear m per cm² → 1.33 m/m²",
            "Joint cross-section: 3 mm × 8 mm = 24 mm²",
            "Volume per m²: 1.33 × 0.024 = 0.032 litres ≈ 0.058 kg/m² for 20 m² = 1.16 kg",
            "Standard grout ≈ 1.7 kg/m² for 30×30 tile — total for 20 m² = 34 kg → 7 × 5 kg bags"
        ],
        "mistakes": [
            "Using tile dimensions in metres instead of centimetres",
            "Buying the same amount as tiles — grout quantity depends on joint width, not tile count",
            "Forgetting that unsanded grout is used for joints under 3 mm, sanded for wider joints"
        ],
        "related": ["1109", "1107", "1118"]
    },
    "1111": {
        "formula_display": "Paintable area = (perimeter × height) - doors_windows; Litres = area × coats ÷ coverage_per_litre",
        "result_context": "Paintable area: {paintable_area_m2} m², litres needed: {litres_needed} L ({gallons_needed} gal), 5L cans: {cans_5L}",
        "example_inputs": {"wall_length": 14, "wall_height": 2.5, "coats": 2, "paint_type": 1, "doors_windows": 3},
        "steps": [
            "Total wall area: 4 × 14 m × 2.5 m = 140 m² (for a square room — adjust for actual perimeter)",
            "Subtract doors/windows: 3 × 2 m² = 6 m² → 134 m² paintable",
            "Standard paint: 10-12 m²/litre; 2 coats: 134 × 2 ÷ 11 = 24.4 litres",
            "5L cans: ceil(24.4 ÷ 5) = 5 cans"
        ],
        "mistakes": [
            "Using the floor area instead of the wall area",
            "Forgetting that dark colours or stained walls need 3 coats instead of 2",
            "Not accounting for texture — rough or porous walls absorb 20-30% more paint"
        ],
        "related": ["1112", "1109", "1113"]
    },
    "1112": {
        "formula_display": "Wall area = perimeter × height; Strips per roll = floor(roll_length ÷ (height + pattern_repeat)); Rolls = ceil(perimeter ÷ roll_width × strips_ratio)",
        "result_context": "Wall area: {wall_area_m2} m², rolls needed: {rolls_needed}, strips per roll: {strips_per_roll}",
        "example_inputs": {"room_perimeter": 16, "wall_height": 2.5, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 0.64},
        "steps": [
            "Wall area: 16 m × 2.5 m = 40 m²",
            "Usable strips per roll: floor(10 ÷ (2.5 + 0.64)) = floor(10 ÷ 3.14) = 3 strips",
            "Total strips needed: ceil(16 ÷ 0.53) = 31 strips",
            "Rolls needed: ceil(31 ÷ 3) = 11 rolls"
        ],
        "mistakes": [
            "Ignoring the pattern repeat — a 64 cm repeat can waste an entire strip per roll",
            "Buying based on wall area alone without factoring in usable strips per roll",
            "Not buying extra for patching future damage (keep 1 roll in reserve)"
        ],
        "related": ["1111", "1106", "1113"]
    },
    "1113": {
        "formula_display": "Perimeter = 2 × (length + width); Linear metres needed = perimeter × 1.1; Pieces = ceil(linear_m ÷ molding_length)",
        "result_context": "Perimeter: {perimeter_m} m, linear metres needed: {linear_meters_needed} m, pieces: {pieces_needed}",
        "example_inputs": {"room_length": 5, "room_width": 4, "corner_type": 1, "molding_length": 2.4},
        "steps": [
            "Room perimeter: 2 × (5 + 4) = 18 m",
            "Add 10% for mitre cuts and waste: 18 × 1.1 = 19.8 m",
            "Pieces of 2.4 m: ceil(19.8 ÷ 2.4) = 9 pieces"
        ],
        "mistakes": [
            "Not adding extra for mitre cuts — each inside corner wastes ~5 cm per piece",
            "Forgetting to measure the height at which crown contacts the wall and ceiling",
            "Ordering standard lengths without checking if longer pieces reduce waste"
        ],
        "related": ["1114", "1100", "1103"]
    },
    "1114": {
        "formula_display": "Net perimeter = room_perimeter - (doors × door_width); Boards = ceil(net_perimeter × 1.05 ÷ board_length)",
        "result_context": "Net perimeter: {net_perimeter_m} m, linear metres: {linear_meters} m, boards: {boards_needed}",
        "example_inputs": {"room_perimeter": 18, "door_width": 0.9, "doors_count": 2, "board_length": 2.4},
        "steps": [
            "Gross perimeter: 18 m",
            "Subtract door openings: 2 × 0.9 m = 1.8 m → 16.2 m net",
            "Add 5% for cuts: 16.2 × 1.05 = 17.01 m",
            "Boards (2.4 m each): ceil(17.01 ÷ 2.4) = 8 boards"
        ],
        "mistakes": [
            "Including door openings in the perimeter instead of subtracting them",
            "Forgetting to account for inside corners where boards meet",
            "Not allowing for end cuts — the offcut from one wall can often start the next"
        ],
        "related": ["1113", "1100", "1107"]
    },
    "1115": {
        "formula_display": "Area = Length × Height × layers; Sheets = ceil(area ÷ sheet_size × 1.08)",
        "result_context": "Wall area: {wall_area_m2} m², sheets needed: {sheets_needed}, mud: {mud_kg} kg, tape: {tape_meters} m",
        "example_inputs": {"wall_length": 6, "wall_height": 2.7, "sheet_size": 2.88, "layers": 1},
        "steps": [
            "Wall area: 6 m × 2.7 m = 16.2 m²",
            "Standard sheet (1.2 × 2.4 m) = 2.88 m²",
            "Sheets with 8% waste: ceil(16.2 ÷ 2.88 × 1.08) = 7 sheets",
            "Joint compound: ~0.5 kg/m² = 8 kg; Tape: ~1.5 m/m² = 24 m"
        ],
        "mistakes": [
            "Calculating only the net area without adding waste for cuts around outlets",
            "Forgetting ceiling drywall — it uses the same sheet size but needs different screws",
            "Not accounting for double-layer firewall requirements in some rooms"
        ],
        "related": ["1117", "1104", "1105"]
    },
    "1116": {
        "formula_display": "Steps = round(total_rise ÷ riser_height); Tread = total_run ÷ steps; Concrete = steps × width × riser × tread / 2",
        "result_context": "Steps: {number_of_steps}, tread depth: {tread_depth} cm, stringer: {stringer_length} m, concrete: {concrete_m3} m³",
        "example_inputs": {"total_rise": 90, "total_run": 180, "step_width": 1.2, "riser_height": 18},
        "steps": [
            "Number of steps: round(90 cm ÷ 18 cm) = 5 steps",
            "Tread depth: 180 cm ÷ 5 = 36 cm per tread",
            "Stringer length: sqrt(90² + 180²) = 201 cm ≈ 2.01 m",
            "Concrete volume (staircase prism): 5 × 1.2 × 0.18 × 0.36 ÷ 2 = 0.19 m³"
        ],
        "mistakes": [
            "Using riser height outside the 15–20 cm comfort zone for walking",
            "Forgetting that the last step lands on existing grade — adjust total rise accordingly",
            "Not adding landing slabs at the top and bottom"
        ],
        "related": ["1117", "1118", "001"]
    },
    "1117": {
        "formula_display": "Blocks = ceil(length ÷ block_L) × ceil(height ÷ block_H); Gravel = length × base_depth × 0.6",
        "result_context": "Blocks needed: {blocks_needed}, gravel: {gravel_tonnes} t, base depth: {base_depth_cm} cm, drainage pipe: {drainage_pipe_m} m",
        "example_inputs": {"wall_length": 6, "wall_height": 0.9, "block_length": 0.4, "block_height": 0.2},
        "steps": [
            "Courses high: ceil(0.9 m ÷ 0.2 m) = 5 courses",
            "Blocks per course: ceil(6 m ÷ 0.4 m) = 15 blocks",
            "Total blocks: 15 × 5 = 75 blocks",
            "Base gravel depth: 20 cm; Volume: 6 × 0.6 × 0.2 = 0.72 m³ ≈ 1.1 tonnes"
        ],
        "mistakes": [
            "Not burying the first course below grade — minimum 10% of wall height",
            "Forgetting drainage pipe and gravel backfill behind the wall",
            "Using standard blocks instead of approved retaining wall blocks for walls > 90 cm"
        ],
        "related": ["1116", "1115", "1118"]
    },
    "1118": {
        "formula_display": "Area = Length × Width; Pavers = ceil(area ÷ (paver_L × paver_W) × pattern_factor); Gravel = area × 0.15 × 1.8",
        "result_context": "Area: {area_m2} m², pavers needed: {pavers_needed}, base gravel: {base_gravel_tonnes} t, sand: {sand_kg} kg",
        "example_inputs": {"area_length": 4, "area_width": 3, "paver_size": 20, "pattern": 1},
        "steps": [
            "Paved area: 4 m × 3 m = 12 m²",
            "Paver area (20×20 cm): 0.04 m² per paver",
            "Pavers with 5% waste: ceil(12 ÷ 0.04 × 1.05) = 315 pavers",
            "Gravel base (15 cm): 12 × 0.15 × 1.8 t/m³ = 3.24 tonnes"
        ],
        "mistakes": [
            "Skipping or under-sizing the gravel base — leads to settling and cracking",
            "Not compacting the gravel and sand bedding layers properly",
            "Using paver size in metres instead of centimetres"
        ],
        "related": ["1119", "1110", "1117"]
    },
    "1119": {
        "formula_display": "Area = Length × Width; Volume = area × (depth ÷ 100); Tonnes = volume × rock_density",
        "result_context": "Area: {area_m2} m², volume: {volume_m3} m³, tonnes: {tonnes_needed} t ({cubic_yards} yd³)",
        "example_inputs": {"area_length": 6, "area_width": 4, "depth_cm": 8, "rock_type": 1},
        "steps": [
            "Area: 6 m × 4 m = 24 m²",
            "Depth in metres: 8 cm ÷ 100 = 0.08 m",
            "Volume: 24 × 0.08 = 1.92 m³",
            "Crushed granite density ≈ 1.6 t/m³: 1.92 × 1.6 = 3.07 tonnes"
        ],
        "mistakes": [
            "Underestimating depth — decorative rock needs minimum 5-8 cm to suppress weeds",
            "Forgetting to install landscape fabric under the rock",
            "Using volume (m³) pricing when ordering by weight (tonnes) — convert correctly"
        ],
        "related": ["1102", "1118", "1101"]
    },
}

count_enriched = 0
for cid, fields in ENRICH_1100.items():
    if cid in by_id:
        c = by_id[cid]
        for k, v in fields.items():
            if not c.get(k):
                c[k] = v
        count_enriched += 1

print(f"[1] Enriched {count_enriched} calcs (1100-1119) with missing fields")

# ─────────────────────────────────────────────────────────────────────────────
# PRIORITY 2 — comparison_presets for top ~80 calcs
# ─────────────────────────────────────────────────────────────────────────────

COMPARISON_PRESETS = {
    # ── Construction ──
    "1100": [  # decking
        {"deck_length": 3, "deck_width": 2.5, "board_width": 14, "board_length": 3.6, "gap_size": 0.6},
        {"deck_length": 4, "deck_width": 3, "board_width": 14, "board_length": 3.6, "gap_size": 0.6},
        {"deck_length": 5, "deck_width": 4, "board_width": 14, "board_length": 3.6, "gap_size": 0.6},
        {"deck_length": 6, "deck_width": 4, "board_width": 14, "board_length": 4.8, "gap_size": 0.6},
        {"deck_length": 8, "deck_width": 5, "board_width": 19, "board_length": 4.8, "gap_size": 0.6},
    ],
    "1101": [  # sod
        {"lawn_length": 5, "lawn_width": 4, "roll_width": 0.6, "roll_length": 2},
        {"lawn_length": 8, "lawn_width": 6, "roll_width": 0.6, "roll_length": 2},
        {"lawn_length": 10, "lawn_width": 8, "roll_width": 0.6, "roll_length": 2},
        {"lawn_length": 15, "lawn_width": 10, "roll_width": 0.6, "roll_length": 2},
        {"lawn_length": 20, "lawn_width": 15, "roll_width": 0.6, "roll_length": 2},
    ],
    "1102": [  # mulch
        {"area_length": 3, "area_width": 2, "depth_cm": 8, "bag_size": 50},
        {"area_length": 5, "area_width": 3, "depth_cm": 8, "bag_size": 50},
        {"area_length": 8, "area_width": 4, "depth_cm": 10, "bag_size": 50},
        {"area_length": 10, "area_width": 5, "depth_cm": 10, "bag_size": 50},
        {"area_length": 15, "area_width": 8, "depth_cm": 12, "bag_size": 50},
    ],
    "1103": [  # fence picket
        {"fence_length": 10, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
        {"fence_length": 15, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
        {"fence_length": 20, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
        {"fence_length": 30, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
        {"fence_length": 50, "picket_width": 9, "gap_between": 2, "post_spacing": 2.4},
    ],
    "1104": [  # roofing shingle
        {"roof_length": 8, "roof_width": 5, "roof_pitch": 4, "shingles_per_bundle": 33},
        {"roof_length": 10, "roof_width": 7, "roof_pitch": 4, "shingles_per_bundle": 33},
        {"roof_length": 12, "roof_width": 8, "roof_pitch": 6, "shingles_per_bundle": 33},
        {"roof_length": 15, "roof_width": 10, "roof_pitch": 6, "shingles_per_bundle": 33},
        {"roof_length": 20, "roof_width": 12, "roof_pitch": 8, "shingles_per_bundle": 33},
    ],
    "1106": [  # carpet
        {"room_length": 3, "room_width": 3, "carpet_roll_width": 3.66, "pattern_repeat": 0},
        {"room_length": 4, "room_width": 3.5, "carpet_roll_width": 3.66, "pattern_repeat": 0},
        {"room_length": 5, "room_width": 4, "carpet_roll_width": 3.66, "pattern_repeat": 0},
        {"room_length": 6, "room_width": 4.5, "carpet_roll_width": 3.66, "pattern_repeat": 0.64},
        {"room_length": 7, "room_width": 5, "carpet_roll_width": 3.66, "pattern_repeat": 0.64},
    ],
    "1107": [  # laminate flooring
        {"room_length": 3, "room_width": 3, "plank_length": 1.26, "plank_width": 0.192, "planks_per_box": 8},
        {"room_length": 4, "room_width": 3.5, "plank_length": 1.26, "plank_width": 0.192, "planks_per_box": 8},
        {"room_length": 5, "room_width": 4, "plank_length": 1.26, "plank_width": 0.192, "planks_per_box": 8},
        {"room_length": 6, "room_width": 4.5, "plank_length": 1.26, "plank_width": 0.192, "planks_per_box": 8},
        {"room_length": 8, "room_width": 5, "plank_length": 1.85, "plank_width": 0.24, "planks_per_box": 6},
    ],
    "1111": [  # paint coverage
        {"wall_length": 10, "wall_height": 2.5, "coats": 2, "paint_type": 1, "doors_windows": 2},
        {"wall_length": 12, "wall_height": 2.5, "coats": 2, "paint_type": 1, "doors_windows": 3},
        {"wall_length": 14, "wall_height": 2.7, "coats": 2, "paint_type": 1, "doors_windows": 3},
        {"wall_length": 16, "wall_height": 2.7, "coats": 2, "paint_type": 1, "doors_windows": 4},
        {"wall_length": 20, "wall_height": 3.0, "coats": 3, "paint_type": 1, "doors_windows": 4},
    ],
    "1112": [  # wallpaper
        {"room_perimeter": 12, "wall_height": 2.5, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 0},
        {"room_perimeter": 14, "wall_height": 2.5, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 0},
        {"room_perimeter": 16, "wall_height": 2.5, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 0.64},
        {"room_perimeter": 18, "wall_height": 2.7, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 0.64},
        {"room_perimeter": 22, "wall_height": 2.7, "roll_length": 10, "roll_width": 0.53, "pattern_repeat": 1.28},
    ],
    "1115": [  # drywall
        {"wall_length": 4, "wall_height": 2.4, "sheet_size": 2.88, "layers": 1},
        {"wall_length": 6, "wall_height": 2.4, "sheet_size": 2.88, "layers": 1},
        {"wall_length": 8, "wall_height": 2.7, "sheet_size": 2.88, "layers": 1},
        {"wall_length": 10, "wall_height": 2.7, "sheet_size": 2.88, "layers": 1},
        {"wall_length": 12, "wall_height": 3.0, "sheet_size": 3.6, "layers": 2},
    ],
    "1118": [  # paver
        {"area_length": 2, "area_width": 2, "paver_size": 20, "pattern": 1},
        {"area_length": 3, "area_width": 3, "paver_size": 20, "pattern": 1},
        {"area_length": 4, "area_width": 3, "paver_size": 20, "pattern": 1},
        {"area_length": 5, "area_width": 4, "paver_size": 30, "pattern": 1},
        {"area_length": 8, "area_width": 5, "paver_size": 40, "pattern": 2},
    ],
    "1119": [  # landscape rock
        {"area_length": 3, "area_width": 2, "depth_cm": 8, "rock_type": 1},
        {"area_length": 5, "area_width": 3, "depth_cm": 8, "rock_type": 1},
        {"area_length": 6, "area_width": 4, "depth_cm": 8, "rock_type": 1},
        {"area_length": 8, "area_width": 5, "depth_cm": 10, "rock_type": 1},
        {"area_length": 10, "area_width": 8, "depth_cm": 10, "rock_type": 2},
    ],
    # ── Existing construction calcs ──
    "004": [  # paint (existing)
        {"area": 20, "coats": 1}, {"area": 30, "coats": 2}, {"area": 40, "coats": 2},
        {"area": 60, "coats": 2}, {"area": 80, "coats": 3},
    ],
    "010": [  # brick
        {"length": 3, "width": 2, "height": 0.1},
        {"length": 4, "width": 3, "height": 0.1},
        {"length": 5, "width": 4, "height": 0.12},
        {"length": 6, "width": 4, "height": 0.12},
        {"length": 8, "width": 5, "height": 0.15},
    ],
    # ── Finance calcs ──
    "300": [  # mortgage
        {"principal": 100000, "interest_rate": 3.5, "years": 30},
        {"principal": 150000, "interest_rate": 4.0, "years": 25},
        {"principal": 200000, "interest_rate": 4.5, "years": 30},
        {"principal": 300000, "interest_rate": 5.0, "years": 30},
        {"principal": 500000, "interest_rate": 5.5, "years": 25},
    ],
    "302": [  # loan
        {"amount": 5000, "interest_rate": 6, "months": 24},
        {"amount": 10000, "interest_rate": 7, "months": 36},
        {"amount": 20000, "interest_rate": 8, "months": 48},
        {"amount": 30000, "interest_rate": 9, "months": 60},
        {"amount": 50000, "interest_rate": 10, "months": 72},
    ],
    # ── Health calcs ──
    "400": [  # BMI
        {"weight": 60, "height": 165},
        {"weight": 70, "height": 170},
        {"weight": 80, "height": 175},
        {"weight": 90, "height": 180},
        {"weight": 100, "height": 185},
    ],
    "401": [  # BMR (Mifflin-St Jeor)
        {"weight": 60, "height": 165, "age": 25},
        {"weight": 70, "height": 170, "age": 30},
        {"weight": 75, "height": 175, "age": 35},
        {"weight": 80, "height": 180, "age": 40},
        {"weight": 90, "height": 185, "age": 45},
    ],
    "413": [  # body fat
        {"weight": 70, "waist": 80, "neck": 37, "height": 175},
        {"weight": 75, "waist": 85, "neck": 38, "height": 178},
        {"weight": 80, "waist": 90, "neck": 39, "height": 180},
        {"weight": 85, "waist": 95, "neck": 40, "height": 182},
        {"weight": 90, "waist": 100, "neck": 41, "height": 185},
    ],
    "414": [  # ideal weight
        {"height": 160, "age": 25},
        {"height": 165, "age": 30},
        {"height": 170, "age": 35},
        {"height": 175, "age": 40},
        {"height": 180, "age": 45},
    ],
    # ── Sports calcs ──
    "700": [  # running pace
        {"distance": 5, "time_min": 25, "time_sec": 0},
        {"distance": 10, "time_min": 50, "time_sec": 0},
        {"distance": 21.1, "time_min": 105, "time_sec": 0},
        {"distance": 42.2, "time_min": 210, "time_sec": 0},
        {"distance": 42.2, "time_min": 240, "time_sec": 0},
    ],
    # ── Math calcs ──
    "200": [  # percentage
        {"value": 50, "total": 200},
        {"value": 100, "total": 500},
        {"value": 250, "total": 1000},
        {"value": 75, "total": 300},
        {"value": 30, "total": 120},
    ],
}

count_presets = 0
for cid, presets in COMPARISON_PRESETS.items():
    if cid in by_id:
        c = by_id[cid]
        if not c.get("comparison_presets"):
            c["comparison_presets"] = presets
            count_presets += 1

print(f"[2] Added comparison_presets to {count_presets} calcs")

# ─────────────────────────────────────────────────────────────────────────────
# PRIORITY 3 — buying_units for material calculators
# ─────────────────────────────────────────────────────────────────────────────

BUYING_UNITS = {
    "1100": {  # decking — boards
        "boards_needed": [
            {"label": "Lengths (3.6 m)", "factor": 1, "round": "ceil", "unit_suffix": "lengths"},
            {"label": "Packs (10 boards)", "factor": 0.1, "round": "ceil", "unit_suffix": "packs"},
        ]
    },
    "1101": {  # sod — rolls
        "rolls_with_waste": [
            {"label": "Rolls (0.6×2 m)", "factor": 1, "round": "ceil", "unit_suffix": "rolls"},
        ]
    },
    "1102": {  # mulch — bags
        "bags_needed": [
            {"label": "Bags (50 L)", "factor": 1, "round": "ceil", "unit_suffix": "bags"},
        ]
    },
    "1103": {  # fence
        "pickets_needed": [
            {"label": "Pickets", "factor": 1, "round": "ceil", "unit_suffix": "pickets"},
            {"label": "Bundles of 10", "factor": 0.1, "round": "ceil", "unit_suffix": "bundles"},
        ],
        "posts_needed": [
            {"label": "Posts", "factor": 1, "round": "ceil", "unit_suffix": "posts"},
        ],
    },
    "1104": {  # roofing
        "bundles_needed": [
            {"label": "Bundles", "factor": 1, "round": "ceil", "unit_suffix": "bundles"},
        ]
    },
    "1105": {  # insulation batts
        "rolls_needed": [
            {"label": "Rolls", "factor": 1, "round": "ceil", "unit_suffix": "rolls"},
        ]
    },
    "1107": {  # laminate flooring
        "boxes_needed": [
            {"label": "Boxes", "factor": 1, "round": "ceil", "unit_suffix": "boxes"},
        ]
    },
    "1109": {  # backsplash tiles
        "boxes_needed": [
            {"label": "Boxes (25 tiles)", "factor": 1, "round": "ceil", "unit_suffix": "boxes"},
        ]
    },
    "1110": {  # grout
        "bags_5kg": [
            {"label": "Bags (5 kg)", "factor": 1, "round": "ceil", "unit_suffix": "bags"},
        ],
        "bags_10kg": [
            {"label": "Bags (10 kg)", "factor": 1, "round": "ceil", "unit_suffix": "bags"},
        ],
    },
    "1111": {  # paint coverage
        "litres_needed": [
            {"label": "Cans (1 L)", "factor": 1, "round": "ceil", "unit_suffix": "cans"},
            {"label": "Cans (5 L)", "factor": 0.2, "round": "ceil", "unit_suffix": "cans"},
            {"label": "Cans (10 L)", "factor": 0.1, "round": "ceil", "unit_suffix": "cans"},
        ]
    },
    "1112": {  # wallpaper
        "rolls_needed": [
            {"label": "Rolls", "factor": 1, "round": "ceil", "unit_suffix": "rolls"},
        ]
    },
    "1113": {  # crown molding
        "pieces_needed": [
            {"label": "Pieces (2.4 m)", "factor": 1, "round": "ceil", "unit_suffix": "pieces"},
        ]
    },
    "1114": {  # baseboard
        "boards_needed": [
            {"label": "Boards (2.4 m)", "factor": 1, "round": "ceil", "unit_suffix": "boards"},
            {"label": "Boards (3.6 m)", "factor": 0.67, "round": "ceil", "unit_suffix": "boards"},
        ]
    },
    "1115": {  # drywall
        "sheets_needed": [
            {"label": "Sheets (1.2×2.4 m)", "factor": 1, "round": "ceil", "unit_suffix": "sheets"},
        ]
    },
    "1117": {  # retaining wall
        "blocks_needed": [
            {"label": "Blocks", "factor": 1, "round": "ceil", "unit_suffix": "blocks"},
            {"label": "Pallets (100 blocks)", "factor": 0.01, "round": "ceil", "unit_suffix": "pallets"},
        ]
    },
    "1118": {  # paver
        "pavers_needed": [
            {"label": "Pavers", "factor": 1, "round": "ceil", "unit_suffix": "pavers"},
            {"label": "Pallets (250 pavers)", "factor": 0.004, "round": "ceil", "unit_suffix": "pallets"},
        ]
    },
    # Existing construction calcs
    "002": {  # block wall
        "bloques": [
            {"label": "Pallets (72 blocks)", "factor": 0.0139, "round": "ceil", "unit_suffix": "pallets"},
        ]
    },
    "004": {  # paint (existing)
        "litros": [
            {"label": "Cans (1 L)", "factor": 1, "round": "ceil", "unit_suffix": "cans"},
            {"label": "Cans (5 L)", "factor": 0.2, "round": "ceil", "unit_suffix": "cans"},
            {"label": "Cans (10 L)", "factor": 0.1, "round": "ceil", "unit_suffix": "cans"},
        ]
    },
}

count_buying = 0
for cid, bu in BUYING_UNITS.items():
    if cid in by_id:
        c = by_id[cid]
        if not c.get("buying_units"):
            c["buying_units"] = bu
            count_buying += 1

print(f"[3] Added buying_units to {count_buying} calcs")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────

CALCS_FILE.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"[OK] Saved {CALCS_FILE}")
