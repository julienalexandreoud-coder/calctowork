import sys
from pathlib import Path
sys.path.insert(0, str(Path(r'C:\Microsaas\obra\scripts')))
from tools_config import TOOL_BY_ID

cid = '087'
info = TOOL_BY_ID[cid]
print('Full info:')
for k, v in info.items():
    print(f'  {k}: {v}')

# Also check TOOLS to understand the structure
from tools_config import TOOLS
print(f'\nTOOLS sample entry: {TOOLS[0] if TOOLS else "empty"}')
