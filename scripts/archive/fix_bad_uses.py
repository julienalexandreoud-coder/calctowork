#!/usr/bin/env python3
"""
Fix 'everyday math problems' placeholder content in auto-generated EN articles.
Detects calculator category from name/formula and replaces bad use-case items.
"""
import os
import re
import sys

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'en')

# Category detection: keyword -> (uses_list, heading)
CATEGORY_RULES = [
    # Plumbing / Tiling
    (["tile", "grout", "adhesive"],
     ["calculating adhesive and grout quantities for floor and wall tiling projects",
      "estimating materials for bathroom, kitchen, and outdoor tiling renovations",
      "planning material orders to minimise waste on large tiling contracts",
      "comparing coverage differences between standard and large-format tiles"],
     "Practical uses in tiling and renovation projects"),

    (["pipe", "drainage", "pex", "copper pipe", "water supply", "plumbing"],
     ["sizing pipes for residential and commercial water supply systems",
      "calculating flow rates and checking pressure-drop compliance",
      "planning new plumbing layouts or validating existing ones",
      "estimating material quantities before ordering for renovations"],
     "Practical uses in plumbing projects"),

    (["water pressure", "water tank", "pool filtration", "drip irrigation",
      "trap", "drain", "water supply connection"],
     ["planning residential water pressure and tank sizing",
      "estimating irrigation requirements for gardens and sports fields",
      "sizing filtration systems for swimming pools and water features",
      "calculating drain and trap sizes to comply with building codes"],
     "Practical uses in water systems and drainage"),

    (["water heater", "boiler", "radiator", "underfloor heating"],
     ["sizing water heaters and boilers for residential hot-water demand",
      "calculating radiator output and room heat load",
      "planning underfloor heating circuits for new builds and renovations",
      "verifying heating system capacity before installation"],
     "Practical uses in heating and hot-water systems"),

    # Electrical
    (["cable cross-section", "voltage drop", "electrical cable"],
     ["sizing cables to comply with IEC and NEC wiring regulations",
      "calculating voltage drop over long cable runs in industrial installations",
      "planning electrical wiring for new residential and commercial builds",
      "selecting the correct cable gauge to prevent overheating and energy loss"],
     "Practical uses in electrical installations"),

    (["led lighting", "lumen", "light points", "lighting"],
     ["designing lighting layouts to meet lux requirements for workspaces",
      "calculating the number of LED fittings needed per room",
      "planning energy-efficient lighting upgrades in commercial buildings",
      "verifying compliance with building-regulation illumination standards"],
     "Practical uses in lighting design"),

    (["electrical panel", "circuit breaker", "distribution board"],
     ["sizing electrical panels and consumer units for new builds",
      "calculating total connected load and diversity factors",
      "planning circuit breaker ratings to comply with electrical codes",
      "verifying that existing panels can handle additional loads"],
     "Practical uses in electrical panel design"),

    (["solar panel", "photovoltaic", "pv"],
     ["sizing residential and commercial solar PV systems",
      "estimating annual energy generation and payback period",
      "calculating the number of solar panels needed for off-grid living",
      "planning roof space requirements and panel orientation"],
     "Practical uses in solar energy planning"),

    (["battery storage", "battery life", "battery"],
     ["sizing battery storage systems for solar installations",
      "estimating backup autonomy time for off-grid and UPS systems",
      "calculating battery capacity for electric vehicles and mobility aids",
      "planning battery bank sizing for remote power applications"],
     "Practical uses in battery and energy storage"),

    (["three-phase", "three phase", "earthing", "grounding", "power factor"],
     ["calculating three-phase power in industrial and commercial electrical systems",
      "sizing transformers and generators for factory loads",
      "verifying earthing and fault-protection compliance",
      "planning power-factor correction to reduce energy bills"],
     "Practical uses in industrial electrical engineering"),

    (["electricity consumption", "electricity cost", "energy consumption"],
     ["estimating monthly electricity bills before they arrive",
      "identifying the highest-consuming appliances in a home or office",
      "planning energy audits and efficiency improvement programmes",
      "comparing the running costs of different appliances or tariff plans"],
     "Practical uses in energy monitoring and cost control"),

    # HVAC
    (["btu", "air conditioning", "cooling load"],
     ["sizing air conditioning units for bedrooms, offices, and server rooms",
      "calculating cooling loads for building permit applications",
      "comparing BTU outputs of different AC models for a given space",
      "planning multi-split systems for commercial buildings"],
     "Practical uses in air conditioning design"),

    (["air duct", "duct sizing", "grilles", "diffusers", "ventilation", "hvac"],
     ["designing HVAC duct layouts for new residential and commercial builds",
      "calculating air-flow rates to meet indoor-air-quality standards",
      "sizing grilles and diffusers for balanced air distribution",
      "verifying duct pressure drops and fan sizing"],
     "Practical uses in HVAC and ventilation design"),

    (["heat pump", "cop", "eer", "refrigerant"],
     ["evaluating heat pump efficiency and seasonal performance factors",
      "calculating refrigerant charge weights for new installations",
      "comparing COP and EER values when selecting HVAC equipment",
      "sizing heat pumps to meet heating and cooling demand"],
     "Practical uses in heat pump and refrigeration engineering"),

    # Carpentry / Metalwork
    (["window", "pvc window", "aluminium window"],
     ["estimating glass and frame areas for window quotations",
      "calculating the number of windows needed per elevation",
      "planning glass specifications and thermal performance",
      "budgeting window replacement or new-build glazing packages"],
     "Practical uses in window and glazing projects"),

    (["door", "sliding door", "interior door"],
     ["estimating door quantities and sizes for construction projects",
      "calculating door-frame materials for fit-out contracts",
      "comparing different door types by cost per opening",
      "planning accessibility compliance for building regulations"],
     "Practical uses in door and joinery projects"),

    (["staircase", "wooden stair", "metal railing", "railing"],
     ["calculating stair dimensions to comply with building codes",
      "estimating timber or metal quantities for staircase construction",
      "planning railing post spacing and baluster counts",
      "verifying rise and run ratios for safe staircase design"],
     "Practical uses in staircase and railing design"),

    (["metal structure", "metal door", "gate", "steel"],
     ["estimating steel section weights and material costs",
      "calculating loads and deflections in light steel structures",
      "planning metal-door and gate fabrication for security applications",
      "budgeting structural metalwork for commercial and industrial projects"],
     "Practical uses in metalwork and structural engineering"),

    (["glass"],
     ["estimating glass quantities and weights for glazing contracts",
      "calculating glass area for thermal or acoustic performance checks",
      "planning glass cutting lists to minimise waste",
      "budgeting glazing for shopfronts, balustrades, and facades"],
     "Practical uses in glazing and glass fitting"),

    # Painting and Finishes
    (["paint", "emulsion", "enamel", "varnish", "primer", "sealer", "filler", "putty"],
     ["estimating paint quantities to avoid under-ordering or overbuying",
      "calculating coverage for multi-coat systems on interior and exterior surfaces",
      "planning primer and sealer requirements before topcoat application",
      "budgeting decorating materials for renovation and fit-out projects"],
     "Practical uses in painting and decorating"),

    (["wallpaper"],
     ["calculating the number of wallpaper rolls needed for a room",
      "planning pattern-repeat allowances to minimise waste",
      "estimating wallpaper costs for renovation and interior design projects",
      "comparing roll coverage for different wallpaper widths and repeat sizes"],
     "Practical uses in wallpapering projects"),

    (["textured finish", "sandpaper"],
     ["estimating finishing materials for plastered and rendered walls",
      "planning sanding schedules for wood floors and furniture",
      "calculating textured-coating coverage for external facades",
      "budgeting surface preparation for painting and decorating projects"],
     "Practical uses in surface preparation and finishing"),

    # Construction Business
    (["hourly rate", "profit margin", "break-even", "roi", "amortisation",
      "workforce cost", "labour cost", "wage"],
     ["calculating break-even points and profit margins for construction quotes",
      "estimating workforce costs and hourly rates for contract pricing",
      "analysing tool and machinery ROI before purchase decisions",
      "tracking amortisation of plant and equipment for tax and accounting"],
     "Practical uses in construction business management"),

    (["fuel cost", "vehicle", "travel", "subsistence", "transport"],
     ["estimating site travel and fuel costs for construction project budgets",
      "calculating vehicle running costs for fleet management",
      "planning subsistence allowances for workers on remote sites",
      "comparing the cost-efficiency of different transport options"],
     "Practical uses in site logistics and transport costing"),

    (["skip rental", "scaffolding", "cleaning", "insurance", "ppe", "signage", "permit"],
     ["estimating skip hire and waste-removal costs for demolition projects",
      "calculating scaffolding rental costs for building facades",
      "budgeting site safety equipment, signage, and insurance premiums",
      "estimating post-construction cleaning requirements and costs"],
     "Practical uses in construction site management"),

    (["vat", "tax", "budget", "renovation budget", "planning"],
     ["preparing accurate construction budgets for client proposals",
      "calculating VAT and tax liabilities on construction contracts",
      "estimating total project costs including contingencies and fees",
      "planning renovation programmes with phased budget allocation"],
     "Practical uses in construction project budgeting"),

    (["productivity", "project planning", "waste factor", "water consumption"],
     ["benchmarking site productivity and identifying inefficiencies",
      "estimating material waste factors for accurate ordering",
      "calculating on-site water consumption for temporary utilities planning",
      "planning project milestones and resource allocation"],
     "Practical uses in construction project planning"),

    (["pool volume", "swimming pool"],
     ["calculating chemical dosing quantities for swimming pool treatment",
      "estimating pool fill times based on water supply flow rate",
      "planning pump and filter sizing for correct pool turnover rates",
      "budgeting water and heating costs for pool operation"],
     "Practical uses in swimming pool planning and maintenance"),

    (["topsoil", "garden"],
     ["estimating topsoil volumes for garden levelling and raised beds",
      "planning mulch and compost quantities for landscape projects",
      "calculating fill volumes for new lawn installations",
      "budgeting soil improvement works for landscaping contracts"],
     "Practical uses in garden and landscaping projects"),

    # Math and Statistics
    (["absolute value", "arithmetic sequence", "geometric sequence", "complex number",
      "matrix", "vector", "dot product", "cross product", "derivative", "integral",
      "trapezoidal", "logarithm", "natural logarithm", "exponential",
      "factorial", "permutations", "combinations",
      "standard deviation", "variance", "median", "quartile", "z-score",
      "arithmetic", "algebra", "geometry", "trigonometry", "calculus"],
     ["solving mathematical problems in school, university, and professional contexts",
      "verifying hand calculations and checking textbook exercise answers",
      "teaching and demonstrating mathematical concepts in the classroom",
      "supporting engineering, science, and data-analysis workflows"],
     "Real-world applications"),

    # Technology / Computing
    (["data transfer", "download time", "bandwidth", "ping", "latency",
      "server uptime", "raid", "screen resolution", "dpi", "ppi",
      "aspect ratio", "image file size", "video file size", "uncompressed image",
      "password entropy", "typing speed", "reading time", "sms cost",
      "data usage", "screen brightness", "nits"],
     ["estimating download and upload times when planning data migrations",
      "calculating storage requirements for media production and backup systems",
      "benchmarking network and server performance for IT infrastructure decisions",
      "comparing screen specifications and computing metrics when buying hardware"],
     "Practical uses in IT and technology"),

    (["fuel cost", "data transfer"],  # duplicate key covered above; kept for safety
     ["estimating fuel costs for fleet management and logistics planning",
      "calculating data transfer times for backup and migration projects",
      "planning operational budgets for transport and IT infrastructure",
      "benchmarking transfer speeds across different network configurations"],
     "Practical uses in technology and operations management"),
]

BAD_USES_PATTERN = re.compile(
    r'<ul>\s*<li>everyday math problems</li>'
    r'(<li>budgeting and planning</li>)?'
    r'(<li>cooking and home measurements</li>)?'
    r'(<li>travel and time calculations</li>)?'
    r'\s*</ul>',
    re.IGNORECASE
)

def detect_category(content: str):
    """Return (uses_list, heading) for the calculator based on its formula/name."""
    content_lower = content.lower()
    for keywords, uses, heading in CATEGORY_RULES:
        if any(kw in content_lower for kw in keywords):
            return uses, heading
    # Fallback
    return (
        ["solving everyday calculation problems accurately and quickly",
         "verifying manual calculations before submitting to clients or authorities",
         "teaching calculation methods in educational settings",
         "supporting professional decision-making with reliable numeric results"],
        "When this calculator comes in handy"
    )


def fix_file(path: str) -> bool:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'everyday math problems' not in content:
        return False

    uses, heading = detect_category(content)
    new_ul = '<ul>\n' + '\n'.join(f'<li>{u}</li>' for u in uses) + '\n</ul>'
    fixed = BAD_USES_PATTERN.sub(new_ul, content)

    if fixed == content:
        # Pattern didn't match; try a broader replace
        fixed = content.replace(
            '<li>everyday math problems</li><li>budgeting and planning</li>'
            '<li>cooking and home measurements</li><li>travel and time calculations</li>',
            '\n'.join(f'<li>{u}</li>' for u in uses)
        )

    if fixed == content:
        print(f"  WARN: could not replace in {os.path.basename(path)}")
        return False

    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed)
    return True


def main():
    fixed = 0
    skipped = 0
    for fname in sorted(os.listdir(CONTENT_DIR)):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(CONTENT_DIR, fname)
        if fix_file(path):
            print(f"  FIXED: {fname}")
            fixed += 1
        else:
            skipped += 1

    print(f"\nDone: {fixed} fixed, {skipped} skipped (no bad content)")


if __name__ == '__main__':
    main()
