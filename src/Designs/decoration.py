# Fichier qui décore le cadre du jeu
from p5 import rect, background, no_stroke

from src.utils.globals import env, couleurs
from src.utils.toolbox import safe_fill


def decoration():
    background(couleurs.background_fill_color)

    bg_color = couleurs.decoration_wall_color
    stroke_weight = env.wall_border_stroke
    stroke_color = couleurs.decoration_border_color

    no_stroke()

    # Rectangles simulant les bords
    safe_fill(stroke_color)

    rect(0, 0, env.wall_width + stroke_weight, env.height)
    rect(0, 0, env.width, env.wall_width + stroke_weight)
    rect(env.width - env.wall_width - stroke_weight, 0, env.wall_width, env.height)
    rect(0, env.height - env.wall_width - stroke_weight, env.width, env.wall_width)

    # Rectangles noirs
    safe_fill(bg_color)

    rect(0, 0, env.wall_width, env.height)
    rect(0, 0, env.width, env.wall_width)
    rect(env.width - env.wall_width, 0, env.wall_width, env.height)
    rect(0, env.height - env.wall_width, env.width, env.wall_width)

