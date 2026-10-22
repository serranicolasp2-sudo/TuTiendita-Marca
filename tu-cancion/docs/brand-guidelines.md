# Tu Canción: guía de marca

Fuente única de la marca Tu Canción, versión 4.0 (04/10/2026). Canciones a medida para regalar. Restauración de fotos dejó de ser un tema de este sistema y tiene el suyo propio ("Restauración de Fotos Design System").

## La idea

Una canción original con la historia de quien la recibe, entregada como se regalaba la música: un disco en su funda, con una dedicatoria escrita a mano. El disco es la ó del logo; la funda con la dedicatoria es lo que cambia de un regalo a otro.

El sistema sirve para **cualquier regalo**: una pareja, la mamá, el viejo, una amiga, un cumpleaños, un aniversario o porque sí. La base no nombra ninguna fecha. Las fechas (Día de la Madre, Navidad, San Valentín) son **campañas**: una capa que se pone unos días y se saca. Ver la sección Campañas.

## Lado A y Lado B

Tu Canción y Restauración de fotos son dos servicios hermanos, del mismo dueño, cada uno con su marca, su web y su sistema. Se nombran como los lados de un disco solo para enlazarse:

| | Qué es | Dónde vive | Sistema |
|---|---|---|---|
| **Lado A** | Canción con tu historia | tucancion.com.ar | Este |
| **Lado B** | Fotos restauradas | restauraciondefotos.com.ar | Restauración de Fotos Design System |
| **Lado A + B** | El combo: canción y video con las fotos | Se vende en las dos webs | El de la web donde se muestra |

En Tu Canción, el Lado B aparece solo como etiqueta (negra y amarilla) en un enlace o en una lista de precios conjunta.

Usuario en redes: **@tucancion.com.ar** (Instagram y TikTok). @tucancion.ar es de un competidor: escribí siempre el dominio completo.

## Para quién y qué prometemos

- **Para quién:** personas de 25 a 55 años que buscan un regalo con significado para alguien cercano.
- **Promesa:** tu historia, hecha canción.
- **Lo que nos distingue:** se escucha antes de regalarla, plazo exacto de 48 horas, precios publicados y hasta 5 cambios incluidos (un minuto de vista previa por cada versión).
- **Personalidad:** cálida, clara, de barrio, cuidadosa. Ni cursi ni tecnológica.

## Cómo hablamos

Voseo rioplatense y frases cortas. Primero lo que recibe la persona, después cómo se hace.

| Somos | Decimos | No decimos |
|---|---|---|
| Cálidos | "Contanos dos o tres recuerdos de esa persona" | "Complete el formulario" |
| Claros | "En 48 horas la tenés para escucharla" | "Entrega rápida garantizada" |
| Honestos | "Hecha con inteligencia artificial y revisada por una persona" | "Compuesta por músicos profesionales" |
| Sobrios | Un emoji por línea como máximo, y solo en redes | Mayúsculas para gritar, signos repetidos |

Mensajes de la base, que valen todo el año:

- **Frase principal:** Tu historia, hecha canción.
- **Para quién:** Para tu pareja, tu mamá, tu viejo o una amiga. Para un cumpleaños, un aniversario o porque sí.
- **Ocasiones:** Una canción para cada historia.
- **Cierre:** Regalá algo que nadie más puede regalar.
- **Llamado a la acción, uno solo por pieza:** "Pedí la tuya".

Los mensajes de una fecha puntual viven en la campaña, no acá.

## Logo

"tu canción" en minúsculas, con la **ó hecha disco de vinilo** y la tilde como acento de color. En la web el disco gira a 33 1/3 rpm (una vuelta cada 1,8 segundos); en las piezas fijas queda quieto. Los archivos y las reglas están en el componente Logo y en el grupo Logos.

## Color

Dos temas con la misma paleta. **Papel** es el de todos los días: fondo claro y títulos en birome. **Birome** lo invierte: fondo azul y texto blanco, para posts que tienen que destacarse. En los componentes usá los tokens con rol (`ground`, `ink`, `display`, `surface`, `accent`, `button`).

- `papel` (#F6F7FA) es el fondo general: alrededor del 60% de la pieza.
- `birome` (#1E3C96) es el color principal: logo, títulos y fondos. Alrededor del 30%.
- `malvon` (#E0435C) es el acento: botón, precio del combo, dedicatoria y aviso de campaña. Alrededor del 10%. Como texto sobre blanco solo desde 24 px, o en negrita desde 19 px. Un post de precios puede ir entero sobre malvón, con texto blanco grande.
- `tinta` (#16205A) es el texto sobre papel y el fondo de la franja final de la web.
- `plata` (#5F6679) es el texto secundario.

## Tipografía

Tres familias, gratuitas, en Google Fonts y en Canva.

- **Títulos, logo y precios:** Bricolage Grotesque. ExtraBold (800) para títulos y precios, Bold (700) para subtítulos, botones y etiquetas, Regular (400) solo para el "tu" del logo. Estilos `display-xl`, `display-lg`, `display-md`, `precio`, `tag`.
- **Texto:** Figtree, de 400 a 700. Estilos `body-lg`, `body`, `label`.
- **A mano:** Reenie Beanie, estilo `hand`. Solo dedicatorias de 2 a 6 palabras, como escritas con birome. El trazo es fino: nunca por debajo de 40 px, y en posts de 1080 px, entre 180 y 230 px.

Para cargar las fuentes en una web:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Figtree:wght@400..800&family=Reenie+Beanie&display=swap">
```

Escala para un post de 1080 px de ancho: títulos de 104 a 118 px, texto de 42 a 52 px, pie de 34 px.

## Motivos

- **El disco**: es la ó del logo, el avatar y el objeto que asoma de la funda. No se dibujan otros objetos (ni casetes, ni notas musicales).
- **La funda con dedicatoria** (componente Dedicatoria): es donde entra la ocasión. La dedicatoria va a mano sobre renglones de tinta, como la etiqueta de un disco, con "Lado A" y la duración arriba. La base dice "Para vos".
- **Los lados** (componente EtiquetaLado): Lado A, Lado A + B y, para enlazar, Lado B.
- **Los renglones**: líneas de 2 px en `line` para separar filas y bordear tarjetas, y los renglones donde se apoya la dedicatoria. No se usan sombras ni degradados.

Esquinas: `radius-sm` (4 px) en etiquetas, `radius-md` (6 px) en tarjetas y botones, `radius-lg` (12 px) en la funda.

## Movimiento

Lo único que se mueve por su cuenta es el disco, y solo en la web: gira a velocidad constante, una vuelta cada 1,8 segundos. Si la persona tiene activado "reducir movimiento", queda quieto. Los botones solo cambian de color al pasar el cursor (150 ms). No hay entradas animadas ni efectos al hacer scroll.

## Imágenes

- Video vertical con la letra subtitulada en Figtree sobre fondo birome y el disco girando.
- Las voces y las historias de los clientes se publican solo con su permiso por escrito.

## Componentes

No hay componentes de React: son clases de `components/bundle.css` sobre HTML común, y usan las variables de `tokens.css`.

| Componente | Clases | Para qué |
|---|---|---|
| Logo | `tc-wm`, `tc-disco`, `tc-gira` y los archivos del grupo Logos | La marca, con el disco que gira |
| Boton | `tc-btn`, `tc-btn--secundario` | El pedido por WhatsApp |
| EtiquetaLado | `tc-lado`, `tc-tag`, `tc-tag--ab`, `tc-tag--b` | Lado A, combo, enlace al Lado B |
| Dedicatoria | `tc-funda`, `tc-funda__renglon`, `tc-funda--chica`, `tc-con-disco` | La dedicatoria a mano sobre renglones, por ocasión |
| ListaPrecios | `tc-precios` y sus filas | Precios publicados |
| AvisoCampana | `tc-aviso` | La franja de una campaña en la web |

Para usar el sistema en una página: cargá las fuentes, después `tokens.css` y `components/bundle.css`, y poné `data-theme="birome"` en el bloque que va sobre fondo azul.

## Control antes de publicar

- Voseo y frases cortas, sin exageraciones.
- Un solo llamado a la acción.
- ¿Es pieza base o de campaña? La base no nombra fechas; la de campaña lleva la fecha límite.
- Malvón una sola vez, y una sola funda por post.
- Usuario @tucancion.com.ar bien escrito.
- Permiso del cliente si aparece su voz o su historia.

## Archivos

```
marca/tu-cancion/
  docs/brand-guidelines.md       esta guía
  docs/campanas.md               cómo se arma una campaña (Día de la Madre es el caso 1)
  assets/design-tokens.json|css  tokens para la web y para Canva
  assets/componentes.css         clases de los componentes
  assets/logos/*.svg             logos maestros en vectores
  piezas/*.html                  fuentes de las piezas base (sin fechas)
  export/*.png                   piezas base y logos con tamaño exacto
marca/campanas/                  piezas de cada campaña, de las dos marcas
web/tucancion/
  index.html                     la web con la campaña del Día de la Madre
  index-base.html                la web sin campaña: reemplaza a index.html después del 18/10
```
