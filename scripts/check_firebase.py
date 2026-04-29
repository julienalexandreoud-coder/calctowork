import urllib.request
import re

BASE = "https://calcto.work.web.app"
PAGES = [
    "/es/hormigon-masa/",
    "/en/",
    "/fr/",
    "/de/",
]

print("Checking Firebase deployed pages...")
for path in PAGES:
    try:
        url = BASE + path
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8')
        
        title = re.search(r'<title>(.*?)</title>', html)
        has_calc = 'calculator.js' in html
        has_content = 'long-content' in html
        
        print(f"{path} -> Status: OK")
        print(f"  Title: {title.group(1) if title else 'MISSING'}")
        print(f"  Has calc JS: {has_calc}")
        print(f"  Has content: {has_content}")
    except Exception as e:
        print(f"{path} -> ERROR: {e}")
    print()

# Check ads.txt
print("Checking ads.txt...")
try:
    url = BASE + "/ads.txt"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8')
    print(f"  ads.txt: {content.strip()}")
except Exception as e:
    print(f"  ads.txt ERROR: {e}")
