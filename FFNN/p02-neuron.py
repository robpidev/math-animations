from manim import (
    BLUE,
    BLUE_A,
    DOWN,
    LEFT,
    RIGHT,
    YELLOW,
    UP,
    Arrow,
    Circle,
    Create,
    FadeOut,
    Line,
    MathTex,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Text,
    Transform,
    TransformFromCopy,
    TransformMatchingShapes,
    TransformMatchingTex,
    VGroup,
    Write,
    color,
    Vector,
    Group,
)


class P01Neuron(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)
        n1_draw = Circle(radius=0.6, color=BLUE)
        n1_bias = MathTex("b_1", color=BLUE).move_to(n1_draw)
        n1 = VGroup(n1_draw, n1_bias)

        input = VGroup(
            *[
                MathTex("a^{(0)}_" + str(i + 1), color=YELLOW).move_to(3 * i * DOWN)
                for i in range(-1, 2, 1)
            ]
        ).to_edge(LEFT)

        w1_conections = VGroup(*[Line(n, n1_draw, color=BLUE_A) for n in input])

        w1_labels = VGroup(
            *[
                MathTex(f"w_{i}", color=BLUE_A).move_to(w).shift(0.5 * UP)
                for i, w in enumerate(w1_conections)
            ]
        )

        w1 = VGroup(w1_conections, w1_labels)

        out_con = Line(n1_draw, 4 * RIGHT, color=BLUE_A)
        out_label = MathTex("a^{(1)}", color=BLUE_A).move_to(out_con).shift(0.5 * UP)

        out = VGroup(out_con, out_label)

        neuron = VGroup(input, w1, out, n1)

        # self.next_section(skip_animations=False)
        self.play(Create(n1_draw), Write(n1_bias))
        self.wait(0.5)

        for i in range(len(input)):
            self.play(Write(input[i]))
            self.wait(0.2)
            self.play(Create(w1_conections[i]))
            self.wait(0.2)
            self.play(Write(w1_labels[i]))
            self.wait(0.2)

        self.play(Create(out_con))
        self.wait(0.2)
        self.play(Write(out_label))
        self.wait(0.2)

        self.wait()

        # self.next_section(skip_animations=False)

        sq = SurroundingRectangle(input[0][0][1:4])
        self.play(Create(sq))

        self.play(Transform(sq, SurroundingRectangle(input[1][0][1:4])))
        self.play(Transform(sq, SurroundingRectangle(input[2][0][1:4])))

        self.wait()

        self.play(FadeOut(sq))

        eq = [
            "w_" + str(i // 2) + "a^{(0)}_" + str(i // 2) if i % 2 == 0 else "+"
            for i in range(2 * len(input))
        ]

        eq.append("b_1")

        eq = MathTex(
            *eq,
        ).to_edge(DOWN)

        # self.next_section(skip_animations=False)

        for i in range(len(input)):
            self.play(
                TransformMatchingShapes(Group(w1_labels[i], input[i]).copy(), eq[2 * i])
            )
            self.wait(0.2)

            if i + 1 == len(input):
                break

            self.play(Write(eq[2 * i + 1]))
            self.wait(0.2)

        self.next_section(skip_animations=False)
