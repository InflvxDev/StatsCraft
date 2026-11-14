# StatsCraft - generador de archivos.
# Edita la lista STATS de abajo y ejecuta:  python tools/generate.py
# Regenera: data/statscraft/function/gen/* y dialog/menu.json
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = os.path.join(ROOT, "data", "statscraft")

CATS = {
    "Menas":       {"col": "aqua"},
    "Minería":     {"col": "gray"},
    "Tala":        {"col": "#C8925A"},
    "Agricultura": {"col": "green"},
    "Combate":     {"col": "red"},
    "Muertes":     {"col": "dark_red"},
    "Movimiento":  {"col": "yellow"},
    "Tiempo":      {"col": "light_purple"},
    "Social":      {"col": "gold"},
    "Objetos":     {"col": "#7FD4FF"},
}

def M(*ids):  return ["minecraft.mined:minecraft." + i for i in ids]
def C(*ids):  return ["minecraft.custom:minecraft." + i for i in ids]
def K(*ids):  return ["minecraft.killed:minecraft." + i for i in ids]
def KB(*ids): return ["minecraft.killed_by:minecraft." + i for i in ids]
def U(*ids):  return ["minecraft.used:minecraft." + i for i in ids]
def B(*ids):  return ["minecraft.broken:minecraft." + i for i in ids]

ORES = {
    "coal": M("coal_ore", "deepslate_coal_ore"),
    "iron": M("iron_ore", "deepslate_iron_ore"),
    "copper": M("copper_ore", "deepslate_copper_ore"),
    "gold": M("gold_ore", "deepslate_gold_ore", "nether_gold_ore"),
    "redstone": M("redstone_ore", "deepslate_redstone_ore"),
    "lapis": M("lapis_ore", "deepslate_lapis_ore"),
    "diamond": M("diamond_ore", "deepslate_diamond_ore"),
    "emerald": M("emerald_ore", "deepslate_emerald_ore"),
    "quartz": M("nether_quartz_ore"),
    "debris": M("ancient_debris"),
}
LOGS = {
    "oak": ("Roble", "oak_log"), "spruce": ("Abeto", "spruce_log"), "birch": ("Abedul", "birch_log"),
    "jungle": ("Jungla", "jungle_log"), "acacia": ("Acacia", "acacia_log"),
    "dark_oak": ("Roble Oscuro", "dark_oak_log"), "mangrove": ("Mangle", "mangrove_log"),
    "cherry": ("Cerezo", "cherry_log"), "pale_oak": ("Roble Pálido", "pale_oak_log"),
    "crimson": ("Tallo Carmesí", "crimson_stem"), "warped": ("Tallo Distorsionado", "warped_stem"),
}
CROPS = {
    "wheat": ("Trigo", ["wheat"]), "carrots": ("Zanahorias", ["carrots"]),
    "potatoes": ("Papas", ["potatoes"]), "beetroots": ("Remolachas", ["beetroots"]),
    "melon": ("Sandías", ["melon"]), "pumpkin": ("Calabazas", ["pumpkin"]),
    "sugar_cane": ("Caña de Azúcar", ["sugar_cane"]), "nether_wart": ("Verrugas del Nether", ["nether_wart"]),
    "cocoa": ("Cacao", ["cocoa"]), "bamboo": ("Bambú", ["bamboo"]),
}
DIST = [
    ("walk", "Caminando", "walk_one_cm"), ("sprint", "Corriendo", "sprint_one_cm"),
    ("crouch", "Agachado", "crouch_one_cm"), ("swim", "Nadando", "swim_one_cm"),
    ("on_water", "Sobre el Agua", "walk_on_water_one_cm"), ("under_water", "Bajo el Agua", "walk_under_water_one_cm"),
    ("climb", "Escalando", "climb_one_cm"), ("fall", "Cayendo", "fall_one_cm"),
    ("aviate", "Con Élitros", "aviate_one_cm"),
    ("fly", "Volando (Creativo)", "fly_one_cm"),
    ("boat", "En Bote", "boat_one_cm"), ("minecart", "En Vagoneta", "minecart_one_cm"),
    ("horse", "A Caballo", "horse_one_cm"), ("pig", "En Cerdo", "pig_one_cm"),
    ("strider", "En Strider", "strider_one_cm"),
    ("happy_ghast", "En Ghast Feliz", "happy_ghast_one_cm"),
]

# (id, nombre, categoria, formato, fuentes)
# formato: n=numero, d=distancia (cm), t=tiempo (ticks), h=corazones (daño x10), r=ratio (x100)
# fuentes: lista de criterios (se suman) o ("ratio", criterio_a, criterio_b)
STATS = []
def S(id, name, cat, fmt, src): STATS.append(dict(id=id, n=name, c=cat, f=fmt, src=src))

# --- Menas
S("ores", "Menas Totales", "Menas", "n", sum(ORES.values(), []))
S("coal", "Menas de Carbón", "Menas", "n", ORES["coal"])
S("iron", "Menas de Hierro", "Menas", "n", ORES["iron"])
S("copper", "Menas de Cobre", "Menas", "n", ORES["copper"])
S("gold", "Menas de Oro", "Menas", "n", ORES["gold"])
S("redstone", "Menas de Redstone", "Menas", "n", ORES["redstone"])
S("lapis", "Menas de Lapislázuli", "Menas", "n", ORES["lapis"])
S("diamond", "Menas de Diamante", "Menas", "n", ORES["diamond"])
S("emerald", "Menas de Esmeralda", "Menas", "n", ORES["emerald"])
S("quartz", "Cuarzo del Nether", "Menas", "n", ORES["quartz"])
S("debris", "Escombros Ancestrales", "Menas", "n", ORES["debris"])
# --- Mineria
S("stone", "Minería de Piedra", "Minería", "n", M("stone", "cobblestone"))
S("deepslate", "Minería de Pizarra", "Minería", "n", M("deepslate", "cobbled_deepslate"))
S("rocks", "Granito/Diorita/Andesita", "Minería", "n", M("granite", "diorite", "andesite"))
S("tuff", "Minería de Toba", "Minería", "n", M("tuff"))
S("netherrack", "Minería de Netherrack", "Minería", "n", M("netherrack"))
S("end_stone", "Minería de Piedra del End", "Minería", "n", M("end_stone"))
S("obsidian", "Minería de Obsidiana", "Minería", "n", M("obsidian", "crying_obsidian"))
S("basalt", "Basalto y Piedra Negra", "Minería", "n", M("basalt", "blackstone"))
S("ice", "Minería de Hielo", "Minería", "n", M("ice", "packed_ice", "blue_ice"))
S("dirt", "Excavación de Tierra", "Minería", "n", M("dirt", "grass_block", "coarse_dirt", "rooted_dirt", "podzol", "mycelium", "mud"))
S("sand", "Excavación de Arena", "Minería", "n", M("sand", "red_sand"))
S("gravel", "Excavación de Grava", "Minería", "n", M("gravel"))
S("clay", "Excavación de Arcilla", "Minería", "n", M("clay"))
S("amethyst", "Amatista Recolectada", "Minería", "n", M("amethyst_cluster"))
S("glowstone", "Piedra Luminosa", "Minería", "n", M("glowstone"))
S("sculk", "Sculk Destruido", "Minería", "n", M("sculk", "sculk_vein", "sculk_sensor", "sculk_shrieker", "sculk_catalyst"))
S("spawner", "Spawners Destruidos", "Minería", "n", M("spawner"))
# --- Tala
S("logs", "Tala Total", "Tala", "n", M(*[v[1] for v in LOGS.values()]))
for k, (name, block) in LOGS.items():
    S("log_" + k, "Tala de " + name, "Tala", "n", M(block))
# --- Agricultura
S("crops", "Cosecha Total", "Agricultura", "n", M(*sum([v[1] for v in CROPS.values()], [])))
for k, (name, blocks) in CROPS.items():
    S("crop_" + k, "Cosecha: " + name, "Agricultura", "n", M(*blocks))
S("bred", "Animales Criados", "Agricultura", "n", C("animals_bred"))
S("fish", "Peces Pescados", "Agricultura", "n", C("fish_caught"))
S("bonemeal", "Polvo de Hueso Usado", "Agricultura", "n", U("bone_meal"))
# --- Combate
S("mob_kills", "Mobs Asesinados", "Combate", "n", C("mob_kills"))
S("player_kills", "Jugadores Asesinados", "Combate", "n", C("player_kills"))
S("kd_pvp", "Ratio K/D (PvP)", "Combate", "r", ("ratio", C("player_kills")[0], C("deaths")[0]))
S("kd_mobs", "Mobs por Muerte", "Combate", "r", ("ratio", C("mob_kills")[0], C("deaths")[0]))
S("dmg_dealt", "Daño Infligido", "Combate", "h", C("damage_dealt"))
S("dmg_taken", "Daño Recibido", "Combate", "h", C("damage_taken"))
S("dmg_shield", "Daño Bloqueado (Escudo)", "Combate", "h", C("damage_blocked_by_shield"))
S("k_zombie", "Zombis Asesinados", "Combate", "n", K("zombie", "zombie_villager", "husk", "drowned"))
S("k_skeleton", "Esqueletos Asesinados", "Combate", "n", K("skeleton", "stray", "bogged"))
S("k_creeper", "Creepers Asesinados", "Combate", "n", K("creeper"))
S("k_spider", "Arañas Asesinadas", "Combate", "n", K("spider", "cave_spider"))
S("k_enderman", "Endermans Asesinados", "Combate", "n", K("enderman"))
S("k_witch", "Brujas Asesinadas", "Combate", "n", K("witch"))
S("k_phantom", "Phantoms Asesinados", "Combate", "n", K("phantom"))
S("k_slime", "Slimes Asesinados", "Combate", "n", K("slime", "magma_cube"))
S("k_blaze", "Blazes Asesinados", "Combate", "n", K("blaze"))
S("k_ghast", "Ghasts Asesinados", "Combate", "n", K("ghast"))
S("k_wither_skeleton", "Esqueletos Wither", "Combate", "n", K("wither_skeleton"))
S("k_piglin", "Piglins Asesinados", "Combate", "n", K("piglin", "piglin_brute", "zombified_piglin"))
S("k_hoglin", "Hoglins Asesinados", "Combate", "n", K("hoglin", "zoglin"))
S("k_guardian", "Guardianes Asesinados", "Combate", "n", K("guardian", "elder_guardian"))
S("k_shulker", "Shulkers Asesinados", "Combate", "n", K("shulker"))
S("k_illager", "Illagers Asesinados", "Combate", "n", K("pillager", "vindicator", "evoker", "ravager", "vex"))
S("k_breeze", "Breezes Asesinados", "Combate", "n", K("breeze"))
S("k_creaking", "Creakings Asesinados", "Combate", "n", K("creaking"))
S("k_warden", "Wardens Asesinados", "Combate", "n", K("warden"))
S("k_wither", "Withers Derrotados", "Combate", "n", K("wither"))
S("k_dragon", "Dragones Derrotados", "Combate", "n", K("ender_dragon"))
S("k_golem", "Gólems de Hierro Asesinados", "Combate", "n", K("iron_golem"))
S("k_villager", "Aldeanos Asesinados", "Combate", "n", K("villager"))
S("k_animals", "Animales Cazados", "Combate", "n", K("cow", "pig", "sheep", "chicken", "rabbit", "mooshroom"))
# --- Muertes
S("deaths", "Muertes", "Muertes", "n", C("deaths"))
S("streak", "Racha sin Morir", "Muertes", "t", C("time_since_death"))
S("by_creeper", "Muertes por Creeper", "Muertes", "n", KB("creeper"))
S("by_zombie", "Muertes por Zombi", "Muertes", "n", KB("zombie", "zombie_villager", "husk", "drowned"))
S("by_skeleton", "Muertes por Esqueleto", "Muertes", "n", KB("skeleton", "stray", "bogged"))
S("by_enderman", "Muertes por Enderman", "Muertes", "n", KB("enderman"))
S("by_warden", "Muertes por Warden", "Muertes", "n", KB("warden"))
S("by_player", "Muertes por Jugadores", "Muertes", "n", KB("player"))
# --- Movimiento
S("dist_total", "Distancia Total", "Movimiento", "d", C(*[d[2] for d in DIST if d[0] not in ("fall", "fly")]))
for k, name, stat in DIST:
    S("dist_" + k, name, "Movimiento", "d", C(stat))
S("jumps", "Saltos", "Movimiento", "n", C("jump"))
# --- Tiempo
S("play_time", "Tiempo Jugado", "Tiempo", "t", C("play_time"))
S("since_rest", "Tiempo sin Dormir", "Tiempo", "t", C("time_since_rest"))
S("sneak_time", "Tiempo Agachado", "Tiempo", "t", C("sneak_time"))
S("sleep", "Veces que Dormiste", "Tiempo", "n", C("sleep_in_bed"))
S("leave", "Desconexiones", "Tiempo", "n", C("leave_game"))
# --- Social / vida
S("xp_level", "Nivel de Experiencia", "Social", "n", ["level"])
S("trades", "Comercios con Aldeanos", "Social", "n", C("traded_with_villager"))
S("talked", "Charlas con Aldeanos", "Social", "n", C("talked_to_villager"))
S("enchant", "Objetos Encantados", "Social", "n", C("enchant_item"))
S("raids", "Raids Ganadas", "Social", "n", C("raid_win"))
S("bells", "Campanas Tocadas", "Social", "n", C("bell_ring"))
S("cake", "Rebanadas de Pastel", "Social", "n", C("eat_cake_slice"))
S("chests", "Cofres Abiertos", "Social", "n", C("open_chest"))
S("enderchest", "Cofre de Ender Abierto", "Social", "n", C("open_enderchest"))
S("shulker_box", "Cajas Shulker Abiertas", "Social", "n", C("open_shulker_box"))
S("crafting", "Mesas de Crafteo Usadas", "Social", "n", C("interact_with_crafting_table"))
S("furnace", "Hornos Usados", "Social", "n", C("interact_with_furnace", "interact_with_blast_furnace", "interact_with_smoker"))
S("anvil", "Yunques Usados", "Social", "n", C("interact_with_anvil"))
S("noteblocks", "Notas Tocadas", "Social", "n", C("play_noteblock"))
S("records", "Discos Reproducidos", "Social", "n", C("play_record"))
S("flowers", "Plantas en Macetas", "Social", "n", C("pot_flower"))
S("target", "Dianas Acertadas", "Social", "n", C("target_hit"))
S("drops", "Objetos Tirados", "Social", "n", C("drop"))
# --- Objetos
S("totems", "Tótems Usados", "Objetos", "n", U("totem_of_undying"))
S("pearls", "Perlas de Ender Lanzadas", "Objetos", "n", U("ender_pearl"))
S("rockets", "Cohetes Usados", "Objetos", "n", U("firework_rocket"))
S("gapples", "Manzanas Doradas Comidas", "Objetos", "n", U("golden_apple", "enchanted_golden_apple"))
S("gcarrots", "Zanahorias Doradas Comidas", "Objetos", "n", U("golden_carrot"))
S("torches", "Antorchas Colocadas", "Objetos", "n", U("torch", "soul_torch"))
S("tnt", "TNT Colocada", "Objetos", "n", U("tnt"))
S("rails", "Rieles Colocados", "Objetos", "n", U("rail", "powered_rail", "detector_rail", "activator_rail"))
S("bow", "Disparos con Arco", "Objetos", "n", U("bow", "crossbow"))
S("trident", "Tridentes Lanzados", "Objetos", "n", U("trident"))
S("pickaxes", "Picos Rotos", "Objetos", "n", B("wooden_pickaxe", "stone_pickaxe", "copper_pickaxe", "iron_pickaxe", "golden_pickaxe", "diamond_pickaxe", "netherite_pickaxe"))

# --------------------------------------------------------------------------
def raw_obj(crit):
    if crit == "level": return "sc.r.level"
    kind, item = crit.split(":", 1)
    short = {"minecraft.mined": "m", "minecraft.custom": "c", "minecraft.killed": "k",
             "minecraft.killed_by": "kb", "minecraft.used": "u", "minecraft.broken": "b"}[kind]
    return "sc.r.%s.%s" % (short, item.split(".", 1)[1])

def snbt(v):
    if isinstance(v, bool): return "1b" if v else "0b"
    if isinstance(v, int): return str(v)
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list): return "[" + ",".join(snbt(x) for x in v) + "]"
    if isinstance(v, dict): return "{" + ",".join("%s:%s" % (k, snbt(x)) for k, x in v.items()) + "}"
    raise TypeError(v)

raws = {}          # objetivo crudo -> criterio
db = []
calc = []

for idx, s in enumerate(STATS):
    i = 101 + idx
    src = s["src"]
    if isinstance(src, tuple):
        a, b = raw_obj(src[1]), raw_obj(src[2])
        raws[a] = src[1]; raws[b] = src[2]
        obj = "sc." + s["id"]
        calc += ["scoreboard players operation #a sc.calc = @s %s" % a,
                 "scoreboard players operation #a sc.calc *= #100 sc.calc",
                 "scoreboard players operation #b sc.calc = @s %s" % b,
                 "execute if score #b sc.calc matches ..0 run scoreboard players set #b sc.calc 1",
                 "scoreboard players operation #a sc.calc /= #b sc.calc",
                 "scoreboard players operation @s %s = #a sc.calc" % obj]
        s["dummy"] = obj
    elif len(src) == 1:
        obj = raw_obj(src[0]); raws[obj] = src[0]
    else:
        obj = "sc." + s["id"]; s["dummy"] = obj
        calc.append("scoreboard players set @s %s 0" % obj)
        for c in src:
            r = raw_obj(c); raws[r] = c
            calc.append("scoreboard players operation @s %s += @s %s" % (obj, r))
    s["o"] = obj
    cat = CATS[s["c"]]
    cmd = "trigger statscraft set %d" % i
    db.append(dict(i=i, id=s["id"], n=s["n"], c=s["c"], col=cat["col"], f=s["f"], o=obj, cmd=cmd,
                   b=dict(label=dict(text=s["n"], color=cat["col"]),
                          tooltip=dict(text=s["c"] + " · ver ranking", color="gray"),
                          action=dict(type="minecraft:run_command", command=cmd))))

def write(rel, text):
    p = os.path.join(NS, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

HDR = "# ARCHIVO GENERADO por tools/generate.py - no editar a mano.\n"

lines = [HDR]
for o, c in sorted(raws.items()):
    lines.append('function statscraft:util/add_obj {o:"%s",c:"%s",d:"%s"}' % (o, c, c))
for s in STATS:
    if "dummy" in s:
        lines.append('function statscraft:util/add_obj {o:"%s",c:"dummy",d:%s}' % (s["dummy"], json.dumps(s["n"], ensure_ascii=False)))
write("function/gen/objectives.mcfunction", "\n".join(lines) + "\n")

pads = ["." * (2 + 3 * k) for k in range(41)]
write("function/gen/db.mcfunction", HDR +
      "data modify storage statscraft:db stats set value %s\n" % snbt(db) +
      "data modify storage statscraft:db pads set value %s\n" % snbt([" %s " % p for p in pads]))

write("function/gen/calc.mcfunction", HDR + "# Calcula las stats combinadas (sumas y ratios) para @s\n" + "\n".join(calc) + "\n")

un = [HDR]
for o in sorted(raws): un.append("scoreboard objectives remove " + o)
for s in STATS:
    if "dummy" in s: un.append("scoreboard objectives remove " + s["dummy"])
write("function/gen/uninstall.mcfunction", "\n".join(un) + "\n")

menu = {
    "type": "minecraft:multi_action",
    "title": {"text": "StatsCraft", "color": "gold", "bold": True},
    "external_title": {"text": "★ StatsCraft", "color": "gold"},
    "body": {"type": "minecraft:plain_message", "width": 400, "contents": [
        {"text": "Rankings del servidor. ", "color": "gray"},
        {"text": "Toca una estadística", "color": "white"},
        {"text": " para ver el top. ", "color": "gray"},
        {"text": "Esc", "color": "yellow"}, {"text": " para salir.", "color": "gray"}]},
    "columns": 3,
    "pause": False,
    # Espera a que el servidor mande el ranking en vez de cerrar el diálogo.
    # Si se cerrara, se volvería al menú de pausa y en un solo jugador el juego
    # se pausa: el /trigger no se procesa hasta que quitas la pausa.
    "after_action": "wait_for_response",
    "actions": [d["b"] for d in db],
    # Sin botón "Cerrar": con wait_for_response ese botón deja al cliente unos
    # segundos en "esperando respuesta". Esc cierra directo, sin esperar.
}
write("dialog/menu.json", json.dumps(menu, ensure_ascii=False, indent=1) + "\n")

print("stats:", len(STATS), "| objetivos crudos:", len(raws))
