from p5 import *

from src.classes.environnement.decoration import decoration
from src.custom_types import *

from src.utils.globals import env, player_variables
from src.classes.mobs.player import Player

def setup():
    size(env.width, env.height)

player = Player("Greensky", 100)

def draw():
    decoration()

    # player.display()
    if key_is_pressed:
        pressed = str(key).lower()

        if pressed in player_variables.deplacements_keymap.left:
            player.move("left")
        elif pressed in player_variables.deplacements_keymap.right:
            player.move("right")
        elif pressed in player_variables.deplacements_keymap.up:
            pass

run()