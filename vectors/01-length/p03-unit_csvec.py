import numpy as np
from funcs.vec2D_tex import *
from funcs.vec_algebra import *
from manim import *
from mobj.mobjets import number_plane


class P03_UnitCsvec(Scene):
    def construct(self):
        self.wait()

        # self.next_section(skip_animations=True)
        title = Tex(r"Vector unitario $[\sin(\theta), \cos(\theta)]$")
        title.scale(1.5)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        num_plane = number_plane()
        self.play(Create(num_plane))
        self.wait()

        # self.next_section(skip_animations=False)

        t = ValueTracker(30)
        self.wait()

        r = 3.5
        rv = Vector(
            [r * np.cos(t.get_value()), r * np.sin(t.get_value()), 0], color=YELLOW
        )
        arc = Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, vec_angle(r, t.get_value())))
        ang = MathTex(r"\theta")
        ang.move_to(
            Angle(
                Line(ORIGIN, RIGHT),
                Line(ORIGIN, vec_angle(r, t.get_value())),
                radius=0.5 + 3 * SMALL_BUFF,
            ).point_from_proportion(0.5)
        )

        rv.add_updater(
            lambda m: m.become(
                Vector(
                    vec_angle(r, t.get_value()),
                    color=YELLOW,
                )
            )
        )

        arc.add_updater(
            lambda m: m.become(
                Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, vec_angle(r, t.get_value())))
            )
        )

        ang.add_updater(
            lambda m: m.move_to(
                Angle(
                    Line(ORIGIN, RIGHT),
                    Line(ORIGIN, vec_angle(r, t.get_value())),
                    radius=0.5 + 3 * SMALL_BUFF,
                ).point_from_proportion(0.5)
            )
        )

        self.play(Create(rv), Create(arc), Write(ang))
        self.wait()

        self.play(t.animate.set_value(330), run_time=2, rate_func=linear)
        self.wait(0.5)
        self.play(t.animate.set_value(50), run_time=2, rate_func=linear)
        self.wait()

        xline = DashedLine([0, 0, 0], xvec(r, t.get_value()), color=RED)
        yline = DashedLine(
            xvec(r, t.get_value()), vec_angle(r, t.get_value()), color=GREEN
        )

        self.play(Create(xline), Create(yline))

        self.wait()

        # NOTE: ============== Axis Lines ==================
        # self.next_section(skip_animations=False)

        rvt = MathTex("r", color=YELLOW).next_to(rv, LEFT)
        rvt.shift(0.5 * RIGHT)
        self.play(Write(rvt))
        self.wait()

        xl = MathTex("x", "=", r"r \cos(\theta)", color=RED)
        xl.next_to(xline, DOWN)

        yl = MathTex("y", "=", r"r \sin(\theta)", color=GREEN)
        yl.next_to(yline, RIGHT)

        self.play(Write(xl))
        self.wait()
        self.play(Write(yl))

        self.wait()

        rt = MathTex(
            r"\mathbf{r}",
            "=",
            vec([r"r\cos(\theta)", r"r\sin(\theta)"]),
        ).to_edge(LEFT + UP)
        rt.shift(1.5 * RIGHT)

        self.remove(rv)

        t.set_value(50)

        rv = Vector(vec_angle(r, t.get_value()), color=YELLOW)

        self.add(rv)

        self.play(TransformFromCopy(rv, rt[0]))

        self.wait()
        self.play(
            Write(rt[1]),
            TransformMatchingShapes(
                VGroup(xl[-1].copy(), yl[-1].copy()),
                rt[2],
            ),
        )
        self.wait()

        # NOTE: ============== Mod calcle ==================
        # self.next_section(skip_animations=False)

        rtc = MathTex(
            r"\mathbf{r}",
            "=",
            "r",
            vec([r"\cos(\theta)", r"\sin(\theta)"]),
        ).move_to(rt)

        self.play(TransformMatchingShapes(rt, rtc))

        rtmod = MathTex(
            r"\implies",
            r"\|\mathbf{r}\|",
            "=",
            r"r",
            r"\sqrt{\cos^2(\theta) + \sin^2(\theta)}",
        ).next_to(rtc, DOWN)

        rtmodc = MathTex(
            r"\implies",
            r"\|\mathbf{r}\|",
            "=",
            r"r",
            r"\sqrt{1}",
        ).next_to(rtmod, DOWN)

        rtmodc2 = MathTex(
            r"\implies",
            r"\|\mathbf{r}\|",
            "=",
            r"r",
        ).next_to(rtmodc, DOWN)

        rtmodG = VGroup(rtmod, rtmodc, rtmodc2)
        rtmodG.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        rtmodG.next_to(rtc, DOWN)

        self.play(TransformMatchingShapes(rtc.copy(), rtmod[1:]), Write(rtmod[0]))
        self.wait()
        self.play(ReplacementTransform(rtmod.copy(), rtmodc))
        self.wait()
        self.play(TransformMatchingTex(rtmodc.copy(), rtmodc2))
        self.wait()

        self.play(FadeOut(rtmodG[:-1]), rtmodc2.animate.next_to(rtc, DOWN))

        ur = MathTex(
            r"\mathbf{\hat{r}}",
            "=",
            r"\frac{1}{\|\mathbf{r}\|}",
            "r" + vec([r"\cos(\theta)", r"\sin(\theta)"]),
            "=",
            r"\frac{r}{r}",
            vec([r"\cos(\theta)", r"\sin(\theta)"]),
            "=",
            vec([r"\cos(\theta)", r"\sin(\theta)"]),
        )

        urs = [
            MathTex(
                r"\mathbf{\hat{r}}",
                "=",
                r"\frac{1}{\|\mathbf{r}\|}",
                "r" + vec([r"\cos(\theta)", r"\sin(\theta)"]),
            ),
            MathTex(
                r"\mathbf{\hat{r}}",
                "=",
                r"\frac{r}{r}",
                vec([r"\cos(\theta)", r"\sin(\theta)"]),
            ),
            MathTex(
                r"\mathbf{\hat{r}}",
                "=",
                vec([r"\cos(\theta)", r"\sin(\theta)"]),
            ),
        ]

        for ur in urs:
            ur.next_to(rtmodG, DOWN)

        self.next_section(skip_animations=False)

        self.play(Write(urs[0]))
        self.wait()
        self.play(TransformMatchingShapes(urs[0], urs[1]))
        self.wait()
        self.play(TransformMatchingShapes(urs[1], urs[2]))
        self.wait()
