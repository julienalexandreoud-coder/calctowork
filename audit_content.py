"""Audit all calculators for long-form content quality"""
import json
import os
import glob

# Load all calculators
calcs = json.loads(open('src/calculators/calculators.json', encoding='utf-8').read())['calculators']

# Load i18n names
i18n = {}
with open('src/i18n/en.json', encoding='utf-8') as f:
    for cid, data in json.load(f).get('calculators', {}).items():
        i18n[cid] = data.get('name', '')

print("=" * 80)
print("CALCULATOR LONG-FORM CONTENT AUDIT")
print("=" * 80)

results = []

for calc in calcs:
    cid = calc['id']
    slug = calc.get('slug', '')
    name = i18n.get(cid, '')
    block = calc.get('block_slug', '?')
    
    # Check source content file
    src_file = f'src/content/en/{cid}.html'
    src_exists = os.path.exists(src_file)
    src_content = ''
    src_words = 0
    src_quality = 'NONE'
    
    if src_exists:
        src_content = open(src_file, encoding='utf-8').read()
        src_words = len(src_content.split())
        
        # Check quality indicators
        has_section = '<section class="long-content">' in src_content
        has_faq = 'faq-item' in src_content.lower()
        has_examples = 'Example' in src_content
        has_formula = 'formula' in src_content.lower() or 'how' in src_content.lower()
        has_steps = '<ol>' in src_content or '<li>' in src_content
        
        if src_words < 200:
            src_quality = 'THIN'
        elif not has_faq or not has_examples:
            src_quality = 'PARTIAL'
        elif has_section and has_faq and has_examples and has_formula:
            src_quality = 'COMPLETE'
        else:
            src_quality = 'GOOD'
    
    # Check generated page
    import glob
    matches = glob.glob(f'public/en/**/{slug}/index.html', recursive=True)
    page_words = 0
    has_long_content = False
    
    if matches:
        page_content = open(matches[0], encoding='utf-8').read()
        page_words = len(page_content.split())
        has_long_content = 'long-content' in page_content
    
    results.append({
        'id': cid,
        'slug': slug,
        'name': name,
        'block': block,
        'src_words': src_words,
        'src_quality': src_quality,
        'page_words': page_words,
        'has_long': has_long_content
    })

# Group by quality
complete = [r for r in results if r['src_quality'] == 'COMPLETE']
good = [r for r in results if r['src_quality'] == 'GOOD']
partial = [r for r in results if r['src_quality'] == 'PARTIAL']
thin = [r for r in results if r['src_quality'] == 'THIN']
none = [r for r in results if r['src_quality'] == 'NONE']

print(f"\nTotal calculators: {len(results)}")
print(f"\n{'COMPLETE':<12} {len(complete):>4} calculators ({len(complete)*100//len(results)}%)")
print(f"{'GOOD':<12} {len(good):>4} calculators")
print(f"{'PARTIAL':<12} {len(partial):>4} calculators")
print(f"{'THIN':<12} {len(thin):>4} calculators")
print(f"{'NONE':<12} {len(none):>4} calculators")

print("\n" + "=" * 80)
print("CALCULATORS WITHOUT QUALITY LONG-FORM CONTENT")
print("=" * 80)

needs_work = partial + thin + none
needs_work.sort(key=lambda x: x['block'])

current_block = ''
for r in needs_work:
    if r['block'] != current_block:
        current_block = r['block']
        print(f"\n### {current_block.upper()} ###")
    
    status = 'THIN' if r['src_words'] > 0 and r['src_words'] < 500 else ('NONE' if r['src_words'] == 0 else 'PARTIAL')
    print(f"  {r['id']}: {r['name'][:50]:<50} ({r['slug']}) [{status}, {r['src_words']} words]")

print("\n" + "=" * 80)
print("SAMPLE OF COMPLETE CONTENT (for reference)")
print("=" * 80)
for r in complete[:5]:
    print(f"  {r['id']}: {r['name'][:45]} ({r['src_words']} words)")

print(f"\n\nSummary: {len(needs_work)} of {len(results)} calculators need content work")
