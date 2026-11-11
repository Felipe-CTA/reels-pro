# Editor de reels por niveles · skill para Claude Code

Convierte un video grabado a cámara en un reel vertical (9:16) para Instagram, TikTok o YouTube Shorts. Claude edita **por niveles**, te enseña capturas antes de cada render y verifica el resultado con mediciones reales.

| Nivel | Qué obtienes |
|---|---|
| **1 · Corte** | Silencios fuera, tomas repetidas fuera y una lista que demuestra que no se perdió ninguna palabra. |
| **2 · Gráficos** | Subtítulos palabra por palabra, un gráfico por idea, un zoom en cada corte, la cara siempre libre y las zonas de Instagram respetadas. |
| **3 · Sonido y color** | Efectos suaves, whooshes, música opcional bajo la voz, color cálido y audio a −14 LUFS. |
| **4 · Estilo** | Analiza un reel que te guste y reconstruye tus escenas con ese movimiento, con tu contenido y tus colores. |
| **Revisión final** | Tabla de cumple / no cumple con evidencia. |

Incluye dos estilos listos: **UI claro azul** (paneles, tarjetas, carrusel, serif itálica) y **tipografía cinética oscura** (texto curvo, palabras detrás de la persona, glitch, pantallas 3D).

## Instalación

Necesitas [Claude Code](https://claude.com/claude-code).

**Opción A · como plugin** (escríbelo dentro de Claude Code):

```text
/plugin marketplace add Felipe-CTA/reels-pro
/plugin install editor-reels@editor-reels
```

**Opción B · como skill suelta**, desde la terminal.

macOS o Linux:

```bash
git clone https://github.com/Felipe-CTA/reels-pro.git /tmp/reels-pro && mkdir -p ~/.claude/skills && cp -r /tmp/reels-pro/skills/editor-reels ~/.claude/skills/
```

Windows (PowerShell):

```powershell
git clone https://github.com/Felipe-CTA/reels-pro.git $env:TEMP\editor-reels; New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse "$env:TEMP\editor-reels\skills\eels-pro" "$HOME\.claude\skills\"
```

Después abre una sesión nueva de Claude Code.

## Requisitos para editar

- `ffmpeg` (versión 6 o superior).
- Python 3.10 o superior, con `pip install -r skills/editor-reels/scripts/requirements.txt`.
- Node.js 18 o superior, para los gráficos con [HyperFrames](https://hyperframes.heygen.com) (`npm i hyperframes`).
- Música y efectos con licencia: los tuyos, una biblioteca libre de derechos o un conector de audio de tu cuenta.

## Uso

Abre Claude Code en la carpeta de tu video y pide, por ejemplo:

> Edita `mi-video.mp4` y conviértelo en un reel. Empieza por el nivel 1.

> Usa `referencia.mp4` como estilo y reconstruye mis escenas con ese movimiento.

Claude te enseñará capturas numeradas (E1, E2…) y esperará tu OK antes de cada render.

## Privacidad

El repositorio no contiene videos, voces, transcripciones, claves ni datos de nadie. Las skills trabajan solo con los archivos que tú le das, en tu equipo. No subas tus videos ni tus claves a un fork público.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
