import re

with open('CALCULATOR_AUDIT.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Add progress tracker after the Rules section
old_rules = '''**Rules:**
- Check one calculator at a time.
- Do NOT skip any item.
- Mark complete only after testing the live page.
- Record findings in the Audit Log at the bottom immediately after each check.'''

new_rules = '''**Rules:**
- Check one calculator at a time.
- Do NOT skip any item.
- Mark complete only after testing the live page.
- Record findings in the Audit Log at the bottom immediately after each check.

## Progress Tracker

| Status | Count | Percentage |
|--------|-------|------------|
| Total | 441 | 100% |
| Audited | 0 | 0% |
| Pass | 0 | 0% |
| Fail | 0 | 0% |
| Partial | 0 | 0% |
| Remaining | 441 | 100% |

*Update this table after each audit session.*'''

content = content.replace(old_rules, new_rules)

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Added progress tracker')
