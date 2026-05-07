f = open(r'C:\Microsaas\obra\public\en\mortgage-calculator\index.html', 'r', encoding='utf-8')
html = f.read()
f.close()
# Check for long-content section
idx = html.find('long-content')
if idx > 0:
    print('Long content found!')
    # Count words in article
    import re
    article_idx = html.find('<section class="long-content">')
    article_end = html.find('</section>', article_idx)
    article = html[article_idx:article_end]
    words = len(re.findall(r'\b\w+\b', article))
    print(f'Article word count: {words}')
else:
    print('No long-content section found')

# Check OG image
print('OG image:', '/og/finanzas.png' in html)
print('twitter:card:', 'summary_large_image' in html)