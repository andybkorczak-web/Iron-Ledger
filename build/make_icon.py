import math
from PIL import Image, ImageDraw

INK = (18, 21, 26, 255)
BRASS = (201, 161, 90, 255)
BRASS_BRIGHT = (228, 192, 126, 255)
BRASS_DIM = (138, 111, 62, 255)

def draw_plate_icon(size, safe_zone_ratio, rounded=True, corner_ratio=0.22):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if rounded:
        radius = int(size * corner_ratio)
        draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=INK)
    else:
        draw.rectangle([0, 0, size - 1, size - 1], fill=INK)
    cx = cy = size / 2
    outer_r = size * safe_zone_ratio / 2
    ring_w = outer_r * 0.30
    inner_r = outer_r - ring_w
    bbox_outer = [cx - outer_r, cy - outer_r, cx + outer_r, cy + outer_r]
    bbox_inner = [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r]
    mask = Image.new("L", (size, size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.ellipse(bbox_outer, fill=255)
    mdraw.ellipse(bbox_inner, fill=0)
    ring_layer = Image.new("RGBA", (size, size), BRASS)
    img.paste(ring_layer, (0, 0), mask)
    hl = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hldraw = ImageDraw.Draw(hl)
    hldraw.arc(bbox_outer, start=200, end=340, fill=BRASS_BRIGHT, width=int(ring_w))
    img = Image.alpha_composite(img, hl)
    draw = ImageDraw.Draw(img)
    bolt_r = ring_w * 0.22
    bolt_dist = (outer_r + inner_r) / 2
    for angle_deg in (45, 135, 225, 315):
        a = math.radians(angle_deg)
        bx = cx + bolt_dist * math.cos(a)
        by = cy + bolt_dist * math.sin(a)
        draw.ellipse([bx - bolt_r, by - bolt_r, bx + bolt_r, by + bolt_r], fill=INK)
    center_r = inner_r * 0.30
    draw.ellipse([cx - center_r, cy - center_r, cx + center_r, cy + center_r], fill=BRASS_DIM)
    return img

icon = draw_plate_icon(1024, safe_zone_ratio=0.78, rounded=True, corner_ratio=0.22)
icon.save("/home/claude/desktop-app/build/icon.png")
print("1024 icon saved")
