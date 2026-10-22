# Restauración de fotos: guía de marca

Fuente única de la marca Restauración de fotos, versión 1.0 (04/10/2026). Restauración de fotos antiguas, para regalar o para volver a colgarlas. Es una marca con sistema propio, hermana de Tu Canción.

## La idea

Una foto vieja vuelve a su lugar en el álbum. El motivo de la marca es el **esquinero de álbum**: dos esquinas rojas, arriba a la izquierda y abajo a la derecha, que sostienen lo que importa. Sostienen el nombre en el logo y sostienen el antes y el después en cada pieza.

El sistema sirve **todo el año y para cualquier motivo**: un cumpleaños, un aniversario, una reunión familiar, tener cerca a alguien que ya no está. La base no nombra ninguna fecha. Las fechas (Día de la Madre, Navidad, Día del Padre) son **campañas**: una capa que se pone unos días y se saca. Ver la sección Campañas.

## Relación con Tu Canción

Tu Canción (canciones a medida, tucancion.com.ar) es el servicio hermano, del mismo dueño, con su propio logo, sus propios colores y su propio sistema ("Tu Canción Design System"). Acá no se usan ni su disco ni su azul.

Lo que se comparte: las tipografías, la forma de hablar, la promesa de vista previa y plazo exacto, y el combo (canción y video con fotos), que se vende en las dos webs. El enlace entre las dos es una línea de texto en el pie: "¿Y una canción con su historia? tucancion.com.ar".

En redes tiene su propia cuenta, **@restauraciondefotos** (Instagram y Facebook, desde el 15/10, D-58), y su web es **restauraciondefotos.com.ar** (D-57).

## Para quién y qué prometemos

- **Para quién:** personas de 25 a 55 años que tienen una foto querida en mal estado, propia o de la familia.
- **Promesa:** esa foto de siempre, como nueva.
- **Lo que nos distingue:** vista previa antes de entregar, plazo exacto de 48 horas, precios publicados, una corrección incluida y respeto por las caras (si la restauración cambia los rasgos, se descarta).
- **Personalidad:** cálida, clara, de barrio, cuidadosa. Ni cursi ni tecnológica.

## Cómo hablamos

Voseo rioplatense y frases cortas. Primero lo que recibe la persona, después cómo se hace.

| Somos | Decimos | No decimos |
|---|---|---|
| Cálidos | "Mandanos la foto como la tengas" | "Suba su archivo" |
| Claros | "En 48 horas te mostramos cómo quedó" | "Entrega rápida garantizada" |
| Honestos | "Si la cara está destruida no la hacemos, porque habría que inventarla" | "Recuperamos cualquier foto" |
| Cuidadosos | "Las borramos a los 30 días y nunca las publicamos sin tu permiso" | Mostrar fotos de clientes sin avisar |

Mensajes de la base, que valen todo el año:

- **Frase principal:** Esa foto de siempre, como nueva.
- **Para qué:** Para regalarla enmarcada, para compartirla con la familia o para volver a colgarla en la pared.
- **Cierre:** Esa foto que está en un cajón puede volver a la pared.
- **Llamado a la acción, uno solo por pieza:** "Mandanos la foto".

Los mensajes de una fecha puntual viven en la campaña, no acá.

## Logo

"restauración de fotos" en minúsculas: "restauración" en ExtraBold y "de fotos" en Regular, entre dos esquineros de álbum en rec. Los archivos y las reglas están en el componente Logo y en el grupo Logos.

## Color

Dos temas con la misma paleta. **Yema** es el de todos los días: fondo amarillo y tinta negra. **Cinta** lo invierte: fondo negro y títulos amarillos, que es donde mejor se ven las fotos. En los componentes usá los tokens con rol (`ground`, `ink`, `display`, `surface`, `accent`, `button`).

- `yema` (#FFD23F) es el color por el que se reconoce la marca. Nunca lleva texto blanco encima.
- `cinta` (#1A1712) es el texto, el logo y el fondo de las piezas con fotos.
- `etiqueta` (#FFFAEB) son las tarjetas, las listas de precios y las secciones largas de texto en la web.
- `rec` (#D7301F) son los esquineros, el botón y el precio del combo. Como texto solo va sobre etiqueta; sobre yema solo desde 24 px o como forma.

## Tipografía

Las mismas tres familias que Tu Canción, gratuitas, en Google Fonts y en Canva.

- **Títulos, logo y precios:** Bricolage Grotesque. ExtraBold (800) para títulos y precios, Bold (700) para subtítulos, botones y etiquetas, Regular (400) para el "de fotos" del logo. Estilos `display-xl`, `display-lg`, `display-md`, `precio`, `tag`.
- **Texto:** Figtree, de 400 a 700. Estilos `body-lg`, `body`, `label`.
- **A mano:** Reenie Beanie, estilo `hand`. Solo para un epígrafe de foto de 2 a 6 palabras, como escrito al dorso ("Mamá, verano del 74"). Es opcional y va una sola vez por pieza.

Para cargar las fuentes en una web:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Figtree:wght@400..800&family=Reenie+Beanie&display=swap">
```

Escala para un post de 1080 px de ancho: títulos de 104 a 112 px, texto de 42 a 52 px, pie de 34 px.

## Motivos

- **El esquinero de álbum**: en rec, siempre de a dos (arriba a la izquierda y abajo a la derecha). Sostiene el logo, el par de fotos o una foto sola. No se usa como adorno suelto.
- **El antes y el después** (componente AntesDespues): las dos fotos lado a lado, con el mismo encuadre.
- **Los renglones**: líneas de 2 px en `line` para separar filas y bordear tarjetas. No se usan sombras ni degradados.

Esquinas: `radius-sm` (4 px) en etiquetas y fotos, `radius-md` (6 px) en tarjetas y botones, `radius-lg` (12 px) en el marco que agrupa dos fotos.

## Movimiento

Nada se mueve por su cuenta. Los botones cambian de color al pasar el cursor (150 ms). En reels, el antes y el después se muestran con un deslizador.

## Imágenes

- Siempre el antes y el después lado a lado, con el mismo encuadre y sin filtros.
- Las fotos de los clientes son datos personales: se borran a los 30 días y se publican solo con su permiso por escrito.
- Las vistas previas que se mandan antes de entregar llevan `rf-simbolo` como marca de agua.
- No se usan fotos de banco de imágenes como si fueran restauraciones.

## Componentes

No hay componentes de React: son clases de `components/bundle.css` sobre HTML común, y usan las variables de `tokens.css`.

| Componente | Clases | Para qué |
|---|---|---|
| Logo | `rf-wm` y los archivos del grupo Logos | La marca |
| Boton | `rf-btn`, `rf-btn--secundario` | El pedido por WhatsApp |
| AntesDespues | `rf-antes-despues`, `rf-foto`, `rf-tag` | Restauraciones |
| ListaPrecios | `rf-precios` y sus filas | Precios publicados |
| AvisoCampana | `rf-aviso` | La franja de una campaña en la web |

Para usar el sistema en una página: cargá las fuentes, después `tokens.css` y `components/bundle.css`, y poné `data-theme="cinta"` en el bloque que va sobre fondo negro.

## Control antes de publicar

- Voseo y frases cortas, sin exageraciones.
- Un solo llamado a la acción.
- ¿Es pieza base o de campaña? La base no nombra fechas; la de campaña lleva la fecha límite.
- Esquineros de a dos y rec una sola vez más (botón o precio).
- Contacto: restauraciondefotos.com.ar.
- Permiso del cliente por escrito si aparece su foto.

## Archivos

```
marca/restauracion-de-fotos/
  docs/brand-guidelines.md       esta guía
  docs/campanas.md               cómo se arma una campaña (Día de la Madre es el caso 1)
  assets/design-tokens.json|css  tokens para la web y para Canva
  assets/componentes.css         clases de los componentes
  assets/logos/*.svg             logos maestros en vectores
  piezas/*.html                  fuentes de las piezas base (sin fechas)
  export/*.png                   piezas base y logos con tamaño exacto
marca/campanas/                  piezas de cada campaña, de las dos marcas
web/restauraciondefotos/
  index.html                     la web con la campaña del Día de la Madre
  index-base.html                la web sin campaña: reemplaza a index.html después del 18/10
```
