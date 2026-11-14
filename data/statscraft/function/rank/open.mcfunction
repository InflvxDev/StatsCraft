# Interno: abre el ranking de la stat {v} para @s
data remove storage statscraft:tmp stat
$data modify storage statscraft:tmp stat set from storage statscraft:db stats[{i:$(v)}]
execute unless data storage statscraft:tmp stat run return run dialog show @s statscraft:menu

# Valores al día de los conectados
execute as @a run function statscraft:gen/calc

# Nombre de quien mira (para resaltarlo)
data modify storage statscraft:tmp me set value ""
data modify storage statscraft:tmp a set value {}
data modify storage statscraft:tmp a.u set from entity @s UUID
function statscraft:rank/me with storage statscraft:tmp a

# Junta y ordena (de mayor a menor) a todos los jugadores registrados con valor > 0
data modify storage statscraft:tmp sorted set value []
data modify storage statscraft:tmp queue set from storage statscraft:players list
execute if data storage statscraft:tmp queue[0] run function statscraft:rank/collect

function statscraft:rank/render
