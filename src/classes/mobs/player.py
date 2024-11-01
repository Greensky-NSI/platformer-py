from src.utils.toolbox import parse_integer, parse_position, safe_stroke, safe_fill, parse_position_in_walls
from src.utils.globals import player_variables
from src.types.movement import Direction
from p5 import rect, strokeWeight

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
        self._x = parse_position_in_walls(parse_position(self._x + self._ds * (1 if direction == "right" else -1), "width"), "width")

    def display(self):
        safe_fill((210, 105, 30))
        safe_stroke((0, 0, 0))
        strokeWeight(1)
        rect(self._x, self._y, self._width, self._height)