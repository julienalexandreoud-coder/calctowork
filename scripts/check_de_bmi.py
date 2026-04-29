import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://calcto.work/de/bmi-rechner/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
    html = resp.read().decode('utf-8')

title = re.search(r'<title>(.*?)</title>', html)
desc = re.search(r'<meta name="description" content="([^"]*)"', html)
has_calc = 'calculator.js' in html
has_content = 'long-content' in html

print("German BMI page:")
print("  Title:", title.group(1) if title else 'MISSING')
print("  Desc:", desc.group(1)[:60] if desc else 'MISSING', "...")
print("  Calc JS:", 'YES' if has_calc else 'NO')
print("  Content:", 'YES' if has_content else 'NO')
