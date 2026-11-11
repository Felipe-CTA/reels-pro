"""Mide cuánto queda la voz por encima de la música + efectos en cada palabra.

Uso:  python voice_margin.py voz.wav fondo.wav palabras.json [--min 8]
- voz.wav: la voz sola, tal como entra en la mezcla.
- fondo.wav: música + efectos ya con su volumen y su ducking (sin la voz).
- palabras.json: salida de transcribe.py en la misma línea de tiempo.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import argparse, json, subprocess, numpy as np

p = argparse.ArgumentParser(); p.add_argument("voz"); p.add_argument("fondo"); p.add_argument("palabras")
p.add_argument("--min", type=float, default=8.0); a = p.parse_args()
SR = 16000
load = lambda f: np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                              capture_output=True, check=True).stdout, np.int16) / 32768.0
v, b = load(a.voz), load(a.fondo)
db = lambda x: 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9) if len(x) else -120
W = json.load(open(a.palabras, encoding="utf8"))
m = [db(v[int(s * SR):int(e * SR)]) - db(b[int(s * SR):int(e * SR)]) for s, e, _ in W]
i = int(np.argmin(m))
print(f"margen por palabra: mínimo {m[i]:.1f} dB ('{W[i][2]}' {W[i][0]:.2f}s) | mediana {np.median(m):.1f} dB")
bajas = [(W[k][2], round(W[k][0], 2), round(m[k], 1)) for k in range(len(W)) if m[k] < a.min]
print(f"palabras por debajo de {a.min} dB:", bajas or "ninguna")
