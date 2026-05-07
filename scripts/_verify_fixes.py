import re

# 1. Check if duplicate was removed
content = open(r'C:\Microsaas\obra\src\content\en\951.html', encoding='utf-8').read()
count = len(re.findall(r'Related Calculators</h2>', content))
print(f'951.html Related Calculators count: {count} (should be 1)')

# 2. Check if öl was fixed in DE files
content = open(r'C:\Microsaas\obra\src\content\de\001.html', encoding='utf-8').read()
has_ol = '<ol>' in content
has_oel = '<\xc3\xb6l>' in content
print(f'DE 001.html: <ol>={has_ol}, <\\xc3\\xb6l>={has_oel} (should be True, False)')

# 3. Check for class quote fixes
content = open(r'C:\Microsaas\obra\src\content\en\097.html', encoding='utf-8').read()
unquoted = 'class="faq-item>' in content
quoted = 'class="faq-item">' in content
print(f'EN 097.html: missing quote={unquoted}, proper={quoted}')
