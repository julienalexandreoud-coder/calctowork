import os, re, glob, random
PUBLIC = r"C:\Microsaas\obra\public"
pages = []
for lang in ["es", "en", "fr", "pt", "de", "it"]:
    lang_dir = os.path.join(PUBLIC, lang)
    if not os.path.exists(lang_dir):
        continue
    all_pages = glob.glob(os.path.join(lang_dir, "*", "index.html"))
    if all_pages:
        pages.extend(random.sample(all_pages, min(2, len(all_pages))))

errors = 0
for page in pages:
    rel = os.path.relpath(page, PUBLIC)
    with open(page, "r", encoding="utf-8") as f:
        c = f.read()

    issues = []
    if not c.startswith("<!DOCTYPE html>"):
        issues.append("bad doctype")
    if "<html" not in c:
        issues.append("no html tag")
    if "</html>" not in c:
        issues.append("no closing html")
    if "<head>" not in c:
        issues.append("no head")
    if "<body>" not in c:
        issues.append("no body")
    if "</body>" not in c:
        issues.append("no closing body")
    if "<title>" not in c:
        issues.append("no title")

    open_scripts = c.count("<script")
    close_scripts = c.count("</script>")
    if open_scripts != close_scripts:
        issues.append(f"script mismatch: {open_scripts} vs {close_scripts}")

    if issues:
        print(f"{rel}: {issues}")
        errors += 1

if errors == 0:
    print(f"All {len(pages)} sampled pages pass HTML structure check")
else:
    print(f"{errors} pages have issues")
