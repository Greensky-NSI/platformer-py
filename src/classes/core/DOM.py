from typing import List

from src.abstract.Cache import Cache
from src.abstract.Stack import Pile
from src.abstract.Ticker import Ticker
from src.classes.environnement.Level import Level
from src.classes.mobs.player import Player
from src.classes.statics.Cadeau import Cadeau
from src.types.DOM import EntitiesType
from src.types.enums import DOMCache
from src.utils.globals import env
from src.utils.toolbox import hitbox_collide
from src.classes.statics.Door import Door
from src.classes.environnement.plateforme import Plateforme


class DOM:
    entities: EntitiesType = EntitiesType()
    ticker: Ticker
    collected_gifts: Pile[Cadeau] = Pile[Cadeau]()
    _cache = Cache = Cache()

    def __init__(self, *, ticker: Ticker = Ticker, players: List[Player] = (), gifts: List[Cadeau] = (), doors: List[Door] = (), platforms: List[Plateforme] = ()):
        # Assertions
        assert all([x is not None and isinstance(x, Player) for x in
                    players]), "La liste des joueurs du DOM contient des éléments qui ne sont pas des joueurs"
        assert all([x is not None and isinstance(x, Cadeau) for x in
                    gifts]), "La liste des cadeaux du DOM contient des éléments qui ne sont pas des cadeaux"
        assert all([x is not None and isinstance(x, Door) for x in
                    doors]), "La liste des portes du DOM contient des éléments qui ne sont pas des portes"
        assert all([x is not None and isinstance(x, Plateforme) for x in
                    platforms]), "La liste des plateformes du DOM contient des éléments qui ne sont pas des plateformes"

        # Assignations
        self.entities.players = list(players)
        self.entities.gifts = list(gifts)
        self.entities.doors = list(doors)
        self.entities.platforms = list(platforms)
        self.ticker = ticker

    def apply_players_gravity(self):
        for player in self.entities.players:
            if player.jumping:
                continue

            platform_heights_under_player = [platform.y for platform in self.entities.platforms if platform.y >= player.y and (platform.x <= player.x <= platform.x + platform.largeur or platform.x <= player.x + player.width <= platform.x + platform.largeur)]
            platform_heights_under_player.append(env.height - env.wall_total_width)

            ground_y = min(platform_heights_under_player)

            distance_from_ground = ground_y - player.y
            if distance_from_ground > player.falling_delta_speed:
                player.fall()
            elif distance_from_ground > 0:
                player.fall(distance_from_ground)
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

    def check_for_doors(self):
        for player in self.entities.players:
            for door in self.entities.doors:
                if hitbox_collide(player.hitbox, door.hitbox):
                    raise NotImplementedError("La collision avec les portes n'est pas encore implémentée")

    def display(self):
        for player in self.entities.players:
            player.display()

        for cadeau in self.entities.gifts:
            cadeau.display()

        for plateforme in self.entities.platforms:
            plateforme.afficher()

        for door in self.entities.doors:
            door.display()

        self.check_for_doors()

        if self._cache.get(DOMCache.CHECK_FOR_GIFTS, True):
            self.check_gift_collisions()

    @property
    def dom_ticker(self):
        return self.ticker

    @staticmethod
    def from_level(level: Level):
        return DOM(players=level.players, gifts=level.gifts, doors=level.doors, platforms=level.platforms)