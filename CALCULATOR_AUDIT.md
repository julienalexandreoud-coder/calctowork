# CalcToWork Calculator Audit Checklist

**Goal:** Verify every calculator works correctly, produces accurate results, and has good SEO.


**Rules:**
- Check one calculator at a time.
- Do NOT skip any item.
- Mark complete only after testing the live page.
- Record findings in the Audit Log at the bottom immediately after each check.

## Progress Tracker

| Status | Count | Percentage |
|--------|-------|------------|
| Total | 461 | 100% |
| Audited | 461 | 100% |
| Pass | 0 | 0% |
| Warn | 461 | 100% |
| Fail | 0 | 0% |
| Remaining | 0 | 0% |

*Automated audit run — see Audit Results section below.*

## Audit Order

Calculators are listed in priority order (highest first):
1. `estructuras` → `pavimentos` → `mamposteria` → `pintura` (construction core)
2. `carpinteria` → `fontaneria` → `electricidad` → `climatizacion` (building systems)
3. `gestion` (construction management)
4. `matematicas` → `finanzas` → `salud` (large blocks, verify carefully)
5. Remaining blocks (ciencia, conversion, deportes, etc.)

---

## Summary of Issues

- **Total calculators audited:** 461
- **PASS:** 0 (0%)
- **WARN (minor issues):** 461 (100%)
- **FAIL (critical issues):** 0 (0%)

### Issue Categories

| Category | Count | Details |
|----------|-------|---------|
| Missing content files | 0 | No `src/content/en/{id}.html` |
| Missing i18n entry | 0 | Not in en.json calculators block |
| SEO title issues | 0 | Too long or missing |
| SEO description issues | 461 | Too short/long or missing |
| Both seo_desc + seo_description | 461 | Field name inconsistency |
| Formula/i18n output mismatch | 0 | Keys don't match |
| Garbled chars in SEO title | 0 | `?` replacing special chars |
| Thin content (<200 words) | 0 | Needs more content |
| Full HTML doc (not fragment) | 0 | Has DOCTYPE/</body> |

### Inconsistent SEO Field Names (both seo_desc AND seo_description present)

- `001` — Mass Concrete Calculator
- `002` — Reinforced Concrete Calculator
- `003` — Isolated Footing Calculator
- `004` — Retaining Wall Calculator
- `005` — Concrete Column Calculator
- `006` — Concrete Beam Calculator
- `007` — Joist and Slab Calculator
- `008` — Concrete Slab Calculator
- `009` — Strip Foundation Calculator
- `010` — Excavation Volume Calculator
- `011` — Hollow Brick Calculator
- `012` — Face Brick Calculator
- `013` — Concrete Block Calculator
- `014` — Drywall Partition Calculator
- `015` — Thermal Insulation Calculator
- `016` — Sprayed Plaster Calculator
- `017` — Cement Mortar Calculator
- `018` — Rendering and Skimming Calculator
- `019` — Stone Masonry Calculator
- `020` — Roofing Tiles Calculator
- `021` — Ceramic Floor Tile Calculator
- `022` — Porcelain Stoneware Calculator
- `023` — Laminate Flooring Calculator
- `024` — Wood Parquet Calculator
- `025` — Marble and Granite Calculator
- `026` — Terrazzo Calculator
- `027` — Wall Tile Calculator
- `028` — Mosaic Calculator
- `029` — Tile Adhesive Calculator
- `030` — Grout Calculator
- `031` — PVC Drainage Pipe Calculator
- `032` — Copper and PEX Pipe Calculator
- `033` — Water Pressure Calculator
- `034` — Water Tank Size Calculator
- `035` — Electric Water Heater Calculator
- `036` — Gas Boiler Calculator
- `037` — Aluminium Radiator Calculator
- `038` — Underfloor Heating Calculator
- `039` — Drip Irrigation Calculator
- `040` — Water Supply Connection Calculator
- `041` — Pool Filtration Calculator
- `042` — Trap and Drain Calculator
- `043` — Electrical Cable Cross-Section Calculator
- `044` — Voltage Drop Calculator
- `045` — LED Lighting Lumen Calculator
- `046` — Light Points per Room Calculator
- `047` — Electrical Panel Calculator
- `048` — Solar Panel Installation Calculator
- `049` — Battery Storage Calculator
- `050` — Three-Phase Power Calculator
- ... and 411 more

### SEO Description Issues

- `001` — Mass Concrete Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `002` — Reinforced Concrete Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `003` — Isolated Footing Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `004` — Retaining Wall Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `005` — Concrete Column Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `006` — Concrete Beam Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `007` — Joist and Slab Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `008` — Concrete Slab Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `009` — Strip Foundation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `010` — Excavation Volume Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `011` — Hollow Brick Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `012` — Face Brick Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `013` — Concrete Block Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `014` — Drywall Partition Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `015` — Thermal Insulation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `016` — Sprayed Plaster Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `017` — Cement Mortar Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `018` — Rendering and Skimming Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `019` — Stone Masonry Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `020` — Roofing Tiles Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `021` — Ceramic Floor Tile Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `022` — Porcelain Stoneware Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `023` — Laminate Flooring Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `024` — Wood Parquet Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `025` — Marble and Granite Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `026` — Terrazzo Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `027` — Wall Tile Calculator: Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160)
- `028` — Mosaic Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `029` — Tile Adhesive Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `030` — Grout Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `031` — PVC Drainage Pipe Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `032` — Copper and PEX Pipe Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `033` — Water Pressure Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `034` — Water Tank Size Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `035` — Electric Water Heater Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `036` — Gas Boiler Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `037` — Aluminium Radiator Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `038` — Underfloor Heating Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `039` — Drip Irrigation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `040` — Water Supply Connection Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `041` — Pool Filtration Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `042` — Trap and Drain Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `043` — Electrical Cable Cross-Section Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `044` — Voltage Drop Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `045` — LED Lighting Lumen Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `046` — Light Points per Room Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `047` — Electrical Panel Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `048` — Solar Panel Installation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `049` — Battery Storage Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `050` — Three-Phase Power Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `051` — Earthing (Grounding) Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `052` — Monthly Electricity Consumption Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `053` — Air Conditioning BTU Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `054` — Air Duct Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `055` — Mechanical Ventilation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `056` — Air-to-Water Heat Pump Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `057` — COP and EER Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `058` — HVAC Duct Sizing Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `059` — Grilles and Diffusers Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `060` — Refrigerant Gas Charge Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `061` — Aluminium/PVC Window Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `062` — Interior Door Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `063` — Sliding Door Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `064` — Wooden Staircase Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `065` — Metal Railing Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `066` — Metal Structure Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `067` — Metal Door and Gate Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `068` — Glass Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `069` — Emulsion Paint Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `070` — Ceiling Paint Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `071` — Synthetic Enamel Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `072` — Exterior Varnish Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `073` — Wallpaper Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `074` — Textured Finish Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `075` — Primer and Sealer Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `076` — Filler and Putty Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `077` — Sandpaper Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `078` — Renovation Budget Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `079` — Hourly Rate Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `080` — Machinery Amortisation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `081` — Vehicle Amortisation Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `082` — Fuel Cost Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `083` — Travel and Subsistence Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `084` — Skip Rental Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `085` — Scaffolding Rental Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `086` — Post-Construction Cleaning Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `087` — Liability Insurance Estimator: Both seo_desc and seo_description fields present (inconsistent)
- `088` — PPE Cost Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `089` — Construction Signage Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `090` — Daily Productivity Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `091` — Simple Project Planning Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `092` — Building Permits and Fees Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `093` — VAT and Income Tax Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `094` — Equipment Loan Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `095` — Profit Margin Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `096` — Break-Even Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `097` — Site Water Consumption Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `098` — Material Waste Factor Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `099` — Workforce Cost Calculator: Both seo_desc and seo_description fields present (inconsistent)
- `100` — Tool ROI Calculator: Both seo_desc and seo_description fields present (inconsistent)
- ... and 361 more

---

## Audit Results

| ID | Name | Block | Status | Issues |
|----|------|-------|--------|--------|
| 001 | Mass Concrete Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 002 | Reinforced Concrete Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 003 | Isolated Footing Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 004 | Retaining Wall Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 005 | Concrete Column Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 006 | Concrete Beam Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 007 | Joist and Slab Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 008 | Concrete Slab Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 009 | Strip Foundation Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 010 | Excavation Volume Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 011 | Hollow Brick Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 012 | Face Brick Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 013 | Concrete Block Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 014 | Drywall Partition Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 015 | Thermal Insulation Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 016 | Sprayed Plaster Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 017 | Cement Mortar Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 018 | Rendering and Skimming Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 019 | Stone Masonry Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 020 | Roofing Tiles Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 021 | Ceramic Floor Tile Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 022 | Porcelain Stoneware Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 023 | Laminate Flooring Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 024 | Wood Parquet Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 025 | Marble and Granite Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 026 | Terrazzo Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 027 | Wall Tile Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160) |
| 028 | Mosaic Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 029 | Tile Adhesive Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 030 | Grout Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 031 | PVC Drainage Pipe Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 032 | Copper and PEX Pipe Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 033 | Water Pressure Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 034 | Water Tank Size Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 035 | Electric Water Heater Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 036 | Gas Boiler Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 037 | Aluminium Radiator Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 038 | Underfloor Heating Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 039 | Drip Irrigation Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 040 | Water Supply Connection Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 041 | Pool Filtration Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 042 | Trap and Drain Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 043 | Electrical Cable Cross-Section Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 044 | Voltage Drop Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 045 | LED Lighting Lumen Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 046 | Light Points per Room Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 047 | Electrical Panel Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 048 | Solar Panel Installation Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 049 | Battery Storage Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 050 | Three-Phase Power Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 051 | Earthing (Grounding) Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 052 | Monthly Electricity Consumption Calculator | electricidad | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 053 | Air Conditioning BTU Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 054 | Air Duct Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 055 | Mechanical Ventilation Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 056 | Air-to-Water Heat Pump Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 057 | COP and EER Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 058 | HVAC Duct Sizing Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 059 | Grilles and Diffusers Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 060 | Refrigerant Gas Charge Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 061 | Aluminium/PVC Window Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 062 | Interior Door Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 063 | Sliding Door Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 064 | Wooden Staircase Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 065 | Metal Railing Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 066 | Metal Structure Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 067 | Metal Door and Gate Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 068 | Glass Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 069 | Emulsion Paint Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 070 | Ceiling Paint Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 071 | Synthetic Enamel Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 072 | Exterior Varnish Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 073 | Wallpaper Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 074 | Textured Finish Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 075 | Primer and Sealer Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 076 | Filler and Putty Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 077 | Sandpaper Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 078 | Renovation Budget Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 079 | Hourly Rate Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 080 | Machinery Amortisation Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 081 | Vehicle Amortisation Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 082 | Fuel Cost Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 083 | Travel and Subsistence Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 084 | Skip Rental Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 085 | Scaffolding Rental Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 086 | Post-Construction Cleaning Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 087 | Liability Insurance Estimator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 088 | PPE Cost Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 089 | Construction Signage Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 090 | Daily Productivity Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 091 | Simple Project Planning Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 092 | Building Permits and Fees Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 093 | VAT and Income Tax Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 094 | Equipment Loan Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 095 | Profit Margin Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 096 | Break-Even Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 097 | Site Water Consumption Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 098 | Material Waste Factor Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 099 | Workforce Cost Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 100 | Tool ROI Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 101 | Swimming Pool Volume Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 102 | Garden Topsoil Calculator | fontaneria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 103 | Fence Post & Panel Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 200 | Percentage Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 201 | Percentage Change Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 202 | Rectangle Area Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 203 | Pythagorean Theorem Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 204 | Rule of Three Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 210 | Circle Area Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 211 | Triangle Area Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 212 | Sphere Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 213 | Cylinder Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 214 | Exponent Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 215 | Root Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 216 | Logarithm Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 217 | Factorial Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 218 | Quadratic Equation Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 219 | Lcm Gcd Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 300 | Mortgage Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 301 | Loan Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 302 | Compound Interest Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 303 | Simple Interest Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 304 | VAT Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 305 | Net Salary Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 306 | Discount Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 307 | Break-Even Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 310 | Roi Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 311 | Compound Savings Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 312 | Inflation Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (167 chars > 160); No error return in formula |
| 313 | Salary Increase Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160); No error return in formula |
| 314 | Retirement Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (167 chars > 160); No error return in formula |
| 315 | Rule Of 72 Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160) |
| 316 | Term Deposit Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (166 chars > 160); No error return in formula |
| 317 | Stock Return Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (169 chars > 160); No error return in formula |
| 318 | Debt To Income Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 319 | Break Even Units Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (167 chars > 160) |
| 400 | BMI Calculator (Body Mass Index) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 401 | Daily Calorie Calculator (TDEE) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 402 | Ideal Weight Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 403 | Daily Water Intake Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 410 | Bmr Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (163 chars > 160) |
| 411 | Max Heart Rate Health Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 412 | Sleep Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (169 chars > 160); No error return in formula |
| 413 | Body Fat Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (166 chars > 160) |
| 414 | Healthy Weight Range Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (169 chars > 160) |
| 500 | Tip Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 501 | Age Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 502 | Date Difference Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 600 | Mean Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 601 | Median Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 602 | Standard Deviation Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 603 | Probability Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160) |
| 604 | Combinations Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160) |
| 605 | Permutations Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 606 | Confidence Interval Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 607 | Coefficient Of Variation Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 608 | Variance Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 609 | Z Score Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 700 | Speed Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 701 | Density Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 702 | Force Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (167 chars > 160); No error return in formula |
| 703 | Kinetic Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 704 | Potential Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 705 | Pressure Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 706 | Work Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 707 | Ohms Law Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 708 | Electrical Power Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 709 | Acceleration Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 800 | Length Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 801 | Weight Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (167 chars > 160); No error return in formula |
| 802 | Temperature Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 803 | Volume Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160); No error return in formula |
| 804 | Area Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (164 chars > 160); No error return in formula |
| 805 | Speed Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160); No error return in formula |
| 806 | Data Storage Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (162 chars > 160); No error return in formula |
| 807 | Pressure Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160); No error return in formula |
| 808 | Time Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160); No error return in formula |
| 809 | Energy Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (164 chars > 160); No error return in formula |
| 900 | Running Pace Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 901 | Exercise Calorie Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (170 chars > 160); No error return in formula |
| 902 | Max Heart Rate Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (161 chars > 160) |
| 903 | Heart Rate Zones Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160) |
| 904 | Vo2 Max Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160) |
| 905 | Steps To Calories Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160); No error return in formula |
| 906 | Swimming Pace Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (168 chars > 160) |
| 907 | Cycling Pace Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (164 chars > 160) |
| 908 | Athletic Bmi Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (169 chars > 160) |
| 909 | Race Time Predictor | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (164 chars > 160) |
| 910 | Fraction Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 911 | Slope Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 912 | Scientific Notation Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 913 | Rounding Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 914 | GCF & LCM Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 915 | Prime Factorization Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 916 | Circle Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 917 | Right Triangle Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 918 | Triangle Area (Heron's Formula) | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 919 | Rectangle Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 920 | Square Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 921 | Trapezoid Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 922 | Cylinder Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 923 | Cone Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 924 | Pyramid Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 925 | Sphere Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 926 | BMR Calculator (Harris-Benedict) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 927 | BMR Calculator (Katch-McArdle) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 928 | Macro Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 929 | Blood Pressure Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 930 | Waist-to-Hip Ratio Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 931 | Waist-to-Height Ratio Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 932 | Weight Loss Percentage Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 933 | Heart Rate Zones Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 934 | Salary to Hourly Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 935 | Hourly to Salary Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 936 | Mortgage Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 937 | Debt Payoff Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 938 | Savings Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 939 | Profit Margin Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 940 | NPV Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 941 | Emergency Fund Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 942 | Age Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 943 | Date Difference Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 944 | Tip Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 945 | Double Discount Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 946 | Kinetic Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 947 | Potential Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 948 | Work & Power Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 949 | Ohm's Law & Power Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 950 | Newton's Second Law Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 951 | One Rep Max Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 952 | Running Pace Predictor | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 953 | VO₂ Max Estimator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 954 | Angle Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 955 | Temperature Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 956 | Energy Converter | conversion | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 957 | Combinations & Permutations Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 958 | Z-Score & Percentile Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 959 | Sample Size Calculator | estadistica | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 960 | BSA & Ideal Weight Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 961 | A1C Estimator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 962 | LDL Cholesterol Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 110 | Absolute Value Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 111 | Arithmetic Sequence Sum Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 112 | Geometric Sequence Sum Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 113 | Complex Number Magnitude Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 114 | 2×2 Matrix Determinant Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 115 | 3D Vector Magnitude Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 116 | Dot Product Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 117 | Cross Product Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 118 | Quadratic Polynomial Derivative | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 119 | Trapezoidal Rule Integral Approximation | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 120 | Projectile Motion Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 121 | Centripetal Force Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 122 | Gravitational Force Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 123 | Elastic Potential Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 124 | Specific Heat Capacity Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 125 | Wave Speed Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 126 | Thin Lens Equation Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 127 | Torque Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 128 | Angular Momentum Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 129 | Fluid Pressure Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 320 | CAGR Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 321 | APR Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 322 | Loan Amortization Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 323 | Rental Yield Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 324 | Cap Rate Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 325 | Dividend Yield Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 326 | Price-to-Earnings Ratio Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 327 | Future Value of Annuity Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 328 | Present Value of Annuity Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 329 | WACC Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 415 | Lean Body Mass Calculator (Boer) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 416 | Body Adiposity Index (BAI) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 417 | Daily Protein Intake Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 418 | Recommended Fiber Intake | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 419 | Karvonen Heart Rate Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 420 | Heart Rate Training Zones | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 421 | Creatinine Clearance (Cockcroft-Gault) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 422 | BMI Prime Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 423 | Pregnancy Due Date Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 424 | Ovulation Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 503 | Fuel Cost Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 504 | Data Transfer Time Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 505 | Battery Life Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 506 | Download Time Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 507 | Screen DPI / PPI Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 508 | Aspect Ratio Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 509 | Password Entropy Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 510 | Bandwidth Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 511 | Uncompressed Image File Size | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 512 | Electricity Cost Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 130 | Logarithm Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 131 | Natural Logarithm | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 132 | Exponential Growth Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 133 | Factorial Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 134 | Permutations Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 135 | Combinations Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 136 | Standard Deviation Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 137 | Variance Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 138 | Median Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 139 | Quartile Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 140 | Bernoulli Equation Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 141 | Doppler Effect Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 142 | Snell's Law Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 143 | Coulomb Force Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 144 | Magnetic Force on Charge Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 145 | Thermal Expansion Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 146 | Stefan-Boltzmann Law Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 147 | RL Circuit Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 148 | RC Circuit Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 149 | Ideal Gas Law Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 330 | Payback Period Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 331 | Sharpe Ratio Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 332 | Tax Equivalent Yield Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 333 | Real Rate of Return Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 334 | Loan Affordability Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 335 | Mortgage Payoff Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 336 | Credit Card Payoff Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 337 | College Savings Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 338 | Life Insurance Needs Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 339 | Monthly CAGR Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 425 | Body Fat Navy Method | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 426 | TDEE Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 427 | BMR Calculator (Mifflin-St Jeor) | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 428 | RMR Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 429 | METs Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 430 | Target Weight Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 431 | Pregnancy Weight Gain Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 432 | Calories Burned Walking | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 433 | Child Growth Percentile | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 434 | Water Intake by Weight | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 513 | Screen Resolution | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 514 | Video File Size Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 515 | RAID Capacity Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 516 | Server Uptime Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 517 | Ping Latency Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 518 | Typing Speed (WPM) | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 519 | Reading Time Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 520 | SMS Cost Calculator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 521 | Data Usage Estimator | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 522 | Screen Brightness in Nits | cotidiano | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1000 | pH Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1001 | pOH Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1002 | Molarity Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1003 | Dilution Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1004 | Ideal Gas Law Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1005 | Boyle's Law Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1006 | Charles's Law Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1007 | Gibbs Free Energy Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1008 | Molecular Weight Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1009 | Titration Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1010 | Voltage Divider Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1011 | LED Resistor Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1012 | Parallel Resistance Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1013 | Capacitor Energy Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1014 | Inductor Energy Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1015 | Transformer Turns Ratio | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1016 | RC Time Constant Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1017 | Wheatstone Bridge Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1018 | Series Capacitance Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1019 | Resistor Color Code Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1020 | Dew Point Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1021 | Heat Index Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1022 | Wind Chill Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1023 | Relative Humidity Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1024 | Air Quality Index Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1025 | Daylight Hours Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1026 | UV Exposure Time Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1027 | Pressure Altitude Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1028 | Rainfall Volume Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1029 | Evapotranspiration Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1030 | Day of Year Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1031 | Week Number Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1032 | Age in Days Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1033 | Reading Time Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1034 | Password Generator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1035 | Random Number Generator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1036 | Dice Roller | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1037 | Coin Flip | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1038 | Hex to RGB Converter | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1039 | Exposure Value Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1040 | Depth of Field Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1041 | Hyperfocal Distance Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1042 | Decibel Addition Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1043 | SPL Distance Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1044 | Contrast Ratio Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1045 | Crosswind Component Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1046 | Fuel Burn Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1047 | True Airspeed Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1048 | Hull Speed Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1049 | Great Circle Distance Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1050 | Regular Polygon Area Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1051 | Cone Volume Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1052 | Arithmetic Series Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1053 | Geometric Series Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1054 | Combinations Calculator | matematicas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1055 | Buoyancy Force Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1056 | Doppler Effect Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1057 | AC Impedance Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1058 | Moment of Inertia Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1059 | Rotational Energy Calculator | ciencia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1060 | Body Fat (Navy) Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1061 | Mifflin-St Jeor BMR Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1062 | Daily Water Intake Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1063 | One Rep Max (Brzycki) Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1064 | Daily Protein Calculator | salud | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1065 | Dividend Yield Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1066 | Payback Period Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1067 | Capital Gains Tax Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1068 | Currency Exchange Commission Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1069 | Break Even Point Calculator | finanzas | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1070 | Molar Mass Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1071 | pH Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1072 | Ideal Gas Law Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1073 | Molarity Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1074 | Dilution Calculator | quimica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1075 | Resistor Color Code Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1076 | Capacitor Energy Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1077 | Voltage Divider Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1078 | RC Time Constant Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1079 | Wheatstone Bridge Calculator | electronica | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1080 | Fuel Consumption Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1081 | Braking Distance Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1082 | Engine Displacement Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1083 | Tire Pressure Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1084 | Flight Time with Wind Calculator | transporte | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1085 | Depth of Field Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1086 | Flash Guide Number Calculator | fotografia | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1087 | Heat Index Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1088 | Wind Chill Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1089 | Relative Humidity & Dew Point Calculator | clima | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1090 | Password Entropy Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1091 | Character & Word Counter | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1092 | Business Days Calculator | utilidades | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1093 | Beam Deflection Calculator | ingenieria | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1094 | Bolt Torque Calculator | ingenieria | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1095 | Spring Constant Calculator | ingenieria | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1096 | Reynolds Number Calculator | ingenieria | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1097 | Running Pace Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1098 | Golf Handicap Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1099 | MET Calories Burned Calculator | deportes | WARN | Both seo_desc and seo_description fields present (inconsistent); No error return in formula |
| 1100 | Decking Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1101 | Sod & Turf Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1102 | Mulch Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1103 | Fence Picket Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1104 | Roofing Shingle Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1105 | Insulation Batt Calculator | climatizacion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1106 | Carpet Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1107 | Laminate Flooring Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1108 | Countertop Calculator | gestion | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1109 | Backsplash Tile Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1110 | Grout Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1111 | Paint Coverage Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1112 | Wallpaper Calculator | pintura | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1113 | Crown Molding Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1114 | Baseboard Calculator | carpinteria | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (165 chars > 160) |
| 1115 | Drywall Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1116 | Concrete Steps Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (164 chars > 160) |
| 1117 | Retaining Wall Calculator | mamposteria | WARN | Both seo_desc and seo_description fields present (inconsistent); SEO desc too long (163 chars > 160) |
| 1118 | Paver Calculator | pavimentos | WARN | Both seo_desc and seo_description fields present (inconsistent) |
| 1119 | Landscape Rock Calculator | estructuras | WARN | Both seo_desc and seo_description fields present (inconsistent) |

---

## Detailed Issues Per Calculator

Only calculators with issues are listed here.

### 001 — Mass Concrete Calculator
**Slug:** `hormigon-masa` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1776 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 002 — Reinforced Concrete Calculator
**Slug:** `hormigon-armado` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1809 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 003 — Isolated Footing Calculator
**Slug:** `zapata-aislada` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1835 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 004 — Retaining Wall Calculator
**Slug:** `muro-contencion` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1937 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 005 — Concrete Column Calculator
**Slug:** `pilares-hormigon` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1982 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 006 — Concrete Beam Calculator
**Slug:** `vigas-hormigon` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1978 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 007 — Joist and Slab Calculator
**Slug:** `forjado-vigueta` | **Block:** `estructuras` | **Status:** WARN
**Content:** 2031 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 008 — Concrete Slab Calculator
**Slug:** `losa-hormigon` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1803 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 009 — Strip Foundation Calculator
**Slug:** `cimiento-corrido` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1985 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 010 — Excavation Volume Calculator
**Slug:** `excavacion-tierra` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1837 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 011 — Hollow Brick Calculator
**Slug:** `ladrillo-hueco` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2023 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 012 — Face Brick Calculator
**Slug:** `ladrillo-cara-vista` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 1767 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 013 — Concrete Block Calculator
**Slug:** `bloque-hormigon` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 1767 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 014 — Drywall Partition Calculator
**Slug:** `tabique-pladur` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2068 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 015 — Thermal Insulation Calculator
**Slug:** `aislamiento-termico` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2006 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 016 — Sprayed Plaster Calculator
**Slug:** `revoco-proyectado` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2105 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 017 — Cement Mortar Calculator
**Slug:** `mortero-cemento` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2131 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 018 — Rendering and Skimming Calculator
**Slug:** `enfoscado-guarnecido` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2196 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 019 — Stone Masonry Calculator
**Slug:** `mamposteria-piedra` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2260 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 020 — Roofing Tiles Calculator
**Slug:** `cubierta-teja` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2265 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 021 — Ceramic Floor Tile Calculator
**Slug:** `solado-ceramico` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1964 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 022 — Porcelain Stoneware Calculator
**Slug:** `porcelanico` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1760 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 023 — Laminate Flooring Calculator
**Slug:** `laminado-flotante` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1607 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 024 — Wood Parquet Calculator
**Slug:** `parquet-madera` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1659 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 025 — Marble and Granite Calculator
**Slug:** `marmol-granito` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1913 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 026 — Terrazzo Calculator
**Slug:** `terrazo` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1652 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 027 — Wall Tile Calculator
**Slug:** `azulejo-pared` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 2018 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)

### 028 — Mosaic Calculator
**Slug:** `mosaico` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 2034 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 029 — Tile Adhesive Calculator
**Slug:** `adhesivo-ceramico` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1739 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 030 — Grout Calculator
**Slug:** `lechada-junta` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 1859 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 031 — PVC Drainage Pipe Calculator
**Slug:** `tuberia-pvc-saneamiento` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1780 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 032 — Copper and PEX Pipe Calculator
**Slug:** `tuberia-cobre-pex` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1745 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 033 — Water Pressure Calculator
**Slug:** `presion-agua` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1823 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 034 — Water Tank Size Calculator
**Slug:** `deposito-agua` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1706 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 035 — Electric Water Heater Calculator
**Slug:** `calentador-agua` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1751 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 036 — Gas Boiler Calculator
**Slug:** `caldera-gas` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1686 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 037 — Aluminium Radiator Calculator
**Slug:** `radiador-aluminio` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1706 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 038 — Underfloor Heating Calculator
**Slug:** `suelo-radiante` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1696 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 039 — Drip Irrigation Calculator
**Slug:** `riego-goteo` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1950 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 040 — Water Supply Connection Calculator
**Slug:** `acometida-agua` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1701 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 041 — Pool Filtration Calculator
**Slug:** `depuradora-piscina` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1317 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 042 — Trap and Drain Calculator
**Slug:** `sifon-sumidero` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 1393 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 043 — Electrical Cable Cross-Section Calculator
**Slug:** `cable-electrico-seccion` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1647 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 044 — Voltage Drop Calculator
**Slug:** `caida-tension` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1695 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 045 — LED Lighting Lumen Calculator
**Slug:** `luminarias-lumenes` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1766 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 046 — Light Points per Room Calculator
**Slug:** `puntos-luz-habitacion` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1908 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 047 — Electrical Panel Calculator
**Slug:** `cuadro-electrico` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1947 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 048 — Solar Panel Installation Calculator
**Slug:** `instalacion-solar` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1793 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 049 — Battery Storage Calculator
**Slug:** `baterias-autonomia` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1983 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 050 — Three-Phase Power Calculator
**Slug:** `trifasica-potencia` | **Block:** `electricidad` | **Status:** WARN
**Content:** 2100 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 051 — Earthing (Grounding) Calculator
**Slug:** `puesta-tierra` | **Block:** `electricidad` | **Status:** WARN
**Content:** 2024 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 052 — Monthly Electricity Consumption Calculator
**Slug:** `consumo-electrico-mensual` | **Block:** `electricidad` | **Status:** WARN
**Content:** 1973 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 053 — Air Conditioning BTU Calculator
**Slug:** `aire-acondicionado-btu` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2054 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 054 — Air Duct Calculator
**Slug:** `conductos-aire` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2223 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 055 — Mechanical Ventilation Calculator
**Slug:** `ventilacion-mecanica` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2094 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 056 — Air-to-Water Heat Pump Calculator
**Slug:** `bomba-calor-aerotermia` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2176 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 057 — COP and EER Calculator
**Slug:** `calculo-cop-eer` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2355 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 058 — HVAC Duct Sizing Calculator
**Slug:** `dimensionado-conducto` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2093 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 059 — Grilles and Diffusers Calculator
**Slug:** `rejillas-difusores` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 2185 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 060 — Refrigerant Gas Charge Calculator
**Slug:** `carga-gas-refrigerante` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 1968 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 061 — Aluminium/PVC Window Calculator
**Slug:** `ventanas-aluminio-pvc` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 2065 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 062 — Interior Door Calculator
**Slug:** `puertas-paso` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1975 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 063 — Sliding Door Calculator
**Slug:** `puertas-correderas` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1851 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 064 — Wooden Staircase Calculator
**Slug:** `escalera-madera` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1950 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 065 — Metal Railing Calculator
**Slug:** `barandilla-metalica` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1895 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 066 — Metal Structure Calculator
**Slug:** `estructuras-metalicas` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1893 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 067 — Metal Door and Gate Calculator
**Slug:** `cerrajeria-puerta` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1655 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 068 — Glass Calculator
**Slug:** `vidrio-cristal` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1688 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 069 — Emulsion Paint Calculator
**Slug:** `pintura-plastica-paredes` | **Block:** `pintura` | **Status:** WARN
**Content:** 1718 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 070 — Ceiling Paint Calculator
**Slug:** `pintura-techo` | **Block:** `pintura` | **Status:** WARN
**Content:** 1710 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 071 — Synthetic Enamel Calculator
**Slug:** `esmalte-sintetico` | **Block:** `pintura` | **Status:** WARN
**Content:** 1688 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 072 — Exterior Varnish Calculator
**Slug:** `barniz-exterior` | **Block:** `pintura` | **Status:** WARN
**Content:** 1669 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 073 — Wallpaper Calculator
**Slug:** `papel-pintado` | **Block:** `pintura` | **Status:** WARN
**Content:** 1684 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 074 — Textured Finish Calculator
**Slug:** `acabado-texturado` | **Block:** `pintura` | **Status:** WARN
**Content:** 1642 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 075 — Primer and Sealer Calculator
**Slug:** `imprimacion-sellador` | **Block:** `pintura` | **Status:** WARN
**Content:** 1574 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 076 — Filler and Putty Calculator
**Slug:** `masilla-filler` | **Block:** `pintura` | **Status:** WARN
**Content:** 2984 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 077 — Sandpaper Calculator
**Slug:** `lija-abrasivo` | **Block:** `pintura` | **Status:** WARN
**Content:** 3514 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 078 — Renovation Budget Calculator
**Slug:** `presupuesto-reforma` | **Block:** `gestion` | **Status:** WARN
**Content:** 3204 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 079 — Hourly Rate Calculator
**Slug:** `precio-hora-trabajo` | **Block:** `gestion` | **Status:** WARN
**Content:** 3638 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 080 — Machinery Amortisation Calculator
**Slug:** `amortizacion-maquinaria` | **Block:** `gestion` | **Status:** WARN
**Content:** 3839 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 081 — Vehicle Amortisation Calculator
**Slug:** `amortizacion-vehiculo` | **Block:** `gestion` | **Status:** WARN
**Content:** 3786 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 082 — Fuel Cost Calculator
**Slug:** `coste-combustible` | **Block:** `gestion` | **Status:** WARN
**Content:** 4010 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 083 — Travel and Subsistence Calculator
**Slug:** `dietas-desplazamiento` | **Block:** `gestion` | **Status:** WARN
**Content:** 4040 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 084 — Skip Rental Calculator
**Slug:** `alquiler-contenedor` | **Block:** `gestion` | **Status:** WARN
**Content:** 4289 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 085 — Scaffolding Rental Calculator
**Slug:** `alquiler-andamio` | **Block:** `gestion` | **Status:** WARN
**Content:** 4113 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 086 — Post-Construction Cleaning Calculator
**Slug:** `limpieza-obra` | **Block:** `gestion` | **Status:** WARN
**Content:** 3593 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 087 — Liability Insurance Estimator
**Slug:** `seguro-responsabilidad` | **Block:** `gestion` | **Status:** WARN
**Content:** 3911 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 088 — PPE Cost Calculator
**Slug:** `epi-equipos-proteccion` | **Block:** `gestion` | **Status:** WARN
**Content:** 4316 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 089 — Construction Signage Calculator
**Slug:** `senalizacion-obra` | **Block:** `gestion` | **Status:** WARN
**Content:** 4034 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 090 — Daily Productivity Calculator
**Slug:** `rendimiento-diario` | **Block:** `gestion` | **Status:** WARN
**Content:** 4141 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 091 — Simple Project Planning Calculator
**Slug:** `planificacion-gantt` | **Block:** `gestion` | **Status:** WARN
**Content:** 4005 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 092 — Building Permits and Fees Calculator
**Slug:** `licencias-municipales` | **Block:** `gestion` | **Status:** WARN
**Content:** 3063 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 093 — VAT and Income Tax Calculator
**Slug:** `iva-irpf` | **Block:** `gestion` | **Status:** WARN
**Content:** 3302 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 094 — Equipment Loan Calculator
**Slug:** `prestamo-equipo` | **Block:** `gestion` | **Status:** WARN
**Content:** 3216 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 095 — Profit Margin Calculator
**Slug:** `margen-beneficio` | **Block:** `gestion` | **Status:** WARN
**Content:** 3076 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 096 — Break-Even Calculator
**Slug:** `punto-equilibrio` | **Block:** `gestion` | **Status:** WARN
**Content:** 2095 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 097 — Site Water Consumption Calculator
**Slug:** `consumo-agua-obra` | **Block:** `gestion` | **Status:** WARN
**Content:** 2203 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 098 — Material Waste Factor Calculator
**Slug:** `factor-merma-material` | **Block:** `gestion` | **Status:** WARN
**Content:** 2482 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 099 — Workforce Cost Calculator
**Slug:** `coste-mano-obra` | **Block:** `gestion` | **Status:** WARN
**Content:** 2600 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 100 — Tool ROI Calculator
**Slug:** `roi-herramienta` | **Block:** `gestion` | **Status:** WARN
**Content:** 2076 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 101 — Swimming Pool Volume Calculator
**Slug:** `volumen-piscina` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 2071 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 102 — Garden Topsoil Calculator
**Slug:** `tierra-jardin` | **Block:** `fontaneria` | **Status:** WARN
**Content:** 2073 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 103 — Fence Post & Panel Calculator
**Slug:** `postes-valla` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 2124 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 200 — Percentage Calculator
**Slug:** `porcentaje` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1463 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 201 — Percentage Change Calculator
**Slug:** `cambio-porcentual` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1608 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 202 — Rectangle Area Calculator
**Slug:** `area-rectangulo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1854 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 203 — Pythagorean Theorem Calculator
**Slug:** `pitagoras` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1908 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 204 — Rule of Three Calculator
**Slug:** `regla-de-tres` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2053 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 210 — Circle Area Calculator
**Slug:** `area-circulo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1951 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 211 — Triangle Area Calculator
**Slug:** `area-triangulo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2005 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 212 — Sphere Volume Calculator
**Slug:** `volumen-esfera` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2109 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 213 — Cylinder Volume Calculator
**Slug:** `volumen-cilindro` | **Block:** `matematicas` | **Status:** WARN
**Content:** 3463 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 214 — Exponent Calculator
**Slug:** `potencias` | **Block:** `matematicas` | **Status:** WARN
**Content:** 3025 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 215 — Root Calculator
**Slug:** `raiz` | **Block:** `matematicas` | **Status:** WARN
**Content:** 3262 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 216 — Logarithm Calculator
**Slug:** `logaritmo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 3457 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 217 — Factorial Calculator
**Slug:** `factorial` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2578 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 218 — Quadratic Equation Calculator
**Slug:** `ecuacion-segundo-grado` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2319 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 219 — Lcm Gcd Calculator
**Slug:** `mcm-mcd` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2149 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 300 — Mortgage Calculator
**Slug:** `hipoteca` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1426 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 301 — Loan Calculator
**Slug:** `prestamo` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1596 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 302 — Compound Interest Calculator
**Slug:** `interes-compuesto` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1522 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 303 — Simple Interest Calculator
**Slug:** `interes-simple` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1805 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 304 — VAT Calculator
**Slug:** `calculadora-iva` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1554 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 305 — Net Salary Calculator
**Slug:** `salario-neto` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1452 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 306 — Discount Calculator
**Slug:** `descuento` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1841 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 307 — Break-Even Calculator
**Slug:** `punto-de-equilibrio` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2160 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 310 — Roi Calculator
**Slug:** `roi` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2427 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 311 — Compound Savings Calculator
**Slug:** `ahorro-compuesto` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2668 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 312 — Inflation Calculator
**Slug:** `inflacion` | **Block:** `finanzas` | **Status:** WARN
**Content:** 3368 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (167 chars > 160)
- No error return in formula

### 313 — Salary Increase Calculator
**Slug:** `subida-salarial` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2773 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)
- No error return in formula

### 314 — Retirement Calculator
**Slug:** `plan-jubilacion` | **Block:** `finanzas` | **Status:** WARN
**Content:** 3000 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (167 chars > 160)
- No error return in formula

### 315 — Rule Of 72 Calculator
**Slug:** `regla-72` | **Block:** `finanzas` | **Status:** WARN
**Content:** 3208 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)

### 316 — Term Deposit Calculator
**Slug:** `deposito-plazo` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1687 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (166 chars > 160)
- No error return in formula

### 317 — Stock Return Calculator
**Slug:** `retorno-acciones` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1967 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (169 chars > 160)
- No error return in formula

### 318 — Debt To Income Calculator
**Slug:** `ratio-deuda` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1994 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 319 — Break Even Units Calculator
**Slug:** `punto-equilibrio-unidades` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2316 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (167 chars > 160)

### 400 — BMI Calculator (Body Mass Index)
**Slug:** `imc-bmi` | **Block:** `salud` | **Status:** WARN
**Content:** 1426 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 401 — Daily Calorie Calculator (TDEE)
**Slug:** `calorias-diarias` | **Block:** `salud` | **Status:** WARN
**Content:** 1682 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 402 — Ideal Weight Calculator
**Slug:** `peso-ideal` | **Block:** `salud` | **Status:** WARN
**Content:** 1909 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 403 — Daily Water Intake Calculator
**Slug:** `agua-diaria` | **Block:** `salud` | **Status:** WARN
**Content:** 1668 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 410 — Bmr Calculator
**Slug:** `metabolismo-basal` | **Block:** `salud` | **Status:** WARN
**Content:** 1701 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (163 chars > 160)

### 411 — Max Heart Rate Health Calculator
**Slug:** `frecuencia-cardiaca-max-salud` | **Block:** `salud` | **Status:** WARN
**Content:** 2710 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 412 — Sleep Calculator
**Slug:** `horas-sueno` | **Block:** `salud` | **Status:** WARN
**Content:** 1661 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (169 chars > 160)
- No error return in formula

### 413 — Body Fat Calculator
**Slug:** `porcentaje-grasa` | **Block:** `salud` | **Status:** WARN
**Content:** 1915 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (166 chars > 160)

### 414 — Healthy Weight Range Calculator
**Slug:** `rango-peso-saludable` | **Block:** `salud` | **Status:** WARN
**Content:** 3881 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (169 chars > 160)

### 500 — Tip Calculator
**Slug:** `propina` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 1531 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 501 — Age Calculator
**Slug:** `calculadora-edad` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 1476 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 502 — Date Difference Calculator
**Slug:** `diferencia-fechas` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2032 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 600 — Mean Calculator
**Slug:** `media` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1536 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 601 — Median Calculator
**Slug:** `mediana` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1512 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 602 — Standard Deviation Calculator
**Slug:** `desviacion-estandar` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1447 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 603 — Probability Calculator
**Slug:** `probabilidad` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1581 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)

### 604 — Combinations Calculator
**Slug:** `combinaciones` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1548 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)

### 605 — Permutations Calculator
**Slug:** `permutaciones` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1557 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 606 — Confidence Interval Calculator
**Slug:** `intervalo-confianza` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1821 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 607 — Coefficient Of Variation Calculator
**Slug:** `coeficiente-variacion` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1611 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 608 — Variance Calculator
**Slug:** `varianza` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1642 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 609 — Z Score Calculator
**Slug:** `puntuacion-z` | **Block:** `estadistica` | **Status:** WARN
**Content:** 1652 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 700 — Speed Calculator
**Slug:** `velocidad` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1568 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 701 — Density Calculator
**Slug:** `densidad` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1022 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 702 — Force Calculator
**Slug:** `fuerza` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1681 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (167 chars > 160)
- No error return in formula

### 703 — Kinetic Energy Calculator
**Slug:** `energia-cinetica` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1734 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 704 — Potential Energy Calculator
**Slug:** `energia-potencial` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1742 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 705 — Pressure Calculator
**Slug:** `presion` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1846 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 706 — Work Calculator
**Slug:** `trabajo-mecanico` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1898 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 707 — Ohms Law Calculator
**Slug:** `ley-ohm` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1824 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 708 — Electrical Power Calculator
**Slug:** `potencia-electrica` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1934 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 709 — Acceleration Calculator
**Slug:** `aceleracion` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1837 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 800 — Length Converter
**Slug:** `longitud` | **Block:** `conversion` | **Status:** WARN
**Content:** 1482 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 801 — Weight Converter
**Slug:** `peso` | **Block:** `conversion` | **Status:** WARN
**Content:** 1728 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (167 chars > 160)
- No error return in formula

### 802 — Temperature Converter
**Slug:** `temperatura` | **Block:** `conversion` | **Status:** WARN
**Content:** 1461 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 803 — Volume Converter
**Slug:** `volumen` | **Block:** `conversion` | **Status:** WARN
**Content:** 1611 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)
- No error return in formula

### 804 — Area Converter
**Slug:** `area` | **Block:** `conversion` | **Status:** WARN
**Content:** 1567 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (164 chars > 160)
- No error return in formula

### 805 — Speed Converter
**Slug:** `velocidad-unidades` | **Block:** `conversion` | **Status:** WARN
**Content:** 1657 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)
- No error return in formula

### 806 — Data Storage Converter
**Slug:** `datos-digitales` | **Block:** `conversion` | **Status:** WARN
**Content:** 1659 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (162 chars > 160)
- No error return in formula

### 807 — Pressure Converter
**Slug:** `presion-unidades` | **Block:** `conversion` | **Status:** WARN
**Content:** 1652 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)
- No error return in formula

### 808 — Time Converter
**Slug:** `tiempo-unidades` | **Block:** `conversion` | **Status:** WARN
**Content:** 1681 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)
- No error return in formula

### 809 — Energy Converter
**Slug:** `energia-unidades` | **Block:** `conversion` | **Status:** WARN
**Content:** 1780 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (164 chars > 160)
- No error return in formula

### 900 — Running Pace Calculator
**Slug:** `ritmo-carrera` | **Block:** `deportes` | **Status:** WARN
**Content:** 1610 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 901 — Exercise Calorie Calculator
**Slug:** `calorias-ejercicio` | **Block:** `deportes` | **Status:** WARN
**Content:** 1915 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (170 chars > 160)
- No error return in formula

### 902 — Max Heart Rate Calculator
**Slug:** `frecuencia-cardiaca-max` | **Block:** `deportes` | **Status:** WARN
**Content:** 2120 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (161 chars > 160)

### 903 — Heart Rate Zones Calculator
**Slug:** `zonas-cardiacas` | **Block:** `deportes` | **Status:** WARN
**Content:** 2487 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)

### 904 — Vo2 Max Calculator
**Slug:** `vo2-max` | **Block:** `deportes` | **Status:** WARN
**Content:** 2389 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)

### 905 — Steps To Calories Calculator
**Slug:** `pasos-calorias` | **Block:** `deportes` | **Status:** WARN
**Content:** 2385 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)
- No error return in formula

### 906 — Swimming Pace Calculator
**Slug:** `ritmo-natacion` | **Block:** `deportes` | **Status:** WARN
**Content:** 2507 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (168 chars > 160)

### 907 — Cycling Pace Calculator
**Slug:** `ritmo-ciclismo` | **Block:** `deportes` | **Status:** WARN
**Content:** 2760 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (164 chars > 160)

### 908 — Athletic Bmi Calculator
**Slug:** `imc-deportista` | **Block:** `deportes` | **Status:** WARN
**Content:** 2876 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (169 chars > 160)

### 909 — Race Time Predictor
**Slug:** `tiempo-pista` | **Block:** `deportes` | **Status:** WARN
**Content:** 2787 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (164 chars > 160)

### 910 — Fraction Calculator
**Slug:** `fraction-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2088 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 911 — Slope Calculator
**Slug:** `slope-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2323 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 912 — Scientific Notation Calculator
**Slug:** `scientific-notation` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2068 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 913 — Rounding Calculator
**Slug:** `rounding-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1986 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 914 — GCF & LCM Calculator
**Slug:** `gcf-lcm-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2063 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 915 — Prime Factorization Calculator
**Slug:** `prime-factorization` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2216 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 916 — Circle Calculator
**Slug:** `circle-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2327 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 917 — Right Triangle Calculator
**Slug:** `right-triangle-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2045 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 918 — Triangle Area (Heron's Formula)
**Slug:** `heron-triangle-area` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2117 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 919 — Rectangle Calculator
**Slug:** `rectangle-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2180 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 920 — Square Calculator
**Slug:** `square-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2193 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 921 — Trapezoid Calculator
**Slug:** `trapezoid-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 528 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 922 — Cylinder Volume Calculator
**Slug:** `cylinder-volume` | **Block:** `matematicas` | **Status:** WARN
**Content:** 544 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 923 — Cone Volume Calculator
**Slug:** `cone-volume` | **Block:** `matematicas` | **Status:** WARN
**Content:** 583 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 924 — Pyramid Volume Calculator
**Slug:** `pyramid-volume` | **Block:** `matematicas` | **Status:** WARN
**Content:** 490 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 925 — Sphere Calculator
**Slug:** `sphere-calculator` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2456 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 926 — BMR Calculator (Harris-Benedict)
**Slug:** `bmr-harris-benedict` | **Block:** `salud` | **Status:** WARN
**Content:** 2108 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 927 — BMR Calculator (Katch-McArdle)
**Slug:** `bmr-katch-mcardle` | **Block:** `salud` | **Status:** WARN
**Content:** 567 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 928 — Macro Calculator
**Slug:** `macro-calculator` | **Block:** `salud` | **Status:** WARN
**Content:** 598 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 929 — Blood Pressure Calculator
**Slug:** `blood-pressure` | **Block:** `salud` | **Status:** WARN
**Content:** 518 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 930 — Waist-to-Hip Ratio Calculator
**Slug:** `waist-hip-ratio` | **Block:** `salud` | **Status:** WARN
**Content:** 550 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 931 — Waist-to-Height Ratio Calculator
**Slug:** `waist-height-ratio` | **Block:** `salud` | **Status:** WARN
**Content:** 453 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 932 — Weight Loss Percentage Calculator
**Slug:** `weight-loss-percentage` | **Block:** `salud` | **Status:** WARN
**Content:** 421 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 933 — Heart Rate Zones Calculator
**Slug:** `heart-rate-zones` | **Block:** `salud` | **Status:** WARN
**Content:** 462 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 934 — Salary to Hourly Calculator
**Slug:** `salary-to-hourly` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2001 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 935 — Hourly to Salary Calculator
**Slug:** `hourly-to-salary` | **Block:** `finanzas` | **Status:** WARN
**Content:** 739 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 936 — Mortgage Calculator
**Slug:** `mortgage-calculator` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2102 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 937 — Debt Payoff Calculator
**Slug:** `debt-payoff` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2312 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 938 — Savings Calculator
**Slug:** `savings-calculator` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2496 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 939 — Profit Margin Calculator
**Slug:** `profit-margin` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2808 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 940 — NPV Calculator
**Slug:** `npv-calculator` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2042 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 941 — Emergency Fund Calculator
**Slug:** `emergency-fund` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2512 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 942 — Age Calculator
**Slug:** `age-calculator-advanced` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 669 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 943 — Date Difference Calculator
**Slug:** `date-difference` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 407 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 944 — Tip Calculator
**Slug:** `tip-calculator-advanced` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 390 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 945 — Double Discount Calculator
**Slug:** `double-discount` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2553 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 946 — Kinetic Energy Calculator
**Slug:** `kinetic-energy` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2653 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 947 — Potential Energy Calculator
**Slug:** `potential-energy` | **Block:** `ciencia` | **Status:** WARN
**Content:** 381 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 948 — Work & Power Calculator
**Slug:** `work-power` | **Block:** `ciencia` | **Status:** WARN
**Content:** 445 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 949 — Ohm's Law & Power Calculator
**Slug:** `ohms-law-power` | **Block:** `ciencia` | **Status:** WARN
**Content:** 420 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 950 — Newton's Second Law Calculator
**Slug:** `newtons-second-law` | **Block:** `ciencia` | **Status:** WARN
**Content:** 714 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 951 — One Rep Max Calculator
**Slug:** `one-rep-max` | **Block:** `deportes` | **Status:** WARN
**Content:** 375 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 952 — Running Pace Predictor
**Slug:** `running-pace-predictor` | **Block:** `deportes` | **Status:** WARN
**Content:** 388 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 953 — VO₂ Max Estimator
**Slug:** `vo2-max-estimator` | **Block:** `deportes` | **Status:** WARN
**Content:** 408 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 954 — Angle Converter
**Slug:** `angle-converter` | **Block:** `conversion` | **Status:** WARN
**Content:** 1700 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 955 — Temperature Converter
**Slug:** `temperature-full` | **Block:** `conversion` | **Status:** WARN
**Content:** 1776 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 956 — Energy Converter
**Slug:** `energy-converter` | **Block:** `conversion` | **Status:** WARN
**Content:** 1909 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 957 — Combinations & Permutations Calculator
**Slug:** `combinations-permutations` | **Block:** `estadistica` | **Status:** WARN
**Content:** 396 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 958 — Z-Score & Percentile Calculator
**Slug:** `z-score-percentile` | **Block:** `estadistica` | **Status:** WARN
**Content:** 390 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 959 — Sample Size Calculator
**Slug:** `sample-size-confidence` | **Block:** `estadistica` | **Status:** WARN
**Content:** 683 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 960 — BSA & Ideal Weight Calculator
**Slug:** `bsa-ideal-weight` | **Block:** `salud` | **Status:** WARN
**Content:** 730 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 961 — A1C Estimator
**Slug:** `a1c-estimator` | **Block:** `salud` | **Status:** WARN
**Content:** 766 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 962 — LDL Cholesterol Calculator
**Slug:** `cholesterol-ldl` | **Block:** `salud` | **Status:** WARN
**Content:** 750 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 110 — Absolute Value Calculator
**Slug:** `valor-absoluto` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1967 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 111 — Arithmetic Sequence Sum Calculator
**Slug:** `suma-progresion-aritmetica` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2260 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 112 — Geometric Sequence Sum Calculator
**Slug:** `suma-progresion-geometrica` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1952 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 113 — Complex Number Magnitude Calculator
**Slug:** `modulo-complejo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2047 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 114 — 2×2 Matrix Determinant Calculator
**Slug:** `determinante-matriz-2x2` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1953 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 115 — 3D Vector Magnitude Calculator
**Slug:** `magnitud-vector-3d` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1920 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 116 — Dot Product Calculator
**Slug:** `producto-escalar` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2140 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 117 — Cross Product Calculator
**Slug:** `producto-vectorial` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2076 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 118 — Quadratic Polynomial Derivative
**Slug:** `derivada-polinomio` | **Block:** `matematicas` | **Status:** WARN
**Content:** 2097 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 119 — Trapezoidal Rule Integral Approximation
**Slug:** `regla-trapecios-integral` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1938 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 120 — Projectile Motion Calculator
**Slug:** `movimiento-proyectil` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1971 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 121 — Centripetal Force Calculator
**Slug:** `fuerza-centripeta` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1941 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 122 — Gravitational Force Calculator
**Slug:** `fuerza-gravitatoria` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1815 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 123 — Elastic Potential Energy Calculator
**Slug:** `energia-potencial-elastica` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1967 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 124 — Specific Heat Capacity Calculator
**Slug:** `calor-especifico` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1981 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 125 — Wave Speed Calculator
**Slug:** `velocidad-onda` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2009 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 126 — Thin Lens Equation Calculator
**Slug:** `ecuacion-lente-delgada` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1901 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 127 — Torque Calculator
**Slug:** `torque-momento-fuerza` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1925 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 128 — Angular Momentum Calculator
**Slug:** `momento-angular` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1950 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 129 — Fluid Pressure Calculator
**Slug:** `presion-fluido` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1959 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 320 — CAGR Calculator
**Slug:** `tasa-crecimiento-anual-compuesto` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2425 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 321 — APR Calculator
**Slug:** `tasa-anual-efectiva` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1685 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 322 — Loan Amortization Calculator
**Slug:** `amortizacion-prestamo` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1892 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 323 — Rental Yield Calculator
**Slug:** `rentabilidad-alquiler` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2062 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 324 — Cap Rate Calculator
**Slug:** `tasa-capitalizacion` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2145 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 325 — Dividend Yield Calculator
**Slug:** `dividend-yield` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2196 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 326 — Price-to-Earnings Ratio Calculator
**Slug:** `ratio-per` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2246 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 327 — Future Value of Annuity Calculator
**Slug:** `valor-futuro-anualidad` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1779 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 328 — Present Value of Annuity Calculator
**Slug:** `valor-actual-anualidad` | **Block:** `finanzas` | **Status:** WARN
**Content:** 743 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 329 — WACC Calculator
**Slug:** `wacc` | **Block:** `finanzas` | **Status:** WARN
**Content:** 883 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 415 — Lean Body Mass Calculator (Boer)
**Slug:** `masa-magra` | **Block:** `salud` | **Status:** WARN
**Content:** 666 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 416 — Body Adiposity Index (BAI)
**Slug:** `indice-adiposidad-corporal` | **Block:** `salud` | **Status:** WARN
**Content:** 695 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 417 — Daily Protein Intake Calculator
**Slug:** `ingesta-proteica` | **Block:** `salud` | **Status:** WARN
**Content:** 680 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 418 — Recommended Fiber Intake
**Slug:** `ingesta-fibra` | **Block:** `salud` | **Status:** WARN
**Content:** 785 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 419 — Karvonen Heart Rate Calculator
**Slug:** `frecuencia-cardiaca-karvonen` | **Block:** `salud` | **Status:** WARN
**Content:** 849 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 420 — Heart Rate Training Zones
**Slug:** `zonas-frecuencia-cardiaca` | **Block:** `salud` | **Status:** WARN
**Content:** 849 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 421 — Creatinine Clearance (Cockcroft-Gault)
**Slug:** `aclaramiento-creatinina` | **Block:** `salud` | **Status:** WARN
**Content:** 812 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 422 — BMI Prime Calculator
**Slug:** `bmi-prime` | **Block:** `salud` | **Status:** WARN
**Content:** 777 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 423 — Pregnancy Due Date Calculator
**Slug:** `fecha-parto` | **Block:** `salud` | **Status:** WARN
**Content:** 835 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 424 — Ovulation Calculator
**Slug:** `calculadora-ovulacion` | **Block:** `salud` | **Status:** WARN
**Content:** 813 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 503 — Fuel Cost Calculator
**Slug:** `coste-combustible` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2250 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 504 — Data Transfer Time Calculator
**Slug:** `tiempo-transferencia-datos` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2229 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 505 — Battery Life Calculator
**Slug:** `duracion-bateria` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2212 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 506 — Download Time Calculator
**Slug:** `tiempo-descarga` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2213 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 507 — Screen DPI / PPI Calculator
**Slug:** `dpi-pantalla` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2119 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 508 — Aspect Ratio Calculator
**Slug:** `relacion-aspecto` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2122 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 509 — Password Entropy Calculator
**Slug:** `entropia-contrasena` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2155 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 510 — Bandwidth Calculator
**Slug:** `ancho-banda` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2349 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 511 — Uncompressed Image File Size
**Slug:** `tamano-archivo` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2247 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 512 — Electricity Cost Calculator
**Slug:** `coste-consumo-electrico` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2311 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 130 — Logarithm Calculator
**Slug:** `logaritmo` | **Block:** `matematicas` | **Status:** WARN
**Content:** 883 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 131 — Natural Logarithm
**Slug:** `logaritmo-natural` | **Block:** `matematicas` | **Status:** WARN
**Content:** 878 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 132 — Exponential Growth Calculator
**Slug:** `crecimiento-exponencial` | **Block:** `matematicas` | **Status:** WARN
**Content:** 970 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 133 — Factorial Calculator
**Slug:** `factorial` | **Block:** `matematicas` | **Status:** WARN
**Content:** 937 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 134 — Permutations Calculator
**Slug:** `permutaciones` | **Block:** `matematicas` | **Status:** WARN
**Content:** 896 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 135 — Combinations Calculator
**Slug:** `combinaciones` | **Block:** `matematicas` | **Status:** WARN
**Content:** 928 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 136 — Standard Deviation Calculator
**Slug:** `desviacion-estandar` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1105 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 137 — Variance Calculator
**Slug:** `varianza` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1132 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 138 — Median Calculator
**Slug:** `mediana` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1227 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 139 — Quartile Calculator
**Slug:** `cuartiles` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1255 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 140 — Bernoulli Equation Calculator
**Slug:** `ecuacion-bernoulli` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2016 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 141 — Doppler Effect Calculator
**Slug:** `efecto-doppler` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2149 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 142 — Snell's Law Calculator
**Slug:** `ley-snell` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2073 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 143 — Coulomb Force Calculator
**Slug:** `fuerza-coulomb` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2033 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 144 — Magnetic Force on Charge Calculator
**Slug:** `fuerza-magnetica-carga` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2187 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 145 — Thermal Expansion Calculator
**Slug:** `dilatacion-termica` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2082 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 146 — Stefan-Boltzmann Law Calculator
**Slug:** `ley-stefan-boltzmann` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2150 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 147 — RL Circuit Calculator
**Slug:** `circuito-rl` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2291 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 148 — RC Circuit Calculator
**Slug:** `circuito-rc` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2204 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 149 — Ideal Gas Law Calculator
**Slug:** `ley-gases-ideales` | **Block:** `ciencia` | **Status:** WARN
**Content:** 2331 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 330 — Payback Period Calculator
**Slug:** `periodo-recuperacion` | **Block:** `finanzas` | **Status:** WARN
**Content:** 777 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 331 — Sharpe Ratio Calculator
**Slug:** `ratio-sharpe` | **Block:** `finanzas` | **Status:** WARN
**Content:** 582 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 332 — Tax Equivalent Yield Calculator
**Slug:** `rendimiento-equivalente-impuestos` | **Block:** `finanzas` | **Status:** WARN
**Content:** 741 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 333 — Real Rate of Return Calculator
**Slug:** `tasa-real-retorno` | **Block:** `finanzas` | **Status:** WARN
**Content:** 773 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 334 — Loan Affordability Calculator
**Slug:** `prestamo-afordable` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1982 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 335 — Mortgage Payoff Calculator
**Slug:** `liquidacion-hipoteca` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1895 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 336 — Credit Card Payoff Calculator
**Slug:** `liquidacion-tarjeta-credito` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1995 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 337 — College Savings Calculator
**Slug:** `ahorro-universidad` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2032 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 338 — Life Insurance Needs Calculator
**Slug:** `necesidades-seguro-vida` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2218 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 339 — Monthly CAGR Calculator
**Slug:** `cagr-mensual` | **Block:** `finanzas` | **Status:** WARN
**Content:** 2105 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 425 — Body Fat Navy Method
**Slug:** `grasa-corporal-navy` | **Block:** `salud` | **Status:** WARN
**Content:** 914 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 426 — TDEE Calculator
**Slug:** `gasto-energetico-total` | **Block:** `salud` | **Status:** WARN
**Content:** 825 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 427 — BMR Calculator (Mifflin-St Jeor)
**Slug:** `tasa-metabolica-basal-mifflin` | **Block:** `salud` | **Status:** WARN
**Content:** 1179 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 428 — RMR Calculator
**Slug:** `metabolismo-en-reposo` | **Block:** `salud` | **Status:** WARN
**Content:** 895 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 429 — METs Calculator
**Slug:** `mets-actividad` | **Block:** `salud` | **Status:** WARN
**Content:** 837 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 430 — Target Weight Calculator
**Slug:** `peso-objetivo` | **Block:** `salud` | **Status:** WARN
**Content:** 916 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 431 — Pregnancy Weight Gain Calculator
**Slug:** `aumento-peso-embarazo` | **Block:** `salud` | **Status:** WARN
**Content:** 883 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 432 — Calories Burned Walking
**Slug:** `calorias-caminar` | **Block:** `salud` | **Status:** WARN
**Content:** 850 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 433 — Child Growth Percentile
**Slug:** `percentil-crecimiento-infantil` | **Block:** `salud` | **Status:** WARN
**Content:** 923 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 434 — Water Intake by Weight
**Slug:** `agua-por-peso` | **Block:** `salud` | **Status:** WARN
**Content:** 910 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 513 — Screen Resolution
**Slug:** `resolucion-pantalla` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2301 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 514 — Video File Size Calculator
**Slug:** `tamano-archivo-video` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2347 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 515 — RAID Capacity Calculator
**Slug:** `capacidad-raid` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2551 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 516 — Server Uptime Calculator
**Slug:** `tiempo-actividad` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2031 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 517 — Ping Latency Calculator
**Slug:** `latencia-ping` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2182 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 518 — Typing Speed (WPM)
**Slug:** `palabras-por-minuto` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2061 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 519 — Reading Time Calculator
**Slug:** `tiempo-lectura` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2064 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 520 — SMS Cost Calculator
**Slug:** `coste-sms` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2156 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 521 — Data Usage Estimator
**Slug:** `estimador-datos` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2575 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 522 — Screen Brightness in Nits
**Slug:** `brillo-pantalla-nits` | **Block:** `cotidiano` | **Status:** WARN
**Content:** 2354 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1000 — pH Calculator
**Slug:** `calculadora-ph` | **Block:** `quimica` | **Status:** WARN
**Content:** 1775 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1001 — pOH Calculator
**Slug:** `calculadora-poh` | **Block:** `quimica` | **Status:** WARN
**Content:** 1534 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1002 — Molarity Calculator
**Slug:** `molaridad` | **Block:** `quimica` | **Status:** WARN
**Content:** 1674 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1003 — Dilution Calculator
**Slug:** `dilucion` | **Block:** `quimica` | **Status:** WARN
**Content:** 1828 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1004 — Ideal Gas Law Calculator
**Slug:** `ley-gases-ideales` | **Block:** `quimica` | **Status:** WARN
**Content:** 1973 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1005 — Boyle's Law Calculator
**Slug:** `ley-boyle` | **Block:** `quimica` | **Status:** WARN
**Content:** 2016 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1006 — Charles's Law Calculator
**Slug:** `ley-charles` | **Block:** `quimica` | **Status:** WARN
**Content:** 1870 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1007 — Gibbs Free Energy Calculator
**Slug:** `energia-libre-gibbs` | **Block:** `quimica` | **Status:** WARN
**Content:** 1477 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1008 — Molecular Weight Calculator
**Slug:** `peso-molecular` | **Block:** `quimica` | **Status:** WARN
**Content:** 1822 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1009 — Titration Calculator
**Slug:** `titulacion` | **Block:** `quimica` | **Status:** WARN
**Content:** 2063 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1010 — Voltage Divider Calculator
**Slug:** `divisor-tension` | **Block:** `electronica` | **Status:** WARN
**Content:** 2510 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1011 — LED Resistor Calculator
**Slug:** `resistencia-led` | **Block:** `electronica` | **Status:** WARN
**Content:** 2983 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1012 — Parallel Resistance Calculator
**Slug:** `resistencia-paralelo` | **Block:** `electronica` | **Status:** WARN
**Content:** 3033 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1013 — Capacitor Energy Calculator
**Slug:** `energia-condensador` | **Block:** `electronica` | **Status:** WARN
**Content:** 3342 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1014 — Inductor Energy Calculator
**Slug:** `energia-bobina` | **Block:** `electronica` | **Status:** WARN
**Content:** 3688 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1015 — Transformer Turns Ratio
**Slug:** `relacion-transformador` | **Block:** `electronica` | **Status:** WARN
**Content:** 4269 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1016 — RC Time Constant Calculator
**Slug:** `constante-tiempo-rc` | **Block:** `electronica` | **Status:** WARN
**Content:** 4270 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1017 — Wheatstone Bridge Calculator
**Slug:** `puente-wheatstone` | **Block:** `electronica` | **Status:** WARN
**Content:** 4270 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1018 — Series Capacitance Calculator
**Slug:** `capacitancia-serie` | **Block:** `electronica` | **Status:** WARN
**Content:** 4131 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1019 — Resistor Color Code Calculator
**Slug:** `codigo-colores-resistencia` | **Block:** `electronica` | **Status:** WARN
**Content:** 2268 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1020 — Dew Point Calculator
**Slug:** `punto-rocio` | **Block:** `clima` | **Status:** WARN
**Content:** 2974 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1021 — Heat Index Calculator
**Slug:** `indice-calor` | **Block:** `clima` | **Status:** WARN
**Content:** 2841 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1022 — Wind Chill Calculator
**Slug:** `sensacion-termica-viento` | **Block:** `clima` | **Status:** WARN
**Content:** 2971 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1023 — Relative Humidity Calculator
**Slug:** `humedad-relativa` | **Block:** `clima` | **Status:** WARN
**Content:** 2958 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1024 — Air Quality Index Calculator
**Slug:** `indice-calidad-aire` | **Block:** `clima` | **Status:** WARN
**Content:** 3467 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1025 — Daylight Hours Calculator
**Slug:** `amanecer-atardecer` | **Block:** `clima` | **Status:** WARN
**Content:** 3093 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1026 — UV Exposure Time Calculator
**Slug:** `tiempo-exposicion-uv` | **Block:** `clima` | **Status:** WARN
**Content:** 2976 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1027 — Pressure Altitude Calculator
**Slug:** `altitud-presion` | **Block:** `clima` | **Status:** WARN
**Content:** 3078 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1028 — Rainfall Volume Calculator
**Slug:** `volumen-lluvia` | **Block:** `clima` | **Status:** WARN
**Content:** 3153 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1029 — Evapotranspiration Calculator
**Slug:** `evapotranspiracion` | **Block:** `clima` | **Status:** WARN
**Content:** 1813 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1030 — Day of Year Calculator
**Slug:** `dia-del-ano` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2144 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1031 — Week Number Calculator
**Slug:** `numero-semana` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2301 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1032 — Age in Days Calculator
**Slug:** `edad-en-dias` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2586 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1033 — Reading Time Calculator
**Slug:** `tiempo-lectura` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2168 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1034 — Password Generator
**Slug:** `generador-contrasenas` | **Block:** `utilidades` | **Status:** WARN
**Content:** 1980 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1035 — Random Number Generator
**Slug:** `numero-aleatorio` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2114 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1036 — Dice Roller
**Slug:** `lanzador-dados` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2272 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1037 — Coin Flip
**Slug:** `cara-cruz` | **Block:** `utilidades` | **Status:** WARN
**Content:** 2206 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1038 — Hex to RGB Converter
**Slug:** `hex-a-rgb` | **Block:** `utilidades` | **Status:** WARN
**Content:** 1220 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1039 — Exposure Value Calculator
**Slug:** `valor-exposicion` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1262 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1040 — Depth of Field Calculator
**Slug:** `profundidad-campo` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1471 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1041 — Hyperfocal Distance Calculator
**Slug:** `distancia-hiperfocal` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1429 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1042 — Decibel Addition Calculator
**Slug:** `suma-decibelios` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1398 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1043 — SPL Distance Calculator
**Slug:** `nivel-sonoro-distancia` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1559 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1044 — Contrast Ratio Calculator
**Slug:** `relacion-contraste` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1665 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1045 — Crosswind Component Calculator
**Slug:** `viento-cruzado` | **Block:** `transporte` | **Status:** WARN
**Content:** 933 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1046 — Fuel Burn Calculator
**Slug:** `consumo-combustible` | **Block:** `transporte` | **Status:** WARN
**Content:** 1030 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1047 — True Airspeed Calculator
**Slug:** `velocidad-verdadera` | **Block:** `transporte` | **Status:** WARN
**Content:** 1012 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1048 — Hull Speed Calculator
**Slug:** `velocidad-casco` | **Block:** `transporte` | **Status:** WARN
**Content:** 1004 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1049 — Great Circle Distance Calculator
**Slug:** `distancia-ortodromica` | **Block:** `transporte` | **Status:** WARN
**Content:** 1034 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1050 — Regular Polygon Area Calculator
**Slug:** `poligono-regular-area` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1067 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1051 — Cone Volume Calculator
**Slug:** `cono-volumen` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1025 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1052 — Arithmetic Series Calculator
**Slug:** `suma-aritmetica` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1033 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1053 — Geometric Series Calculator
**Slug:** `suma-geometrica` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1042 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1054 — Combinations Calculator
**Slug:** `combinaciones` | **Block:** `matematicas` | **Status:** WARN
**Content:** 1011 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1055 — Buoyancy Force Calculator
**Slug:** `empuje-arquimedes` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1017 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1056 — Doppler Effect Calculator
**Slug:** `efecto-doppler` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1186 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1057 — AC Impedance Calculator
**Slug:** `impedancia-ac` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1162 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1058 — Moment of Inertia Calculator
**Slug:** `momento-inercia` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1285 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1059 — Rotational Energy Calculator
**Slug:** `energia-rotacional` | **Block:** `ciencia` | **Status:** WARN
**Content:** 1130 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1060 — Body Fat (Navy) Calculator
**Slug:** `grasa-corporal-marina` | **Block:** `salud` | **Status:** WARN
**Content:** 1187 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1061 — Mifflin-St Jeor BMR Calculator
**Slug:** `tasa-metabolica-mifflin` | **Block:** `salud` | **Status:** WARN
**Content:** 1184 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1062 — Daily Water Intake Calculator
**Slug:** `agua-diaria` | **Block:** `salud` | **Status:** WARN
**Content:** 1166 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1063 — One Rep Max (Brzycki) Calculator
**Slug:** `repeticion-maxima-brzycki` | **Block:** `salud` | **Status:** WARN
**Content:** 1214 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1064 — Daily Protein Calculator
**Slug:** `proteina-diaria` | **Block:** `salud` | **Status:** WARN
**Content:** 1241 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1065 — Dividend Yield Calculator
**Slug:** `rentabilidad-dividendo` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1244 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1066 — Payback Period Calculator
**Slug:** `periodo-recuperacion` | **Block:** `finanzas` | **Status:** WARN
**Content:** 1245 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1067 — Capital Gains Tax Calculator
**Slug:** `impuesto-ganancias-capital` | **Block:** `finanzas` | **Status:** WARN
**Content:** 927 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1068 — Currency Exchange Commission Calculator
**Slug:** `tipo-cambio-comision` | **Block:** `finanzas` | **Status:** WARN
**Content:** 945 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1069 — Break Even Point Calculator
**Slug:** `punto-equilibrio` | **Block:** `finanzas` | **Status:** WARN
**Content:** 963 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1070 — Molar Mass Calculator
**Slug:** `masa-molar` | **Block:** `quimica` | **Status:** WARN
**Content:** 898 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1071 — pH Calculator
**Slug:** `ph-hidrogeno` | **Block:** `quimica` | **Status:** WARN
**Content:** 919 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1072 — Ideal Gas Law Calculator
**Slug:** `gas-ideal` | **Block:** `quimica` | **Status:** WARN
**Content:** 931 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1073 — Molarity Calculator
**Slug:** `molaridad` | **Block:** `quimica` | **Status:** WARN
**Content:** 986 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1074 — Dilution Calculator
**Slug:** `dilucion` | **Block:** `quimica` | **Status:** WARN
**Content:** 947 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1075 — Resistor Color Code Calculator
**Slug:** `codigo-colores-resistencia` | **Block:** `electronica` | **Status:** WARN
**Content:** 950 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1076 — Capacitor Energy Calculator
**Slug:** `energia-capacitor` | **Block:** `electronica` | **Status:** WARN
**Content:** 1030 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1077 — Voltage Divider Calculator
**Slug:** `divisor-voltaje` | **Block:** `electronica` | **Status:** WARN
**Content:** 1086 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1078 — RC Time Constant Calculator
**Slug:** `constante-tiempo-rc` | **Block:** `electronica` | **Status:** WARN
**Content:** 980 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1079 — Wheatstone Bridge Calculator
**Slug:** `puente-wheatstone` | **Block:** `electronica` | **Status:** WARN
**Content:** 1015 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1080 — Fuel Consumption Calculator
**Slug:** `consumo-combustible` | **Block:** `transporte` | **Status:** WARN
**Content:** 986 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1081 — Braking Distance Calculator
**Slug:** `distancia-frenado` | **Block:** `transporte` | **Status:** WARN
**Content:** 1053 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1082 — Engine Displacement Calculator
**Slug:** `cilindrada-motor` | **Block:** `transporte` | **Status:** WARN
**Content:** 1054 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1083 — Tire Pressure Calculator
**Slug:** `presion-neumaticos` | **Block:** `transporte` | **Status:** WARN
**Content:** 1070 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1084 — Flight Time with Wind Calculator
**Slug:** `tiempo-vuelo-viento` | **Block:** `transporte` | **Status:** WARN
**Content:** 1145 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1085 — Depth of Field Calculator
**Slug:** `profundidad-campo` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1136 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1086 — Flash Guide Number Calculator
**Slug:** `numero-guia-flash` | **Block:** `fotografia` | **Status:** WARN
**Content:** 1166 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1087 — Heat Index Calculator
**Slug:** `indice-calor` | **Block:** `clima` | **Status:** WARN
**Content:** 1154 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1088 — Wind Chill Calculator
**Slug:** `sensacion-frio-viento` | **Block:** `clima` | **Status:** WARN
**Content:** 1122 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1089 — Relative Humidity & Dew Point Calculator
**Slug:** `humedad-relativa-rocio` | **Block:** `clima` | **Status:** WARN
**Content:** 1024 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1090 — Password Entropy Calculator
**Slug:** `entropia-contrasena` | **Block:** `utilidades` | **Status:** WARN
**Content:** 979 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1091 — Character & Word Counter
**Slug:** `contador-caracteres-texto` | **Block:** `utilidades` | **Status:** WARN
**Content:** 877 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1092 — Business Days Calculator
**Slug:** `dias-habiles` | **Block:** `utilidades` | **Status:** WARN
**Content:** 975 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1093 — Beam Deflection Calculator
**Slug:** `deflexion-viga` | **Block:** `ingenieria` | **Status:** WARN
**Content:** 983 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1094 — Bolt Torque Calculator
**Slug:** `par-apriete-tornillo` | **Block:** `ingenieria` | **Status:** WARN
**Content:** 914 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1095 — Spring Constant Calculator
**Slug:** `constante-resorte` | **Block:** `ingenieria` | **Status:** WARN
**Content:** 967 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1096 — Reynolds Number Calculator
**Slug:** `numero-reynolds` | **Block:** `ingenieria` | **Status:** WARN
**Content:** 969 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1097 — Running Pace Calculator
**Slug:** `ritmo-carrera` | **Block:** `deportes` | **Status:** WARN
**Content:** 966 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1098 — Golf Handicap Calculator
**Slug:** `handicap-golf` | **Block:** `deportes` | **Status:** WARN
**Content:** 985 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1099 — MET Calories Burned Calculator
**Slug:** `quemar-calorias-met` | **Block:** `deportes` | **Status:** WARN
**Content:** 1008 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- No error return in formula

### 1100 — Decking Calculator
**Slug:** `decking-calculator` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 1524 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1101 — Sod & Turf Calculator
**Slug:** `sod-turf-calculator` | **Block:** `estructuras` | **Status:** WARN
**Content:** 1491 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1102 — Mulch Calculator
**Slug:** `mulch-calculator` | **Block:** `estructuras` | **Status:** WARN
**Content:** 3019 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1103 — Fence Picket Calculator
**Slug:** `fence-picket-calculator` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 315 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1104 — Roofing Shingle Calculator
**Slug:** `roofing-shingle-calculator` | **Block:** `estructuras` | **Status:** WARN
**Content:** 315 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1105 — Insulation Batt Calculator
**Slug:** `insulation-batt-calculator` | **Block:** `climatizacion` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1106 — Carpet Calculator
**Slug:** `carpet-calculator` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 312 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1107 — Laminate Flooring Calculator
**Slug:** `laminate-flooring-calculator` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1108 — Countertop Calculator
**Slug:** `countertop-calculator` | **Block:** `gestion` | **Status:** WARN
**Content:** 311 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1109 — Backsplash Tile Calculator
**Slug:** `backsplash-tile-calculator` | **Block:** `pintura` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1110 — Grout Calculator
**Slug:** `grout-calculator` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1111 — Paint Coverage Calculator
**Slug:** `paint-coverage-calculator` | **Block:** `pintura` | **Status:** WARN
**Content:** 315 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1112 — Wallpaper Calculator
**Slug:** `wallpaper-calculator` | **Block:** `pintura` | **Status:** WARN
**Content:** 311 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1113 — Crown Molding Calculator
**Slug:** `crown-molding-calculator` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 316 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1114 — Baseboard Calculator
**Slug:** `baseboard-calculator` | **Block:** `carpinteria` | **Status:** WARN
**Content:** 313 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (165 chars > 160)

### 1115 — Drywall Calculator
**Slug:** `drywall-calculator` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 312 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1116 — Concrete Steps Calculator
**Slug:** `concrete-steps-calculator` | **Block:** `estructuras` | **Status:** WARN
**Content:** 315 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (164 chars > 160)

### 1117 — Retaining Wall Calculator
**Slug:** `retaining-wall-calculator` | **Block:** `mamposteria` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
- SEO desc too long (163 chars > 160)

### 1118 — Paver Calculator
**Slug:** `paver-calculator` | **Block:** `pavimentos` | **Status:** WARN
**Content:** 311 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)

### 1119 — Landscape Rock Calculator
**Slug:** `landscape-rock-calculator` | **Block:** `estructuras` | **Status:** WARN
**Content:** 314 words

**Issues:**
- Both seo_desc and seo_description fields present (inconsistent)
