# Interno: agrega una fila "N. [cabeza] Nombre ..... valor"
# Valor con formato -> r.s
function statscraft:fmt/run
execute store result storage statscraft:tmp r.p int 1 run scoreboard players get #pos sc.calc
# Relleno con puntos para que todas las filas midan parecido (y queden alineadas)
execute store result score #len sc.calc run data get storage statscraft:tmp r.n
execute store result score #l2 sc.calc run data get storage statscraft:tmp r.s
scoreboard players operation #len sc.calc += #l2 sc.calc
execute if score #pos sc.calc matches 10.. run scoreboard players add #len sc.calc 1
execute if score #pos sc.calc matches 100.. run scoreboard players add #len sc.calc 1
scoreboard players set #pad sc.calc 30
scoreboard players operation #pad sc.calc -= #len sc.calc
execute if score #pad sc.calc matches ..0 run scoreboard players set #pad sc.calc 0
execute if score #pad sc.calc matches 41.. run scoreboard players set #pad sc.calc 40
execute store result storage statscraft:tmp r.k int 1 run scoreboard players get #pad sc.calc
function statscraft:rank/row_build with storage statscraft:tmp r
