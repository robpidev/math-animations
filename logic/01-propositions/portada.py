from manim import *


class Anim(Scene):
    def construct(self):
        # self.add(NumberPlane())

        t1 = Tex("Si ", r"$ax^2 + bx + c = 0$").move_to([-4, 1.5, 0])
        f = MathTex(r"\quad \Rightarrow", r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        f.move_to([-3, 0.2, 0])

        p = MathTex(r"p \Rightarrow q").move_to([-3.5, -2.5, 0]).scale(1.2)

        title = Text("¿Qué es una")
        title2 = Text("Proposición?").scale(1.2)

        vg = VGroup(title, title2).arrange(DOWN)
        vg.move_to([2.7, 0, 0]).scale(1.3)

        bc = Brace(t1[1], UP).set_color(PURPLE)
        bt = bc.get_tex("p").set_color(PURPLE)
        bc2 = Brace(f[1]).set_color(PINK)
        bt2 = bc2.get_tex("q").set_color(PINK)


        vg2 = VGroup(
                t1, f, p, bc, bt, bc2, bt2
                ).scale(0.8).move_to([-4, 0, 0])

        self.add(t1, f, bc, bt, bc2, bt2, p, vg)
        
