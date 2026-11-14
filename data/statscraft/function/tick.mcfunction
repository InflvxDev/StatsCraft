# Jugador nuevo o que volvió a entrar
execute as @a unless score @s sc.leave matches 0 run function statscraft:player/login

# Botones de los diálogos (van por /trigger, así no hace falta OP)
execute as @a[scores={statscraft=1..}] run function statscraft:trigger

# Stats combinadas (sumas/ratios) una vez por segundo
scoreboard players add #t sc.calc 1
execute if score #t sc.calc matches 20.. as @a run function statscraft:gen/calc
execute if score #t sc.calc matches 20.. run scoreboard players set #t sc.calc 0
