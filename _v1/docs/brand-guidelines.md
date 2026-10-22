# Tu Canción: guía de marca

Fuente única de la marca. Cuando cambie algo, se edita acá y después se actualizan `assets/design-tokens.json` / `.css` y las piezas.
Versión 1.0, 03/10/2026.

## 1. Esencia
- **Qué hacemos:** canciones personalizadas para regalar (hechas con IA y revisadas por una persona) y restauración de fotos viejas, con impresión opcional enviada a domicilio.
- **Para quién:** personas de 25 a 55 años que buscan un regalo con significado para la mamá, la abuela, la pareja o un amigo. Primera fecha fuerte: el Día de la Madre (domingo 18/10/2026).
- **Promesa:** tu historia, hecha canción; esa foto de siempre, como nueva.
- **Personalidad:** cálida, clara, de barrio, cuidadosa. Ni cursi ni tecnológica.
- **Diferencial:** vista previa antes de entregar, plazos exactos (48 h), precios publicados y combo de canción + video con fotos.

## 2. Arquitectura
| Nivel | Nombre | Dominio | Uso |
|---|---|---|---|
| Marca | Tu Canción | tucancion.com.ar | Redes, WhatsApp, Mercado Libre |
| Línea | Tu Canción · Restauración de fotos | restauraciondefotos.com.ar | Web y publicaciones de fotos |
| Producto | El combo (canción + video con fotos) | las dos webs | La oferta principal para fechas especiales |

Usuario en redes: **@tucancion.com.ar** (Instagram y TikTok). **@tucancion.ar ya es de un competidor en Instagram**: no lo uses, no lo etiquetes y escribí siempre el dominio completo.

## 3. Voz y tono
Voseo rioplatense. Frases cortas. Primero lo que recibe la persona, después cómo se hace.

| Atributo | Es | No es |
|---|---|---|
| Cálida | "Contanos dos o tres recuerdos de ella" | "Complete el formulario" |
| Clara | "Pedila hasta el jueves 15 y la tenés antes del domingo" | "Entrega rápida garantizada" |
| Honesta | "Hecha con inteligencia artificial y revisada por una persona" | "Compuesta por músicos profesionales" (falso) |
| Sobria | Un emoji por línea, como máximo | "✨¡¡MAGIA!!✨", mayúsculas para gritar |

Según el canal:
- **Instagram y TikTok:** cercano; la emoción la ponen las historias de los clientes.
- **Mercado Libre:** descriptivo; qué incluye, plazos y cómo se pide.
- **WhatsApp:** conversación de persona a persona, con respuestas cortas.

## 4. Mensajes
- **Frase principal:** Tu historia, hecha canción.
- **Fotos:** Esa foto de siempre, como nueva.
- **Día de la Madre:** Ella te cantó toda la vida. Ahora te toca a vos.
- **Pruebas que respaldan los mensajes:** vista previa con marca de agua antes de la entrega final; 1 corrección incluida; entrega en 48 h; precios publicados.
- **Llamado a la acción, siempre uno solo:** "Pedí la tuya" (canción), "Mandanos la foto" (fotos).

Precios aprobados (D-03): canción $27.000 · foto $6.500 · 3 fotos $15.900 · combo $59.900. Impresión: costo + recargo (D-06).

## 5. Logo
- **Logotipo:** "tu canción" en minúsculas, Bricolage Grotesque ExtraBold. "tu" va en Regular color birome y la **ó es un disco de vinilo con la tilde en malvón**.
- **Símbolo (avatar):** el disco con la tilde, blanco sobre círculo birome.
- **Línea de fotos:** el logotipo más "Restauración de fotos" con un esquinero de álbum en malvón.
- **Espacio libre:** igual a la altura del disco por cada lado. **Tamaño mínimo:** 120 px de ancho para el logotipo y 32 px para el símbolo.
- **No:** deformarlo, rotarlo, ponerle sombra o degradé, escribirlo en mayúsculas, ni cambiar los colores fuera de las versiones aprobadas: sobre papel, sobre birome y sobre malvón (en esta última, la tilde y la etiqueta del disco van en birome).

## 6. Color
| Token | Nombre | Hex | Uso | Proporción |
|---|---|---|---|---|
| color.primary | Birome | #1E3C96 | fondos, logo, títulos | 30% |
| color.accent | Malvón | #E0435C | botón, precio, dedicatoria | 10% como máximo |
| color.ink | Tinta | #16205A | texto sobre papel | — |
| color.paper | Papel | #F6F7FA | fondo general | 60% |
| color.silver | Plata | #5F6679 | texto secundario, el "antes" | — |

Contraste: tinta sobre papel es 14,1:1, blanco sobre birome 9,8:1 y plata sobre papel 5,4:1; todos cumplen AA. El malvón sobre blanco (4,1:1) se usa solo en textos de 24 px o más, o para elementos que no son texto.

## 7. Tipografía (todas gratuitas en Google Fonts y Canva)
| Rol | Fuente | Pesos | Escala para posts de 1080 px |
|---|---|---|---|
| Logo y títulos | Bricolage Grotesque | 400 / 600 / 800 | 72–120 px |
| Texto y precios | Figtree | 400 / 500 / 600 | 32–40 px |
| Dedicatoria a mano | Reenie Beanie | 400 | 80–120 px, solo frases de 2 a 6 palabras |

## 8. Imágenes
- **Fotos:** siempre se muestran el antes y el después lado a lado, o con un deslizador en el reel. Nunca se publica la foto de un cliente sin su permiso por escrito.
- **Canciones:** video vertical con la letra subtitulada en Figtree y el disco girando. Las reacciones de los clientes, solo con su permiso.
- **Esquinas:** radio de 6 px en tarjetas. Las fotos llevan esquineros de álbum en lugar de esquinas redondeadas.

## 9. Archivos
```
marca/
  docs/brand-guidelines.md       ← esta guía
  assets/design-tokens.json|css  ← tokens para la web y Canva
  piezas/*.html                  ← fuentes de las piezas
  export/*.png                   ← piezas finales con tamaño exacto
  manual-de-marca.html           ← manual visual
```
Nombres de archivo: `tc-{pieza}-{formato}-{ancho}x{alto}.png`, por ejemplo `tc-avatar-1080x1080.png`.

## 10. Control antes de publicar
- [ ] Voseo y frases cortas, sin exageraciones
- [ ] Un solo llamado a la acción y la fecha límite (15/10) si es para el Día de la Madre
- [ ] Colores y fuentes de esta guía, con el malvón en un 10% como máximo
- [ ] Usuario @tucancion.com.ar bien escrito
- [ ] Permiso del cliente si aparece su foto, su voz o su historia
