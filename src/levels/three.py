from src.classes.environnement.Level import Level
from src.classes.environnement.plateforme import Plateforme
from src.classes.mobs.Monster import Monster
from src.classes.statics.Cadeau import Cadeau
from src.utils.globals import env
from src.classes.statics.Door import Door

level_three = Level(3)

for i in range(10):
    length = 38
    level_three.add_platform(Plateforme((400 - length) - i * length, 768 - 30 * i, length, 10))

level_three.add_platform(Plateforme(130, 440, env.width - env.wall_total_width - 130, 10))

level_three.set_player_spawn(523, 778)
level_three.add_door_on_player_spawn(35, 45)
level_three.add_platform(Plateforme(340, 415, 40, 5))

for i in range(5):
    level_three.add_platform(Plateforme(37 - i * 2, 410 - i * 75, 35, 5))
    level_three.add_platform(Plateforme(97 + i * 2, 430 - i * 75, 35, 5))

    level_three.add_platform(Plateforme(182 + 70 * i, 130, 35, 5))

level_three.add_monster(Monster(y=440, move_range_x=(170, env.width - env.wall_total_width - 40), echelle=1, delta_x=2))
level_three.add_cadeau(Cadeau(x=528, y=440))
level_three.add_platform(Plateforme(462, 130, env.width - env.wall_total_width - 462, 5))
level_three.add_door(Door.create_door_with_particles(543, 130, 35, 45, 10, True))