from src.abstract.Ticker import Ticker
from src.classes.core.DOM import DOM
from src.classes.mobs.player import Player

from src.levels.one import level_one as lvl_1

player = Player("Greensky", 100)

game_ticker = Ticker()
game_DOM=[DOM.from_level(lvl_1, player)]

for i in range(len(game_DOM)):
    game_DOM[i].set_ticker(game_ticker)
