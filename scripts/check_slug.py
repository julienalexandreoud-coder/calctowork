import sys
sys.path.insert(0, 'scripts')
from tools_config import TOOL_BY_ID

# Get German slug for calculator 001
cfg = TOOL_BY_ID.get('001', {})
print("ID 001 slugs:")
for lang in ['es', 'en', 'fr', 'de', 'it', 'pt']:
    print(f"  {lang}: {cfg.get('slugs', {}).get(lang, 'MISSING')}")
