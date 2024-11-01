# Fichier qui décore le cadre du jeu
from src.utils.toolbox import safe_fill
from src.utils.globals import env
from p5 import rect, background, no_stroke

def decoration():
    background(200)

    bg_color = (0, 12, 20)
    bg_width = 20
    stroke_weight = 2
    stroke_color = (128, 128, 128)

    no_stroke()

    # Rectangles simulant les bords
    safe_fill(stroke_color)

    rect(0, 0, bg_width + stroke_weight, env.height)
    rect(0, 0, env.width, bg_width + stroke_weight)
    rect(env.width - bg_width - stroke_weight, 0, bg_width, env.height)
    rect(0, env.height - bg_width - stroke_weight, env.width, bg_width)

    # Rectangles noirs
    safe_fill(bg_color)

    rect(0, 0, bg_width, env.height)
    rect(0, 0, env.width, bg_width)
    rect(env.width - bg_width, 0, bg_width, env.height)
    rect(0, env.height - bg_width, env.width, bg_width)

