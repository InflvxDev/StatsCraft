# Interno: guarda el nombre de @s en storage statscraft:players list
# (así el ranking incluye también a los jugadores desconectados).
# El nombre se saca de su cabeza, generada en un item_display temporal.
execute at @s run summon minecraft:item_display ~ ~ ~ {Tags:["sc.name"]}
execute at @s run loot replace entity @n[type=minecraft:item_display,tag=sc.name,distance=..1] contents loot statscraft:player_head
data modify storage statscraft:tmp reg set value {}
execute at @s run data modify storage statscraft:tmp reg.n set from entity @n[type=minecraft:item_display,tag=sc.name,distance=..1] item.components."minecraft:profile".name
data modify storage statscraft:tmp reg.u set from entity @s UUID
kill @e[type=minecraft:item_display,tag=sc.name]
execute unless data storage statscraft:tmp reg.n run return fail
function statscraft:player/register_run with storage statscraft:tmp reg
