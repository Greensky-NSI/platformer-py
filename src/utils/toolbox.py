from typing import Literal
from src.utils.globals import env
from p5 import fill, stroke
from src.types.entities import hitbox_type

def parse_integer(number: any, default = 0) -> int:
    """
    Renvoie l'entrée sous forme d'entier si possible, sinon renvoie la valeur par défaut.

    :param number: any - La valeur à convertir en entier.
    :param default: int - La valeur par défaut à renvoyer si la conversion échoue.
    :return: int
    """
    return int(parse_float(number, default))

def parse_float(number: any, default = 0.0) -> float:
    """
    Renvoie l'entrée sous forme de flottant si possible, sinon renvoie la valeur par défaut.

    :param number: any - La valeur à convertir en flottant.
    :param default: float - La valeur par défaut à renvoyer si la conversion échoue.
    :return: float
    """

    try:
        return float(number)
    except ValueError:
        return default

def parse_position(position: int, dimension: Literal["width", "height"] = "width") -> int:
    """
    Renvoie la position sous forme d'entier positif, encadrée par les dimensions du jeu.

    :param position: int - La position à convertir.
    :param dimension: Literal["width", "height"] - La dimension à laquelle la position doit être encadrée.
    :return: int
    """

    dimens = env.width
    if dimension == "height":
        dimens = env.height

    return max(min(position, dimens), 0)
def safe_fill(couleur: tuple[int, int, int]):
    """
    Remplit la forme suivante avec la couleur donnée, et sauvegarde la couleur actuelle.

    :param couleur: tuple[int, int, int] - La couleur à utiliser.
    """
    r, g, b = couleur

    fill(r, g, b)
def safe_stroke(couleur: tuple[int, int, int]):
    """
    Définit la couleur du contour suivant avec la couleur donnée, et sauvegarde la couleur actuelle.

    :param couleur: tuple[int, int, int] - La couleur à utiliser.
    """
    r, g, b = couleur

    stroke(r, g, b)

def parse_position_in_walls(position: int, dimension: Literal["width", "height"] = "width") -> int:
    """
    Renvoie la position sous forme d'entier positif, encadrée par les dimensions du jeu, en prenant en compte les murs.

    :param position: int - La position à convertir.
    :param dimension: Literal["width", "height"] - La dimension à laquelle la position doit être encadrée.
    :return: int
    """

    left_limit = env.wall_total_width
    right_limit = env.width - env.wall_total_width

    if dimension == "height":
        left_limit = env.wall_width
        right_limit = env.height - env.wall_total_width


    return max(min(position, right_limit), left_limit)

def hitbox_collide(a: hitbox_type, b: hitbox_type):
    """
    Vérifie si deux hitbox se touchent

    :param a: hitbox de l'objet 1
    :param b: hitbox de l'objet 2
    :return: bool le résultat du test
    """

    return (a[0] <= b[0] and a[2] >= b[2] and a[1] <= b[1] and a[3] >= b[3]) or (b[0] <= a[0] and b[2] >= a[2] and b[1] <= a[1] and b[3] >= a[3])