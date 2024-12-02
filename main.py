from p5 import *

from src.Designs.decoration import decoration
from src.custom_types import *
from src.utils.globals import env, player_variables
from src.utils.variables import game_ticker, game_DOM, player
from src.classes.core.Menu import Menu

def setup():
    size(env.width, env.height)
    game_ticker.register("game_start")

menu = Menu(game_DOM)

def draw():
    if not game_DOM.started:
        menu.display_menu()
        return

    game_DOM.ticker.tick()

    background(128)
    game_DOM.display()

    if key_is_pressed:
        pressed = str(key).lower()

        # Tests de déplacements horizontaux
        if pressed in player_variables.deplacements_keymap.left:
            game_DOM.players[0].move("left")
        elif pressed in player_variables.deplacements_keymap.right:
            game_DOM.players[0].move("right")
        else:
            game_DOM.players[0].stop_moving()

        # Test de déplacement vertical
        if pressed in player_variables.deplacements_keymap.up:
            game_DOM.players[0].jump(game_DOM.ticker)
    else:
        game_DOM.players[0].stop_moving()
    if mouse_is_pressed:
        game_DOM.players[0].jump(game_DOM.ticker)

    if env.dev:
        fill(0)
        text(f"X: {mouse_x} Y: {mouse_y}", 30, 30)

        if mouse_is_pressed and mouse_button == "RIGHT":
            game_DOM.players[0].teleport(mouse_x, mouse_y)


run()
