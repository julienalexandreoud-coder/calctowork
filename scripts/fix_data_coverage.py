#!/usr/bin/env python3
"""
CalcToWork Data Fix Script — Phase 3
Resolves duplicate slugs, fills missing units, expands related, adds buying_units.
Idempotent: safe to re-run.
"""
import json
import os
from collections import Counter

CALCS_PATH = 'src/calculators/calculators.json'
CONTENT_DIR = 'src/content'

def load_calcs():
    with open(CALCS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_calcs(data):
    with open(CALCS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def dedupe_slugs(data):
    calcs = data['calculators']
    by_slug = {}
    for c in calcs:
        by_slug.setdefault(c['slug'], []).append(c)

    renames = {}  # old_slug -> new_slug
    for slug, group in by_slug.items():
        if len(group) <= 1:
            continue
        # Sort by: has content file > number of non-empty fields > id
        def score(c):
            sid = c['id']
            en_file = os.path.join(CONTENT_DIR, 'en', f"{sid}.html")
            has_content = os.path.exists(en_file)
            fields_filled = sum(1 for v in c.values() if v is not None and v != [] and v != {} and v != '')
            return (has_content, fields_filled, -int(sid))
        group.sort(key=score, reverse=True)
        for i, c in enumerate(group):
            if i == 0:
                continue
            old = c['slug']
            new = old + f"-{i+1}"
            c['slug'] = new
            renames[old] = new
            print(f"  Renamed {c['id']} {old} -> {new}")

    # Sweep related references
    for c in calcs:
        new_related = []
        for r in c.get('related', []):
            # r might be an id string; find if any calc was renamed
            # We need to map from old slug to new slug, but related stores IDs.
            # Check if the related ID's calc was renamed and its old slug appears anywhere.
            # Actually, related[] stores IDs like '001', '002'. No slug references there.
            pass
    print(f"Deduped {len(renames)} slugs.")
    return data

def fill_missing_units(data):
    calcs = data['calculators']
    defaults = {
        'length': 'm', 'mass': 'kg', 'time': 's', 'percentage': '%',
        'velocity': 'm/s', 'speed': 'm/s', 'acceleration': 'm/s²',
        'force': 'N', 'energy': 'J', 'power': 'W', 'pressure': 'Pa',
        'area': 'm²', 'volume': 'm³', 'angle': 'deg', 'frequency': 'Hz',
        'digital_storage': 'MB', 'data_rate': 'Mbps', 'density': 'kg/m³',
        'temperature': '°C', 'currency_per_volume': '$/L', 'currency': 'USD',
        'current': 'A', 'voltage': 'V', 'resistance': 'ohm', 'capacitance': 'F',
    }
    count = 0
    for c in calcs:
        if c.get('units'):
            continue
        inferred = {}
        for inp in c.get('inputs', []):
            cat = inp.get('unit_category', '')
            uid = inp.get('id', '')
            if cat and cat in defaults:
                inferred[uid] = defaults[cat]
            elif 'porcent' in uid or 'pct' in uid or 'rate' in uid or 'ratio' in uid:
                inferred[uid] = '%'
            elif 'longitud' in uid or 'largo' in uid or 'ancho' in uid or 'altura' in uid or 'profundidad' in uid or 'height' in uid or 'width' in uid or 'length' in uid:
                inferred[uid] = 'm'
            elif 'peso' in uid or 'masa' in uid or 'weight' in uid or 'mass' in uid:
                inferred[uid] = 'kg'
            elif 'tiempo' in uid or 'time' in uid or 'duracion' in uid or 'duration' in uid:
                inferred[uid] = 's'
        if inferred:
            c['units'] = inferred
            count += 1
    print(f"Filled units on {count} calcs.")
    return data

def expand_related(data):
    calcs = data['calculators']
    by_block = {}
    id_map = {c['id']: c for c in calcs}
    for c in calcs:
        by_block.setdefault(c.get('block_slug', ''), []).append(c['id'])

    improved = 0
    for c in calcs:
        related = c.get('related', [])
        if len(related) >= 4:
            continue
        block = c.get('block_slug', '')
        candidates = [cid for cid in by_block.get(block, []) if cid != c['id'] and cid not in related]
        # Score by formula variable overlap
        def score(cid):
            oc = id_map.get(cid)
            if not oc:
                return 0
            my_inputs = {i['id'] for i in c.get('inputs', []) if i.get('type') == 'number'}
            their_inputs = {i['id'] for i in oc.get('inputs', []) if i.get('type') == 'number'}
            overlap = len(my_inputs & their_inputs)
            return overlap
        candidates.sort(key=score, reverse=True)
        for cid in candidates[:4 - len(related)]:
            related.append(cid)
            improved += 1
        c['related'] = related
    print(f"Expanded related on {improved} slots.")
    return data

def add_buying_units(data):
    calcs = data['calculators']
    patterns = [
        (lambda s: 'tile' in s, {'box': 12, 'sqm_per_box': 1.44}),
        (lambda s: 'paint' in s, {'can_l': 4, 'l_coverage': 12}),
        (lambda s: 'brick' in s, {'pallet': 500}),
        (lambda s: 'concrete' in s and 'bag' in s, {'bag_kg': 25}),
        (lambda s: 'decking' in s, {'board_m': 2.4}),
        (lambda s: 'fence' in s, {'panel': 1.8}),
        (lambda s: 'roof' in s or 'shingle' in s, {'bundle': 3}),
        (lambda s: 'insulation' in s, {'roll': 10}),
        (lambda s: 'plaster' in s, {'bag_kg': 25}),
        (lambda s: 'gravel' in s or 'aggregate' in s, {'tonne': 1}),
    ]
    count = 0
    for c in calcs:
        slug = c.get('slug', '')
        if c.get('buying_units'):
            continue
        for match_fn, bu in patterns:
            if match_fn(slug):
                c['buying_units'] = bu
                count += 1
                break
    print(f"Added buying_units to {count} calcs.")
    return data

def main():
    data = load_calcs()
    print("=== Deduping slugs ===")
    data = dedupe_slugs(data)
    print("=== Filling missing units ===")
    data = fill_missing_units(data)
    print("=== Expanding related ===")
    data = expand_related(data)
    print("=== Adding buying_units ===")
    data = add_buying_units(data)
    save_calcs(data)
    print("Done.")

if __name__ == '__main__':
    main()
