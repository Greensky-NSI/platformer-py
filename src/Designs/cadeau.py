from p5 import translate, scale, rect, strokeWeight, ellipse
from src.utils.toolbox import safe_fill, safe_stroke
from src.utils.globals import variables_cadeau

def cadeau_ruban():
    safe_fill(variables_cadeau.couleurs.couleur_ruban)
    rect(variables_cadeau.size // 2 - variables_cadeau.epaisseur_ruban // 2, -variables_cadeau.size,
         variables_cadeau.epaisseur_ruban, variables_cadeau.size)  # Ruban vertical
    rect(0, -(variables_cadeau.size // 2 + variables_cadeau.epaisseur_ruban // 2), variables_cadeau.size,
         variables_cadeau.epaisseur_ruban)  # Ruban horizontal

def cadeau_noeud():
    safe_fill(variables_cadeau.couleurs.couleur_ruban)
    ellipse(variables_cadeau.size // 2 - variables_cadeau.size // 8, -variables_cadeau.size * 1.05,
            variables_cadeau.tailles_noeuds[0], variables_cadeau.tailles_noeuds[0])
    ellipse(variables_cadeau.size // 2 + variables_cadeau.size // 8, -variables_cadeau.size,
            variables_cadeau.tailles_noeuds[1], variables_cadeau.tailles_noeuds[1])

def cadeau_boite():
    safe_fill(variables_cadeau.couleurs.couleur_principale)
    rect(0, 0, variables_cadeau.size, -variables_cadeau.size)

def cadeau_dessin(x, y, t = 1):
    """
    Dessine un cadeau

    :param x: Coordonnée X du coin inférieur gauche
    :param y: Coordonnée Y du coin inférieur droit
    :param t: échelle
    :return: None
    """
    translate(x, y)
    scale(t)

    strokeWeight(2)
    safe_stroke((0, 0, 0))

    cadeau_noeud()
    cadeau_boite()
    cadeau_ruban()

    scale(1 / t)
    translate(-x, -y)
