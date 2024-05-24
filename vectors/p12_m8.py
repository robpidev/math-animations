from manim import *
from funcs.vec_algebra import *
from funcs.vec2D_tex import *
from mobj.mobjets import number_plane

class Prop8(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        #NOTE: ########### background #########
        d = MathTex(
            r"\text{(D). }",
            "x(y + z)", "=", "xy + xz",
            r",\quad\forall x, y, z \in \mathbb{R}"
        ).scale(0.8).to_edge(UP + LEFT)

        self.add(d)
        self.wait()
        plane = number_plane() 
        self.play(Create(plane))
        self.wait()

        a = [2, 1]

        u = Vector(a, color=YELLOW)
        u2 = Vector(vec_scale(2, a), color=GREEN_B)
        u3 = Vector(vec_scale(3, a), color=GREEN_E)

        u.set_z_index(5)
        u2.set_z_index(4)
        u3.set_z_index(3)

        ul = MathTex(r"\mathbf{u}", color=YELLOW).move_to(u, UP)
        u2l = MathTex(r"2\mathbf{u}", color=GREEN_B).move_to([2.5, 2, 0])
        u3l = MathTex(r"3\mathbf{u}", color=GREEN_E).move_to([4.5, 3, 0])
        self.play(Create(u), Write(ul))
        self.wait()
        self.play(Create(u2), Write(u2l))
        self.wait()
        self.play(Create(u3), Write(u3l))
        self.wait()

        self.play(
            u2.animate.move_to([-2, -3, 0]),
            u2l.animate.move_to([-2.5, -2.5, 0])
        )

        self.play(
            u3.animate.move_to([3, -0.5, 0]),
            u3l.animate.move_to([2.4, -0.3, 0])
        )
        self.wait()

        r = Arrow([-4, -4, 0], [6, 1, 0], buff=0, color=RED).set_z_index(6)
        r.set_opacity(0.6)
        rl = MathTex(
            "3", r"\mathbf{u}",
            "=", r"2\mathbf{u} + 3\mathbf{u}",
            color=RED
        ).move_to([2.5, -2.5, 0])

        rl_alt = MathTex(
            "(2 + 3)", r"\mathbf{u}",
            "=", r"2\mathbf{u} + 3\mathbf{u}",
            color=RED
        ).move_to([2.5, -2.5, 0])



        self.play(
            TransformFromCopy(u, r),
            TransformMatchingShapes(ul.copy(), rl[0:2])
        )

        self.wait()
        self.play(
            TransformMatchingShapes(Group(u2l, u3l).copy(), rl[2:])
        )
        self.wait()

        self.play(Transform(rl, rl_alt))

        self.wait()
        
        self.play(FadeOut(u, ul, plane))

        fig = VGroup(u2, u3, u2l, u3l, r, rl)
        self.play(fig.animate.scale(0.5).to_edge(DOWN + RIGHT))
        self.wait()

        #NOTE: ############# Proof ################

        l1 = MathTex(
            r"c, d", "\in \mathbb{R}",
            r"\wedge" , r"\mathbf{u}", r"\in \mathbb{R}^2",","
        )

        l2 = MathTex(
            r"(c + d)", r"\mathbf{u}",
            r"=", vec_comps("(c+d)u"),
            r"=", vec_add_comps("cu", "du"),
        )

        l3 = MathTex(
            r"(c + d)\mathbf{u}", "=",
            vec_comps("cu"), "+", vec_comps("du"),
            "=", r"c\mathbf{u}", "+", r"d\mathbf{u}",
        )

        result = MathTex(
            r"\text{8. }",
            r"(c + d)", r"\mathbf{u}", "=",
            r"c\mathbf{u} + d\mathbf{u}",
            r", \quad", r"\forall", "c, d", r"\in \mathbb{R}",
            r"\wedge", r"\forall", "\mathbf{u}", r"\in \mathbb{R}^2"
        )

        VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT)

        m2 = MathTex(
            r"\text{(M2). }xy = yx, \quad\forall x, y \in \mathbb{R}"
        ).scale(0.8).to_edge(UP + LEFT).shift(0.5 * DOWN)

        d_alt = MathTex(
            r"\text{(D). }",
            "(y + z)x", "=", "yx + zx",
            r",\quad\forall x, y, z \in \mathbb{R}"
        ).scale(0.8).to_edge(UP + LEFT)


        self.play(Write(l1[0:2]))
        self.play(Write(l1[2:]))

        self.play(
            TransformFromCopy(l1[0], l2[0][1:-1]),
            FadeIn(l2[0][0], l2[0][-1]),
            TransformFromCopy(l1[3], l2[1])
        )

        self.wait()
        self.play(Write(l2[2]))
        self.play(TransformFromCopy(l2[0:2], l2[3]))
        self.wait()

        self.play(Write(m2))
        self.wait()

        self.play(TransformMatchingShapes(d, d_alt))
        self.play(FadeOut(d_alt[0], m2))
        self.wait()

        self.play(Write(l2[4]))
        self.play(TransformMatchingShapes(l2[3].copy(), l2[5]))
        self.wait()

        self.play(Write(l3[1]))

        self.play(
            TransformMatchingShapes(
                Group(l2[5][1:4], l2[5][8:11]).copy(), l3[2]
            ),
            TransformFromCopy(VGroup(l2[5][4], l2[5][11]), l3[3]),
            TransformMatchingShapes(
                Group(l2[5][5:8], l2[5][12:15]).copy(), l3[4]
            ),
        )

        self.wait()
        self.play(Write(l3[5]))
        self.play(
            TransformFromCopy(l3[2:5], l3[6:]),
        )
        self.wait()

        self.play(
            ReplacementTransform(l2[0:3], result[1:4]),
            ReplacementTransform(l3[-3:], result[4]),
            FadeOut(l2[3:], l3[1:-3])
        )
        self.play(Write(result[5]))
        self.play(
            TransformMatchingShapes(
                l1, result[6:],
                fade_transform_mismatches=True
            )
        )

        self.wait()
        self.play(Write(result[0]))

        self.play(
            result.animate.scale(0.8).to_edge(UP + LEFT),
            FadeOut(d_alt, fig)
        )
        self.wait()

        eq = MathTex(
            r"2\mathbf{u} + 4\mathbf{v} + 1\mathbf{u} + (-1\mathbf{v})",
            "=", r"(2 + 1)\mathbf{u} + (4 - 1)\mathbf{v}",
        )

        eq1 = MathTex(
            r"2\mathbf{u} + 4\mathbf{v} + 1\mathbf{u} + (-1\mathbf{v})",
            "=", r"3\mathbf{u} + 3\mathbf{v}",
            "=", r"3(\mathbf{u} + \mathbf{v})",
        )

        VGroup(eq, eq1).arrange(DOWN, aligned_edge=LEFT)

        self.play(Write(eq[0]))
        self.wait()
        self.play(Write(eq[1]))
        self.play(
            TransformMatchingShapes(
                eq[0].copy(), eq[2],
                transform_mismatches=True,
                path_arc=PI/2
            )
        )

        self.wait()
        self.play(Write(eq1[1]))
        self.play(
            TransformMatchingShapes(
                eq[2][:6].copy(), eq1[2][0:2],
                transform_mismatches=True,
            ),TransformFromCopy(eq[2][6], eq1[2][2]),
            TransformMatchingShapes(
                eq[2][7:].copy(), eq1[2][3:],
                transform_mismatches=True,
            )
        )

        self.wait()
        self.play(Write(eq1[3]))

        # self.next_section(skip_animations=False)
        self.play(
            Transform(
                Group(eq1[2][0], eq1[2][3]).copy(), eq1[4][0]
            ),
            TransformMatchingShapes(
                Group(eq1[2][1:3], eq1[2][-1]).copy(), eq1[4][1:],
                fade_transform_mismatches=True
            )
        )
        self.wait()

