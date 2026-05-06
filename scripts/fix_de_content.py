"""
Fix German content HTML files:
1. Replace English phrase with German
2. Fix French accents (Métrische -> Metrische)
3. Fix missing umlauts (fur -> für)
"""
import os, re, glob

CONTENT_DIR = r"C:\Microsaas\obra\src\content\de"

# English phrase to replace
ENGLISH_PHRASE = "ensure all values use a single consistent unit system"
GERMAN_PHRASE = "stellen Sie sicher, dass alle Werte ein einheitliches Maßsystem verwenden"

fixed_count = 0
total = 0

files = sorted(glob.glob(os.path.join(CONTENT_DIR, "*.html")))

for filepath in files:
    total += 1
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # Replace English phrase (case-insensitive)
    if ENGLISH_PHRASE.lower() in content.lower():
        # Use a case-insensitive replacement
        content = re.sub(re.escape(ENGLISH_PHRASE), GERMAN_PHRASE, content, flags=re.IGNORECASE)
        modified = True
    
    # Fix French accent in "Métrische" -> "Metrische"
    content = content.replace('Métrische', 'Metrische')
    content = content.replace('métrische', 'metrische')
    if 'Métrische' in original or 'métrische' in original:
        modified = True
    
    # Fix "fur " -> "für " (missing umlaut in "für")
    # Only fix when it's clearly the German word "für", not "Fur" as in fur
    # Pattern: "fur " preceded by a space or start of sentence
    content = re.sub(r'(?<![a-zA-ZäöüÄÖÜß])fur ', 'für ', content)
    content = re.sub(r'(?<![a-zA-ZäöüÄÖÜß])Fur ', 'Für ', content)
    if content != original and 'fur ' in original.lower():
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1

print(f"Total: {total} | Fixed: {fixed_count}")
