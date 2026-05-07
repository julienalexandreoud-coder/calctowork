#!/usr/bin/env python3
"""
Aggressive mojibake fix for i18n JSON files.
Handles double, triple, and quadruple UTF-8/cp1252 encoding layers.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent / "src" / "i18n"

def fix_text(text: str) -> str:
    """Iteratively fix mojibake until text stabilizes."""
    if not isinstance(text, str):
        return text
    
    for _ in range(5):
        prev = text
        try:
            # Try cp1252 decode first
            text = text.encode('cp1252').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            try:
                text = text.encode('latin-1').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                break
        if text == prev:
            break
    return text

def process_value(value):
    if isinstance(value, str):
        return fix_text(value)
    if isinstance(value, dict):
        return {k: process_value(v) for k, v in value.items()}
    if isinstance(value, list):
        return [process_value(v) for v in value]
    return value

def main():
    for lang_file in sorted(ROOT.glob("*.json")):
        print(f"Processing {lang_file.name}...")
        with open(lang_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        data = process_value(data)
        with open(lang_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"  Saved {lang_file.name}")
    print("Done.")

if __name__ == "__main__":
    main()
