from typing import List
from datetime import datetime
from p5 import text, scale

from src.Designs.decoration import decoration
from src.Designs.end_screen import end_screen
from src.abstract.Cache import Cache
from src.abstract.Stack import Pile
from src.abstract.Ticker import Ticker
from src.classes.environnement.Level import Level
from src.classes.mobs.player import Player
from src.classes.statics.Cadeau import Cadeau
from src.types.DOM import EntitiesType
from src.types.enums import DOMCache
from src.utils.globals import env
from src.utils.toolbox import hitbox_collide, safe_fill
from src.classes.statics.Door import Door
from src.classes.environnement.plateforme import Plateforme
from src.classes.mobs.Monster import Monster


class DOM:
    entities: EntitiesType = EntitiesType()
    ticker: Ticker
    collected_gifts: Pile[Cadeau] = Pile[Cadeau]()
    _cache = Cache = Cache()
    _ended = False
    _started = False
    spawn: tuple[int, int] = (0, 0)

    def __init__(self, *, ticker: Ticker = Ticker, players: List[Player] = (), gifts: List[Cadeau] = (), doors: List[Door] = (), platforms: List[Plateforme] = (), monsters: List[Monster] = ()):
        # Assertions
        assert all([x is not None and isinstance(x, Player) for x in
                    players]), "La liste des joueurs du DOM contient des éléments qui ne sont pas des joueurs"
        assert all([x is not None and isinstance(x, Cadeau) for x in
                    gifts]), "La liste des cadeaux du DOM contient des éléments qui ne sont pas des cadeaux"
        assert all([x is not None and isinstance(x, Door) for x in
                    doors]), "La liste des portes du DOM contient des éléments qui ne sont pas des portes"
        assert all([x is not None and isinstance(x, Plateforme) for x in
                    platforms]), "La liste des plateformes du DOM contient des éléments qui ne sont pas des plateformes"
        assert all([x is not None and isinstance(x, Monster) for x in
                    monsters]), "La liste des monstres du DOM contient des éléments qui ne sont pas des monstres"

        # Assignations
        self.entities.players = list(players)
        self.entities.gifts = list(gifts)
        self.entities.doors = list(doors)
        self.entities.platforms = list(platforms)
        self.entities.monsters = list(monsters)
        self.ticker = ticker
        self.spawn = players[0].x, players[0].y

        self._cache.cache(DOMCache.GAME_START_TIME, self.current_time)

    @property
    def started(self):
        return self._started

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

    @property
    def players(self):
        return self.entities.players

    def check_gift_collisions(self):
        if self.collected_gifts.taille == len(self.entities.gifts):
            self._cache.cache(DOMCache.CHECK_FOR_GIFTS, False)
            return

        for player in self.entities.players:
            self.check_collision_with_gifts_player(player)

    def check_for_doors(self):
        for player in self.entities.players:
            for door in self.entities.doors:
                if door.is_exit and hitbox_collide(player.hitbox, door.hitbox):
                    self.ended_callback()

    def ended_callback(self):
        self._ended = True

        self._cache.cache(DOMCache.GAME_END_TIME, self.current_time)

    def on_end(self):
        time = self._cache.get(DOMCache.GAME_END_TIME) - self._cache.get(DOMCache.GAME_START_TIME)
        end_screen(time)

    def reset(self):
        self.entities.players[0].teleport(*self.spawn)

        self._ended = False
        while not self.collected_gifts.vide:
            gift = self.collected_gifts.depiler()
            gift.reveal()

        self._cache.delete(DOMCache.CHECK_FOR_GIFTS)

    def check_collision_with_monsters(self):
        for monster in self.entities.monsters:
            for player in self.entities.players:
                if hitbox_collide(player.hitbox, monster.hitbox):
                    self.reset()

    def display(self):
        if self._ended:
            self.on_end()
            return

        decoration()

        for door in self.entities.doors:
            if self.collected_all_gifts and door.is_exit:
                door.display()
            elif not door.is_exit:
                door.display()

        for player in self.entities.players:
            player.display()

        self.apply_players_jump()
        self.apply_players_gravity()

        for cadeau in self.entities.gifts:
            cadeau.display()

        for plateforme in self.entities.platforms:
            plateforme.afficher()

        for monster in self.entities.monsters:
            monster.tick()
            monster.display()

        self.display_time()

        self.check_collision_with_monsters()
        self.check_for_doors()

        if self._cache.get(DOMCache.CHECK_FOR_GIFTS, True):
            self.check_gift_collisions()

    def reload_from_level(self, level: Level):
        self.entities.gifts = level.gifts
        self.entities.doors = level.doors
        self.entities.platforms = level.platforms
        self.entities.monsters = level.monsters

        self._cache.cache(DOMCache.GAME_START_TIME, self.current_time)

        self.spawn = level.player_spawn

        self._started = True
        for p in self.players:
            p.teleport(*self.spawn)

    def set_none_level(self):
        self._started = False

    def display_time(self):
        time = self.current_time - self._cache.get(DOMCache.GAME_START_TIME)
        time = time // 1000

        safe_fill((30, 10, 10))

        # Convert to seconds, minutes and hours
        seconds = time % 60
        minutes = time // 60
        hours = minutes // 60

        displayed_text = ""
        if hours > 0:
            displayed_text += f"{hours}h"
        if minutes > 0:
            if len(displayed_text) > 0:
                displayed_text += " "
            displayed_text += f"{minutes}m"
        if seconds > 0:
            if len(displayed_text) > 0:
                displayed_text += " "
            displayed_text += f"{seconds}s"

        scale(1.2)
        text(displayed_text, env.wall_total_width + 3, env.wall_total_width + 3)
        scale(1 / 1.2)

    def set_ticker(self, ticker: Ticker):
        self.ticker = ticker

    @property
    def dom_ticker(self):
        return self.ticker

    @property
    def collected_all_gifts(self):
        return self.collected_gifts.taille == len(self.entities.gifts)

    @staticmethod
    def from_level(level: Level, player: Player):
        player.teleport(*level.player_spawn)

        return DOM(gifts=level.gifts, doors=level.doors, platforms=level.platforms, players=[player], monsters=level.monsters)

    @property
    def current_time(self):
        return int(datetime.now().timestamp() * 1000) # En millisecondes