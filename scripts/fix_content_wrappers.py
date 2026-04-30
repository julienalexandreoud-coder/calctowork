"""Strip full-HTML document wrappers from content fragment files.

Content files should contain only HTML fragments (a <section class="long-content"> block).
119 files were incorrectly generated as full HTML pages. This script extracts just the
<section class="long-content"> fragment and rewrites each file.
"""
import re
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "src" / "content"

# Pattern to find the start of the actual content fragment
FRAGMENT_PATTERN = re.compile(
    r'(<section\s[^>]*class=["\'][^"\']*long-content[^"\']*["\'][^>]*>)',
    re.IGNORECASE
)


def extract_fragment(text: str) -> str | None:
    """Extract the <section class="long-content">...</section> fragment from a full HTML doc."""
    m = FRAGMENT_PATTERN.search(text)
    if not m:
        return None
    start = m.start()
    # Find the matching closing </section> by counting open/close tags
    depth = 0
    pos = start
    while pos < len(text):
        open_m = re.search(r'<section\b', text[pos:], re.IGNORECASE)
        close_m = re.search(r'</section\s*>', text[pos:], re.IGNORECASE)
        if not close_m:
            break
        close_abs = pos + close_m.start()
        open_abs = pos + open_m.start() if open_m else len(text)
        if open_abs < close_abs:
            depth += 1
            pos = open_abs + 1
        else:
            if depth == 0:
                end = close_abs + len(close_m.group())
                return text[start:end].strip()
            depth -= 1
            pos = close_abs + 1
    # Fallback: return everything from the section start
    return text[start:].strip()


def is_full_document(text: str) -> bool:
    head = text[:500].lower()
    return "<!doctype" in head or "<html" in head


fixed = 0
errors = 0
skipped = 0

for path in sorted(CONTENT_DIR.rglob("*.html")):
    text = path.read_text(encoding="utf-8")
    if not is_full_document(text):
        skipped += 1
        continue
    fragment = extract_fragment(text)
    if fragment is None:
        print(f"  [WARN] No <section class='long-content'> found in {path.name} — skipping")
        errors += 1
        continue
    path.write_text(fragment + "\n", encoding="utf-8")
    fixed += 1

print(f"\nFixed: {fixed} files")
print(f"Skipped (already fragments): {skipped} files")
print(f"Could not fix: {errors} files")
