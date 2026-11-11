# HyperFrames: notas prácticas

Consulta siempre `npx hyperframes docs <tema>` y `npx hyperframes <comando> --help`: la CLI documenta su propia versión.

## Flujo

```bash
npx hyperframes init reel -e blank --non-interactive
# editar reel/index.html (1080×1920), copiar videos a reel/assets/
npx hyperframes check                     # debe terminar en "Check passed"
npx hyperframes snapshot --at 1.2,3.4 --no-end -o capturas
npx hyperframes render -f 30 -q delivery -o salida.mp4
```

Renderiza la imagen **sin audio** y mezcla el audio después con ffmpeg (`-c:v copy`). Así puedes ajustar la música sin volver a renderizar.

## Errores frecuentes

| Síntoma / error de `check` | Solución |
|---|---|
| `video_nested_in_timed_element` | Un `<video>` con `data-start` no puede ir dentro de otro elemento con `data-start`. Sácalo a nivel raíz y anima su contenedor sin tiempos. |
| `media_missing_id` (video congelado en el render) | Todo `<video>` temporizado necesita `id`. |
| `gsap_css_transform_conflict` | No pongas `transform` en el CSS de algo que GSAP anima; usa `gsap.set(...)` al cargar. |
| `font_family_without_font_face` | Copia el `.woff2` a `assets/fonts/` y declara `@font-face`. |
| `content_overlap` intencional | Atributo `data-layout-allow-overlap` en el elemento. |
| Un `fromTo` que empieza tarde se ve desde el segundo 0 | Añade `immediateRender:false`. |
| Un `tl.set` de 1 cuadro no aparece en la captura | Colócalo unos 12 ms antes del límite del cuadro. |
| La captura no muestra un efecto que sí se ve en el render | Reproduce el momento sobre el render final, no sobre la composición. |

## Composición

- Un único timeline GSAP en pausa registrado en `window.__timelines["main"]`, con lógica determinista (sin `Math.random()` ni `Date.now()`).
- Capas típicas: cámara (con `transform-origin:0 0` y zoom por corte) → elementos detrás → persona recortada → tinte/viñeta → gráficos → subtítulos → flashes y grano.
- Genera el HTML con un script (por ejemplo, Python) a partir de las marcas de las palabras: es mucho más fácil reajustar los tiempos que tocar el HTML a mano.
