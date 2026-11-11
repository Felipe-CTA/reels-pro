# Color y recorte de la persona

## Gradación

- "Más cálido" = `sepia` baja (0,1–0,2) + `saturate` 1,05–1,1 + `hue-rotate` −4 a −6°, aplicado **igual a toda la imagen**.
- Nunca tiñas a la persona con el color de la línea gráfica. Si la referencia tiene la habitación roja, la piel tiene que seguir viéndose natural.

## Recortar a la persona

Se necesita para palabras detrás de la cabeza, siluetas y fondos de otro color.

```bash
npx hyperframes remove-background video.mp4 -o persona.webm --quality best   # ~2–3 cuadros/s en CPU
```

Ponlo en dos capas con **las mismas transformaciones** de cámara: fondo (`video` completo) → elementos "detrás" → persona (`persona.webm`).

## El problema de teñir el fondo distinto que a la persona

Si el fondo lleva un color (por ejemplo azul) y la persona otro (natural), cualquier fallo del recorte deja ver la capa de abajo, **que también contiene a la persona** pintada de ese color:

- **Línea clara alrededor del pelo y las orejas**: píxeles de pared pegados al borde.
- **Resplandor de color en los dedos** al mover la mano rápido: el modelo no reconoce como persona la mano con desenfoque de movimiento.
- **Micrófono, escritorio o brazos que cambian de color** al cruzarse.

Opciones, de más segura a más arriesgada:

1. **Fondo y persona con la misma gradación** (habitación natural) y la línea gráfica en textos, pantallas, destellos y transiciones. No hay ningún error de bordes. **Es la recomendada.**
2. Fondo teñido + persona natural con el borde del recorte encogido 2–3 px y suavizado (`erosion` ×3 + `gblur=1.4` sobre el canal alfa). Quita la línea clara, pero no resuelve las manos rápidas.
3. Pared vacía reconstruida (mediana temporal de los cuadros donde el recorte dice "fondo") y recorte por diferencia con esa pared. Solo con cámara fija. Puede dejar huecos o trazos sueltos: pruébalo en los momentos de movimiento y enséñaselo a la persona antes de aplicarlo.

Antes de prometer un fondo de otro color, enséñale a la persona un acercamiento a una mano en movimiento y a la oreja.

## Comprobar

- Recorta la zona de la cara y de las manos en 6–8 momentos con gestos rápidos **del video renderizado** y míralas ampliadas.
- Los bordes que no se ven en una captura fija sí se ven en el móvil al reproducir: revisa también los cuadros intermedios de un gesto (cada 0,1 s).
