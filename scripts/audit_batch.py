import json, os

with open(r'C:\Microsaas\obra\src\calculators\calculators.json', 'r', encoding='utf-8') as f:
    calcs = json.load(f)

calc_by_id = {}
for c in calcs:
    cid = str(c.get('id', ''))
    calc_by_id[cid] = c

target_ids = [
    '946', '947', '948', '949', '950',
    '951', '952', '953', '954', '955', '956',
    '1097', '1098', '1099',
    '1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009',
    '1010', '1011', '1012', '1013', '1014', '1015', '1016', '1017', '1018', '1019',
    '1070', '1071', '1072', '1073', '1074', '1075', '1076', '1077', '1078', '1079',
    '1087', '1088', '1089',
]

with open(r'C:\Microsaas\obra\src\i18n\en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open(r'C:\Microsaas\obra\src\i18n\es.json', 'r', encoding='utf-8') as f:
    es = json.load(f)

en_calcs = en.get('calculators', {})
es_calcs = es.get('calculators', {})

content_en_dir = r'C:\Microsaas\obra\src\content\en'
content_es_dir = r'C:\Microsaas\obra\src\content\es'

header = f'{"ID":<6} {"Slug":<35} {"Def":<5} {"EN_i18n":<8} {"ES_i18n":<8} {"EN_html":<8} {"ES_html":<8} {"Formula":<8} {"Status":<8} {"Issues"}'
print('=' * 140)
print(header)
print('=' * 140)

pass_count = 0
fail_count = 0
partial_count = 0
missing_count = 0

for tid in target_ids:
    issues = []

    if tid not in calc_by_id:
        line = f'{tid:<6} {"---":<35} {"MISS":<5}'
        print(line)
        missing_count += 1
        continue

    c = calc_by_id[tid]
    slug = c.get('slug', '')

    formula = c.get('formula', '')
    inputs = c.get('inputs', [])
    outputs = c.get('outputs', [])
    formula_ok = 'OK'
    if not formula:
        formula_ok = 'MISS'
        issues.append('No formula')
    if not inputs:
        issues.append('No inputs')
    if not outputs:
        issues.append('No outputs')

    en_data = en_calcs.get(tid, {})
    en_ok = 'OK' if en_data else 'MISS'
    if en_data:
        en_title = en_data.get('seo_title', '')
        en_desc = en_data.get('seo_description', '')
        en_label = en_data.get('label', '')
        if not en_title:
            issues.append('EN: missing seo_title')
        elif len(en_title) < 30:
            issues.append(f'EN: short seo_title ({len(en_title)}ch)')
        if not en_desc:
            issues.append('EN: missing seo_description')
        elif len(en_desc) < 50:
            issues.append(f'EN: short seo_desc ({len(en_desc)}ch)')
        if not en_label:
            issues.append('EN: missing label')

    es_data = es_calcs.get(tid, {})
    es_ok = 'OK' if es_data else 'MISS'
    if es_data:
        es_title = es_data.get('seo_title', '')
        es_desc = es_data.get('seo_description', '')
        es_label = es_data.get('label', '')
        if not es_title:
            issues.append('ES: missing seo_title')
        elif len(es_title) < 30:
            issues.append(f'ES: short seo_title ({len(es_title)}ch)')
        if not es_desc:
            issues.append('ES: missing seo_description')
        elif len(es_desc) < 50:
            issues.append(f'ES: short seo_desc ({len(es_desc)}ch)')
        if not es_label:
            issues.append('ES: missing label')

    en_html_path = os.path.join(content_en_dir, f'{tid}.html')
    es_html_path = os.path.join(content_es_dir, f'{tid}.html')
    en_html = 'OK' if os.path.exists(en_html_path) else 'MISS'
    es_html = 'OK' if os.path.exists(es_html_path) else 'MISS'

    if en_html == 'MISS':
        issues.append('EN content file missing')
    if es_html == 'MISS':
        issues.append('ES content file missing')

    if en_html == 'OK':
        sz = os.path.getsize(en_html_path)
        if sz < 2000:
            issues.append(f'EN content thin ({sz}B)')
    if es_html == 'OK':
        sz = os.path.getsize(es_html_path)
        if sz < 2000:
            issues.append(f'ES content thin ({sz}B)')

    if not issues:
        status = 'PASS'
        pass_count += 1
    else:
        has_miss = False
        for check in [en_ok, es_ok, en_html, es_html, formula_ok]:
            if check == 'MISS':
                has_miss = True
        if has_miss:
            status = 'FAIL'
            fail_count += 1
        else:
            status = 'PARTIAL'
            partial_count += 1

    issue_str = '; '.join(issues) if issues else '-'
    line = f'{tid:<6} {slug:<35} {"OK":<5} {en_ok:<8} {es_ok:<8} {en_html:<8} {es_html:<8} {formula_ok:<8} {status:<8} {issue_str}'
    print(line)

print('=' * 140)
print(f'SUMMARY: {len(target_ids)} audited | PASS: {pass_count} | PARTIAL: {partial_count} | FAIL: {fail_count} | MISSING_DEF: {missing_count}')
