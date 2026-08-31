from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Angle,
    Create,
    FadeOut,
    MathTex,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Text,
    Transform,
    TransformMatchingTex,
    Vector,
    VGroup,
    Write,
)
from utils.panels import PanelLayout


class P2Cos(Scene):
    def construct(self):

        self.next_section(skip_animations=True)
        layout = PanelLayout(2)
        borders = layout.show_borders()

        self.add(borders)

        self.wait()

        title = Text("Coseno entre dos vectores")

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # === Diagram ===
        # self.next_section(skip_animations=False)

        self.wait()
        u_c = [5, 1, 0]
        v_c = [2, 3, 0]
        u = Vector(u_c, color=BLUE)
        ul = MathTex(r"\mathbf{u}", color=BLUE).next_to(u, RIGHT).shift(UP * 0.5)

        # e1 = Vector(RIGHT, color=BLUE)
        # e2 = Vector(UP, color=BLUE)

        v = Vector(v_c, color=GREEN)
        vl = (
            MathTex(r"\mathbf{v}", color=GREEN)
            .move_to(v.point_from_proportion(0.5))
            .shift(v.copy().rotate(PI / 2).get_unit_vector() * 0.5)
        )

        a = Angle(u, v, radius=0.8)
        a_l = MathTex(r"\theta").move_to(
            Angle(u, v, radius=0.8 + 0.3).point_from_proportion(0.5)
        )

        # Equations

        graph = VGroup(u, ul, v, vl, a, a_l)

        graph.move_to(ORIGIN)

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))

        self.play(Create(a), Write(a_l))

        self.wait()

        self.play(graph.animate.shift(UP))
        self.wait()

        eq1 = MathTex(
            *r"\mathbf{u}\cdot\mathbf{v} = u v \cos\theta".split(" ")
        ).next_to(graph, 3 * DOWN)
        eq2 = MathTex(
            *r"\cos\theta = \frac{ \mathbf{u}\cdot\mathbf{v} }{ u v } ".split(" ")
        ).move_to(eq1)

        self.play(Write(eq1))
        self.wait()

        self.play(TransformMatchingTex(eq1, eq2), run_time=2)

        self.wait()

        rs = SurroundingRectangle(eq2, color=YELLOW, corner_radius=0.2)

        self.play(Create(rs))
        self.wait()

        graph.add(rs, eq2)
        self.wait()

        # === Ejemplo ===

        # self.next_section(skip_animations=False)

        um = MathTex(
            *r"""
                    \mathbf{u} = \begin{bmatrix}
                        5 \\ 1 
                    \end{bmatrix}
                    """.split(" "),
            color=BLUE,
        ).next_to(ul, UP + 1.5 * LEFT)
        vm = (
            MathTex(
                r"""
                    \mathbf{v} = \begin{bmatrix}
                        2 \\ 3
                    \end{bmatrix}
                    """,
                color=GREEN,
            )
            .move_to(vl)
            .shift(0.5 * UP + 0.5 * LEFT)
        )

        self.play(Transform(ul, um))
        self.wait()

        self.play(Transform(vl, vm))
        self.wait()

        graph.add(um, vm)
        self.play(layout.animate_fit(graph, index=0))
        self.wait()

        # === Length u ===
        # self.next_section(skip_animations=False)
        ulen = MathTex(*r"u = \sqrt{ 5^2 + 1^2 }".split(" "))
        layout.fit(ulen, index=1)
        ulen.shift(UP * 2.5)

        self.play(TransformMatchingTex(um.copy(), ulen, transform_mismatches=True))
        self.wait()

        ulen1 = MathTex(*r"u = \sqrt{ 25 + 1 }".split(" ")).next_to(
            ulen, DOWN, aligned_edge=LEFT
        )
        self.play(TransformMatchingTex(ulen.copy(), ulen1, transform_mismatches=True))
        self.wait()

        ulen2 = MathTex(*r"u = \sqrt{ 26 }".split(" ")).next_to(
            ulen1, DOWN, aligned_edge=LEFT
        )

        self.play(TransformMatchingTex(ulen1.copy(), ulen2, transform_mismatches=True))
        self.wait()

        # === Length v ===
        # self.next_section(skip_animations=False)
        vlen = MathTex(*r"v = \sqrt{ 2^2 + 3^2 }".split(" "))
        layout.fit(vlen, index=1)
        vlen.next_to(ulen2, DOWN, aligned_edge=LEFT).shift(DOWN)

        self.play(TransformMatchingTex(vm.copy(), vlen, transform_mismatches=True))
        self.wait()

        vlen1 = MathTex(*r"v = \sqrt{ 4 + 9 }".split(" ")).next_to(
            vlen, DOWN, aligned_edge=LEFT
        )

        self.play(
            ReplacementTransform(
                vlen.copy(),
                vlen1,
            )
        )

        vlen2 = MathTex(*r"v = \sqrt{ 13 }".split(" ")).next_to(
            vlen1, DOWN, aligned_edge=LEFT
        )

        self.play(ReplacementTransform(vlen1.copy(), vlen2))
        self.wait()

        uv_values = VGroup(ulen2, vlen2)

        self.play(
            uv_values.animate.arrange(RIGHT, buff=0.5),
            FadeOut(ulen, ulen1, vlen, vlen1),
        )

        self.wait()

        self.play(layout.animate_fit(uv_values, index=1).shift(UP * 3))
        self.wait()

        # === u dot v ===
        self.next_section(skip_animations=False)

        udotv = MathTex(
            *r"""
                        u \cdot v = 
                        \begin{bmatrix}
                            5 \\ 1
                        \end{bmatrix}
                            \cdot 
                        \begin{bmatrix}
                            2 \\ 3
                        \end{bmatrix}
            """
        )
