# Interno: @s usó /trigger statscraft
execute store result storage statscraft:tmp args.v int 1 run scoreboard players get @s statscraft
scoreboard players set @s statscraft 0
scoreboard players enable @s statscraft
execute if data storage statscraft:tmp args{v:1} run return run dialog show @s statscraft:menu
# 2 = Cerrar: el cliente está en "esperando respuesta", se cierra al instante
execute if data storage statscraft:tmp args{v:2} run return run dialog clear @s
function statscraft:rank/open with storage statscraft:tmp args
