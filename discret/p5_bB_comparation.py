from manim import (
    DOWN,
    RIGHT,
    UP,
    YELLOW,
    Brace,
    Create,
    Scene,
    Square,
    Text,
    Transform,
    Vector,
    VGroup,
    Write,
)


def create_bits(bits: str) -> VGroup:
    bits = bits.replace(" ", "")
    vg = VGroup()
    for b in bits:
        sq = Square().set_fill(YELLOW, 1 if b == "1" else 0)
        text = Text(b).scale(2).next_to(sq, DOWN)
        bit = VGroup(sq, text).arrange(DOWN)
        vg.add(bit)
    vg.arrange(RIGHT, buff=1)
    return vg


class P5BbComparation(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        byte = create_bits("0010 1101").scale(0.5)
        arrow = Vector(DOWN).next_to(byte[3], UP)
        bit_name = Text("bit (b)").next_to(arrow, UP)

        brace = Brace(byte, DOWN)
        brace_text = brace.get_text("Byte (B)").scale(1.5)

        vg = VGroup(byte, arrow, bit_name, brace, brace_text)

        self.play(Create(byte), run_time=2)
        self.play(Create(arrow), Write(bit_name))
        self.wait()

        self.play(Write(brace), Write(brace_text))
        self.wait()

        comps_text = [
            "Byte = 8 bits",
            "KiloByte (KB) = 8 kilobits (Kb)",
            "MegaByte (MB) = 8 Megabits (Mb)",
            "GigaByte (GB) = 8 gigabits (Gb)",
            "TeraByte (TB) = 8 terabits (Tb)",
        ]

        comp = Text("Byte = 8 bits").to_edge(DOWN)
        self.play(vg.animate.to_edge(UP))

        self.play(Write(comp))
        self.wait()

        for text in comps_text:
            self.play(Transform(comp, Text(text).to_edge(DOWN)))
            self.wait(0.5)

        self.wait()
