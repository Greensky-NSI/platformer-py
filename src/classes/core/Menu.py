"""importer tout les niveaux de la forme suivante:
from fichier import niveau as lvl_n
et n le numéro de niveau
penser à ajouter chaque niveau dans la dictionnaire niveaux tel que {'n':[lvl_n,False]} sauf pour lvl_1 avec {'1':[lvl_1,True]}"""
from p5 import *

from src.classes.environnement.Level import Level
from src.utils.toolbox import safe_fill, hitbox_collide
from src.utils.globals import env
from src.custom_types import *
from src.classes.core.DOM import DOM
from src.utils.niveaux import niveaux


class Button:
    def __init__(self, x, y, taille, num_lvl, action=None):
        self.x=x
        self.y=y
        self.s=taille
        self.a=action
        self.num=num_lvl
        self.hovered = False

    def draw_button(self):
        safe_fill((200 if self.is_mouse_over() else 255,) * 3)
        rect(self.x, self.y, self.s, -self.s)
        
        # Dessiner le texte
        safe_fill((0, 0, 0))
        text_align(CENTER, CENTER)
        text(str(self.num), self.x + self.s / 2, self.y - self.s / 2)

        self.handle_mouse()

    @property
    def hitbox(self):
        return self.x, self.y, self.x + self.s, self.y - self.s

    def is_mouse_over(self):
        return hitbox_collide(self.hitbox, (mouse_x, mouse_y, mouse_x, mouse_y))
    
    def handle_mouse(self):
        if self.is_mouse_over() and mouse_is_pressed:
            if self.num==1:
                self.a()
            elif niveaux[self.num-1][1] and self.a is not None:
                self.a()
        


class Menu:
    _dom: DOM
    def __init__(self, dom: DOM):
        self.buttons = []
        self._dom = dom

        self.creer_boutons()

    def set_dom(self, level: Level, number: int):
        self._dom.reload_from_level(level, number)

    def creer_boutons(self):
        for lvl in niveaux.keys():
            if int(lvl)<=6:
                self.buttons.append(Button(50+100*(int(lvl)-1), 125, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 6<int(lvl)<=12:
                self.buttons.append(Button(50+100*(int(lvl)-7), 225, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 12<int(lvl)<=18:
                self.buttons.append(Button(50+100*(int(lvl)-13), 325, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 18<int(lvl)<=24:
                self.buttons.append(Button(50+100*(int(lvl)-19), 425, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 24<int(lvl)<=30:
                self.buttons.append(Button(50+100*(int(lvl)-25), 525, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 30<int(lvl)<=36:
                self.buttons.append(Button(50+100*(int(lvl)-31), 625, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))
            elif 36<int(lvl)<=42:
                self.buttons.append(Button(50+100*(int(lvl)-37), 725, 50, int(lvl), lambda: self.set_dom(niveaux[lvl][0], lvl)))

    def display_menu(self):
        background(165)

        coef = 3
        scale(coef)
        safe_fill((127, 12, 98))

        text("Menu", (env.width - 2 * coef) // (coef * 2), coef * 3)

        scale(1 / coef)

        for button in self.buttons:
            button.draw_button()
