# -*- coding: utf-8 -*-
"""Sistema visual do curso Tecnologia na Prática — funções de desenho."""
from __future__ import annotations

import math
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fontes")

# ---------------------------------------------------------------- cores
AZUL = "#1657A8"
NOITE = "#0A2E5C"
GRAFITE = "#1F2933"
CREME = "#FFF8EC"
BRANCO = "#FFFFFF"
AMARELO = "#FFC53D"
VERMELHO = "#D92D20"
CINZA = "#5B6770"
LINHA = "#D6DBE0"

TRILHAS = {
    "geral": {"nome": "TECNOLOGIA NA PRÁTICA", "cor": AZUL, "claro": "#DCE8F7",
              "rotulo": "8 a 13 · 14 a 18 · 18+", "curto": "TODAS AS IDADES"},
    "exploradores": {"nome": "EXPLORADORES", "cor": "#0F7B5A", "claro": "#D9F2E6",
                     "rotulo": "8 a 13 anos", "curto": "8–13"},
    "makers": {"nome": "MAKERS/DEVS", "cor": "#C2570A", "claro": "#FDE8D3",
               "rotulo": "14 a 18 anos", "curto": "14–18"},
    "profissionais": {"nome": "PROFISSIONAIS", "cor": "#5B3FA8", "claro": "#E8E1F7",
                      "rotulo": "18+", "curto": "18+"},
}

SITE = "marquezbertin.github.io/laboratorio-tech-social"
REPO = "github.com/Marquezbertin/Curso-Tecnologia-Sao-Pedro"


def hx(c: str, a: int = 255):
    c = c.lstrip("#")
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


_font_cache: dict = {}


def font(weight: str = "regular", size: int = 40, mono: bool = False):
    key = (weight, size, mono)
    if key in _font_cache:
        return _font_cache[key]
    if mono:
        path = os.path.join(FONTS, "JetBrainsMono-Regular.ttf")
        f = ImageFont.truetype(path, size)
        try:
            f.set_variation_by_axes([400])
        except Exception:
            pass
    else:
        path = os.path.join(FONTS, "Inter-Variable.ttf")
        f = ImageFont.truetype(path, size)
        w = {"light": 300, "regular": 400, "medium": 500, "semibold": 600,
             "bold": 700, "black": 800}[weight]
        try:
            f.set_variation_by_axes([32, w])
        except Exception:
            pass
    _font_cache[key] = f
    return f


display_files = {"light": "Light", "regular": "Regular", "medium": "Medium",
                 "semibold": "SemiBold", "bold": "Bold", "extrabold": "ExtraBold",
                 "black": "ExtraBold"}


def display(size: int, weight: str = "bold"):
    path = os.path.join(FONTS, f"Poppins-{display_files.get(weight, 'Bold')}.ttf")
    if not os.path.exists(path):
        path = os.path.join(FONTS, "Poppins-Bold.ttf")
    key = ("poppins", weight, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


# ---------------------------------------------------------------- canvas
def canvas(w: int, h: int, bg=CREME):
    img = Image.new("RGB", (w, h), hx(bg) if isinstance(bg, str) else bg)
    return img


def gradient(w: int, h: int, c1: str, c2: str, horizontal=False):
    a = hx(c1)
    b = hx(c2)
    grad = Image.new("RGB", (w, h))
    px = grad.load()
    n = w if horizontal else h
    for i in range(n):
        t = i / max(1, n - 1)
        col = (round(a[0] + (b[0] - a[0]) * t),
               round(a[1] + (b[1] - a[1]) * t),
               round(a[2] + (b[2] - a[2]) * t))
        if horizontal:
            for y in range(h):
                px[i, y] = col
        else:
            for x in range(w):
                px[x, i] = col
    return grad


def overlay(img):
    return Image.new("RGBA", img.size, (0, 0, 0, 0))


def paste_alpha(base, layer):
    base.paste(layer, (0, 0), layer)


# ---------------------------------------------------------------- texto
def text(d: ImageDraw.ImageDraw, xy, s, f, fill, anchor="la", spacing=4):
    d.multiline_text(xy, s, font=f, fill=hx(fill) if isinstance(fill, str) else fill,
                     anchor=anchor, spacing=spacing)


def tracked(d, xy, s, f, fill, tracking=0.0, anchor="la"):
    """Texto com espaçamento entre letras (tracking em fração do tamanho)."""
    x, y = xy
    fill = hx(fill) if isinstance(fill, str) else fill
    total = 0
    widths = []
    for ch in s:
        bb = d.textbbox((0, 0), ch, font=f)
        w = bb[2] - bb[0]
        widths.append(w)
        total += w + tracking * f.size
    total -= tracking * f.size
    if anchor.startswith("m"):
        x -= total / 2
    elif anchor.startswith("r"):
        x -= total
    for ch, w in zip(s, widths):
        d.text((x, y), ch, font=f, fill=fill, anchor="ls")
        x += w + tracking * f.size
    return total


def wrap(d, s, f, maxw):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=f) <= maxw or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, xy, s, f, fill, maxw, lh=1.35, anchor="la"):
    lines = wrap(d, s, f, maxw)
    x, y = xy
    fill = hx(fill) if isinstance(fill, str) else fill
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill, anchor=anchor)
        y += int(f.size * lh)
    return y


def fit_display(d, s, maxw, start, min_size=40, weight="bold"):
    size = start
    while size > min_size:
        f = display(size, weight)
        if d.textlength(s, font=f) <= maxw:
            return f
        size -= 4
    return display(min_size, weight)


def text_height(d, s, f, maxw, lh=1.25):
    return len(wrap(d, s, f, maxw)) * f.size * lh


# ---------------------------------------------------------------- formas
def rrect(d, box, r, fill=None, outline=None, width=2):
    d.rounded_rectangle(box, radius=r,
                        fill=hx(fill) if isinstance(fill, str) else fill,
                        outline=hx(outline) if isinstance(outline, str) else outline,
                        width=width)


def shadowed_card(img, box, r=28, fill=BRANCO, blur=28, offset=(0, 14), alpha=60):
    ov = overlay(img)
    od = ImageDraw.Draw(ov)
    x0, y0, x1, y1 = box
    od.rounded_rectangle((x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]),
                         radius=r, fill=(0, 0, 0, alpha))
    ov = ov.filter(ImageFilter.GaussianBlur(blur))
    paste_alpha(img, ov)
    d = ImageDraw.Draw(img)
    rrect(d, box, r, fill=fill)
    return d


def pill(d, xy, s, f, bg, fg, padx=28, pady=12, tracking=0.04, outline=None):
    x, y = xy
    w = d.textlength(s, font=f) + tracking * f.size * len(s) + padx * 2
    h = f.size + pady * 2
    rrect(d, (x, y, x + w, y + h), h // 2, fill=bg, outline=outline, width=2)
    tracked(d, (x + padx, y + pady + f.size * 0.78), s, f, fg, tracking)
    return w, h


def tag(img, xy, s, bg, fg=BRANCO, size=24, padx=26, pady=13, tracking=0.10):
    d = ImageDraw.Draw(img)
    return pill(d, xy, s.upper(), display(size, "semibold"), bg, fg, padx, pady, tracking)


# ---------------------------------------------------------------- marca
def draw_mark(img, x, y, size, color=AZUL, bg=None, stroke=None):
    """Símbolo: quadrado arredondado, três nós e play central."""
    d = ImageDraw.Draw(img)
    col = hx(color)
    sw = max(2, int(size * 0.075))
    r = int(size * 0.20)
    if bg is not None:
        rrect(d, (x, y, x + size, y + size), r, fill=bg)
    rrect(d, (x + sw // 2, y + sw // 2, x + size - sw // 2, y + size - sw // 2),
          r - sw // 2, outline=col, width=sw)
    nodes = [(0.27, 0.31), (0.73, 0.31), (0.50, 0.755)]
    pts = [(x + size * a, y + size * b) for a, b in nodes]
    lw = max(2, int(size * 0.068))
    for i in range(3):
        d.line([pts[i], pts[(i + 1) % 3]], fill=col, width=lw)
    nr = size * 0.062
    for px, py in pts:
        d.ellipse((px - nr, py - nr, px + nr, py + nr), fill=col)
    # play
    cx, cy = x + size * 0.5, y + size * 0.455
    t = size * 0.105
    d.polygon([(cx - t * 0.75, cy - t), (cx - t * 0.75, cy + t), (cx + t, cy)], fill=col)


def logo_h(img, x, y, height=76, color=AZUL, sub=True, sub_color=CINZA):
    """Assinatura horizontal: símbolo + nome + cidade."""
    d = ImageDraw.Draw(img)
    draw_mark(img, x, y, height, color)
    tx = x + height + height * 0.30
    f1 = display(int(height * 0.235), "bold")
    f2 = display(int(height * 0.235), "semibold")
    d.text((tx, y + height * 0.06), "TECNOLOGIA", font=f1, fill=hx(color), anchor="la")
    d.text((tx, y + height * 0.34), "NA PRÁTICA", font=f2, fill=hx(color), anchor="la")
    if sub:
        f3 = font("semibold", int(height * 0.135))
        tracked(d, (tx + 2, y + height * 0.78), "SÃO PEDRO/SP", f3, sub_color, 0.14)


def logo_v(img, cx, y, height=220, color=AZUL, sub=True, sub_color=CINZA):
    d = ImageDraw.Draw(img)
    draw_mark(img, cx - height / 2, y, height, color)
    f1 = display(int(height * 0.125), "bold")
    f2 = display(int(height * 0.125), "semibold")
    tracked(d, (cx, y + height + height * 0.12), "TECNOLOGIA NA PRÁTICA", f1, color, 0.02, "ma")
    if sub:
        f3 = font("semibold", int(height * 0.058))
        tracked(d, (cx, y + height + height * 0.30), "SÃO PEDRO/SP", f3, sub_color, 0.18, "ma")


# ---------------------------------------------------------------- ícones
def icon(img, kind, x, y, s, color=AZUL, width=None):
    d = ImageDraw.Draw(img)
    col = hx(color)
    w = width or max(3, int(s * 0.09))
    r = s * 0.18
    if kind == "play":
        d.polygon([(x + s * 0.30, y + s * 0.20), (x + s * 0.30, y + s * 0.80),
                   (x + s * 0.82, y + s * 0.50)], fill=col)
    elif kind == "check":
        d.line([(x + s * .20, y + s * .52), (x + s * .42, y + s * .73),
                (x + s * .82, y + s * .25)], fill=col, width=w, joint="curve")
    elif kind == "star4":
        cx, cy = x + s / 2, y + s / 2
        d.polygon([(cx, y), (cx + s * .12, cy - s * .12), (x + s, cy),
                   (cx + s * .12, cy + s * .12), (cx, y + s),
                   (cx - s * .12, cy + s * .12), (x, cy),
                   (cx - s * .12, cy - s * .12)], fill=col)
    elif kind == "code":
        d.line([(x + s * .38, y + s * .22), (x + s * .10, y + s * .50),
                (x + s * .38, y + s * .78)], fill=col, width=w, joint="curve")
        d.line([(x + s * .62, y + s * .22), (x + s * .90, y + s * .50),
                (x + s * .62, y + s * .78)], fill=col, width=w, joint="curve")
        d.line([(x + s * .56, y + s * .14), (x + s * .44, y + s * .86)],
               fill=col, width=w)
    elif kind == "wifi":
        for i, rad in enumerate([0.44, 0.30]):
            d.arc((x + s * (.5 - rad), y + s * (.55 - rad), x + s * (.5 + rad), y + s * (.55 + rad)),
                  200, 340, fill=col, width=w)
        d.ellipse((x + s * .44, y + s * .62, x + s * .56, y + s * .74), fill=col)
    elif kind == "lock":
        rrect(d, (x + s * .18, y + s * .45, x + s * .82, y + s * .88), int(r),
              fill=None, outline=col, width=w)
        d.arc((x + s * .30, y + s * .16, x + s * .70, y + s * .62), 180, 360, fill=col, width=w)
        d.ellipse((x + s * .46, y + s * .60, x + s * .54, y + s * .68), fill=col)
    elif kind == "chart":
        d.line([(x + s * .12, y + s * .86), (x + s * .88, y + s * .86)], fill=col, width=w)
        for i, h in enumerate([0.28, 0.48, 0.66]):
            d.rectangle((x + s * (.22 + i * .22), y + s * (.86 - h), x + s * (.36 + i * .22),
                         y + s * .86), fill=col)
    elif kind == "cert":
        rrect(d, (x + s * .14, y + s * .14, x + s * .86, y + s * .70), int(r),
              outline=col, width=w)
        for i in range(3):
            d.line([(x + s * .28, y + s * (.30 + i * .12)), (x + s * .66, y + s * (.30 + i * .12))],
                   fill=col, width=max(2, w // 2))
        d.ellipse((x + s * .40, y + s * .62, x + s * .60, y + s * .82), fill=col)
        d.polygon([(x + s * .42, y + s * .80), (x + s * .38, y + s * .98),
                   (x + s * .50, y + s * .90), (x + s * .62, y + s * .98),
                   (x + s * .58, y + s * .80)], fill=col)
    elif kind == "money0":
        d.ellipse((x + s * .14, y + s * .14, x + s * .86, y + s * .86), outline=col, width=w)
        f = display(int(s * .46), "bold")
        d.text((x + s * .5, y + s * .54), "0", font=f, fill=col, anchor="mm")
    elif kind == "arrow":
        d.line([(x + s * .18, y + s * .5), (x + s * .78, y + s * .5)], fill=col, width=w)
        d.line([(x + s * .56, y + s * .26), (x + s * .80, y + s * .5),
                (x + s * .56, y + s * .74)], fill=col, width=w, joint="curve")
    elif kind == "clock":
        d.ellipse((x + s * .12, y + s * .12, x + s * .88, y + s * .88), outline=col, width=w)
        d.line([(x + s * .5, y + s * .28), (x + s * .5, y + s * .52),
                (x + s * .68, y + s * .62)], fill=col, width=w, joint="curve")
    elif kind == "pin":
        d.ellipse((x + s * .22, y + s * .12, x + s * .78, y + s * .62), outline=col, width=w)
        d.line([(x + s * .5, y + s * .62), (x + s * .5, y + s * .92)], fill=col, width=w)
        d.ellipse((x + s * .42, y + s * .30, x + s * .58, y + s * .46), fill=col)


# ---------------------------------------------------------------- motivos
def motif_circuit(img, box, color, alpha=40, nodes=True):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    col = hx(color, alpha)
    lw = max(2, int(min(w, h) * 0.012))
    pts = [(0.06, 0.20), (0.34, 0.20), (0.34, 0.52), (0.68, 0.52),
           (0.68, 0.82), (0.94, 0.82)]
    p = [(x0 + w * a, y0 + h * b) for a, b in pts]
    d.line(p, fill=col, width=lw, joint="curve")
    pts2 = [(0.10, 0.72), (0.10, 0.44), (0.52, 0.44), (0.52, 0.14), (0.86, 0.14)]
    p2 = [(x0 + w * a, y0 + h * b) for a, b in pts2]
    d.line(p2, fill=col, width=lw, joint="curve")
    if nodes:
        for px, py in p + p2:
            nr = min(w, h) * 0.022
            d.ellipse((px - nr, py - nr, px + nr, py + nr), fill=col)


def motif_blocks(img, box, color, alpha=255):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    col = hx(color, alpha)
    for i in range(3):
        bx = x0 + w * (0.04 + i * 0.06)
        by = y0 + h * (0.10 + i * 0.24)
        bw = w * (0.62 - i * 0.04)
        bh = h * 0.17
        rrect(d, (bx, by, bx + bw, by + bh), int(h * 0.045), fill=col)
        # encaixe
        d.rounded_rectangle((bx + bw * 0.18, by + bh * 0.80, bx + bw * 0.40, by + bh * 1.02),
                            radius=int(h * 0.015), fill=col)


def motif_code(img, box, color, bg=NOITE):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    rrect(d, box, int(h * 0.06), fill=bg)
    # barra
    d.rounded_rectangle((x0, y0, x1, y0 + h * 0.13), radius=int(h * 0.06), fill=hx("#123E70"))
    d.rectangle((x0, y0 + h * 0.08, x1, y0 + h * 0.13), fill=hx("#123E70"))
    for i, c in enumerate([VERMELHO, AMARELO, "#1FA97A"]):
        cx = x0 + w * (0.06 + i * 0.06)
        cy = y0 + h * 0.065
        rr = h * 0.018
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=hx(c))
    lines = [(0.10, 0.30, 0.44), (0.16, 0.42, 0.62), (0.16, 0.54, 0.50),
             (0.10, 0.66, 0.58), (0.16, 0.78, 0.38)]
    f = font("regular", int(h * 0.055), mono=True)
    for a, b, c in lines:
        d.rectangle((x0 + w * a, y0 + h * b, x0 + w * c, y0 + h * b + h * 0.028),
                    fill=hx(color, 210))
    if color != AMARELO:
        d.rectangle((x0 + w * 0.10, y0 + h * 0.30, x0 + w * 0.16, y0 + h * 0.328),
                    fill=hx(AMARELO))


def motif_terminal(img, box, color=AMARELO):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    rrect(d, box, int(h * 0.06), fill=NOITE)
    d.rounded_rectangle((x0, y0, x1, y0 + h * 0.12), radius=int(h * 0.06), fill=hx("#061C3A"))
    d.rectangle((x0, y0 + h * 0.07, x1, y0 + h * 0.12), fill=hx("#061C3A"))
    f = font("regular", int(h * 0.085), mono=True)
    fb = font("semibold", int(h * 0.085), mono=True)
    d.text((x0 + w * .08, y0 + h * .30), ">", font=fb, fill=hx(color), anchor="la")
    d.text((x0 + w * .16, y0 + h * .30), "automatizar.py", font=f, fill=hx(BRANCO), anchor="la")
    d.text((x0 + w * .08, y0 + h * .48), "backup concluído", font=f, fill=hx("#8FE3B0"), anchor="la")
    d.text((x0 + w * .08, y0 + h * .66), "8 testes verdes", font=f, fill=hx(color), anchor="la")
    d.rectangle((x0 + w * .08, y0 + h * .82, x0 + w * .42, y0 + h * .86), fill=hx("#2F6FBF"))


def motif_mosaic(img, box, colors, alpha=255):
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    cells = [(0.02, 0.02, 0.34, 0.34), (0.38, 0.02, 0.66, 0.26),
             (0.70, 0.02, 0.98, 0.44), (0.02, 0.38, 0.22, 0.66),
             (0.26, 0.38, 0.58, 0.70), (0.62, 0.48, 0.98, 0.74),
             (0.02, 0.70, 0.40, 0.98), (0.44, 0.74, 0.70, 0.98),
             (0.74, 0.78, 0.98, 0.98)]
    for i, (a, b, c, e) in enumerate(cells):
        col = hx(colors[i % len(colors)], alpha)
        rrect(d, (x0 + w * a, y0 + h * b, x0 + w * c, y0 + h * e), int(min(w, h) * 0.05), fill=col)


def pattern_grid(img, step=48, color="#0A2E5C", alpha=14):
    d = ImageDraw.Draw(img)
    col = hx(color, alpha)
    for x in range(0, img.width, step):
        d.line([(x, 0), (x, img.height)], fill=col, width=1)
    for y in range(0, img.height, step):
        d.line([(0, y), (img.width, y)], fill=col, width=1)


def pattern_dots(img, step=40, color="#0A2E5C", alpha=30):
    d = ImageDraw.Draw(img)
    col = hx(color, alpha)
    for x in range(step // 2, img.width, step):
        for y in range(step // 2, img.height, step):
            d.ellipse((x - 3, y - 3, x + 3, y + 3), fill=col)


# ---------------------------------------------------------------- QR
def qr(url: str, size: int = 420, dark=NOITE, light=BRANCO):
    import qrcode
    q = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                      box_size=12, border=2)
    q.add_data(url)
    q.make(fit=True)
    im = q.make_image(fill_color=dark, back_color=light).convert("RGB")
    return im.resize((size, size), Image.NEAREST)


# ---------------------------------------------------------------- save
def save_png(img, path, scale=1):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if scale != 1:
        img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    img.save(path, "PNG", optimize=True)
    return path


def save_pdf(img, path, dpi=300):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PDF", resolution=dpi)
    return path


def save_jpg(img, path, quality=92):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.convert("RGB").save(path, "JPEG", quality=quality, optimize=True)
    return path
