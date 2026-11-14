# Interno: @s usó /trigger statscraft
execute store result storage statscraft:tmp args.v int 1 run scoreboard players get @s statscraft
scoreboard players set @s statscraft 0
scoreboard players enable @s statscraft
execute if data storage statscraft:tmp args{v:1} run return run dialog show @s statscraft:menu
function statscraft:rank/open with storage statscraft:tmp args
