# Calculators Needing Long-Form Content (13 remaining)

Write unique, high-quality content following the template in `content_template.md`.

## High Priority (Health - User facing)

### 1. ID: 402 - Peso Ideal (Ideal Weight Calculator)
- **Slug:** `peso-ideal` | **Block:** salud
- **File:** `src/content/en/402.html`
- **Key topics:** Devine formula, Robinson formula, Miller formula, Hamwi method, healthy weight ranges by height, BMI correlation, body frame size

### 2. ID: 403 - Agua Diaria (Daily Water Intake Calculator)  
- **Slug:** `agua-diaria` | **Block:** salud
- **File:** `src/content/en/403.html`
- **Key topics:** 8x8 rule, weight-based calculation, activity level adjustments, climate factors, hydration signs, urine color chart

## High Priority (Math - High traffic)

### 3. ID: 200 - Porcentaje (Percentage Calculator)
- **Slug:** `porcentaje` | **Block:** matematicas
- **File:** `src/content/en/200.html`
- **Key topics:** Percentage formula, percentage of a number, percentage increase/decrease, real-world examples (tips, discounts, tax)

### 4. ID: 201 - Cambio Porcentual (Percentage Change Calculator)
- **Slug:** `cambio-porcentual` | **Block:** matematicas
- **File:** `src/content/en/201.html`
- **Key topics:** Increase/decrease formula, growth rate, before/after comparisons, business and finance applications

### 5. ID: 203 - Pitágoras (Pythagorean Theorem Calculator)
- **Slug:** `pitagoras` | **Block:** matematicas
- **File:** `src/content/en/203.html`
- **Key topics:** a² + b² = c², right triangles, hypotenuse calculation, real-world applications (construction, navigation)

### 6. ID: 210 - Área Círculo (Circle Area Calculator)
- **Slug:** `area-circulo` | **Block:** matematicas
- **File:** `src/content/en/210.html`
- **Key topics:** A = πr², diameter vs radius, circumference relationship, practical examples (pizza, pools, gardens)

## Medium Priority (Everyday use)

### 7. ID: 500 - Propina (Tip Calculator)
- **Slug:** `propina` | **Block:** cotidiano
- **File:** `src/content/en/500.html`
- **Key topics:** Tip percentages (15%, 18%, 20%), splitting bills, regional customs, service quality considerations

### 8. ID: 501 - Calculadora Edad (Age Calculator)
- **Slug:** `calculadora-edad` | **Block:** cotidiano
- **File:** `src/content/en/501.html`
- **Key topics:** Calculate age in years/months/days, leap years, date differences, age milestones

## Lower Priority (Reference/Science)

### 9. ID: 700 - Velocidad (Speed Calculator)
- **Slug:** `velocidad` | **Block:** ciencia
- **File:** `src/content/en/700.html`
- **Key topics:** Speed = distance/time, unit conversions (mph, km/h, m/s), average vs instantaneous speed

### 10. ID: 800 - Longitud (Length Converter)
- **Slug:** `longitud` | **Block:** conversion
- **File:** `src/content/en/800.html`
- **Key topics:** Metric vs imperial, conversion factors, common conversions (feet to meters, inches to cm)

### 11. ID: 802 - Temperatura (Temperature Converter)
- **Slug:** `temperatura` | **Block:** conversion
- **File:** `src/content/en/802.html`
- **Key topics:** Celsius, Fahrenheit, Kelvin formulas, conversion examples, absolute zero

### 12. ID: 600 - Media (Mean Calculator)
- **Slug:** `media` | **Block:** estadistica
- **File:** `src/content/en/600.html`
- **Key topics:** Arithmetic mean formula, mean vs median vs mode, when to use each, examples with datasets

### 13. ID: 900 - Ritmo Carrera (Running Pace Calculator)
- **Slug:** `ritmo-carrera` | **Block:** deportes
- **File:** `src/content/en/900.html`
- **Key topics:** Pace = time/distance, marathon/half marathon training, speed vs pace, target pace calculations

---

## Quick Start

1. Open `content_template.md` for the structure
2. Pick one calculator from above
3. Research the topic (formulas, common questions, use cases)
4. Write unique content following the template
5. Save to `src/content/en/{ID}.html`
6. Run: `python scripts/generate_calctowork.py` to rebuild

## Example Reference

See `src/content/en/400.html` (BMI Calculator) for a complete, high-quality example.
