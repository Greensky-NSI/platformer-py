# Variables à utiliser dans tout le projet
# Les variables sont définies ici sous forme de classe pour éviter les problèmes de portée, et pour avoir l'auto complétion dans les IDE, ainsi que la vérification de type/erreurs pré-exécution

## Variables relatives au joueur
class movements:
    left = ["q", "a", "left"]
    right = ["d", "right"]
    up = ["z", "w", "up", " "]

class player_variables:
    max_health =  100
    min_health = 0
    width = 10
    height = 20
    delta_speed = 2

    deplacements_keymap = movements

    player_colors = {
        "hero_color": (30, 144, 255),  # Couleur principale
        "body_color": (0, 128, 128),  # Couleur du corps
        "detail_color": (255, 215, 0)
    }

## Variables relatives à l'environnement
class env:
    width = 600
    height = 800