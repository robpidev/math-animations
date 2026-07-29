from manim import *
from mobj.mobjets import number_plane
from numpy import cos, sin


def vec(r: ValueTracker, u: ValueTracker) -> list:
    return [r.get_value() * cos(u.get_value()), r.get_value() * sin(u.get_value()), 0]


def vec_add(
    u: ValueTracker, v: ValueTracker, tu: ValueTracker, tv: ValueTracker
) -> list:
    return [
        u.get_value() * cos(tu.get_value()) + v.get_value() * cos(tv.get_value()),
        u.get_value() * sin(tu.get_value()) + v.get_value() * sin(tv.get_value()),
        0,
    ]


def Pvector(vec):
    x = vec[0]
    y = vec[1]
    return r"\begin{bmatrix}" + f"{x:.2f}" + r"\\" + f"{y:.2f}" + r"\end{bmatrix}"


def vec_tex(u):
    return r"\begin{bmatrix}" + f"{u}_x" + r"\\" + f"{u}_y" + r"\end{bmatrix}"


def vec_tex_add(u, v):
    return (
        r"\begin{bmatrix}"
        + f"{u}_x + {v}_x"
        + r"\\"
        + f"{u}_y + {v}_y"
        + r"\end{bmatrix}"
    )


class Add1(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        plane = number_plane()

        self.wait()
        a1_tex = Tex(
            "(A1). Si ", r"$ x, y \in \mathbb{R} \implies x + y \in \mathbb{R}$"
        )
        self.play(Write(a1_tex))
        self.wait()
        self.play(a1_tex.animate.scale(0.8).to_edge(UP + LEFT))
        self.wait()
        self.play(Create(plane))
        self.wait()

        u = ValueTracker(3.162277)
        v = ValueTracker(4.47)
        tu = ValueTracker(108.43 * PI / 180)
        tv = ValueTracker(-0.4636)

        vec_u = Vector(vec(u, tu), color=GREEN)
        vec_v = Vector(vec(v, tv), color=BLUE)
        lu = DashedLine([0, 0, 0], vec_u.get_end(), color=GREEN)
        lv = DashedLine([0, 0, 0], vec_v.get_end(), color=BLUE)
        vec_r = Vector(vec_add(u, v, tu, tv), color=RED)

        eq = (
            VGroup(
                MathTex(Pvector(vec(u, tu))).set_color(GREEN),
                MathTex("+"),
                MathTex(Pvector(vec(v, tv))).set_color(BLUE),
                MathTex("="),
                MathTex(Pvector(vec_add(u, v, tu, tv))).set_color(RED),
            )
            .arrange(RIGHT)
            .move_to([3.25, -3, 0])
        )

        eq[0].set_color(GREEN)
        eq[2].set_color(BLUE)
        eq[4].set_color(RED)

        self.play(Create(vec_u), Write(eq[0]))
        self.play(Create(vec_v), Write(eq[2]))
        self.play(Create(vec_r), Write(eq[4]))

        self.add(lu, lv)

        self.play(lu.animate.move_to([3.5, -0.5, 0]), Write(eq[1]))
        self.play(lv.animate.move_to([1, 2, 0]), Write(eq[3]))
        self.wait()

        vec_u.add_updater(lambda mob: mob.become(Vector(vec(u, tu), color=GREEN)))

        vec_v.add_updater(lambda mob: mob.become(Vector(vec(v, tv), color=BLUE)))

        vec_r.add_updater(
            lambda mob: mob.become(Vector(vec_add(u, v, tu, tv), color=RED))
        )

        lu.add_updater(
            lambda mob: mob.become(
                DashedLine(vec(v, tv), vec_add(u, v, tu, tv), color=GREEN)
            )
        )

        lv.add_updater(
            lambda mob: mob.become(
                DashedLine(vec(u, tu), vec_add(u, v, tu, tv), color=BLUE)
            )
        )

        self.add(eq)
        eq.add_updater(
            lambda mob: mob.become(
                VGroup(
                    MathTex(Pvector(vec(u, tu))).set_color(GREEN),
                    MathTex("+"),
                    MathTex(Pvector(vec(v, tv))).set_color(BLUE),
                    MathTex("="),
                    MathTex(Pvector(vec_add(u, v, tu, tv))).set_color(RED),
                )
                .arrange(RIGHT)
                .move_to([3.25, -3, 0])
            )
        )

        self.play(
            u.animate.set_value(1),
            tu.animate.set_value(2.5),
            v.animate.set_value(4),
            tv.animate.set_value(0.5),
            run_time=2,
        )

        self.play(
            u.animate.set_value(2),
            tu.animate.set_value(PI / 6),
            v.animate.set_value(2),
            tv.animate.set_value(PI),
            run_time=2,
        )

        self.play(
            u.animate.set_value(2),
            tu.animate.set_value(-PI / 4),
            v.animate.set_value(4),
            tv.animate.set_value(225 * PI / 180),
            run_time=2,
        )

        self.play(
            u.animate.set_value(3),
            tu.animate.set_value(0),
            v.animate.set_value(2),
            tv.animate.set_value(320 * PI / 180),
            run_time=2,
        )

        self.play(
            u.animate.set_value(4.5),
            tu.animate.set_value(0),
            v.animate.set_value(3),
            tv.animate.set_value(PI / 3),
            run_time=3.5,
        )

        self.wait()

        self.clear()
        self.add(a1_tex, plane)

        # self.add(eq, vec_v, vec_r, vec_u, a1_tex, lu, lv)
        vec_u = Vector(vec(u, tu), color=GREEN)
        vec_v = Vector(vec(v, tv), color=BLUE)
        vec_r = Vector(vec_add(u, v, tu, tv), color=RED)
        lu = DashedLine(vec(v, tv), vec_add(u, v, tu, tv), color=GREEN)
        lv = DashedLine(vec(u, tu), vec_add(u, v, tu, tv), color=RED)

        ut = MathTex(r"\mathbf{u}").move_to([0.5, 1.5, 0]).set_color(BLUE)
        vt = MathTex(r"\mathbf{v}").move_to([2.5, -0.5, 0]).set_color(GREEN)
        uvt = MathTex(r"\mathbf{u} + \mathbf{v}").move_to([3, 2, 0]).set_color(RED)

        vg = VGroup(ut, vt, uvt, vec_u, vec_r, vec_v, lu, lv)
        self.play(
            Write(ut),
            Write(vt),
            Write(uvt),
            FadeOut(plane, eq),
            vg.animate.scale(0.6).move_to([5, -3, 0]),
        )

        # self.next_section(skip_animations=False)
        add_tex = MathTex(
            r"\mathbf{u} + \mathbf{v} =" + vec_tex("u") + "+" + vec_tex("v") + "=",
            vec_tex_add("u", "v"),
            ",",
        )

        proof = VGroup(
            MathTex(
                r"\mathbf{u}, \mathbf{v} \in \mathbb{R}^2",
                r"\implies",
                r"u_x, u_y, v_x, v_y \in \mathbb{R},",
            ),
            add_tex,
            MathTex(
                r"u_x + v_x",
                r"\in \mathbb{R}",
                r"\wedge ",
                "u_y + v_y",
                r"\in \mathbb{R}",
            ),
            MathTex(r"\implies" + vec_tex_add("u", "v") + r"\in \mathbb{R}^2"),
            MathTex(r"\therefore", r"\mathbf{u} + \mathbf{v} \in \mathbb{R}^2"),
        ).arrange(DOWN)

        rect = SurroundingRectangle(a1_tex)

        self.play(Write(proof[0][0]))
        self.wait()
        self.play(Write(proof[0][1:]))
        self.wait()
        self.play(Write(proof[1]))
        self.wait()
        self.play(TransformFromCopy(add_tex[-2][1:6], proof[2][0]))
        self.play(Write(proof[2][1]), Create(rect))
        self.wait()
        self.play(Write(proof[2][2]), FadeOut(rect))
        self.play(TransformFromCopy(add_tex[-2][6:-1], proof[2][3]))
        self.play(Write(proof[2][4:]))
        self.wait()
        self.play(Write(proof[3]))
        self.wait()
        self.play(Write(proof[4]))
        self.wait()

        result = MathTex(
            r"\text{1. }",
            r"\mathbf{u}, \mathbf{v} \in \mathbb{R}^2 \implies",
            r"\mathbf{u} + \mathbf{v} \in \mathbb{R}^2",
        )

        self.play(FadeOut(proof[0][2], proof[1:-1], proof[-1][0]))
        self.play(
            proof[0][0:2].animate.move_to(result[1].get_center()),
            proof[-1][1].animate.move_to(result[2].get_center()),
        )
        self.play(Write(result[0]))
        self.wait()
