import re
from pathlib import Path
from bs4 import BeautifulSoup

d = Path(r'C:\Microsaas\obra\src\content')

# Fix 1: Remove duplicate Related Calculators sections
print('=== Fixing duplicate sections ===')
dup_count = 0
for lang_dir in d.iterdir():
    if not lang_dir.is_dir():
        continue
    for f in lang_dir.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        
        # Find duplicate Related Calculators sections
        sections = list(re.finditer(r'<h2>Related Calculators</h2>', content))
        if len(sections) > 1:
            # Keep the first section, remove subsequent duplicates
            first_end = sections[0].start()
            for s in sections[1:]:
                # Find where this section starts (the opening tag before h2)
                section_start = content.rfind('<div', s.start() - 200, s.start())
                if section_start < 0:
                    section_start = s.start()
                # Find where the section ends (look for </div> or next <h2> or </section>)
                section_end = content.find('</div>', s.end())
                if section_end < 0:
                    section_end = content.find('</section>', s.end())
                if section_end < 0:
                    section_end = len(content)
                else:
                    section_end += 6
                
                content = content[:section_start] + content[section_end:]
                dup_count += 1
                print(f'  Removed duplicate in {lang_dir.name}/{f.name}')
        
        f.write_text(content, encoding='utf-8')

print(f'\nDuplicate sections fixed: {dup_count}')

# Fix 2: Find and fix HTML bugs (missing quotes in tags)
print('\n=== Fixing HTML bugs ===')
bug_count = 0
for lang_dir in d.iterdir():
    if not lang_dir.is_dir():
        continue
    for f in lang_dir.glob('*.html'):
        content = f.read_text(encoding='utf-8')
        original = content
        
        # Fix: missing closing quote in attributes like class="faq-item
        content = re.sub(r'class="faq-item\s+', 'class="faq-item" ', content)
        content = re.sub(r'class="faq-item<', 'class="faq-item"><', content)
        
        # Fix: <div class="faq-item> without closing quote
        content = re.sub(r'class="faq-item>', 'class="faq-item">', content)
        
        # Fix: <öl> instead of <ol> (German files had this)
        content = content.replace('<öl>', '<ol>')
        content = content.replace('</öl>', '</ol>')
        
        # Fix: <div class="faq-ap> instead of <div class="faq-a"><p>
        content = content.replace('class="faq-ap"', 'class="faq-a"')
        content = re.sub(r'class="faq-ap>', 'class="faq-a"><p>', content)
        
        # Fix: unclosed <p> tags inside FAQ answers
        content = re.sub(r'class="faq-a"><p>', 'class="faq-a">', content)
        
        if content != original:
            f.write_text(content, encoding='utf-8')
            bug_count += 1
            if bug_count <= 20:
                print(f'  Fixed HTML bugs in {lang_dir.name}/{f.name}')

print(f'\nHTML bugs fixed: {bug_count} files')
