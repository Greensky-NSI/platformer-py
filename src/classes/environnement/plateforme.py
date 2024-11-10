from p5 import rect

from src.utils.toolbox import safe_fill


class Plateforme:
    def __init__(self, x, y, largeur, hauteur, couleur):
        """
        Initialise une nouvelle plateforme.

        Args:
            x (int): Position x de la plateforme.
            y (int): Position y de la plateforme.
            largeur (int): Largeur de la plateforme.
            hauteur (int): Hauteur de la plateforme.
            couleur (tuple): couleur de la plateforme.
        """
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

    def afficher(self):
        """
        Affiche la plateforme sur l'écran
        """
        self.couleur = (139, 69, 19)
        safe_fill(self.couleur)# couleur marron pour représenter une plateforme classique
        rect(self.x, self.y, self.largeur, self.hauteur)

    def collision(self, mob):
        """
        Vérifie si le joueur entre en collision avec la plateforme.

        Args:
            mob: Un objet représentant le joueur (ou un monstre) avec des attributs de position et de taille.

        Return:
            bool: True si le joueur est en collision avec la plateforme, sinon False.
        """
        return (
            mob.x + mob.largeur > self.x and
            mob.x < self.x + self.largeur and
            mob.y + mob.hauteur > self.y and
            mob.y < self.y + self.hauteur
        )
