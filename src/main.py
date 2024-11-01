from p5 import *

from src.classes.environnement.decoration import decoration
from src.custom_types import *

from src.utils.variables import game_ticker
from src.utils.globals import env, player_variables
from src.classes.mobs.player import Player

def setup():
    size(env.width, env.height)
    game_ticker.register("game_start")

player = Player("Greensky", 100)

def draw():
    game_ticker.tick()
    decoration()

    player.display()
    if key_is_pressed:
        pressed = str(key).lower()

        if pressed in player_variables.deplacements_keymap.left:
            player.move("left")
        elif pressed in player_variables.deplacements_keymap.right:
            player.move("right")
        elif pressed in player_variables.deplacements_keymap.up:
            pass

run()