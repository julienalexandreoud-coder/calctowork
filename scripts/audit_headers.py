"""Analyze what English headers remain in non-EN files."""
import re
from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')

HEADER_PATTERNS = [
    'Real-World Examples',
    'Common Mistakes',
    'Pro Tips?',
    'FAQs?',
    'Related Calculators?',
    'Step-by-Step Guide',
    'Formulas? Explained',
    'Frequently Asked Questions',
    'What (Is|Are)',
    'How (It Works|to)',
    'Common Mistakes to Avoid',
    'Step-by-Step Guide to Using',
    'Common uses of',
    'Common mistakes with',
    'Real-World Example',
    'Pro Tip',
]

for lang in ['es', 'fr', 'de', 'it', 'pt']:
    ld = d / lang
    header_counts = {}
    header_files = {}
    
    for f in ld.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        for pat in HEADER_PATTERNS:
            matches = re.findall(r'<h[1-6]>' + pat + r'</h[1-6]>', content)
            if matches:
                match_text = matches[0]
                header_counts[match_text] = header_counts.get(match_text, 0) + 1
                if match_text not in header_files:
                    header_files[match_text] = []
                if len(header_files[match_text]) < 5:
                    header_files[match_text].append(f.name)
    
    print(f'\n{lang.upper()} - English Headers Found:')
    for hdr, count in sorted(header_counts.items(), key=lambda x: -x[1]):
        files_str = ', '.join(header_files[hdr][:3])
        print(f'  [{count}] {hdr} (e.g. {files_str})')
