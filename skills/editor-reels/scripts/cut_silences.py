"""Corta los silencios de un video conservando un margen para que no suene entrecortado.

Uso:  python cut_silences.py entrada.mp4 salida.mp4 [--min 0.3] [--db -40] [--margen 0.08]
- Detecta silencios de más de --min segundos por debajo de --db.
- Deja --margen segundos de aire a cada lado y un fundido de 10 ms en cada unión (sin clics).
- Escribe salida.tramos.json con los tramos conservados (útil para mapear tiempos).
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import argparse, json, re, subprocess

p = argparse.ArgumentParser()
p.add_argument("entrada"); p.add_argument("salida")
p.add_argument("--min", type=float, default=0.3); p.add_argument("--db", type=float, default=-40)
p.add_argument("--margen", type=float, default=0.08)
a = p.parse_args()

dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.entrada],
                           capture_output=True, text=True, check=True).stdout)
log = subprocess.run(["ffmpeg", "-hide_banner", "-i", a.entrada, "-af", f"silencedetect=noise={a.db}dB:d={a.min}", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
sil = list(zip(starts, ends + [dur] * (len(starts) - len(ends))))

keep, cur = [], 0.0
for s, e in sil:
    rs = 0.0 if s <= 0.01 else s + a.margen
    re_ = dur if e >= dur - 0.01 else e - a.margen
    if re_ <= rs: continue
    if rs > cur: keep.append((cur, rs))
    cur = re_
if cur < dur: keep.append((cur, dur))
keep = [(round(x, 3), round(y, 3)) for x, y in keep if y - x > 0.05]

fc = []
for i, (x, y) in enumerate(keep):
    d = y - x
    fc.append(f"[0:v]trim={x}:{y},setpts=PTS-STARTPTS[v{i}]")
    fc.append(f"[0:a]atrim={x}:{y},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={max(0, d - 0.012):.3f}:d=0.012[a{i}]")
fc.append("".join(f"[v{i}][a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=1:a=1[vo][ao]")
script = a.salida + ".filtros.txt"
open(script, "w").write(";\n".join(fc))
# ffmpeg >= 9 usa -/filter_complex <archivo>; versiones anteriores, -filter_complex_script
ver = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True).stdout
major = int(re.search(r"ffmpeg version n?(\d+)", ver).group(1)) if re.search(r"ffmpeg version n?(\d+)", ver) else 9
flag = ["-/filter_complex", script] if major >= 7 else ["-filter_complex_script", script]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.entrada, *flag, "-map", "[vo]", "-map", "[ao]",
                "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.salida], check=True)
json.dump(keep, open(a.salida + ".tramos.json", "w"))
nuevo = sum(y - x for x, y in keep)
print(f"{len(sil)} silencios, {len(keep)} tramos | antes {dur:.2f} s -> después {nuevo:.2f} s")
