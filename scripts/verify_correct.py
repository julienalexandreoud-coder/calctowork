import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "https://calcto.work"

# Check with CORRECT German slug
url = BASE + "/de/stampfbeton-rechner/"
print("Checking:", url)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        html = resp.read().decode('utf-8')
    
    title = re.search(r'<title>(.*?)</title>', html)
    has_content = 'long-content' in html
    has_calc = 'calculator.js' in html
    
    print("Status:", resp.status)
    print("Title:", title.group(1) if title else 'MISSING')
    print("Has content:", 'YES' if has_content else 'NO')
    print("Has calc JS:", 'YES' if has_calc else 'NO')
    
    if has_content:
        m = re.search(r'class="long-content"[^>]*>(.*?)</section>', html, re.DOTALL)
        if m:
            text = re.sub(r'<[^>]+>', ' ', m.group(1))
            words = len(text.split())
            print("Word count:", words)
            print("First 200 chars:", text[:200])
    
    # Check last-modified or build date
    modified = re.search(r'Last updated : ([^<]+)', html)
    if modified:
        print("Build date:", modified.group(1))
    
except Exception as e:
    print("ERROR:", e)
