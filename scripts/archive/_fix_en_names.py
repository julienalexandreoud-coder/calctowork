"""Fix ALL English names based on actual calculator function (inputs/outputs/formula)."""
import json, glob

# Map: calculator_id -> correct English name (determined by reading actual inputs/outputs)
FIXES = {
    # Finance block - names shifted by +2 positions
    "300": "Mortgage Calculator",
    "301": "Loan Payment Calculator",
    "302": "Compound Interest Calculator",
    "303": "Simple Interest Calculator",
    "305": "Net Salary Calculator",
    "306": "Discount Calculator",
    "307": "Break-Even Point Calculator",
    "310": "ROI Calculator",
    "311": "Compound Savings Calculator",
    "312": "Inflation Calculator",
    "313": "Salary Increase Calculator",
    "314": "Retirement Savings Calculator",
    "315": "Rule of 72 Calculator",
    "316": "Fixed Deposit Calculator",
    "318": "Debt-to-Income Ratio Calculator",
    "319": "Break-Even Analysis Calculator",
    "320": "CAGR Calculator",
    "321": "APR Calculator",
    "322": "Loan Amortization Calculator",
    "323": "Rental Yield Calculator",
    "324": "Cap Rate Calculator",
    "325": "Dividend Yield Calculator",
    "326": "P/E Ratio Calculator",
    "327": "Future Value of Annuity Calculator",
    "328": "Present Value of Annuity Calculator",
    "329": "WACC Calculator",
    "330": "Payback Period Calculator",
    "331": "Sharpe Ratio Calculator",
    "332": "Tax Equivalent Yield Calculator",
    "333": "Real Rate of Return Calculator",
    "334": "Loan Affordability Calculator",
    "335": "Early Mortgage Payoff Calculator",
    "336": "Credit Card Payoff Calculator",
    "337": "College Savings Calculator",
    "338": "Life Insurance Needs Calculator",
    "339": "Monthly CAGR Calculator",
    
    # Cotidiano block - completely wrong English names
    "500": "Tip Calculator",
    "501": "Age Calculator",
    "502": "Date Difference Calculator",
    "503": "Fuel Cost Calculator",
    "504": "Data Transfer Time Calculator",
    "505": "Battery Life Calculator",
    "506": "Download Time Calculator",
    "507": "Screen DPI Calculator",
    "508": "Aspect Ratio Calculator",
    "509": "Password Strength Checker",
    "510": "Bandwidth Calculator",
    "511": "Image File Size Calculator",
    "512": "Electricity Cost Calculator",
    "513": "Screen Resolution Calculator",
    "514": "Video File Size Calculator",
    "515": "RAID Capacity Calculator",
    "516": "Uptime & SLA Calculator",
    "517": "Network Latency Calculator",
    "518": "Typing Speed Test (WPM)",
    "519": "Reading Time Calculator",
    "520": "SMS Cost Calculator",
    "521": "Data Usage Estimator",
    
    # Conversion block
    "800": "Length Converter",
    "801": "Weight Converter",
    "802": "Temperature Converter",
    "803": "Volume Converter",
    "804": "Area Converter",
    "805": "Speed Converter",
    "806": "Digital Storage Converter",
    "807": "Pressure Converter",
    "808": "Time Units Converter",
    "809": "Energy Converter",
    
    # Chemistry block
    "1000": "pH Calculator",
    "1001": "pOH Calculator",
    "1002": "Molarity Calculator",
    "1003": "Dilution Calculator",
    "1004": "Ideal Gas Law Calculator",
    "1005": "Boyle's Law Calculator",
    "1006": "Charles's Law Calculator",
    "1007": "Gibbs Free Energy Calculator",
    "1008": "Molecular Weight Calculator",
    "1009": "Titration Calculator",
    
    # Electronics block  
    "1010": "Voltage Divider Calculator",
    "1011": "LED Resistor Calculator",
    "1012": "Parallel Resistance Calculator",
    "1013": "Capacitor Energy Calculator",
    "1014": "Inductor Energy Calculator",
    "1015": "Transformer Turns Ratio Calculator",
    "1016": "RC Time Constant Calculator",
    "1017": "Wheatstone Bridge Calculator",
    "1018": "Series Capacitance Calculator",
    "1019": "Resistor Color Code Calculator",
    
    # Sports block
    "900": "Running Pace Calculator",
    "901": "Calories Burned Calculator",
    "902": "Max Heart Rate Calculator",
    "903": "Heart Rate Zones Calculator",
    "904": "VO2 Max Calculator",
    "905": "Steps to Calories Calculator",
    "906": "Swimming Pace Calculator",
    "907": "Cycling Speed Calculator",
    "908": "Athlete BMI Calculator",
    "909": "Track Time Calculator",
    
    # Construction batch (1100-1119)
    "1100": "Decking Calculator",
    "1101": "Sod & Turf Calculator",
    "1102": "Mulch Calculator",
    "1103": "Fence Picket Calculator",
    "1104": "Roofing Shingle Calculator",
    "1105": "Insulation Batt Calculator",
    "1106": "Carpet Calculator",
    "1107": "Laminate Flooring Calculator",
    "1108": "Countertop Calculator",
    "1109": "Backsplash Tile Calculator",
    "1110": "Grout Calculator",
    "1111": "Paint Coverage Calculator",
    "1112": "Wallpaper Calculator",
    "1113": "Crown Molding Calculator",
    "1114": "Baseboard Calculator",
    "1115": "Drywall Calculator",
    "1116": "Concrete Steps Calculator",
    "1117": "Retaining Wall Calculator",
    "1118": "Paver Calculator",
    "1119": "Landscape Rock Calculator",
    
    # Math - wrongly named  
    "910": "Fraction Calculator",
    "911": "Slope Calculator",
    "912": "Scientific Notation Calculator",
    "913": "Rounding Calculator",
    "914": "GCF & LCM Calculator",
    "915": "Prime Factorization Calculator",
    "916": "Circle Calculator",
    "917": "Right Triangle Calculator",
    
    # Health - shifted
    "414": "Healthy Weight Range Calculator",
    "415": "Lean Body Mass Calculator",
    "416": "Body Adiposity Index Calculator",
    "418": "Fiber Intake Calculator",
    "420": "Heart Rate Zones Calculator",
    "422": "BMI Prime Calculator",
    "425": "Navy Body Fat Calculator",
    "426": "TDEE Calculator",
    "427": "BMR Calculator (Mifflin-St Jeor)",
    "428": "Resting Metabolic Rate Calculator",
    "431": "Pregnancy Weight Gain Calculator",
    "432": "Calories Burned Walking Calculator",
    "434": "Water Intake by Weight Calculator",
    
    # Statistics
    "606": "Confidence Interval Calculator",
    "607": "Coefficient of Variation Calculator",
    "609": "Z-Score Calculator",
    
    # Science
    "701": "Density Calculator",
    "707": "Ohm's Law Calculator",
}

fixed = 0
for fp in sorted(glob.glob('src/calculators/*.json')):
    with open(fp,'r',encoding='utf-8') as f:
        d = json.load(f)
    cid = d['id']
    if cid in FIXES:
        old_name = d.get('i18n',{}).get('en',{}).get('name','')
        new_name = FIXES[cid]
        if old_name != new_name:
            d['i18n']['en']['name'] = new_name
            with open(fp,'w',encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
                f.write('\n')
            fixed += 1
            print(f'  {cid}: "{old_name}" -> "{new_name}"')

print(f'\nFixed {fixed} English names')
