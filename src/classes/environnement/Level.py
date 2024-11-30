from src.classes.environnement.plateforme import Plateforme
from src.classes.mobs.Monster import Monster
from src.classes.statics.Cadeau import Cadeau
from src.classes.statics.Door import Door
from src.utils.toolbox import is_pos_in_walls


class Level:
    _gifts: list[Cadeau]
    _doors: list[Door]
    _platforms: list[Plateforme]
    _player_spawn: tuple[int, int]
    _number: int = 0
    _monsters: list[Monster]

    def __init__(self, number: int):
        self._number = number

        self._gifts = []
        self._doors = []
        self._platforms = []
        self._monsters = []
        self._player_spawn = (50, 50)
        self._ended = False

    def add_platform(self, platform: Plateforme):
        assert isinstance(platform, Plateforme), "La plateforme doit être une instance de Plateforme"

        self._platforms.append(platform)

    def add_cadeau(self, cadeau: Cadeau):
        assert isinstance(cadeau, Cadeau), "Le cadeau doit être une instance de Cadeau"

        self._gifts.append(cadeau)

    def add_door(self, door: Door):
        assert isinstance(door, Door), "La porte doit être une instance de Door"

        self._doors.append(door)
    
    def add_door_on_player_spawn(self, longueur, hauteur, couleur=(0, 0, 0)):
        door = Door(self._player_spawn[0] - longueur // 2, self._player_spawn[1], longueur, hauteur, False, [], couleur=couleur)
        
        self._doors.append(door)

    def add_monster(self, monster: Monster):
        assert isinstance(monster, Monster), "Le monstre doit être une instance de Monster"

        self._monsters.append(monster)

    def set_player_spawn(self, x: int, y: int):
        assert isinstance(x, int), "La coordonnée x doit être un entier"
        assert isinstance(y, int), "La coordonnée y doit être un entier"
        assert is_pos_in_walls(x, y), "La position du joueur doit être dans les murs"

        self._player_spawn = (x, y)

    @property
    def gifts(self):
        return self._gifts

    @property
    def doors(self):
        return self._doors

    @property
    def platforms(self):
        return self._platforms

    @property
    def player_spawn(self):
        return self._player_spawn

    @property
    def number(self):
        return self._number

    @property
    def monsters(self):
        return self._monsters