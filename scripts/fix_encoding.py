"""Fix mojibake (UTF-8 bytes read as cp1252/latin-1, re-saved) in JSON files.

Handles double AND triple encoding by running the sliding-window fix repeatedly
until stable (up to 4 passes).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _encode_char(c: str) -> bytes | None:
    for enc in ("cp1252", "latin-1"):
        try:
            return c.encode(enc)
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return None


def _fix_pass(s: str) -> tuple[str, bool]:
    """One sliding-window pass: pairs of chars encoded as cp1252 → decoded as UTF-8."""
    result: list[str] = []
    i = 0
    changed = False
    while i < len(s):
        if i + 1 < len(s):
            ba = _encode_char(s[i])
            bb = _encode_char(s[i + 1])
            if ba and bb:
                try:
                    fixed = (ba + bb).decode("utf-8")
                    if fixed != s[i : i + 2]:
                        result.append(fixed)
                        i += 2
                        changed = True
                        continue
                except (UnicodeDecodeError, ValueError):
                    pass
        result.append(s[i])
        i += 1
    return "".join(result), changed


def fix_mojibake(s: str) -> str:
    for _ in range(4):
        s, changed = _fix_pass(s)
        if not changed:
            break
    return s


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
    orig_str = json.dumps(data, ensure_ascii=False)
    new_str = json.dumps(fixed_data, ensure_ascii=False)
    if orig_str != new_str:
        path.write_text(json.dumps(fixed_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return sum(1 for a, b in zip(orig_str, new_str) if a != b) + abs(len(new_str) - len(orig_str))
    return 0


files_to_fix = [
    ROOT / "src" / "calculators" / "calculators.json",
    ROOT / "src" / "i18n" / "es.json",
    ROOT / "src" / "i18n" / "it.json",
    ROOT / "src" / "i18n" / "fr.json",
    ROOT / "src" / "i18n" / "de.json",
    ROOT / "src" / "i18n" / "pt.json",
    ROOT / "src" / "i18n" / "en.json",
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
