"""Check content for uniqueness and accuracy - not just template filler"""
import json
import os

# Load some content files to audit
calcs_to_check = [
    ('400', 'BMI Calculator'),  # We expanded
    ('413', 'Body Fat Calculator'),  # We expanded
    ('926', 'BMR Calculator'),  # We expanded
    ('411', 'Max Heart Rate'),  # Thin content - check template
    ('701', 'Density Calculator'),  # Thin - check template
    ('303', 'Simple Interest'),  # Thin - check template
    ('202', 'Rectangle Area'),  # Thin - check template
    ('801', 'Weight Converter'),  # Thin - check template
]

print("=" * 70)
print("CONTENT UNIQUENESS & ACCURACY AUDIT")
print("=" * 70)

for cid, name in calcs_to_check:
    f = f'src/content/en/{cid}.html'
    if not os.path.exists(f):
        print(f"\n{cid}: {name} - FILE MISSING")
        continue
    
    content = open(f, encoding='utf-8').read()
    words = len(content.split())
    
    # Check for template indicators
    template_phrases = [
        'the formula behind this calculation is',
        'understanding how the result is derived',
        'this calculator is particularly useful',
        'ensure all values use a single consistent unit',
        'results are mathematically exact',
        'the calculator applies the standard formula',
        'final accuracy depends on the precision',
        'this tool gives you instant, accurate results',
        'learn how to use this calculator',
    ]
    
    template_count = sum(1 for phrase in template_phrases if phrase.lower() in content.lower())
    
    # Check for unique content indicators
    unique_phrases = [
        'for example',
        'example:',
        'specific',
        'typically',
        'research shows',
        'studies show',
        'according to',
        'in practice',
        'real-world',
        'common mistake',
        'pro tip',
    ]
    
    unique_count = sum(1 for phrase in unique_phrases if phrase.lower() in content.lower())
    
    # Check for specific numbers (good sign)
    import re
    specific_numbers = len(re.findall(r'\d+\.?\d*\s*(?:lbs?|kg|cm|inches?|mph|km/h|calories?|%)', content.lower()))
    
    # Check for FAQ quality
    faq_count = content.lower().count('faq-item')
    
    # Rating
    if template_count > 3:
        quality = "HEAVILY TEMPLATED - needs rewrite"
    elif template_count > 1:
        quality = "SOME TEMPLATE PHRASES - minor edits needed"
    elif specific_numbers < 5:
        quality = "GENERIC - needs specific examples"
    else:
        quality = "UNIQUE/GOOD"
    
    print(f"\n{cid}: {name}")
    print(f"  Words: {words} | Template phrases: {template_count} | Unique indicators: {unique_count}")
    print(f"  Specific numbers/examples: {specific_numbers} | FAQs: {faq_count}")
    print(f"  VERDICT: {quality}")
    
    if template_count > 0:
        print(f"  Template phrases found:")
        for phrase in template_phrases:
            if phrase.lower() in content.lower():
                print(f"    - '{phrase}'")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("\nTemplate-based content has:")
print("  - Generic phrases like 'the formula behind this calculation'")
print("  - No specific real-world examples with actual numbers")
print("  - Repetitive FAQ answers ('click calculate', 'use the share button')")
print("  - Placeholder text like 'enter your values: 24; 30'")
print("\nUnique content has:")
print("  - Specific scenarios (e.g., 'Sarah, 42 years old, 165 lbs')")
print("  - Actual calculations shown step-by-step")
print("  - Research-backed claims with numbers")
print("  - Distinctive voice and practical advice")
