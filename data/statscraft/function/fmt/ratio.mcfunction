# x100 -> "1.25"
scoreboard players operation #a sc.calc = #v sc.calc
scoreboard players operation #a sc.calc /= #100 sc.calc
scoreboard players operation #b sc.calc = #v sc.calc
scoreboard players operation #b sc.calc %= #100 sc.calc
execute store result storage statscraft:tmp f.a int 1 run scoreboard players get #a sc.calc
execute store result storage statscraft:tmp f.b int 1 run scoreboard players get #b sc.calc
execute if score #b sc.calc matches ..9 run return run function statscraft:fmt/s_r0 with storage statscraft:tmp f
function statscraft:fmt/s_r with storage statscraft:tmp f
