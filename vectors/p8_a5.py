from manim import *
from funcs.vec2D_tex import *
from mobj.mobjets import number_plane
from funcs.vec_algebra import *
from numpy import arctan


class Anim(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        self.wait()

        a5 = Tex("(A5). ",
                 r"$ \forall x \in \mathbb{R}, \exists -x \in \mathbb{R} :"
                 + r"x + (-x) = x$",)


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
        self.next_section(skip_animations=False)
        self.wait()
        self.play(r.animate.set_value(2), t.animate.set_value(160), run_time=2)
        self.play(r.animate.set_value(5), t.animate.set_value(200), run_time=2)
        self.play(r.animate.set_value(1), t.animate.set_value(300), run_time=2)
        self.play(r.animate.set_value(4), t.animate.set_value(490), run_time=2)




