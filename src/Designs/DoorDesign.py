from p5 import *


def draw_door(x, y, longueur, hauteur):
    strokeWeight(0)
    fill(0, 0, 0)
    rect(x, y, longueur, -hauteur)
    ellipse(x + longueur / 2, y - hauteur, longueur, hauteur / 2)
