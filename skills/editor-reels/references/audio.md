# Audio

## Mejora de voz (ffmpeg)

Mide primero: nivel de ruido en las pausas, reparto de energía por bandas y rango dinámico. Aplica solo lo que haga falta.

```text
highpass=f=75:poles=2,
afftdn=nr=10:nf=-50:tn=1,                       # reducción de ruido suave
equalizer=f=250:t=q:w=1.0:g=-2.5,               # quita lo "encajonado"
equalizer=f=3500:t=q:w=1.2:g=3,                 # presencia: claridad de las palabras
highshelf=f=9000:g=2.5,                         # aire
deesser=i=0.35:m=0.5:f=0.5,
acompressor=threshold=-20dB:ratio=3:attack=5:release=60:makeup=2,
alimiter=limit=0.89:level=false
```

Para estilos de mucha energía con música densa: compresión más firme (−24 dB, 4:1, y una segunda etapa a −10 dB, 8:1) para que la voz corte por encima.

Objetivo orientativo: presencia (2–5 kHz) en torno al 18 % de la energía y rango p95–p50 entre 2,5 y 5 dB.

## Mezcla

```text
[voz]asplit=3[v][k1][k2];
[musica]volume=-18dB[mu];   [mu][k1]sidechaincompress=threshold=0.02:ratio=5:attack=10:release=300[mud];
[efectos][k2]sidechaincompress=threshold=0.03:ratio=3:attack=5:release=150[sd];
[v][mud][sd]amix=inputs=3:normalize=0:duration=first,
loudnorm=I=-14:TP=-1.5:LRA=9
```

- **Música**: empieza unos 30–35 dB por debajo de la voz en las palabras. Súbela solo si la piden.
- **Efectos**: pop/clic −21 a −24 dBFS de pico, whoosh −20 a −26, impactos −15 a −18 con la cola recortada a < 1 s.
- Coloca cada efecto alineando su **pico** con el evento visual (resta su `peak_offset`).
- Si un efecto cae en el ataque de una palabra (−0,05 a +0,12 s del inicio), bájalo 6–10 dB.
- Densidad: 0,7–1,2 efectos/s en estilos sobrios; 1,5–2/s en estilos cinéticos. Agrupa: no pongas dos swishes a menos de 0,6 s.

## Verificación

- `scripts/voice_margin.py`: margen de la voz sobre música + efectos en cada palabra. Mínimo ≥ 8 dB, mediana ≥ 18 dB.
- Retranscribe el **archivo final con la mezcla completa** y compara: si una palabra desaparece, casi siempre la tapa un efecto o una cola grave.
- `ffmpeg -i final.mp4 -af ebur128=peak=true -f null -`: integrado −14 ± 0,5 LUFS, pico ≤ −1,5 dBTP.

## Música y efectos: origen

- Usa audio con licencia: el de la persona, una biblioteca libre de derechos o un conector de audio si está disponible.
- Descarga los archivos a la carpeta de trabajo. **No guardes enlaces firmados** (con `X-Amz-Signature`, `token=`, etc.) en ningún archivo que se vaya a compartir.
