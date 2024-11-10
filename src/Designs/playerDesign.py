from p5 import rect
from src.utils.globals import player_variables
from src.utils.toolbox import safe_fill

def draw_head(i=1):
    safe_fill(player_variables.player_colors["head_color"])
    rect(8*i, -36*i, 16*i, -16*i)

def draw_body(i=1):
    safe_fill(player_variables.player_colors["body_color"])
    rect(8*i, -12*i, 16*i, -24*i)

def draw_left_arm(i=1):
    safe_fill(player_variables.player_colors["left_arm_color"])
    rect(0, -12*i, 8*i, -24*i)

def draw_right_arm(i=1):
    safe_fill(player_variables.player_colors["right_arm_color"])
    rect(24*i, -12*i, 8*i, -24*i)

def draw_left_leg(i=1):
    safe_fill(player_variables.player_colors["left_leg_color"])
    rect(8*i, 0, 8*i, -12*i)
    
def draw_right_leg(i=1):
    safe_fill(player_variables.player_colors["right_leg_color"])
    rect(16*i, 0, 8*i, -12*i)

def draw_belt(i=1):
    safe_fill(player_variables.player_colors["detail_color"])
    rect(11.5*i, -12*i, 10*i, -6*i)

def draw_face(i=2):
    draw_head(i)
    draw_body(i)
    draw_left_arm(i)
    draw_right_arm(i)
    draw_left_leg(i)
    draw_right_leg(i)
    draw_belt(i)

def draw_head_profile(i=1, is_left=False):
    safe_fill(player_variables.player_colors["head_color"])
    if is_left:
        rect(8*i, -36*i, 16*i, -16*i)
    else:
        rect(8*i, -36*i, 16*i, -16*i)# Tête en profil

def draw_body_profile(i=1, is_left=False):
    safe_fill(player_variables.player_colors["body_color"])
    rect(8*i, -12*i, 16*i, -24*i)  # Corps de profil

def draw_arm_profile(i=1, is_left=False):
    safe_fill(player_variables.player_colors["left_arm_color"] if is_left else player_variables.player_colors["right_arm_color"])
    rect(10*i, -14*i, 12*i, -20*i)  # Bras en profil

def draw_leg_profile(i=1, is_left=False):
    safe_fill(player_variables.player_colors["right_leg_color"] if is_left else player_variables.player_colors["left_leg_color"])
    rect(14*i, 0, 8*i, -12*i)  # Jambe arrière en profil

    safe_fill(player_variables.player_colors["left_leg_color"] if is_left else player_variables.player_colors["right_leg_color"])
    rect(8*i, 0, 8*i, -12*i)  # Jambe avant en profil

def draw_right_profile(i=1):
    draw_head_profile(i)
    draw_body_profile(i)
    draw_arm_profile(i)
    draw_leg_profile(i)

def draw_left_profile(i=1):
    draw_head_profile(i, is_left=True)
    draw_body_profile(i, is_left=True)
    draw_arm_profile(i, is_left=True)
    draw_leg_profile(i, is_left=True)
