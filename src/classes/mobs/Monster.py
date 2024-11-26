from src.Designs.monster_design import monster_design
from src.types.entities import hitbox_type
from src.utils.toolbox import is_pos_in_walls
from src.types.movement import Direction


class Monster:
    x: int
    y: int
    move_range_x: tuple[int, int]
    echelle: int
    last_direction: Direction
    delta_x: int

    def __init__(self, *, y, move_range_x: tuple[int, int], echelle = 1, delta_x = 10):
        assert isinstance(move_range_x, tuple), "move_range_x doit être un tuple de 2 entiers"
        assert len(move_range_x) == 2 and all([isinstance(x, int) for x in move_range_x]) , "move_range_x doit être un tuple de 2 entiers"

        assert isinstance(y, int), "y doit être un entiers"
        assert is_pos_in_walls(move_range_x[0], y), "La position de départ du monstre doit être dans les murs"
        assert isinstance(echelle, int) and echelle > 0, "L'échelle doit être un entier positif"
        assert isinstance(delta_x, int) and delta_x > 0, "delta_x doit être un entier positif"

        self.x = (move_range_x[0] + move_range_x[1]) // 2
        self.y = y
        self.move_range_x = (min(move_range_x), max(move_range_x))
        self.echelle = echelle
        self.delta_x = delta_x
        self.last_direction = "right"

    def display(self):
        monster_design(self.x, self.y, echelle = self.echelle, direction = self.last_direction)

    def tick(self):
        if self.last_direction == "right":
            self.x += self.delta_x
            if self.x >= self.move_range_x[1]:
                self.last_direction = "left"
                self.x = self.move_range_x[1]
        else:
            self.x -= self.delta_x
            if self.x <= self.move_range_x[0]:
                self.last_direction = "right"
                self.x = self.move_range_x[0]

    @property
    def hitbox(self) -> hitbox_type:
        return self.x, self.y, self.x + 40 * self.echelle, self.y -40 * self.echelle