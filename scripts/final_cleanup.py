"""Final cleanup: fix spacing, extend short descriptions, remove 'for category' patterns."""
import json, os, re

I18N_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'i18n')

TOTAL = 0

for lang in ['es', 'fr', 'pt', 'de', 'it']:
    fpath = os.path.join(I18N_DIR, f'{lang}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    calcs = data['calculators']
    fixed = 0
    
    for cid, ci in calcs.items():
        desc = ci.get('seo_description', '') or ci.get('seo_desc', '')
        
        # Fix double spaces
        new_desc = re.sub(r'\s{2,}', ' ', desc)
        
        # Fix "for X." pattern - remove it and replace with a proper ending
        # E.g., "Calculate X for construction. Y." -> "Calculate X. Y."
        for_patterns = [
            r' para construccion\.\s*',
            r' para mamposteria\.\s*',
            r' para pavimentos\.\s*',
            r' para fontaneria\.\s*',
            r' para electricidad\.\s*',
            r' para climatizacion\.\s*',
            r' para carpinteria\.\s*',
            r' para pintura\.\s*',
            r' para gestion\.\s*',
            r' para matematicas\.\s*',
            r' para finanzas\.\s*',
            r' para salud\.\s*',
            r' para cotidiano\.\s*',
            r' para estadistica\.\s*',
            r' para ciencia\.\s*',
            r' para conversion\.\s*',
            r' para deporte\.\s*',
            r' para ingenieria\.\s*',
            r' para quimica\.\s*',
            r' para electronica\.\s*',
            r' para transporte\.\s*',
            r' para fotografia\.\s*',
            r' para clima\.\s*',
            r' para utilidades\.\s*',
            r" pour construction\.\s*",
            r" pour maconnerie\.\s*",
            r" pour revetement\.\s*",
            r" pour plomberie\.\s*",
            r" pour electricite\.\s*",
            r" pour climatisation\.\s*",
            r" pour menuiserie\.\s*",
            r" pour peinture\.\s*",
            r" pour gestion\.\s*",
            r" pour mathematiques\.\s*",
            r" pour finance\.\s*",
            r" pour sante\.\s*",
            r" pour quotidien\.\s*",
            r" pour statistiques\.\s*",
            r" pour science\.\s*",
            r" pour conversion\.\s*",
            r" pour sport\.\s*",
            r" pour ingenierie\.\s*",
            r" pour chimie\.\s*",
            r" pour electronique\.\s*",
            r" pour transport\.\s*",
            r" pour photographie\.\s*",
            r" pour climat\.\s*",
            r" pour utilitaires\.\s*",
            r' para construcao\.\s*',
            r' para alvenaria\.\s*',
            r' para piso\.\s*',
            r' para encanamento\.\s*',
            r' para eletricidade\.\s*',
            r' para climatizacao\.\s*',
            r' para carpintaria\.\s*',
            r' para pintura\.\s*',
            r' para gestao\.\s*',
            r' para matematica\.\s*',
            r' para financas\.\s*',
            r' para saude\.\s*',
            r' para cotidiano\.\s*',
            r' para estatistica\.\s*',
            r' para ciencia\.\s*',
            r' para conversao\.\s*',
            r' para esporte\.\s*',
            r' para engenharia\.\s*',
            r' para quimica\.\s*',
            r' para eletronica\.\s*',
            r' para transporte\.\s*',
            r' para fotografia\.\s*',
            r' para clima\.\s*',
            r' para utilidades\.\s*',
            r" fur Bau\.\s*",
            r" fur Mauerwerk\.\s*",
            r" fur Boden\.\s*",
            r" fur Sanitar\.\s*",
            r" fur Elektrik\.\s*",
            r" fur Klima\.\s*",
            r" fur Zimmerei\.\s*",
            r" fur Maler\.\s*",
            r" fur Gesch\w*\.\s*",
            r" fur Math\w*\.\s*",
            r" fur Finanz\w*\.\s*",
            r" fur Gesund\w*\.\s*",
            r" fur Allt\w*\.\s*",
            r" fur Stati\w*\.\s*",
            r" fur Wiss\w*\.\s*",
            r" fur Umrec\w*\.\s*",
            r" fur Sport\w*\.\s*",
            r" fur Inge\w*\.\s*",
            r" fur Chemie\.\s*",
            r" fur Elek\w*\.\s*",
            r" fur Trans\w*\.\s*",
            r" fur Foto\w*\.\s*",
            r" fur Wetter\.\s*",
            r" fur Hilf\w*\.\s*",
            r" per costru\w*\.\s*",
            r" per murat\w*\.\s*",
            r" per pavim\w*\.\s*",
            r" per idrau\w*\.\s*",
            r" per elettr\w*\.\s*",
            r" per climat\w*\.\s*",
            r" per carpe\w*\.\s*",
            r" per pitt\w*\.\s*",
            r" per gesti\w*\.\s*",
            r" per matema\w*\.\s*",
            r" per finan\w*\.\s*",
            r" per salute\.\s*",
            r" per quoti\w*\.\s*",
            r" per stati\w*\.\s*",
            r" per scien\w*\.\s*",
            r" per conver\w*\.\s*",
            r" per sport\w*\.\s*",
            r" per ingeg\w*\.\s*",
            r" per chim\w*\.\s*",
            r" per tras\w*\.\s*",
            r" per foto\w*\.\s*",
            r" per met\w*\.\s*",
            r" per util\w*\.\s*",
        ]
        
        for pat in for_patterns:
            new_desc = re.sub(pat, '', new_desc).strip()
        
        # Fix sentences starting with lowercase after period-space
        new_desc = re.sub(r'\.\s+([a-z])', lambda m: '. ' + m.group(1).upper(), new_desc)
        
        # Fix sentence fragments that don't end properly
        if not new_desc.endswith('.'):
            new_desc += '.'
        
        # Remove trailing spaces before period
        new_desc = re.sub(r'\s+\.', '.', new_desc)
        
        if new_desc != desc:
            ci['seo_description'] = new_desc
            ci['seo_desc'] = new_desc
            fixed += 1
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    
    print(f"  {lang}: cleaned {fixed} descriptions")
    TOTAL += fixed

print(f"\n  Total cleaned: {TOTAL}")