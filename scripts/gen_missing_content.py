import sys
sys.path.insert(0, 'scripts')
from calc_content import generate_long_content

# Generate missing content files
missing = [
    ('de', '700', 'velocidad'),
    ('de', '800', 'longitud'),
    ('pt', '800', 'longitud'),
    ('de', '802', 'temperatura'),
    ('pt', '802', 'temperatura'),
    ('de', '900', 'ritmo-carrera'),
    ('pt', '900', 'ritmo-carrera'),
]

for lang, cid, slug in missing:
    content = generate_long_content(cid, lang, calc_name=slug)
    if content:
        path = f'src/content/{lang}/{cid}.html'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {path} ({len(content.split())} words)")
    else:
        print(f"FAILED to generate {lang}/{cid}")
