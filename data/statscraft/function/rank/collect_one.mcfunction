# Interno: {n, o}. Inserta {n, v} en "sorted" en su posición (búsqueda binaria).
scoreboard players set #v sc.calc 0
$execute store result score #v sc.calc run scoreboard players get $(n) $(o)
execute unless score #v sc.calc matches 1.. run return 0
data modify storage statscraft:tmp row set value {n:"",v:0}
data modify storage statscraft:tmp row.n set from storage statscraft:tmp a.n
execute store result storage statscraft:tmp row.v int 1 run scoreboard players get #v sc.calc
scoreboard players set #lo sc.calc 0
execute store result score #hi sc.calc run data get storage statscraft:tmp sorted
function statscraft:rank/bsearch
execute store result storage statscraft:tmp b.i int 1 run scoreboard players get #lo sc.calc
function statscraft:rank/insert with storage statscraft:tmp b
