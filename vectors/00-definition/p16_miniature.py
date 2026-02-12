from math import atan
from manim import *
from funcs.vec2D_tex import vec_comps, vec_scalar


class Miniature(Scene):
    def construct(self):
        plane = NumberPlane()

        u = Vector([2, 1], color=RED)
        v = u.copy().shift([-3, -1.5, 0])
        w = u.copy().shift([1, 0.5, 0])
        u = u.shift([-1, -0.5, 0])

        vl = MathTex("\mathbf{u}").move_to([-2, -1.5, 0]).set_color(RED)

        vecs = VGroup(u, v, w)

        b = Brace(vecs, direction=Vector([2, 1]).rotate(PI / 2).get_unit_vector())
        b = b.set_color(WHITE)

        bl = (
            b.get_tex(r"\mathbf{u + u + u} = 3 \mathbf{u}")
            .set_color(RED)
            .set_color(WHITE)
        )
        bl.shift(RIGHT * 1.2 + 0.1 * DOWN).rotate(atan(1 / 2.15))

        text = (
            MathTex(r"3\mathbf{u} = ", vec_comps("3u"))
            .move_to([1.3, -0.7, 0])
            .set_color(BLUE)
        )

        title = Tex(r"¿Vectores?").move_to([0, 3.5, 0])
        title.set_color(YELLOW).scale(3)

        image = VGroup(u, v, w, vl, bl, text, b).scale(1.5)
        image.move_to(ORIGIN)

        VGroup(image, title).move_to(ORIGIN)

        self.add(image, title)
        # self.wait()
