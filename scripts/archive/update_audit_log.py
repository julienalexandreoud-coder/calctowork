import re

with open('CALCULATOR_AUDIT.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the audit log section
old_log = '''## Audit Log

| Date | Calculator ID | Auditor | Notes |
|------|---------------|---------|-------|
| | | | |'''

new_log = '''## Audit Log

| # | Date | Calc ID | Slug | Status | Issues Found | Fixed | Auditor | Notes |
|---|------|---------|------|--------|--------------|-------|---------|-------|
| 1 | | | | | | | | |

**Status codes:** `PASS` = all checks green, `FAIL` = critical issue, `PARTIAL` = minor issues only

**Issue codes:** `F` = Formula, `U` = UI, `S` = SEO, `C` = Content, `I` = i18n, `A` = Analytics, `M` = Mobile, `R` = Revenue/Ads

---

## Quick Reference: Calculator URLs

**Base URL pattern:** `https://calcto.work/{lang}/{slug}/`

**Example:** Calculator 001 (hormigon-masa)
- EN: https://calcto.work/en/mass-concrete-calculator/
- ES: https://calcto.work/es/calculadora-hormigon-masa/
- FR: https://calcto.work/fr/calculateur-beton-masse/
- PT: https://calcto.work/pt/calculadora-concreto-massa/
- DE: https://calcto.work/de/stampfbeton-rechner/
- IT: https://calcto.work/it/calcolatore-calcestruzzo-massa/

---'''

content = content.replace(old_log, new_log)

with open('CALCULATOR_AUDIT.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated audit log format')
