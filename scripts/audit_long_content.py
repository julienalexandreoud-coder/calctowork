import re, sys

with open('scripts/calc_content.py', 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'LONG_CONTENT = {LONG_CONTENT = {'
section = content.split(marker, 1)
if len(section) < 2:
    print("ERROR: marker not found")
    sys.exit(1)

body = section[1].split('\ndef generate_long_content')[0]

ids = re.findall(r'"(\d{3})"\s*:\s*\{', body)
print(f'Total calc IDs in LONG_CONTENT: {len(ids)}')

en_count = len(re.findall(r'"en":\s*"""', body))
es_count = len(re.findall(r'"es":\s*"""', body))
print(f'EN entries: {en_count}')
print(f'ES entries: {es_count}')

# Split into individual calc blocks and analyze quality
blocks = re.split(r'\n\s+"(\d{3})"\s*:\s*\{', body)

en_rich = 0
en_thin = 0
es_rich = 0
es_thin = 0
thin_details = []

i = 1
while i < len(blocks) - 1:
    cid = blocks[i]
    block_content = blocks[i+1]
    i += 2

    for lang in ['en', 'es']:
        lang_match = re.search(r'"' + lang + r'":\s*"""(.*?)"""', block_content, re.DOTALL)
        if not lang_match:
            continue
        html = lang_match.group(1)
        words = len(html.split())
        has_faq = 'faq-item' in html or 'faq-q' in html
        has_examples = bool(re.search(r'Example|Ejemplo|ejemplo', html))
        has_mistakes = bool(re.search(r'Mistake|Error|error', html))
        sections = len(re.findall(r'<h2', html))
        has_protip = bool(re.search(r'Pro tip|Pro Tip|tip', html, re.IGNORECASE))
        has_related = bool(re.search(r'Related|Relacionad|Ver tamb', html))
        score = sum([has_faq, has_examples, has_mistakes, sections >= 5, has_protip])

        if score >= 3 and words >= 500:
            if lang == 'en': en_rich += 1
            else: es_rich += 1
        else:
            if lang == 'en': en_thin += 1
            else: es_thin += 1
            if lang == 'en':
                thin_details.append(f'{cid}|{lang}|{words}w|{sections}sec|faq={has_faq}|ex={has_examples}|mist={has_mistakes}|protip={has_protip}|score={score}')

print(f'\nEN: {en_rich} rich (score>=3, 500+words), {en_thin} thin')
print(f'ES: {es_rich} rich, {es_thin} thin')
print(f'\n=== THIN EN DETAILS (need improvement) ===')
for d in thin_details:
    print(d)
