"""Genera las piezas de Tu Canción (HTML) y las exporta a PNG con Chrome headless.

Uso:  python generar.py            -> todas
      python generar.py avatar     -> solo las que contengan "avatar" en el nombre
"""
import pathlib, subprocess, sys

AQUI = pathlib.Path(__file__).parent
EXPORT = AQUI.parent / "export"
EXPORT.mkdir(exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

BIROME, MALVON, TINTA, PAPEL, PLATA = "#1E3C96", "#E0435C", "#16205A", "#F6F7FA", "#5F6679"
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;'
         '12..96,600;12..96,800&family=Figtree:wght@400;500;600&family=Reenie+Beanie&display=block">')


def disco(vinilo=BIROME, hueco=PAPEL, etiqueta=MALVON, tilde=MALVON, cls="disco"):
    """La ó de la marca: vinilo con tilde. viewBox 100x118."""
    surcos = "".join(f'<circle cx="50" cy="68" r="{r}" fill="none" stroke="{hueco}" stroke-opacity=".22" stroke-width="1.4"/>'
                     for r in (40, 33, 26))
    return (f'<svg class="{cls}" viewBox="0 0 100 118" aria-hidden="true">'
            f'<circle cx="50" cy="68" r="48" fill="{vinilo}"/>{surcos}'
            f'<circle cx="50" cy="68" r="17" fill="{etiqueta}"/><circle cx="50" cy="68" r="3.6" fill="{hueco}"/>'
            f'<rect x="50" y="0" width="16" height="30" rx="7" fill="{tilde}" transform="rotate(32 58 15)"/></svg>')


def wordmark(texto=TINTA, tu=BIROME, vinilo=BIROME, hueco=PAPEL, size=120, etiqueta=MALVON, tilde=MALVON):
    return (f'<div class="wm" style="font-size:{size}px;color:{texto}"><span class="tu" style="color:{tu}">tu</span>'
            f'canci{disco(vinilo=vinilo, hueco=hueco, etiqueta=etiqueta, tilde=tilde)}n</div>')


BASE_CSS = f"""
*{{box-sizing:border-box;margin:0}}
html,body{{width:var(--w);height:var(--h);overflow:hidden}}
body{{font-family:'Figtree','Segoe UI',sans-serif;-webkit-font-smoothing:antialiased}}
.wm{{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;letter-spacing:-.035em;line-height:1;display:inline-flex;align-items:baseline;white-space:nowrap}}
.wm .tu{{font-weight:400;margin-right:.18em}}
.wm .disco{{height:.74em;width:auto;margin:0 .01em;transform:translateY(.035em);flex:none}}
.d{{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.02}}
.mano{{font-family:'Reenie Beanie',cursive;line-height:.9}}
.esquina{{position:absolute;width:56px;height:56px;border:10px solid {MALVON}}}
"""


def pagina(w, h, cuerpo, css=""):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}'
            f'<style>:root{{--w:{w}px;--h:{h}px}}{BASE_CSS}{css}</style></head><body>{cuerpo}</body></html>')


PIEZAS = {}


def pieza(nombre, w, h):
    def reg(fn):
        PIEZAS[nombre] = (w, h, fn)
        return fn
    return reg


@pieza("tc-avatar-1080x1080", 1080, 1080)
def avatar():
    return pagina(1080, 1080, f'<div class="c">{disco(vinilo="#FFFFFF", hueco=BIROME)}</div>',
                  f"body{{background:{BIROME};display:grid;place-items:center}}"
                  ".c{width:560px;transform:translateY(-38px)} .c svg{width:100%;height:auto}")


@pieza("tc-logo-papel-2000x800", 2000, 800)
def logo_papel():
    return pagina(2000, 800, wordmark(size=330), "body{background:#FFFFFF;display:grid;place-items:center}")


@pieza("tc-logo-birome-2000x800", 2000, 800)
def logo_birome():
    return pagina(2000, 800, wordmark(texto="#FFFFFF", tu="#AFC0FF", vinilo="#FFFFFF", hueco=BIROME, size=330),
                  f"body{{background:{BIROME};display:grid;place-items:center}}")


@pieza("tc-logo-fotos-2000x800", 2000, 800)
def logo_fotos():
    cuerpo = (f'<div class="g">{wordmark(size=230)}<div class="sub"><span class="esq"></span>Restauración de fotos</div></div>')
    return pagina(2000, 800, cuerpo,
                  "body{background:#FFFFFF;display:grid;place-items:center}"
                  ".g{display:grid;gap:34px}"
                  f".sub{{font-family:'Bricolage Grotesque';font-weight:600;font-size:92px;letter-spacing:-.01em;color:{TINTA};display:flex;align-items:center;gap:34px}}"
                  f".esq{{width:64px;height:64px;border-left:16px solid {MALVON};border-top:16px solid {MALVON};flex:none}}")


@pieza("tc-post-antes-despues-1080x1350", 1080, 1350)
def post_antes():
    cuerpo = f"""
<div class="top"><h1 class="d">La foto del casamiento<br>de los abuelos, 1962.</h1></div>
<div class="fotos">
  <div class="foto vieja"><span>antes</span><i class="esquina a"></i></div>
  <div class="foto nueva"><span>después</span><i class="esquina b"></i></div>
</div>
<div class="pie"><span>Restauración de fotos · $6.500</span><span>@tucancion.com.ar</span></div>"""
    return pagina(1080, 1350, cuerpo, f"""
body{{background:{BIROME};color:#fff;padding:72px 64px 60px;display:grid;grid-template-rows:auto 1fr auto;gap:48px}}
h1{{font-size:76px}}
.fotos{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.foto{{position:relative;border-radius:4px}}
.foto.vieja{{background:repeating-linear-gradient(115deg,#8f8a80 0 4px,#a29d92 4px 10px);filter:sepia(.5) contrast(.8)}}
.foto.nueva{{background:linear-gradient(160deg,#d9c3a7,#9a7b62 55%,#5d4a3f)}}
.foto span{{position:absolute;left:18px;bottom:18px;font:600 26px 'Figtree';letter-spacing:.1em;text-transform:uppercase;background:rgba(0,0,0,.5);padding:8px 14px;border-radius:3px}}
.esquina.a{{top:-12px;left:-12px;border-right:0;border-bottom:0}}
.esquina.b{{bottom:-12px;right:-12px;border-left:0;border-top:0}}
.pie{{display:flex;justify-content:space-between;font-size:30px;color:#C9D3FF}}""")


@pieza("tc-post-dedicatoria-1080x1350", 1080, 1350)
def post_dedicatoria():
    cuerpo = f"""
{wordmark(size=64)}
<div class="medio"><div class="mano">para vos, ma</div>
<p class="verso">"Me enseñaste a cocinar sin receta<br>y a volver siempre a casa"</p></div>
<div class="pie"><span>Una canción con tu historia · $27.000</span><span class="play"></span></div>"""
    return pagina(1080, 1350, cuerpo, f"""
body{{background:#FFFFFF;color:{TINTA};padding:80px 72px;display:grid;grid-template-rows:auto 1fr auto}}
.medio{{align-self:center;display:grid;gap:40px}}
.mano{{font-size:190px;color:{MALVON};transform:rotate(-4deg);transform-origin:left}}
.verso{{font:600 44px/1.4 'Figtree';color:{BIROME}}}
.pie{{display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:500}}
.play{{width:104px;height:104px;border-radius:50%;background:{MALVON};display:grid;place-items:center}}
.play::before{{content:"";border-left:34px solid #fff;border-top:21px solid transparent;border-bottom:21px solid transparent;margin-left:8px}}""")


@pieza("tc-post-precios-1080x1350", 1080, 1350)
def post_precios():
    filas = [("Canción con tu historia", "$27.000"), ("Foto restaurada", "$6.500"),
             ("3 fotos restauradas", "$15.900"), ("Canción + video con fotos", "$59.900")]
    lis = "".join(f"<li><span>{a}</span><b>{b}</b></li>" for a, b in filas)
    cuerpo = f"""
<div class="k">Día de la Madre · domingo 18 de octubre</div>
<ul>{lis}</ul>
<div class="pie"><span class="mano">pedila hasta el jueves 15</span>{wordmark(texto="#FFFFFF", tu="#FFD3DA", vinilo="#FFFFFF", hueco=MALVON, size=54, etiqueta=BIROME, tilde=BIROME)}</div>"""
    css = f"""
body{{background:{MALVON};color:#fff;padding:80px 72px;display:grid;grid-template-rows:auto 1fr auto}}
.k{{font:600 30px 'Figtree';letter-spacing:.12em;text-transform:uppercase}}
ul{{list-style:none;padding:0;align-self:center;display:grid;gap:34px}}
li{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid rgba(255,255,255,.4);padding-bottom:26px;font-size:42px}}
li b{{font:800 64px 'Bricolage Grotesque';letter-spacing:-.02em;font-variant-numeric:tabular-nums}}
.pie{{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}}
.pie .mano{{font-size:76px;white-space:nowrap}}
"""
    return pagina(1080, 1350, cuerpo, css)


@pieza("tc-story-dia-madre-1080x1920", 1080, 1920)
def story():
    cuerpo = f"""
{wordmark(texto="#FFFFFF", tu="#AFC0FF", vinilo="#FFFFFF", hueco=BIROME, size=96)}
<div class="medio">
  <h1 class="d">Ella te cantó<br>toda la vida.</h1>
  <p class="mano">Ahora te toca a vos.</p>
  <p class="txt">Contanos su historia y en 48 horas tenés su canción.</p>
</div>
<div class="cta"><span>Pedí la tuya</span><small>hasta el jueves 15/10 · $27.000</small></div>"""
    return pagina(1080, 1920, cuerpo, f"""
body{{background:{BIROME};color:#fff;padding:220px 80px 300px;display:grid;grid-template-rows:auto 1fr auto;justify-items:start}}
.medio{{align-self:center;display:grid;gap:36px}}
h1{{font-size:128px}}
.mano{{font-size:120px;color:#FF8A9B;transform:rotate(-3deg);transform-origin:left}}
.txt{{font-size:44px;line-height:1.4;color:#DCE3FF;max-width:820px}}
.cta{{background:{MALVON};border-radius:999px;padding:34px 60px;display:grid;gap:4px;justify-self:stretch;text-align:center}}
.cta span{{font:800 60px 'Bricolage Grotesque'}}
.cta small{{font-size:32px}}""")


def exportar(nombre):
    w, h, fn = PIEZAS[nombre]
    html = AQUI / f"{nombre}.html"
    html.write_text(fn(), encoding="utf-8")
    png = EXPORT / f"{nombre}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h}", "--virtual-time-budget=8000", f"--screenshot={png}", html.as_uri()],
                   check=True, capture_output=True)
    print("ok", png.name)


if __name__ == "__main__":
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    for n in PIEZAS:
        if filtro in n:
            exportar(n)
