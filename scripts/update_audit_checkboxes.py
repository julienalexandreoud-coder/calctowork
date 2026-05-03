import re

with open('CALCULATOR_AUDIT.md', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = '''- [ ] Formula tested and accurate
- [ ] UI consistent (buttons, copy, share, fav)
- [ ] SEO title + description good
- [ ] Content quality OK
- [ ] i18n complete (all 6 languages)'''

new_block = '''- [ ] Formula tested and accurate
- [ ] UI consistent (buttons, copy, share, fav)
- [ ] SEO title + description good
- [ ] Content quality OK
- [ ] i18n complete (all 6 languages)
- [ ] Unit conversion + share prefill work
- [ ] Analytics events fire (calc, fav, share)
- [ ] Mobile + dark mode OK
- [ ] Ads + affiliates load correctly'''

count = content.count(old_block)
content = content.replace(old_block, new_block)

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Updated {count} calculators')
