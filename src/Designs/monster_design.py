from p5 import scale, rect, no_stroke

from src.utils.toolbox import safe_fill, safe_stroke
from src.types.movement import Direction


def monster_design(x: int, y: int, *, echelle = 1, couleur: tuple[int, int, int] = (180, 0, 0), direction: Direction):
    safe_fill(couleur)

    scale(echelle, echelle)

    global_offset = 2 * (-1 if direction == "left" else 1)

    safe_stroke((0, 0, 0))
    rect(x, y, 40, -40)

    safe_fill((0, 0, 0))
    rect(x + 10 + global_offset, y - 30, 5, -5)
    rect(x + 25 + global_offset, y - 30, 5, -5)
    rect(x + 5 + global_offset, y - 5, 30, -5)

    no_stroke()
    scale(1 / echelle, 1 / echelle)