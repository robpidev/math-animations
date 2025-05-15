from manim import *
from moderngl_window.context import base

from mobj.mobjets import number_plane
from funcs.vec2D_tex import *


class P04_Base(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)
        title = Tex(r"Base en $\mathbb{R}^2$")
        title.scale(1.5)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        plane = number_plane()
        self.play(Create(plane))
        self.wait()

        # self.next_section(skip_animations=False)

        P = [4, 3, 0]
        rv = Vector(P, color=YELLOW)
        rt = MathTex(r"\mathbf{r}", "=", vec(["x", "y"]), color=YELLOW)
        rt.next_to(rv, LEFT)
        rt.shift(LEFT)

        rts = [
            rt,
            MathTex(
                r"\mathbf{r}", "=",
                vec(["x", "0"]), "+",
                vec(["0", "y"]),
            ).move_to(rt),
            MathTex(
                r"\mathbf{r}", "=",
                "x", vec([1, 0]), "+",
                "y", vec([0, 1]),
            ).move_to(rt),
            MathTex(
                r"\mathbf{r}", "=",
                "x", r"\mathbf{\hat{\imath}}", "+",
                "y", r"\mathbf{\hat{\jmath}}"
            ).move_to(rt)
        ]



        rts[1][2].set_color(RED)
        rts[1][4].set_color(GREEN)
        rts[2][2:4].set_color(RED)
        rts[2][5:].set_color(GREEN)
        rts[3][3].set_color(RED)
        rts[3][6].set_color(GREEN)




        rx = Vector([4, 0, 0], color=RED)
        ry = Arrow([4, 0, 0], [4, 3, 0], color=GREEN, buff=0)


        self.play(Create(rv), Write(rt))

        self.wait()
        self.play(TransformMatchingShapes(rts[0], rts[1]))
        self.wait()
        self.play(TransformFromCopy(rts[1][2], rx))
        self.play(TransformFromCopy(rts[1][4], ry))
        self.wait()
        self.play(TransformMatchingShapes(rts[1], rts[2]))
        self.wait()

        it = MathTex(r"\mathbf{\hat{\imath}}", "=", vec([1, 0]), color=RED)
        jt = MathTex(r"\mathbf{\hat{\jmath}}", "=", vec([0, 1]), color=GREEN)

        iv = Vector([1, 0, 0], color=RED)
        jv = Vector([0, 1, 0], color=GREEN)

        base = VGroup(it, jt).arrange(DOWN, buff=0.5)
        base.to_edge(LEFT+DOWN)


        self.next_section(skip_animations=False)
        self.play(
            rx.animate.set_opacity(0.2).set_color(WHITE),
            ry.animate.set_opacity(0.2).shift(4 * LEFT).set_color(WHITE),
        )

        self.wait()
        self.play(TransformMatchingShapes(
            rts[2][3].copy(), it
        ))
        self.play(TransformFromCopy(it, iv))

        self.wait()
        self.play(TransformMatchingShapes(
            rts[2][6].copy(), jt
        ))
        self.play(TransformFromCopy(jt, jv))

        self.wait()

        self.play(ReplacementTransform(rts[2], rts[3]))
        self.wait()

        self.play(FadeOut(rts[3], plane, rv, rx, ry, iv, jv))


        baseG = VGroup(
            Tex("Base de $\mathbb{R}^2$").scale(1.5),
            MathTex(r"\{\mathbf{\hat{\imath}}, \mathbf{\hat{\jmath}}\}")
        ).arrange(DOWN, buff=1.5)

        self.play(Write(baseG[0]))
        self.wait()
        self.play(ReplacementTransform(base, baseG[1]))
        self.wait()


