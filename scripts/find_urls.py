import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://calcto.work"

# Try various possible slugs for calculator 001 (concrete mass)
slugs_to_try = [
    "/es/hormigon-masa/",
    "/es/calculadora-hormigon-masa/",
    "/es/hormigon/",
    "/es/calculadora-hormigon/",
]

print("Trying to find calculator 001 page...")
for slug in slugs_to_try:
    try:
        url = BASE + slug
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode('utf-8')
        title = re.search(r'<title>(.*?)</title>', html)
        print(f"{slug} -> FOUND: {title.group(1)[:60] if title else 'no title'}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"{slug} -> 404")
        else:
            print(f"{slug} -> HTTP {e.code}")
    except Exception as e:
        print(f"{slug} -> ERROR: {e}")

# Also try sitemap to get valid URLs
print("\nFetching sitemap to get valid URLs...")
try:
    url = BASE + "/sitemap-es.xml"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
        sitemap = resp.read().decode('utf-8')
    urls = re.findall(r'<loc>([^<]+)</loc>', sitemap)
    print(f"Found {len(urls)} URLs in Spanish sitemap")
    for u in urls[:10]:
        print(f"  {u}")
except Exception as e:
    print(f"Sitemap error: {e}")
