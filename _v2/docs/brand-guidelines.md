# Tu Canción: guía de marca

Fuente única de la marca, versión 2.0 (03/10/2026). Reemplaza a la identidad 1.0 (birome y malvón), que quedó archivada en `marca/_v1/`. La misma guía está publicada como sistema de diseño en Claude ("Tu Canción Design System"); cuando cambie algo, se edita en los dos lados.

## La idea

Un casete grabado para alguien. Antes de las playlists, regalar música era grabar un casete, escribirle "para vos" en la etiqueta con marcador y entregarlo en mano. Tu Canción hace eso mismo hoy: una canción con la historia de quien la recibe.

El casete tiene dos lados, y la marca también:

| | Qué es | Dónde vive |
|---|---|---|
| **Lado A** | Canciones a medida | tucancion.com.ar |
| **Lado B** | Fotos restauradas | restauraciondefotos.com.ar |
| **Lado A + B** | El combo: canción y video con las fotos | las dos webs |

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

## Color

Dos temas con los mismos cuatro colores. **Yema** es el de todos los días: fondo amarillo y tinta negra. **Cinta** lo invierte: fondo negro y títulos amarillos, para posts que tienen que destacarse y para la marca sobre video.

- `yema` (#FFD23F) es el color por el que se nos reconoce. Ocupa la mayor parte de cada pieza, como `ground` o como `display` sobre cinta.
- `cinta` (#1A1712) es el texto y el logo. Sobre yema da 12,4:1.
- `etiqueta` (#FFFAEB) es el papel de la etiqueta del casete: tarjetas, listas de precios y secciones largas de texto en la web.
- `rec` (#D7301F) es el botón de grabar. Aparece **una sola vez por pieza**: el botón, el precio del combo o la duración de la canción. Como texto solo va sobre etiqueta; sobre yema solo desde 24 px o como forma.

Nunca texto blanco sobre yema, ni texto yema sobre etiqueta. En los componentes usá los tokens con rol (`ground`, `ink`, `surface`, `accent`, `button`), no los colores sueltos, para que el tema cinta funcione sin tocar nada.

## Tipografía

Una sola familia para casi todo, **Archivo**, en dos anchos, más una fuente de marcador. Las dos son gratuitas y están en Google Fonts y en Canva.

- **Títulos y precios:** Archivo a peso 800 o 900 y ancho 125% (`font-stretch: 125%`, "Archivo Expanded" en Canva). Minúsculas en el logo; mayúscula inicial normal en los títulos. Estilos `display-xl`, `display-lg`, `display-md`, `precio`.
- **Texto:** Archivo a ancho normal, peso 400 a 600. Estilos `body-lg`, `body`, `label`.
- **A mano:** Permanent Marker, estilo `hand`. Solo para lo que alguien escribiría en la etiqueta del casete: una dedicatoria de 2 a 5 palabras. Nunca para títulos, precios ni párrafos.

Para cargar las fuentes en una web:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Permanent+Marker&display=swap">
```

Escala para un post de 1080 px de ancho: multiplicá los tamaños de los estilos por 2,57 (título de 108 a 118 px, texto de 38 a 46 px, dedicatoria de 113 px).

## El casete y sus partes

El motivo de la marca es el casete, y se usa por partes:

- **El símbolo** (el casete entero) es el logo y el avatar.
- **La etiqueta** (componente EtiquetaCasete) lleva la dedicatoria a mano. Una por pieza.
- **Los lados** (componente EtiquetaLado) dicen si algo es canción o foto.
- **Los renglones**: líneas de 2 px en `line`, como los de la etiqueta, para separar filas. No se usan otros adornos.

Esquinas: `radius-sm` (4 px) en etiquetas, `radius-md` (6 px) en tarjetas y botones. Sin sombras ni degradados.

## Imágenes

- **Fotos:** siempre el antes y el después lado a lado (componente AntesDespues), con el mismo encuadre. En reels, con un deslizador.
- **Canciones:** video vertical con la letra subtitulada en Archivo sobre fondo cinta y el casete girando.
- Las fotos, las voces y las historias de los clientes se publican solo con su permiso por escrito.
- Las vistas previas que se mandan antes de entregar llevan `tc-simbolo-tinta` como marca de agua.

## Componentes

No hay componentes de React: son clases de `components/bundle.css` sobre HTML común, y usan las variables de `tokens.css`.

| Componente | Clases | Para qué |
|---|---|---|
| Logo | archivos del grupo Logos | La marca, en todas sus versiones |
| Boton | `tc-btn`, `tc-btn--secundario` | El pedido por WhatsApp |
| EtiquetaLado | `tc-lado`, `tc-tag`, `tc-tag--b` | Lado A, Lado B |
| EtiquetaCasete | `tc-etiqueta` y sus partes | La dedicatoria a mano |
| ListaPrecios | `tc-precios` y sus filas | Precios publicados |
| AntesDespues | `tc-antes-despues`, `tc-foto` | Restauraciones |

Para usar el sistema en una página: cargá las fuentes, después `tokens.css` y `components/bundle.css`, y poné `data-theme="yema"` o `data-theme="cinta"` en el elemento que querés tematizar.

## Control antes de publicar

- Voseo y frases cortas, sin exageraciones.
- Un solo llamado a la acción, y la fecha límite (15/10) si es para el Día de la Madre.
- Yema, cinta y etiqueta; rec una sola vez.
- Una sola dedicatoria a mano por pieza.
- Usuario @tucancion.com.ar bien escrito.
- Permiso del cliente si aparece su foto, su voz o su historia.

## Archivos

```
marca/
  docs/brand-guidelines.md         esta guía
  assets/design-tokens.json|css    tokens para la web y para Canva
  assets/componentes.css           clases de los componentes (tc-btn, tc-tag, tc-etiqueta, tc-precios, tc-foto)
  assets/logos/*.svg               logos maestros en vectores
  piezas/*.html                    fuentes de las piezas de redes
  export/*.png                     piezas finales con tamaño exacto
  _v1/                             identidad anterior, archivada
web/
  tucancion/index.html             landing de tucancion.com.ar
  restauraciondefotos/index.html   landing de restauraciondefotos.com.ar
```

Nombres de archivo: `tc-{pieza}-{ancho}x{alto}.png`, por ejemplo `tc-avatar-1080x1080.png`.
