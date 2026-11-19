# Interno: arma el diálogo del ranking en statscraft:tmp ui y lo muestra
data modify storage statscraft:tmp ui set value {type:"minecraft:multi_action",title:{text:"",bold:true},body:[],columns:1,pause:false,after_action:"wait_for_response",actions:[{label:{text:"↻ Actualizar",color:"green"},action:{type:"minecraft:run_command",command:""}}],exit_action:{label:"Volver",action:{type:"minecraft:show_dialog",dialog:"statscraft:menu"}}}
data modify storage statscraft:tmp ui.title.text set from storage statscraft:tmp stat.n
data modify storage statscraft:tmp ui.title.color set from storage statscraft:tmp stat.col
data modify storage statscraft:tmp ui.actions[0].action.command set from storage statscraft:tmp stat.cmd

# Cabecera: "Categoría · N jugadores"
data modify storage statscraft:tmp h set value {}
data modify storage statscraft:tmp h.c set from storage statscraft:tmp stat.c
execute store result score #total sc.calc run data get storage statscraft:tmp sorted
execute store result storage statscraft:tmp h.k int 1 run scoreboard players get #total sc.calc
function statscraft:rank/header with storage statscraft:tmp h

execute if score #total sc.calc matches 0 run data modify storage statscraft:tmp ui.body append value {type:"minecraft:plain_message",contents:{text:"Nadie ha sumado puntos en esta estadística todavía.",color:"gray",italic:true}}

# Filas (máximo 100)
scoreboard players set #pos sc.calc 0
scoreboard players set #mypos sc.calc 0
scoreboard players set #rank sc.calc 0
scoreboard players set #prev sc.calc -1
execute if data storage statscraft:tmp sorted[0] run function statscraft:rank/row_loop

# Pie: puesto de quien mira
execute if score #total sc.calc matches 1.. run function statscraft:rank/footer

function statscraft:rank/show with storage statscraft:tmp
