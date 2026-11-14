# Interno: crea un objetivo {o, c, d}. Va por macro para que, si un criterio no
# existe en esta versión, solo falle esa línea y no toda la carga.
$scoreboard objectives add $(o) $(c) "$(d)"
