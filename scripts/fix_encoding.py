"""Fix mojibake (UTF-8 bytes interpreted as Latin-1) in JSON and i18n files."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def fix_mojibake(text: str) -> str:
    """Reverse double-encoding: take UTF-8 text read as Latin-1, re-encode correctly."""
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Fall back to character-by-character fix for mixed content
        result = []
        i = 0
        while i < len(text):
            # Try to fix a 2-char mojibake window
            if i + 1 < len(text):
                chunk = text[i:i+2]
                try:
                    fixed = chunk.encode("latin-1").decode("utf-8")
                    result.append(fixed)
                    i += 2
                    continue
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass
            result.append(text[i])
            i += 1
        return "".join(result)


def fix_value(v):
    if isinstance(v, str):
        return fix_mojibake(v)
    if isinstance(v, list):
        return [fix_value(x) for x in v]
    if isinstance(v, dict):
        return {fix_value(k): fix_value(val) for k, val in v.items()}
    return v


def fix_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    data = json.loads(original)
    fixed_data = fix_value(data)
    fixed_text = json.dumps(fixed_data, ensure_ascii=False, indent=2)
    if fixed_text != json.dumps(json.loads(original), ensure_ascii=False, indent=2):
        path.write_text(fixed_text + "\n", encoding="utf-8")
        # Count changed characters
        orig_str = json.dumps(data, ensure_ascii=False)
        new_str = json.dumps(fixed_data, ensure_ascii=False)
        changes = sum(1 for a, b in zip(orig_str, new_str) if a != b)
        return changes
    return 0


files_to_fix = [
    ROOT / "src" / "calculators" / "calculators.json",
    ROOT / "src" / "i18n" / "fr.json",
    ROOT / "src" / "i18n" / "de.json",
    ROOT / "src" / "i18n" / "it.json",
    ROOT / "src" / "i18n" / "pt.json",
    ROOT / "src" / "i18n" / "en.json",
    ROOT / "src" / "i18n" / "es.json",
]

total = 0
for f in files_to_fix:
    if f.exists():
        changes = fix_file(f)
        print(f"  {f.name}: {changes} chars fixed")
        total += changes
    else:
        print(f"  {f.name}: NOT FOUND")

print(f"\nTotal characters fixed: {total}")
