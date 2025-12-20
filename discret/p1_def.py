from manim import (
    DOWN,
    ORIGIN,
    RIGHT,
    UP,
    YELLOW,
    Create,
    FadeOut,
    MathTex,
    ReplacementTransform,
    Scene,
    Square,
    SurroundingRectangle,
    Text,
    Transform,
    TransformMatchingShapes,
    Vector,
    VGroup,
    Write,
)


class P1Def(Scene):
    def construct(self):
        # grid = NumberPlane().set_opacity(0.2)
        # self.add(grid)
        # self.next_section(skip_animations=True)

        self.wait()
        sq = Square().set_fill(YELLOW, 0)
        text = Text("1").scale(2)
        bite = Text("bit").scale(2).to_edge(UP)

        vg = VGroup(sq, text).arrange(DOWN, buff=0.5)

        self.play(Create(sq))
        self.wait()

        self.play(sq.animate.set_fill(opacity=1))
        self.wait()
        self.play(Create(text))
        self.wait()

        tex2 = Text("0").scale(2).move_to(text)

        self.play(sq.animate.set_fill(opacity=0), text.animate.become(tex2))

        self.wait()
        self.play(Write(bite))
        self.wait()

        byte = VGroup()
        for i in range(8):
            sq = Square().set_fill(YELLOW, 0).scale(0.5)
            text = Text("0")
            vg_aux = VGroup(sq, text).arrange(DOWN, buff=0.5)
            byte.add(vg_aux)

        byte.arrange(RIGHT, buff=0.5)

        byte0 = byte.copy()

        self.play(ReplacementTransform(vg, byte[0]))
        self.wait()
        self.play(Create(byte[1:]))
        self.wait()

        byte_label = Text("byte").scale(2).to_edge(UP)
        self.play(ReplacementTransform(bite, byte_label))
        self.wait()

        # self.next_section(skip_animations=False)

        bits_matrix = [
            [1, 0, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 1],
        ]

        for i in range(5):
            byte1 = VGroup()
            for j in range(8):
                bite = bits_matrix[i][j]
                sq = Square().set_fill(YELLOW, opacity=bite).scale(0.5)
                text = Text(str(bite))
                vg_aux = VGroup(sq, text).arrange(DOWN, buff=0.5)
                byte1.add(vg_aux)

            if i == 4:
                byte_aux = byte.copy()
            byte1.arrange(RIGHT, buff=0.5)
            self.play(Transform(byte, byte1))
            self.wait()

        # Elevar las potencias
        # self.next_section(skip_animations=False)
        arrows = VGroup()
        twos = VGroup()
        pows = VGroup()

        for i in range(8):
            arrow = Vector(DOWN).next_to(byte[i], DOWN)
            twos.add(MathTex(f"2^{7 - i}").next_to(arrow, DOWN).scale(1.5))
            pows.add(MathTex(f"{2 ** (7 - i)}").next_to(arrow, DOWN).scale(1.5))
            arrows.add(arrow)

        eq = MathTex("32", "+", "8", "+", "4", "+", "1")
        eq.scale(2)
        eq.next_to(twos, DOWN)
        eq.shift(0.5 * DOWN)

        objets = VGroup(byte.copy(), arrows, twos, pows, eq).move_to(ORIGIN)

        self.play(Transform(byte, objets[0]), FadeOut(byte_label))
        self.wait()

        for i in range(8):
            self.play(Create(arrows[i]))
            self.wait()
            self.play(Write(twos[i][0][0]))
            self.wait()
            rect = SurroundingRectangle(byte[i + 1 :])
            self.play(Create(rect))
            self.wait(0.5)
            self.play(ReplacementTransform(rect, twos[i][0][1]))
            self.wait()
            self.play(ReplacementTransform(twos[i], pows[i]))
            self.wait()

        # self.next_section(skip_animations=False)
        self.wait()

        self.play(
            TransformMatchingShapes(pows[2].copy(), eq[0]),
            ReplacementTransform(pows[4].copy(), eq[2]),
            ReplacementTransform(pows[5].copy(), eq[4]),
            ReplacementTransform(pows[7].copy(), eq[6]),
            Write(eq[1::2]),
        )
        # Animacion de binario a entero
        self.wait()

        result = MathTex("45").scale(2).move_to(eq.get_center())

        self.play(Transform(eq, result))
        self.wait()
        self.play(FadeOut(eq))
        self.wait()

        # Repetir la animacion de binario a entero
        # self.next_section(skip_animations=False)
        byte_aux.move_to(byte.get_center())
        self.play(Transform(byte, byte_aux))
        self.wait()

        eq = MathTex("128", "+", "32", "+", "16")
        eq.scale(2).next_to(twos, DOWN)
        eq.shift(0.5 * DOWN)

        self.play(
            TransformMatchingShapes(pows[0].copy(), eq[0]),
            TransformMatchingShapes(pows[2].copy(), eq[2]),
            TransformMatchingShapes(pows[3].copy(), eq[4]),
            Write(eq[1::2]),
        )
        self.wait()

        result = MathTex(f"{128 + 32 + 16}").scale(2)
        result.move_to(eq.get_center())

        self.play(Transform(eq, result))
        self.wait()
        self.play(FadeOut(eq))
        self.wait()

        # Numero entero a bynero
        # self.next_section(skip_animations=False)
        byte0.move_to(byte.get_center())
        self.play(Transform(byte, byte0))
        self.wait()

        number = MathTex("73").scale(2).move_to(result.get_center())
        self.play(Write(number))

        sum = MathTex("64", "+", "9").scale(2)
        sum.move_to(number.get_center())

        req = SurroundingRectangle(pows[1])
        self.play(Create(req))
        self.wait()

        self.play(ReplacementTransform(number, sum))
        self.wait()

        self.play(TransformMatchingShapes(sum[0], pows[1]), FadeOut(sum[1]))
        self.wait()

        self.play(
            byte[1][0].animate.set_fill(opacity=1),
            Transform(byte[1][1], Text("1").move_to(byte[1][1].get_center())),
        )
        self.wait()

        self.play(Transform(req, SurroundingRectangle(pows[4])))
        self.wait()

        sum1 = MathTex("8", "+", "1").scale(2)
        sum1.move_to(sum.get_center())

        self.play(ReplacementTransform(sum[-1], sum1))
        self.wait()

        self.play(ReplacementTransform(sum1[0], pows[4]), FadeOut(sum1[1]))
        self.wait()

        self.play(
            byte[4][0].animate.set_fill(opacity=1),
            Transform(byte[4][1], Text("1").move_to(byte[4][1].get_center())),
        )

        self.wait()

        self.next_section(skip_animations=False)
        self.play(
            Transform(req, SurroundingRectangle(pows[-1])),
        )
        self.wait()

        self.play(TransformMatchingShapes(sum1[-1], pows[-1]))
        self.wait()

        self.play(
            byte[-1][0].animate.set_fill(opacity=1),
            Transform(byte[-1][1], Text("1").move_to(byte[-1][1].get_center())),
        )

        self.wait()

        self.play(FadeOut(req))
        self.wait()
