# Interno: formatea #v según stat.f y lo deja en statscraft:tmp r.s
data modify storage statscraft:tmp f set value {}
execute if data storage statscraft:tmp stat{f:"d"} run return run function statscraft:fmt/dist
execute if data storage statscraft:tmp stat{f:"t"} run return run function statscraft:fmt/time
execute if data storage statscraft:tmp stat{f:"h"} run return run function statscraft:fmt/hearts
execute if data storage statscraft:tmp stat{f:"r"} run return run function statscraft:fmt/ratio
execute store result storage statscraft:tmp f.a int 1 run scoreboard players get #v sc.calc
function statscraft:fmt/s_num with storage statscraft:tmp f
