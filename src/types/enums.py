# Liste des énumérateurs

## Les énumérateurs sont définis par une classe pour une approche plus interactive lors du développement
## Par convention, on définira les noms des énumérateurs en CamelCase
## Les clés des valeurs sont définies en majuscule, avec des "_" pour séparer les mots
## Les valeurs des clés seront des textes ou des nombres (de préférence seulement des entiers) ou des booléens

class PlayerCache:
    JUMPING = "player_jumping"
    JUMP_START_TICK = "player_jump_start_tick"
    JUMP_START_Y = "player_jump_start_height"
    JUMP_LAST_OUTPUT = "player_jump_function_last_y"
    TOUCHED_GROUND = "player_touched_ground_after_jump"

class DOMCache:
    CHECK_FOR_GIFTS = "dom_run_gift_collisions_test"