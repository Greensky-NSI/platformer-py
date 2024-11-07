from src.utils.toolbox import parse_integer, parse_position, safe_stroke, safe_fill
from src.utils.globals import player_variables
from src.types.movement import Direction
from p5 import rect, translate

class Player:
    def __init__(self, name, health):
        self._name = name
        self._health = min(max(parse_integer(health), player_variables.min_health), player_variables.max_health)
        self._x = 0
        self._y = 0
        self._ds = player_variables.delta_speed
        self._width = player_variables.width
        self._height = player_variables.height

    def move(self, direction: Direction):
        self._x = parse_position(self._x + self._ds * (1 if direction == "right" else -1), "width")

    def display(self):
        translate(self._x, self._y)
        # Tête
        safe_fill(player_variables.player_colors["hero_color"])
        rect((24, 8), 16, 16)

        # Corps
        safe_fill(player_variables.player_colors["body_color"])
        rect(22, 24, 20, 24)

        # Bras
        rect(14, 26, 8, 18)  # bras gauche
        rect(42, 26, 8, 18)  # bras droit

        # Jambes
        safe_fill(player_variables.player_colors["hero_color"])
        rect(24, 48, 8, 12)  # jambe gauche
        rect(32, 48, 8, 12)  # jambe droite

        # Détails : ceinture
        safe_fill(player_variables.player_colors["detail_color"])
        rect(28, 40, 8, 4)

        translate(-self._x, -self._y)