import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tools_config import TOOL_BY_ID

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
i18n = json.load(open('src/i18n/en.json', encoding='utf-8'))['calculators']

# Define block priority order
BLOCK_PRIORITY = [
    'estructuras', 'pavimentos', 'mamposteria', 'pintura', 'carpinteria',
    'fontaneria', 'electricidad', 'climatizacion', 'gestion',
    'matematicas', 'finanzas', 'salud', 'cotidiano', 'estadistica',
    'ciencia', 'conversion', 'deportes', 'quimica', 'electronica',
    'clima', 'utilidades', 'fotografia', 'transporte', 'ingenieria'
]

# Group calculators by block
blocks = {}
for c in calcs:
    cid = c['id']
    if cid not in TOOL_BY_ID:
        continue
    block = c.get('block_slug', 'unknown')
    if block not in blocks:
        blocks[block] = []
    blocks[block].append(c)

# Sort blocks by priority, then by ID within each block
sorted_calcs = []
for block in BLOCK_PRIORITY:
    if block in blocks:
        sorted_calcs.extend(sorted(blocks[block], key=lambda x: int(x['id'])))

# Add any remaining blocks not in priority list
for block, items in blocks.items():
    if block not in BLOCK_PRIORITY:
        sorted_calcs.extend(sorted(items, key=lambda x: int(x['id'])))

print(f'Total calculators in order: {len(sorted_calcs)}')

# Build the markdown file
lines = []

# Header
lines.append('# CalcToWork Calculator Audit Checklist')
lines.append('')
lines.append('**Goal:** Verify every calculator works correctly, produces accurate results, and has good SEO.')
lines.append('')
lines.append('**Rules:**')
lines.append('- Check one calculator at a time.')
lines.append('- Do NOT skip any item.')
lines.append('- Mark complete only after testing the live page.')
lines.append('- Record findings in the Audit Log at the bottom immediately after each check.')
lines.append('')
lines.append('## Progress Tracker')
lines.append('')
lines.append('| Status | Count | Percentage |')
lines.append('|--------|-------|------------|')
lines.append('| Total | 441 | 100% |')
lines.append('| Audited | 0 | 0% |')
lines.append('| Pass | 0 | 0% |')
lines.append('| Fail | 0 | 0% |')
lines.append('| Partial | 0 | 0% |')
lines.append('| Remaining | 441 | 100% |')
lines.append('')
lines.append('*Update this table after each audit session.*')
lines.append('')
lines.append('## Audit Order')
lines.append('')
lines.append('Calculators are listed in priority order (highest first):')
lines.append('1. `estructuras` → `pavimentos` → `mamposteria` → `pintura` (construction core)')
lines.append('2. `carpinteria` → `fontaneria` → `electricidad` → `climatizacion` (building systems)')
lines.append('3. `gestion` (construction management)')
lines.append('4. `matematicas` → `finanzas` → `salud` (large blocks, verify carefully)')
lines.append('5. Remaining blocks (ciencia, conversion, deportes, etc.)')
lines.append('')
lines.append('## How to Record Findings')
lines.append('')
lines.append('1. Open the calculator URL (live site)')
lines.append('2. Work through all 9 checkboxes systematically')
lines.append('3. In the Audit Log at bottom, record:')
lines.append('   - **Date**: When you checked')
lines.append('   - **Calculator ID**: e.g. `001`')
lines.append('   - **Status**: `PASS` / `FAIL` / `PARTIAL`')
lines.append('   - **Issues**: Brief description (e.g. "Formula wrong", "ES missing units")')
lines.append('   - **Fixed**: `Y` / `N` / `PENDING`')
lines.append('   - **Notes**: Any additional context')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Audit Checklist (441 Calculators)')
lines.append('')

# Per-calculator checklist template
def calc_checklist(cid, slug, name_en, content_tier, seo_desc_len):
    content_status = 'Tier A' if content_tier else 'Tier B/C'
    desc_status = 'OK' if seo_desc_len > 50 else f'SHORT ({seo_desc_len})'
    
    lines = []
    lines.append(f'### {cid}. {name_en}')
    lines.append(f'**Slug:** `{slug}` | **Content:** {content_status} | **SEO:** {desc_status}')
    lines.append('')
    lines.append(f'- [ ] Formula + answer quality (precision, units, formatting, rounding, buying units)')
    lines.append(f'- [ ] UI consistent (buttons, copy, share, fav)')
    lines.append(f'- [ ] SEO title + description good')
    lines.append(f'- [ ] Content quality OK')
    lines.append(f'- [ ] i18n deep check (labels, units, selects, numbers, currency, pluralization)')
    lines.append(f'- [ ] Unit conversion + share prefill work')
    lines.append(f'- [ ] Analytics events fire (calc, fav, share)')
    lines.append(f'- [ ] Mobile + dark mode OK')
    lines.append(f'- [ ] Ads + affiliates load correctly')
    lines.append('')
    return '\n'.join(lines)

# Add each calculator
for i, c in enumerate(sorted_calcs, 1):
    cid = c['id']
    slug = c['slug']
    ci18n = i18n.get(cid, {})
    name_en = ci18n.get('name', slug)
    seo_desc = ci18n.get('seo_description', '')
    content_file = f'src/content/en/{cid}.html'
    has_content = os.path.exists(content_file)
    
    lines.append(calc_checklist(cid, slug, name_en, has_content, len(seo_desc)))

lines.append('---')
lines.append('')
lines.append('## Audit Log')
lines.append('')
lines.append('| # | Date | Calc ID | Slug | Status | Issues Found | Fixed | Auditor | Notes |')
lines.append('|---|------|---------|------|--------|--------------|-------|---------|-------|')
lines.append('| 1 | | | | | | | | |')
lines.append('')
lines.append('**Status codes:** `PASS` = all checks green, `FAIL` = critical issue, `PARTIAL` = minor issues only')
lines.append('')
lines.append('**Issue codes:** `F` = Formula, `U` = UI, `S` = SEO, `C` = Content, `I` = i18n, `A` = Analytics, `M` = Mobile, `R` = Revenue/Ads')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Quick Reference: Calculator URLs')
lines.append('')
lines.append('**Base URL pattern:** `https://calcto.work/{lang}/{slug}/`')
lines.append('')
lines.append('**Example:** Calculator 001 (hormigon-masa)')
lines.append('- EN: https://calcto.work/en/mass-concrete-calculator/')
lines.append('- ES: https://calcto.work/es/calculadora-hormigon-masa/')
lines.append('- FR: https://calcto.work/fr/calculateur-beton-masse/')
lines.append('- PT: https://calcto.work/pt/calculadora-concreto-massa/')
lines.append('- DE: https://calcto.work/de/stampfbeton-rechner/')
lines.append('- IT: https://calcto.work/it/calcolatore-calcestruzzo-massa/')
lines.append('')

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Wrote CALCULATOR_AUDIT.md with {len(sorted_calcs)} calculators in priority order')
