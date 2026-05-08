from pathlib import Path
d = Path(r'C:\Microsaas\obra\src\calculators')
for e in list(d.iterdir())[:5]:
    print(f'name={e.name}, is_file={e.is_file()}, suffix="{e.suffix}", ext="{os.path.splitext(e.name)[1]}"')

import os
# Try to read one directly
with open(r'C:\Microsaas\obra\src\calculators\001', 'r', encoding='utf-8') as f:
    print(f'First 100 chars: {f.read(100)}')
