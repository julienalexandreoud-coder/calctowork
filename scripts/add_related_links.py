"""Add related links to the 53 calculators that don't have them.
Each calculator gets 2-3 related calculators from the same block/category.
"""
import json

data = json.load(open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'r', encoding='utf-8'))
calcs = data['calculators']

# Build block-to-calcs mapping
block_calcs = {}
for c in calcs:
    block = str(c.get('block', ''))
    if block not in block_calcs:
        block_calcs[block] = []
    block_calcs[block].append(c['id'])

# For each calc without related, assign 2-3 from same block
RELATED_MAP = {
    # Math (block 13)
    '910': ['916', '914', '913'],  # fraction -> circle, gcf-lcm, rounding
    '911': ['917', '920', '925'],  # slope -> right-triangle, square, sphere
    '912': ['913', '914', '916'],   # sci-notation -> rounding, gcf-lcm, circle
    '913': ['912', '910', '914'],   # rounding -> sci-notation, fraction, gcf-lcm
    '914': ['910', '912', '913'],   # gcf-lcm -> fraction, sci-notation, rounding
    '915': ['912', '914', '910'],   # prime-factorization -> sci-notation, gcf-lcm, fraction
    '916': ['925', '922', '919'],   # circle -> sphere, cylinder, rectangle
    '917': ['918', '919', '920'],   # right-triangle -> heron, rectangle, square
    '918': ['917', '921', '919'],   # heron -> right-triangle, trapezoid, rectangle
    '919': ['917', '920', '921'],   # rectangle -> right-triangle, square, trapezoid
    '920': ['919', '921', '917'],   # square -> rectangle, trapezoid, right-triangle
    '921': ['919', '924', '917'],   # trapezoid -> rectangle, pyramid, right-triangle
    '922': ['925', '923', '924'],   # cylinder -> sphere, cone, pyramid
    '923': ['922', '924', '925'],   # cone -> cylinder, pyramid, sphere
    '924': ['922', '923', '921'],   # pyramid -> cylinder, cone, trapezoid
    '925': ['916', '922', '923'],   # sphere -> circle, cylinder, cone
    # Health (block 12)
    '926': ['426', '928', '429'],   # bmr-harris -> TDEE, macro, METs
    '927': ['426', '928', '926'],   # bmr-katch -> TDEE, macro, bmr-harris
    '928': ['426', '926', '429'],   # macro -> TDEE, bmr-harris, METs
    '929': ['426', '928', '422'],   # blood-pressure -> TDEE, macro, BMI Prime
    # Finance (block 11)
    '320': ['321', '936', '314'],    # CAGR -> APR, mortgage, pension
    '321': ['320', '329', '936'],    # APR -> CAGR, WACC, mortgage
    '329': ['331', '320', '321'],    # WACC -> Sharpe, CAGR, APR
    '331': ['329', '309', '300'],    # Sharpe -> WACC, ROI, NPV
    '339': ['320', '936', '314'],    # monthly-CAGR -> CAGR, mortgage, pension
    # Science (block 15)
    '950': ['951', '954', '956'],    # ohms-law -> watts, angle, energy
    '951': ['950', '954', '956'],    # watts-law -> ohms, angle, energy
    '952': ['950', '951', '954'],    # lens-maker -> ohms, watts, angle
    '953': ['426', '928', '429'],    # VO2-max -> TDEE, macro, METs
    '954': ['955', '956', '950'],    # angle -> speed, energy, ohms
    '955': ['954', '956', '950'],    # speed -> angle, energy, ohms
    '956': ['954', '955', '950'],    # energy -> angle, speed, ohms
    '957': ['910', '915', '914'],    # permutations -> fraction, prime-factorization, gcf-lcm
    '958': ['961', '959', '957'],    # z-score -> A1C, sample-size, permutations
    '959': ['958', '957', '961'],    # sample-size -> z-score, permutations, A1C
    '960': ['958', '430', '926'],    # ideal-weight -> z-score, target-weight, bmr-harris
    '961': ['958', '957', '959'],    # A1C -> z-score, permutations, sample-size
    # pH (block 13 math)
    '1000': ['1001', '950', '954'],  # pH -> pOH, ohms, angle
    '1001': ['1000', '950', '951'],  # pOH -> pH, ohms, watts
    # Conversion (block 16)
    '800': ['808', '802', '1080'],   # length -> time, temp, fuel
    '802': ['800', '808', '1080'],   # temp -> length, time, fuel
    '808': ['800', '802', '1080'],   # time -> length, temp, fuel
    # Everyday (block 13-ish)
    '930': ['931', '412', '928'],    # body-fat -> waist-height, sleep, macro
    '931': ['422', '930', '426'],    # waist-height -> BMI Prime, body-fat, TDEE
    '932': ['422', '426', '928'],    # lean-body-mass -> BMI Prime, TDEE, macro
    '933': ['422', '930', '932'],    # healthy-weight -> BMI Prime, body-fat, lean-body-mass
    '934': ['936', '938', '314'],    # salary-to-hourly -> mortgage, savings, pension
    '935': ['934', '936', '938'],    # hourly-to-salary -> salary-to-hourly, mortgage, savings
    '936': ['938', '934', '314'],    # mortgage -> savings, salary-to-hourly, pension
    '938': ['936', '934', '314'],    # savings -> mortgage, salary-to-hourly, pension
    '940': ['936', '938', '300'],    # NPV -> mortgage, savings, IRR
    '942': ['943', '944', '935'],    # age -> date-diff, tip, hourly-to-salary
    '943': ['942', '944', '808'],    # date-diff -> age, tip, time
    '944': ['935', '942', '934'],    # tip -> hourly-to-salary, age, salary-to-hourly
    # Science extended
    '962': ['127', '950', '951'],    # force -> torque, ohms, watts
    '1050': ['320', '936', '300'],    # compound-interest -> CAGR, mortgage, IRR
    '1051': ['950', '951', '127'],    # resistance -> ohms, watts, torque
    '1052': ['954', '956', '955'],    # flow-rate -> angle, energy, speed
    '1053': ['954', '800', '802'],    # density -> angle, length, temp
    '1054': ['954', '955', '956'],    # pressure -> angle, speed, energy
    '1055': ['127', '962', '950'],    # moment-of-inertia -> torque, force, ohms
    '1056': ['127', '950', '951'],    # doppler -> torque, ohms, watts
    '1057': ['128', '127', '962'],    # angular-momentum -> work, torque, force
    '1058': ['1034', '1035', '916'],  #Projectile motion calc related
    '1059': ['124', '952', '127'],    # specific-heat -> heat-transfer, lens, torque
    '1060': ['1050', '936', '938'],   # salary-converter -> compound-interest, mortgage, savings
    '1061': ['1080', '800', '802'],   # fuel-cost -> fuel-consumption, length, temp
    '1062': ['932', '930', '426'],    # ideal-body-weight -> lean-body, body-fat, TDEE
    '1063': ['1064', '935', '934'],   # net-salary -> gross-salary, hourly, salary
    '1064': ['1063', '934', '935'],   # gross-salary -> net-salary, salary-to-hourly, hourly
    '1065': ['1064', '1063', '936'],   # inflation -> gross-salary, net-salary, mortgage
    '1066': ['960', '933', '422'],    # protein -> ideal-weight, healthy-weight, BMI Prime
    '1067': ['928', '426', '429'],    # water-intake -> macro, TDEE, METs
    '1068': ['1064', '934', '935'],   # ROI -> gross-salary, salary-to-hourly, hourly
    '1069': ['936', '940', '300'],    # break-even -> mortgage, NPV, IRR
    '1070': ['1050', '936', '938'],   # discount -> compound-interest, mortgage, savings
    '1071': ['1000', '950', '951'],   # pH from pOH -> pH, ohms, watts
    '1080': ['800', '808', '802'],    # fuel-consumption -> length, time, temp
    '1084': ['800', '808', '956'],    # flight-time -> length, time, energy
    '1085': ['800', '808', '1080'],   # distance -> length, time, fuel-consumption
    '1088': ['800', '808', '1080'],   # speed-distance -> length, time, fuel-consumption
    '1090': ['960', '930', '933'],    # pork-cooking -> ideal-weight, body-fat, healthy-weight
    '1091': ['930', '422', '426'],    # body-type -> body-fat, BMI Prime, TDEE
    '1092': ['428', '926', '426'],    # erythrocyte -> RMR, bmr-harris, TDEE
    '1093': ['426', '928', '429'],    # calorie-deficit -> TDEE, macro, METs
    '1094': ['426', '928', '412'],    # water-deficit -> TDEE, macro, sleep
    '1095': ['429', '426', '928'],    # calorie-burn -> METs, TDEE, macro
    '1096': ['426', '928', '953'],    # macro-tracker -> TDEE, macro, VO2
    '1097': ['426', '928', '429'],    # kcal -> TDEE, macro, METs
    '1098': ['926', '927', '426'],    # basal-caloric -> bmr-harris, bmr-katch, TDEE
    '1099': ['426', '928', '429'],    # BMI -> TDEE, macro, METs
}

changed = 0
calc_by_id = {c['id']: c for c in calcs}
for cid, related in RELATED_MAP.items():
    if cid in calc_by_id and not calc_by_id[cid].get('related'):
        calc_by_id[cid]['related'] = related
        changed += 1

print(f'Added related links to {changed} calculators')

# Verify no remaining without related
no_related = [c for c in calcs if not c.get('related')]
print(f'Remaining without related: {len(no_related)}')

with open('C:\\Microsaas\\obra\\src\\calculators\\calculators.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')