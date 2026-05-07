from run_batch1 import CATALOG, engine, LANGS, CONTENT_DIR

for calc in CATALOG:
    for lang in LANGS:
        html = engine.generate(calc, lang)
        out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
        out_path.write_text(html, encoding="utf-8")

print(f"[OK] Regenerated {len(CATALOG) * len(LANGS)} content files")
