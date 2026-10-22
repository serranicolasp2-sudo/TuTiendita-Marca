"""Isologos de tutienditaia (marca paraguas) para la foto de perfil de WhatsApp Business. Exporta PNG 1080x1080
y una hoja de revisión con el recorte circular, en grande y en tamaño de chat.

  python generar.py
"""
import pathlib
import subprocess

from PIL import Image, ImageDraw

AQUI = pathlib.Path(__file__).parent
EXPORT = AQUI.parent / "export"
EXPORT.mkdir(exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FUENTES = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:'
           'opsz,wght@12..96,400..800&display=block">')

BIROME, MALVON, PAPEL, TINTA = "#1E3C96", "#E0435C", "#F6F7FA", "#16205A"
YEMA, CINTA, REC = "#FFD23F", "#1A1712", "#D7301F"


def disco(cx, cy, r, vinilo, surco, etiqueta, tilde, hueco):
    """El vinilo de Tu Canción con su tilde (la ó del logo)."""
    surcos = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r * k:.1f}" fill="none" stroke="{surco}" stroke-opacity=".28" '
                     f'stroke-width="{r * 0.03:.1f}"/>' for k in (0.83, 0.69, 0.55))
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{vinilo}"/>{surcos}'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.36:.1f}" fill="{etiqueta}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.075:.1f}" fill="{hueco}"/>'
            f'<rect x="{cx + r * 0.05:.1f}" y="{cy - r * 1.42:.1f}" width="{r * 0.33:.1f}" height="{r * 0.62:.1f}" '
            f'rx="{r * 0.15:.1f}" fill="{tilde}" transform="rotate(32 {cx + r * 0.22:.1f} {cy - r * 1.11:.1f})"/>')


def toldo(x, y, ancho, alto, n, c1, c2, techo):
    """Toldo de almacén a rayas con borde festoneado."""
    w = ancho / n
    r = w / 2
    partes = [f'<rect x="{x - 14}" y="{y - 34}" width="{ancho + 28}" height="40" rx="12" fill="{techo}"/>']
    for i in range(n):
        color = c1 if i % 2 == 0 else c2
        xi = x + i * w
        partes.append(f'<rect x="{xi:.1f}" y="{y}" width="{w + 0.6:.1f}" height="{alto}" fill="{color}"/>')
        partes.append(f'<circle cx="{xi + r:.1f}" cy="{y + alto}" r="{r:.1f}" fill="{color}"/>')
    return "".join(partes)


def esquinero(x, y, lado, grosor, color, giro):
    return (f'<path d="M{x},{y + lado} L{x},{y} L{x + lado},{y}" fill="none" stroke="{color}" '
            f'stroke-width="{grosor}" stroke-linecap="square" transform="rotate({giro} {x + lado / 2} {y + lado / 2})"/>')


def pagina(fondo, svg):
    return (f'<!doctype html><html><head><meta charset="utf-8">{FUENTES}<style>*{{margin:0}}html,body{{width:1080px;'
            f'height:1080px;overflow:hidden;background:{fondo}}}svg{{display:block}}'
            f'text{{font-family:"Bricolage Grotesque",sans-serif}}</style></head><body>'
            f'<svg width="1080" height="1080" viewBox="0 0 1080 1080">{svg}</svg></body></html>')


def opcion_a():
    svg = (toldo(200, 300, 680, 150, 8, MALVON, PAPEL, PAPEL)
           + '<text x="540" y="700" text-anchor="middle" font-size="150" font-weight="800" letter-spacing="-5" fill="#FFFFFF">'
             '<tspan font-weight="400" fill="#AFC0FF">tu</tspan>tiendita</text>'
           + f'<rect x="455" y="752" width="170" height="92" rx="46" fill="{YEMA}"/>'
           + f'<text x="540" y="823" text-anchor="middle" font-size="68" font-weight="800" letter-spacing="2" fill="{CINTA}">IA</text>')
    return pagina(BIROME, svg)


def opcion_b():
    svg = (esquinero(250, 230, 150, 34, REC, 0) + esquinero(680, 620, 150, 34, REC, 180)
           + disco(540, 545, 225, BIROME, PAPEL, MALVON, MALVON, PAPEL)
           + f'<text x="540" y="920" text-anchor="middle" font-size="72" font-weight="800" letter-spacing="-2" fill="{TINTA}">'
             f'<tspan font-weight="400" fill="{BIROME}">tu</tspan>tiendita<tspan fill="{REC}">ia</tspan></text>')
    return pagina(YEMA, svg)


def opcion_c():
    svg = (toldo(230, 270, 620, 150, 8, MALVON, PAPEL, PAPEL)
           + f'<rect x="300" y="470" width="480" height="360" rx="18" fill="{TINTA}"/>'
           + disco(540, 683, 134, "#FFFFFF", BIROME, YEMA, MALVON, BIROME))
    return pagina(BIROME, svg)


OPCIONES = {"tti-isologo-a-toldo": opcion_a, "tti-isologo-b-disco-esquineros": opcion_b, "tti-isologo-c-vidriera": opcion_c}


def exportar(nombre, fn):
    html = AQUI / f"{nombre}.html"
    html.write_text(fn(), encoding="utf-8")
    png = EXPORT / f"{nombre}-1080x1080.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1080", "--virtual-time-budget=8000", f"--screenshot={png}", html.as_uri()],
                   check=True, capture_output=True)
    return png


def hoja_revision(pngs):
    """Cada opción recortada en círculo (como la muestra WhatsApp) en 400 px y en 64 px (lista de chats)."""
    hoja = Image.new("RGB", (len(pngs) * 470 + 30, 560), "#E9EDEF")
    d = ImageDraw.Draw(hoja)
    for i, png in enumerate(pngs):
        im = Image.open(png).convert("RGB")
        for lado, (x, y) in ((400, (30 + i * 470, 30)), (64, (30 + i * 470 + 168, 460))):
            chico = im.resize((lado, lado), Image.LANCZOS)
            mascara = Image.new("L", (lado, lado), 0)
            ImageDraw.Draw(mascara).ellipse((0, 0, lado - 1, lado - 1), fill=255)
            hoja.paste(chico, (x, y), mascara)
        d.text((30 + i * 470, 440), "ABC"[i], fill="#111")
    salida = EXPORT / "revision-circulo.png"
    hoja.save(salida)
    return salida


if __name__ == "__main__":
    pngs = [exportar(n, f) for n, f in OPCIONES.items()]
    print("\n".join(p.name for p in pngs), "\n", hoja_revision(pngs))
