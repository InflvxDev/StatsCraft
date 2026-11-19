# Interno: {p, n, s, k}
$data modify storage statscraft:tmp line set value {type:"minecraft:plain_message",width:340,contents:{text:"",extra:[{text:"$(p). ",color:"gray",bold:true},{type:"object",object:"player",player:{name:"$(n)"}},{text:" $(n)",color:"white"},{text:"",color:"dark_gray"},{text:"$(s)",color:"white"}]}}
$data modify storage statscraft:tmp line.contents.extra[3].text set from storage statscraft:db pads[$(k)]
# Oro, plata y bronce para el top 3
execute if score #rank sc.calc matches 1 run data modify storage statscraft:tmp line.contents.extra[0].color set value "#FFD700"
execute if score #rank sc.calc matches 1 run data modify storage statscraft:tmp line.contents.extra[4].color set value "#FFD700"
execute if score #rank sc.calc matches 2 run data modify storage statscraft:tmp line.contents.extra[0].color set value "#C0C0C0"
execute if score #rank sc.calc matches 2 run data modify storage statscraft:tmp line.contents.extra[4].color set value "#C0C0C0"
execute if score #rank sc.calc matches 3 run data modify storage statscraft:tmp line.contents.extra[0].color set value "#CD7F32"
execute if score #rank sc.calc matches 3 run data modify storage statscraft:tmp line.contents.extra[4].color set value "#CD7F32"
# Quien mira sale en celeste
execute if score #diff sc.calc matches 0 run data modify storage statscraft:tmp line.contents.extra[2].color set value "aqua"
data modify storage statscraft:tmp ui.body append from storage statscraft:tmp line
