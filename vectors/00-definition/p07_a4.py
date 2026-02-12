from manim import *
from funcs.vec2D_tex import *


class Add4(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()

        a4 = Tex(
            "(A4). ",
            r"$\exists 0 \in \mathbb{R} : x + 0 = x,"
            + r"\quad \forall x \in \mathbb{R}$",
        )
        self.play(Write(a4))

        self.wait()
        self.play(a4.animate.to_edge(UP + LEFT).scale(0.8))
        #
        # plane = NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.4,
        #     },
        #     axis_config={
        #         "stroke_width": 1,
        #         "stroke_opacity": 0.8,
        #     }
        # )
        #
        # self.add(plane)

        l1 = MathTex(
            r"\mathbf{0}",
            "=",
            vec_matrix(0, 0),
            ",\quad",
            r"\mathbf{0} \in \mathbb{R}^2",
        )
        l2 = MathTex(
            r"\mathbf{u}",
            "+",
            r"\mathbf{0}",
            "=",
            vec_comps("u"),
            "+",
            vec_matrix(0, 0),
            "=",
            vec_matrix("u_x + 0", "u_y + 0"),
            "=",
            vec_matrix("u_x", "u_y"),
            "=",
            r"\mathbf{u}",
        )

        proof = VGroup(l1, l2)
        proof.arrange(DOWN, buff=1)

        self.wait()
        self.play(Write(l1[0:3]))
        self.wait()
        self.play(Write(l1[3:]))
        self.wait()

        self.play(Write(l2[0:3]))
        self.play(Write(l2[3]))
        self.play(TransformFromCopy(l2[0], l2[4]))
        self.wait()
        self.play(TransformFromCopy(l2[1], l2[5]))
        self.play(TransformFromCopy(l2[2], l2[6]))
        self.wait()

        self.play(Write(l2[7]))
        self.play(TransformMatchingShapes(l2[4:7].copy(), l2[8]))
        self.wait()

        rect = SurroundingRectangle(a4)
        self.play(Create(rect))
        self.wait()
        self.play(Write(l2[9]))
        self.play(TransformFromCopy(l2[8].copy(), l2[10]))
        self.play(FadeOut(rect))
        self.play(Write(l2[11]))
        self.play(TransformFromCopy(l2[10], l2[12]))
        self.wait()

        result = MathTex(
            r"\exists",
            r"\mathbf{0} \in \mathbb{R}^2",
            ":",
            r"\mathbf{u} + \mathbf{0}",
            r"=\mathbf{u}",
            r",\quad \forall \mathbf{u} \in \mathbb{R}^2",
        )

        # self.next_section(skip_animations=False)
        self.play(FadeOut(l1[0:4], l2[3:-1]))
        self.play(
            Write(result[0]),
            Transform(l1[-1], result[1]),
            Write(result[2]),
            Transform(l2[0:3], result[3]),
            Transform(l2[-2:], result[4]),
        )
        self.wait()
        self.play(Write(result[5]))
        self.wait()

        enum = Tex("4. ").next_to(result, LEFT)
        self.play(Write(enum))
        self.wait()
