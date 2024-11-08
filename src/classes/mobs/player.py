from src.utils.toolbox import parse_integer, parse_position, safe_stroke, safe_fill, parse_position_in_walls
from src.utils.globals import player_variables, env
from src.types.movement import Direction
from src.abstract.Cache import Cache
from src.types.enums import PlayerCache
from math import sin
from uuid import uuid4
from src.abstract.Ticker import Ticker
from p5 import translate, scale

from src.Designs.playerDesign import draw_face

class Player:
    def __init__(self, name, health):
        self._name = name
        self._health = min(max(parse_integer(health), player_variables.min_health), player_variables.max_health)
        self._x = env.width // 2
        self._y = env.height - player_variables.height - env.wall_total_width
        self._ds = player_variables.delta_speed
        self._fds = player_variables.falling_delta_speed
        self._width = player_variables.width
        self._height = player_variables.height
        self._cache = Cache()

        self._id = uuid4()

    def move(self, direction: Direction):
        modifier = 1 if direction == "right" else -1
        new_position = self._x + self._ds * modifier

        new_position = parse_position_in_walls(parse_position(new_position, "width"), "width")
        new_position = parse_position_in_walls(new_position + self._width, "width") - self._width
        self._x = new_position

    def fall(self):
        self._y = parse_position_in_walls(self._y + self._fds, "height")

    def jump(self, ticker: Ticker):
        if not self.can_jump:
            return

        self._cache.cache(PlayerCache.JUMPING, True)
        self._cache.cache(PlayerCache.JUMP_START_TICK, ticker.current_tick)
        self._cache.cache(PlayerCache.JUMP_START_Y, self._y)
        self._cache.cache(PlayerCache.TOUCHED_GROUND, False)

        ticker.register(PlayerCache.JUMP_START_TICK)

    def touched_ground(self):
        self._cache.cache(PlayerCache.TOUCHED_GROUND, True)

    def add_jump(self, ticker: Ticker):
        if not self.jumping:
            return
        maximum = 1.5 * self._height

        jump_function = lambda x: sin(x / 4.3)
        x = ticker.diff(PlayerCache.JUMP_START_TICK)

        coeff = jump_function(x)
        total_height = self._cache.get(PlayerCache.JUMP_START_Y, 0) - coeff * maximum

        self._y = total_height

        if coeff == 1 or coeff <= self._cache.get(PlayerCache.JUMP_LAST_OUTPUT, 0):
            self._cache.delete(PlayerCache.JUMPING)
            self._cache.delete(PlayerCache.JUMP_START_TICK)
            self._cache.delete(PlayerCache.JUMP_START_Y)
            self._cache.delete(PlayerCache.JUMP_LAST_OUTPUT)
        else:
            self._cache.cache(PlayerCache.JUMP_LAST_OUTPUT, coeff)

    def display(self):
        translate(self._x, self._y)
        draw_face(1.2)
        translate(-self._x, -self._y)

    @property
    def jumping(self):
        return self._cache.get(PlayerCache.JUMPING, False)

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @property
    def delta_speed(self):
        return self._ds

    @property
    def falling_delta_speed(self):
        return self._fds

    @property
    def can_jump(self):
        return not self.jumping and self._cache.get(PlayerCache.TOUCHED_GROUND, True)

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return other.id == self.id

