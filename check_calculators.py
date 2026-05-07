import json, os, glob, re
from collections import defaultdict

CALC_DIR = r'C:\Microsaas\obra\src\calculators'
LANGS = ['es', 'en', 'fr', 'pt', 'de', 'it']

SPANISH_WORDS = [
    '\\bde\\b', '\\bdel\\b', '\\bla\\b', '\\bel\\b', '\\blos\\b', '\\blas\\b', '\\bun\\b', '\\buna\\b', '\\by\\b',
    '\\bcon\\b', '\\bpara\\b', '\\bpor\\b', '\\ben\\b', '\\bque\\b', '\\bes\\b', '\\bson\\b', '\\bcomo\\b', '\\bmás\\b',
    '\\beste\\b', '\\besta\\b', '\\bdesde\\b', '\\bhasta\\b', '\\bentre\\b', '\\bsegún\\b', '\\bsin\\b', '\\bsobre\\b',
    '\\bcada\\b', '\\bentre\\b', '\\bo\\b', '\\bse\\b', '\\bsu\\b', '\\bal\\b', '\\bcálculo\\b', '\\bcalcular\\b',
    '\\bresultado\\b', '\\bvalor\\b', '\\bvalores\\b', '\\bintroduce\\b', '\\bintroducir\\b', '\\bobtener\\b',
    '\\bobtén\\b', '\\bpulsa\\b', '\\bresultados\\b', '\\bfórmula\\b', '\\bunidad\\b', '\\bunidades\\b',
    '\\bpotencia\\b', '\\btensión\\b', '\\bcorriente\\b', '\\bcálculo\\b', '\\bcalculadora\\b',
    '\\butil\\b', '\\butilizada\\b', '\\beléctrico\\b', '\\beléctrica\\b', '\\btérmica\\b', '\\btérmico\\b',
    '\\bdimensionar\\b', '\\bdimensionado\\b', '\\bconsumo\\b', '\\brendimiento\\b', '\\beficiencia\\b',
    '\\bsección\\b', '\\bcable\\b', '\\btubería\\b', '\\binstalación\\b', '\\bvivienda\\b',
    '\\bpresión\\b', '\\btemperatura\\b', '\\bvolumen\\b', '\\bsuperficie\\b', '\\baltura\\b',
    '\\bfrente\\b', '\\bresistencia\\b', '\\benergética\\b', '\\benergético\\b', '\\bclase\\b',
    '\\bclasificar\\b', '\\bmodo\\b', '\\bcalor\\b', '\\bfrío\\b', '\\bestacional\\b', '\\bnominal\\b',
    '\\bcarga\\b', '\\bmáxima\\b', '\\banual\\b', '\\bcatálogo\\b', '\\bensayo\\b', '\\bcondiciones\\b',
    '\\breal\\b', '\\binferior\\b', '\\bconfundir\\b', '\\busar\\b', '\\bignorar\\b', '\\bverificar\\b',
    '\\busados\\b', '\\bdatos\\b', '\\bdato\\b', '\\bhora\\b', '\\bhoras\\b', '\\bdía\\b', '\\bdías\\b',
]

SPANISH_PATTERN = re.compile('|'.join(SPANISH_WORDS), re.IGNORECASE)

TEXT_FIELDS = ['result_context', 'example_label', 'steps', 'mistakes', 'range_hints', 
               'seo_description', 'description', 'formula_display', 'name']

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cid = data.get('id', '???')
    slug = data.get('slug', '???')
    issues = []
    
    inputs = data.get('inputs', [])
    outputs = data.get('outputs', [])
    input_ids = {inp['id'] for inp in inputs}
    output_ids = {out['id'] for out in outputs}
    
    i18n = data.get('i18n', {})
    
    for lang in LANGS:
        if lang not in i18n:
            issues.append(f'{lang}: MISSING ENTIRE LANGUAGE')
            continue
        
        ld = i18n[lang]
        
        # Check empty/missing fields
        for field in ['example_label', 'result_context', 'formula_display']:
            if not ld.get(field) or not ld[field].strip():
                issues.append(f'{lang}: EMPTY {field}')
        
        if not ld.get('steps') or len(ld['steps']) == 0:
            issues.append(f'{lang}: EMPTY steps')
        elif len(ld['steps']) < 3:
            issues.append(f'{lang}: TOO FEW steps ({len(ld["steps"])})')
            
        if not ld.get('mistakes') or len(ld['mistakes']) == 0:
            issues.append(f'{lang}: EMPTY mistakes')
        elif len(ld.get('mistakes', [])) < 2:
            issues.append(f'{lang}: TOO FEW mistakes ({len(ld["mistakes"])})')
        
        # Check SEO lengths
        seo_title = ld.get('seo_title', '')
        if seo_title and len(seo_title) > 60:
            issues.append(f'{lang}: SEO_TITLE too long ({len(seo_title)} chars): {seo_title[:80]}...')
        
        seo_desc = ld.get('seo_description', '')
        if seo_desc and len(seo_desc) > 160:
            issues.append(f'{lang}: SEO_DESC too long ({len(seo_desc)} chars)')
        
        # Check Spanish in non-Spanish languages
        if lang != 'es' and lang != 'pt':
            for field in TEXT_FIELDS:
                val = ld.get(field)
                if val is None:
                    continue
                if isinstance(val, str):
                    matches = SPANISH_PATTERN.findall(val)
                    if matches:
                        issues.append(f'{lang}: SPANISH in {field}: found {sorted(set(m[:20] for m in matches))[:5]}')
                elif isinstance(val, list):
                    for i, item in enumerate(val):
                        matches = SPANISH_PATTERN.findall(item)
                        if matches:
                            issues.append(f'{lang}: SPANISH in {field}[{i}]: found {sorted(set(m[:20] for m in matches))[:5]}')
        
        # Check input labels
        inp_labels = ld.get('inputs', {})
        for inp_id in input_ids:
            if inp_id not in inp_labels:
                issues.append(f'{lang}: MISSING input label: {inp_id}')
        
        # Check output labels
        out_labels = ld.get('outputs', {})
        for out_id in output_ids:
            if out_id not in out_labels:
                issues.append(f'{lang}: MISSING output label: {out_id}')
        
        # Check Spanish in pt (some overlap but flag)
        if lang == 'pt':
            for field in TEXT_FIELDS:
                val = ld.get(field)
                if val is None:
                    continue
                if isinstance(val, str) and (' eléctrico' in val or ' térmico' in val or 'presión ' in val):
                    issues.append(f'{lang}: POSSIBLE spanish in {field}')
    
    return cid, slug, issues

if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(CALC_DIR, '*.json')))
    all_issues = {}
    
    for f in files:
        try:
            cid, slug, issues = check_file(f)
            if int(cid) > 50:
                continue
            if issues:
                all_issues[cid] = {'slug': slug, 'file': os.path.basename(f), 'issues': issues}
                print(f"\n{'='*80}")
                print(f"ID {cid}: {slug} ({os.path.basename(f)})")
                for issue in issues:
                    print(f"  - {issue}")
        except Exception as e:
            print(f"ERROR in {f}: {e}")
    
    print(f"\n{'='*80}")
    total_issues = sum(len(v['issues']) for v in all_issues.values())
    print(f"Total files with issues: {len(all_issues)}")
    print(f"Total issues: {total_issues}")
