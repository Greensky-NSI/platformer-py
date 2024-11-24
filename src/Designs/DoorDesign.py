from p5 import *

from src.utils.toolbox import safe_fill


def draw_door(x, y, longueur, hauteur, couleur):
    strokeWeight(0)
    safe_fill(couleur)
    rect(x, y, longueur, -hauteur)
    ellipse(x + longueur / 2, y - hauteur, longueur, hauteur / 2)
