from p5 import background, text, scale, text_align
from src.utils.globals import env
from src.utils.toolbox import safe_fill


def end_screen():
    background(128)

    def title():
        coef = 5
        coef_inverse = 1/coef

        safe_fill((255, 255, 255))
        scale(coef)

        text_align("CENTER")
        text("Victoire !", env.width // 2 * coef_inverse, env.height // 2.5 * coef_inverse)

        scale(coef_inverse)
    def content():
        coef = 2.5
        coef_inverse = 1/coef

        safe_fill((210, 150, 140))

        scale(coef)

        text_align("CENTER")
        text("Vous avez terminé le niveau !", env.width // 2 * coef_inverse, env.height // 2 * coef_inverse)

        scale(coef_inverse)

    title()
    content()