import random

from p5 import *
from src.Designs.DoorDesign import draw_door



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

class Door:
    def __init__(self, x, y, longueur, hauteur, exit=False, particles: list[Particle] = []):
        self.x = x
        self.y = -y
        self.l = longueur
        self.h = hauteur
        self.exit = exit
        self.particles = particles

    def display(self):
        draw_door(self.x, self.y, self.l, self.h)

    def draw_particles(self):
        for p in self.particles:
            p.update()
            p.display()

            if p.particle_position():
                self.particles.remove(p)
            if p.pos_porte[0] - 1 < p.x < p.pos_porte[0] + 1 and p.pos_porte[1] - 1 < p.y < p.pos_porte[1] + 1:
                self.particles.remove(p)
