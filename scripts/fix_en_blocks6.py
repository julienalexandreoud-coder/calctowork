#!/usr/bin/env python3
"""Fix English — final blocks: electronica, conversion, estadistica, clima, utilidades, transporte, fotografia, ingenieria."""

import json, os, glob
CALC = r"C:\Microsaas\obra\src\calculators"
f = {}

# ── electronica (Electronics) ──
f.update({
    "900": {"name": "Ohm's Law Calculator", "description": "Calculate voltage, current, and resistance using Ohm's Law V = IR. Enter two values to find the third.", "seo_title": "Ohm's Law Calculator — V = IR | CalcToWork", "seo_description": "Calculate voltage, current and resistance. Free electronics calculator."},
    "901": {"name": "Ohm's Law — Power Calculator", "description": "Calculate electrical power P = VI = I²R = V²/R. Enter voltage and current.", "seo_title": "Ohm's Law Power Calculator — P=VI | CalcToWork", "seo_description": "Calculate electrical power. Free electronics and physics calculator."},
    "902": {"name": "LED Resistor Calculator", "description": "Calculate the current-limiting resistor for an LED circuit. Enter supply voltage, LED voltage, and current.", "seo_title": "LED Resistor Calculator — Protection | CalcToWork", "seo_description": "Calculate resistor value for LED circuits. Free electronics calculator."},
    "903": {"name": "Resistor Color Code Calculator", "description": "Decode resistor color bands to find resistance value and tolerance. 4, 5, and 6 band support.", "seo_title": "Resistor Color Code Calculator — Decoder | CalcToWork", "seo_description": "Decode resistor color bands. Free electronics and engineering calculator."},
    "904": {"name": "Series Capacitance Calculator", "description": "Calculate total capacitance for capacitors in series or parallel. Enter individual capacitance values.", "seo_title": "Capacitance Calculator — Series & Parallel | CalcToWork", "seo_description": "Calculate equivalent capacitance. Free electronics calculator."},
    "905": {"name": "Parallel Resistance Calculator", "description": "Calculate equivalent resistance for resistors in parallel. Enter individual resistance values.", "seo_title": "Parallel Resistance Calculator — 1/R | CalcToWork", "seo_description": "Calculate parallel resistance. Free electronics calculator."},
    "906": {"name": "Voltage Divider Calculator", "description": "Calculate output voltage of a resistive divider. Enter input voltage and resistor values.", "seo_title": "Voltage Divider Calculator — Vout | CalcToWork", "seo_description": "Calculate voltage divider output. Free electronics calculator."},
    "907": {"name": "RC Time Constant Calculator", "description": "Calculate the time constant τ = RC for resistor-capacitor circuits.", "seo_title": "RC Time Constant Calculator — τ | CalcToWork", "seo_description": "Calculate RC circuit time constant. Free electronics calculator."},
    "908": {"name": "RC Circuit Calculator", "description": "Calculate RC circuit behavior — charge, discharge, cutoff frequency.", "seo_title": "RC Circuit Calculator — Filter | CalcToWork", "seo_description": "Calculate RC filter characteristics. Free electronics calculator."},
    "909": {"name": "RL Circuit Calculator", "description": "Calculate RL circuit behavior and time constant τ = L/R.", "seo_title": "RL Circuit Calculator — Time Constant | CalcToWork", "seo_description": "Calculate RL circuit time constant. Free electronics calculator."},
    "910": {"name": "AC Impedance Calculator", "description": "Calculate AC impedance for R, L, and C circuits. Enter frequency and component values.", "seo_title": "AC Impedance Calculator — RLC | CalcToWork", "seo_description": "Calculate AC circuit impedance. Free electronics and physics calculator."},
    "911": {"name": "Three-Phase Power Calculator", "description": "Calculate three-phase electrical power. Enter voltage, current, and power factor.", "seo_title": "Three Phase Power Calculator — kW | CalcToWork", "seo_description": "Calculate three-phase power. Free electrical engineering calculator."},
    "912": {"name": "Electric Power Cost Calculator", "description": "Calculate electricity cost of appliances. Enter power, hours used, and electricity rate.", "seo_title": "Electricity Cost Calculator — kWh | CalcToWork", "seo_description": "Calculate appliance electricity cost. Free energy and home calculator."},
    "913": {"name": "Transformer Turns Ratio Calculator", "description": "Calculate transformer turns ratio and voltage transformation. Np/Ns = Vp/Vs.", "seo_title": "Transformer Calculator — Turns Ratio | CalcToWork", "seo_description": "Calculate transformer ratio. Free electrical engineering calculator."},
    "914": {"name": "Wheatstone Bridge Calculator", "description": "Calculate unknown resistance using a Wheatstone bridge circuit.", "seo_title": "Wheatstone Bridge Calculator — Rx | CalcToWork", "seo_description": "Calculate bridge resistance. Free electronics calculator."},
    "915": {"name": "Decibel Addition Calculator", "description": "Add sound levels in decibels. Enter dB values for combined sound pressure level.", "seo_title": "Decibel Calculator — dB Addition | CalcToWork", "seo_description": "Add decibel levels. Free acoustics and electronics calculator."},
    "916": {"name": "Sound Level vs Distance Calculator", "description": "Calculate sound pressure level at distance. Inverse square law for acoustics.", "seo_title": "Sound Distance Calculator — dB SPL | CalcToWork", "seo_description": "Calculate sound level at distance. Free acoustics calculator."},
})

# ── conversion (Unit Converters) ──
f.update({
    "1000": {"name": "Length Converter", "description": "Convert between all length units — m, km, cm, mm, ft, in, yd, mi, nautical miles.", "seo_title": "Length Converter — All Units | CalcToWork", "seo_description": "Convert length between meters, feet, inches, miles and all units. Free unit converter."},
    "1001": {"name": "Mass & Weight Converter", "description": "Convert between mass units — kg, g, mg, t, lb, oz, stone. Full weight conversion.", "seo_title": "Weight Converter — kg, lb, oz | CalcToWork", "seo_description": "Convert weight and mass between kg, pounds, ounces, tonnes. Free unit converter."},
    "1002": {"name": "Volume Converter", "description": "Convert between volume units — L, mL, m³, cm³, ft³, gallons, quarts, pints.", "seo_title": "Volume Converter — Liters & Gallons | CalcToWork", "seo_description": "Convert volume between liters, gallons, cubic meters and all units. Free converter."},
    "1003": {"name": "Area Converter", "description": "Convert between area units — m², km², hectares, acres, ft², in².", "seo_title": "Area Converter — m², acres, ft² | CalcToWork", "seo_description": "Convert area between square meters, acres, square feet. Free unit converter."},
    "1004": {"name": "Temperature Converter", "description": "Convert between Celsius, Fahrenheit, Kelvin, and Rankine. Full temperature conversion.", "seo_title": "Temperature Converter — °C, °F, K | CalcToWork", "seo_description": "Convert temperature between Celsius, Fahrenheit and Kelvin. Free unit converter."},
    "1005": {"name": "Pressure Converter", "description": "Convert between pressure units — Pa, kPa, bar, psi, atm, mmHg, Torr.", "seo_title": "Pressure Converter — bar, psi, Pa | CalcToWork", "seo_description": "Convert pressure between bar, psi, Pascal and all units. Free converter."},
    "1006": {"name": "Speed Converter", "description": "Convert between speed units — km/h, mph, m/s, knots, ft/s, mach.", "seo_title": "Speed Converter — km/h, mph, knots | CalcToWork", "seo_description": "Convert speed between km/h, mph, m/s and all units. Free converter."},
    "1007": {"name": "Energy Converter", "description": "Convert between energy units — J, kJ, kcal, Wh, kWh, BTU, eV.", "seo_title": "Energy Converter — Joules, kcal, kWh | CalcToWork", "seo_description": "Convert energy between joules, calories, kilowatt-hours. Free converter."},
    "1008": {"name": "Time Units Converter", "description": "Convert between time units — seconds, minutes, hours, days, weeks, months, years.", "seo_title": "Time Converter — All Units | CalcToWork", "seo_description": "Convert time between seconds, hours, days and all units. Free converter."},
    "1009": {"name": "Digital Storage Converter", "description": "Convert between digital storage units — bytes, KB, MB, GB, TB, PB.", "seo_title": "Data Storage Converter — Bytes to TB | CalcToWork", "seo_description": "Convert digital storage between bytes, megabytes, gigabytes. Free converter."},
})

# ── estadistica (Statistics) ──
f.update({
    "1100": {"name": "Mean (Average) Calculator", "description": "Calculate the arithmetic mean of a set of numbers. Enter comma-separated values.", "seo_title": "Mean Calculator — Average | CalcToWork", "seo_description": "Calculate arithmetic mean and average. Free statistics calculator."},
    "1101": {"name": "Median Calculator", "description": "Calculate the median (middle value) of a dataset. Enter your numbers.", "seo_title": "Median Calculator — Middle Value | CalcToWork", "seo_description": "Calculate the median. Free statistics calculator."},
    "1102": {"name": "Standard Deviation Calculator", "description": "Calculate standard deviation for population or sample. Enter your dataset.", "seo_title": "Standard Deviation Calculator — σ & s | CalcToWork", "seo_description": "Calculate standard deviation. Free statistics calculator."},
    "1103": {"name": "Variance Calculator", "description": "Calculate variance (σ²) for population or sample. Measure of data spread.", "seo_title": "Variance Calculator — σ² & s² | CalcToWork", "seo_description": "Calculate statistical variance. Free statistics calculator."},
    "1104": {"name": "Quartile Calculator", "description": "Calculate quartiles Q1, Q2, Q3 and interquartile range of a dataset.", "seo_title": "Quartile Calculator — Q1, Q2, Q3 | CalcToWork", "seo_description": "Calculate quartiles and IQR. Free statistics calculator."},
    "1105": {"name": "Z-Score Calculator", "description": "Calculate the Z-score (standard score) of a value. z = (x - μ) / σ.", "seo_title": "Z-Score Calculator — Standard Score | CalcToWork", "seo_description": "Calculate Z-score and percentile. Free statistics calculator."},
    "1106": {"name": "Confidence Interval Calculator", "description": "Calculate confidence intervals for means. Enter sample data and confidence level.", "seo_title": "Confidence Interval Calculator — 95% | CalcToWork", "seo_description": "Calculate confidence intervals. Free statistics calculator."},
    "1107": {"name": "Sample Size Calculator", "description": "Calculate required sample size for surveys and experiments. Enter margin of error and confidence.", "seo_title": "Sample Size Calculator — Survey | CalcToWork", "seo_description": "Calculate minimum sample size. Free statistics calculator."},
    "1108": {"name": "Coefficient of Variation Calculator", "description": "Calculate CV = σ/μ × 100%. Compare relative variability between datasets.", "seo_title": "Coefficient of Variation Calculator | CalcToWork", "seo_description": "Calculate CV percentage. Free statistics calculator."},
    "1109": {"name": "Combinations and Permutations", "description": "Calculate combinations (nCr) and permutations (nPr). Free combinatorics tool.", "seo_title": "Combinations Permutations Calculator | CalcToWork", "seo_description": "Calculate nCr and nPr. Free combinatorics and statistics calculator."},
})

# ── clima (Climate & Weather) ──
f.update({
    "1200": {"name": "Temperature Converter", "description": "Convert between all temperature scales — Celsius, Fahrenheit, Kelvin, Rankine.", "seo_title": "Temperature Converter — Full Scales | CalcToWork", "seo_description": "Convert temperature between Celsius, Fahrenheit, Kelvin. Free weather calculator."},
    "1201": {"name": "Relative Humidity Calculator", "description": "Calculate relative humidity from temperature and dew point. Understand air moisture.", "seo_title": "Relative Humidity Calculator — % | CalcToWork", "seo_description": "Calculate relative humidity percentage. Free weather and climate calculator."},
    "1202": {"name": "Dew Point Calculator", "description": "Calculate dew point temperature from air temperature and relative humidity.", "seo_title": "Dew Point Calculator — Temperature | CalcToWork", "seo_description": "Calculate dew point. Free weather and HVAC calculator."},
    "1203": {"name": "Wind Chill Calculator", "description": "Calculate wind chill (feels-like) temperature. Enter air temperature and wind speed.", "seo_title": "Wind Chill Calculator — Feels Like | CalcToWork", "seo_description": "Calculate wind chill temperature. Free weather calculator."},
    "1204": {"name": "Heat Index Calculator", "description": "Calculate heat index (apparent temperature) from temperature and humidity.", "seo_title": "Heat Index Calculator — Apparent Temp | CalcToWork", "seo_description": "Calculate heat index. Free weather and safety calculator."},
    "1205": {"name": "Rainfall Volume Calculator", "description": "Calculate rainwater collection from roof area and rainfall. Estimate water harvesting potential.", "seo_title": "Rainwater Harvesting Calculator | CalcToWork", "seo_description": "Calculate rainfall collection volume. Free sustainability calculator."},
    "1206": {"name": "Sunrise & Sunset Calculator", "description": "Calculate sunrise and sunset times for any location and date.", "seo_title": "Sunrise Sunset Calculator — Times | CalcToWork", "seo_description": "Calculate sunrise and sunset times. Free astronomy and weather calculator."},
    "1207": {"name": "Evapotranspiration Calculator", "description": "Calculate potential evapotranspiration for irrigation planning. Enter climate data.", "seo_title": "Evapotranspiration Calculator — ET | CalcToWork", "seo_description": "Calculate crop water needs. Free agriculture and climate calculator."},
    "1208": {"name": "True Airspeed Calculator", "description": "Calculate true airspeed from indicated airspeed, altitude, and temperature.", "seo_title": "True Airspeed Calculator — TAS | CalcToWork", "seo_description": "Calculate true airspeed. Free aviation calculator."},
    "1209": {"name": "Crosswind Calculator", "description": "Calculate crosswind and headwind components for aviation. Enter wind speed and direction.", "seo_title": "Crosswind Calculator — Aviation | CalcToWork", "seo_description": "Calculate crosswind and headwind. Free aviation weather calculator."},
})

# ── misc remaining ──
f.update({
    "968": {"name": "Angle Converter", "description": "Convert angles between degrees, radians, and gradians.", "seo_title": "Angle Converter | CalcToWork", "seo_description": "Convert angles. Free math calculator."},
    "969": {"name": "Resistor Color Code (4-Band)", "description": "Calculate resistance from 4-band resistor color codes.", "seo_title": "Resistor Color Code 4-Band | CalcToWork", "seo_description": "Decode 4-band resistor values. Free electronics calculator."},
    "972": {"name": "Ideal Gas Law (Combined)", "description": "Calculate combined gas law properties.", "seo_title": "Ideal Gas Law Calculator | CalcToWork", "seo_description": "Calculate gas properties. Free chemistry calculator."},
    "975": {"name": "Molar Mass Calculator", "description": "Calculate molar mass of compounds from chemical formula.", "seo_title": "Molar Mass Calculator | CalcToWork", "seo_description": "Calculate molecular weight. Free chemistry calculator."},
    "984": {"name": "Stefan-Boltzmann Law Calculator", "description": "Calculate thermal radiation using the Stefan-Boltzmann law.", "seo_title": "Stefan-Boltzmann Calculator | CalcToWork", "seo_description": "Calculate radiative heat transfer. Free physics calculator."},
    "985": {"name": "Snell's Law Calculator", "description": "Calculate refraction angles using Snell's law n1sinθ1 = n2sinθ2.", "seo_title": "Snell's Law Calculator — Refraction | CalcToWork", "seo_description": "Calculate light refraction. Free physics and optics calculator."},
    "987": {"name": "Reynolds Number Calculator", "description": "Calculate Reynolds number for fluid flow. Determine laminar vs turbulent flow.", "seo_title": "Reynolds Number Calculator — Fluid Flow | CalcToWork", "seo_description": "Calculate Reynolds number. Free fluid dynamics calculator."},
    "988": {"name": "Bernoulli Equation Calculator", "description": "Calculate fluid flow using Bernoulli's principle. Enter pressure, velocity, and height.", "seo_title": "Bernoulli Equation Calculator | CalcToWork", "seo_description": "Calculate Bernoulli's equation. Free fluid mechanics calculator."},
    "990": {"name": "Spring Constant Calculator", "description": "Calculate spring constant k = F/x using Hooke's law.", "seo_title": "Spring Constant Calculator — Hooke's Law | CalcToWork", "seo_description": "Calculate spring constant. Free physics calculator."},
    "993": {"name": "Capacitor Energy Calculator", "description": "Calculate energy stored in a capacitor E = ½CV².", "seo_title": "Capacitor Energy Calculator | CalcToWork", "seo_description": "Calculate capacitor stored energy. Free electronics calculator."},
    "994": {"name": "Inductor Energy Calculator", "description": "Calculate energy stored in an inductor E = ½LI².", "seo_title": "Inductor Energy Calculator | CalcToWork", "seo_description": "Calculate inductor stored energy. Free electronics calculator."},
    "998": {"name": "Thin Lens Equation Calculator", "description": "Calculate focal length, object distance, or image distance using 1/f = 1/do + 1/di.", "seo_title": "Lens Equation Calculator — Optics | CalcToWork", "seo_description": "Calculate thin lens properties. Free optics and photography calculator."},
    "999": {"name": "Doppler Effect Calculator", "description": "Calculate observed frequency due to the Doppler effect. Enter source and observer speeds.", "seo_title": "Doppler Effect Calculator — Frequency Shift | CalcToWork", "seo_description": "Calculate Doppler frequency shift. Free physics calculator."},
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
