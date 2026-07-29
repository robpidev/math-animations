from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    FadeOut,
    MathTex,
    Rectangle,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Tex,
    TransformFromCopy,
    TransformMatchingShapes,
    TransformMatchingTex,
    VGroup,
    Write,
    config,
)

#
# # ---------- Render maestro ----------
# config.pixel_width = 2160  # 4K vertical
# config.pixel_height = 3840
#
# # Sistema de coordenadas
# config.pixel_width = 2160
# config.pixel_height = 3840
#
# config.frame_width = 12
# config.frame_height = 21.333333  # mantiene la relación 9:16
# # config.frame_width = 9
# # config.frame_height = 16
# #
# ---------- Zona segura (YouTube 16:9) ----------


config.pixel_width = 2160
config.pixel_height = 2880  # 3:4

# ==========================
# Mundo de Manim
# ==========================

config.frame_width = 12
config.frame_height = 16  # Relación 3:

# ==========================
# Zona segura 16:9
# ==========================

SAFE_WIDTH = config.frame_width
SAFE_HEIGHT = SAFE_WIDTH * 9 / 16


class Exe(Scene):
    def create_safe_area(self):
        safe = Rectangle(
            width=SAFE_WIDTH,
            height=SAFE_HEIGHT,
            stroke_color=YELLOW,
            stroke_width=2,
        )
        safe.set_z_index(1000)
        return safe

    def construct(self) -> None:
        self.wait()

        # self.add(self.create_safe_area())
        # self.next_section(skip_animations=True)
        problem = r"""
        \parbox{8cm}{
            Dada una variable aleatoria continua $x$,
            con densidad de probabilidad:
            $$
            P(x) = A e^{-2x},\quad x > 0
            $$

            Hallar el valor de $A$ y la probablidad que $x > 1$.

                }
                """

        problem = Tex(problem, tex_environment="flushleft")
        self.play(Write(problem[0]), run_time=2)
        self.wait()

        self.play(problem.animate.to_edge(UP))
        self.wait()

        solution = (
            Tex("SOLUCIÓN.").next_to(problem, DOWN, aligned_edge=LEFT).shift(DOWN)
        )
        self.play(Write(solution))
        self.wait()

        vg = VGroup(problem, solution)

        # self.next_section(skip_animations=False)
        prob = MathTex(r"\int_{0}^{\infty}", "P(x)", "dx", "=1")
        prob.next_to(vg, DOWN)
        self.play(Write(prob))
        self.wait()

        eq = MathTex(r"\implies", r"\int_{0}^{\infty}", "A", "e^{-2x}", "dx", "=1")
        eq.next_to(prob, DOWN)

        self.play(Write(eq[0]))
        self.play(TransformFromCopy(prob[0], eq[1]))
        self.wait(0.2)
        self.play(TransformMatchingShapes(problem[0][65:70].copy(), eq[2:4]))
        self.wait()
        self.play(TransformMatchingShapes(prob[-2:].copy(), eq[-4:]))
        self.wait()

        # self.next_section(skip_animations=False)
        self.wait()

        eq1 = MathTex(
            r"\implies", "A", r"\int_{0}^{\infty}", "e^{-2x}", "dx", "=1"
        ).move_to(eq)

        self.play(TransformMatchingTex(eq, eq1))
        self.wait()

        self.play(
            ReplacementTransform(
                eq1,
                MathTex(
                    r"\implies",
                    r"A\lim_{b\to\infty}",
                    r"\int_{0}^{b}",
                    "e^{-2x}",
                    r"\, dx",
                    "=1",
                ).move_to(eq1),
            )
        )

        self.wait()

        # self.next_section(skip_animations=True)
        eq2 = MathTex(
            r"\implies",
            r"A\lim_{b\to\infty}",
            r"\left[",
            r"-\frac{1}{2}",
            "e^{-2x}",
            r"\right]_{0}^{b}",
            "=1",
        ).next_to(eq1, DOWN)

        self.play(Write(eq2[0]))
        self.play(TransformFromCopy(eq1[1], eq2[1]))
        self.wait(0.2)
        self.play(Write(eq2[2]))
        self.wait(0.2)
        self.play(TransformFromCopy(eq1[3][-3:-1], eq2[3]))
        self.wait()
        self.play(TransformMatchingShapes(eq1[3].copy(), eq2[4]))
        self.wait()
        # self.play(Write(eq2[5]), run_time=0.5)
        self.play(TransformFromCopy(eq1[2], eq2[5]))
        self.wait()
        self.play(TransformMatchingShapes(eq1[-1], eq2[-1]))
        self.wait()

        # self.next_section(skip_animations=False)

        eq3 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A\lim_{b\to\infty}",
            r"\left[",
            "e^{-2x}",
            r"\right]_{0}^{b}",
            "=1",
        ).move_to(eq2)

        self.play(
            TransformMatchingTex(
                eq2,
                eq3,
            )
        )
        self.wait()

        eq4 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A\lim_{b\to\infty}",
            r"\left[",
            r"e^{-2b}",
            r"-e^{0}"
            r"\right]",
            "=1",
        ).next_to(eq2, DOWN)

        self.play(TransformMatchingTex(eq3.copy(), eq4, transform_mismatches=True))
        self.wait()

        self.remove(eq4)
        eq4 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A",
            r"\lim_{b\to\infty}",
            r"\left[",
            r"e^{-2b}",
            r"-",
            r"e^{0}"
            r"\right]",
            "=1",
        ).move_to(eq4)

        self.add(eq4)

        eq5 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A",
            r"\left[",
            r"\lim_{b\to\infty}",
            r"e^{-2b}",
            r"-",
            r"e^{0}"
            r"\right]",
            "=1",
        ).move_to(eq4)

        self.play(TransformMatchingTex(eq4, eq5))

        self.remove(eq5)

        eq5 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A",
            r"\left[",
            r"\lim_{b\to\infty}e^{-2b}",
            r"-",
            r"e^{0}",
            r"\right]",
            "=1",
        ).move_to(eq5)

        self.add(eq5)

        eq6 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A",
            r"\left[",
            "0",
            "-",
            r"1",
            r"\right]",
            "=1",
        ).next_to(eq5, DOWN)

        self.play(TransformMatchingTex(eq5.copy(), eq6, transform_mismatches=True))

        eq7 = MathTex(
            r"\implies",
            r"-\frac{1}{2}",
            r"A",
            r"\left[",
            r"-1",
            r"\right]",
            "=1",
        ).next_to(eq6, DOWN)

        self.play(TransformMatchingTex(eq6.copy(), eq7))

        eq8 = MathTex(
            r"\implies",
            r"\frac{1}{2}",
            r"A",
            "=",
            "1",
        ).move_to(eq7)

        self.play(TransformMatchingTex(eq7, eq8))
        self.wait()

        eq9 = MathTex(r"\implies", "A", "=", "2").next_to(eq8, DOWN)
        self.play(TransformMatchingTex(eq8.copy(), eq9, transform_mismatches=True))
        self.wait()

        # self.next_section(skip_animations=False)
        rect = SurroundingRectangle(eq9[1:].copy(), corner_radius=0.1)
        self.play(Write(rect))

        a_value = MathTex("A", "=", "2").next_to(solution, RIGHT, buff=0.5)
        self.wait()
        self.play(FadeOut(*self.mobjects[5:-1]), ReplacementTransform(eq9[1:], a_value))
        self.remove(*self.mobjects)
        self.add(problem, solution, a_value)
        self.wait()

        # self.next_section(skip_animations=True)

        # self.next_section(skip_animations=False)
        self.wait()

        eq = MathTex("P(x>1)=", r"\int_1^{\infty}", "P(x)", "dx")
        eq.next_to(vg, DOWN)

        self.play(Write(eq))
        self.wait()

        eq1 = MathTex(r"\implies", "P(x>1)=", r"\int_1^{\infty}", "Ae^{-2x}", "dx")
        eq1.next_to(eq, DOWN)

        self.play(TransformMatchingTex(eq.copy(), eq1, transform_mismatches=True))
        self.wait()

        self.remove(eq1)
        eq1 = MathTex(
            r"\implies", "P(x>1)=", r"\int_1^{\infty}", "A", "e^{-2x}", "dx"
        ).move_to(eq1)
        self.add(eq1)

        eq2 = MathTex(
            r"\implies", "P(x>1)=", "A", r"\int_1^{\infty}", "e^{-2x}", "dx"
        ).move_to(eq1)

        self.play(TransformMatchingTex(eq1, eq2, transform_mismatches=True))
        self.wait()

        eq3 = MathTex(
            r"\implies",
            "P(x>1)=",
            "A",
            r"\lim_{b\to\infty}",
            r"\int_1^{b}",
            "e^{-2x}",
            r"dx",
        )

        self.play(TransformMatchingTex(eq2, eq3, transform_mismatches=True))
        self.wait()

        eq4 = MathTex(
            r"\implies",
            "P(x>1)=",
            "A",
            r"\lim_{b\to\infty}",
            r"\left[",
            r"-\frac{1}{2}",
            "e^{-2x}",
            r"\right]_{1}^{b}",
        ).next_to(eq3, DOWN)

        # self.next_section(skip_animations=False)

        self.play(TransformMatchingTex(eq3.copy(), eq4, transform_mismatches=True))
        self.wait()

        eq5 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"-\frac{1}{2}",
            "A",
            r"\lim_{b\to\infty}",
            r"\left[",
            "e^{-2x}",
            r"\right]_{1}^{b}",
        ).move_to(eq4)

        self.play(TransformMatchingTex(eq4, eq5, transform_mismatches=True))
        self.wait()

        eq6 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"-\frac{1}{2}",
            "A",
            r"\lim_{b\to\infty}",
            r"\left[",
            r"e^{-2b}",
            "-",
            "e^{-2}",
            r"\right]",
        ).next_to(eq5, DOWN)
        self.play(TransformMatchingTex(eq5.copy(), eq6, transform_mismatches=True))
        self.wait()

        eq7 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"-\frac{1}{2}",
            "A",
            r"\left[",
            r"\lim_{b\to\infty}",
            r"e^{-2b}",
            "-",
            "e^{-2}",
            r"\right]",
        ).next_to(eq6, DOWN)
        self.play(TransformMatchingTex(eq6.copy(), eq7, transform_mismatches=True))
        self.wait()

        eq8 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"-\frac{1}{2}",
            "A",
            r"\left[",
            r"0",
            "-",
            "e^{-2}",
            r"\right]",
        ).next_to(eq7, DOWN)
        self.play(TransformMatchingTex(eq7.copy(), eq8, transform_mismatches=True))
        self.wait()

        eq9 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"\frac{1}{2}",
            "A",
            "e^{-2}",
        ).next_to(eq8, DOWN)
        self.play(
            TransformMatchingTex(
                eq8.copy(),
                eq9,
            )
        )
        self.wait()

        eq10 = MathTex(
            r"\implies",
            "P(x>1)=",
            r"\frac{1}{2}",
            "2",
            "e^{-2}",
        ).move_to(eq9)

        self.play(TransformMatchingTex(eq9, eq10, transform_mismatches=False))
        self.wait()

        result = MathTex(
            r"\therefore",
            "P(x>1)=",
            "e^{-2}",
        ).move_to(eq10)

        self.play(
            TransformMatchingTex(
                eq10,
                result,
                # key_map={r"\implies": r"\therefore"},
            )
        )

        rect = SurroundingRectangle(result, corner_radius=0.1)
        self.play(Write(rect))
        self.wait()
