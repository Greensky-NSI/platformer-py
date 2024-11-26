import random

from p5 import *
from src.Designs.DoorDesign import draw_door
from src.utils.toolbox import safe_fill


class Particle:
    def __init__(self, x, y, longueur_porte, hauteur_porte, vitesse_particule=3):
        self.direction = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.x = x + longueur_porte / 2
        self.y = y - hauteur_porte / 2
        self.l = longueur_porte
        self.h = hauteur_porte
        self.v = vitesse_particule
        self.pos_porte = (x + longueur_porte / 2, y - hauteur_porte / 2)

    @staticmethod
    def create_particles(nb_particules, x, y, longueur_porte, hauteur_porte):
        return [Particle(x, y, longueur_porte, hauteur_porte) for _ in range(nb_particules)]

    def update(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def display(self):
        strokeWeight(0)
        safe_fill((0, 0, 255))
        ellipse(self.x, self.y, 6, 6)

    def particle_position(self):
        return not ((self.pos_porte[0] - self.l < self.x < self.pos_porte[0] + self.l) and (
                    self.pos_porte[1] - self.h < self.y < self.pos_porte[1] + self.h))

class Door:
    def __init__(self, x, y, longueur, hauteur, exit=False, particles: list[Particle] = [], *, couleur=(0, 0, 0)):
        self.x = x
        self.y = y
        self.l = longueur
        self.h = hauteur
        self.exit = exit
        self.particles = particles
        self.couleur = couleur

    def display(self):
        draw_door(self.x, self.y, self.l, self.h, self.couleur)
        self.draw_particles()

    def draw_particles(self):
        for p in self.particles:
            p.update()
            p.display()

            if p.particle_position():
                self.particles.remove(p)
            if p.pos_porte[0] - 1 < p.x < p.pos_porte[0] + 1 and -p.pos_porte[1] - 1 < p.y < -p.pos_porte[1] + 1:
                self.particles.remove(p)

    @staticmethod
    def create_door_with_particles(x, y, longueur, hauteur, nb_particules):
        door = Door(x, y, longueur, hauteur)
        door.particles = Particle.create_particles(nb_particules, x, y, longueur, hauteur)
        return door

    @property
    def hitbox(self):
        return self.x, self.y, self.x + self.l, self.y - self.h