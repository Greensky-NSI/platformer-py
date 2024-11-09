# Variables à utiliser dans tout le projet
# Les variables sont définies ici sous forme de classe pour éviter les problèmes de portée, et pour avoir l'auto complétion dans les IDE, ainsi que la vérification de type/erreurs pré-exécution
from p5 import Color


## Couleurs
class couleurs_cadeau:
    couleur_principale = (121, 33, 255)
    couleur_ruban = (255, 213, 61)

class couleurs:
    decoration_border_color = (128, 128, 128)
    decoration_wall_color = (0, 12, 20)
    background_fill_color = 200

    couleurs_cadeau: couleurs_cadeau

## Variables relatives au joueur
class movements:
    left = ["q", "a", "left"]
    right = ["d", "right"]
    up = ["z", "w", "up", " "]

class player_variables:
    max_health =  100
    min_health = 0
    width = 30
    height = 52
    delta_speed = 5
    falling_delta_speed = int(delta_speed)

    deplacements_keymap = movements

    player_colors = {
        "hero_color": (30, 144, 255),  # Couleur principale
        "body_color": (0, 128, 128),  # Couleur du corps
        "head_color": (0, 0, 0),
        "left_leg_color": (0, 0, 255),
        "right_leg_color": (255, 255, 255),
        "left_arm_color": (255, 0, 0),
        "right_arm_color": (0, 255, 0),
        "detail_color": (255, 215, 0)
    }

## Variables relatives à l'environnement
class env:
    width = 600
    height = 800
    wall_width = 20
    wall_border_stroke = 2
    wall_total_width = wall_width + wall_border_stroke

## Variables relatives au objets
class variables_cadeau:
    couleurs = couleurs_cadeau

    size = 50
    tailles_noeuds = [20, 25]

    epaisseur_ruban = 8
