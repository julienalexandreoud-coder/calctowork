from calc_content import LONG_CONTENT

print(f"Total LONG_CONTENT entries: {len(LONG_CONTENT)}")
print("\nIDs with LONG_CONTENT:")
for cid, entry in sorted(LONG_CONTENT.items()):
    langs = [k for k in entry.keys() if k in ('en','es','fr','pt','de','it')]
    en_len = len(entry.get('en', '')) if 'en' in entry else 0
    print(f"  {cid}: languages={langs}, en_words={len(entry.get('en', '').split())}")