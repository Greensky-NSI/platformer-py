from src.Designs.cadeau import cadeau_dessin
from src.utils.globals import variables_cadeau

class Cadeau:
    def __init__(self, *, x = 0, y = 0, echelle = 1):
        self._x = x
        self._y = y
        self._scale = echelle
        self._displayed = True

    def display(self):
        if self._displayed:
            cadeau_dessin(self._x, self._y, self._scale)

    @property
    def affiche(self):
        return self._displayed

    @property
    def width(self):
        return variables_cadeau.size * self._scale

    @property
    def height(self):
        return self.width

    def hide(self):
        self._displayed = False