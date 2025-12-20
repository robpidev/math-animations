from manim import (
    DOWN,
    PI,
    RIGHT,
    UP,
    YELLOW,
    Brace,
    Create,
    FadeOut,
    MathTex,
    Rectangle,
    ReplacementTransform,
    Scene,
    Square,
    Text,
    Transform,
    TransformFromCopy,
    TransformMatchingShapes,
    VGroup,
    Write,
)


def create_byte(byte_text="1000 1101"):
    byte_text = byte_text.replace(" ", "")
    byte = VGroup()
    for b in byte_text:
        sq = Square().scale(0.5).set_fill(YELLOW, 1 if b == "1" else 0)
        text = Text(b).scale(1.5).next_to(sq, DOWN)
        bit = VGroup(sq, text).arrange(DOWN)
        byte.add(bit)
    byte.arrange(RIGHT, buff=0.5)
    return byte


def create_pow(color=1, pow=0):
    return VGroup(
        Rectangle(height=1, width=2).set_fill(
            color=YELLOW, opacity=0.2 if color == 1 else 0
        ),
        MathTex("1024" + (f"^{pow}" if pow != 1 else "")).scale(1.2)
        if pow != 0
        else Text("Byte"),
    )


class P4MultByte(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        byte = create_byte()
        self.play(Create(byte), run_time=2)
        self.wait()

        byte_name = Text("Byte (B)").to_edge(UP)
        self.play(Write(byte_name))
        self.wait()

        vg, vg_name = self.pow(byte, byte_name, "Kilo")
        vg, vg_name = self.pow(vg, vg_name, "Mega", pow=1)
        vg, vg_name = self.pow(vg, vg_name, "Giga", pow=2)
        self.next_section(skip_animations=False)
        vg, vg_name = self.pow(vg, vg_name, "Tera", pow=3)

        # Bit and byte comparation

    def pow(self, unity: VGroup, u_title: Text, u_name: str, pow=0):
        vg = VGroup(
            *[create_pow(color=i % 2, pow=pow) for i in range(2)],
            Text("...").scale(2),
            *[create_pow(color=i % 2, pow=pow) for i in range(2)],
        ).arrange(RIGHT, buff=0.5)

        self.play(
            ReplacementTransform(
                unity,
                vg[0],
            )
        )
        self.wait()
        self.play(Create(vg[1:]), run_time=2)
        self.wait()

        brace = Brace(vg, direction=DOWN, buff=0.1)
        brace_text = MathTex("1024").scale(1.5).next_to(brace, DOWN)

        self.play(Write(brace))
        self.play(Write(brace_text))
        self.wait()

        value = (
            MathTex(("1024" + f"^{pow}") if pow > 0 else "1", r"\cdot", "1024")
            .scale(2)
            .to_edge(DOWN)
        )

        self.play(
            ReplacementTransform(vg[0][1].copy(), value[0]),
            Write(value[1]),
            TransformMatchingShapes(brace_text.copy(), value[2]),
        )

        self.wait()

        self.play(
            Transform(value, MathTex(f"{1024 ** (pow + 1)}").scale(2).to_edge(DOWN))
        )

        self.wait()

        unity_name = Text(f"{u_name}Byte ({u_name[0].capitalize()}B)")
        unity_name.to_edge(UP)
        start = u_title.text.find("B")
        self.play(
            ReplacementTransform(
                value,
                unity_name[:4],
            ),
            ReplacementTransform(u_title[start : start + 4], unity_name[4:8]),
            FadeOut(u_title[start + 4 :], u_title[:start]),
        )

        self.wait()

        self.play(
            TransformFromCopy(unity_name[0], unity_name[-3], path_arc=PI / 2),
            TransformFromCopy(unity_name[4], unity_name[-2], path_arc=PI / 2),
            Write(unity_name[-4::3]),
        )

        self.wait()

        return VGroup(vg, brace, brace_text), unity_name
