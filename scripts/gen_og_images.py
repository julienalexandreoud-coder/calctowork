"""Generate OG images per category using Pillow."""
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'og')
os.makedirs(OUTPUT, exist_ok=True)

CATEGORIES = {
    'estructuras': {'icon': '🏗️', 'en': 'Construction Calculators', 'color': (249, 115, 22)},
    'mamposteria': {'icon': '🧱', 'en': 'Masonry Calculators', 'color': (180, 83, 9)},
    'pavimentos': {'icon': '🪨', 'en': 'Flooring & Tiling', 'color': (120, 53, 15)},
    'fontaneria': {'icon': '🔧', 'en': 'Plumbing & Water', 'color': (37, 99, 235)},
    'electricidad': {'icon': '⚡', 'en': 'Electrical Calculators', 'color': (234, 179, 8)},
    'climatizacion': {'icon': '🌡️', 'en': 'HVAC Calculators', 'color': (6, 182, 212)},
    'carpinteria': {'icon': '🪵', 'en': 'Carpentry & Metalwork', 'color': (139, 92, 246)},
    'pintura': {'icon': '🎨', 'en': 'Painting & Finishes', 'color': (236, 72, 153)},
    'gestion': {'icon': '📊', 'en': 'Management & Costs', 'color': (34, 197, 94)},
    'matematicas': {'icon': '📐', 'en': 'Math Calculators', 'color': (99, 102, 241)},
    'finanzas': {'icon': '💰', 'en': 'Finance Calculators', 'color': (16, 185, 129)},
    'salud': {'icon': '❤️', 'en': 'Health Calculators', 'color': (239, 68, 68)},
    'cotidiano': {'icon': '🏠', 'en': 'Everyday Calculators', 'color': (251, 146, 60)},
    'ciencia': {'icon': '🔬', 'en': 'Science & Physics', 'color': (14, 165, 233)},
    'conversion': {'icon': '🔄', 'en': 'Unit Conversions', 'color': (168, 85, 247)},
    'deportes': {'icon': '🏃', 'en': 'Sports & Fitness', 'color': (245, 158, 11)},
    'quimica': {'icon': '⚗️', 'en': 'Chemistry Calculators', 'color': (20, 184, 166)},
    'electronica': {'icon': '🔌', 'en': 'Electronics Calculators', 'color': (234, 179, 8)},
    'estadistica': {'icon': '📈', 'en': 'Statistics Calculators', 'color': (139, 92, 246)},
    'clima': {'icon': '🌤️', 'en': 'Weather & Climate', 'color': (56, 189, 248)},
}

def create_og_image(text, color, filename):
    img = Image.new('RGB', (1200, 630), color)
    draw = ImageDraw.Draw(img)
    
    # Add gradient overlay
    for y in range(630):
        alpha = int(40 + (y / 630) * 80)
        draw.line([(0, y), (1200, y)], fill=(0, 0, 0))
    
    # White card
    draw.rounded_rectangle([60, 60, 1140, 570], radius=24, fill=(255, 255, 255, 240))
    
    # Orange accent bar
    draw.rounded_rectangle([60, 60, 1140, 100], radius=0, fill=color)
    
    # Site name
    try:
        font_title = ImageFont.truetype("arial.ttf", 52)
        font_subtitle = ImageFont.truetype("arial.ttf", 36)
        font_brand = ImageFont.truetype("arial.ttf", 28)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_brand = ImageFont.load_default()
    
    # Brand
    draw.text((600, 85), "CalcToWork", fill=color, font=font_brand, anchor="mm")
    
    # Title
    draw.text((600, 320), text, fill=(30, 30, 30), font=font_title, anchor="mm")
    
    # Subtitle
    draw.text((600, 400), "Free Online Calculator", fill=(120, 120, 120), font=font_subtitle, anchor="mm")
    
    # URL
    draw.text((600, 520), "calcto.work", fill=(160, 160, 160), font=font_brand, anchor="mm")
    
    img.save(os.path.join(OUTPUT, filename), 'PNG', quality=95)
    return filename

for slug, info in CATEGORIES.items():
    filename = create_og_image(info['en'], info['color'], f'{slug}.png')
    print(f'Created {filename}')

# Also create a default OG image
default = create_og_image('Free Online Calculators', (249, 115, 22), 'default.png')
print(f'Created {default}')

print(f'\nTotal: {len(CATEGORIES) + 1} OG images created')