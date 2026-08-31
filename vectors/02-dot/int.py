from manim import (
    DOWN,
    GREEN,
    LEFT,
    PINK,
    RIGHT,
    UP,
    YELLOW,
    Arrow,
    Axes,
    Create,
    DashedLine,
    Dot,
    FadeOut,
    MathTex,
    Polygon,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Tex,
    Transform,
    TransformMatchingShapes,
    TransformMatchingTex,
    VGroup,
    Write,
    config,
)
from utils.panels import PanelLayout

config.frame_width = 9
config.frame_height = 16  # Re


class DotScene(Scene):
    def construct(self):
        layout = PanelLayout(4)
        borders = layout.show_borders()
        self.add(borders)
        self.wait()
        self.next_section(skip_animations=True)

        problem = r"""\parbox{8cm}{
La distribución de probababilidad $P(x, y)$ tiene la forma
$$P(x, y) = Dxy$$
para dos números aleatorios $x$ e $y$ en la región $x > 0$, $y > 0$ y $x + y < 1$,
donde $D$ es una constante, y $P(x, y) = 0$ fuera del rango.\\

(a) Cálcule el valor de $D$.\\
(b) Cuál es la probablidad de que $x < 1/2$.\\
(c) ¿$x$ e $y$ son independientes?\\
}"""

        problem_tex = Tex(problem, tex_environment="flushleft").scale(0.75)

        self.play(Write(problem_tex), run_time=5)
        self.wait()

        self.play(layout.animate_fit(problem_tex, index=0).shift(DOWN * 0.5))
        self.wait()

        solution = (
            Tex("SOLUCIÓN")
            .next_to(problem_tex, DOWN, aligned_edge=LEFT)
            .shift(DOWN * 0.5)
        )
        self.play(Write(solution))
        self.wait()

        # === Region drawing ===
        AXIS_COLOR = PINK
        REGION_COLOR = GREEN

        axes = Axes(
            x_range=[-0.1, 1.2, 1],
            y_range=[-0.1, 1.2, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "color": AXIS_COLOR,
                "include_ticks": True,
                "include_numbers": True,
            },
            tips=True,
        )

        x_label = axes.get_x_axis_label(MathTex("x", color=AXIS_COLOR))
        y_label = axes.get_y_axis_label(MathTex("y", color=AXIS_COLOR))

        # Región sombreada
        region = Polygon(
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            axes.c2p(1, 0),
            fill_color=REGION_COLOR,
            fill_opacity=0.4,
            stroke_width=0,
        )

        # Frontera y = 1 - x (punteada)
        boundary = DashedLine(
            axes.c2p(0, 1),
            axes.c2p(1, 0),
            color=REGION_COLOR,
            dash_length=0.12,
        )

        x_itercept = Dot(axes.c2p(1, 0), color=GREEN)
        y_itercept = Dot(axes.c2p(0, 1), color=GREEN)

        x_values = MathTex("x > 0")
        y_values = MathTex("y > 0")
        xy_values = MathTex("x + y < 1")

        graph = VGroup(axes, x_label, y_label, boundary, region, x_itercept, y_itercept)
        graph.next_to(solution, DOWN, aligned_edge=LEFT)
        self.play(Create(axes), Create(x_label), Create(y_label))

        eqs = VGroup(x_values, y_values, xy_values)
        eqs.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        eqs.next_to(boundary, RIGHT)

        self.play(Write(x_values))
        self.wait()
        self.play(Write(y_values))
        self.wait()
        self.play(Write(xy_values))

        # self.next_section(skip_animations=False)
        self.wait()
        self.play(
            Transform(xy_values, MathTex(r"x + y = 1", color=GREEN).move_to(xy_values))
        )

        self.wait()
        self.play(
            Transform(xy_values, MathTex(r"0 + y = 1", color=GREEN).move_to(xy_values))
        )

        self.wait(0.5)
        self.play(Create(y_itercept))
        self.wait(0.5)

        self.play(
            Transform(xy_values, MathTex(r"x + 0 = 1", color=GREEN).move_to(xy_values))
        )
        self.wait(0.5)
        self.play(Create(x_itercept))
        self.wait(0.5)
        self.play(
            Transform(xy_values, MathTex(r"x + y < 1", color=GREEN).move_to(xy_values))
        )

        self.play(Create(boundary))
        self.wait(0.5)
        self.play(Create(region))
        self.wait()

        r = MathTex(
            *r"R = \left\{ (x,y) | 0 < x < 1 \wedge 0 < y < 1 - x \right\}".split(" ")
        )
        r.next_to(graph, DOWN)

        # self.next_section(skip_animations=False)

        self.play(Write(r[0:5]), Write(r[-1]))
        self.wait()

        arrow = Arrow(axes.c2p(0, 0), axes.c2p(1, 0), color=YELLOW, buff=0)
        self.play(Create(arrow))
        self.wait()

        self.play(ReplacementTransform(arrow, r[5:10]))
        self.play(Write(r[10]))
        self.wait()

        arrow = Arrow(axes.c2p(0.5, 0), axes.c2p(0.5, 0.5), color=YELLOW, buff=0)
        self.play(Create(arrow))
        self.wait()

        self.play(ReplacementTransform(arrow, r[11:-1]))
        self.wait()

        self.play(
            FadeOut(graph, eqs), r.animate.next_to(solution, DOWN, aligned_edge=LEFT)
        )
        self.wait()

        # ==== Founding D ===

        # Cordinates transformation
        # self.next_section(skip_animations=False)
        definition = MathTex(*r"\iint_R P(x,y) \,dA = 1".split(" "))

        self.play(Write(definition))
        self.wait()

        eq = MathTex(*r"\iint_R D x y \,dA = 1".split(" "))
        eq.next_to(definition, DOWN, aligned_edge=LEFT)

        self.play(
            TransformMatchingShapes(definition.copy(), eq, transform_mismatches=True)
        )
        self.wait()

        eq_alt = MathTex(*r"D \iint_R x y \,dA = 1".split(" ")).move_to(eq)

        self.play(TransformMatchingShapes(eq, eq_alt))

        self.wait()

        eq1_limits = MathTex(*r"D \int \int x y  \,dA = 1".split(" "))
        eq1_limits.next_to(eq, DOWN)

        self.play(TransformMatchingShapes(eq_alt.copy(), eq1_limits))
        self.wait()

        eq1_xlim = MathTex(*r"D \int_0^1 \int x y  \,dA = 1".split(" "))
        eq1_xlim.move_to(eq1_limits)

        sr = SurroundingRectangle(r[5:10], corner_radius=0.2)
        self.play(Create(sr))
        self.wait()

        self.play(TransformMatchingShapes(eq1_limits, eq1_xlim))
        self.wait()

        self.play(Transform(sr, SurroundingRectangle(r[11:-1], corner_radius=0.2)))
        self.wait()

        eq1_ylim = MathTex(*r"D \int_0^1 \int_0^{1-x} x y  \,dA = 1".split(" "))
        eq1_ylim.move_to(eq1_xlim)
        self.play(TransformMatchingShapes(eq1_xlim, eq1_ylim))
        self.wait()

        eq1_dxdy = MathTex(*r"D \int_0^1 \int_0^{1-x} x y  \,dydx = 1".split(" "))
        eq1_dxdy.move_to(eq1_ylim)

        self.play(ReplacementTransform(eq1_ylim, eq1_dxdy))
        self.play(FadeOut(sr))
        self.wait()

        # Calc dy integral
        # self.next_section(skip_animations=False)
        eq2_xdy = MathTex(*r"D \int_0^1 x \int_0^{1-x} y  \, dy dx = 1".split(" "))
        eq2_xdy.next_to(eq1_dxdy, DOWN)
        self.play(
            TransformMatchingShapes(eq1_dxdy.copy(), eq2_xdy, transform_mismatches=True)
        )
        self.wait()

        eq2_limits = MathTex(
            *r"D \int_0^1 x \left[ \frac{1}{2} y^2 \right]_0^{1-x}  \, dx = 1".split(
                " "
            )
        ).next_to(eq2_xdy, DOWN)

        self.play(
            TransformMatchingTex(eq2_xdy.copy(), eq2_limits, transform_mismatches=True)
        )
        self.wait()

        eq2_eval = MathTex(
            *r" \frac{1}{2} D \int_0^1 x \left[  y^2 \right]_0^{1-x}  \, dx = 1".split(
                " "
            )
        ).move_to(eq2_limits)

        self.play(TransformMatchingTex(eq2_limits, eq2_eval, transform_mismatches=True))

        self.wait()

        eq2_yeval = MathTex(
            *r" \frac{1}{2} D \int_0^1 x \left[  (1 - x)^2 - 0^2 \right]  \, dx = 1".split(
                " "
            )
        ).move_to(eq2_eval)

        self.play(TransformMatchingTex(eq2_eval, eq2_yeval, transform_mismatches=True))
        self.wait()

        eq2_yevalued = MathTex(
            *r" \frac{1}{2} D \int_0^1 x \left[  (1 - x)^2 \right]  \, dx = 1".split(
                " "
            )
        ).move_to(eq2_yeval)

        self.play(
            TransformMatchingTex(eq2_yeval, eq2_yevalued, transform_mismatches=True)
        )
        self.wait()

        eq2_yevalued_equiv = MathTex(
            *r" \frac{1}{2} D \int_0^1 x \left[  (x - 1)^2 \right]  \, dx = 1".split(
                " "
            )
        ).move_to(eq2_yevalued)

        self.play(
            TransformMatchingTex(
                eq2_yevalued, eq2_yevalued_equiv, transform_mismatches=True
            )
        )
        self.wait()

        self.play(
            FadeOut(*self.mobjects[6:-4]),
            layout.animate_fit(eq2_yevalued_equiv, index=2).shift(3 * UP),
        )

        self.wait()

        eq2_xint = MathTex(
            *r" \frac{1}{2} D \int_0^1 x \left[  x^2 - 2x + 1 \right]  \, dx = 1".split(
                " "
            )
        ).next_to(eq2_yevalued_equiv, DOWN)

        self.play(
            TransformMatchingShapes(
                eq2_yevalued_equiv.copy(),
                eq2_xint,
                transform_mismatches=True,
            )
        )
        self.wait()

        eq2_dist = MathTex(
            *r"\frac{1}{2} D \int_0^1  \left[  x^3 - 2x^2 + x \right]  \, dx = 1".split(
                " "
            )
        ).next_to(eq2_xint, DOWN)

        self.play(TransformMatchingShapes(eq2_xint.copy(), eq2_dist))
        self.wait()

        eq3_integrated = MathTex(
            *r"\frac{1}{2} D \left[ \frac{1}{4} x^4 -\frac{2}{3} x^3 + \frac{1}{2} x^2 \right]_0^1 = 1".split(
                " "
            )
        ).next_to(eq2_dist, DOWN)

        self.play(
            TransformMatchingTex(
                eq2_dist.copy(),
                eq3_integrated,
                transform_mismatches=True,
            )
        )
        self.wait()

        eq4_valuation = MathTex(
            *r"\frac{1}{2} D \left[ \frac{1}{4} -\frac{2}{3} + \frac{1}{2} \right] = 1".split(
                " "
            )
        ).next_to(eq3_integrated, DOWN)

        # self.next_section(skip_animations=False)
        self.play(
            TransformMatchingTex(
                eq3_integrated.copy(),
                eq4_valuation,
                transform_mismatches=True,
            )
        )

        eq5 = MathTex(
            *r"\frac{1}{2} D \left[ \frac{7}{12} \right] = 1".split(" ")
        ).next_to(eq4_valuation, DOWN)

        self.play(
            TransformMatchingTex(
                eq4_valuation.copy(),
                eq5,
                transform_mismatches=True,
            )
        )
        self.wait()

        eq6 = MathTex(*r"\frac{7}{24} D = 1".split(" ")).move_to(eq5)
        self.play(
            TransformMatchingTex(
                eq5,
                eq6,
                transform_mismatches=True,
            )
        )
        self.wait()

        # self.next_section(skip_animations=False)

        d_value = MathTex(*r"D = \frac{24}{7}".split(" ")).move_to(eq6)
        self.play(
            TransformMatchingShapes(
                eq6,
                d_value,
            )
        )

        sr = SurroundingRectangle(d_value, corner_radius=0.2)
        self.play(Create(sr))
        self.wait()

        self.play(FadeOut(*self.mobjects[6:-1]))
        self.wait()

        # ==== Question B solution
        self.next_section(skip_animations=False)

        prob = MathTex(
            *r"P(x < 1/2) = \int_0^{1/2} \int_1^x D x y \, dy \, dx".split(" ")
        )
