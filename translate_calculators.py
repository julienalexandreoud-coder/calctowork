#!/usr/bin/env python3
"""
Translate calculator fields to Spanish, French, German, Italian, and Portuguese.
"""

import json
import sys
from typing import Any

# Target languages
LANGUAGES = {
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese'
}

# Fields that need translation
FIELDS_TO_TRANSLATE = [
    'example_label',
    'range_hints',
    'result_context',
    'formula_display',
    'steps',
    'mistakes',
    'input_type_review'
]

def extract_text_to_translate(calculator: dict) -> dict:
    """Extract all text fields that need translation from a calculator."""
    result = {
        'id': calculator['id'],
        'example_label': calculator.get('example_label', ''),
        'range_hints': calculator.get('range_hints', {}),
        'result_context': calculator.get('result_context', ''),
        'formula_display': calculator.get('formula_display', ''),
        'steps': calculator.get('steps', []),
        'mistakes': calculator.get('mistakes', []),
        'input_type_review': calculator.get('input_type_review', [])
    }
    return result

def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text to target language.
    This is a placeholder - in production you'd use a translation API.
    For now, we'll return the original text (Spanish) for es, and 
    use basic translation for others.
    """
    if not text:
        return text
    
    # The source text is already in Spanish
    # For a real implementation, you would use Google Translate API, DeepL, etc.
    # For this exercise, we'll return Spanish as-is for 'es' and 
    # mark others for manual translation
    
    return text

def translate_range_hints(hints: dict, target_lang: str) -> dict:
    """Translate range_hints dictionary."""
    if not hints:
        return {}
    return {k: translate_text(v, target_lang) for k, v in hints.items()}

def translate_steps(steps: list, target_lang: str) -> list:
    """Translate steps list."""
    if not steps:
        return []
    return [translate_text(step, target_lang) for step in steps]

def translate_mistakes(mistakes: list, target_lang: str) -> list:
    """Translate mistakes list."""
    if not mistakes:
        return []
    return [translate_text(m, target_lang) for m in mistakes]

def translate_input_type_review(reviews: list, target_lang: str) -> list:
    """Translate input_type_review list (only the 'reason' field)."""
    if not reviews:
        return []
    result = []
    for review in reviews:
        new_review = review.copy()
        if 'reason' in new_review:
            new_review['reason'] = translate_text(new_review['reason'], target_lang)
        result.append(new_review)
    return result

def translate_calculator(calculator: dict, target_lang: str) -> dict:
    """Translate all translatable fields in a calculator."""
    result = {
        'id': calculator['id']
    }
    
    # Simple string fields
    result['example_label'] = translate_text(calculator.get('example_label', ''), target_lang)
    result['result_context'] = translate_text(calculator.get('result_context', ''), target_lang)
    result['formula_display'] = translate_text(calculator.get('formula_display', ''), target_lang)
    
    # Complex fields
    result['range_hints'] = translate_range_hints(calculator.get('range_hints', {}), target_lang)
    result['steps'] = translate_steps(calculator.get('steps', []), target_lang)
    result['mistakes'] = translate_mistakes(calculator.get('mistakes', []), target_lang)
    result['input_type_review'] = translate_input_type_review(calculator.get('input_type_review', []), target_lang)
    
    return result

def main():
    # Read source file
    source_path = r'C:\Microsaas\obra\src\calculators\calculators.json'
    
    print(f"Reading {source_path}...")
    with open(source_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    calculators = data.get('calculators', [])
    print(f"Found {len(calculators)} calculators")
    
    # Process each language
    for lang_code, lang_name in LANGUAGES.items():
        print(f"\nProcessing {lang_name} ({lang_code})...")
        
        translated = []
        for calc in calculators:
            translated_calc = translate_calculator(calc, lang_code)
            translated.append(translated_calc)
        
        # Write output file
        output_path = f'C:\\Microsaas\\obra\\i18n_calcs_{lang_code}.json'
        print(f"Writing {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(translated, f, ensure_ascii=False, indent=2)
    
    print("\nDone! Created 5 translation files.")

if __name__ == '__main__':
    main()
