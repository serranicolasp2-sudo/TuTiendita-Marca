# Tu Canción: guía de marca

Fuente única de la marca, versión 3.0 (04/10/2026). Reemplaza a la 2.0 (casete, Archivo), archivada en `marca/_v2/`; la 1.0 está en `marca/_v1/`. La misma guía está publicada como sistema de diseño en Claude ("Tu Canción Design System"); cuando cambie algo, se edita en los dos lados. Vuelve a las tipografías y al logo del disco de la 1.0, y mantiene la idea de Lado A y Lado B.

## La idea

Un disco tiene dos lados, y la marca también. Cada lado tiene su propia paleta, y los dos comparten el logo, las tipografías y la forma de hablar.

| | Qué es | Dónde vive | Paleta |
|---|---|---|---|
| **Lado A** | Canciones a medida | tucancion.com.ar | Birome, malvón, tinta, papel, plata |
| **Lado B** | Fotos restauradas | restauraciondefotos.com.ar | Yema, cinta, etiqueta, rec |
| **Lado A + B** | El combo: canción y video con las fotos | las dos webs | La del lado donde se muestra |

La marca paraguas es Tu Canción y usa el Lado A: el perfil de redes, WhatsApp, Mercado Libre y todo lo que hable de los dos servicios juntos va en birome y malvón. El Lado B se usa solo cuando la pieza o la página es de fotos.

Usuario en redes: **@tucancion.com.ar** (Instagram y TikTok). @tucancion.ar es de un competidor: escribí siempre el dominio completo.

## Para quién y qué prometemos

- **Para quién:** personas de 25 a 55 años que buscan un regalo con significado para la mamá, la abuela, la pareja o un amigo. Primera fecha fuerte: Día de la Madre, domingo 18/10/2026.
- **Promesa:** tu historia, hecha canción; esa foto de siempre, como nueva.
- **Lo que nos distingue:** vista previa antes de entregar, plazo exacto de 48 horas, precios publicados y una corrección incluida.
- **Personalidad:** cálida, clara, de barrio, cuidadosa. Ni cursi ni tecnológica.

## Cómo hablamos

Voseo rioplatense y frases cortas. Primero lo que recibe la persona, después cómo se hace.

| Somos | Decimos | No decimos |
|---|---|---|
| Cálidos | "Contanos dos o tres recuerdos de ella" | "Complete el formulario" |
| Claros | "Pedila hasta el jueves 15 y la tenés antes del domingo" | "Entrega rápida garantizada" |
| Honestos | "Hecha con inteligencia artificial y revisada por una persona" | "Compuesta por músicos profesionales" |
| Sobrios | Un emoji por línea como máximo, y solo en redes | Mayúsculas para gritar, signos repetidos |

Mensajes que se repiten tal cual:

- **Frase principal:** Tu historia, hecha canción.
- **Fotos:** Esa foto de siempre, como nueva.
- **Día de la Madre:** Ella te cantó toda la vida. Ahora te toca a vos.
- **Fecha límite:** Pedila hasta el jueves 15/10 y la tenés antes del Día de la Madre.
- **Llamado a la acción, uno solo por pieza:** "Pedí la tuya" para canciones, "Mandanos la foto" para fotos.

## Logo

"tu canción" en minúsculas, con la **ó hecha disco de vinilo** y la tilde como acento de color. En las webs el disco gira a 33 1/3 rpm (una vuelta cada 1,8 segundos); en las piezas fijas queda quieto. Los archivos y las reglas están en el componente Logo y en el grupo Logos.

## Color

Dos temas, uno por lado. En los componentes usá los tokens con rol (`ground`, `ink`, `display`, `surface`, `strong`, `accent`, `button`) y elegí el lado con `data-theme="lado-a"` o `data-theme="lado-b"`.

**Lado A, canciones**

- `papel` (#F6F7FA) es el fondo general: alrededor del 60% de la pieza.
- `birome` (#1E3C96) es el color principal: logo, títulos y bloques de fondo. Alrededor del 30%.
- `malvon` (#E0435C) es el acento: botón, precio del combo, dedicatoria. Alrededor del 10%. Como texto sobre blanco solo desde 24 px, o en negrita desde 19 px.
- `tinta` (#16205A) es el texto sobre papel y el fondo de la franja final de las webs.
- `plata` (#5F6679) es el texto secundario.

**Lado B, fotos**

- `yema` (#FFD23F) es el fondo principal. Nunca lleva texto blanco encima.
- `cinta` (#1A1712) es el texto, el logo y los fondos oscuros.
- `etiqueta` (#FFFAEB) son las tarjetas y las secciones largas de texto.
- `rec` (#D7301F) es el acento: botón, esquineros y precio del combo. Como texto solo sobre etiqueta.

No se mezclan los lados en una misma pieza, salvo las etiquetas de lado (Lado A en birome, Lado B en cinta y yema), que conservan su color en cualquier fondo.

## Tipografía

Tres familias, iguales en los dos lados. Son gratuitas y están en Google Fonts y en Canva.

- **Títulos, logo y precios:** Bricolage Grotesque. ExtraBold (800) para títulos y precios, Bold (700) para subtítulos, botones y etiquetas, Regular (400) solo para el "tu" del logo. Estilos `display-xl`, `display-lg`, `display-md`, `precio`, `tag`.
- **Texto:** Figtree, de 400 a 700. Estilos `body-lg`, `body`, `label`.
- **A mano:** Reenie Beanie, estilo `hand`. Solo dedicatorias de 2 a 6 palabras, como escritas con birome. El trazo es fino: nunca por debajo de 40 px, y en posts de 1080 px, entre 190 y 230 px.

Para cargar las fuentes en una web:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Figtree:wght@400..800&family=Reenie+Beanie&display=swap">
```

Escala para un post de 1080 px de ancho: títulos de 104 a 118 px, texto de 42 a 52 px, pie de 34 px.

## Motivos

- **El disco**: es la ó del logo, el avatar y el objeto que asoma de la funda. No se dibujan otros objetos (ni casetes, ni notas musicales).
- **La funda con dedicatoria** (componente Dedicatoria): solo en el Lado A, una por pieza.
- **Los lados** (componente EtiquetaLado): dicen si algo es canción, foto o combo.
- **El esquinero de álbum**: solo en el Lado B, en rec, sobre una de las dos fotos y en el logo de fotos.
- **Los renglones**: líneas de 2 px en `line` para separar filas y bordear tarjetas. No se usan sombras ni degradados.

Esquinas: `radius-sm` (4 px) en etiquetas y fotos, `radius-md` (6 px) en tarjetas y botones, `radius-lg` (12 px) en la funda.

## Movimiento

Lo único que se mueve por su cuenta es el disco, y solo en la web: gira a velocidad constante, una vuelta cada 1,8 segundos. Si la persona tiene activado "reducir movimiento", queda quieto. Los botones solo cambian de color al pasar el cursor (150 ms). No hay entradas animadas ni efectos al hacer scroll.

## Imágenes

- **Fotos:** siempre el antes y el después lado a lado (componente AntesDespues), con el mismo encuadre. En reels, con un deslizador.
- **Canciones:** video vertical con la letra subtitulada en Figtree sobre fondo birome y el disco girando.
- Las fotos, las voces y las historias de los clientes se publican solo con su permiso por escrito.
- Las vistas previas que se mandan antes de entregar llevan `tc-simbolo` como marca de agua.

## Componentes

No hay componentes de React: son clases de `components/bundle.css` sobre HTML común, y usan las variables de `tokens.css`.

| Componente | Clases | Para qué |
|---|---|---|
| Logo | `tc-wm`, `tc-disco`, `tc-gira` y los archivos del grupo Logos | La marca, con el disco que gira |
| Boton | `tc-btn`, `tc-btn--secundario` | El pedido por WhatsApp |
| EtiquetaLado | `tc-lado`, `tc-tag`, `tc-tag--b`, `tc-tag--ab` | Lado A, Lado B, combo |
| Dedicatoria | `tc-funda` y sus partes | La dedicatoria a mano |
| ListaPrecios | `tc-precios` y sus filas | Precios publicados |
| AntesDespues | `tc-antes-despues`, `tc-foto` | Restauraciones |

Para usar el sistema en una página: cargá las fuentes, después `tokens.css` y `components/bundle.css`, y poné `data-theme="lado-a"` o `data-theme="lado-b"` en el `<html>` o en el bloque que querés tematizar.

## Control antes de publicar

- Voseo y frases cortas, sin exageraciones.
- Un solo llamado a la acción, y la fecha límite (15/10) si es para el Día de la Madre.
- Un solo lado por pieza: birome y malvón, o yema y cinta.
- El acento (malvón o rec) una sola vez, y una sola dedicatoria a mano.
- Usuario @tucancion.com.ar bien escrito.
- Permiso del cliente si aparece su foto, su voz o su historia.

## Archivos

```
marca/
  docs/brand-guidelines.md         esta guía
  assets/design-tokens.json|css    tokens para la web y para Canva
  assets/componentes.css           clases de los componentes (tc-wm, tc-disco, tc-btn, tc-tag, tc-funda, tc-precios, tc-foto)
  assets/logos/*.svg               logos maestros en vectores
  piezas/*.html                    fuentes de las piezas de redes
  export/*.png                     piezas y logos finales con tamaño exacto
  _v1/ y _v2/                      identidades anteriores, archivadas
web/
  tucancion/index.html             landing de tucancion.com.ar (Lado A, con el disco que gira)
  restauraciondefotos/index.html   landing de restauraciondefotos.com.ar (Lado B)
```

Nombres de archivo: `tc-{pieza}-{ancho}x{alto}.png`, por ejemplo `tc-avatar-1080x1080.png`.
