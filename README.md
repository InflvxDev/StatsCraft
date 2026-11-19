# StatsCraft

Rankings de estadísticas para SMP (Minecraft 26.4). Funciona para **todos los jugadores, con o sin OP**.

- Se abre desde el **menú de pausa** / **acciones rápidas**, o con `/trigger statscraft`.
- 146 estadísticas en 11 categorías: Logros, Menas, Minería, Tala, Agricultura, Combate, Muertes, Movimiento, Tiempo, Social y Objetos.
- Al tocar una stat se ve el ranking: `1. [cabeza] Jugador ..... valor`, con el top 3 en oro, plata y bronce, tu fila resaltada y tu puesto al final.
- El ranking incluye a los jugadores desconectados (se registran la primera vez que entran).

## Notas
- **Logros Conseguidos** (primera stat del menú): si está instalado [BlazeandCave's Advancements Pack](https://www.planetminecraft.com/data-pack/blazeandcave-s-advancements-pack/), usa su contador `bac_advancements`. Si no, cuenta los 122 logros vanilla. A diferencia de las demás stats, sí incluye los logros conseguidos antes de instalar StatsCraft.
- Las estadísticas empiezan a contarse **desde que se instala** el datapack. No incluyen lo que se hizo antes.
- Desinstalar: `/function statscraft:uninstall` y después quitar el datapack.

## Agregar o cambiar stats
Edita la lista `STATS` en `tools/generate.py` y ejecuta `python tools/generate.py`.
Ese script regenera `function/gen/*` y `dialog/menu.json`.
