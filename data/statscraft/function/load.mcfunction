# StatsCraft - carga
scoreboard objectives add sc.calc dummy
# Trigger principal: cualquier jugador (con o sin OP) puede usar /trigger
#   1 = menú, 101+ = ranking de una estadística
scoreboard objectives add statscraft trigger "StatsCraft"
# Detecta cuando un jugador vuelve a entrar (para registrar/actualizar su nombre)
scoreboard objectives add sc.leave minecraft.custom:minecraft.leave_game

scoreboard players set #2 sc.calc 2
scoreboard players set #20 sc.calc 20
scoreboard players set #24 sc.calc 24
scoreboard players set #100 sc.calc 100
scoreboard players set #1000 sc.calc 1000
scoreboard players set #1200 sc.calc 1200
scoreboard players set #72000 sc.calc 72000
scoreboard players set #100000 sc.calc 100000

# Objetivos de estadísticas + base de datos (generados por tools/generate.py)
function statscraft:gen/objectives
function statscraft:gen/db
execute unless data storage statscraft:players list run data modify storage statscraft:players list set value []

# Limpieza única de los objetivos del buscador (versión anterior)
execute unless data storage statscraft:db {search_removed:1b} run function statscraft:legacy/remove_search
data modify storage statscraft:db search_removed set value 1b

# Re-registra a los que ya están conectados (por si se agregaron stats nuevas)
execute as @a run function statscraft:player/login
