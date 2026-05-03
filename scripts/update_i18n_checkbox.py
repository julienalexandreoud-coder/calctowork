with open('CALCULATOR_AUDIT.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the per-calculator summary checkbox line
old_line = '- [ ] i18n complete (all 6 languages)'
new_line = '- [ ] i18n deep check (labels, units, selects, numbers, currency, pluralization)'

count = content.count(old_line)
content = content.replace(old_line, new_line)

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Updated {count} calculators')
