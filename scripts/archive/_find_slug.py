from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(r'C:\Microsaas\obra\scripts')))
from tools_config import TOOL_BY_ID
for cid, info in TOOL_BY_ID.items():
    slugs = info.get('slugs', {})
    en_slug = slugs.get('en', '')
    if 'area' in en_slug:
        print(f'{cid}: area-converter -> {slugs}')
