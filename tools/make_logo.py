"""Trace raw_input/logo.jpg (a 436px scan of the jar label) into crisp SVGs.

The label is black ink on white, too small to show sharply on a phone, so we
upscale, threshold and vectorise it with potracer. Run from the repo root:

    .venv/bin/python tools/make_logo.py

Writes img/emblem.svg (arc, banner, flower-bee and the wordmark) and
img/mark.svg (just the bee in the flower, for the header and favicon).
Ink is the site's --ink teal (an <img> SVG can't inherit CSS colour).
Also writes img/favicon.svg: the mark on a pale round.
"""
from PIL import Image, ImageDraw
import potrace

SCALE = 4
INK = "#1b5a61"   # keep in step with --ink in css/site.css
GROUND = "#f2f6f2"  # --paper
SRC = Image.open("raw_input/logo.jpg").convert("L")


def trace(box, erase=(), out="img/out.svg", label="", favicon=None):
    im = SRC.crop(box)
    draw = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in erase:  # erase boxes are in source coordinates
        draw.rectangle((x0 - box[0], y0 - box[1], x1 - box[0], y1 - box[1]), fill=255)
    w, h = im.size
    big = im.resize((w * SCALE, h * SCALE), Image.LANCZOS)
    # potracer traces the dark pixels of a "1" image, so ink must stay dark here
    ink = big.point(lambda v: 0 if v < 140 else 255).convert("1")
    paths = potrace.Bitmap(ink).trace(turdsize=6, alphamax=1.0, opttolerance=0.2)
    d = []
    for curve in paths:
        s = curve.start_point
        seg = [f"M{s.x:.1f} {s.y:.1f}"]
        for c in curve.segments:
            if c.is_corner:
                seg.append(f"L{c.c.x:.1f} {c.c.y:.1f}L{c.end_point.x:.1f} {c.end_point.y:.1f}")
            else:
                seg.append(f"C{c.c1.x:.1f} {c.c1.y:.1f} {c.c2.x:.1f} {c.c2.y:.1f} {c.end_point.x:.1f} {c.end_point.y:.1f}")
        d.append("".join(seg) + "Z")
    path = f'<path fill="{INK}" fill-rule="evenodd" d="{"".join(d)}"/>'
    W, H = w * SCALE, h * SCALE
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'role="img" aria-label="{label}">{path}</svg>\n')
    open(out, "w").write(svg)
    print(out, len(svg) // 1024, "KB")
    if favicon:
        side = max(W, H) * 1.18
        x0, y0 = (W - side) / 2, (H - side) / 2
        ico = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {side:.0f} {side:.0f}">'
               f'<circle cx="{W/2:.0f}" cy="{H/2:.0f}" r="{side/2:.0f}" fill="{GROUND}"/>{path}</svg>\n')
        open(favicon, "w").write(ico)
        print(favicon, len(ico) // 1024, "KB")


# Corner fleurons sit beside the arc text, and specks sit under "ck"; blank them out.
trace((50, 8, 406, 276), erase=[(50, 8, 97, 52), (348, 8, 406, 52), (180, 270, 225, 276)],
      out="img/emblem.svg", label="Wofchuck Honey Co. — Please thank the bees!")
trace((180, 132, 270, 226), out="img/mark.svg", label="", favicon="img/favicon.svg")
