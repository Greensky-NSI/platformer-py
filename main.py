from p5 import *

from src.Designs.decoration import decoration
from src.custom_types import *
from src.utils.globals import env, player_variables
from src.utils.variables import game_ticker, game_DOM, player
from src.classes.core.Menu import Menu

global menu
menu=Menu()

def setup():
    size(env.width, env.height)
    game_ticker.register("game_start")

    for i in range(len(game_DOM)):
        game_DOM[i].add_player_in_dom(player)


def draw():
    game_ticker.tick()
    menu.display_menu()
        
    
    if key_is_pressed:
        pressed = str(key).lower()

        # Tests de déplacements horizontaux
        if pressed in player_variables.deplacements_keymap.left:
            player.move("left")
        elif pressed in player_variables.deplacements_keymap.right:
            player.move("right")
        else:
            player.stop_moving()

        # Test de déplacement vertical
        if pressed in player_variables.deplacements_keymap.up:
            player.jump(game_ticker)
    else:
        player.stop_moving()
    if mouse_is_pressed:
        player.jump(game_ticker)

    if env.dev:
        fill(0)
        text(f"X: {mouse_x} Y: {mouse_y}", 30, 30)

        if mouse_is_pressed and mouse_button == "RIGHT":
            player.teleport(mouse_x, mouse_y)


run()