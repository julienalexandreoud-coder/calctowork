"""
Fix common missing umlauts in German content HTML files.
Patterns: fur->für, schatzen->schätzen, uber->über, etc.
"""
import os, re, glob

CONTENT_DIR = r"C:\Microsaas\obra\src\content\de"

# Common German words that frequently miss umlauts in these files
UMLAUT_FIXES = [
    # (pattern, replacement) - using word boundary for safety
    (r'\bfur\b', 'für'),
    (r'\bFur\b', 'Für'),
    (r'\bschatzen\b', 'schätzen'),
    (r'\bSchatzen\b', 'Schätzen'),
    (r'\buber\b', 'über'),
    (r'\bUber\b', 'Über'),
    (r'\bAbhangen\b', 'Abhängen'),
    (r'\babhangen\b', 'abhängen'),
    (r'\bGroBe\b', 'Größe'),
    (r'\bgroBe\b', 'größe'),
    (r'\bHohe\b', 'Höhe'),
    (r'\bhohe\b', 'höhe'),
    (r'\bStarke\b', 'Stärke'),
    (r'\bstarke\b', 'stärke'),
    (r'\bLange\b', 'Länge'),
    (r'\blange\b', 'länge'),
    (r'\bTur\b', 'Tür'),
    (r'\btur\b', 'tür'),
    (r'\bFusse\b', 'Füße'),
    (r'\bfusse\b', 'füße'),
    (r'\bKorper\b', 'Körper'),
    (r'\bkorper\b', 'körper'),
    (r'\bFlache\b', 'Fläche'),
    (r'\bflache\b', 'fläche'),
    (r'\bKuche\b', 'Küche'),
    (r'\bkuche\b', 'küche'),
    (r'\bHolzer\b', 'Hölzer'),
    (r'\bholzer\b', 'hölzer'),
    (r'\bMobel\b', 'Möbel'),
    (r'\bmobel\b', 'möbel'),
    (r'\bSchlosser\b', 'Schlösser'),
    (r'\bschlosser\b', 'schlösser'),
    (r'\bOl\b', 'Öl'),
    (r'\bol\b', 'öl'),
    (r'\bOffnung\b', 'Öffnung'),
    (r'\boffnung\b', 'öffnung'),
    (r'\bSchatzen\b', 'Schätzen'),
    (r'\bschatzen\b', 'schätzen'),
    (r'\bSchatzung\b', 'Schätzung'),
    (r'\bschatzung\b', 'schätzung'),
    (r'\bMussen\b', 'Müssen'),
    (r'\bmussen\b', 'müssen'),
    (r'\bKonnen\b', 'Können'),
    (r'\bkonnen\b', 'können'),
    (r'\bWahrend\b', 'Während'),
    (r'\bwahrend\b', 'während'),
    (r'\bMochten\b', 'Möchten'),
    (r'\bmochten\b', 'möchten'),
    # "e" replacements where umlaut characters should be
    # e.g. "schatzen" (schätzen), "uber" (über)
]

fixed_count = 0
total = 0

files = sorted(glob.glob(os.path.join(CONTENT_DIR, "*.html")))

for filepath in files:
    total += 1
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = False
    
    for pattern, replacement in UMLAUT_FIXES:
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1

print(f"Total: {total} | Fixed missing umlauts: {fixed_count}")
