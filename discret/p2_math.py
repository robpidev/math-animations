from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    PINK,
    RED,
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
    TransformFromCopy,
    TransformMatchingShapes,
    Vector,
    VGroup,
    Write,
)


def create_byte(byte_text: str):
    """
    Return byte, bins, arrows, pows, 2^pow
    """
    byte_text = byte_text.replace(" ", "")
    byte = VGroup()
    bins = VGroup()
    arrows = VGroup()
    pows = VGroup()
    two_pows = VGroup()

    for b in byte_text:
        byte.add(Square().scale(0.5).set_fill(YELLOW, 1 if b == "1" else 0))

    byte.arrange(RIGHT, buff=0.5)

    for i, c in enumerate(byte_text):
        bins.add(Text(c).next_to(byte[i], DOWN))
        arrows.add(Vector(DOWN).next_to(bins[i], DOWN))
        two_pows.add(MathTex(f"2^{7 - i}").next_to(arrows[i], DOWN))
        pows.add(MathTex(f"{2 ** (7 - i)}").scale(1.5).next_to(arrows[i], DOWN))

    return byte, bins, arrows, pows, two_pows


def create_bits(bits: str) -> VGroup:
    bits = bits.replace(" ", "")
    vg = VGroup()
    for b in bits:
        vg.add(Square().set_fill(YELLOW, 1 if b == "1" else 0))
    vg.arrange(RIGHT, buff=0.5)
    return vg


class P2Math(Scene):
    def num_count(self, bites: VGroup) -> Text:
        num = Text("0").scale(2).move_to(bites).to_edge(LEFT)
        rec = SurroundingRectangle(bites[0], corner_radius=0.1, color=RED)
        self.play(Write(num), Create(rec))

        for i in range(1, len(bites)):
            self.play(
                Transform(
                    rec, SurroundingRectangle(bites[i], corner_radius=0.1, color=RED)
                ),
                Transform(num, Text(str(i)).scale(2).move_to(num)),
            )
            self.wait(0.5)

        self.wait(0.5)

        return num, rec

    def construct(self):
        self.wait()

        # self.next_section(skip_animations=True)
        byte, bins, arrows, pows, two_pows = create_byte("0010 1101")

        vg = VGroup(byte, bins, arrows, pows).move_to(ORIGIN)

        self.play(Create(byte), Write(bins), run_time=2)
        self.wait()

        self.play(Create(arrows), Create(pows))

        self.wait()

        # NOTE: EPLICATION
        # self.next_section(skip_animations=False)

        self.play(vg.animate.to_edge(UP))

        self.play(
            Transform(vg[:2], VGroup(create_byte("0000 0000")).to_edge(UP)[:2]),
            FadeOut(pows),
        )

        # NOTE: 1th bite
        # self.next_section(skip_animations=False)

        num = Text("0").scale(2).to_edge(DOWN)

        bite1 = (
            VGroup(
                Square().scale(0.5).set_fill(YELLOW, 0),
                Square().scale(0.5).set_fill(YELLOW, 1),
            )
            .arrange(DOWN)
            .shift(DOWN)
        )

        self.play(TransformFromCopy(byte[-1], bite1))

        self.wait()

        rec = SurroundingRectangle(bite1[0], corner_radius=0.1, color=RED)
        self.play(Create(rec))

        self.wait()

        self.play(Write(num))
        self.wait()

        self.play(
            Transform(
                rec, SurroundingRectangle(bite1[1], corner_radius=0.1, color=RED)
            ),
            Transform(num, Text("1").scale(2).move_to(num)),
        )
        self.wait()

        self.play(
            ReplacementTransform(num, pows[-1]),
            FadeOut(rec),
            bite1.animate.shift(3 * LEFT),
        )

        self.wait()

        # NOTE: 2 BITS
        # self.next_section(skip_animations=False)

        bite2 = (
            VGroup(*[create_bits(b) for b in ["00", "01", "10", "11"]])
            .arrange_in_grid(2, 2, buff=3)
            .scale(0.25)
            .shift(DOWN)
        )

        self.play(
            ReplacementTransform(bite1[0].copy(), bite2[0][0]),
            TransformFromCopy(byte[-2], bite2[0][1]),
            ReplacementTransform(bite1[0], bite2[1][0]),
            TransformFromCopy(byte[-2], bite2[1][1]),
        )

        self.wait()

        self.play(
            ReplacementTransform(bite1[1].copy(), bite2[2][0]),
            TransformFromCopy(byte[-2], bite2[2][1]),
            ReplacementTransform(bite1[1], bite2[3][0]),
            TransformFromCopy(byte[-2], bite2[3][1]),
        )

        num, rec = self.num_count(bite2)

        self.wait(0.5)

        self.play(ReplacementTransform(num, pows[-2:]), FadeOut(rec))

        self.wait()

        #  NOTE: 3 BITS
        # self.next_section(skip_animations=False)

        bits = ["000", "001", "010", "011", "100", "101", "110", "111"]

        bits3 = (
            VGroup(*[create_bits(b) for b in bits])
            .arrange_in_grid(3, 3, buff=3)
            .scale(0.25)
            .shift(2 * DOWN)
        )

        self.play(TransformMatchingShapes(bite2, bits3))
        self.wait()

        num, rec = self.num_count(bits3)

        self.wait(0.5)

        self.play(ReplacementTransform(num, pows[-3:]), FadeOut(rec))

        self.wait()

        # NOTE: 4BITS
        # self.next_section(skip_animations=False)

        bits = [
            "0000",
            "0001",
            "0010",
            "0011",
            "0100",
            "0101",
            "0110",
            "0111",
            "1000",
            "1001",
            "1010",
            "1011",
            "1100",
            "1101",
            "1110",
            "1111",
        ]

        bits4 = (
            VGroup(*[create_bits(b) for b in bits])
            .arrange_in_grid(4, 4, buff=3)
            .scale(0.20)
            .shift(2 * DOWN)
        )

        self.play(TransformMatchingShapes(bits3, bits4))
        self.wait()

        num, rec = self.num_count(bits4)

        self.wait(0.5)

        self.play(ReplacementTransform(num, pows[-4:]), FadeOut(rec))

        self.wait()

        self.play(FadeOut(bits4))

        # NOTE: next bits as double
        # self.next_section(skip_animations=False)

        rec = SurroundingRectangle(pows[-1], corner_radius=0.1, color=PINK)

        self.play(Create(rec))

        for i in range(1, 4):
            self.play(
                Transform(
                    rec,
                    SurroundingRectangle(pows[-i - 1], corner_radius=0.1, color=PINK),
                )
            )

        for i in range(4, 8):
            self.play(
                Transform(
                    rec,
                    SurroundingRectangle(pows[-i - 1], corner_radius=0.1, color=PINK),
                )
            )
            self.wait(0.5)
            self.play(ReplacementTransform(pows[-i].copy(), pows[-i - 1]))
        self.wait()

        self.play(FadeOut(rec))

        # NOTE: range
        # self.next_section(skip_animations=False)

        num = MathTex("0").scale(3).shift(2 * DOWN)
        self.play(Write(num))

        self.wait()

        self.play(
            Transform(vg, VGroup(create_byte("1111 1111")[:-1]).move_to(vg)),
            FadeOut(num),
        )

        self.wait()

        num = MathTex("128 + 64 + 32 + 16 + 8 + 4 + 2 + 1").scale(1.2).shift(2 * DOWN)

        self.play(TransformMatchingShapes(pows.copy(), num))

        self.wait()

        self.play(Transform(num, MathTex("255").scale(3).move_to(num)))

        self.wait()

        self.play(FadeOut(num))

        # NOTE:
        # Animacion final
        self.next_section(skip_animations=False)

        self.play(vg.animate.move_to(ORIGIN))
        self.play(TransformFromCopy(pows, two_pows))
        self.wait()

        self.play(FadeOut(two_pows))

        self.play(
            Transform(vg, VGroup(create_byte("0000 0000")[:-1]).to_edge(DOWN)),
        )

        self.wait()

        text = "Te_amo"
        textbin = [f"{ord(c):08b}" for c in text]
        t = Text(text).scale(2.5).to_edge(UP)
        tbin = (
            VGroup(*[Text(c) for c in textbin])
            .arrange_in_grid(3, 3, buff=(1, 0.3))
            .scale(1)
            .next_to(t, DOWN)
        )

        for i in range(len(t)):
            self.play(
                Write(t[i]),
                Transform(vg, VGroup(create_byte(textbin[i])[:-1]).to_edge(DOWN)),
            )
            self.play(TransformFromCopy(vg[0], tbin[i]))
