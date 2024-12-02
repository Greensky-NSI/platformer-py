"""importer tout les niveaux de la forme suivante:
from fichier import niveau as lvl_n
et n le numéro de niveau
penser à ajouter chaque niveau dans la dictionnaire niveaux tel que {'n':[lvl_n,False]} sauf pour lvl_1 avec {'1':[lvl_1,False]}"""
from p5 import *

from src.utils.toolbox import safe_fill, hitbox_collide, safe_stroke
from src.utils.globals import env
from src.custom_types import *
from src.classes.core.DOM import DOM
from src.utils.niveaux import niveaux
from src.utils.variables import game_DOM


class Button:
    def __init__(self, x, y, taille, num_lvl):
        self.x=x
        self.y=y
        self.s=taille
        self.num=num_lvl
        self.hovered = False

    def draw_button(self):
        safe_stroke((0, 0, 0))
        safe_fill((200 if self.is_mouse_over() and self.previous_unlocked else 255,) * 3)
        rect(self.x, self.y, self.s, -self.s)
        
        # Dessiner le texte
        no_stroke()
        safe_fill((0, 0, 0))
        text_align(CENTER, CENTER)
        text(str(self.num), self.x + self.s / 2, self.y - self.s / 2)

        self.handle_mouse()

    def set_dom(self):
        game_DOM.reload_from_level(niveaux[str(self.num)][0], self.num)
    @property
    def previous_unlocked(self):
        if self.num == 1:
            return True
        return niveaux[str(self.num - 1)][1]
    @property
    def hitbox(self):
        return self.x, self.y, self.x + self.s, self.y - self.s

    def is_mouse_over(self):
        return hitbox_collide(self.hitbox, (mouse_x, mouse_y, mouse_x, mouse_y))
    
    def handle_mouse(self):
        if self.is_mouse_over() and mouse_is_pressed:
            if self.num==1:
                self.set_dom()
            elif self.num >= 2 and self.previous_unlocked:
                self.set_dom()



class Menu:
    _dom: DOM
    def __init__(self, dom: DOM):
        self.buttons = []
        self._dom = dom

        self.creer_boutons()

    def creer_boutons(self):
        for lvl in niveaux.keys():
            if int(lvl)<=6:
                self.buttons.append(Button(50+100*(int(lvl)-1), 125, 50, int(lvl)))
            elif 6<int(lvl)<=12:
                self.buttons.append(Button(50+100*(int(lvl)-7), 225, 50, int(lvl)))
            elif 12<int(lvl)<=18:
                self.buttons.append(Button(50+100*(int(lvl)-13), 325, 50, int(lvl)))
            elif 18<int(lvl)<=24:
                self.buttons.append(Button(50+100*(int(lvl)-19), 425, 50, int(lvl)))
            elif 24<int(lvl)<=30:
                self.buttons.append(Button(50+100*(int(lvl)-25), 525, 50, int(lvl)))
            elif 30<int(lvl)<=36:
                self.buttons.append(Button(50+100*(int(lvl)-31), 625, 50, int(lvl)))
            elif 36<int(lvl)<=42:
                self.buttons.append(Button(50+100*(int(lvl)-37), 725, 50, int(lvl)))

    def display_menu(self):
        background(165)

        coef = 3
        scale(coef)
        safe_fill((127, 12, 98))

        text("Menu", (env.width - 2 * coef) // (coef * 2), coef * 3)

        scale(1 / coef)

        for button in self.buttons:
            button.draw_button()
