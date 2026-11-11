# Los niveles en detalle

Cada nivel parte del archivo del nivel anterior. Trabaja en una carpeta temporal y exporta solo los entregables a la carpeta de la persona.

## Nivel 1 · Corte limpio (solo ffmpeg + Python)

1. **Transcribe con marcas por palabra**: `python scripts/transcribe.py crudo.mp4 palabras.json`.
   - Usa el modo literal (`--literal`) para detectar arranques en falso: la transcripción normal "limpia" las repeticiones y oculta las tomas duplicadas.
   - Desconfía del texto que aparece en silencios largos al final: Whisper puede inventar frases ("suscríbete al canal…") donde no se dijo nada. Si el texto cae en un tramo sin energía de audio, no existe.
2. **Detecta silencios** de más de 0,3 s (`silencedetect=noise=-40dB:d=0.3`) y córtalos dejando **80 ms de margen** a cada lado y un fundido de **10 ms** en cada unión para evitar clics: `python scripts/cut_silences.py crudo.mp4 nivel1.mp4`.
3. **Tomas repetidas**: busca frases dichas dos veces o arranques que se cortan y se retoman. Conserva la última toma completa, salvo que otra suene claramente mejor.
4. **Verifica**: retranscribe `nivel1.mp4` y compara (`scripts/compare_words.py`). Por cada diferencia, transcribe solo ese fragmento de 3 s para saber si la palabra falta de verdad o si fue un error del transcriptor. Entrega la lista.
5. Informa la duración antes y después.

## Nivel 2 · Subtítulos, gráficos y movimiento (HyperFrames)

- **Subtítulos** palabra por palabra durante todo el video, en grupos de 2–4 palabras, que cortan en signos de puntuación y en pausas de más de 0,25 s. Resalta **una** palabra clave por frase (color de acento y, si encaja, serif itálica).
- **Un gráfico por idea**, que entra 0,2–0,3 s **antes** de que se diga la palabra. Piezas típicas: tarjeta de perfil, contador que sube, flecha de proceso, burbuja de pensamiento, comentario de chat, lista de pasos, tarjeta de video, caja de comentario que se escribe sola (CTA "comenta X").
- **Movimiento de cámara**: un zoom distinto en cada corte (1,1×–1,5×, centrado en la cara) más un empuje lento del 4–5 % durante el plano.
- **Zonas**: gráficos por encima de la cabeza (≈ y 250–560) o en la franja de la cara si la escena es de pantalla dividida; subtítulos bajo el mentón. Nada en las zonas de Instagram.
- Antes de renderizar: `npx hyperframes check` sin errores y una captura por escena (`npx hyperframes snapshot --at t1,t2,…`) etiquetada E1…En con las zonas de Instagram marcadas. **Espera el OK.**

## Nivel 3 · Sonido, música, color y loudness

- **Pop suave** en cada entrada de gráfico y **whoosh** en cada corte o transición, con el pico del whoosh justo en el corte.
- Los efectos y la música se **retiran automáticamente cuando hay voz** (sidechain). Si un pop cae en el ataque de una palabra, bájalo 6–10 dB.
- **Música**: opcional; si la persona no la aporta, pregunta o déjala fuera. Detalles en `audio.md`.
- **Color**: un poco más cálido en toda la imagen por igual (ver `color-y-recorte.md`).
- **Normaliza** a −14 LUFS integrados, pico real −1,5 dBTP.

## Nivel 4 · Estilo de una referencia

1. Extrae fotogramas a 1 por segundo y cuadro a cuadro en 2 o 3 transiciones (`references/analizar-referencia.md`).
2. Analiza también el **audio**: densidad de efectos por segundo, tipo (whoosh, glitch, impacto grave, clic) y tempo de la música.
3. Escribe una **ficha de estilo** (entradas, curvas, tipografía, color, ritmo, sonido) y guárdala junto al video.
4. Reconstruye las escenas con ese lenguaje usando **el contenido, los clips y los colores de la persona**. Nunca copies textos, logos ni imágenes de la referencia.
5. Capturas → OK → render.

## Revisión final

Pasa la lista de `verificacion.md` sobre el **archivo final** (no sobre la composición) y entrega una tabla cumple / no cumple con la medida de cada punto.

## Aprendizajes de sesiones reales

- Cuando la persona dice "estaba mejor antes", recupera la versión anterior **sin borrar** la nueva (renómbrala). Pregunta qué parte prefería si no es obvio.
- Las capturas que manda la persona con flechas o recuadros son la prioridad: revisa exactamente esos puntos en el video renderizado, no en la composición.
- El nombre de una persona o marca citada en el guion se confirma con quien edita antes de ponerlo en pantalla.
- Una música que en la mezcla parece "presente" suele parecerle alta a quien habla. Empieza con la música unos 30 dB por debajo de la voz y súbela solo si la piden.
