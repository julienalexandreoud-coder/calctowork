#!/usr/bin/env python3
"""Fix English — remaining blocks: cotidiano, deportes, quimica, electronica, conversion, estadistica, clima, utilidades, transporte, fotografia."""

import json, os, glob
CALC = r"C:\Microsaas\obra\src\calculators"

f = {}
# ── cotidiano (Everyday) ──
f.update({
    "600": {"name": "Age Calculator", "description": "Calculate your exact age in years, months, and days. Enter your birth date for precise age calculation.", "seo_title": "Age Calculator — Years, Months & Days | CalcToWork", "seo_description": "Calculate your exact age. Enter birth date. Free everyday calculator."},
    "601": {"name": "Date Difference Calculator", "description": "Calculate the number of days between two dates. Enter start and end dates.", "seo_title": "Date Difference Calculator — Days Between | CalcToWork", "seo_description": "Calculate days between two dates. Free date calculator."},
    "602": {"name": "Day of Year Calculator", "description": "Find what day of the year a date falls on. Calculate the day number (1-366).", "seo_title": "Day of Year Calculator — Julian Day | CalcToWork", "seo_description": "Calculate day number of the year. Free date calculator."},
    "603": {"name": "Week Number Calculator", "description": "Find the ISO week number for any date. Know which week of the year it is.", "seo_title": "Week Number Calculator — ISO 8601 | CalcToWork", "seo_description": "Calculate ISO week number. Free calendar and date calculator."},
    "604": {"name": "Working Days Calculator", "description": "Calculate working days between dates, excluding weekends and holidays. Great for project planning.", "seo_title": "Working Days Calculator — Business Days | CalcToWork", "seo_description": "Calculate business days between dates. Excludes weekends. Free project planning tool."},
    "605": {"name": "Tip Calculator (Advanced)", "description": "Calculate tip amount and split bill among people. Enter bill, tip percentage, and number of people.", "seo_title": "Advanced Tip Calculator — Split Bill | CalcToWork", "seo_description": "Calculate tip and split the bill. Free restaurant and service calculator."},
    "606": {"name": "Reading Time Calculator", "description": "Calculate how long it takes to read a text. Enter word count and reading speed.", "seo_title": "Reading Time Calculator — Minutes | CalcToWork", "seo_description": "Estimate reading time from word count. Free productivity calculator."},
    "607": {"name": "Typing Speed Calculator (WPM)", "description": "Calculate your typing speed in words per minute. Enter words typed and time.", "seo_title": "Typing Speed Calculator — WPM | CalcToWork", "seo_description": "Calculate typing speed in WPM. Free productivity and skill calculator."},
    "609": {"name": "Golf Handicap Calculator", "description": "Calculate your golf handicap index. Enter your scores, course rating, and slope.", "seo_title": "Golf Handicap Calculator — Index | CalcToWork", "seo_description": "Calculate golf handicap index. Free sports calculator."},
    "610": {"name": "Password Entropy Calculator", "description": "Check the strength of a password. Calculate entropy in bits and estimated crack time.", "seo_title": "Password Strength Calculator — Entropy | CalcToWork", "seo_description": "Check password strength and entropy. Free security calculator."},
    "611": {"name": "Password Generator", "description": "Generate strong random passwords. Choose length, character types, and quantity.", "seo_title": "Password Generator — Strong & Random | CalcToWork", "seo_description": "Generate secure random passwords. Free security tool."},
    "613": {"name": "Text Character Counter", "description": "Count characters, words, sentences, and paragraphs in any text. Paste or type for instant counts.", "seo_title": "Character Counter — Text Statistics | CalcToWork", "seo_description": "Count characters, words and sentences. Free text analysis tool."},
    "614": {"name": "File Size Calculator", "description": "Calculate file sizes and convert between bytes, KB, MB, GB, TB. Digital storage calculator.", "seo_title": "File Size Calculator — Digital Storage | CalcToWork", "seo_description": "Calculate and convert file sizes. Free digital storage calculator."},
    "615": {"name": "Video File Size Calculator", "description": "Estimate video file size based on resolution, bitrate, frame rate, and duration.", "seo_title": "Video File Size Calculator — Bitrate | CalcToWork", "seo_description": "Estimate video file size. Free multimedia calculator."},
    "616": {"name": "Data Transfer Time Calculator", "description": "Calculate download or upload time. Enter file size and connection speed.", "seo_title": "Download Time Calculator — Speed | CalcToWork", "seo_description": "Calculate data transfer time. Free network and internet calculator."},
    "617": {"name": "Ping Latency Calculator", "description": "Understand network latency. Calculate round-trip time effects on data transfers.", "seo_title": "Ping Latency Calculator — Network | CalcToWork", "seo_description": "Calculate network latency effects. Free networking calculator."},
    "618": {"name": "Bandwidth Calculator", "description": "Calculate required bandwidth for data transfer. Enter file size and transfer time.", "seo_title": "Bandwidth Calculator — Mbps & Gbps | CalcToWork", "seo_description": "Calculate bandwidth requirements. Free networking calculator."},
    "619": {"name": "Battery Life Calculator", "description": "Calculate battery runtime. Enter battery capacity and device power consumption.", "seo_title": "Battery Runtime Calculator — Hours | CalcToWork", "seo_description": "Calculate battery life and runtime. Free electronics calculator."},
    "620": {"name": "Battery Autonomy Calculator", "description": "Calculate battery autonomy for solar or backup systems. Enter capacity and load.", "seo_title": "Battery Autonomy Calculator — Backup | CalcToWork", "seo_description": "Calculate battery backup autonomy. Free solar and electronics calculator."},
    "621": {"name": "Screen Resolution Calculator", "description": "Calculate screen resolution, pixels, aspect ratio. Enter width and height.", "seo_title": "Screen Resolution Calculator — Pixels | CalcToWork", "seo_description": "Calculate screen resolution and aspect ratio. Free display calculator."},
    "622": {"name": "Screen DPI Calculator", "description": "Calculate DPI (dots per inch) of a display. Enter resolution and screen size.", "seo_title": "DPI Calculator — Screen Density | CalcToWork", "seo_description": "Calculate screen DPI from resolution and size. Free display calculator."},
    "623": {"name": "Screen Brightness (Nits) Calculator", "description": "Calculate screen brightness in nits (cd/m²). Enter lumens and screen area.", "seo_title": "Nits Calculator — Screen Brightness | CalcToWork", "seo_description": "Calculate screen brightness in nits. Free display calculator."},
    "624": {"name": "Aspect Ratio Calculator", "description": "Calculate aspect ratio from width and height. Find equivalent resolutions.", "seo_title": "Aspect Ratio Calculator — 16:9, 4:3 | CalcToWork", "seo_description": "Calculate display aspect ratio. Free multimedia calculator."},
    "625": {"name": "Contrast Ratio Calculator", "description": "Calculate contrast ratio between two colors or luminance values.", "seo_title": "Contrast Ratio Calculator — Colors | CalcToWork", "seo_description": "Calculate contrast ratio. Free design and accessibility calculator."},
    "626": {"name": "Data Usage Estimator", "description": "Estimate monthly data usage based on activities. Calculate streaming, browsing, and download needs.", "seo_title": "Data Usage Calculator — Monthly GB | CalcToWork", "seo_description": "Estimate monthly data usage. Free internet and mobile calculator."},
    "627": {"name": "RAID Capacity Calculator", "description": "Calculate usable storage in RAID configurations. Enter drives, size, and RAID level.", "seo_title": "RAID Calculator — Storage Capacity | CalcToWork", "seo_description": "Calculate RAID array capacity. Free storage calculator."},
    "628": {"name": "Fuel Consumption Calculator", "description": "Calculate fuel consumption in L/100km or MPG. Enter distance and fuel used.", "seo_title": "Fuel Consumption Calculator — L/100km | CalcToWork", "seo_description": "Calculate fuel efficiency. Free automotive calculator."},
    "629": {"name": "Fuel Cost Calculator", "description": "Calculate fuel cost for a trip. Enter distance, consumption, and fuel price.", "seo_title": "Fuel Cost Calculator — Trip Budget | CalcToWork", "seo_description": "Calculate trip fuel cost. Free travel and automotive calculator."},
    "630": {"name": "Tire Pressure Calculator", "description": "Calculate recommended tire pressure. Enter vehicle type, load, and tire specs.", "seo_title": "Tire Pressure Calculator — PSI & Bar | CalcToWork", "seo_description": "Calculate optimal tire pressure. Free automotive calculator."},
    "631": {"name": "Braking Distance Calculator", "description": "Calculate braking distance based on speed, reaction time, and road conditions.", "seo_title": "Braking Distance Calculator — Safety | CalcToWork", "seo_description": "Calculate vehicle braking distance. Free automotive safety calculator."},
    "632": {"name": "Engine Displacement Calculator", "description": "Calculate engine displacement (cc). Enter bore, stroke, and number of cylinders.", "seo_title": "Engine Displacement Calculator — CC | CalcToWork", "seo_description": "Calculate engine displacement in cc. Free automotive calculator."},
    "633": {"name": "Great Circle Distance Calculator", "description": "Calculate the shortest distance between two points on Earth. Enter latitude/longitude coordinates.", "seo_title": "Great Circle Distance Calculator | CalcToWork", "seo_description": "Calculate distance between geographic coordinates. Free navigation calculator."},
})

# ── deportes (Sports & Fitness) ──
f.update({
    "700": {"name": "Running Pace Calculator", "description": "Calculate running pace, speed, and finish times for any distance from 5K to marathon.", "seo_title": "Running Pace Calculator — Race Times | CalcToWork", "seo_description": "Calculate running pace and race finish times. Free running calculator."},
    "701": {"name": "Running Pace Predictor", "description": "Predict race finish times across distances based on a recent performance.", "seo_title": "Race Time Predictor — Marathon | CalcToWork", "seo_description": "Predict race times at different distances. Free running calculator."},
    "702": {"name": "Cycling Speed Calculator", "description": "Calculate cycling speed, cadence, and gear ratios. Enter wheel size and cadence.", "seo_title": "Cycling Speed Calculator — Gear Ratios | CalcToWork", "seo_description": "Calculate cycling speed and gear ratios. Free cycling calculator."},
    "703": {"name": "Swimming Pace Calculator", "description": "Calculate swimming pace per 100m and predict race times for pool and open water.", "seo_title": "Swimming Pace Calculator — 100m Splits | CalcToWork", "seo_description": "Calculate swimming pace and splits. Free swimming calculator."},
    "704": {"name": "One Rep Max Calculator", "description": "Calculate your one-rep maximum for weightlifting exercises. Multiple formulas available.", "seo_title": "1RM Calculator — Weightlifting | CalcToWork", "seo_description": "Calculate one-rep max for bench, squat, deadlift. Free strength training calculator."},
    "705": {"name": "Max Heart Rate Calculator", "description": "Calculate maximum heart rate based on age using multiple formulas.", "seo_title": "Max HR Calculator — Training Zones | CalcToWork", "seo_description": "Calculate maximum heart rate. Free fitness calculator."},
    "706": {"name": "Heart Rate Zones Calculator", "description": "Calculate training heart rate zones for fat burning, endurance, and performance.", "seo_title": "Heart Rate Zones — Training | CalcToWork", "seo_description": "Calculate heart rate training zones. Free fitness calculator."},
    "707": {"name": "VO2 Max Estimator", "description": "Estimate your VO2 max from field tests. Multiple test protocols available.", "seo_title": "VO2 Max Estimator — Fitness Score | CalcToWork", "seo_description": "Estimate VO2 max from Cooper test or Rockport walk. Free fitness calculator."},
    "708": {"name": "Calories Burned by MET", "description": "Calculate calories burned during activities using MET values. Choose from many activities.", "seo_title": "MET Calories Calculator — Exercise | CalcToWork", "seo_description": "Calculate exercise calories using MET values. Free fitness calculator."},
    "709": {"name": "Golf Handicap Calculator", "description": "Calculate your golf handicap index. Enter recent scores and course ratings.", "seo_title": "Golf Handicap Calculator — Index | CalcToWork", "seo_description": "Calculate golf handicap. Free sports calculator."},
    "710": {"name": "Wind Chill Calculator", "description": "Calculate wind chill (feels-like temperature). Enter air temperature and wind speed.", "seo_title": "Wind Chill Calculator — Feels Like | CalcToWork", "seo_description": "Calculate wind chill temperature. Free weather calculator."},
    "711": {"name": "Heat Index Calculator", "description": "Calculate heat index (apparent temperature). Enter temperature and relative humidity.", "seo_title": "Heat Index Calculator — Feels Like | CalcToWork", "seo_description": "Calculate heat index from temperature and humidity. Free weather calculator."},
})

# ── quimica (Chemistry) ──
f.update({
    "800": {"name": "Molarity Calculator", "description": "Calculate molarity (concentration) of a solution. Enter moles of solute and volume of solution.", "seo_title": "Molarity Calculator — Concentration | CalcToWork", "seo_description": "Calculate molarity of solutions. Free chemistry calculator."},
    "801": {"name": "Dilution Calculator", "description": "Calculate dilution factors using C1V1 = C2V2. Enter initial concentration and desired dilution.", "seo_title": "Dilution Calculator — C1V1 = C2V2 | CalcToWork", "seo_description": "Calculate solution dilutions. Free chemistry and lab calculator."},
    "802": {"name": "pH Calculator", "description": "Calculate pH from hydrogen ion concentration. Enter [H+] to find pH value.", "seo_title": "pH Calculator — [H+] to pH | CalcToWork", "seo_description": "Calculate pH from hydrogen ion concentration. Free chemistry calculator."},
    "803": {"name": "pOH Calculator", "description": "Calculate pOH and pH from hydroxide concentration. pH + pOH = 14.", "seo_title": "pOH Calculator — [OH-] to pOH | CalcToWork", "seo_description": "Calculate pOH from hydroxide ions. Free chemistry calculator."},
    "804": {"name": "Molecular Weight Calculator", "description": "Calculate molecular weight from chemical formula. Enter element symbols and quantities.", "seo_title": "Molecular Weight Calculator | CalcToWork", "seo_description": "Calculate molecular mass. Free chemistry calculator."},
    "805": {"name": "Titration Calculator", "description": "Calculate titration results. Enter concentration and volumes for acid-base titrations.", "seo_title": "Titration Calculator — Acid-Base | CalcToWork", "seo_description": "Calculate titration concentrations. Free chemistry calculator."},
    "806": {"name": "Gibbs Free Energy Calculator", "description": "Calculate Gibbs free energy ΔG = ΔH - TΔS. Enter enthalpy, entropy, and temperature.", "seo_title": "Gibbs Free Energy Calculator — ΔG | CalcToWork", "seo_description": "Calculate Gibbs free energy. Free thermodynamics calculator."},
    "807": {"name": "Ideal Gas Law Calculator", "description": "Calculate gas properties using PV = nRT. Enter known values to find the unknown.", "seo_title": "Ideal Gas Law Calculator — PV=nRT | CalcToWork", "seo_description": "Calculate gas pressure, volume, temperature or moles. Free chemistry calculator."},
    "808": {"name": "Boyle's Law Calculator", "description": "Calculate gas pressure and volume using P1V1 = P2V2 at constant temperature.", "seo_title": "Boyle's Law Calculator — P1V1=P2V2 | CalcToWork", "seo_description": "Calculate gas expansion and compression. Free physics and chemistry calculator."},
    "809": {"name": "Charles's Law Calculator", "description": "Calculate gas volume and temperature using V1/T1 = V2/T2 at constant pressure.", "seo_title": "Charles Law Calculator — V1/T1=V2/T2 | CalcToWork", "seo_description": "Calculate gas thermal expansion. Free chemistry calculator."},
})

def apply():
    updated = 0
    for fp in sorted(glob.glob(os.path.join(CALC, "*.json"))):
        if "bak" in fp or "monolithic" in fp or os.path.basename(fp) == "calculators.json": continue
        with open(fp, "r", encoding="utf-8-sig") as fh: calc = json.load(fh)
        cid = calc.get("id", "")
        if cid not in f: continue
        en = calc.setdefault("i18n", {}).setdefault("en", {})
        changed = False
        for k, v in f[cid].items():
            if k in en and en[k] == v: continue
            en[k] = v
            changed = True
        if changed:
            with open(fp, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(calc, fh, ensure_ascii=False, indent=2)
            updated += 1
    print(f"Updated {updated}")

apply()
