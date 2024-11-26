from src.classes.environnement.Level import Level
from src.classes.environnement.plateforme import Plateforme
from src.classes.statics.Cadeau import Cadeau
from src.classes.statics.Door import Door

level_one = Level(1)

level_one.add_platform(Plateforme(215, 745, 150, 10))
level_one.add_platform(Plateforme(450, 703, 128, 8))
level_one.add_platform(Plateforme(298, 668, 75, 10))
level_one.add_platform(Plateforme(426, 616, 20, 5))
level_one.add_platform(Plateforme(530, 603, 40, 10, (8, 173, 219)))
level_one.add_platform(Plateforme(47, 629, 185, 10))

for i in range(5):
    level_one.add_platform(Plateforme(68 - i * 2, 594 - i * 75, 35, 5))
    level_one.add_platform(Plateforme(168 + i * 2, 547 - i * 75, 35, 5))

level_one.add_platform(Plateforme(249, 195, 150, 10))
level_one.add_platform(Plateforme(448, 150, 131, 10))
level_one.add_platform(Plateforme(22, 132, 151, 5, (8, 173, 219)))

level_one.add_cadeau(Cadeau(x=545, y=603, echelle=.8))
level_one.add_cadeau(Cadeau(x=22, y=131, echelle=.6))

level_one.set_player_spawn(54, 774)

level_one.add_door(Door.create_door_with_particles(546, 150, 30, 40, 10))