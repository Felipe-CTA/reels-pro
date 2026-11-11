# Estilo B · Tipografía cinética oscura

Lenguaje intenso, de mucho ritmo. Funciona para ganchos, anuncios de comunidad y lanzamientos.

## Movimiento

| Patrón | Detalle |
|---|---|
| Palabra que entra de lado | Desde ±700 px con `scaleX` 1,8 → 1 y blur 16 → 0 en **0,18 s**, `expo.out`. Las palabras de un mismo bloque alternan el lado de entrada. |
| Bloque que empuja al anterior | Cuando entra el bloque nuevo, el anterior sale a latigazo hacia el lado contrario en 0,12 s. |
| Deriva | El bloque se desplaza ±14 px mientras está en pantalla; nunca queda quieto. |
| Texto curvo | Palabras sobre un arco alrededor de la cabeza o bajo la barbilla, que barren a lo largo del arco en 0,22 s y luego rotan despacio. |
| Palabra gigante detrás de la persona | Requiere recortar a la persona. La palabra entra con escala 1,6 → 1 y blur. |
| Título desde ruido | Fondo negro; cada línea aparece en 6 cuadros recortada en franjas (clip-path) con desplazamiento, más separación de color rojo/cian. |
| Pantallas 3D | Plano oscuro en perspectiva (rotateX ~20°, rotateY ±22°) que entra en diagonal con blur y sigue escalando; dentro, clips, chat o tarjetas. |
| Transiciones | Latigazo de cámara (blur horizontal de 4 cuadros) en cada corte, flash blanco de 1–2 cuadros, bandas de luz que parpadean, negativo de 2 cuadros, temblor de 6 cuadros en los impactos. |
| Gancho | Silueta blanca y "rayos X" de 1 cuadro alternándose sobre la persona recortada. |

## Tipografía

- Sans de peso **black** con interletraje cerrado para lo fuerte; **itálica fina** para conectores ("se llama", "y tiene su").
- Acento con resplandor (text-shadow en tres capas) en un color cálido o frío según la línea gráfica; un segundo acento neón para lo negativo ("carísimas", "no").
- Serif itálica pesada con resplandor para una frase especial (un producto, un nicho).

## Color

- El estilo original tiñe la habitación de un color intenso (rojo/naranja) con negros aplastados, viñeta y grano.
- **La persona debe verse natural.** Lee `color-y-recorte.md` antes de teñir el fondo distinto que a la persona: los bordes del recorte delatan el truco al mover las manos. La variante más segura es la **habitación natural con los acentos de color en textos, pantallas y destellos**.

## Sonido

- Música trap/phonk o electrónica oscura de 125–155 BPM, continua.
- **1,5–2 efectos por segundo**: swish en las palabras fuertes (no en todas), whoosh en cada corte, glitch y estática en los títulos y negativos, impacto grave en los golpes (recorta su cola a < 1 s para que no tape las palabras siguientes), una subida con glitch antes del primer título.
