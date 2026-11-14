# Interno: busca la primera posición cuyo valor sea menor que #v
execute if score #lo sc.calc >= #hi sc.calc run return 0
scoreboard players operation #mid sc.calc = #lo sc.calc
scoreboard players operation #mid sc.calc += #hi sc.calc
scoreboard players operation #mid sc.calc /= #2 sc.calc
execute store result storage statscraft:tmp b.m int 1 run scoreboard players get #mid sc.calc
function statscraft:rank/mid with storage statscraft:tmp b
execute if score #m sc.calc >= #v sc.calc run scoreboard players operation #lo sc.calc = #mid sc.calc
execute if score #m sc.calc >= #v sc.calc run scoreboard players add #lo sc.calc 1
execute if score #m sc.calc < #v sc.calc run scoreboard players operation #hi sc.calc = #mid sc.calc
function statscraft:rank/bsearch
