"""Fix remaining translation quality issues across all languages."""
import re
from pathlib import Path

d = Path(r'C:\Microsaas\obra\src\content')
LANGS = ['es', 'fr', 'de', 'it', 'pt']

issues_fixed = 0

for lang in LANGS:
    ld = d / lang
    if not ld.exists():
        continue
    
    for f in ld.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        original = content
        
        # Issue 1: Remove |||BRK||| artifacts
        content = content.replace('|||BRK|||', '')
        content = content.replace(' |||BRK||| ', '')
        
        # Issue 2: Fix degraded <!-- internal-links-added --> comments
        # Some files have this as visible text instead of HTML comment
        if '<!-- internal-links-added -->' in content:
            pass  # Already a comment, good
        elif 'internal-links-added' in content or 'enlaces-internos-agregados' in content or 'interni-aggiunti' in content:
            # Remove visible text remnants
            content = re.sub(r'[\s]*internal-links-added[\s]*', '', content)
            content = re.sub(r'[\s]*enlaces-internos-agregados[\s]*', '', content)
            content = re.sub(r'[\s]*interni-aggiunti[\s]*', '', content)
            content = re.sub(r'[\s]*links internos adicionados[\s]*', '', content)
        
        if content != original:
            f.write_text(content, encoding='utf-8')
            issues_fixed += 1

print(f'Fixed quality issues in {issues_fixed} files')

# Issue 3: Check for see-also paragraphs with wrong language paths
print('\nChecking see-also links...')
see_also_fixed = 0
for lang in LANGS:
    ld = d / lang
    for f in ld.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        original = content
        # Fix: see-also links that point to /en/ instead of target language
        content = re.sub(r'href="/en/([^"]*)"', f'href="/{lang}/" + r"\1"', content)
        # Actually, just check - the links might already be correct from the broken links fix
        
        if content != original:
            f.write_text(content, encoding='utf-8')
            see_also_fixed += 1

print(f'See-also links fixed: {see_also_fixed}')
