# Interno: procesa queue[0] y sigue (recursivo)
data modify storage statscraft:tmp a set value {}
data modify storage statscraft:tmp a.n set from storage statscraft:tmp queue[0].n
data modify storage statscraft:tmp a.o set from storage statscraft:tmp stat.o
function statscraft:rank/collect_one with storage statscraft:tmp a
data remove storage statscraft:tmp queue[0]
execute if data storage statscraft:tmp queue[0] run function statscraft:rank/collect
