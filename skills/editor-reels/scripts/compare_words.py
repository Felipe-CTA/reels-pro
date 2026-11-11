"""Compara dos transcripciones (JSON de transcribe.py) y lista las palabras que desaparecieron o cambiaron.

Uso:  python compare_words.py original.json editado.json
Una diferencia no siempre es una palabra perdida: transcribe solo ese fragmento para confirmarlo.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import json, re, sys, difflib

norm = lambda w: re.sub(r"[^\wáéíóúüñ]", "", w.lower())
O = json.load(open(sys.argv[1], encoding="utf8")); E = json.load(open(sys.argv[2], encoding="utf8"))
o, e = [norm(w[2]) for w in O], [norm(w[2]) for w in E]
print(f"original: {len(o)} palabras | editado: {len(e)} palabras")
n = 0
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, o, e, autojunk=False).get_opcodes():
    if tag == "equal": continue
    n += 1
    t = f"{O[i1][0]:.2f}s" if i1 < len(O) else "final"
    print(f"  {tag:7s} original {[O[k][2] for k in range(i1, i2)]} @ {t}  ->  editado {[E[k][2] for k in range(j1, j2)]}")
print("diferencias:", n)
