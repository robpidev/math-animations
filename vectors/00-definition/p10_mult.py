from funcs.vec2D_tex import *
from funcs.vec_algebra import *
from manim import *
from mobj import mobjets


def vec_scalar_comps_color(k: ValueTracker, a: list) -> MathTex:
    tex = MathTex(
        f"{k.get_value():.2f}",
        vec(a),
        "=",
        vec_scalar_comps(f"{k.get_value():.2f}", a),
        "=",
        vec_matrix(f"{k.get_value() * a[0]:.2f}", f"{k.get_value() * a[1]:.2f}"),
    )

    tex[0].set_color("YELLOW")
    tex[1].set_color("GREEN")
    tex[3].set_color("GREEN")

    if k.get_value() >= 0:
        tex[3][1:5].set_color("YELLOW")
        tex[3][7:11].set_color("YELLOW")
    else:
        tex[3][1:6].set_color("YELLOW")
        tex[3][8:13].set_color("YELLOW")

    tex[5].set_color("RED")
    tex.move_to([0, -3, 0])

    return tex


def vec_scalar_name(k: ValueTracker, a: str) -> MathTex:
    tex = MathTex(f"{k.get_value():.2f}", r"\mathbf{" + a + "}")
    tex[0].set_color(YELLOW)
    tex[1].set_color(RED)
    return tex


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
            color=YELLOW,
        )
        br_lb = br.get_tex(r"\mathbf{u} + \mathbf{u}").set_color(YELLOW)
        br_l = br.get_tex(r"2\mathbf{u}").set_color(YELLOW)

        vecs.add(u3)

        br2 = Brace(
            vecs,
            direction=Line(a, c).rotate(90 * DEGREES).get_unit_vector(),
            color=YELLOW,
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
        self.play(Transform(br, br2), Transform(br_l, br2_l))
        self.wait()
        self.play(FadeOut(mg[:-1]))

        plane = mobjets.number_plane()
        self.play(Create(plane))

        u1 = Vector(a, color=GREEN)
        u2 = Arrow(a, b, color=GREEN, buff=0)
        self.play(Create(u1))
        self.wait()

        eq = (
            VGroup(
                MathTex(vec(a)).set_color(GREEN),
                MathTex("+"),
                MathTex(vec(a)).set_color(GREEN),
                MathTex("="),
                MathTex(vec(b)).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([0, -3, 0])
        )

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

        eq2 = (
            VGroup(
                MathTex(vec_add_int(a, a)).set_color(GREEN),
                MathTex("="),
                MathTex(vec(b)).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([0, -3, 0])
        )

        self.play(
            TransformMatchingShapes(eq[:3], eq2[0]),
            TransformMatchingShapes(eq[3], eq2[1]),
            TransformMatchingShapes(eq[4], eq2[2]),
        )
        self.wait()

        eq3 = (
            VGroup(
                MathTex(vec_matrix(r"2\cdot2", r"2\cdot 1")).set_color(GREEN),
                MathTex("="),
                MathTex(vec(b)).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([0, -3, 0])
        )

        eq3[0][0][1].set_color(YELLOW)
        eq3[0][0][4].set_color(YELLOW)

        self.play(ReplacementTransform(eq2, eq3))
        self.wait()

        eq4 = (
            VGroup(
                MathTex("2").set_color(YELLOW),
                MathTex(vec(a)).set_color(GREEN),
                MathTex("="),
                MathTex(vec(b)).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([0, -3, 0])
        )

        self.play(
            Transform(Group(eq3[0][0][1:3], eq3[0][0][4:6]), eq4[0]),
            TransformMatchingShapes(eq3[0][0][0], eq4[1][0][0]),
            TransformMatchingShapes(eq3[0][0][3], eq4[1][0][1]),
            TransformMatchingShapes(eq3[0][0][6], eq4[1][0][2]),
            TransformMatchingShapes(eq3[0][0][-1], eq4[1][0][-1]),
        )

        self.play(TransformFromCopy(eq3[-1], r))
        self.wait()

        self.play(FadeOut(u1, u2, r, eq3[-1], eq3[0][0][1], eq4[1:2], eq3[1], plane))
        self.wait()

        ######################################################
        ################# Def de product #####################
        ######################################################

        self.next_section(skip_animations=False)

        l1 = MathTex(
            r"\text{Def. }",
            r"\mathbf{u} \in \mathbb{R}^2",
            r"\wedge c \in \mathbb{R}",
            r",(c \text{ es llamado \textit{escalar}})",
        )
        l2 = Tex(
            "Se define el producto escalar:",
        )

        l3 = MathTex(
            r"c",
            r"\mathbf{u}",
            "=",
            "c",
            vec_comps("u"),
            "=",
            vec_scalar_var_comps("c", "u"),
            r"\in \mathbb{R}^2",
        )

        m1 = (
            MathTex(
                r"\quad (M1). \quad",
                r"x, y \in \mathbb{R} \implies x \cdot y \in \mathbb{R}",
            )
            .to_edge(UP + LEFT)
            .scale(0.8)
        )

        result = MathTex(
            r"6. \quad",
            r"\mathbf{u} \in \mathbb{R}^2",
            r"\wedge c \in \mathbb{R}",
            r"\implies",
            r"c \mathbf{u}",
            r"\in \mathbb{R}^2",
        )

        def_g = VGroup(VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT), l3, result)

        def_g.arrange(DOWN, buff=1)

        for m in l1:
            self.play(Write(m))
            self.wait()

        self.play(Write(l2))

        self.play(Write(l3[0:2]))
        self.play(Write(l3[2]))
        self.play(TransformFromCopy(l3[0], l3[3]))
        self.play(TransformFromCopy(l3[1], l3[4]))
        self.play(Write(l3[5]))
        self.play(TransformMatchingShapes(l3[3:5].copy(), l3[6]))

        self.wait()
        self.play(Write(m1))

        rec1 = SurroundingRectangle(l3[-2][1:5])
        self.play(Create(rec1))

        tex1 = MathTex(r"\in \mathbb{R}").next_to(rec1, UP)
        tex1.set_color(YELLOW)
        self.play(Write(tex1))
        self.wait()

        rec2 = SurroundingRectangle(l3[-2][5:9])
        self.play(Create(rec2))

        tex2 = MathTex(r"\in \mathbb{R}").next_to(rec2, DOWN)
        tex2.set_color(YELLOW)
        self.play(Write(tex2))
        self.wait()

        self.play(
            FadeOut(rec1, rec2), TransformMatchingShapes(Group(tex1, tex2), l3[-1])
        )
        self.wait()

        self.play(TransformFromCopy(l1[1:3], result[1:3]))
        self.play(Write(result[3]))
        self.play(TransformFromCopy(l3[0:2], result[4]))
        self.play(TransformFromCopy(l3[-1], result[5]))
        self.wait()

        self.play(Write(result[0]))

        self.wait()
        self.play(FadeOut(m1, def_g))

        self.next_section(skip_animations=True)
        #######################################################
        ################ More about scalars ##################
        #######################################################

        self.play(Create(plane))
        self.wait()

        k = ValueTracker(1)
        a = [3, 2, 0]

        u = Vector(a, color=GREEN)
        r = Vector(a, color=RED)

        ul = MathTex(r"\mathbf{u}").move_to(u.get_center() + 0.5 * UP)
        ul.set_color(GREEN)

        rl = MathTex("1", r"\mathbf{u}").move_to(r.get_center() + 0.7 * DOWN)
        rl[0].set_color(YELLOW)
        rl[1].set_color(RED)

        self.play(Create(u))
        self.play(Create(ul))

        math_scal = MathTex(vec_scalar_comps("1.00", a), color=GREEN)

        math_scal[0][1:5].set_color(YELLOW)
        math_scal[0][7:11].set_color(YELLOW)

        eq = (
            VGroup(
                MathTex("1.00").set_color(YELLOW),
                MathTex(vec(a)).set_color(GREEN),
                MathTex("="),
                math_scal,
                MathTex("="),
                MathTex(vec_float(a)).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([0, -3, 0])
        )

        self.play(Write(eq[0]))
        self.play(TransformFromCopy(u, eq[1]))
        self.play(TransformMatchingShapes(eq[0:2].copy(), eq[2:-1]))
        self.play(Create(r))
        self.play(Create(rl))
        self.play(ReplacementTransform(r, eq[-1]))
        # self.play(r.interpolate)
        self.wait()

        r = Vector(a, color=RED)
        self.remove(Group(u, r))
        self.add(r, u)
        self.wait()

        self.play(u.animate.set_opacity(0.5))

        eq.add_updater(lambda m: m.become(vec_scalar_comps_color(k, a)))

        rl.add_updater(
            lambda m: m.become(
                vec_scalar_name(k, "u").move_to(
                    Vector(vec_scale(k.get_value(), a)).get_center() + 0.7 * DOWN
                )
            )
        )

        r.add_updater(
            lambda m: m.become(Vector(vec_scale(k.get_value(), a), color=RED))
        )

        self.add(eq)

        # NOTE: ############ Scaling a vector #########################

        # self.next_section(skip_animations=False)

        self.play(k.animate.set_value(1.5))
        self.wait()
        self.play(k.animate.set_value(2))
        self.wait()
        self.play(k.animate.set_value(0.5))
        self.wait()

        # NOTE: ############### vec 0 as product #######################

        self.play(k.animate.set_value(0))
        self.wait()

        tex = MathTex(
            r"0 \mathbf{u}",
            r"=",
            vec_scalar_var_comps("0", "u"),
            r"=",
            vec(),
            r"=",
            r"\mathbf{0}",
        ).move_to([-3.5, 2, 0])

        for i in tex[:3]:
            self.play(Write(i))

        self.wait()
        self.play(Write(tex[3]))

        self.play(TransformFromCopy(tex[2], tex[4]))
        self.play(Write(tex[5]))
        self.play(TransformFromCopy(tex[4], tex[6]))
        self.wait()
        self.play(FadeOut(tex))
        self.wait()

        # NOTE:################ vec -u as product #############
        self.play(k.animate.set_value(-1))
        self.wait()

        tex = (
            MathTex(
                r"-1 \mathbf{u}",
                "=",
                vec_scalar_var_comps("-1", "u"),
                r"=",
                vec_comps("-u"),
                r"=",
                r"-\mathbf{u}",
            )
            .move_to([-3.5, 2, 0])
            .scale(0.9)
        )

        self.play(Write(tex[0]))
        self.play(Write(tex[1]))
        self.play(Write(tex[2]))
        self.wait()
        self.play(Write(tex[3]))
        self.play(TransformFromCopy(tex[2], tex[4]))
        self.play(Write(tex[5]))
        self.play(TransformFromCopy(tex[4], tex[6]))
        self.wait()
        self.play(FadeOut(tex))
        self.wait()
        self.play(k.animate.set_value(-2))
        self.wait()
        self.play(k.animate.set_value(-0.5))
        self.wait()
