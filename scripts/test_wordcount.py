import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from calc_content import CALC_FACTS, LONG_CONTENT, generate_long_content

# Check all 6 languages for a good LONG_CONTENT entry
for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    article = generate_long_content('200', lang, calc_name='Percentage Calculator')
    if article:
        words = len(article.split())
        print(f"200/{lang}: {words} words, {len(article)} chars")
    else:
        print(f"200/{lang}: EMPTY")

# Check CALC_FACTS-based entry in all languages
for lang in ['en', 'es', 'fr', 'pt', 'de', 'it']:
    article = generate_long_content('001', lang, calc_name='Mass Concrete Calculator')
    if article:
        words = len(article.split())
        print(f"001/{lang}: {words} words, {len(article)} chars")
    else:
        print(f"001/{lang}: EMPTY")