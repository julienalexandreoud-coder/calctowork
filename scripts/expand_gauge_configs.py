#!/usr/bin/env python3
"""Expand GAUGE_CONFIGS in generate_calctowork.py for percentage/rate/efficiency/ratio calcs."""
import json
import re

with open('src/calculators/calculators.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

calcs = data['calculators']

# Load existing gauge configs
with open('scripts/generate_calctowork.py', 'r', encoding='utf-8') as f:
    gen = f.read()

# Extract existing GAUGE_CONFIGS
m = re.search(r'GAUGE_CONFIGS = \{([^}]+)\}', gen, re.DOTALL)
if not m:
    print("Could not find GAUGE_CONFIGS")
    exit(1)

existing = {}
for line in m.group(1).strip().split('\n'):
    line = line.strip().rstrip(',')
    if not line:
        continue
    parts = line.split(':', 1)
    if len(parts) == 2:
        key = parts[0].strip().strip('"')
        existing[key] = line

patterns = [
    (r'porcent|percent|pct|ratio|rate|score|effici|eficien|rendimiento|ahorro|interes|tasa|margen|retorno|roi|yield|wacc|apr|cagr|cap.rate|body.fat|grasa|humedad|humidity|uptime|dividend|a1c|bai|bfp|tax|real|thermal|cop|eer', 'percentage'),
]

added = 0
for c in calcs:
    cid = c['id']
    if cid in existing:
        continue
    slug = c.get('slug', '')
    outputs = c.get('outputs', [])
    first_out = ''
    if isinstance(outputs, list) and outputs:
        first_out = outputs[0] if isinstance(outputs[0], str) else outputs[0].get('label', '') if isinstance(outputs[0], dict) else ''
    elif isinstance(outputs, dict) and outputs:
        first_out = list(outputs.values())[0]
    matched = False
    for pat, kind in patterns:
        if re.search(pat, slug, re.I) or re.search(pat, first_out, re.I):
            matched = True
            break
    if matched:
        existing[cid] = f'    "{cid}":                 {{"min": 0, "max": 100, "label": "%", "unit": "%"}}'
        added += 1

print(f"Added {added} new gauge configs.")

# Rebuild the dict block
lines = ['GAUGE_CONFIGS = {']
for k in sorted(existing.keys(), key=lambda x: int(x) if x.isdigit() else x):
    lines.append(existing[k] + ',')
lines.append('}')

new_gen = gen[:m.start()] + '\n'.join(lines) + gen[m.end():]
with open('scripts/generate_calctowork.py', 'w', encoding='utf-8') as f:
    f.write(new_gen)
print("Updated generator.")
