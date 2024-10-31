from typing import Literal

from src.utils.globals import env

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
    return max(min(position, env["width" if dimension == "width" else "height"]), 0)