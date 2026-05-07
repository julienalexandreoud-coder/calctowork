import urllib.request
import re
import ssl

# Disable SSL verification for this check
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://calcto.work"
PAGES = [
    "/es/hormigon-masa/",
    "/en/",
    "/fr/",
    "/de/",
    "/it/",
    "/pt/",
]

print("Checking live site pages...")
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
        
        print(f"{path} -> OK")
        print(f"  Title: {title.group(1)[:70] if title else 'MISSING'}")
        print(f"  Desc: {desc.group(1)[:60] if desc else 'MISSING'}...")
        print(f"  Calc JS: {'YES' if has_calc else 'NO'}")
        print(f"  Content: {'YES' if has_content else 'NO'}")
        print(f"  Robots: {robots.group(1) if robots else 'missing'}")
    except Exception as e:
        print(f"{path} -> ERROR: {e}")
    print()

# Check ads.txt
print("Checking ads.txt...")
try:
    url = BASE + "/ads.txt"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
        content = resp.read().decode('utf-8')
    print(f"  ads.txt: {content.strip()}")
except Exception as e:
    print(f"  ads.txt ERROR: {e}")
