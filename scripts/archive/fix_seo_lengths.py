"""Fix SEO titles >60 chars and descriptions >160 chars."""
import json, glob, os, re

CALC_DIR = "src/calculators"
MAX_TITLE = 60
MAX_DESC = 160

def smart_truncate(text, max_len):
    """Truncate to max_len at a word boundary."""
    if len(text) <= max_len:
        return text
    # Try to cut at last space within limit
    truncated = text[:max_len].rstrip()
    last_space = truncated.rfind(' ')
    if last_space > max_len * 0.7:  # At least 70% of max before cutting
        return truncated[:last_space]
    return truncated

def fix_seo_title(title, max_len=60):
    """Fix a title that's too long."""
    if len(title) <= max_len:
        return title
    
    # Remove emoji/special chars if present (they add length)
    # Strategy 1: Remove " | CalcToWork" suffix and re-add if space permits
    suffix = " | CalcToWork"
    if title.endswith(suffix):
        base = title[:-len(suffix)]
        # Try removing emoji patterns: some emoji + space
        base = re.sub(r'\s*[^\x00-\x7F]{1,3}\s*', ' ', base).strip()
        # Limit base so that suffix fits
        available = max_len - len(suffix)
        base = smart_truncate(base, available)
        result = base + suffix
        if len(result) <= max_len:
            return result
    
    # Strategy 2: Just truncate with ...
    available = max_len - 3
    truncated = title[:available].rstrip()
    last_space = truncated.rfind(' ')
    if last_space > available * 0.7:
        return truncated[:last_space] + '...'
    return truncated + '...'

def fix_seo_description(desc, max_len=160):
    """Fix a description that's too long."""
    if len(desc) <= max_len:
        return desc
    
    # Try to cut at sentence boundary
    sentences = re.split(r'(?<=[.!?])\s+', desc)
    result = ""
    for s in sentences:
        if len(result) + len(s) + 1 <= max_len:
            result = (result + " " + s).strip()
        else:
            break
    
    if not result:
        result = smart_truncate(desc, max_len)
    
    return result

fixed_titles = 0
fixed_descs = 0

for fp in sorted(glob.glob(os.path.join(CALC_DIR, "*.json"))):
    if "bak" in fp or "monolithic" in fp:
        continue
    with open(fp, "r", encoding="utf-8-sig") as f:
        data = json.load(f)
    
    changed = False
    i18n = data.get("i18n", {})
    
    for lang in i18n:
        lang_data = i18n.get(lang)
        if not isinstance(lang_data, dict):
            continue
        
        title = lang_data.get("seo_title", "")
        if title and len(title) > MAX_TITLE:
            new_title = fix_seo_title(title, MAX_TITLE)
            lang_data["seo_title"] = new_title
            print(f"  TITLE {data['slug']} ({lang}): {len(title)} -> {len(new_title)} chars")
            fixed_titles += 1
            changed = True
        
        desc = lang_data.get("seo_description", "")
        if desc and len(desc) > MAX_DESC:
            new_desc = fix_seo_description(desc, MAX_DESC)
            lang_data["seo_description"] = new_desc
            print(f"  DESC  {data['slug']} ({lang}): {len(desc)} -> {len(new_desc)} chars")
            fixed_descs += 1
            changed = True
    
    if changed:
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

print(f"\nFixed: {fixed_titles} titles, {fixed_descs} descriptions")
