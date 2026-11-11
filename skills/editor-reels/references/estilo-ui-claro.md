# Estilo A · UI claro azul

Lenguaje sobrio tipo "producto/SaaS". Funciona para explicar herramientas, procesos y ofertas.

## Movimiento

| Patrón | Detalle medido |
|---|---|
| Entrada principal | De desenfoque a nítido en **≈ 0,27 s** (8 cuadros a 30 fps): blur ~15 px → 0, opacidad 0 → 1, escala 0,96 → 1, subida de ~20 px. **Sin rebote.** |
| Curva | `expo.out` o `quart.out`: el 80 % del recorrido ocurre en el primer tercio. |
| Escalonado | 0,08–0,12 s entre piezas del mismo grupo. |
| Salidas | Corte seco o desenfoque + fundido de 0,15–0,2 s. |
| Subtítulos | Cada palabra nace al 25–35 % de opacidad con algo de blur y sube al 100 % en ≈ 0,2 s. |
| Transición de cámara | Desenfoque rápido de la cámara (3–4 cuadros) que vuelve a enfocar cuando entra el siguiente texto. |
| Después de entrar | Deriva mínima: los números siguen contando, la cámara sigue con un zoom lento. |

## Composiciones

- **Pantalla dividida**: panel azul arriba (≈ 40–45 % de la altura) que baja en 0,36 s; la cámara se desplaza hacia abajo sin tapar la cara. Dentro del panel van un título y una tarjeta blanca o dos clips de video como "posts".
- **Pantalla azul completa** solo para una palabra o un ícono con texto, ≈ 1 s. Avisa a la persona de que en esos tramos no se le ve la cara.
- **Carrusel**: una tarjeta centrada y las vecinas asomando más pequeñas y desenfocadas, con flechas ‹ › y puntos debajo; pasa de una a otra en 0,3 s.
- **Fila de íconos tipo app** (tarjetas blancas de esquinas redondeadas) bajo el subtítulo.

## Tipografía

- Sans limpia (Inter o similar), blanco, peso medio en el texto corrido y negrita en la palabra fuerte.
- **Palabra con carga emocional en serif itálica** (Instrument Serif o similar). Es la firma del estilo.
- Subtítulos pequeños, a la altura del pecho, 1–2 líneas.
- Si usas una fuente que no se resuelve sola, declara su `@font-face` con el `.woff2` dentro de `assets/`.

## Color

- Panel: degradado azul eléctrico con 4–5 rayos de luz diagonales suaves y una retícula muy tenue.
- Tarjetas: blanco puro, esquinas ≈ 24 px, sombra amplia y suave.
- Cámara: algo cálida, con la parte inferior oscurecida y ligeramente desenfocada para que el subtítulo respire.

## Sonido

Whoosh muy suave en cada corte, uno más marcado en los paneles y pantallas azules, pop en cada tarjeta, clic en cada paso de carrusel y tecleo en la caja de comentario. Música tranquila, minimalista y tecnológica, muy por debajo de la voz.
