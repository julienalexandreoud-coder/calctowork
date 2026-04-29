import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://calcto.work"

# Check a specific content that ONLY exists because of our restoration
# Check German concrete page which was restored from git history
url = BASE + "/de/beton-unbewehr/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        html = resp.read().decode('utf-8')
    
    title = re.search(r'<title>(.*?)</title>', html)
    has_content = 'long-content' in html
    has_calc = 'calculator.js' in html
    
    print("German concrete page (/de/beton-unbewehr/):")
    print("  Status:", resp.status)
    print("  Title:", title.group(1) if title else 'MISSING')
    print("  Has content:", 'YES' if has_content else 'NO')
    print("  Has calc JS:", 'YES' if has_calc else 'NO')
    
    # Extract first paragraph to verify it's high-quality German content
    m = re.search(r'class="long-content"[^>]*>(.*?)</section>', html, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', ' ', m.group(1))
        words = len(text.split())
        print("  Word count:", words)
        print("  First 200 chars:", text[:200])
    else:
        print("  NO LONG CONTENT FOUND")
except Exception as e:
    print("ERROR:", e)

print()

# Also verify via sitemap that we have the right number of URLs
url = BASE + "/sitemap.xml"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
        sitemap = resp.read().decode('utf-8')
    sitemaps = re.findall(r'<loc>([^<]+)</loc>', sitemap)
    print("Sitemap contains", len(sitemaps), "language sitemaps:")
    for sm in sitemaps:
        print(" ", sm)
except Exception as e:
    print("Sitemap ERROR:", e)

# Check Spanish sitemap size
url = BASE + "/sitemap-es.xml"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
        sm = resp.read().decode('utf-8')
    urls = re.findall(r'<loc>([^<]+)</loc>', sm)
    print("\nSpanish sitemap has", len(urls), "URLs")
except Exception as e:
    print("Spanish sitemap ERROR:", e)
