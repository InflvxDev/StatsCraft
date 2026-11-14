# Interno: {n, u}. Si el UUID ya estaba, solo actualiza el nombre (cambio de nick).
$execute if data storage statscraft:players list[{u:$(u)}] run return run data modify storage statscraft:players list[{u:$(u)}].n set value "$(n)"
$data modify storage statscraft:players list append value {n:"$(n)",u:$(u)}
