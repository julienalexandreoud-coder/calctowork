import json

data = json.load(open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'r', encoding='utf-8'))
calcs = data['calculators']
calc_by_id = {c['id']: c for c in calcs}

REMAINING = {
    '937': ['936', '938', '314'],    # debt-payoff -> mortgage, savings, pension
    '939': ['937', '320', '940'],    # profit-margin -> debt-payoff, CAGR, NPV
    '941': ['938', '936', '937'],    # emergency-fund -> savings, mortgage, debt-payoff
    '945': ['320', '936', '934'],    # double-discount -> CAGR, mortgage, salary-to-hourly
    '946': ['947', '948', '127'],   # kinetic-energy -> potential-energy, work-power, torque
    '947': ['946', '948', '950'],   # potential-energy -> kinetic-energy, work-power, ohms
    '948': ['946', '947', '951'],   # work-power -> kinetic-energy, potential-energy, watts
    '949': ['950', '951', '948'],   # ohms-law-power -> ohms, watts, work-power
}

changed = 0
for cid, related in REMAINING.items():
    if cid in calc_by_id and not calc_by_id[cid].get('related'):
        calc_by_id[cid]['related'] = related
        changed += 1

print(f'Added related links to {changed} calculators')

no_related = [c for c in calcs if not c.get('related')]
print(f'Remaining without related: {len(no_related)}')

with open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')