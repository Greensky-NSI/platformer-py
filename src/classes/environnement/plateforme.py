class Plateforme:
    def __init__(self, x, y, largeur, hauteur):
        """
        Initialise une nouvelle plateforme.

        Args:
            x (int): Position x de la plateforme.
            y (int): Position y de la plateforme.
            largeur (int): Largeur de la plateforme.
            hauteur (int): Hauteur de la plateforme.
        """
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur

    def afficher(self):
        """
        Affiche la plateforme sur l'écran (méthode utile pour un jeu utilisant une bibliothèque)
        """
        self.couleur = (139, 69, 19)
        safe_fill(self.couleur)# couleur marron pour représenter une plateforme classique
        rect(self.x, self.y, self.largeur, self.hauteur)

    def collision(self, joueur):
        """
        Vérifie si le joueur entre en collision avec la plateforme.

        Args:
            joueur: Un objet représentant le joueur avec des attributs de position et de taille.

        Return:
            bool: True si le joueur est en collision avec la plateforme, sinon False.
        """
        return (
            joueur.x + joueur.largeur > self.x and
            joueur.x < self.x + self.largeur and
            joueur.y + joueur.hauteur > self.y and
            joueur.y < self.y + self.hauteur
        )
