from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    ORIGIN,
    PI,
    RED,
    RIGHT,
    UP,
    YELLOW,
    Angle,
    Brace,
    Create,
    DashedLine,
    FadeOut,
    MathTex,
    NumberPlane,
    Scene,
    Square,
    SurroundingRectangle,
    Transform,
    TransformFromCopy,
    TransformMatchingTex,
    Vector,
    VGroup,
    Write,
)


def number_plane():
    return NumberPlane(
        x_range=[-10, 10],
        y_range=[-10, 10],
        background_line_style={
            "stroke_width": 2,
            "stroke_opacity": 0.3,
        },
        axis_config={
            "stroke_width": 1,
            "stroke_opacity": 0.5,
        },
    )


def add(u: list, v: list) -> list:
    return [x + y for x, y in zip(u, v)]


assert add([1, 2], [3, 4]) == [4, 6]


def scale(c: float, v: list) -> list:
    return [c * x for x in v]


assert scale(2, [1, 2]) == [2, 4]


def norm(v: list) -> float:
    return sum([x**2 for x in v]) ** 0.5


assert norm([3, 4]) == 5


def dot(u: list, v: list) -> float:
    return sum([x * y for x, y in zip(u, v)])


assert dot([1, 2], [3, 4]) == 11


def unit(v: list) -> list:
    return [x / norm(v) for x in v]


assert unit([3, 4]) == [3 / 5, 4 / 5]


def angleuv(u: list, v: list) -> float:
    return dot(u, v) / (norm(u) * norm(v))


def project(u: list, v: list) -> list:
    """Projection of u onto v"""
    return scale(dot(u, v) / dot(v, v), v)


assert project([3, 3], [1, 0]) == [3, 0]
assert project([3, 3], [0, 1]) == [0, 3]


class P1DotDef(Scene):
    def construct(self):
        u_c = [5, 1]
        v_c = [2, 3]
        u = Vector(u_c, color=BLUE)
        ul = MathTex(r"\mathbf{u}", color=BLUE).next_to(u, RIGHT).shift(UP * 0.5)

        e1 = Vector(RIGHT, color=BLUE)
        e2 = Vector(UP, color=BLUE)

        v = Vector(v_c, color=GREEN)
        vl = (
            MathTex(r"\mathbf{v}", color=GREEN)
            .move_to(v.point_from_proportion(0.5))
            .shift(v.copy().rotate(PI / 2).get_unit_vector() * 0.5)
        )

        p = Vector(project(v_c, u_c), color=RED)

        # Dashed line
        line = DashedLine(p, v.get_end(), color=YELLOW)

        # 90 degree square angle
        square = (
            Square(color=BLUE)
            .scale(0.4)
            .rotate(u.get_angle())
            .move_to(line.get_start())
            .shift(0.1 * (UP + LEFT))
            .scale(0.2)
        )

        a = Angle(u, v, radius=0.8)
        a_l = MathTex(r"\theta").move_to(
            Angle(u, v, radius=0.8 + 0.3).point_from_proportion(0.5)
        )

        objects = VGroup(
            e1.set_opacity(0),
            e2.set_opacity(0),
            u,
            ul,
            v,
            vl,
            a,
            p,
            a_l,
            line,
            square,
        )
        objects.move_to(ORIGIN)

        self.wait(0.5)
        self.next_section(skip_animations=True)

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))

        self.play(Create(a), Write(a_l))
        self.wait()

        self.play(Create(line), Create(square))
        self.wait()

        self.play(Create(p))

        self.next_section(skip_animations=True)

        brace = Brace(p, direction=p.copy().rotate(-PI / 2).get_unit_vector())
        self.play(Write(brace))
        brace_tex = brace.get_tex(r"v", r"\cos", r"\theta").set_color(RED)
        self.play(TransformFromCopy(v, brace_tex[0]))
        self.wait(0.5)
        self.play(Write(VGroup(brace_tex[1])))
        self.wait()
        self.play(TransformFromCopy(a_l, brace_tex[2]))
        self.wait()

        objects.add(brace, brace_tex)
        self.play(objects.animate.to_edge(UP))
        self.wait()

        self.next_section(skip_animations=True)

        dot_def = MathTex(
            r"\mathbf u", "\\cdot", r"\mathbf v", "=", "u", "v", "\\cos", "\\theta"
        ).shift(DOWN * 1.5)

        self.play(TransformFromCopy(u, dot_def[4]))
        self.wait(0.5)
        self.play(TransformFromCopy(brace_tex, dot_def[5:]))
        self.wait(0.5)
        self.play(TransformFromCopy(ul, dot_def[0]))
        self.wait(0.5)
        self.play(Write(dot_def[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(vl, dot_def[2]))
        self.play(Write(dot_def[3]))

        self.wait()

        self.play(
            FadeOut(p, brace, brace_tex),
            dot_def.animate.to_edge(UP).shift(1.5 * RIGHT + 0.8 * DOWN),
        )
        self.next_section(skip_animations=True)

        plane = number_plane().move_to(u.get_start())

        self.play(Create(plane))
        self.wait()

        alpha = Angle(e1, u, radius=0.5, color=BLUE)
        alpha_l = MathTex(r"\alpha", color=BLUE).next_to(
            Angle(e1, u, radius=0.5 + 0.3).point_from_proportion(0.5)
        )
        self.play(Write(alpha_l), Create(alpha))
        self.wait()

        beta = Angle(e1, v, radius=0.65).set_color(GREEN)
        beta_l = MathTex(r"\beta", color=GREEN).next_to(
            Angle(e1, v, radius=0.65 + 0.3).point_from_proportion(0.5)
        )

        self.play(Write(beta_l), Create(beta))
        self.wait()

        self.play(FadeOut(plane))

        self.next_section(skip_animations=False)

        dot_def_copy = dot_def.copy().move_to(ORIGIN)

        self.play(TransformFromCopy(dot_def, dot_def_copy))
        self.wait()

        dot_dif = MathTex(
            r"\mathbf u",
            r"\cdot",
            r"\mathbf v",
            "=",
            "u",
            "v",
            "\\cos",
            r"(\beta - \alpha)",
        ).shift(DOWN)

        self.play(TransformFromCopy(dot_def_copy, dot_dif))

        dot_dif11 = MathTex(
            r"\mathbf u",
            r"\cdot",
            r"\mathbf v",
            "=",
            "u",
            "v",
            r"\left[",
            r"\cos(\beta) \cos(\alpha) ",
            r"+",
            r"\sin(\beta) \sin(\alpha) ",
            r"\right]",
        ).next_to(dot_dif, DOWN)

        self.play(
            TransformMatchingTex(dot_dif.copy(), dot_dif11, transform_mismatches=True)
        )
        self.wait()

        dot_dif1 = MathTex(
            r"\mathbf u",
            "\\cdot",
            r"\mathbf v",
            "=",
            "u",
            "v",
            r"\cos(\beta) \cos(\alpha) ",
            "+",
            "u",
            "v",
            r"\sin(\beta) \sin(\alpha) ",
        ).next_to(dot_dif11, DOWN)

        self.play(TransformMatchingTex(dot_dif11.copy(), dot_dif1))
        self.wait()

        dot_dif2 = MathTex(
            r"\mathbf u",
            "\\cdot",
            r"\mathbf v",
            "=",
            "u",
            r"\cos(\beta)",
            "v",
            r"\cos(\alpha) ",
            "+",
            "u",
            r"\sin(\beta)",
            "v",
            r"\sin(\alpha) ",
        ).move_to(dot_dif1, DOWN)

        self.play(TransformMatchingTex(dot_dif1, dot_dif2, path_arc=PI / 2))
        self.wait()

        self.remove(dot_dif2)

        dot_dif2_alt = MathTex(
            *(
                r"\mathbf{u} \cdot \mathbf{v} = u\cos(\beta) v\cos(\alpha) + u\sin(\beta) v\sin(\alpha)".split(
                    " "
                )
            )
        ).move_to(dot_dif2)

        self.add(dot_dif2_alt)

        # Vectors in cordinates
        um = (
            MathTex(
                r"\mathbf{u}",
                "=",
                r"\begin{bmatrix} u \cos(\alpha) \\ u \sin(\alpha) \end{bmatrix}",
                color=BLUE,
            )
            .scale(0.5)
            .move_to(ul)
            .shift(RIGHT)
        )
        vm = (
            MathTex(
                r"\mathbf{v}",
                "=",
                r"\begin{bmatrix} v \cos(\beta) \\ v \sin(\beta) \end{bmatrix}",
                color=GREEN,
            )
            .scale(0.5)
            .next_to(
                v.point_from_proportion(0.5), v.copy().rotate(PI / 2).get_unit_vector()
            )
        )

        self.play(Transform(ul, um))
        self.wait()
        self.play(Transform(vl, vm))
        self.wait()

        dot_dif3 = MathTex(
            r"\mathbf u",
            "\\cdot",
            r"\mathbf v",
            "=",
            r"u_x",
            r"v_x",
            "+",
            r"u_y",
            r"v_y",
        ).next_to(dot_dif2, 2 * DOWN)

        self.play(TransformFromCopy(dot_dif2_alt[0:4], dot_dif3[0:4]))

        for t, s in zip(dot_dif2_alt[4:], dot_dif3[4:]):
            self.play(TransformFromCopy(t, s))
            self.wait(0.2)

        sr = SurroundingRectangle(dot_dif3, color=YELLOW)
        self.play(Create(sr))
