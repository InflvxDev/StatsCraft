# El daño viene x10 en puntos de vida (1 corazón = 20) -> "12.5 ❤"
scoreboard players operation #a sc.calc = #v sc.calc
scoreboard players operation #a sc.calc /= #20 sc.calc
scoreboard players operation #b sc.calc = #v sc.calc
scoreboard players operation #b sc.calc %= #20 sc.calc
scoreboard players operation #b sc.calc /= #2 sc.calc
execute store result storage statscraft:tmp f.a int 1 run scoreboard players get #a sc.calc
execute store result storage statscraft:tmp f.b int 1 run scoreboard players get #b sc.calc
function statscraft:fmt/s_hearts with storage statscraft:tmp f
