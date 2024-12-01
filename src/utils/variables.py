from src.utils.niveaux import niveaux
from src.abstract.Ticker import Ticker
from src.classes.mobs.player import Player
from src.classes.core.DOM import DOM


player = Player("Greensky", 100)

game_ticker = Ticker()
game_DOM: DOM = DOM(ticker=game_ticker, players=[player])

levels = len(niveaux)