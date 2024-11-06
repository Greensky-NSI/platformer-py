from p5 import *

# Définir les couleurs du personnage
hero_color = Color(30, 144, 255)    # Couleur principale
body_color = Color(0, 128, 128)     # Couleur du corps
detail_color = Color(255, 215, 0)   # Couleur des détails (ex. ceinture)

def setup():
    size(64, 64)

def draw_character():
    background(220)
    
    # Tête
    fill(hero_color)
    rect((24, 8), 16, 16)

    # Corps
    fill(body_color)
    rect((22, 24), 20, 24)

    # Bras
    rect((14, 26), 8, 18)  # bras gauche
    rect((42, 26), 8, 18)  # bras droit

    # Jambes
    fill(hero_color)
    rect((24, 48), 8, 12)  # jambe gauche
    rect((32, 48), 8, 12)  # jambe droite

    # Détails : ceinture
    fill(detail_color)
    rect((28, 40), 8, 4)

def draw():
    draw_character()
    
run()
