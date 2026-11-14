# ticks -> "3d 4h 12m" o "4h 12m"
scoreboard players operation #h sc.calc = #v sc.calc
scoreboard players operation #h sc.calc /= #72000 sc.calc
scoreboard players operation #m sc.calc = #v sc.calc
scoreboard players operation #m sc.calc %= #72000 sc.calc
scoreboard players operation #m sc.calc /= #1200 sc.calc
scoreboard players operation #d sc.calc = #h sc.calc
scoreboard players operation #d sc.calc /= #24 sc.calc
scoreboard players operation #h sc.calc %= #24 sc.calc
execute store result storage statscraft:tmp f.d int 1 run scoreboard players get #d sc.calc
execute store result storage statscraft:tmp f.h int 1 run scoreboard players get #h sc.calc
execute store result storage statscraft:tmp f.m int 1 run scoreboard players get #m sc.calc
execute if score #d sc.calc matches 1.. run return run function statscraft:fmt/s_dhm with storage statscraft:tmp f
function statscraft:fmt/s_hm with storage statscraft:tmp f
