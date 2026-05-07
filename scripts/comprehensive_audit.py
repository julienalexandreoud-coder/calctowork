"""
Comprehensive content quality audit across all 6 languages.
Checks every file for: English fragments, BRK artifacts, wrong content, broken HTML, missing translations.
"""
import re, sys, json
from pathlib import Path
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(r'C:\Microsaas\obra\scripts')))
from tools_config import TOOL_BY_ID

d = Path(r'C:\Microsaas\obra\src\content')
i18n_en = json.load(open(d.parent / 'i18n' / 'en.json', encoding='utf-8'))

LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt']

# English patterns that should NOT appear in non-EN files (unless code/technical)
ENGLISH_HEADERS = [
    r'<h2>Real-W(orl)?d Examples</h2>',
    r'<h2>Common Mistakes</h2>',
    r'<h2>Pro Tips?</h2>',
    r'<h2>FAQs?</h2>',
    r'<h2>Related Calculators</h2>',
    r'<h2>Step-by-Step Guide</h2>',
    r'<h2>Formulas? Explained</h2>',
    r'<h2>What (Is|Are)',
    r'<h2>How (It|to)',
    r'<h2>Frequently Asked Questions</h2>',
    r'<h2>Related Calculator</h2>',
]

ENGLISH_PATTERNS = [
    r'\|\|\|BRK\|\|\|',
    r'internal-links-added',
    r'enlaces-internos-agregados',
    r'liens? internes? ajoutés?',
    r'links internos adicionados',
    r'interni-aggiunti',
]

# Language-specific English text that should have been translated
ENGLISH_TEXTS = {
    'es': [r'\band\b', r'\buseful\b', r'See also', r'Related Calculators'],
    'fr': [r'\band\b', r'\buseful\b', r'See also', r'Related Calculators'],
    'de': [r'\band\b', r'\buseful\b', r'See also', r'Related Calculators'],
    'it': [r'\band\b', r'\buseful\b', r'See also', r'Related Calculators'],
    'pt': [r'\band\b', r'\buseful\b', r'See also', r'Related Calculators'],
}

results = {lang: [] for lang in LANGS}

# Helper: get EN topic for comparison
def get_en_topic(filename):
    f = d / 'en' / filename
    if not f.exists():
        return None
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    h1 = soup.find('h1')
    h2 = soup.find('h2')
    txt = soup.get_text(strip=True)[:200]
    return (h1.get_text(strip=True) if h1 else '',
            h2.get_text(strip=True)[:80] if h2 else '',
            txt[:100])

print('=' * 80)
print('COMPREHENSIVE CONTENT QUALITY AUDIT')
print('=' * 80)

for lang in LANGS:
    ld = d / lang
    if not ld.exists():
        continue
    
    lang_issues = []
    
    for f in sorted(ld.glob('*.html')):
        content = f.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        issues = []
        
        # Check 1: BRK artifacts
        if 'BRK' in content or '|||' in content:
            issues.append('BRK_ARTIFACT')
        
        # Check 2: internal-links-added artifacts
        for pat in ENGLISH_PATTERNS:
            if re.search(pat, content, re.IGNORECASE):
                issues.append(f'EN_ARTIFACT:{pat}')
        
        # Check 3: English headers in non-EN files
        if lang != 'en':
            for pat in ENGLISH_HEADERS:
                if re.search(pat, content):
                    # Make sure it's not inside a code block
                    issues.append(f'EN_HEADER:{pat}')
            
            # Check 4: Verbatim English text
            for pat in ENGLISH_TEXTS.get(lang, []):
                matches = re.findall(pat, content)
                if matches:
                    # Filter out code/math content
                    text_only = soup.get_text()
                    if re.search(pat, text_only):
                        issues.append(f'EN_TEXT:"{pat}"')
        
        # Check 5: Content topic mismatch
        if lang != 'en':
            en_topic = get_en_topic(f.name)
            if en_topic:
                h1 = soup.find('h1')
                h2 = soup.find('h2')
                h1_text = h1.get_text(strip=True) if h1 else ''
                h2_text = h2.get_text(strip=True)[:80] if h2 else ''
                
                # Check if first h2 seems related to EN topic
                en_h2 = en_topic[1].lower() if en_topic[1] else ''
                this_h2 = h2_text.lower()
                
                # If EN h2 has key terms and target h2 doesn't, flag it
                en_words = set(re.findall(r'\w+', en_h2))
                this_words = set(re.findall(r'\w+', this_h2))
                common = en_words & this_words
                if len(en_words) > 3 and len(common) < 2 and len(this_words) > 2:
                    issues.append(f'TOPIC_MISMATCH:ENh2="{en_h2[:50]}" vs LANGh2="{h2_text[:50]}"')
        
        # Check 6: HTML structure issues
        if '<öl>' in content or '</öl>' in content:
            issues.append('OEL_TAG')
        
        # Check 7: Empty or near-empty content
        text_len = len(soup.get_text(strip=True))
        en_file = d / 'en' / f.name
        if en_file.exists():
            en_len = len(BeautifulSoup(en_file.read_text(encoding='utf-8'), 'html.parser').get_text(strip=True))
            if en_len > 1000 and text_len / en_len < 0.3:
                issues.append(f'TOO_SHORT:{text_len}/{en_len}({text_len/en_len*100:.0f}%)')
            elif en_len > 1000 and text_len / en_len > 2.0:
                issues.append(f'TOO_LONG:{text_len}/{en_len}({text_len/en_len*100:.0f}%)')
        
        if issues:
            lang_issues.append((f.name, issues, text_len))
    
    # Print summary for this language
    print(f'\n--- {lang.upper()} ({len(lang_issues)} files with issues) ---')
    
    # Group by issue type
    issue_types = {}
    for fn, iss, _ in lang_issues:
        for i in iss:
            itype = i.split(':')[0]
            issue_types[itype] = issue_types.get(itype, 0) + 1
    
    for itype, count in sorted(issue_types.items(), key=lambda x: -x[1]):
        print(f'  {itype}: {count}')
    
    # Show sample files for each issue type
    for itype in sorted(issue_types.keys(), key=lambda x: -issue_types[x]):
        samples = [fn for fn, iss, _ in lang_issues if any(i.startswith(itype) for i in iss)]
        print(f'  {itype} samples: {samples[:5]}')

print('\n' + '=' * 80)
print('TOPIC MISMATCH DETAILS')
print('=' * 80)
for lang in ['es', 'fr', 'de', 'it', 'pt']:
    ld = d / lang
    mismatches = []
    for f in sorted(ld.glob('*.html')):
        content = f.read_text(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        en_topic = get_en_topic(f.name)
        if not en_topic:
            continue
        h2 = soup.find('h2')
        h2_text = h2.get_text(strip=True)[:80] if h2 else ''
        en_h2 = en_topic[1].lower()
        this_h2 = h2_text.lower()
        en_words = set(re.findall(r'\w+', en_h2))
        this_words = set(re.findall(r'\w+', this_h2))
        common = en_words & this_words
        if len(en_words) > 3 and len(common) < 2 and len(this_words) > 2:
            mismatches.append((f.name, en_topic[1][:60], h2_text[:60]))
    
    if mismatches:
        print(f'\n{lang} ({len(mismatches)} mismatches):')
        for fn, enh2, langh2 in mismatches[:10]:
            print(f'  {fn}: EN="{enh2}" vs {lang}="{langh2}"')
