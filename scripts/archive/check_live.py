import urllib.request
import re

BASE = "https://calcto.work"
PAGES = [
    "/es/hormigon-masa/",
    "/en/plain-concrete/",
    "/fr/beton-masse/",
    "/de/beton-unbewehr/",
    "/it/calcestruzzo-massa/",
    "/pt/concreto-maco/",
]

print("Checking live deployed pages...")
for path in PAGES:
    try:
        url = BASE + path
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8')
        
        title = re.search(r'<title>(.*?)</title>', html)
        desc = re.search(r'<meta name="description" content="([^"]*)"', html)
        has_calc = 'calculator.js' in html
        has_content = 'long-content' in html
        robots = re.search(r'<meta name="robots" content="([^"]*)"', html)
        robots_val = robots.group(1) if robots else "missing"
        
        print(f"{path}")
        print(f"  Title: {title.group(1) if title else 'MISSING'}")
        print(f"  Desc: {desc.group(1)[:60] if desc else 'MISSING'}...")
        print(f"  Calculator JS: {'YES' if has_calc else 'NO'}")
        print(f"  Long content: {'YES' if has_content else 'NO'}")
        print(f"  Robots: {robots_val}")
        print()
    except Exception as e:
        print(f"{path} ERROR: {e}")
        print()

# Check ads.txt
print("Checking ads.txt...")
try:
    url = BASE + "/ads.txt"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8')
    print(f"  ads.txt content: {content.strip()}")
except Exception as e:
    print(f"  ads.txt ERROR: {e}")

# Check sitemap
print("\nChecking sitemap.xml...")
try:
    url = BASE + "/sitemap.xml"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8')
    if '<sitemapindex' in content:
        print("  Sitemap index present")
    else:
        print("  Sitemap present")
except Exception as e:
    print(f"  sitemap ERROR: {e}")
