import re
from pathlib import Path
p = Path(r'C:\Microsaas\obra\public')

print('=== CRITICAL FIX VERIFICATION ===')

# 1: German homepage title
d = (p/'de'/'index.html').read_text(encoding='utf-8')
m = re.search(r'<title>([^<]+)</title>', d)
title = m.group(1) if m else 'NOT FOUND'
has_french = 'Calculateurs' in title or 'Gratuits' in title
print(f'\nDE title: {title}')
print(f'  French text: {"BUG!" if has_french else "OK"}')

# 2: Mass-concrete article
m = (p/'en'/'mass-concrete-calculator'/'index.html').read_text(encoding='utf-8')
has_pipe = 'Concrete Pipe' in m
has_concrete = 'slab' in m.lower() and 'concrete' in m.lower()
print(f'\nMass concrete: pipe={"BUG!" if has_pipe else "OK"}, slab={"OK" if has_concrete else "MISSING"}')

# 3: SEO title duplication
title_m = re.search(r'<title>([^<]+)</title>', m)
if title_m:
    t = title_m.group(1)
    bc = t.count('CalcToWork')
    print(f'SEO title: "{t}"')
    print(f'  Brand count: {bc} (should be 1) {"BUG!" if bc > 1 else "OK"}')

# 4: Area converter
a = (p/'en'/'area-converter'/'index.html').read_text(encoding='utf-8')
hm = 'Molecular' in a
ha = 'Area Converter' in a or 'area converter' in a
print(f'\nArea converter: molecular={"BUG!" if hm else "OK"}, area converter={"OK" if ha else "MISSING"}')

# 5: Compound interest mojibake
ci = (p/'en'/'compound-interest-calculator'/'index.html').read_text(encoding='utf-8')
hc = '\u00e2\u201a\u00ac' in ci or 'â‚¬' in ci
print(f'\nCompound interest mojibake: {"BUG!" if hc else "OK"}')

# 6: Sex dropdown
bi = (p/'en'/'bmi-calculator'/'index.html').read_text(encoding='utf-8')
hmj = 'Mujer' in bi or 'mujer' in bi
hml = 'Male' in bi or 'male' in bi
print(f'\nSex dropdown: mujer={"BUG!" if hmj else "OK"}, male={"OK" if hml else "MISSING"}')

print('\n=== DONE ===')
