import sys
sys.path.insert(0, 'scripts')
from tools_config import TOOL_BY_ID

# Find BMI calculator
for cid, cfg in TOOL_BY_ID.items():
    en = cfg['slugs'].get('en', '')
    if 'bmi' in en:
        print("ID %s: EN=%s, DE=%s" % (cid, en, cfg['slugs'].get('de')))
        break
