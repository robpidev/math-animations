from manim import (
    BLUE,
    BLUE_A,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    YELLOW,
    Axes,
    Brace,
    Circle,
    Create,
    FadeOut,
    Group,
    Line,
    MathTex,
    Scene,
    SurroundingRectangle,
    Transform,
    VGroup,
    Write,
)


class P01Example(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        self.wait()

        n1_biasv = 1.2
        n1_draw = Circle(radius=0.6, color=BLUE)
        n1_bias = MathTex(f"{n1_biasv}", color=BLUE).move_to(n1_draw)

        a1 = Line(n1_draw, RIGHT * 3, color=BLUE)
        a1_lab = MathTex("a_1", color=BLUE).move_to(a1).shift(UP * 0.5)

        base = VGroup(n1_draw, n1_bias, a1, a1_lab)

        a0v = [0.3, 0.2, 0.4]
        w1v = [0.2, 0.4, 0.9]

        a0 = VGroup(
            *[
                MathTex(f"{a0v[i + 1]}", color=YELLOW).move_to(3 * i * DOWN)
                for i in range(-1, 2, 1)
            ]
        ).to_edge(LEFT)

        w1_con = VGroup(*[Line(a, n1_draw, color=BLUE_A) for a in a0])

        w1_lab = VGroup(
            *[
                MathTex(f"{w1v[i]}", color=BLUE_A).move_to(w).shift(0.5 * UP)
                for i, w in enumerate(w1_con)
            ]
        )

        w1 = VGroup(w1_con, w1_lab)

        nn = VGroup(base, w1, a0)

        sq = SurroundingRectangle(a1)

        self.play(Create(n1_draw), Write(n1_bias))
        self.wait(0.5)

        for i in range(len(a0)):
            self.play(Write(a0[i]))
            self.wait(0.2)
            self.play(Write(w1_con[i]))
            self.wait(0.2)
            self.play(Write(w1_lab[i]))
            self.wait(0.2)

        self.play(Create(a1), Write(a1_lab))
        self.wait(0.5)

        self.play(Create(sq))
        self.wait()
        self.play(FadeOut(sq))

        # self.next_section(skip_animations=False)
        eq = [
            f"{w1v[i // 2]} \\cdot {a0v[i // 2]}" if i % 2 == 0 else "+"
            for i in range(2 * len(a0))
        ]

        eq.append(f"{n1_biasv}")

        eq = MathTex(*eq).to_edge(DOWN).shift(UP)

        for i in range(len(a0)):
            self.play(Transform(Group(a0[i], w1_lab[i]).copy(), eq[2 * i]))

            self.wait(0.2)

            if i + 1 == len(a0):
                break

            self.play(Write(eq[2 * i + 1]))
            self.wait(0.2)

        # self.next_section(skip_animations=False)

        result = sum([i * j for i, j in zip(a0v, w1v)])

        brace = Brace(eq[:-2], DOWN)
        brace_lab = MathTex(f"{result}").next_to(brace, DOWN)

        self.play(Create(brace), Write(brace_lab))
        self.wait()

        self.next_section(skip_animations=False)
        self.play(nn.animate.scale(0.5).to_edge(LEFT + UP))

        # DRAW Scalon function
        axes = Axes([-3, 3], [-1, 2], x_length=6, y_length=6, tips=True)
        axes.to_edge(UP)

        # f = lambda x: 1 if x > 0 else 0

        graph1 = axes.plot(lambda x: 1, x_range=[0, 3], color=BLUE)
        graph2 = axes.plot(lambda x: 0, x_range=[-3, 0], color=BLUE)

        self.play(Create(axes))
        self.wait()
        self.play(Create(graph1))
        self.wait()
        self.play(Create(graph2))
        self.wait()

        self.next_section(skip_animations=False)
        self.play(nn.animate.scale(0.5).to_edge(LEFT + UP))

        self.play(Create(axes))
        self.wait()
