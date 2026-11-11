# Lista de verificación final

Pásala sobre el **archivo exportado** y entrega una tabla con la medida de cada punto.

| Punto | Cómo se mide | Aprobado si |
|---|---|---|
| Ninguna palabra comida | Retranscribir el final (con música y efectos) y `compare_words.py` contra el crudo | 0 diferencias, o diferencias explicadas por el transcriptor (comprueba el fragmento) |
| Subtítulos sin errores | Comparar el texto en pantalla (extraído del HTML, más títulos y pantallas completas) con lo dicho | Coinciden palabra por palabra; nombres propios confirmados |
| La cara nunca tapada | `face_track.py` + posiciones de los elementos en el navegador cada 0,1 s | Sin solapes mientras se ve la cámara (avisa de las pantallas completas que la sustituyen) |
| Zonas de Instagram | Cajas de texto y tarjetas frente a arriba 220 px, abajo 420 px, derecha 150 px | Nada importante dentro; solo piezas de paso en movimiento |
| Audio a −14 LUFS | `ebur128=peak=true` | −14 ± 0,5 LUFS, pico ≤ −1,5 dBTP |
| Voz por encima del fondo | `voice_margin.py` | Mínimo ≥ 8 dB por palabra |
| Ninguna imagen quieta > 1,5 s | `motion_check.py` | Tramo quieto más largo < 1,5 s |
| Bordes del recorte | Acercamientos a manos y orejas en gestos rápidos del render | Sin líneas ni resplandores visibles |

Di también qué **no** comprobaste (por ejemplo, que no reprodujiste el video entero con sonido).
