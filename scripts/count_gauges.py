import re

with open('scripts/generate_calctowork.py', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'GAUGE_CONFIGS = \{([^}]+)\}', text, re.DOTALL)
if match:
    entries = re.findall(r'"(\d+)"', match.group(1))
    print(f'Existing GAUGE_CONFIGS: {len(entries)}')
    print(entries)
