import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://calcto.work"
PAGES = [
    "/es/calculadora-hormigon-masa/",
    "/en/percentage-calculator/",
    "/fr/calculateur-imc/",
    "/de/beton-rechner/",
    "/it/calcolatore-bmi/",
    "/pt/calculadora-juros-compostos/",
]

print("Checking live calculator pages...")
for path in PAGES:
    try:
        url = BASE + path
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            html = resp.read().decode('utf-8')
        
        title = re.search(r'<title>(.*?)</title>', html)
        desc = re.search(r'<meta name="description" content="([^"]*)"', html)
        has_calc = 'calculator.js' in html
        has_content = 'long-content' in html
        robots = re.search(r'<meta name="robots" content="([^"]*)"', html)
        canonical = re.search(r'<link rel="canonical" href="([^"]*)"', html)
        hreflangs = re.findall(r'rel="alternate" hreflang="([^"]*)"', html)
        
        print(f"{path} -> OK")
        print(f"  Title: {title.group(1)[:70] if title else 'MISSING'}")
        print(f"  Desc: {desc.group(1)[:60] if desc else 'MISSING'}...")
        print(f"  Calc JS: {'YES' if has_calc else 'NO'}")
        print(f"  Content: {'YES' if has_content else 'NO'}")
        print(f"  Robots: {robots.group(1) if robots else 'missing'}")
        print(f"  Canonical: {canonical.group(1)[:50] if canonical else 'missing'}")
        print(f"  Hreflangs: {len(hreflangs)} tags")
    except Exception as e:
        print(f"{path} -> ERROR: {e}")
    print()

# Check parametric page has noindex
print("Checking parametric page...")
try:
    url = BASE + "/es/calculadora-aire-acondicionado-btu/10m2-2-4m/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
        html = resp.read().decode('utf-8')
    robots = re.search(r'<meta name="robots" content="([^"]*)"', html)
    print(f"  Robots tag: {robots.group(1) if robots else 'MISSING'}")
except Exception as e:
    print(f"  ERROR: {e}")
