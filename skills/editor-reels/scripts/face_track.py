"""Detecta la cara a lo largo del video (5 muestras por segundo) para saber dónde NO poner gráficos.

Uso:  python face_track.py video.mp4 caras.json
Salida: [[t, x1, y1, x2, y2], ...] en píxeles del video original, y la caja que las envuelve a todas.
Requiere: pip install "opencv-python-headless<5"   (OpenCV 5 eliminó CascadeClassifier)
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import json, sys, cv2, numpy as np

cap = cv2.VideoCapture(sys.argv[1]); fps = cap.get(cv2.CAP_PROP_FPS) or 30
W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)); s = 540 / W
cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
out, i, n = [], 0, 0
while True:
    ok, f = cap.read()
    if not ok: break
    if i % max(1, int(fps / 5)) == 0:
        n += 1
        g = cv2.cvtColor(cv2.resize(f, (540, int(H * s))), cv2.COLOR_BGR2GRAY)
        fs = cas.detectMultiScale(g, 1.1, 6, minSize=(60, 60))
        if len(fs):
            x, y, w, h = max(fs, key=lambda r: r[2] * r[3])
            out.append([round(i / fps, 3), int(x / s), int(y / s), int((x + w) / s), int((y + h) / s)])
    i += 1
json.dump(out, open(sys.argv[2], "w"))
b = np.array([o[1:] for o in out]) if out else np.zeros((1, 4))
print(f"muestras {n}, con cara {len(out)} | caja que las envuelve: x {b[:,0].min()}-{b[:,2].max()}, y {b[:,1].min()}-{b[:,3].max()}")
print("Recuerda: la caja va de cejas a barbilla; añade ~20 % arriba para el pelo.")
