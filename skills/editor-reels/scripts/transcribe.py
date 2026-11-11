"""Transcribe un video o audio con marcas de tiempo por palabra.

Uso:  python transcribe.py entrada.mp4 palabras.json [--lang es] [--model medium] [--literal]
Salida: JSON con [[inicio, fin, "palabra"], ...]
--literal intenta conservar muletillas y arranques en falso (útil para detectar tomas repetidas).
Requiere: pip install faster-whisper numpy   (y ffmpeg en el PATH)
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import argparse, json, subprocess
import numpy as np
from faster_whisper import WhisperModel

p = argparse.ArgumentParser()
p.add_argument("entrada"); p.add_argument("salida")
p.add_argument("--lang", default="es"); p.add_argument("--model", default="medium")
p.add_argument("--literal", action="store_true")
a = p.parse_args()

# se decodifica con ffmpeg para no depender de la versión de PyAV
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.entrada, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
model = WhisperModel(a.model, device="cpu", compute_type="int8")
kw = dict(language=a.lang, word_timestamps=True)
if a.literal:
    kw.update(condition_on_previous_text=False, initial_prompt="Eh, este, este… bueno, o sea, eh, la, la idea.")
segs, _ = model.transcribe(audio, **kw)
words = [[round(w.start, 3), round(w.end, 3), w.word.strip()] for s in segs for w in s.words]
json.dump(words, open(a.salida, "w", encoding="utf8"), ensure_ascii=False)
print(f"{len(words)} palabras -> {a.salida}")
