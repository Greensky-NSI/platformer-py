from src.abstract.Ticker import Ticker
from src.classes.core.DOM import DOM
from src.classes.mobs.player import Player

from src.levels import one

player = Player("Greensky", 100)

game_ticker = Ticker()
game_DOM = DOM.from_level(one.level_one, player)

game_DOM.set_ticker(game_ticker)
