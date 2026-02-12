from manim import *


class Intro(Scene):
    def construct(self):
        self.wait()

        # self.next_section(skip_animations=True)
        rect = Rectangle(width=2, height=1, color=BLUE).shift(UP * 0.5)
        m = MathTex(r"m = 10\text{ kg}").move_to([0, 0.5, 0]).scale(0.7)
        f = Vector([2, 0, 0], color=YELLOW).shift(RIGHT + UP * 0.5)
        fl = MathTex(r"\mathbf{F} = 50\mathbf{i} \text{ N}").scale(0.7)
        fl.next_to(f, UP)
        bloc = VGroup(rect, m, f, fl).shift(LEFT * 6)

        line = Line([-10, 0, 0], [10, 0, 0], color=RED)

        self.play(Write(line))
        self.play(Create(rect), Write(m))
        self.play(Create(f), Write(fl))
        self.wait()
        self.play(
            MoveAlongPath(
                bloc,
                Line([-5, 0.6, 0], [10, 0.6, 0]),
                rate_func=lambda t: t**2,
            ),
            run_time=2,
        )

        # self.next_section(skip_animations=False)
        n = Vector([0, 2, 0])
        nl = MathTex(r"\mathbf{n}").next_to(n, RIGHT)
        angle = Square(side_length=0.2).move_to([0.1, 0.1, 0])
        self.play(Create(n), Write(nl), Create(angle))
        self.wait()

        # self.add(number_plane())

        rect_g = VGroup(n, nl, angle, line)
        self.play(rect_g.animate.rotate(30 * DEGREES))

        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{mathrsfs}")

        eq = Tex(
            r"$\mathscr{L}: \mathbf{n} \cdot \overrightarrow{PX} = 0$",
            tex_template=template,
            font_size=72,
        ).move_to([3, -2.5, 0])

        p = Dot([-4, -2.47, 0])
        pl = MathTex(r"P = (x_0, y_0)").next_to(p, LEFT + 0.5 * UP)

        x = Dot([3, 1.57, 0])
        xl = MathTex(r"X = (x, y)").next_to(x, RIGHT * 1.5)

        self.play(Create(p), Create(x), Write(pl), Write(xl))

        # self.play(Write(eq))
        self.play(Write(eq))
        self.wait()
