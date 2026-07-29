from bites import create_byte, int_to_bin
from manim import (
    DOWN,
    UP,
    Brace,
    Create,
    FadeOut,
    MathTex,
    ReplacementTransform,
    Scene,
    Text,
    Transform,
    TransformFromCopy,
    ValueTracker,
    Vector,
    VGroup,
    Write,
)

font = "JetBrainsMono Nerd Font"


class P1Unsigned(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        self.wait()

        num = ValueTracker(113)

        byte_text = Text(f"{int(num.get_value())}", font=font).scale(2)
        byte = create_byte(int_to_bin(num.get_value())).scale(0.75)

        gbyte = VGroup(byte_text, byte)

        self.play(Write(byte_text))
        self.wait()
        num_text_c = byte_text.copy()
        byte_text.set_opacity(0)
        self.play(ReplacementTransform(num_text_c, byte))
        self.wait()
        self.play(gbyte.animate.arrange(DOWN, buff=1))
        byte_text.set_opacity(1)
        self.play(TransformFromCopy(byte, byte_text))
        self.wait()

        # === Def U8 ===
        # self.next_section(skip_animations=False)
        brace = Brace(byte, DOWN)
        brace_label = brace.get_text("Byte (B)")

        self.play(Write(brace), Write(brace_label))
        self.wait()
        self.play(Transform(brace_label, brace.get_text("8 bits (b)")))
        self.wait()

        self.play(FadeOut(brace_label, brace))
        self.wait()

        byte_text.add_updater(
            lambda m: m.become(
                Text(f"{int(num.get_value())}", font=font).scale(2).move_to(m)
            )
        )

        byte.add_updater(
            lambda m: m.become(
                create_byte(int_to_bin(num.get_value())).scale(0.75).move_to(m)
            )
        )

        # self.next_section(skip_animations=False)
        self.play(num.animate.set_value(0), run_time=2)
        self.wait()
        self.play(num.animate.set_value(255), run_time=2)
        self.wait()

        # === 8 bits ===
        vec = Vector(UP)
        text = Text("1", font=font)

        # self.next_section(skip_animations=False)
        counter = VGroup(vec, text).arrange(DOWN).next_to(byte[-1], DOWN)
        self.play(Create(vec))
        self.play(Write(text))
        self.wait()

        for i in range(1, 8):
            self.play(
                vec.animate.next_to(byte[7 - i], DOWN),
                Transform(
                    text,
                    Text(f"{i + 1}", font=font)
                    .next_to(byte[7 - i], DOWN)
                    .shift(1.2 * DOWN),
                ),
            )

        self.next_section(skip_animations=False)

        eq = MathTex("2^{}", "{}^8", "-", "1").scale(2)
        eq.to_edge(DOWN)

        self.play(Create(eq[0]))
        self.wait()

        self.play(TransformFromCopy(text, eq[1]))

        self.wait()

        self.remove(*self.mobjects)
        self.add(byte, byte_text, counter)

        resut = MathTex("256").scale(2)
        resut.move_to(eq[:2])

        self.play(TransformFromCopy(eq[:2], resut))
        self.wait()

        self.play(Transform(resut, eq[:2]))
        self.wait()

        self.next_section(skip_animations=False)
        self.play(num.animate.set_value(0))
        self.wait()
        self.play(num.animate.set_value(255))
        self.wait()
        self.play(Write(eq[2:]))
        self.wait()
