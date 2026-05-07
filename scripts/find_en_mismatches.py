"""Find calculators where EN name doesn't match the actual calculator logic."""
import json
from pathlib import Path

CALC_DIR = Path(r"C:\Microsaas\obra\src\calculators")

# Build a mapping by analyzing formulas to determine calculator type
# Check EN names that seem wrong by comparing with Spanish source name
mismatches = []
for cf in sorted(CALC_DIR.glob("*.json")):
    if cf.name in ("calculators.json", "monolithic.json", "backup.json"):
        continue
    with open(cf, "r", encoding="utf-8") as f:
        c = json.load(f)
    
    en_name = c.get("i18n", {}).get("en", {}).get("name", "")
    es_name = c.get("i18n", {}).get("es", {}).get("name", "")
    de_name = c.get("i18n", {}).get("de", {}).get("name", "")
    slug = c.get("slug", "")
    cid = c.get("id", "")
    
    # Key terms in slug that should relate to the English name
    slug_keywords = set(slug.lower().replace("-", " ").split())
    en_keywords = set(en_name.lower().split())
    
    # Check overlap between slug and EN name
    common = slug_keywords & en_keywords
    
    # If no common words and both have meaningful content
    if not common and slug_keywords and en_keywords:
        # Check if DE matches Spanish better
        de_keywords = set(de_name.lower().split())
        es_en_common = len(set(es_name.lower().split()) & en_keywords)
        slug_de_common = len(slug_keywords & de_keywords)
        slug_es_common = len(slug_keywords & set(es_name.lower().split()))
        
        # If DE matches slug/ES but EN doesn't match either
        if slug_de_common > 0 or slug_es_common > 0:
            if slug_de_common == 0 and slug_es_common == 0:
                continue  # DE is also wrong
            mismatches.append((cid, slug, en_name, es_name, de_name))

print(f"Found {len(mismatches)} calculators where EN name doesn't match slug/ES/DE\n")
print(f"{'ID':>4} {'slug':40s} {'EN name':35s} {'ES name':35s} {'DE name':35s}")
print("-" * 150)
for cid, slug, en, es, de in sorted(mismatches, key=lambda x: x[0]):
    print(f"{cid:>4} {slug:40s} {en:35s} {es:35s} {de:35s}")
