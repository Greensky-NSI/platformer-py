from p5 import *

# Définir les couleurs du personnage
head_color = Color(0, 0, 0)
left_leg_color = Color(0, 0, 255)
right_leg_color = Color(255, 255, 255)
left_arm_color = Color(255, 0, 0)
right_arm_color = Color(0, 255, 0)# Couleur principale
body_color = Color(0, 128, 128)     # Couleur du corps
detail_color = Color(255, 215, 0)   # Couleur des détails (ex. ceinture)

def setup():
    size(640, 640)
    
def draw_head(i=1):
    fill(head_color)
    rect((24*i, 8*i), 16*i, 16*i)

def draw_body(i=1):
    fill(body_color)
    rect((22*i, 24*i), 20*i, 24*i)

def draw_left_arm(i=1):
    fill(left_arm_color)
    rect((14*i, 26*i), 8*i, 18*i)

def draw_right_arm(i=1):
    fill(right_arm_color)
    rect((42*i, 26*i), 8*i, 18*i)

def draw_left_leg(i=1):
    fill(left_leg_color)
    rect((24*i, 48*i), 8*i, 12*i)
    
def draw_right_leg(i=1):
    fill(right_leg_color)
    rect((32*i, 48*i), 8*i, 12*i)

def draw_belt(i=1):
    fill(detail_color)
    rect((28*i, 40*i), 8*i, 4*i)

def draw_face(i=2):
    background(220)
    draw_head(i)
    draw_body(i)
    draw_left_arm(i)
    draw_right_arm(i)
    draw_left_leg(i)
    draw_right_leg(i)
    draw_belt(i)

def draw():
    draw_face()
    
run()
