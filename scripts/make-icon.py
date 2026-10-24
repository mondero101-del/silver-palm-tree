# Draws the app icon and splash screen during the build, so no picture files are needed in the repository.
import math, os, random
from PIL import Image, ImageDraw, ImageFilter

random.seed(7)
BG = (5, 6, 10)
SHADES = [(59, 130, 246), (96, 165, 250), (147, 197, 253), (37, 99, 235), (191, 219, 254)]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(out, exist_ok=True)


def heart_layer(size, scale):
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d, g = ImageDraw.Draw(base), ImageDraw.Draw(glow)
    cx, cy = size / 2, size / 2 + size * 0.02
    s = size * scale / 32
    pts = []
    for _ in range(5200):
        if random.random() < 0.35:
            t = random.random() * 2 * math.pi
            x = 16 * math.sin(t) ** 3
            y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
            r = 1 - random.random() * 0.03
            pts.append((x * r, -(y * r + 2.5)))
        else:
            while True:
                x = (random.random() * 2 - 1) * 1.15
                y = random.random() * 2.25 - 1
                q = x * x + y * y - 1
                if q ** 3 - x * x * y ** 3 <= 0:
                    break
            pts.append((x * 14, -(y - 0.125) * 13))
    for x, y in pts:
        c = random.choice(SHADES)
        r = max(1.2, size * random.uniform(0.0018, 0.0042))
        px, py = cx + x * s, cy + y * s
        d.ellipse([px - r, py - r, px + r, py + r], fill=c + (255,))
        g.ellipse([px - r * 2.4, py - r * 2.4, px + r * 2.4, py + r * 2.4], fill=c + (150,))
    glow = glow.filter(ImageFilter.GaussianBlur(size * 0.018))
    return Image.alpha_composite(glow, base)


def with_bg(layer, size):
    bg = Image.new("RGBA", (size, size), BG + (255,))
    halo = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse([size * .15, size * .15, size * .85, size * .85], fill=(37, 99, 235, 70))
    halo = halo.filter(ImageFilter.GaussianBlur(size * 0.12))
    return Image.alpha_composite(Image.alpha_composite(bg, halo), layer)


with_bg(heart_layer(1024, 0.74), 1024).convert("RGB").save(os.path.join(out, "icon-only.png"))
heart_layer(1024, 0.46).save(os.path.join(out, "icon-foreground.png"))
Image.new("RGB", (1024, 1024), BG).save(os.path.join(out, "icon-background.png"))
splash = with_bg(heart_layer(2732, 0.30), 2732).convert("RGB")
splash.save(os.path.join(out, "splash.png"))
splash.save(os.path.join(out, "splash-dark.png"))
print("icons written to", os.path.abspath(out))
