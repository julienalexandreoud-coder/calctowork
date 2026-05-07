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
    # Find end of opening tag
    tag_end = text.find('>', start) + 1
    # Walk forward tracking open/close <section> depth, starting at depth=1
    depth = 1
    pos = tag_end
    while pos < len(text) and depth > 0:
        next_open = text.lower().find('<section', pos)
        next_close = text.lower().find('</section', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 8
        else:
            depth -= 1
            if depth == 0:
                end = text.find('>', next_close) + 1
                return text[start:end].strip()
            pos = next_close + 9
    return None


def is_full_document(text: str) -> bool:
    head = text[:500].lower()
    tail = text[-500:].lower()
    return ("<!doctype" in head or "<html" in head
            or "</body>" in tail or "</html>" in tail or "</footer>" in tail)


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
