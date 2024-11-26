from typing import List

from src.classes.mobs.Monster import Monster
from src.classes.mobs.player import Player
from src.classes.statics.Cadeau import Cadeau
from src.classes.statics.Door import Door
from src.classes.environnement.plateforme import Plateforme

# à compléter avec les classes qui correspondent
class EntitiesType:
    players: List[Player]
    platforms: List[Plateforme]
    monsters: List[Monster]
    gifts: List[Cadeau]
    doors: List[Door]
