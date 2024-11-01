from src.utils.toolbox import parse_integer, parse_position, safe_stroke, safe_fill, parse_position_in_walls
from src.utils.globals import player_variables, env
from src.types.movement import Direction
from p5 import rect, strokeWeight

class Player:
    def __init__(self, name, health):
        self._name = name
        self._health = min(max(parse_integer(health), player_variables.min_health), player_variables.max_health)
        self._x = env.width // 2
        self._y = env.height - player_variables.height - env.wall_width
        self._ds = player_variables.delta_speed
        self._width = player_variables.width
        self._height = player_variables.height

    def move(self, direction: Direction):
        modifier = 1 if direction == "right" else -1
        new_position = self._x + self._ds * modifier

        new_position = parse_position_in_walls(parse_position(new_position, "width"), "width")
        new_position = parse_position_in_walls(new_position + self._width, "width") - self._width
        self._x = new_position

    def display(self):
        safe_fill((210, 105, 30))
        safe_stroke((0, 0, 0))
        strokeWeight(1)
        rect(self._x, self._y, self._width, self._height)