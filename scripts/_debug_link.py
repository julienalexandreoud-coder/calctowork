import re
content = open(r'C:\Microsaas\obra\src\content\en\097.html', encoding='utf-8').read()
print('Contains ohms-law:', '/en/ohms-law/' in content)
matches = re.findall(r'<a\s+href="([^"]*)"\s*>([^<]*)</a>', content)
for h, t in matches:
    if 'ohms' in h:
        print(f'HREF: [{h}] TEXT: [{t}]')
