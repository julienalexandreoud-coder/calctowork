"""Generate favicon.ico and apple-touch-icon.png from favicon.svg"""
from PIL import Image, ImageDraw
import os

PUBLIC = os.path.join(os.path.dirname(__file__), '..', 'public')

# Create a simple 180x180 orange circle icon for apple-touch-icon
img_180 = Image.new('RGBA', (180, 180), (0, 0, 0, 0))
draw = ImageDraw.Draw(img_180)
# Orange circle (#f97316)
draw.ellipse([10, 10, 170, 170], fill=(249, 115, 22, 255))
# White calculator text
draw.text((45, 60), "CTW", fill=(255, 255, 255, 255))
img_180.save(os.path.join(PUBLIC, 'apple-touch-icon.png'), 'PNG')

# Create 32x32 favicon.ico
img_32 = img_180.resize((32, 32), Image.LANCZOS)
img_16 = img_180.resize((16, 16), Image.LANCZOS)
# Save as ICO with multiple sizes
ico_sizes = [(16, 16), (32, 32), (48, 48)]
imgs = []
for size in ico_sizes:
    imgs.append(img_180.resize(size, Image.LANCZOS))
imgs[0].save(
    os.path.join(PUBLIC, 'favicon.ico'),
    format='ICO',
    sizes=[(16, 16), (32, 32), (48, 48)],
    append_images=imgs[1:]
)

print('Created apple-touch-icon.png and favicon.ico')