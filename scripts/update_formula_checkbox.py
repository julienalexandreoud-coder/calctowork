with open('CALCULATOR_AUDIT.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the per-calculator summary checkbox line for formula
old_line = '- [ ] Formula tested and accurate'
new_line = '- [ ] Formula + answer quality (precision, units, formatting, rounding, buying units)'

count = content.count(old_line)
content = content.replace(old_line, new_line)

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Updated {count} calculators')
