from manim import *


def delta(x, epsilon):
    if x < -epsilon:
        return 0
    elif x > epsilon:
        return 0
    else:
        return 1 / (2 * epsilon)


class Anim(Scene):
    def construct(self):
        self.wait()

        self.next_section(skip_animations=True)
        # axes with labels and numbers
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={
                # "include_numbers": True
            },
            x_length=8,
            y_length=6
        )

        axes.set_opacity(0.7)

        dtex = MathTex(r"""
            \delta_\epsilon(x) =
            \begin{cases}
                0 & x < -\epsilon \\
                \frac{1}{2\epsilon} & -\epsilon \leq x \leq \epsilon \\
                0 & x > \epsilon
            \end{cases}
        """)


        self.play(Write(dtex[0][:5]))
        self.wait(0.5)
        self.play(Write(dtex[0][5:11]))
        self.wait(0.5)
        self.play(Write(dtex[0][11]))
        self.wait(0.5)
        self.play(Write(dtex[0][12:16]))
        self.wait(0.5)
        self.play(Write(dtex[0][16:20]))
        self.wait(0.5)
        self.play(Write(dtex[0][20:26]))
        self.wait(0.5)
        self.play(Write(dtex[0][26]))
        self.wait(0.5)
        self.play(Write(dtex[0][27:]))
        self.wait()

        # self.next_section(skip_animations=False)
        self.play(dtex.animate.scale(0.8).to_edge(UP + LEFT))

        self.play(Create(axes))
        self.wait()

        self.next_section(skip_animations=False)

        eps = 1
        p1 = [-eps, 0, 0]
        p2 = [-eps, 1/(2 * eps), 0]
        p3 = [eps, 1/(2 * eps), 0]
        p4 = [eps, 0, 0]

        f = VGroup(
            Line(p2, p3).set_color(YELLOW).set_stroke(width=5),
            DashedLine(p1, p2).set_color(YELLOW).set_stroke(width=5),
            DashedLine(p4, p3).set_color(YELLOW).set_stroke(width=5),
            MathTex(r"-\epsilon").next_to(p1, DOWN),
            MathTex(r"\epsilon").next_to(p4, DOWN),
        )


        self.play(Create(f))
        self.wait()

