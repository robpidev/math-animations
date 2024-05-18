from manim import *

from mobj import mobjets
from funcs.vec2D_tex import *
from funcs.vec_algebra import *


class Def_Mult(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)

        a = [2, 1, 0]
        b = [4, 2, 0]
        c = [6, 3, 0]
        

        u1 = Vector(a, color=GREEN)
        u2 = Arrow(a, b, color=GREEN, buff=0)
        u3 = Arrow(b, c, color=GREEN, buff=0)
        u1l = MathTex(r"\mathbf{u}", color=GREEN).next_to(u1, DOWN)
        u2l = MathTex(r"\mathbf{u}", color=GREEN).next_to(u2, DOWN)
        u3l = MathTex(r"\mathbf{u}", color=GREEN).next_to(u3, DOWN)
        vecs = VGroup(u1, u2)

        br = Brace(
            vecs,
            direction=Line(a, b).rotate(90 * DEGREES).get_unit_vector(),
            color=YELLOW
        )
        br_lb = br.get_tex(r"\mathbf{u} + \mathbf{u}").set_color(YELLOW)
        br_l = br.get_tex(r"2\mathbf{u}").set_color(YELLOW)

        vecs.add(u3)
        
        br2 = Brace(
            vecs,
            direction=Line(a, c).rotate(90 * DEGREES).get_unit_vector(),
            color=YELLOW
        )
        br2_l = br2.get_tex(r"3\mathbf{u}").set_color(YELLOW)


        mg = Group(u1, u2, u3, u1l, u2l, u3l, br, br_l, br2, br2_l, br_lb)
        mg.move_to(ORIGIN)



        self.play(Create(u1), Write(u1l))
        self.play(Create(u2), Write(u2l))
        self.wait()
        self.play(Create(br))
        self.play(Write(br_lb))
        self.wait()
        self.play(ReplacementTransform(br_lb, br_l))
        self.wait()
        self.play(Create(u3), Write(u3l))
        self.wait()
        self.play(Transform(br, br2)
                  , Transform(br_l, br2_l))
        self.wait()
        self.play(FadeOut(mg[:-1]))


        plane = mobjets.number_plane()
        self.play(Create(plane))

        u1 = Vector(a, color=GREEN)
        u2 = Arrow(a, b, color=GREEN, buff=0)
        self.play(Create(u1))
        self.wait()

        eq = VGroup(
            MathTex(vec(a)).set_color(GREEN),
            MathTex("+"),
            MathTex(vec(a)).set_color(GREEN),
            MathTex("="),
            MathTex(vec(b)).set_color(RED),
        ).arrange(RIGHT).move_to([0, -2.5, 0])

        self.play(TransformFromCopy(u1, eq[0]))
        self.wait()
        self.play(Create(u2))
        self.play(Write(eq[1]))
        self.play(TransformFromCopy(u1, eq[2]))
        self.play(Write(eq[3]))
        self.play(TransformFromCopy(eq[:-2], eq[4]))
        self.wait()


        r = Vector(b, color=RED)

        self.play(TransformFromCopy(eq[-1], r))
        self.wait()

        eq2 = VGroup(
            MathTex(vec_add_int(a, a)).set_color(GREEN),
            MathTex("="),
            MathTex(vec(b)).set_color(RED),
        ).arrange(RIGHT).move_to([0, -2.5, 0])

        self.play(
            TransformMatchingShapes(eq[:3], eq2[0]),
            TransformMatchingShapes(eq[3], eq2[1]),
            TransformMatchingShapes(eq[4], eq2[2])
        )
        self.wait()
        
        eq3 = VGroup(
            MathTex(vec_matrix("2\cdot2", "2\cdot 1")).set_color(GREEN),
            MathTex("="),
            MathTex(vec(b)).set_color(RED),
        ).arrange(RIGHT).move_to([0, -2.5, 0])

        eq3[0][0][1].set_color(YELLOW)
        eq3[0][0][4].set_color(YELLOW)

        self.next_section(skip_animations=False)
        self.play(ReplacementTransform(eq2, eq3))
        self.wait()

        eq4 = VGroup(
            MathTex("2").set_color(YELLOW),
            MathTex(vec(a)).set_color(GREEN),
            MathTex("="),
            MathTex(vec(b)).set_color(RED),
        ).arrange(RIGHT).move_to([0, -2.5, 0])


        self.play(
            Transform(Group(eq3[0][0][1:3], eq3[0][0][4:6]), eq4[0]),
            TransformMatchingShapes(eq3[0][0][0], eq4[1][0][0]),
            TransformMatchingShapes(eq3[0][0][3], eq4[1][0][1]),
            TransformMatchingShapes(eq3[0][0][6], eq4[1][0][2]),
            TransformMatchingShapes(eq3[0][0][-1], eq4[1][0][-1]),
        )

        self.next_section(skip_animations=False)
        self.play(TransformFromCopy(eq3[-1], r))
        self.wait()

