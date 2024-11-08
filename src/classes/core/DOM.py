from src.classes.mobs.player import Player
from src.classes.typeClasses.DOM import EntitiesType
from typing import List
from src.utils.globals import env
from src.abstract.Ticker import Ticker

class DOM:
    entities: EntitiesType = EntitiesType()
    ticker: Ticker

    def __init__(self, *, ticker: Ticker = Ticker, players: List[Player] = ()):
        # Assertions
        assert all([x is not None and isinstance(x, Player) for x in players]), "La liste des joueurs du DOM contient des éléments qui ne sont pas des joueurs"

        # Assignations
        self.entities.players = list(players)
        self.ticker = ticker

    def apply_players_gravity(self):
        for player in self.entities.players:
            if player.jumping:
                continue
            # à compléter avec les plateformes
            ground_y = env.height - env.wall_total_width

            distance_from_ground = ground_y - player.y
            if distance_from_ground > 0:
                player.fall()
            else:
                player.touched_ground()

    def apply_players_jump(self):
        for player in self.entities.players:
            if not player.jumping:
                return

            player.add_jump(self.ticker)

    def tick(self):
        self.apply_players_gravity()
        self.apply_players_jump()

    def add_player_in_dom(self, player: Player):
        # Assertions
        assert isinstance(player, Player), "Le joueur n'est pas de type joueur"

        # Code
        if not player in self.entities.players:
            self.entities.players.append(player)


    @property
    def dom_ticker(self):
        return self.ticker