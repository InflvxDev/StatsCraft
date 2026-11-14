# Interno: procesa sorted[0] y sigue (recursivo)
scoreboard players add #pos sc.calc 1
data modify storage statscraft:tmp r set value {}
data modify storage statscraft:tmp r.n set from storage statscraft:tmp sorted[0].n
execute store result score #v sc.calc run data get storage statscraft:tmp sorted[0].v
# ¿Es quien está mirando? (#diff = 0 si los nombres son iguales)
data modify storage statscraft:tmp cmp set from storage statscraft:tmp r.n
execute store success score #diff sc.calc run data modify storage statscraft:tmp cmp set from storage statscraft:tmp me
execute if score #diff sc.calc matches 0 run scoreboard players operation #mypos sc.calc = #pos sc.calc
execute if score #pos sc.calc matches ..100 run function statscraft:rank/row
data remove storage statscraft:tmp sorted[0]
execute if data storage statscraft:tmp sorted[0] run function statscraft:rank/row_loop
