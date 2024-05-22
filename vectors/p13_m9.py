from manim import *
from funcs.vec_algebra import vec_scale
from funcs.vec2D_tex import *


class Prop9(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        m3 = MathTex(
           r"\text{M3. }",
            "x(yz) = (xy)z",
           r", \quad \forall x, y, z \in \mathbb{R}"
        )

        self.play(Write(m3))
        self.wait()
        self.play(m3.animate.scale(0.8).to_edge(UP + LEFT))
        self.wait()

        plane = NumberPlane(
            background_line_style={
                "stroke_width": 2,
                "stroke_opacity": 0.4,
            },
            axis_config={
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
        )

        self.play(Create(plane))
        self.wait()

        a = [2, 1]

        u = Vector(a, color=YELLOW).set_z_index(13)
        ul = MathTex(r"\mathbf{u}", color=YELLOW).move_to(u, UP)

        self.play(Create(u), Write(ul))
        self.wait()

        u2 = Vector(vec_scale(2, a), color=GREEN).set_z_index(12)
        u2l = MathTex(r"2\mathbf{u}", color=GREEN).move_to([3, 2, 0])

        self.play(Create(u2), Write(u2l))
        self.wait()

        self.play(
            u2.animate.move_to([-4, -2, 0]),
            u2l.animate.move_to([-4.5, -1.5, 0])
        )

        self.wait()


        u3 = Vector(vec_scale(6, a), color=GREEN).set_z_index(11)
        u3.move_to(ORIGIN)
        u3l = MathTex(r"3(2\mathbf{u})", color=GREEN).move_to(u2l.get_center())

        self.play(TransformMatchingShapes(u2l, u3l))
        self.wait()



        self.play(ReplacementTransform(u2, u3), u3l.animate.move_to([-0.5, 0.5, 0]))
        self.wait()

        u3_alt = u3.copy().set_color(YELLOW).set_z_index(12)
        u3_altl = MathTex(r"6\mathbf{u}", color=YELLOW).move_to(ul.get_center())

        self.play(ReplacementTransform(ul, u3_altl))

        self.play(ReplacementTransform(u, u3_alt), Write(u3_altl))
        self.wait()

        eq = MathTex(
            r"3(2\mathbf{u})", "=",  r"6", r"\mathbf{u}",
        ).move_to([2, -1, 0])

        eq_alt = MathTex(
            r"3(2\mathbf{u})", "=", r"(3\cdot 2)", r"\mathbf{u}",
        ).move_to([2, -1, 0])

        self.play(TransformMatchingShapes(Group(u3l, u3_altl).copy(), eq))
        self.wait()

        self.play(ReplacementTransform(
            eq, eq_alt, transform_mismatches=True))
        self.wait()

        self.play(FadeOut(u3l, u3_altl, eq_alt, u3, u3_alt, plane))
        self.wait()


        #NOTE: ################ Prooff ######################

        l1 = MathTex(
            r"c, d",  r"\in \mathbb{R}",
            r"\wedge", r"\mathbf{u}",  r"\in \mathbb{R}^2", ","
        )

        l2 = MathTex(
            r"c(d\mathbf{u})",
            "=", r"c" + vec_comps("du"),
            "=", vec_matrix("c(du_x)", "c(du_y)"),
            "=", vec_comps("(cd)u"),
            "=", r"(cd) \mathbf{u}"
        )

        result = MathTex(
            r"\text{9. }",
            r"c(d \mathbf{u})",
            "=", r"(cd) \mathbf{u}",
            r",\quad ", r"\forall c, d \in \mathbb{R}",
            r"\wedge", r"\forall \mathbf{u} \in \mathbb{R}^2",
        )


        VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(l1))
        self.wait()

        self.play(TransformMatchingShapes(
            Group(l1[0], l1[-2]).copy(), l2[0],
            fade_transform_mismatches=True
        ))

        self.wait()
        self.play(Write(l2[1]))
        self.play(TransformMatchingShapes(
            l2[0].copy(), l2[2],
            transform_mismatches=True
        ))

        self.wait()
        self.play(Write(l2[3]))
        self.play(TransformMatchingShapes(
            l2[2].copy(), l2[4],
            transform_mismatches=True
        ))

        rect = SurroundingRectangle(m3)
        self.play(Create(rect))
        self.wait()
        self.play(Write(l2[5]))

        self.play(TransformMatchingShapes(
            l2[4].copy(), l2[6],
            transform_mismatches=True
        ))
        self.play(FadeOut(rect))
        self.wait()

        self.play(Write(l2[7]))
        self.play(TransformMatchingShapes(
            l2[6].copy(), l2[8],
            transform_mismatches=True
        ))
        self.wait()

        self.play(
            FadeOut(l2[2:-1]),
            TransformMatchingShapes(
                Group(l2[0:2], l2[-1]), result[1:4],
                transform_mismatches=True
            )
        )
        self.play(Write(result[4]))

        self.play(TransformMatchingShapes(
            l1, result[5:],
            transform_mismatches=True,
            path_arc=-PI/2
        ))
        
        self.wait()
        self.play(Write(result[0]))
        self.wait()

        self.play(result.animate.scale(0.8).to_edge(UP + LEFT),
                  FadeOut(m3))

        self.wait()

        #NOTE: ################ example #####################

        eq = MathTex(
            "3 (2\mathbf{u} + 5\mathbf{v})",
            "=", "(3\cdot2)", r"\mathbf{u}", "+", r"(3\cdot5)", "\mathbf{v}",
        )

        eq1 = MathTex(
            "3 (2\mathbf{u} + 5\mathbf{v})",
            "=", r"6" , r"\mathbf{u}", "+", "15", r"\mathbf{v}",
        )

        VGroup(eq, eq1).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(eq[0]))
        self.wait()
        self.play(Write(eq[1]))
        self.play(
            TransformMatchingShapes(
                eq[0].copy(), eq[2:],
                fade_transform_mismatches=True,
                path_arc = PI/2
            )
        )

        self.wait()
        self.play(TransformMatchingShapes(
            eq[1:].copy(), eq1[1:],
            transform_mismatches=True
        ))

        self.wait()

        # self.next_section(skip_animations=False)
        arrow = Arrow(
            eq1[3:].get_center(),
            eq[0][1:].get_center(), path_arc=-2.5 * PI/3,
            color=YELLOW,
            buff=0.4
        )

        self.play(Create(arrow))
