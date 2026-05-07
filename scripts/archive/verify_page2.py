f = open(r'C:\Microsaas\obra\public\en\mass-concrete-calculator\index.html', 'r', encoding='utf-8')
html = f.read()
f.close()
# Find FAQ section
idx = html.find('faq-section')
if idx > 0:
    print('FAQ section found at', idx)
    print(html[idx:idx+500])
else:
    print('No FAQ section found')

# Find HowTo section
idx2 = html.find('howto-section')
if idx2 > 0:
    print('\nHowTo section found at', idx2)
    print(html[idx2:idx2+500])