#!/usr/bin/env python3
"""
Add 20 new high-quality calculators targeting low-competition long-tail keywords
Each with unique formulas, original content, and SEO optimization
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CALCS_FILE = ROOT / "src" / "calculators" / "calculators.json"
I18N_DIR = ROOT / "src" / "i18n"
CONTENT_DIR = ROOT / "src" / "content"

# 20 new calculators with unique positioning
NEW_CALCULATORS = [
    {
        "id": "1100",
        "slug": "decking-calculator",
        "block": 7,
        "block_slug": "carpinteria",
        "name_en": "Decking Calculator – Composite & Wood Deck Boards",
        "name_es": "Calculadora de Tarimas – Madera y Compuesto",
        "inputs": [
            {"id": "deck_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "deck_width", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "board_width", "type": "number", "min": 5, "max": 30, "step": 0.5, "default": 14, "unit": "cm", "unit_category": "length"},
            {"id": "board_length", "type": "number", "min": 1, "max": 6, "step": 0.3, "default": 3.6, "unit": "m", "unit_category": "length"},
            {"id": "gap_size", "type": "number", "min": 0, "max": 2, "step": 0.1, "default": 0.6, "unit": "cm", "unit_category": "length"},
        ],
        "outputs": ["deck_area_m2", "boards_needed", "board_rows", "waste_percent", "total_linear_meters"],
        "formula": "boards_per_row = deck_width / (board_width + gap); rows_needed = deck_length / board_length; total_boards = boards_per_row × rows_needed × (1 + waste)",
    },
    {
        "id": "1101",
        "slug": "sod-turf-calculator",
        "block": 1,
        "block_slug": "estructuras",
        "name_en": "Sod & Turf Calculator – Grass Rolls Needed",
        "name_es": "Calculadora de Césped – Rollos de Tepe Necesarios",
        "inputs": [
            {"id": "lawn_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 10, "unit": "m", "unit_category": "length"},
            {"id": "lawn_width", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "roll_width", "type": "number", "min": 0.3, "max": 1, "step": 0.05, "default": 0.6, "unit": "m", "unit_category": "length"},
            {"id": "roll_length", "type": "number", "min": 1, "max": 3, "step": 0.1, "default": 1.5, "unit": "m", "unit_category": "length"},
        ],
        "outputs": ["lawn_area_m2", "rolls_needed", "rolls_with_waste", "coverage_m2_per_roll"],
        "formula": "roll_area = roll_width × roll_length; rolls_needed = lawn_area / roll_area; with_waste = rolls × 1.05",
    },
    {
        "id": "1102",
        "slug": "mulch-calculator",
        "block": 1,
        "block_slug": "estructuras",
        "name_en": "Mulch Calculator – Bags & Cubic Yards",
        "name_es": "Calculadora de Mantillo – Bolsas y Yardas Cúbicas",
        "inputs": [
            {"id": "area_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "area_width", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "depth_cm", "type": "number", "min": 1, "max": 20, "step": 0.5, "default": 5, "unit": "cm", "unit_category": "length"},
            {"id": "bag_size", "type": "number", "min": 10, "max": 100, "step": 5, "default": 40, "unit": "L", "unit_category": "volume"},
        ],
        "outputs": ["area_m2", "volume_m3", "bags_needed", "cubic_yards"],
        "formula": "volume = length × width × depth; bags = volume_m3 × 1000 / bag_size_L",
    },
    {
        "id": "1103",
        "slug": "fence-picket-calculator",
        "block": 7,
        "block_slug": "carpinteria",
        "name_en": "Fence Picket Calculator – Wood & Vinyl",
        "name_es": "Calculadora de Valla – Estacas de Madera",
        "inputs": [
            {"id": "fence_length", "type": "number", "min": 1, "max": 500, "step": 0.1, "default": 30, "unit": "m", "unit_category": "length"},
            {"id": "picket_width", "type": "number", "min": 5, "max": 20, "step": 0.5, "default": 10, "unit": "cm", "unit_category": "length"},
            {"id": "gap_between", "type": "number", "min": 0, "max": 15, "step": 0.5, "default": 5, "unit": "cm", "unit_category": "length"},
            {"id": "post_spacing", "type": "number", "min": 1, "max": 5, "step": 0.1, "default": 2.4, "unit": "m", "unit_category": "length"},
        ],
        "outputs": ["pickets_needed", "posts_needed", "rails_needed", "total_linear_meters"],
        "formula": "pickets = fence_length / (picket_width + gap); posts = fence_length / post_spacing + 1",
    },
    {
        "id": "1104",
        "slug": "roofing-shingle-calculator",
        "block": 1,
        "block_slug": "estructuras",
        "name_en": "Roofing Shingle Calculator – Bundles & Squares",
        "name_es": "Calculadora de Tejas – Paquetes y Cuadrados",
        "inputs": [
            {"id": "roof_length", "type": "number", "min": 1, "max": 100, "step": 0.1, "default": 10, "unit": "m", "unit_category": "length"},
            {"id": "roof_width", "type": "number", "min": 1, "max": 50, "step": 0.1, "default": 8, "unit": "m", "unit_category": "length"},
            {"id": "roof_pitch", "type": "select", "options": [{"value": "3/12", "label": "3/12 (Low)"}, {"value": "6/12", "label": "6/12 (Medium)"}, {"value": "9/12", "label": "9/12 (Steep)"}, {"value": "12/12", "label": "12/12 (Very Steep)"}], "default": "6/12"},
            {"id": "shingles_per_bundle", "type": "number", "min": 20, "max": 40, "step": 1, "default": 29, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["roof_area_m2", "roofing_squares", "bundles_needed", "waste_percent"],
        "formula": "pitch_multiplier = 1.0 to 1.5 based on pitch; area = length × width × multiplier; squares = area / 9.29; bundles = squares × 3",
    },
    {
        "id": "1105",
        "slug": "insulation-batt-calculator",
        "block": 6,
        "block_slug": "climatizacion",
        "name_en": "Insulation Batt Calculator – Rolls & R-Value",
        "name_es": "Calculadora de Aislamiento – Rollos y Valor R",
        "inputs": [
            {"id": "wall_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 1, "max": 10, "step": 0.1, "default": 2.7, "unit": "m", "unit_category": "length"},
            {"id": "stud_spacing", "type": "select", "options": [{"value": "400", "label": "400mm (16\")"}, {"value": "600", "label": "600mm (24\")"}], "default": "400"},
            {"id": "roll_width", "type": "number", "min": 30, "max": 100, "step": 5, "default": 40, "unit": "cm", "unit_category": "length"},
            {"id": "roll_length", "type": "number", "min": 5, "max": 30, "step": 1, "default": 12, "unit": "m", "unit_category": "length"},
        ],
        "outputs": ["wall_area_m2", "rolls_needed", "coverage_per_roll", "total_linear_meters"],
        "formula": "area = length × height; rolls = area / (roll_width × roll_length)",
    },
    {
        "id": "1106",
        "slug": "carpet-calculator",
        "block": 3,
        "block_slug": "pavimentos",
        "name_en": "Carpet Calculator – Square Yards & Rolls",
        "name_es": "Calculadora de Alfombra – Yardas Cuadradas",
        "inputs": [
            {"id": "room_length", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "room_width", "type": "number", "min": 0.1, "max": 30, "step": 0.1, "default": 4, "unit": "m", "unit_category": "length"},
            {"id": "carpet_roll_width", "type": "select", "options": [{"value": "3.66", "label": "12 ft (3.66m)"}, {"value": "4.57", "label": "15 ft (4.57m)"}], "default": "3.66"},
            {"id": "pattern_repeat", "type": "number", "min": 0, "max": 100, "step": 1, "default": 0, "unit": "cm", "unit_category": "length"},
        ],
        "outputs": ["room_area_m2", "square_yards", "linear_meters_needed", "waste_percent"],
        "formula": "area = length × width; sq_yards = area / 0.836; with_pattern = area × (1 + pattern_waste)",
    },
    {
        "id": "1107",
        "slug": "laminate-flooring-calculator",
        "block": 3,
        "block_slug": "pavimentos",
        "name_en": "Laminate Flooring Calculator – Planks & Boxes",
        "name_es": "Calculadora de Suelo Laminado – Tablas y Cajas",
        "inputs": [
            {"id": "room_length", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "room_width", "type": "number", "min": 0.1, "max": 30, "step": 0.1, "default": 4, "unit": "m", "unit_category": "length"},
            {"id": "plank_length", "type": "number", "min": 0.5, "max": 2, "step": 0.05, "default": 1.2, "unit": "m", "unit_category": "length"},
            {"id": "plank_width", "type": "number", "min": 10, "max": 30, "step": 1, "default": 19, "unit": "cm", "unit_category": "length"},
            {"id": "planks_per_box", "type": "number", "min": 5, "max": 20, "step": 1, "default": 8, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["room_area_m2", "planks_needed", "boxes_needed", "waste_percent"],
        "formula": "area = length × width; plank_area = plank_length × plank_width; planks = area / plank_area × 1.10",
    },
    {
        "id": "1108",
        "slug": "countertop-calculator",
        "block": 9,
        "block_slug": "gestion",
        "name_en": "Countertop Calculator – Granite & Quartz",
        "name_es": "Calculadora de Encimera – Granito y Cuarzo",
        "inputs": [
            {"id": "counter_length", "type": "number", "min": 0.1, "max": 10, "step": 0.05, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "counter_depth", "type": "number", "min": 30, "max": 100, "step": 5, "default": 63, "unit": "cm", "unit_category": "length"},
            {"id": "backsplash_height", "type": "number", "min": 0, "max": 50, "step": 1, "default": 10, "unit": "cm", "unit_category": "length"},
            {"id": "cutouts", "type": "number", "min": 0, "max": 5, "step": 1, "default": 1, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["surface_area_m2", "linear_meters", "backsplash_area_m2", "estimated_cost"],
        "formula": "area = length × depth; backsplash = length × backsplash_height; total = area + backsplash - cutouts",
    },
    {
        "id": "1109",
        "slug": "backsplash-tile-calculator",
        "block": 8,
        "block_slug": "pintura",
        "name_en": "Backsplash Tile Calculator – Kitchen & Bathroom",
        "name_es": "Calculadora de Salpicadero – Cocina y Baño",
        "inputs": [
            {"id": "wall_length", "type": "number", "min": 0.1, "max": 10, "step": 0.05, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 0.1, "max": 2, "step": 0.05, "default": 0.45, "unit": "m", "unit_category": "length"},
            {"id": "tile_size", "type": "select", "options": [{"value": "10x10", "label": "10×10 cm"}, {"value": "15x15", "label": "15×15 cm"}, {"value": "20x20", "label": "20×20 cm"}, {"value": "7.5x15", "label": "7.5×15 cm (Subway)"}], "default": "10x10"},
            {"id": "window_openings", "type": "number", "min": 0, "max": 5, "step": 1, "default": 0, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["wall_area_m2", "tiles_needed", "boxes_needed", "waste_percent"],
        "formula": "area = length × height - openings; tiles = area / tile_area × 1.10",
    },
    {
        "id": "1110",
        "slug": "grout-calculator",
        "block": 3,
        "block_slug": "pavimentos",
        "name_en": "Grout Calculator – Bags & Coverage",
        "name_es": "Calculadora de Lechada – Bolsas y Cobertura",
        "inputs": [
            {"id": "tile_length", "type": "number", "min": 1, "max": 100, "step": 0.5, "default": 30, "unit": "cm", "unit_category": "length"},
            {"id": "tile_width", "type": "number", "min": 1, "max": 100, "step": 0.5, "default": 30, "unit": "cm", "unit_category": "length"},
            {"id": "tile_area", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 10, "unit": "m2", "unit_category": "area"},
            {"id": "grout_width", "type": "number", "min": 1, "max": 20, "step": 0.5, "default": 3, "unit": "mm", "unit_category": "length"},
            {"id": "tile_thickness", "type": "number", "min": 5, "max": 30, "step": 1, "default": 10, "unit": "mm", "unit_category": "length"},
        ],
        "outputs": ["grout_kg_needed", "bags_5kg", "bags_10kg", "coverage_m2_per_kg"],
        "formula": "grout_kg = (tile_length + tile_width) / (tile_length × tile_width) × tile_thickness × grout_width × area × density",
    },
    {
        "id": "1111",
        "slug": "paint-coverage-calculator",
        "block": 8,
        "block_slug": "pintura",
        "name_en": "Paint Coverage Calculator – Litres & Gallons",
        "name_es": "Calculadora de Pintura – Litros y Galones",
        "inputs": [
            {"id": "wall_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 1, "max": 10, "step": 0.1, "default": 2.7, "unit": "m", "unit_category": "length"},
            {"id": "coats", "type": "number", "min": 1, "max": 4, "step": 1, "default": 2, "unit": "pcs", "unit_category": "count"},
            {"id": "paint_type", "type": "select", "options": [{"value": "primer", "label": "Primer (12 m²/L)"}, {"value": "latex", "label": "Latex (10 m²/L)"}, {"value": "oil", "label": "Oil-based (8 m²/L)"}], "default": "latex"},
            {"id": "doors_windows", "type": "number", "min": 0, "max": 10, "step": 1, "default": 1, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["paintable_area_m2", "litres_needed", "gallons_needed", "cans_5L"],
        "formula": "area = (length × height - openings) × coats; litres = area / coverage_per_litre",
    },
    {
        "id": "1112",
        "slug": "wallpaper-calculator",
        "block": 8,
        "block_slug": "pintura",
        "name_en": "Wallpaper Calculator – Rolls & Pattern Match",
        "name_es": "Calculadora de Papel Pintado – Rollos",
        "inputs": [
            {"id": "room_perimeter", "type": "number", "min": 1, "max": 100, "step": 0.1, "default": 15, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 1, "max": 5, "step": 0.1, "default": 2.7, "unit": "m", "unit_category": "length"},
            {"id": "roll_length", "type": "number", "min": 5, "max": 20, "step": 1, "default": 10, "unit": "m", "unit_category": "length"},
            {"id": "roll_width", "type": "number", "min": 0.5, "max": 1.5, "step": 0.05, "default": 0.53, "unit": "m", "unit_category": "length"},
            {"id": "pattern_repeat", "type": "number", "min": 0, "max": 100, "step": 1, "default": 0, "unit": "cm", "unit_category": "length"},
        ],
        "outputs": ["wall_area_m2", "rolls_needed", "strips_per_roll", "waste_percent"],
        "formula": "strips = perimeter / roll_width; strips_per_roll = roll_length / wall_height; rolls = strips / strips_per_roll",
    },
    {
        "id": "1113",
        "slug": "crown-molding-calculator",
        "block": 7,
        "block_slug": "carpinteria",
        "name_en": "Crown Molding Calculator – Linear Feet & Corners",
        "name_es": "Calculadora de Cornisa – Metros Lineales",
        "inputs": [
            {"id": "room_length", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "room_width", "type": "number", "min": 0.1, "max": 30, "step": 0.1, "default": 4, "unit": "m", "unit_category": "length"},
            {"id": "corner_type", "type": "select", "options": [{"value": "miter", "label": "Mitered (45°)"}, {"value": "copied", "label": "Coped"}, {"value": "blocks", "label": "Corner Blocks"}], "default": "miter"},
            {"id": "molding_length", "type": "number", "min": 1, "max": 5, "step": 0.3, "default": 2.4, "unit": "m", "unit_category": "length"},
        ],
        "outputs": ["perimeter_m", "linear_meters_needed", "pieces_needed", "corner_pieces"],
        "formula": "perimeter = 2 × (length + width); pieces = perimeter / molding_length × 1.10",
    },
    {
        "id": "1114",
        "slug": "baseboard-calculator",
        "block": 7,
        "block_slug": "carpinteria",
        "name_en": "Baseboard Calculator – Linear Meters & Returns",
        "name_es": "Calculadora de Zócalo – Metros Lineales",
        "inputs": [
            {"id": "room_perimeter", "type": "number", "min": 1, "max": 100, "step": 0.1, "default": 18, "unit": "m", "unit_category": "length"},
            {"id": "door_width", "type": "number", "min": 0.5, "max": 2, "step": 0.1, "default": 0.9, "unit": "m", "unit_category": "length"},
            {"id": "doors_count", "type": "number", "min": 0, "max": 10, "step": 1, "default": 1, "unit": "pcs", "unit_category": "count"},
            {"id": "board_length", "type": "number", "min": 1, "max": 5, "step": 0.3, "default": 2.4, "unit": "m", "unit_category": "length"},
        ],
        "outputs": ["net_perimeter_m", "linear_meters", "boards_needed", "returns_needed"],
        "formula": "net_perimeter = perimeter - (doors × door_width); boards = net_perimeter / board_length × 1.05",
    },
    {
        "id": "1115",
        "slug": "drywall-calculator",
        "block": 2,
        "block_slug": "mamposteria",
        "name_en": "Drywall Calculator – Sheets, Mud & Tape",
        "name_es": "Calculadora de Pladur – Placas, Masilla y Cinta",
        "inputs": [
            {"id": "wall_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 1, "max": 10, "step": 0.1, "default": 2.7, "unit": "m", "unit_category": "length"},
            {"id": "sheet_size", "type": "select", "options": [{"value": "1.2x2.4", "label": "1.2×2.4m (4×8 ft)"}, {"value": "1.2x3.0", "label": "1.2×3.0m (4×10 ft)"}, {"value": "1.2x3.6", "label": "1.2×3.6m (4×12 ft)"}], "default": "1.2x2.4"},
            {"id": "layers", "type": "number", "min": 1, "max": 3, "step": 1, "default": 1, "unit": "pcs", "unit_category": "count"},
        ],
        "outputs": ["wall_area_m2", "sheets_needed", "mud_kg", "tape_meters", "screws_count"],
        "formula": "area = length × height × layers; sheets = area / sheet_area; mud = area × 0.5 kg/m²; tape = seams × length",
    },
    {
        "id": "1116",
        "slug": "concrete-steps-calculator",
        "block": 1,
        "block_slug": "estructuras",
        "name_en": "Concrete Steps Calculator – Stringers & Treads",
        "name_es": "Calculadora de Escalones – Vigas y Huellas",
        "inputs": [
            {"id": "total_rise", "type": "number", "min": 0.1, "max": 5, "step": 0.01, "default": 1, "unit": "m", "unit_category": "length"},
            {"id": "total_run", "type": "number", "min": 0.5, "max": 10, "step": 0.1, "default": 2.5, "unit": "m", "unit_category": "length"},
            {"id": "step_width", "type": "number", "min": 0.5, "max": 3, "step": 0.1, "default": 1.2, "unit": "m", "unit_category": "length"},
            {"id": "riser_height", "type": "number", "min": 10, "max": 25, "step": 1, "default": 18, "unit": "cm", "unit_category": "length"},
        ],
        "outputs": ["number_of_steps", "tread_depth", "stringer_length", "concrete_m3"],
        "formula": "steps = total_rise / riser_height; tread = total_run / steps; stringer = sqrt(rise² + run²)",
    },
    {
        "id": "1117",
        "slug": "retaining-wall-calculator",
        "block": 2,
        "block_slug": "mamposteria",
        "name_en": "Retaining Wall Calculator – Blocks & Gravel",
        "name_es": "Calculadora de Muro de Contención – Bloques y Grava",
        "inputs": [
            {"id": "wall_length", "type": "number", "min": 1, "max": 100, "step": 0.1, "default": 10, "unit": "m", "unit_category": "length"},
            {"id": "wall_height", "type": "number", "min": 0.3, "max": 3, "step": 0.1, "default": 1, "unit": "m", "unit_category": "length"},
            {"id": "block_length", "type": "number", "min": 20, "max": 60, "step": 5, "default": 40, "unit": "cm", "unit_category": "length"},
            {"id": "block_height", "type": "number", "min": 10, "max": 30, "step": 5, "default": 20, "unit": "cm", "unit_category": "length"},
        ],
        "outputs": ["blocks_needed", "gravel_tonnes", "base_depth_cm", "drainage_pipe_m"],
        "formula": "blocks_per_row = length / block_length; rows = height / block_height; total = blocks_per_row × rows × 1.05",
    },
    {
        "id": "1118",
        "slug": "paver-calculator",
        "block": 3,
        "block_slug": "pavimentos",
        "name_en": "Paver Calculator – Patio & Walkway",
        "name_es": "Calculadora de adoquines – Patio y Sendero",
        "inputs": [
            {"id": "area_length", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "area_width", "type": "number", "min": 0.1, "max": 30, "step": 0.1, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "paver_size", "type": "select", "options": [{"value": "10x20", "label": "10×20 cm"}, {"value": "15x15", "label": "15×15 cm"}, {"value": "20x20", "label": "20×20 cm"}, {"value": "15x30", "label": "15×30 cm"}], "default": "20x20"},
            {"id": "pattern", "type": "select", "options": [{"value": "running", "label": "Running Bond (5% waste)"}, {"value": "herringbone", "label": "Herringbone (10% waste)"}, {"value": "basket", "label": "Basket Weave (8% waste)"}], "default": "running"},
        ],
        "outputs": ["area_m2", "pavers_needed", "base_gravel_tonnes", "sand_kg"],
        "formula": "area = length × width; pavers = area / paver_area × (1 + waste%); gravel = area × 0.1 × 1.6 tonnes/m³",
    },
    {
        "id": "1119",
        "slug": "landscape-rock-calculator",
        "block": 1,
        "block_slug": "estructuras",
        "name_en": "Landscape Rock Calculator – Tons & Cubic Yards",
        "name_es": "Calculadora de Piedras – Toneladas y Yardas",
        "inputs": [
            {"id": "area_length", "type": "number", "min": 0.1, "max": 100, "step": 0.1, "default": 5, "unit": "m", "unit_category": "length"},
            {"id": "area_width", "type": "number", "min": 0.1, "max": 50, "step": 0.1, "default": 3, "unit": "m", "unit_category": "length"},
            {"id": "depth_cm", "type": "number", "min": 2, "max": 30, "step": 1, "default": 5, "unit": "cm", "unit_category": "length"},
            {"id": "rock_type", "type": "select", "options": [{"value": "gravel", "label": "Gravel (1.6 t/m³)"}, {"value": "crushed", "label": "Crushed Stone (1.7 t/m³)"}, {"value": "river", "label": "River Rock (1.5 t/m³)"}, {"value": "decomposed", "label": "Decomposed Granite (1.8 t/m³)"}], "default": "gravel"},
        ],
        "outputs": ["area_m2", "volume_m3", "tonnes_needed", "cubic_yards"],
        "formula": "volume = length × width × depth; tonnes = volume × density; yards = volume × 1.308",
    },
]

# Load existing calculators
with open(CALCS_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new calculators
for calc in NEW_CALCULATORS:
    # Build full calculator definition
    new_calc = {
        "id": calc["id"],
        "slug": calc["slug"],
        "block": calc["block"],
        "block_slug": calc["block_slug"],
        "inputs": calc["inputs"],
        "outputs": calc["outputs"],
        "formula": calc.get("formula", ""),
    }
    data["calculators"].append(new_calc)
    print(f"Added calculator {calc['id']}: {calc['slug']}")

# Save updated calculators.json
with open(CALCS_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nTotal calculators now: {len(data['calculators'])}")
print("Calculators added successfully!")
