"""Mide si alguna parte del video queda quieta más de un umbral (por defecto 1,5 s).

Uso:  python motion_check.py video.mp4 [--max 1.5] [--umbral 0.15]
--umbral es el cambio medio por cuadro (niveles de gris, 0-255) por debajo del cual un cuadro se considera quieto.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import argparse, subprocess, numpy as np

p = argparse.ArgumentParser(); p.add_argument("video")
p.add_argument("--max", type=float, default=1.5); p.add_argument("--umbral", type=float, default=0.15)
a = p.parse_args()
fps = eval(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate", "-of", "csv=p=0", a.video],
                          capture_output=True, text=True).stdout.strip())
W, H = 270, 480
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.video, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.int16)
d = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))
runs, start = [], None
for i, s in enumerate(list(d < a.umbral) + [False]):
    if s and start is None: start = i
    if not s and start is not None: runs.append((start / fps, (i - start) / fps)); start = None
longest = max((r[1] for r in runs), default=0)
print(f"{len(fr)} cuadros | cambio medio por cuadro: mediana {np.median(d):.2f}")
print(f"tramo quieto más largo: {longest:.2f} s | tramos > {a.max} s: {[(round(t, 2), round(l, 2)) for t, l in runs if l > a.max]}")
print("CUMPLE" if longest <= a.max else "NO CUMPLE")
