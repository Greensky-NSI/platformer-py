"""importer tout les niveaux de la forme suivante:
from fichier import niveau as lvl_n
et n le numéro de niveau
penser à ajouter chaque niveau dans la dictionnaire niveaux tel que {'n':[lvl_n,False]} sauf pour lvl_1 avec {'1':[lvl_1,True]}"""
from p5 import*
#from src.levels.one import level_one as lvl_1
from src.utils.variables import game_ticker, game_DOM
from src.utils.globals import env
lvl_1='kaka'
global niveaux
niveaux={'1':[lvl_1,True]}

class Button:
    def __init__(self,x,y,size,num_lvl,action=None):
        self.x=x
        self.y=-y
        self.s=size
        self.a=action
        self.num=num_lvl
        self.hovered = False

    def draw_button(self):
        fill(200 if self.hovered else 255)
        rect((self.x, self.y), self.s, self.s)
        
        # Dessiner le texte
        fill(0)
        text_align(CENTER, CENTER)
        text(self.num, (self.x + self.s / 2, self.y + self.s / 2))
        
    def is_mouse_over(self):
        return ((self.x <= mouse_x <= self.x + self.s) and
                (self.y >= mouse_y-600-self.s >= self.y - self.s))
    
    def handle_mouse(self):
        if self.is_mouse_over and mouse_is_pressed:
            if self.num==1:
                self.a()
            elif niveaux[self.num-1][1] and self.a is not None:
                self.a()
        


class Menu:
    def __init__(self):
        self.buttons=[]
        
    def creer_boutons(self):
        for lvl in niveaux.keys():
            if int(lvl)<=6:
                self.buttons.append(Button(50+100*(int(lvl)-1), env.height-25, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 6<int(lvl)<=12:
                self.buttons.append(Button(50+100*(int(lvl)-7), env.height-225, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 12<int(lvl)<=18:
                self.buttons.append(Button(50+100*(int(lvl)-13), env.height-325, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 18<int(lvl)<=24:
                self.buttons.append(Button(50+100*(int(lvl)-19), env.height-425, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 24<int(lvl)<=30:
                self.buttons.append(Button(50+100*(int(lvl)-25), env.height-525, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 30<int(lvl)<=36:
                self.buttons.append(Button(50+100*(int(lvl)-31), env.height-625, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))
            elif 36<int(lvl)<=42:
                self.buttons.append(Button(50+100*(int(lvl)-37), env.height-725, 50, lvl,lambda:game_DOM[int(lvl)-1].display()))

    def display_menu(self):
        translate(0,env.height)
        background(165)
        self.creer_boutons()
        for button in self.buttons:
            button.draw_button()
