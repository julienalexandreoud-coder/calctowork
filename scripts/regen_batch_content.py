# -*- coding: utf-8 -*-
"""
Regenerate long_content HTML files for existing batch calculators
using the fixed ContentEngine (translated headers).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from run_batch1 import engine as engine1, CATALOG as catalog1
from run_batch2 import engine as engine2, CATALOG as catalog2

CONTENT_DIR = ROOT / "src" / "content"
LANGS = ["es", "en", "fr", "pt", "de", "it"]

# run_batch2 imports its own engine instance but it's the same class
# We'll use engine1 since the class is identical
engine = engine1

combined = list(catalog1) + list(catalog2)
print(f"Regenerating content for {len(combined)} calculators across {len(LANGS)} languages...")

total = 0
for calc in combined:
    for lang in LANGS:
        html = engine.generate(calc, lang)
        out_path = CONTENT_DIR / lang / f"{calc['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        total += 1

print(f"[OK] Regenerated {total} content files.")
