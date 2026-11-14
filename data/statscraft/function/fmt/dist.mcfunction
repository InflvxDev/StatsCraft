# cm -> "123 m" o "12.34 km"
scoreboard players operation #a sc.calc = #v sc.calc
execute if score #v sc.calc matches ..99999 run scoreboard players operation #a sc.calc /= #100 sc.calc
execute if score #v sc.calc matches ..99999 store result storage statscraft:tmp f.a int 1 run scoreboard players get #a sc.calc
execute if score #v sc.calc matches ..99999 run return run function statscraft:fmt/s_m with storage statscraft:tmp f
scoreboard players operation #a sc.calc /= #100000 sc.calc
scoreboard players operation #b sc.calc = #v sc.calc
scoreboard players operation #b sc.calc %= #100000 sc.calc
scoreboard players operation #b sc.calc /= #1000 sc.calc
execute store result storage statscraft:tmp f.a int 1 run scoreboard players get #a sc.calc
execute store result storage statscraft:tmp f.b int 1 run scoreboard players get #b sc.calc
execute if score #b sc.calc matches ..9 run return run function statscraft:fmt/s_km0 with storage statscraft:tmp f
function statscraft:fmt/s_km with storage statscraft:tmp f
