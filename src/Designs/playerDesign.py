from p5 import rect
from src.utils.globals import player_variables
from src.utils.toolbox import safe_fill

def draw_head(i=1):
    safe_fill(player_variables.player_colors["head_color"])
    rect(24*i, 8*i, 16*i, 16*i)

def draw_body(i=1):
    safe_fill(player_variables.player_colors["body_color"])
    rect(22*i, 24*i, 20*i, 24*i)

def draw_left_arm(i=1):
    safe_fill(player_variables.player_colors["left_arm_color"])
    rect(14*i, 26*i, 8*i, 18*i)

def draw_right_arm(i=1):
    safe_fill(player_variables.player_colors["right_arm_color"])
    rect(42*i, 26*i, 8*i, 18*i)

def draw_left_leg(i=1):
    safe_fill(player_variables.player_colors["left_leg_color"])
    rect(24*i, 48*i, 8*i, 12*i)
    
def draw_right_leg(i=1):
    safe_fill(player_variables.player_colors["right_leg_color"])
    rect(32*i, 48*i, 8*i, 12*i)

def draw_belt(i=1):
    safe_fill(player_variables.player_colors["detail_color"])
    rect(28*i, 40*i, 8*i, 4*i)

def draw_face(i=2):
    draw_head(i)
    draw_body(i)
    draw_left_arm(i)
    draw_right_arm(i)
    draw_left_leg(i)
    draw_right_leg(i)
    draw_belt(i)
