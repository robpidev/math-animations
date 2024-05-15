from manim import *
from manim.mobject.logo import se
from funcs.vec2D_tex import *
from mobj.mobjets import number_plane
from funcs.vec_algebra import *
from numpy import arctan


class Anim(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()

        a5 = Tex("(A5). ",
                 r"$ \forall x \in \mathbb{R}, \exists -x \in \mathbb{R} :"
                 + r"x + (-x) = 0$",)


        self.play(Write(a5))
        self.wait()
        self.play(a5.animate.to_edge(UP + LEFT).scale(0.8))

        plane = number_plane()
        self.play(Create(plane))


        pu = [2, 3, 0]
        pv = [4, 2, 0]
        u = Vector(pu, color=GREEN)
        v = Arrow(pu, pv, buff=0, color=YELLOW)
        r = Vector(pv, color=RED)

        eq = VGroup(
            MathTex(vec_float(pu)), MathTex("+"),
            MathTex(vec_float(vec_ab(pu, pv))),
            MathTex("="), MathTex(vec_float(pv))
        ).arrange(RIGHT, buff=0.3).move_to([3.5, -2.5, 0])

        
        eq[0].set_color(GREEN)
        eq[2].set_color(YELLOW)
        eq[4].set_color(RED)

        self.play(Create(u))
        self.wait()
        self.play(TransformFromCopy(u, eq[0]))
        self.wait()
        self.play(Write(eq[1]))
        self.play(Create(v))
        self.play(TransformFromCopy(v, eq[2]))
        self.play(Write(eq[3]))
        self.play(Create(r))

        self.play(TransformFromCopy(r, eq[4]))


        x = ValueTracker(4)
        y = ValueTracker(2)

        v.add_updater(
            lambda m: m.become(
                Arrow(pu, [x.get_value(), y.get_value(), 0], color=YELLOW, buff=0)
            )
        )

        r.add_updater(
            lambda m: m.become(
                Vector([x.get_value(), y.get_value(), 0], color=RED)
            )
        )
        self.add(eq)

        eq.add_updater(
            lambda m: m.become(
                VGroup(
                    MathTex(vec_float(pu)).set_color(GREEN),
                    MathTex("+"),
                    MathTex(vec_float(vec_ab(pu, [x.get_value(), y.get_value(), 0]))).set_color(YELLOW),
                    MathTex("="),
                    MathTex(vec_float([x.get_value(), y.get_value(), 0])).set_color(RED)
                ).arrange(RIGHT, buff=0.3).move_to([3.5, -2.5, 0])
            )
        )

        self.wait()
        self.play(x.animate.set_value(3), y.animate.set_value(1))
        self.play(x.animate.set_value(0), y.animate.set_value(-2), run_time=2)
        self.play(x.animate.set_value(-2), y.animate.set_value(0), run_time=1.5)
        self.wait()
        self.play(x.animate.set_value(0), y.animate.set_value(0))
        self.play(v.animate.set_opacity(0.6))

        self.wait()

        u = Vector([2, 3, 0], color=GREEN)
        v = Arrow([2, 3, 0], [0, 0, 0], buff=0, color=YELLOW)

        r = ValueTracker((13)**0.5)
        t = ValueTracker(arctan(3/2) * 180 / PI)

        u.add_updater(
            lambda m: m.become(
                Vector(vec_mod_angled(r.get_value(), t.get_value()), color=GREEN)
            )
        )

        v.add_updater(
            lambda m: m.become(
                Arrow(
                    vec_mod_angled(r.get_value(), t.get_value()),
                    [0, 0, 0],
                    buff=0,
                    color=YELLOW,
                )
            )
        )

        eq.remove_updater(x).remove_updater(y)
        eq.add_updater(
            lambda m: m.become(
                VGroup(
                    MathTex(vec_float(vec_mod_angled(r.get_value(),
                                                     t.get_value()))).set_color(GREEN),
                    MathTex("+"),
                    MathTex(vec_float(vec_ab(vec_mod_angled(r.get_value(), t.get_value()),
                                             [0, 0, 0]))).set_color(YELLOW),
                    MathTex("="),
                    MathTex(vec_float([0, 0, 0])).set_color(RED)
                ).arrange(RIGHT, buff=0.3).move_to([3.5, -2.5, 0])
            )
        )


        self.clear()
        self.add(u, v, eq, plane, a5)
        self.wait()
        self.play(r.animate.set_value(2), t.animate.set_value(160), run_time=2)
        self.play(r.animate.set_value(5), t.animate.set_value(200), run_time=2)
        self.play(r.animate.set_value(1), t.animate.set_value(300), run_time=2)
        self.play(r.animate.set_value(4), t.animate.set_value(390), run_time=2)
        self.wait()


        self.remove(u, v)
        
        u = Vector(vec_mod_angled(4, 390), color=GREEN)
        v = Arrow(vec_mod_angled(4, 390), [0, 0, 0], buff=0, color=YELLOW)
        self.add(u, v)

        l1 = MathTex(
            r"\mathbf{u}", "=", vec_comps("u"),
            r",\quad \text{Def. }", r"-\mathbf{u}", "=", vec_comps("-u"), ","
        )

        l2 = MathTex(
            r"\mathbf{u}", "+", r"(\mathbf {-u})", "=",
            vec_comps("u"), "+", vec_comps("-u"),
            "=", vec_matrix("u_x + (-u_x)", "u_y + (-u_y)"),
            "=", vec_matrix("0", "0"),
            "=", "\mathbf{0}",
        )

        l3 = Tex(
            "Se acostumbra escribir: ",
            r"$\mathbf{u} + (-\mathbf{v}) = \mathbf{u} - \mathbf{v}$",
        )

        proof = VGroup(l1, l2, l3).arrange(DOWN, buff=0.5)

        self.play(Transform(u, l1[0]))
        self.play(Write(l1[1]))
        self.play(Write(l1[2]))
        self.wait()
        self.play(Write(l1[3]))
        self.play(Transform(v, l1[4]))
        self.play(Write(l1[5]))
        self.play(TransformMatchingShapes(l1[2].copy(), l1[6]))
        self.play(Write(l1[7]))

        self.remove(eq)

        eq = VGroup(
            MathTex(vec_float(vec_mod_angled(4, 390))).set_color(GREEN),
            MathTex("+"),
            MathTex(vec_float(vec_ab(vec_mod_angled(4, 390), [0, 0, 0]))).set_color(YELLOW),
            MathTex("="),
            MathTex(vec_float([0, 0, 0])).set_color(RED)
        ).arrange(RIGHT, buff=0.3).move_to([3.5, -2.5, 0])
        self.play(FadeOut(plane, eq))
        self.wait()

        self.play(
            TransformFromCopy(l1[0], l2[0]),
            Write(l2[1]),
            TransformMatchingShapes(l1[-4], l2[2]),
            )
        self.wait()
        self.play(Write(l2[3]))
        self.play(TransformFromCopy(l1[2], l2[4]))
        self.play(Write(l2[5]))
        self.play(TransformFromCopy(l1[-2], l2[6]))
        self.wait()
       
        self.play(Write(l2[7]))
        # self.play(Transform(l2[4:7].copy(), l2[8]))
        self.play(
            TransformFromCopy(l2[4][0], l2[8][0]),
            TransformFromCopy(l2[6][-1], l2[8][-1]),
            TransformMatchingShapes(
                Group(l2[4][1:3].copy(), l2[6][1:4].copy(), l2[5].copy()
            ), l2[8][1:9]),
            TransformMatchingShapes(
                Group(l2[4][3:5].copy(), l2[6][4:6].copy(), l2[5].copy()),
                l2[8][9:17]
            )
        )


        rect = SurroundingRectangle(a5)
        self.play(Create(rect))
        self.play(Write(l2[9]))
        self.play(
            TransformFromCopy(
                Group(l2[8][0], l2[8][-1]),
                 Group(l2[10][0], l2[10][-1])
            ),
            TransformFromCopy(
                Group(l2[8][1:9], l2[8][9:17]),
                Group(l2[10][1], l2[10][2])
            )
        )
        self.play(FadeOut(rect))
        self.play(Write(l2[11]))
        self.play(TransformFromCopy(l2[10], l2[12]))
        self.wait()

        self.play(Write(l3))
        self.wait()

        self.clear()
        self.add(a5, proof)

        result = MathTex(
            r"\forall \mathbf{u} = "+ vec_comps("u"), r"\in\mathbb{R}^2,\quad",
            r"\exists -\mathbf{u} ="+ vec_comps("-u") ,r"\in \mathbb{R}^2", ":",
        )

        result1 = MathTex(
            r"\mathbf{u} + (-\mathbf{u})", "=", r"\mathbf{0}"
        )

        resultg = VGroup(result, result1).arrange(RIGHT, buff=0.5).shift(UP)
        self.play(

            FadeOut(l1[3], l1[-1], l2[4:-1], l3),
        )

        self.play(
            TransformMatchingShapes(l1[0:3], result[0]),
            FadeIn(result[1]),
            # Write(result[1]), Write(result[-1]), Write(result[-2]),
            # TransformMatchingShapes(l2[:4], result1[:2], path_rc = PI/2),
        )

        self.play(
            TransformMatchingShapes(l1[4:7], result[2]),
            FadeIn(result[-2])
        )

        self.play(Write(result[-1]))
        self.wait()

        self.play(
            TransformMatchingShapes(l2[:4], result1[:2], path_rc = PI/2),
            Transform(l2[-1], result1[-1]),

        )
        self.wait()

        self.clear()
        self.add(a5, resultg)

        self.play(FadeOut(a5, resultg))

        # self.play(
            # Write(result[1]),
        # )

        eq = MathTex(
            r"\mathbf{u} - \mathbf{v}",
            "=", r"\mathbf{u}" ,"+",  "(-\mathbf{v})",
            "=", vec_comps("u"), "+", vec_comps("-v"),
            "=", vec_matrix("u_x + (-v_x)", "u_y + (-v_y)")
        )
        self.play(Write(eq[0:5]))
        self.play(Write(eq[5]))
        self.play(TransformFromCopy(eq[2], eq[6]))
        self.play(Write(eq[7]))
        self.play(TransformFromCopy(eq[4], eq[8]))
        self.wait()
        self.play(Write(eq[9]))
        self.play(TransformMatchingShapes(eq[6:9].copy(), eq[10]))
        self.wait()

        eq_aux = MathTex(
            vec_sub_comps("u", "v")
        ).move_to(eq[-1].get_center())

        self.play(TransformMatchingShapes(eq[10], eq_aux))
        self.wait()
        self.play(FadeOut(eq[2:-1]))


        eq_result = MathTex(
            r"\mathbf{u} - \mathbf{v}",
            "=", vec_comps("u"), "-", vec_comps("v"),
            "=", vec_sub_comps("u", "v")
        ) 

        self.play(
            TransformFromCopy(eq[0][0], eq_result[2]),
            TransformFromCopy(eq[0][1], eq_result[3]),
            TransformFromCopy(eq[0][2], eq_result[4])
        )
        self.play(Write(eq_result[-2]))
        self.play(
            Transform(eq[0:2], eq_result[0:2]),
            TransformMatchingShapes(eq_aux, eq_result[-1])
        )
        self.wait()
        self.clear()
        self.play(eq_result.animate.scale(0.8).to_edge(UP+LEFT))
        
        self.play(Create(plane))

        p = [4, 3, 0]
        q = [-2, 2, 0]
        u = Vector(p, color=GREEN)
        v = Vector(q, color=BLUE)
        v1 = Arrow(q, [0, 0, 0], buff=0, color=ORANGE)
        r = Arrow(q, p, buff=0, color=RED)



        ul = MathTex(r"\mathbf{u}", color=GREEN).move_to([2.5, 1.3, 0])
        vl = MathTex(r"\mathbf{v}", color=BLUE).move_to([-1.5, 0.5, 0])
        v1l = MathTex(r"\mathbf{-v}", color=ORANGE).move_to([-.5, 1.5, 0])
        rl = MathTex(
            r"\mathbf{u}","+", r"(-\mathbf{v})",
            color=RED
        ).move_to([0.5, 3, 0])

        rlc = MathTex(r"\mathbf{u}","-", r"\mathbf{v}",
                      color=RED).move_to([0.5, 3, 0])

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))

        eq = MathTex(
            r"\mathbf{u} - \mathbf{v}",
            r"=", r"\mathbf{u} + (", "-\mathbf{v}" ,")",
        ).move_to([0, -1.5, 0])

        self.play(Write(eq[0]))
        self.wait()
        self.play(Write(eq[1:]))
        self.wait()

        self.play(TransformFromCopy(eq[-2], v1))
        self.play(Write(v1l))

        self.wait()
        self.play(Create(r))
        self.play(
            TransformFromCopy(ul, rl[0]),
            Write(rl[1]),
            TransformMatchingShapes(v1l.copy(), rl[2])
        )
        self.wait()
        self.play(TransformMatchingShapes(rl, rlc))
        self.wait()
        self.play(FadeOut(eq, v1, v1l))

        self.wait()

        vG = Group(vl, v, rlc[1:])

        for _ in range(0, 5):
            self.play(vG.animate.set_color(YELLOW), run_time=0.4)
            self.play(vG.animate.set_color(BLUE), run_time=0.3)

        self.wait()

        uG = Group(u, ul, rlc[0])
        for _ in range(0, 5):
            self.play(uG.animate.set_color(YELLOW), run_time=0.4)
            self.play(uG.animate.set_color(GREEN), run_time=0.3)

        self.wait()

        # self.next_section(skip_animations=False)
        eq = MathTex(
            vec(p), "-", vec(q),
            "=", vec_sub_int(p, q),
            "=", vec_matrix("6", "1")
        ).move_to([0, -2, 0])
        eq[0].set_color(GREEN)
        eq[2].set_color(BLUE)
        eq[4].set_color(RED)
        eq[6].set_color(RED)

        self.play(TransformFromCopy(u, eq[0]))
        self.wait()
        self.play(Write(eq[1]))
        self.play(TransformFromCopy(v, eq[2]))
        self.wait()
        rect = SurroundingRectangle(eq_result)
        self.play(Create(rect))
        self.play(Write(eq[3]))
        self.play(TransformMatchingShapes(eq[:3].copy(), eq[4]))
        self.play(FadeOut(rect))
        self.wait()

        eq_aux = MathTex(vec_matrix("4 + 2", "3 - 2"))
        eq_aux.set_color(RED).move_to(eq[4].get_center())
        self.play(TransformMatchingShapes(eq[4], eq_aux))
        self.play(Write(eq[5]))
        self.play(TransformFromCopy(eq_aux, eq[6]))
        self.wait()
        self.play(TransformFromCopy(eq[6], r))
        self.wait()

