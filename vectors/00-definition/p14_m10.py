from manim import *


class Prop10(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)
        self.next_section(skip_animations=False)
        prop = MathTex(
            r"\text{10. }",
            r"1 \mathbf{u}",
            "=",
            r"\mathbf{u}",
            r", \quad \forall\mathbf{u} \in \mathbb{R}",
        )

        for mo in prop:
            self.play(Write(mo))

        self.wait()
        self.play(prop.animate.scale(0.8).to_edge(UP + LEFT))
        self.wait()

        eq = MathTex(
            r"3 \mathbf{u} + \mathbf{u}",
            "=",
            r"3 \mathbf{u} + 1\mathbf{u}",
            "=",
            r"4 \mathbf{u}",
        )

        self.play(Write(eq[0]))
        self.wait()
        self.play(Write(eq[1]))

        self.play(
            TransformMatchingShapes(eq[0].copy(), eq[2], transform_mismatches=True)
        )

        self.wait()
        self.play(Write(eq[3]))
        self.play(
            TransformMatchingShapes(eq[2].copy(), eq[4], transform_mismatches=True)
        )

        self.wait()
