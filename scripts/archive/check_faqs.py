import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'C:\\Microsaas\\obra\\scripts')
from calc_content import FAQS
block = 'estructuras'
print(f'Block: {block}')
print(f'EN FAQs ({len(FAQS[block]["en"])}):')
for i, faq in enumerate(FAQS[block]['en'][:3]):
    print(f'  FAQ {i}: {type(faq).__name__} = {str(faq)[:120]}')