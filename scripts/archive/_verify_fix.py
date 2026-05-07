import re
content = open(r'C:\Microsaas\obra\src\content\en\097.html', encoding='utf-8').read()
matches = re.findall(r'<a\s+href="([^"]*)"', content)
ohms = [h for h in matches if 'ohms' in h.lower()]
print(f'Remaining ohms-law links: {len(ohms)}')
# Show a few fixed links
for h in matches:
    if 'liability-insurance' in h or 'signage' in h or 'renovation' in h:
        print(f'Fixed link: {h}')
