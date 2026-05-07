import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'C:\\Microsaas\\obra\\scripts')
from calc_content import HOWTO

print(f'HOWTO blocks: {len(HOWTO)}')
h = HOWTO['matematicas']
print(f'matematicas keys: {list(h.keys())}')
print(f'matematicas en: {h["en"][:2]}')