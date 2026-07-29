from funcs.vec2D_tex import *
from manim import *
from mobj.mobjets import number_plane


class Add2(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()
        a2 = Tex(r"(A2). $x + y = y + x, \forall x, y \in \mathbb{R}$")

        self.play(Write(a2))
        self.wait()
        self.play(a2.animate.scale(0.8).to_edge(UP + LEFT))

        plane = number_plane()

        self.play(Create(plane))
        self.wait()

        u = Vector([1, 3], color=GREEN)
        v = Vector([4, -2], color=BLUE)
        r = Vector([5, 1], color=RED)
        ul = MathTex(r"\mathbf{u}", color=GREEN).next_to(u, LEFT)
        vl = MathTex(r"\mathbf{v}", color=BLUE).move_to([2, -1.5, 0])
        rl = MathTex(r"\mathbf{u}", "+", r"\mathbf{v}", color=RED).move_to([3, 0, 0])

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))
        self.wait()

        self.play(v.animate.move_to([3, 2, 0]), vl.animate.move_to([3, 2.5, 0]))
        self.wait()
        self.play(Create(r))
        self.play(
            TransformFromCopy(ul, rl[0]),
            TransformFromCopy(vl, rl[2]),
            Write(rl[1]),
        )
        self.wait()

        eq1 = MathTex(
            vec([1, 3]),
            "+",
            vec([4, -2]),
            "=",
            vec_add_int([1, 3], [4, -2]),
            "=",
            vec([5, 1]),
        ).move_to([3.5, -3, 0])
        eq1[0].set_color(GREEN)
        eq1[2].set_color(BLUE)
        eq1[6].set_color(RED)

        eq1[4][1].set_color(GREEN)
        eq1[4][4].set_color(GREEN)
        eq1[4][3].set_color(BLUE)
        eq1[4][6:-1].set_color(BLUE)

        self.play(Write(eq1))
        self.wait()

        self.play(v.animate.move_to([2, -1, 0]), vl.animate.move_to([2, -1.5, 0]))
        self.wait()
        self.play(u.animate.move_to([4.5, -0.5, 0]), ul.animate.move_to([[5, -1, 0]]))
        self.wait()

        eq2 = MathTex(
            vec([4, -2]),
            "+",
            vec([1, 3]),
            "=",
            vec_add_int([4, -2], [1, 3]),
            "=",
            vec([5, 1]),
        ).move_to([3.5, -3, 0])

        eq2[0].set_color(BLUE)
        eq2[2].set_color(GREEN)
        eq2[6].set_color(RED)
        eq2[4][1].set_color(BLUE)
        eq2[4][4:6].set_color(BLUE)
        eq2[4][3].set_color(GREEN)
        eq2[4][-2].set_color(GREEN)

        self.play(
            eq1[0].animate.move_to(eq2[2].get_center()),
            eq1[2].animate.move_to(eq2[0].get_center()),
            eq1[1].animate.move_to(eq2[1].get_center()),
            TransformMatchingShapes(eq1[4], eq2[4]),
            eq1[3].animate.move_to(eq2[3].get_center()),
            eq1[5].animate.move_to(eq2[5].get_center()),
            eq1[6].animate.move_to(eq2[6].get_center()),
            run_time=1.5,
        )
        self.wait()

        self.clear()
        self.add(plane, u, v, r, ul, vl, rl, eq2, a2)

        u2 = Vector([1, 3], color=GREEN)
        v2 = Arrow([1, 3, 0], [5, 1, 0], color=BLUE, buff=0)
        r2 = Vector([5, 1], color=RED)
        u2l = MathTex(r"\mathbf{u}", color=GREEN).next_to(u2, LEFT)
        v2l = MathTex(r"\mathbf{v}", color=BLUE).move_to([3, 2.5, 0])
        r2l = MathTex(r"\mathbf{u}", "+", r"\mathbf{v}", color=RED).move_to([3, 0, 0])

        vecs1 = VGroup(u2, v2, r2, u2l, v2l, r2l)
        vecs2 = VGroup(u, v, r, ul, vl, rl)

        self.add(r2, r2l)
        self.play(Create(u2), Create(v2), Write(u2l), Write(v2l))

        self.play(
            vecs1.animate.scale(0.6).move_to([5, 1, 0]),
            vecs2.animate.scale(0.6).move_to([5.1, -1, 0]),
            FadeOut(rl, eq2, plane),
        )

        l1 = MathTex(
            r"\mathbf{u}",
            "+",
            r"\mathbf{v}",
            "=",
            vec_comps("u"),
            "+",
            vec_comps("v"),
            "=",
            vec_add_comps("u", "v"),
        )

        l2 = MathTex(
            r"\mathbf{u}+\mathbf{v}=",
            vec_add_comps("v", "u"),
            "=",
            vec_comps("v"),
            "+",
            vec_comps("u"),
        )

        l3 = MathTex(r"\mathbf{u}+\mathbf{v}", "=", r"\mathbf{v}", "+", r"\mathbf{u}")

        proof = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        proof.move_to([-2, 0, 0])

        self.play(Write(l1))
        self.wait()

        self.play(Write(l2[0][-1]), Write(l2[1][0]), Write(l2[1][-1]))
        sx = l1[-1][1:6].copy()
        self.play(sx.animate.move_to(l2[1][1:6].get_center()))
        self.wait()

        rec = SurroundingRectangle(a2, buff=0.1)
        self.play(Create(rec))
        self.play(TransformMatchingShapes(sx, l2[1][1:6]))
        self.wait()
        self.play(TransformFromCopy(l1[-1][6:11], l2[1][6:11]))
        self.play(FadeOut(rec))
        self.wait()

        self.play(Write(l2[2]), Write(l2[3][0]), Write(l2[3][-1]))
        self.play(
            TransformFromCopy(l2[1][1:3], l2[3][1:3]),
            TransformFromCopy(l2[1][6:8], l2[3][3:5]),
        )
        self.play(Write(l2[4]), Write(l2[5][0]), Write(l2[5][-1]))

        self.play(
            TransformFromCopy(l2[1][4:6], l2[5][1:3]),
            TransformFromCopy(l2[1][9:11], l2[5][3:5]),
        )
        self.wait()
        self.play(Write(l3[1]))
        self.play(TransformFromCopy(l2[-3], l3[2]))
        self.play(TransformFromCopy(l2[-2], l3[3]))
        self.play(TransformFromCopy(l2[-1], l3[-1]))

        result = MathTex(
            r"\text{2. }",
            r"\mathbf{u}+\mathbf{v}=",
            r"\mathbf{v}+\mathbf{u}",
            r",\quad \forall \mathbf{u}, \mathbf{v} \in \mathbb{R}^2",
        )

        result.move_to([-2, 0, 0])

        self.clear()
        self.add(vecs1, vecs2, a2, l1, l2[0][-1], l2[1:], l3[1:])
        self.remove(rl)

        # self.next_section(skip_animations=False)
        self.play(FadeOut(l1[4:], l2[0][-1], l2[1:], l3[1]))

        self.play(Transform(l1[0:4], result[1]), Transform(l3[2:], result[2]))

        self.play(Write(result[0]))
        self.wait()
        self.play(Write(result[-1]))
