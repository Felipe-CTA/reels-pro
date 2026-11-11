---
name: editor-reels
description: Edita un video vertical a cámara (talking head) y lo convierte en un reel 9:16 para Instagram, TikTok o Shorts, por niveles - corte de silencios sin comerse palabras, subtítulos palabra por palabra, motion graphics sincronizados con HyperFrames, efectos de sonido, música, color y audio a -14 LUFS - con capturas de aprobación antes de cada render y verificación automática al final. Incluye dos estilos de referencia listos (UI claro azul y tipografía cinética oscura) y un método para copiar el estilo de cualquier reel de referencia. Úsala cuando alguien pida "edita mi reel", "convierte este video en un reel", "corta los silencios", "ponle subtítulos/gráficos/efectos", "edítalo como este ejemplo", "hazlo estilo X", o entregue un .mp4/.mov vertical para editar.
---

# Editor de reels por niveles

Convierte un video crudo grabado a cámara en un reel vertical profesional. El trabajo avanza por **niveles**: cada nivel produce un archivo exportado (`nivel1.mp4`, `nivel2.mp4`…) para que la persona compare, apruebe o vuelva atrás. No saltes niveles salvo que la persona lo pida.

## Reglas que no se negocian

1. **Ninguna palabra comida.** Después de cada corte, retranscribe y compara palabra por palabra contra el original (`scripts/compare_words.py`). Si una palabra "falta", transcribe solo ese fragmento antes de declarar el error: el transcriptor a veces se salta palabras que sí están.
2. **La cara nunca tapada.** Gráficos y subtítulos van por encima de la cabeza o por debajo del mentón. Mide la cara (`scripts/face_track.py`) y comprueba que nada la pise.
3. **Zonas de la interfaz de Instagram libres** (lienzo 1080×1920): nada importante en los 220 px de arriba, los 420 px de abajo ni la franja derecha de 150 px.
4. **Ninguna imagen quieta más de 1,5 s.** Zoom distinto en cada corte más un empuje lento continuo. Verifícalo con `scripts/motion_check.py`.
5. **Capturas antes de renderizar.** Antes de cada render largo, muestra una captura por escena numerada (E1, E2…) con las zonas de Instagram marcadas y **espera el OK**.
6. **Audio final a −14 LUFS** con pico ≤ −1,5 dBTP, y la voz siempre por encima de música y efectos (margen mínimo de 8 dB en cada palabra, `scripts/voice_margin.py`).
7. **No inventes datos sin avisar.** Si pones usuarios, nombres, cifras o comentarios de ejemplo en un gráfico, dilo en el mensaje para que la persona los cambie. Confirma la ortografía de nombres propios (el transcriptor suele equivocarse con ellos).
8. **Nunca sobrescribas una versión aprobada.** Si una corrección empeora el resultado, la persona tiene que poder volver a la anterior: guarda las variantes con otro nombre.

## Requisitos

- `ffmpeg` y `ffprobe` (en ffmpeg ≥ 9 el script de filtros se pasa con `-/filter_complex archivo.txt`).
- Python 3.10+ en un entorno virtual con `faster-whisper numpy opencv-python-headless<5` (OpenCV 5 eliminó `CascadeClassifier`, que usa `face_track.py`).
- HyperFrames CLI para los gráficos: `npm i hyperframes` en una carpeta de trabajo, luego `npx hyperframes --help`. Si la persona no quiere HyperFrames, los niveles 1 y 3 funcionan solo con ffmpeg.
- Música y efectos: los aporta la persona, o se buscan en una biblioteca de audio con licencia. Si hay un conector de audio disponible (por ejemplo, uno con una herramienta de búsqueda de música y efectos), úsalo. **Nunca guardes en archivos del proyecto URLs firmadas ni claves**: descarga el audio y referencia el archivo local.

## Los niveles

Lee `references/niveles.md` para el detalle de cada uno. Resumen:

| Nivel | Qué hace | Entrega |
|---|---|---|
| 1 · Corte | Transcripción por palabra, silencios > 0,3 s fuera con 80 ms de margen, tomas repetidas fuera, verificación palabra por palabra | `nivel1.mp4` + duración antes/después + lista de palabras desaparecidas |
| 2 · Gráficos | Subtítulos palabra por palabra con la palabra clave resaltada, un gráfico por idea que entra justo antes de decirla, zoom en cada corte | Capturas E1…En → OK → `nivel2.mp4` |
| 3 · Sonido y color | Pop suave en cada entrada de gráfico, whoosh en cada transición, música opcional, color algo más cálido, −14 LUFS | `nivel3.mp4` |
| 4 · Estilo de referencia | Analiza un reel de referencia (fotogramas 1/s y cuadro a cuadro en transiciones), escribe una ficha de estilo y reconstruye escenas con ese movimiento, con el contenido y los colores de la persona | Ficha + capturas → OK → `nivel4.mp4` |
| Final · Revisión | Lista de verificación completa con evidencia medida | Tabla cumple / no cumple |

## Estilos incluidos

- `references/estilo-ui-claro.md`: **UI claro azul**. Subtítulos pequeños de tenue a blanco, palabra clave en serif itálica, panel azul con rayos de luz, pantalla dividida, carrusel, tarjetas blancas, entradas de desenfoque a nítido sin rebote.
- `references/estilo-cinetico.md`: **tipografía cinética oscura**. Palabras que entran de lado con estela, texto curvo en arco, palabras gigantes detrás de la persona, título que se arma desde ruido, pantallas 3D inclinadas, flashes, glitch y 1–2 efectos de sonido por segundo.
- `references/analizar-referencia.md`: cómo extraer y escribir la ficha de cualquier reel que la persona traiga como ejemplo. **No copies textos, logos ni imágenes de la referencia**: copia el lenguaje de movimiento, el ritmo y la estructura.

## Audio, color y recortes

- `references/audio.md`: cadena de mejora de voz, mezcla con música y efectos, ducking, normalización y los errores que más se notan.
- `references/color-y-recorte.md`: gradación, recorte de la persona y por qué **teñir el fondo distinto que a la persona suele romper los bordes**. Lee esto antes de prometer un fondo de otro color.
- `references/hyperframes-notas.md`: errores frecuentes de HyperFrames y cómo evitarlos.

## Cierre de cada nivel

Al terminar un nivel informa en español claro (o en el idioma de la persona):

- la ruta del archivo exportado, su duración y su nivel en LUFS;
- qué se comprobó y con qué resultado (palabras, cara, zonas, movimiento, margen de voz);
- qué **no** se comprobó (por ejemplo: "no lo he reproducido completo");
- qué datos son inventados o dudosos.
