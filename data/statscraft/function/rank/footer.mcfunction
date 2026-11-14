execute if score #mypos sc.calc matches 0 run return run data modify storage statscraft:tmp ui.body append value {type:"minecraft:plain_message",contents:{text:"Todavía no apareces en este ranking.",color:"dark_gray",italic:true}}
data modify storage statscraft:tmp h set value {}
execute store result storage statscraft:tmp h.p int 1 run scoreboard players get #mypos sc.calc
execute store result storage statscraft:tmp h.k int 1 run scoreboard players get #total sc.calc
function statscraft:rank/footer_run with storage statscraft:tmp h
