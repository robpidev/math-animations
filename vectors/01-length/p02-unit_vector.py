from funcs.vec2D_tex import *
from manim import *
from mobj.mobjets import number_plane


def vut(name: str) -> str:
    return r"\mathbf{\hat{" + name + r"}}"


class P02_UnitVector(Scene):
    def construct(self):
        self.wait()
        title = Tex(r"Vector unitario $\mathbf{\hat{u}}$")
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # self.next_section(skip_animations=True)
        plane = number_plane()
        # self.play(Create(plane))

        l1 = MathTex(
            r"\mathbf{u_r}",
            "&=",
            r"\mathbf{\frac{r}{\|r\|}}",
            "=",
            r"\frac{1}{\|\mathbf{r}\|}\mathbf{r}",
        )

        l2 = MathTex(
            r"\implies",
            r"\mathbf{\|u_r\|}",
            "=",
            r"\left\|\frac{1}{\|\mathbf{r}\|}\mathbf{r}\right\|",
            "=",
            r"\frac{1}{\|\mathbf{r}\|}",
            r"\|\mathbf{r}\|}",
            "=",
            "1",
        )

        eq = VGroup(l1, l2)
        eq.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        for exp in l1[:4]:
            self.play(Write(exp))
            self.wait()

        self.play(
            TransformMatchingShapes(
                l1[2][0].copy(),
                VGroup(l1[-1][-1], l1[-1][0]),
                fade_transform_mismatches=True,
            ),
            TransformMatchingShapes(
                l1[2][1:].copy(),
                l1[-1][1:-1],
            ),
        )

        self.wait()

        self.play(Write(l2[0]))
        self.play(TransformMatchingShapes(l1[0].copy(), l2[1]))

        self.wait()
        self.play(Write(l2[2]))

        self.play(TransformMatchingShapes(l1[-1].copy(), l2[3]))

        self.wait()
        self.play(Write(l2[4]))

        self.play(TransformMatchingShapes(l2[3][4:9].copy(), l2[5]))

        self.wait()
        self.play(
            # ReplacementTransform(l2[3][9].copy(), l2[6][1:-1])
            TransformMatchingShapes(
                VGroup(l2[3][9:], l2[3][0:4]).copy(),
                l2[6],
                fade_transform_mismatches=True,
            )
        )

        self.wait()
        self.play(Write(l2[7]))

        self.play(ReplacementTransform(VGroup(l2[5], l2[6]).copy(), l2[8]))
        self.wait()

        # NOTE:=============== Name unit vector =================

        self.play(FadeOut(l2), l1.animate.scale(1.5).move_to(ORIGIN))

        l1_alt = MathTex(
            r"\mathbf{\hat r}",
            "&=",
            r"\mathbf{\frac{r}{\|r\|}}",
            "=",
            r"\frac{1}{\|\mathbf{r}\|}\mathbf{r}",
        ).scale(1.5)

        self.wait()

        self.play(TransformMatchingTex(l1, l1_alt, transform_mismatches=True))
        self.wait()

        eq = MathTex(
            r"\mathbf{\hat r}", "=", r"\frac{1}{\|\mathbf{r}\|}\mathbf{r}"
        ).scale(1.5)

        self.play(TransformMatchingTex(l1_alt, eq))
        self.wait()

        imp = MathTex(r"\implies")

        eq1 = MathTex(
            r"\|\mathbf{r}\|",
            r"\mathbf{\hat r}",
            "=",
            r"\|\mathbf{r}\|",
            r"\frac{1}{\|\mathbf{r}\|}\mathbf{r}",
        )

        eq2 = MathTex(r"\|\mathbf{r}\|", r"\mathbf{\hat r}", "=", r"\mathbf{r}")

        self.remove(eq)
        eq = MathTex(eq.get_tex_string())

        eqc = eq.copy().scale(1.5)

        eqs = VGroup(eq, imp.copy(), eq1, imp.copy(), eq2).arrange(RIGHT)

        # self.next_section(skip_animations=True)

        self.play(ReplacementTransform(eqc, eq))
        self.wait()

        self.play(Write(eqs[1]))

        self.play(
            TransformMatchingShapes(
                eq.copy(),
                eq1,
                fade_transform_mismatches=True,
                # transform_mismatches=True
            )
        )

        self.wait()
        self.play(Write(eqs[3]))
        self.play(TransformMatchingShapes(eq1.copy(), eq2))

        self.wait()

        mod_vec = MathTex(
            r"\mathbf{r}"
            "="
            r"\|\mathbf{r}\|",
            r"\mathbf{\hat r}",
        )
        result = VGroup(eq.copy(), MathTex(r"\iff"), mod_vec).arrange(RIGHT)

        self.play(
            ReplacementTransform(eqs[0], result[0]),
            ReplacementTransform(eqs[1:-1], result[1]),
            TransformMatchingShapes(eqs[-1], result[2]),
        )

        self.wait()

        # NOTE:============= Explain Unit Vec ================
        self.play(FadeOut(result[:-1]), mod_vec.animate.scale(1).to_edge(LEFT + UP))

        self.play(Create(plane))
        self.wait()

        # self.next_section(skip_animations=False)
        self.wait()

        up = [-2, -1, 0]
        ut = MathTex(r"\mathbf{u}", "=", vec(up), color=GREEN)
        uv = Vector(up, color=GREEN)
        ut.next_to(uv, LEFT)

        self.play(Write(ut))
        self.play(Create(uv))

        self.wait()

        uut = MathTex(
            r"\mathbf{\hat{u}}",
            "=",
            r"\frac{1}{\sqrt{(-2)^2 + (-1)^2}}",
            vec(up),
        ).next_to(uv, RIGHT)

        uu1 = MathTex(
            r"\mathbf{\hat{u}}",
            "=",
            r"\frac{1}{\sqrt{5}}",
            vec(up),
        ).move_to(uut)

        self.play(Write(uut[:-2]), Write(uut[-2][:4]))
        self.wait(0.5)
        self.play(TransformMatchingShapes(ut[-1].copy(), uut[-2][4:]))
        self.wait(0.5)
        self.play(TransformFromCopy(ut[-1], uut[-1]))
        self.wait(0.5)
        self.play(ReplacementTransform(uut, uu1, fade_transform_mismatches=False))

        self.wait()

        uup = [-2 / 5**0.5, -1 / 5**0.5, 0]
        uuv = Vector(uup).set_z_index(2)

        self.play(TransformFromCopy(uu1, uuv))
        self.wait()
        self.play(FadeOut(Group(ut, uv)))
        self.wait()

        # self.next_section(skip_animations=False)
        rt = MathTex(r"\mathbf{r}", "=", "4", r"\mathbf{\hat{r}}")
        rtc = MathTex(r"\mathbf{r}", "=", "4", r"\mathbf{\hat{u}}")
        rt.next_to(mod_vec, DOWN)
        rtc.move_to(rt)

        rvt = MathTex(
            r"\mathbf{r}",
            "=",
            r"\frac{4}{\sqrt{5}}",
            vec([-2, -1]),
            "=",
            vec([r"-8/\sqrt{5}", r"-4/\sqrt{5}"]),
        )
        rP = [-2 * 4 / 5**0.5, -1 * 4 / 5**0.5, 0]
        rv = Vector(rP, color=YELLOW)
        rvt.set_color(YELLOW).next_to(rv, DOWN)

        self.play(
            TransformMatchingShapes(mod_vec.copy(), rt, fade_transform_mismatches=False)
        )

        self.wait(0.5)

        self.play(Transform(rt, rtc))
        self.wait()

        self.play(Create(rv))
        self.wait()
        self.play(
            Transform(rt[:2].copy(), rvt[:2]),
            TransformMatchingShapes(rt[2].copy(), rvt[2][0]),
            TransformMatchingShapes(uut[2][1:].copy(), rvt[2][1:]),
            TransformFromCopy(uut[3], rvt[3]),
        )
        self.wait()
        self.play(Write(rvt[4]))
        self.play(TransformFromCopy(rvt[2:4], rvt[-1]))
        self.wait()

        self.clear()
        self.add(mod_vec, plane, uuv, uut, rt, rvt)
        self.wait()
