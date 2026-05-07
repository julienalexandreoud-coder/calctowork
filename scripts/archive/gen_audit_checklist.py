import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tools_config import TOOL_BY_ID

calcs = json.load(open('src/calculators/calculators.json', encoding='utf-8'))['calculators']
i18n = {lang: json.load(open(f'src/i18n/{lang}.json', encoding='utf-8'))['calculators'] for lang in ['en','es','fr','de','it','pt']}

lines = []
lines.append('# CalcToWork Calculator Audit Checklist')
lines.append('')
lines.append('**Goal:** Verify every calculator works correctly, produces accurate results, and has good SEO.')
lines.append('')
lines.append('**Rules:**')
lines.append('- Check one calculator at a time.')
lines.append('- Do NOT skip any item.')
lines.append('- Mark complete only after testing the live page.')
lines.append('')
lines.append('---')
lines.append('')

lines.append('## Audit Criteria (for each calculator)')
lines.append('')
lines.append('For every calculator page, verify:')
lines.append('')
lines.append('1. **Formula Accuracy**')
lines.append('   - [ ] Open the calculator page')
lines.append('   - [ ] Enter test values (use the example values from the article if available)')
lines.append('   - [ ] Press Calculate')
lines.append('   - [ ] Result matches expected value (cross-check with manual calculation or known formula)')
lines.append('   - [ ] All output fields populate correctly')
lines.append('   - [ ] Edge cases handled (zero, negative, very large values)')
lines.append('')
lines.append('2. **UI Consistency**')
lines.append('   - [ ] Form has same structure as other calculators (grouped inputs, labels, units)')
lines.append('   - [ ] Calculate button works (click and/or auto-calculate)')
lines.append('   - [ ] Copy Results button appears after calculation and works')
lines.append('   - [ ] Share button appears after calculation and works')
lines.append('   - [ ] Favorite (heart) button works')
lines.append('   - [ ] Reset button clears form')
lines.append('   - [ ] No console errors in browser dev tools')
lines.append('')
lines.append('3. **SEO and Metadata**')
lines.append('   - [ ] Title tag is descriptive and includes year/keyword where appropriate')
lines.append('   - [ ] Meta description > 50 characters and accurately describes the tool')
lines.append('   - [ ] Canonical URL is correct')
lines.append('   - [ ] Hreflang tags present for all 6 languages')
lines.append('   - [ ] OG image present')
lines.append('   - [ ] Schema.org JSON-LD present (SoftwareApplication + Article/FAQ)')
lines.append('')
lines.append('4. **Content Quality**')
lines.append('   - [ ] Long-form article present (not fallback/template text)')
lines.append('   - [ ] Article is relevant to the calculator topic')
lines.append('   - [ ] No broken characters (A tilde, question mark box, etc.)')
lines.append('   - [ ] Featured snippet box at top (if applicable)')
lines.append('   - [ ] Step-by-step guide matches calculator inputs')
lines.append('   - [ ] FAQ questions are relevant')
lines.append('')
lines.append('5. **i18n Completeness**')
lines.append('   - [ ] Input labels make sense in all 6 languages')
lines.append('   - [ ] Output labels make sense in all 6 languages')
lines.append('   - [ ] Button text translated')
lines.append('   - [ ] No placeholder text like Calculator 1105')
lines.append('')
lines.append('---')
lines.append('')

blocks = {}
for c in calcs:
    cid = c['id']
    if cid not in TOOL_BY_ID:
        continue
    block = c.get('block_slug', 'unknown')
    if block not in blocks:
        blocks[block] = []
    blocks[block].append(c)

block_names = {
    'estructuras': 'Estructuras (Structures)',
    'mamposteria': 'Mamposteria (Masonry)',
    'pavimentos': 'Pavimentos (Flooring)',
    'fontaneria': 'Fontaneria (Plumbing)',
    'electricidad': 'Electricidad (Electrical)',
    'climatizacion': 'Climatizacion (HVAC)',
    'carpinteria': 'Carpinteria (Carpentry)',
    'pintura': 'Pintura (Painting)',
    'gestion': 'Gestion (Management)',
    'matematicas': 'Matematicas (Math)',
    'finanzas': 'Finanzas (Finance)',
    'salud': 'Salud (Health)',
    'cotidiano': 'Cotidiano (Daily Life)',
    'estadistica': 'Estadistica (Statistics)',
    'ciencia': 'Ciencia (Science)',
    'conversion': 'Conversion (Conversion)',
    'deportes': 'Deportes (Sports)',
    'quimica': 'Quimica (Chemistry)',
    'electronica': 'Electronica (Electronics)',
    'clima': 'Clima (Weather)',
    'utilidades': 'Utilidades (Utilities)',
    'fotografia': 'Fotografia (Photography)',
    'transporte': 'Transporte (Transport)',
    'ingenieria': 'Ingenieria (Engineering)',
}

total = 0
for block, items in blocks.items():
    name = block_names.get(block, block)
    lines.append('## ' + name + ' (' + str(len(items)) + ' calculators)')
    lines.append('')
    for c in items:
        cid = c['id']
        slug = c['slug']
        ci18n = i18n['en'].get(cid, {})
        name_en = ci18n.get('name', slug)
        seo_desc = ci18n.get('seo_description', '')
        content_file = 'src/content/en/' + cid + '.html'
        has_content = os.path.exists(content_file)
        content_status = 'Tier A (handcrafted)' if has_content else 'Tier B/C (fallback)'
        desc_len = len(seo_desc)
        desc_status = 'OK (' + str(desc_len) + ' chars)' if desc_len > 50 else 'TOO SHORT (' + str(desc_len) + ' chars)'
        
        lines.append('### ' + cid + ' - ' + name_en)
        lines.append('- Slug: `' + slug + '`')
        lines.append('- Content: ' + content_status)
        lines.append('- SEO desc: ' + desc_status)
        lines.append('')
        lines.append('- [ ] Formula tested and accurate')
        lines.append('- [ ] UI consistent (buttons, copy, share, fav)')
        lines.append('- [ ] SEO title + description good')
        lines.append('- [ ] Content quality OK')
        lines.append('- [ ] i18n complete (all 6 languages)')
        lines.append('')
        total += 1
    lines.append('---')
    lines.append('')

lines.append('**Total: ' + str(total) + ' calculators to audit**')
lines.append('')
lines.append('## Audit Log')
lines.append('')
lines.append('| Date | Calculator ID | Auditor | Notes |')
lines.append('|------|---------------|---------|-------|')
lines.append('| | | | |')

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Wrote CALCULATOR_AUDIT.md with ' + str(total) + ' calculators')
