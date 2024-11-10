from src.abstract.Cache import Cache
from src.classes.mobs.player import Player
from src.classes.statics.Cadeau import Cadeau
from src.classes.typeClasses.DOM import EntitiesType
from typing import List

from src.types.enums import DOMCache
from src.utils.globals import env
from src.abstract.Ticker import Ticker
from src.abstract.Stack import Pile
from src.utils.toolbox import hitbox_collide


class DOM:
    entities: EntitiesType = EntitiesType()
    ticker: Ticker
    collected_gifts: Pile[Cadeau] = Pile[Cadeau]()
    _cache = Cache = Cache()

    def __init__(self, *, ticker: Ticker = Ticker, players: List[Player] = (), gifts: List[Cadeau] = ()):
        # Assertions
        assert all([x is not None and isinstance(x, Player) for x in players]), "La liste des joueurs du DOM contient des éléments qui ne sont pas des joueurs"
        assert all([x is not None and isinstance(x, Cadeau) for x in gifts]), "La liste des cadeaux du DOM contient des éléments qui ne sont pas des cadeaux"

        # Assignations
        self.entities.players = list(players)
        self.entities.gifts = list(gifts)
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

    def check_collision_with_gifts_player(self, player: Player):
        player_hitbox = player.hitbox  # On stocke la hitbox pour ne pas avoir à la re-calculer constamment
        for gift in self.entities.gifts:
            if not gift.affiche:
                continue

            if hitbox_collide(player_hitbox, gift.hitbox):
                gift.hide()
                self.collected_gifts.empiler(gift)

    def check_gift_collisions(self):
        if self.collected_gifts.taille == len(self.entities.gifts):
            self._cache.cache(DOMCache.CHECK_FOR_GIFTS, False)
            return

        for player in self.entities.players:
            self.check_collision_with_gifts_player(player)

    def display(self):
        for player in self.entities.players:
            player.display()

        for cadeau in self.entities.gifts:
            cadeau.display()

        if self._cache.get(DOMCache.CHECK_FOR_GIFTS, True):
            self.check_gift_collisions()

    @property
    def dom_ticker(self):
        return self.ticker