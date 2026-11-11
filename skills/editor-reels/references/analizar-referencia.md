# Analizar un reel de referencia

La persona trae un reel que le gusta. El objetivo es extraer su **lenguaje** (movimiento, ritmo, tipografía, color, sonido), no su contenido.

## 1. Fotogramas

```bash
# hoja de contacto, 1 fotograma por segundo
ffmpeg -i ref.mp4 -vf "fps=1,scale=180:-1,tile=10x3" -frames:v 1 hoja_%d.png

# detectar cortes y transiciones
ffmpeg -i ref.mp4 -vf "select='gt(scene,0.25)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*"

# cuadro a cuadro alrededor de una transición (1,2 s desde el segundo T)
ffmpeg -ss T -t 1.2 -i ref.mp4 -vf "scale=150:-1,drawtext=text='%{pts\:flt}':fontsize=18:fontcolor=yellow,tile=12x3" -frames:v 1 transicion.png
```

Elige 2 o 3 transiciones distintas (por ejemplo cámara → gráfico, gráfico → cámara y texto → texto) y cuenta cuántos cuadros dura cada fase.

## 2. Audio

- Transcribe la voz con marcas por palabra.
- Marca los transitorios que **no** coinciden con el inicio de una palabra: son efectos. Clasifícalos por espectro (graves = impacto, agudos largos = whoosh, agudos cortos = clic o pop, ruido = glitch) y calcula cuántos hay por segundo.
- Estima el tempo de la música por autocorrelación de los graves.
- Comprueba cuántos efectos coinciden con cortes visuales.

## 3. Ficha de estilo

Escribe un archivo `Ficha de estilo.md` con estas secciones: entradas, curvas y duraciones, transiciones, tipografía, color, ritmo y sonido. Cierra con una tabla que relacione cada patrón con la escena del reel de la persona donde se va a usar.

## 4. Límites

- No copies textos, logos, marcas, imágenes ni música de la referencia.
- Si la referencia usa logos de terceros (por ejemplo, de apps), sustitúyelos por íconos genéricos o por los de la persona.
- No nombres a quien creó la referencia dentro del video.
