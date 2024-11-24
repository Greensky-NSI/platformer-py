import random

from p5 import *
from src.Designs.DoorDesign import draw_door


class Door():
    def __init__(self, x, y, longueur, hauteur, Exit=False):
        self.x = x
        self.y = -y
        self.l = longueur
        self.h = hauteur
        self.Exit = Exit

    def display(self):
        draw_door(self.x, self.y, self.l, self.h)


class Particle:
    def __init__(self, x, y, longueur_porte, hauteur_porte, vitesse_particule=3):
        self.direction = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.x = x + longueur_porte / 2 + self.direction[0]
        self.y = -y - hauteur_porte / 2 + self.direction[1]
        self.l = longueur_porte
        self.h = hauteur_porte
        self.v = vitesse_particule
        self.pos_porte = (x + longueur_porte / 2, -y - hauteur_porte / 2)

    def update(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def display(self):
        strokeWeight(0)
        fill('yellow')
        ellipse(self.x, self.y, 6, 6)

    def particle_position(self):
        return not ((self.pos_porte[0] - self.l < self.x < self.pos_porte[0] + self.l) and (
                    self.pos_porte[1] - self.h < self.y < self.pos_porte[1] + self.h))


def creer_particule(x, y, longueur, hauteur):
    return Particle(x, y, longueur, hauteur)


global particles, Porte
particles = [creer_particule(256, 256, 41, 53) for x in range(15)]
Porte = Door(256, 256, 41, 53)


def draw_particles():
    # Mise à jour et affichage des particules
    for p in particles:
        p.update()
        p.display()

        # Supprime les particules qui sortent de l'écran
        if p.particle_position():
            p.v *= -2
        if p.pos_porte[0] - 1 < p.x < p.pos_porte[0] + 1 and p.pos_porte[1] - 1 < p.y < p.pos_porte[1] + 1:
            particles.remove(p)
