"""
Add internal links to content files by injecting a contextual "see also" sentence
near the end of the intro paragraph, using each calc's related[] field.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "src" / "content" / "en"
CALCS_JSON = ROOT / "src" / "calculators" / "calculators.json"
I18N_EN = ROOT / "src" / "i18n" / "en.json"

data = json.loads(CALCS_JSON.read_text(encoding="utf-8"))
calcs = data["calculators"]
calcs_by_id = {c["id"]: c for c in calcs}
i18n = json.loads(I18N_EN.read_text(encoding="utf-8"))
calcs_i18n = i18n.get("calculators", {})

calc_info = {}
for c in calcs:
    ci = calcs_i18n.get(c["id"], {})
    name = ci.get("name", "")
    slug = c.get("slug", "")
    if name and slug:
        calc_info[c["id"]] = {"name": name, "slug": slug}

content_files = sorted(
    CONTENT_DIR.glob("*.html"),
    key=lambda f: f.stat().st_size,
    reverse=True
)

ALREADY_LINKED = re.compile(r'<a\s+href="/en/[^"]+">.*?</a>', re.IGNORECASE)
INJECTION_MARKER = "<!-- internal-links-added -->"

total_links = 0
files_changed = 0

for content_file in content_files:
    cid = content_file.stem
    calc = calcs_by_id.get(cid)
    if not calc:
        continue

    related_ids = [str(r) for r in calc.get("related", [])]
    if not related_ids:
        continue

    html = content_file.read_text(encoding="utf-8")

    # Skip if already processed
    if INJECTION_MARKER in html:
        continue

    # Build link list for related calcs (up to 3)
    link_parts = []
    for rel_id in related_ids[:3]:
        info = calc_info.get(rel_id)
        if not info:
            continue
        link_parts.append(f'<a href="/en/{info["slug"]}/">{info["name"]}</a>')

    if not link_parts:
        continue

    # Find the first closing </p> tag after the opening <section> to inject after
    # We look for the end of the first substantial paragraph (after intro h2)
    inject_after = "</p>"
    idx = html.find(inject_after)
    if idx == -1:
        continue

    # Build the "see also" sentence
    if len(link_parts) == 1:
        see_also = f"You may also find the {link_parts[0]} useful."
    elif len(link_parts) == 2:
        see_also = f"You may also find the {link_parts[0]} and {link_parts[1]} useful."
    else:
        see_also = f"You may also find the {link_parts[0]}, {link_parts[1]}, and {link_parts[2]} useful."

    injection = f'\n  <p class="see-also">{see_also}</p>\n  {INJECTION_MARKER}'

    new_html = html[:idx + len(inject_after)] + injection + html[idx + len(inject_after):]
    content_file.write_text(new_html, encoding="utf-8")

    added = len(link_parts)
    total_links += added
    files_changed += 1
    print(f"  [+{added} links] {cid} {calc.get('slug','')}")

print(f"\n[DONE] Added {total_links} internal links across {files_changed} content files")
