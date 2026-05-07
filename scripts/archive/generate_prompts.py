"""Generate copy-paste Gemini prompts for all template-only calculators."""
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# --- Metadata: (display name, what it calculates, formula) ---
DESCS = {
    "111": ("Arithmetic Sequence Sum", "Sum of all terms in an arithmetic sequence", "S = n/2 x (2*a1 + (n-1)*d)"),
    "112": ("Geometric Sequence Sum", "Sum of all terms in a geometric sequence", "S = a1 x (1 - r^n) / (1 - r)"),
    "113": ("Complex Number Magnitude", "Modulus (length) of a complex number a+bi", "|z| = sqrt(a^2 + b^2)"),
    "114": ("2x2 Matrix Determinant", "Determinant of a 2x2 matrix [[a,b],[c,d]]", "det = a*d - b*c"),
    "115": ("3D Vector Magnitude", "Length of a 3-dimensional vector (x, y, z)", "|v| = sqrt(x^2 + y^2 + z^2)"),
    "116": ("Dot Product (3D)", "Scalar dot product of two 3D vectors", "A.B = ax*bx + ay*by + az*bz"),
    "117": ("Cross Product (3D)", "Vector cross product of two 3D vectors", "AxB = (ay*bz-az*by, az*bx-ax*bz, ax*by-ay*bx)"),
    "118": ("Polynomial Derivative", "Derivative of a single polynomial term ax^n", "d/dx[ax^n] = n*a*x^(n-1)"),
    "119": ("Trapezoidal Rule Integration", "Numerical integral of f(x) over [a,b] using one trapezoid", "Integral approx = (b-a)/2 * (f(a) + f(b))"),
    "120": ("Projectile Motion", "Range, max height and flight time of a projectile", "R = v0^2*sin(2*theta)/g ; H = v0^2*sin^2(theta)/(2g)"),
    "121": ("Centripetal Force", "Force required to keep an object in circular motion", "F = m*v^2/r"),
    "122": ("Gravitational Force", "Attractive force between two masses", "F = G*m1*m2/r^2"),
    "123": ("Elastic Potential Energy", "Energy stored in a compressed or stretched spring", "E = 0.5*k*x^2"),
    "124": ("Specific Heat / Heat Energy", "Thermal energy absorbed or released by a substance", "Q = m*c*delta_T"),
    "125": ("Wave Speed", "Speed of a wave from its frequency and wavelength", "v = f * lambda"),
    "126": ("Thin Lens Equation", "Image distance formed by a thin lens", "1/f = 1/do + 1/di"),
    "127": ("Torque", "Rotational force (moment) about a pivot point", "tau = F * r * sin(theta)"),
    "128": ("Angular Momentum", "Rotational momentum of a spinning object", "L = I * omega"),
    "129": ("Fluid Pressure at Depth", "Pressure exerted by a fluid column at a given depth", "P = rho * g * h"),
    "130": ("Common Logarithm (log10)", "Base-10 logarithm of a number", "log10(x) = log(x)"),
    "131": ("Natural Logarithm (ln)", "Base-e logarithm of a number", "ln(x) = loge(x)"),
    "132": ("Exponential Growth & Decay", "Final value after exponential growth or decay over time", "y = a * e^(r*t)"),
    "133": ("Factorial", "Product of all positive integers up to n", "n! = n * (n-1) * ... * 2 * 1"),
    "134": ("Permutations P(n,r)", "Number of ordered arrangements of r items from n", "P(n,r) = n! / (n-r)!"),
    "135": ("Combinations C(n,r)", "Number of unordered selections of r items from n", "C(n,r) = n! / (r! * (n-r)!)"),
    "136": ("Standard Deviation", "Spread of values in a data set around the mean", "sigma = sqrt(sum((xi-mu)^2)/N)"),
    "137": ("Variance", "Average squared deviation of values from the mean", "sigma^2 = sum((xi-mu)^2)/N"),
    "138": ("Median", "Middle value of a sorted data set", "Median = middle value (or avg of two middle values)"),
    "139": ("Quartiles & IQR", "Q1, Q2, Q3 and interquartile range of a data set", "IQR = Q3 - Q1"),
    "140": ("Bernoulli Equation (Fluid)", "Pressure-velocity relationship along a streamline", "P + 0.5*rho*v^2 + rho*g*h = constant"),
    "141": ("Doppler Effect", "Observed frequency shift due to relative motion between source and observer", "f_obs = f_src * (v + v_obs)/(v + v_src)"),
    "142": ("Snell's Law (Refraction)", "Angle of refraction when light passes between two media", "n1*sin(theta1) = n2*sin(theta2)"),
    "143": ("Coulomb's Law", "Electrostatic force between two point charges", "F = k*q1*q2/r^2"),
    "144": ("Magnetic Force on a Charge", "Force on a charged particle moving in a magnetic field", "F = q*v*B*sin(theta)"),
    "145": ("Thermal Linear Expansion", "Length change of a material due to a temperature change", "delta_L = alpha * L0 * delta_T"),
    "146": ("Stefan-Boltzmann Radiation", "Thermal radiation power emitted by a surface", "P = epsilon * sigma * A * T^4"),
    "147": ("RL Circuit Time Constant", "Current rise time constant in a series RL circuit", "tau = L / R"),
    "148": ("RC Circuit Time Constant", "Charge and voltage buildup time constant in an RC circuit", "tau = R * C"),
    "149": ("Ideal Gas Law", "Relates pressure, volume, temperature and moles of a gas", "PV = nRT"),
    "320": ("CAGR (Compound Annual Growth Rate)", "Annualized growth rate of an investment over multiple years", "CAGR = (End/Start)^(1/years) - 1"),
    "321": ("Effective Annual Rate (EAR)", "True annual interest rate accounting for intra-year compounding", "EAR = (1 + r/n)^n - 1"),
    "322": ("Loan Amortization Schedule", "Monthly payment and total interest for a fully amortizing loan", "M = P*r*(1+r)^n / ((1+r)^n - 1)"),
    "323": ("Rental Yield Calculator", "Gross and net rental yield of an investment property", "Yield = (Annual rent / Property value) * 100"),
    "324": ("Capitalization Rate (Cap Rate)", "Property value estimate from net operating income", "Cap rate = NOI / Property value"),
    "325": ("Dividend Yield", "Annual dividend income as a percentage of the share price", "Yield = Annual dividend per share / Share price * 100"),
    "326": ("P/E Ratio", "Price-to-earnings ratio used to value a stock", "P/E = Share price / Earnings per share"),
    "327": ("Future Value of Annuity", "Future value of a series of equal periodic payments", "FV = PMT * ((1+r)^n - 1) / r"),
    "328": ("Present Value of Annuity", "Present value of a series of equal future payments", "PV = PMT * (1 - (1+r)^(-n)) / r"),
    "329": ("WACC", "Weighted average cost of capital for a company", "WACC = (E/V)*Re + (D/V)*Rd*(1-Tc)"),
    "330": ("Payback Period", "Time to recover an initial investment from annual cash flows", "Payback = Initial investment / Annual cash flow"),
    "331": ("Sharpe Ratio", "Risk-adjusted return of an investment portfolio", "Sharpe = (Rp - Rf) / sigma_p"),
    "332": ("Tax-Equivalent Yield", "Pre-tax yield needed to match a tax-exempt bond yield", "TEY = Tax-exempt yield / (1 - marginal tax rate)"),
    "333": ("Real Rate of Return", "Investment return after adjusting for inflation", "Real return approx Nominal return - Inflation rate"),
    "334": ("Affordable Loan Amount", "Maximum loan amount given a monthly payment budget", "P = PMT * (1 - (1+r)^(-n)) / r"),
    "335": ("Mortgage Payoff Time", "Extra monthly payment needed to pay off a mortgage early", "Uses standard amortization with extra principal"),
    "336": ("Credit Card Payoff", "Months to pay off a credit card balance with a fixed monthly payment", "n = -log(1 - r*P/PMT) / log(1+r)"),
    "337": ("College Savings Calculator", "Monthly savings required to reach a college fund target", "Uses FV of annuity solved for PMT"),
    "338": ("Life Insurance Need", "Recommended life insurance coverage for your family", "Need = annual income * years + outstanding debts"),
    "339": ("Monthly CAGR", "Month-over-month compound growth rate from start and end values", "Monthly CAGR = (End/Start)^(1/months) - 1"),
    "415": ("Lean Body Mass", "Fat-free body mass using the Boer formula", "LBM = 0.407*W + 0.267*H - 19.2 (men); 0.252*W + 0.473*H - 48.3 (women)"),
    "416": ("Body Adiposity Index (BAI)", "Body fat percentage estimate from hip circumference and height", "BAI = (Hip cm / Height m^1.5) - 18"),
    "417": ("Daily Protein Intake", "Recommended daily protein based on weight and activity level", "Protein g/day = weight kg * 0.8 to 2.2 g/kg"),
    "418": ("Daily Fiber Intake", "Recommended dietary fiber intake based on daily calorie needs", "Fiber g = 14 g per 1,000 kcal consumed"),
    "419": ("Karvonen Heart Rate", "Target heart rate using the heart rate reserve (Karvonen) method", "THR = RHR + intensity% * (HRmax - RHR)"),
    "420": ("Heart Rate Training Zones", "5 exercise intensity zones from resting and maximum heart rate", "Zone 1: 50-60% HRmax through Zone 5: 90-100% HRmax"),
    "421": ("Creatinine Clearance (CrCl)", "Estimated kidney filtration rate using Cockcroft-Gault formula", "CrCl = ((140-age)*weight) / (72*serum Cr) [x0.85 for women]"),
    "422": ("BMI Prime", "How far a person's BMI is from the upper limit of normal (25)", "BMI Prime = BMI / 25"),
    "423": ("Due Date Calculator", "Estimated delivery date from last menstrual period or conception date", "EDD = LMP + 280 days (Naegele rule)"),
    "424": ("Ovulation Calculator", "Estimated ovulation window and fertile days from cycle length", "Ovulation approx = Day 1 + (cycle length - 14) days"),
    "425": ("Body Fat % (US Navy Method)", "Body fat percentage using US Navy circumference measurements", "Men: %BF = 86.01*log(abdomen-neck) - 70.04*log(height) + 36.76"),
    "426": ("TDEE – Total Daily Energy Expenditure", "Total daily calories burned including physical activity", "TDEE = BMR * activity multiplier (1.2 to 1.9)"),
    "427": ("BMR – Mifflin-St Jeor", "Basal metabolic rate using the Mifflin-St Jeor equation", "BMR = 10*W + 6.25*H - 5*age + 5 (men); -161 (women)"),
    "428": ("Resting Metabolic Rate (RMR)", "Calories burned at complete rest, using lean body mass", "RMR = 370 + 21.6 * lean mass kg"),
    "429": ("MET Calorie Calculator", "Calories burned during an activity from its MET value", "Calories = MET * weight kg * duration hours"),
    "430": ("Target Weight Calculator", "Goal body weight corresponding to a target BMI", "Target weight kg = BMI * height m^2"),
    "431": ("Pregnancy Weight Gain", "Recommended total gestational weight gain by pre-pregnancy BMI", "IOM 2009: underweight 12.5-18kg; normal 11.5-16kg; overweight 7-11.5kg; obese 5-9kg"),
    "432": ("Calories Burned Walking", "Energy expenditure from walking at different speeds", "Calories = MET * weight kg * hours (MET 2.5-5 depending on speed)"),
    "433": ("Child Growth Percentile", "Height and weight percentile vs WHO/CDC growth reference charts", "Uses WHO/CDC lookup tables for age and sex"),
    "434": ("Daily Water Intake by Weight", "Recommended daily water intake based on body weight", "Water L = weight kg * 0.033"),
    "503": ("Fuel Cost Calculator", "Total trip fuel cost from distance, fuel efficiency and price per litre", "Cost = (Distance / Fuel economy) * Fuel price"),
    "504": ("Data Transfer Time", "Time to transfer a file at a given internet connection speed", "Time = File size bits / Speed bps"),
    "505": ("Battery Life Calculator", "How long a battery lasts given its capacity and the device's current draw", "Life hours = Capacity mAh / Current draw mA"),
    "506": ("Download Time Calculator", "Estimated download time for a file at a given speed", "Time = File size MB * 8 / Speed Mbps"),
    "507": ("PPI / Screen Pixel Density", "Pixels per inch of a display from resolution and diagonal size", "PPI = sqrt(w^2 + h^2) / diagonal inches"),
    "508": ("Aspect Ratio Calculator", "Scaled screen or image dimensions maintaining the original ratio", "New width = new height * (original width / original height)"),
    "509": ("Password Entropy", "Strength of a password in bits of entropy", "Entropy bits = length * log2(character_set_size)"),
    "510": ("Bandwidth Calculator", "Network bandwidth required to transfer data within a time limit", "Bandwidth = Data size / Transfer time"),
    "511": ("File Size Estimator", "Estimated uncompressed file size from image resolution and bit depth", "Size bytes = width * height * bit_depth / 8"),
    "512": ("Electricity Cost Calculator", "Monthly electricity cost of running a household appliance", "Cost = (Watts * hours/day * days/month) / 1000 * price per kWh"),
    "513": ("Screen Resolution Calculator", "Total pixel count and megapixels from display resolution", "Total pixels = width * height"),
    "514": ("Video File Size Calculator", "Estimated video file size from resolution, frame rate and duration", "Size = bitrate Mbps * duration seconds / 8 MB"),
    "515": ("RAID Storage Capacity", "Usable storage from a RAID array given disk count and size", "RAID 0: all; RAID 1: half; RAID 5: (n-1) drives; RAID 6: (n-2) drives"),
    "516": ("Uptime & SLA Calculator", "Maximum allowable downtime per year/month for a given uptime SLA", "Downtime = (1 - uptime%) * period"),
    "517": ("Ping / Network Latency", "Estimated round-trip ping from distance and signal propagation speed", "RTT = 2 * distance / speed (approx 200,000 km/s in fibre)"),
    "518": ("Words Per Minute (WPM)", "Typing or reading speed in words per minute from word count and time", "WPM = total words / minutes taken"),
    "519": ("Reading Time Calculator", "Estimated time to read an article from its word count", "Time minutes = word count / 200 (average adult reading speed)"),
    "520": ("SMS Cost Calculator", "Total cost of sending a batch of text messages", "Total cost = number of messages * rate per SMS"),
    "521": ("Mobile Data Usage Estimator", "Estimated monthly mobile data from daily app and streaming habits", "Total = sum of (sessions per day * MB per session * 30 days)"),
    "522": ("Screen Brightness (Nits) Guide", "Minimum display brightness recommended for different lighting conditions", "Approx: indoor 100-300 nits; outdoor sun 500-1000+ nits"),
    "910": ("Fraction Calculator", "Add, subtract, multiply or divide two fractions with full simplification", "a/b + c/d = (a*d + b*c) / (b*d); simplify by GCF"),
    "911": ("Slope Calculator", "Slope (gradient), angle and line equation from two coordinate points", "m = (y2-y1) / (x2-x1); y = mx + b"),
    "912": ("Scientific Notation Converter", "Convert any number to and from standard scientific notation", "a x 10^n where 1 <= a < 10"),
    "913": ("Rounding Calculator", "Round a number to a specified number of decimal places or significant figures", "Standard half-up rounding or banker's rounding"),
    "914": ("GCF & LCM Calculator", "Greatest common factor and least common multiple of two integers", "GCF via Euclidean algorithm; LCM = a*b / GCF(a,b)"),
    "915": ("Prime Factorization", "Express any positive integer as a product of prime factors", "Trial division: test primes up to sqrt(n)"),
    "916": ("Circle Calculator", "Area, circumference, diameter or radius of a circle from any one value", "A = pi*r^2; C = 2*pi*r; d = 2r"),
    "917": ("Right Triangle Calculator", "Missing side or angle of a right triangle from any two known values", "a^2 + b^2 = c^2; sin/cos/tan functions"),
    "918": ("Triangle Area – Heron's Formula", "Area of any triangle given all three side lengths (no angle needed)", "s = (a+b+c)/2; A = sqrt(s*(s-a)*(s-b)*(s-c))"),
    "919": ("Rectangle Calculator", "Area, perimeter and diagonal of a rectangle from length and width", "A = l*w; P = 2*(l+w); d = sqrt(l^2+w^2)"),
    "920": ("Square Calculator", "Area, perimeter and diagonal of a square from side length", "A = s^2; P = 4*s; d = s*sqrt(2)"),
    "921": ("Trapezoid Area Calculator", "Area of a trapezoid from its two parallel bases and height", "A = 0.5 * (a+b) * h"),
    "922": ("Cylinder Volume & Surface Area", "Volume and total surface area of a right circular cylinder", "V = pi*r^2*h; SA = 2*pi*r*(r+h)"),
    "923": ("Cone Volume & Surface Area", "Volume and lateral/total surface area of a right circular cone", "V = (1/3)*pi*r^2*h; SA = pi*r*(r + slant height)"),
    "924": ("Rectangular Pyramid Volume", "Volume of a pyramid with a rectangular base", "V = (1/3) * l * w * h"),
    "925": ("Sphere Calculator", "Volume and surface area of a sphere from its radius", "V = (4/3)*pi*r^3; SA = 4*pi*r^2"),
    "926": ("BMR – Harris-Benedict", "Basal metabolic rate using the original Harris-Benedict (1919) equations", "Men: BMR = 88.36 + 13.4*W + 4.8*H - 5.7*age"),
    "927": ("BMR – Katch-McArdle", "BMR based solely on lean body mass (most accurate if body fat is known)", "BMR = 370 + 21.6 * LBM kg"),
    "928": ("Macronutrient Calculator", "Daily grams of protein, fat and carbohydrates from TDEE and goal", "Protein 4 cal/g, fat 9 cal/g, carbs 4 cal/g"),
    "929": ("Blood Pressure Interpreter", "Categorise a blood pressure reading per AHA guidelines", "Normal <120/80; Elevated 120-129/<80; Stage 1 HBP 130-139/80-89; Stage 2 HBP >=140/>=90"),
    "930": ("Waist-to-Hip Ratio (WHR)", "Abdominal obesity risk from waist and hip circumference", "WHR = waist / hip; at-risk: >0.90 men, >0.85 women"),
    "931": ("Waist-to-Height Ratio", "Cardiometabolic health risk indicator from waist and height", "WHtR = waist / height; healthy threshold < 0.5"),
    "932": ("Weight Loss Percentage", "Percentage of initial body weight lost", "% lost = (initial - current) / initial * 100"),
    "933": ("Heart Rate Training Zones", "5 heart rate training zones based on maximum heart rate", "Zone boundaries at 50, 60, 70, 80, 90% of HRmax"),
    "934": ("Salary to Hourly Rate", "Equivalent hourly wage from an annual salary", "Hourly = Annual / (weeks per year * hours per week)"),
    "935": ("Hourly Rate to Annual Salary", "Annual salary from an hourly pay rate", "Annual = hourly * hours/week * 52 weeks"),
    "936": ("Mortgage Payment Calculator", "Monthly payment, total interest paid and amortization for a home loan", "M = P*r*(1+r)^n / ((1+r)^n - 1)"),
    "937": ("Debt Payoff Calculator", "Number of months to pay off a debt with a fixed monthly payment", "n = -log(1 - r*P/PMT) / log(1+r)"),
    "938": ("Savings Goal Calculator", "Monthly contribution needed to reach a savings target by a deadline", "PMT = FV * r / ((1+r)^n - 1)"),
    "939": ("Profit Margin Calculator", "Gross, operating or net profit margin from revenue and costs", "Margin % = (Revenue - Cost) / Revenue * 100"),
    "940": ("NPV (Net Present Value)", "Present value of future cash flows minus the initial investment", "NPV = sum of CF_t/(1+r)^t - Initial investment"),
    "941": ("Emergency Fund Calculator", "Recommended size of an emergency fund based on monthly expenses", "Fund = monthly essential expenses * 3 to 6 months"),
    "942": ("Age Calculator (Detailed)", "Exact age in years, months and days with next birthday countdown", "Age = today - birth date"),
    "943": ("Date Difference Calculator", "Exact days, weeks and months between any two calendar dates", "Delta = end date - start date"),
    "944": ("Tip Calculator (Advanced)", "Tip amount per person when splitting a restaurant bill", "Tip = bill * tip%; Per person = (bill + tip) / people"),
    "945": ("Double Discount Calculator", "Final price after two successive percentage discounts applied", "Final = Price * (1 - d1) * (1 - d2)"),
    "946": ("Kinetic Energy Calculator", "Kinetic energy of a moving object from its mass and velocity", "KE = 0.5 * m * v^2"),
    "947": ("Gravitational Potential Energy", "Potential energy of an object at height above a reference point", "PE = m * g * h"),
    "948": ("Work and Power Calculator", "Mechanical work done and power output from force, distance and time", "W = F * d; P = W / t"),
    "949": ("Ohm's Law + Power Calculator", "Find any of voltage, current, resistance or power given two values", "V = I*R; P = V*I; P = I^2*R; P = V^2/R"),
    "950": ("Newton's Second Law Calculator", "Find force, mass or acceleration from any two of the three", "F = m * a"),
    "951": ("One Rep Max (1RM)", "Maximum single-rep lifting weight estimated from a submaximal set", "Epley: 1RM = weight * (1 + reps/30)"),
    "952": ("Running Race Time Predictor", "Predicted race finish time from a recent training or race result", "Riegel: T2 = T1 * (D2/D1)^1.06"),
    "953": ("VO2 Max Estimator", "Aerobic capacity estimate from resting and maximum heart rates", "VO2max approx 15 * HRmax/HRrest (Fox method)"),
    "954": ("Angle Unit Converter", "Convert between degrees, radians, gradians and turns", "rad = deg * pi/180; grad = deg * 10/9"),
    "955": ("Temperature Converter (Full)", "Convert between Celsius, Fahrenheit, Kelvin and Rankine", "F = C*9/5 + 32; K = C + 273.15"),
    "956": ("Energy Unit Converter", "Convert between joules, calories, kilocalories, kWh, BTU and eV", "1 kcal = 4184 J; 1 kWh = 3,600,000 J"),
    "957": ("Combinations & Permutations", "Calculate both C(n,r) and P(n,r) from a single set of inputs", "P(n,r) = n!/(n-r)!; C(n,r) = n!/(r!*(n-r)!)"),
    "958": ("Z-Score to Percentile", "Percentile rank in the normal distribution from a z-score", "Phi(z) = cumulative standard normal CDF"),
    "959": ("Sample Size Calculator", "Required survey sample size for a confidence level and margin of error", "n = Z^2 * p*(1-p) / e^2"),
    "960": ("BSA & Ideal Body Weight", "Body surface area (Mosteller) and ideal body weight (Devine formula)", "BSA = sqrt(H*W/3600); IBW men = 50 + 2.3*(height inches - 60)"),
    "961": ("A1C to Estimated Average Glucose", "Convert HbA1c percentage to estimated average blood glucose", "eAG mg/dL = 28.7 * A1C - 46.7"),
    "962": ("LDL Cholesterol (Friedewald)", "Estimated LDL cholesterol from a standard lipid panel", "LDL = Total cholesterol - HDL - Triglycerides/5"),
    "1000": ("pH Calculator", "pH of a solution from its hydrogen ion concentration", "pH = -log10[H+]"),
    "1001": ("pOH Calculator", "pOH from hydroxide ion concentration and its relationship to pH", "pOH = -log10[OH-]; pH + pOH = 14"),
    "1002": ("Molarity Calculator", "Molar concentration of a solute in a solution", "M = moles of solute / volume of solution in litres"),
    "1003": ("Dilution Calculator", "Volume of stock solution needed to prepare a diluted solution", "C1*V1 = C2*V2"),
    "1004": ("Ideal Gas Law Calculator", "Find P, V, n or T for an ideal gas given the other three", "PV = nRT"),
    "1005": ("Boyle's Law Calculator", "Pressure-volume relationship at constant temperature", "P1*V1 = P2*V2"),
    "1006": ("Charles's Law Calculator", "Volume-temperature relationship at constant pressure", "V1/T1 = V2/T2"),
    "1007": ("Gibbs Free Energy", "Spontaneity of a chemical reaction from enthalpy, entropy and temperature", "delta_G = delta_H - T * delta_S"),
    "1008": ("Molecular Weight Calculator", "Molecular weight of a compound from its chemical formula", "MW = sum of (atomic mass * count) for each element"),
    "1009": ("Titration Calculator", "Unknown concentration from titration volume and known concentration", "C1*V1 = C2*V2 for 1:1 stoichiometry"),
    "1010": ("Voltage Divider Calculator", "Output voltage of a two-resistor voltage divider", "Vout = Vin * R2 / (R1 + R2)"),
    "1011": ("LED Resistor Calculator", "Series resistor value for an LED in a DC circuit", "R = (Supply voltage - LED forward voltage) / LED current"),
    "1012": ("Parallel Resistance Calculator", "Total resistance of resistors connected in parallel", "1/Rt = 1/R1 + 1/R2 + ..."),
    "1013": ("Capacitor Energy Calculator", "Energy stored in a charged capacitor", "E = 0.5 * C * V^2"),
    "1014": ("Inductor Energy Calculator", "Energy stored in an inductor carrying current", "E = 0.5 * L * I^2"),
    "1015": ("Transformer Ratio Calculator", "Secondary voltage and current from transformer turns ratio", "V1/V2 = N1/N2; I1/I2 = N2/N1"),
    "1016": ("RC Circuit Time Constant", "Charge and voltage time constant for an RC circuit", "tau = R * C"),
    "1017": ("Wheatstone Bridge Calculator", "Unknown resistance in a balanced Wheatstone bridge", "Rx = R2 * R3 / R1"),
    "1018": ("Capacitors in Series", "Total capacitance of capacitors connected in series", "1/Ct = 1/C1 + 1/C2 + ..."),
    "1019": ("Resistor Color Code Calculator", "Resistance value and tolerance from 4-band color code", "Value = (band1*10 + band2) * 10^band3; tolerance = band4"),
    "1020": ("Dew Point Calculator", "Dew point temperature from air temperature and relative humidity", "Td approx T - (100 - RH)/5 (Magnus approximation)"),
    "1021": ("Heat Index Calculator", "Apparent (feels-like) temperature from air temperature and humidity", "Steadman/Rothfusz regression equation"),
    "1022": ("Wind Chill Calculator", "Apparent temperature from air temperature and wind speed", "WC = 13.12 + 0.6215*T - 11.37*v^0.16 + 0.3965*T*v^0.16"),
    "1023": ("Relative Humidity Calculator", "Relative humidity from dry-bulb and wet-bulb temperatures", "Uses psychrometric approximation"),
    "1024": ("Air Quality Index (AQI)", "AQI category and health advice from PM2.5 concentration", "EPA breakpoint linear interpolation formula"),
    "1025": ("Sunrise & Sunset Calculator", "Approximate sunrise and sunset times from latitude, longitude and date", "NOAA simplified solar position algorithm"),
    "1026": ("UV Index & Safe Exposure Time", "Maximum safe sun exposure before sunburn risk at a given UV index", "Time to burn = skin type factor / UV index"),
    "1027": ("Altitude & Atmospheric Pressure", "Atmospheric pressure at a given altitude above sea level", "P = 101325 * (1 - 2.25577e-5 * h)^5.25588 Pa"),
    "1028": ("Rainfall Volume Calculator", "Total rainwater collected from a surface for a given rainfall", "Volume = catchment area * rainfall depth"),
    "1029": ("Evapotranspiration (ET0)", "Reference crop evapotranspiration using simplified Penman-Monteith", "ET0 depends on temperature, humidity, wind speed and solar radiation"),
    "1030": ("Day of Year Calculator", "Julian day number (1-365 or 366) from a Gregorian calendar date", "Count days from January 1"),
    "1031": ("ISO Week Number Calculator", "ISO 8601 week number (1-53) for any given calendar date", "ISO 8601 standard: week containing first Thursday of year is week 1"),
    "1032": ("Age in Days Calculator", "Exact number of days lived from birth date to a target date", "Days = target date - birth date"),
    "1033": ("Reading Time Estimator", "Estimated reading time from word count at average reading speed", "Time = words / 200 words per minute"),
    "1034": ("Password Generator", "Generate a random password with chosen length and character types", "Cryptographically random selection from allowed character set"),
    "1035": ("Random Number Generator", "Generate random integers or decimals within a custom range", "Uniform distribution between min and max"),
    "1036": ("Dice Roller", "Simulate rolling one or more dice with any number of sides", "Sum of N dice, each uniformly random 1 to S"),
    "1037": ("Coin Flip Simulator", "Flip a coin multiple times and count heads vs tails", "Bernoulli trial with p = 0.5"),
    "1038": ("Hex to RGB Color Converter", "Convert hex color codes (#RRGGBB) to RGB values and back", "R = hex(RR); G = hex(GG); B = hex(BB)"),
    "1039": ("Exposure Value (EV) Calculator", "Camera EV from aperture, shutter speed and ISO sensitivity", "EV = log2(N^2/t) adjusted for ISO"),
    "1040": ("Depth of Field Calculator", "Near and far focus limits and total depth of field for a lens", "DOF = 2*u^2*N*c / f^2"),
    "1041": ("Hyperfocal Distance Calculator", "Focus distance that maximises depth of field for a given aperture", "H = f^2 / (N * c)"),
    "1042": ("Sound Level Addition (dB)", "Combined noise level from two independent sound sources in decibels", "L_total = 10 * log10(10^(L1/10) + 10^(L2/10))"),
    "1043": ("Sound Level vs Distance", "Sound pressure level at a new distance from a point source", "L2 = L1 - 20 * log10(d2/d1)"),
    "1044": ("Display Contrast Ratio", "Contrast ratio of a display from white and black luminance", "CR = L_white / L_black"),
    "1045": ("Crosswind Component Calculator", "Effective crosswind component for aircraft runway operations", "Crosswind = wind speed * sin(angle between wind and runway)"),
    "1046": ("Fuel Consumption Calculator", "Vehicle fuel consumption in L/100km or mpg and cost per trip", "L/100km = (fuel used litres / distance km) * 100"),
    "1047": ("True Airspeed (TAS) Calculator", "True airspeed from indicated airspeed, altitude and temperature", "TAS approx IAS * (1 + altitude ft / 1000 * 0.02)"),
    "1048": ("Hull Speed Calculator", "Theoretical maximum displacement hull speed of a boat", "Hull speed knots = 1.34 * sqrt(waterline length feet)"),
    "1049": ("Great-Circle Distance (Haversine)", "Shortest distance between two GPS coordinates on Earth", "Haversine formula using lat/lon"),
    "1050": ("Regular Polygon Area", "Area of a regular polygon from number of sides and side length", "A = (n * s^2) / (4 * tan(pi/n))"),
    "1051": ("Cone Volume (Alternate)", "Volume of a right circular cone", "V = (1/3) * pi * r^2 * h"),
    "1052": ("Arithmetic Series Sum", "Sum of an arithmetic series from first term, last term and count", "S = n * (first + last) / 2"),
    "1053": ("Geometric Series Sum", "Sum of a finite geometric series", "S = a * (1 - r^n) / (1 - r)"),
    "1054": ("Combinations Calculator", "Number of ways to choose r items from n without regard to order", "C(n,r) = n! / (r! * (n-r)!)"),
    "1055": ("Buoyancy (Archimedes)", "Buoyant force acting on an object submerged in a fluid", "F_b = rho_fluid * g * V_displaced"),
    "1056": ("Doppler Effect (Sound)", "Observed frequency when source or observer is moving", "f_obs = f_src * (v + v_obs) / (v - v_src)"),
    "1057": ("AC Circuit Impedance", "Total impedance of a series RLC AC circuit", "Z = sqrt(R^2 + (X_L - X_C)^2)"),
    "1058": ("Moment of Inertia", "Rotational inertia of common geometric shapes", "Solid cylinder: I = 0.5*m*r^2; Thin rod: I = m*L^2/12"),
    "1059": ("Rotational Kinetic Energy", "Kinetic energy of a rotating rigid body", "KE_rot = 0.5 * I * omega^2"),
    "1060": ("Body Fat % – Navy Method", "Body fat percentage using US Navy tape-measure formula", "Same as ID 425 – circumference-based formula"),
    "1061": ("BMR – Mifflin-St Jeor (Alt)", "Basal metabolic rate via Mifflin-St Jeor equation", "Same as ID 427"),
    "1062": ("Daily Water Intake", "Daily hydration target based on body weight", "Water L = weight kg * 0.033"),
    "1063": ("One Rep Max – Brzycki", "One-rep max via Brzycki formula from a submaximal set", "1RM = weight / (1.0278 - 0.0278 * reps)"),
    "1064": ("Daily Protein Requirement", "Daily protein intake recommendation by weight and activity", "Protein g = weight kg * 0.8 to 2.2 g/kg"),
    "1065": ("Dividend Yield (Alt)", "Annual dividend yield as percentage of share price", "Yield = Annual dividend / Share price * 100"),
    "1066": ("Payback Period (Alt)", "Investment payback period from annual cash flows", "Payback = Initial cost / Annual cash flow"),
    "1067": ("Capital Gains Tax Estimator", "Estimated tax owed on investment capital gain", "Tax = gain * applicable capital gains tax rate"),
    "1068": ("Currency Exchange with Fee", "Amount received after applying exchange rate and commission", "Received = amount * exchange rate * (1 - fee%)"),
    "1069": ("Break-Even Point (Alt)", "Units to sell to cover fixed and variable costs", "Units = Fixed costs / (Selling price - Variable cost per unit)"),
    "1070": ("Molar Mass Calculator", "Molar mass of a compound from element symbols and counts", "MW = sum of atomic mass * quantity for each element"),
    "1071": ("pH from H+ Concentration", "pH from hydrogen ion concentration", "pH = -log10[H+]"),
    "1072": ("Ideal Gas Law (Alt)", "Pressure-volume-temperature for ideal gas", "PV = nRT"),
    "1073": ("Molarity (Alt)", "Concentration of a solution in mol/L", "M = n / V"),
    "1074": ("Dilution Formula (Alt)", "Stock solution volume for a target dilution", "C1*V1 = C2*V2"),
    "1075": ("Resistor Color Code (Alt)", "4-band resistor reading", "Value = (10*b1 + b2) * 10^b3"),
    "1076": ("Capacitor Energy (Alt)", "Energy stored in a capacitor", "E = 0.5 * C * V^2"),
    "1077": ("Voltage Divider (Alt)", "Output voltage of voltage divider", "Vout = Vin * R2/(R1+R2)"),
    "1078": ("RC Time Constant (Alt)", "Time constant of RC circuit", "tau = R * C"),
    "1079": ("Wheatstone Bridge (Alt)", "Unknown resistor in Wheatstone bridge", "Rx = R2*R3/R1"),
    "1080": ("Fuel Economy (Alt)", "L/100km or MPG fuel economy", "L/100km = litres / km * 100"),
    "1081": ("Braking Distance Calculator", "Vehicle stopping distance from initial speed and road friction", "d = v^2 / (2 * mu * g)"),
    "1082": ("Engine Displacement Calculator", "Total engine cylinder displacement volume", "V = pi/4 * bore^2 * stroke * number of cylinders"),
    "1083": ("Tire Pressure Converter", "Convert tire pressure between PSI, bar and kPa", "1 bar = 14.5038 PSI = 100 kPa"),
    "1084": ("Flight Time with Wind", "Adjusted flight time with headwind or tailwind component", "Time = distance / (airspeed +/- wind speed)"),
    "1085": ("Depth of Field (Alt)", "Camera depth of field from aperture, focal length and focus distance", "DOF = 2*u^2*N*c/f^2"),
    "1086": ("Flash Guide Number Calculator", "Camera flash guide number and required power for correct exposure", "GN = subject distance * f-number"),
    "1087": ("Heat Index (Alt)", "Apparent temperature from heat and humidity", "Rothfusz equation"),
    "1088": ("Wind Chill (Alt)", "Feels-like temperature in cold and windy conditions", "WC = 13.12 + 0.6215*T - 11.37*v^0.16 + 0.3965*T*v^0.16"),
    "1089": ("Dew Point (Alt)", "Dew point from temperature and relative humidity", "Td approx T - (100-RH)/5"),
    "1090": ("Password Entropy (Alt)", "Entropy bits of a password", "H = L * log2(N)"),
    "1091": ("Character & Word Counter", "Count characters, words, sentences and paragraphs in a text", "Direct string processing"),
    "1092": ("Business Days Calculator", "Number of working days between two dates, excluding weekends", "Count Monday-Friday between dates"),
    "1093": ("Beam Deflection Calculator", "Maximum deflection of a simply-supported beam under uniform load", "delta = 5*w*L^4 / (384*E*I)"),
    "1094": ("Bolt Torque Calculator", "Recommended tightening torque for a bolt from clamp force and friction", "T = K * d * F"),
    "1095": ("Spring Constant (Hooke's Law)", "Spring constant or required force from extension and load", "F = k * x; k = F / x"),
    "1096": ("Reynolds Number Calculator", "Flow regime (laminar vs turbulent) in a pipe or channel", "Re = rho * v * D / mu"),
    "1097": ("Running Pace Calculator", "Running pace per km/mile and predicted finish time for any distance", "Pace = time / distance"),
    "1098": ("Golf Handicap Calculator", "Golf handicap index from a set of recent score differentials", "Handicap = 0.96 * average of best 8 of last 20 differentials"),
    "1099": ("Calories Burned by Activity (MET)", "Calories burned during physical activity from MET value", "Calories = MET * weight kg * duration hours"),
}

PROMPT_TEMPLATE = """Write a high-quality 1000-word calculator article for a multilingual calculator site.

Calculator: {name} (ID: {cid})
What it calculates: {desc}
Formula: {formula}

Write TWO versions:
1. Spanish ("es") — article in Spanish
2. English ("en") — article in English

Format each as HTML inside <section class="long-content">...</section>
Include these sections: intro paragraph (2 sentences), formula with explanation,
2 worked examples with real numbers, list of common uses (6 items),
common mistakes (4 items), pro tip, FAQ with 4 questions.

For FAQ use this exact HTML structure:
<div class="faq-list">
<div class="faq-item"><button class="faq-q" aria-expanded="false">Question?</button><div class="faq-a"><p>Answer.</p></div></div>
</div>

The output for each language should be a single Python string starting with:
    "es": \"\"\"<section class="long-content">
and ending with:
    </section>\"\"\",

Ready to paste directly into the LONG_CONTENT dict in calc_content.py as entry "{cid}".
"""

# Build output
lines = []
lines.append("=" * 70)
lines.append("GEMINI PROMPTS FOR CALCTOWORK — 252 CALCULATORS WITHOUT CONTENT")
lines.append("=" * 70)
lines.append("")
lines.append("Instructions:")
lines.append("1. For each section below, copy the PROMPT and paste into Gemini/NotebookLM")
lines.append("2. Take the output and add it to LONG_CONTENT in scripts/calc_content.py")
lines.append("3. Format: add  \"ID\": { ...output... },  inside the LONG_CONTENT dict")
lines.append("4. After adding all articles for a batch: rebuild + deploy")
lines.append("   Python: C:\\Users\\julie\\AppData\\Local\\Programs\\Python\\Python314\\python.exe scripts/generate_calctowork.py")
lines.append("   Deploy: firebase deploy --only hosting")
lines.append("")

# Read template-only IDs
import re
with open('scripts/calc_content.py', encoding='utf-8') as f:
    content = f.read()
start = content.index('LONG_CONTENT = {')
segment = content[start:start+500000]
long_content_ids = set(re.findall(r'\n    \"(\d+)\"\s*:', segment))
with open('src/calculators/calculators.json', encoding='utf-8') as f:
    data = json.load(f)
calcs = data['calculators']
all_ids = set(c['id'] for c in calcs)
template_only = sorted(all_ids - long_content_ids, key=lambda x: int(x))

# Group by category
categories = {
    'Math & Physics (111-149)': [i for i in template_only if 111 <= int(i) <= 149],
    'Finance (320-339)': [i for i in template_only if 320 <= int(i) <= 339],
    'Health (415-434)': [i for i in template_only if 415 <= int(i) <= 434],
    'Everyday / Tech (503-522)': [i for i in template_only if 503 <= int(i) <= 522],
    'Extra Math/Health/Finance (910-962)': [i for i in template_only if 910 <= int(i) <= 962],
    'Chemistry (1000-1009)': [i for i in template_only if 1000 <= int(i) <= 1009],
    'Electronics (1010-1019)': [i for i in template_only if 1010 <= int(i) <= 1019],
    'Weather & Climate (1020-1029)': [i for i in template_only if 1020 <= int(i) <= 1029],
    'Utilities & Date/Time (1030-1044)': [i for i in template_only if 1030 <= int(i) <= 1044],
    'Aviation & Transport (1045-1049)': [i for i in template_only if 1045 <= int(i) <= 1049],
    'Extended Physics (1050-1059)': [i for i in template_only if 1050 <= int(i) <= 1059],
    'Extended Health/Sports (1060-1099)': [i for i in template_only if 1060 <= int(i) <= 1099],
}

total = 0
for cat_name, ids in categories.items():
    if not ids:
        continue
    lines.append("")
    lines.append("=" * 70)
    lines.append(f"CATEGORY: {cat_name}  ({len(ids)} calculators)")
    lines.append("=" * 70)
    for cid in ids:
        if cid not in DESCS:
            lines.append(f"\n--- ID {cid} — NO DESCRIPTION (skip or add manually) ---")
            continue
        name, desc, formula = DESCS[cid]
        lines.append(f"\n{'─'*60}")
        lines.append(f"PROMPT FOR ID {cid} — {name}")
        lines.append('─'*60)
        lines.append(PROMPT_TEMPLATE.format(cid=cid, name=name, desc=desc, formula=formula))
        total += 1

lines.append("")
lines.append(f"Total prompts generated: {total}")

out = "\n".join(lines)
with open('GEMINI_PROMPTS.txt', 'w', encoding='utf-8') as f:
    f.write(out)
print(f"Written {len(out):,} chars, {total} prompts to GEMINI_PROMPTS.txt")
