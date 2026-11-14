# Uso: /function statscraft:uninstall  (después quita el datapack)
function statscraft:gen/uninstall
scoreboard objectives remove statscraft
scoreboard objectives remove sc.leave
scoreboard objectives remove sc.calc
data remove storage statscraft:db stats
data remove storage statscraft:db pads
data remove storage statscraft:players list
data remove storage statscraft:tmp ui
tellraw @s {text:"✔ StatsCraft desinstalado. Ya puedes quitar el datapack.",color:"green"}
