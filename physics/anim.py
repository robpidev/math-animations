from manim import *


class Anim(Scene):
    def construct(self):
        self.wait()
        tex = MathTex(r"\theta'' + \frac{g}{l}\sin\theta = 0")
        tex.scale(4)
        self.play(Write(tex))
        self.wait()
