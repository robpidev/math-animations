from manim import *


def create_bit(bit="0"):
    return VGroup(
        Square().set_fill(color=YELLOW, opacity=1 if bit == "1" else 0),
        Text(bit).scale(2)
    ).arrange(DOWN)

def create_kb(color=1):
    return VGroup(
        Rectangle(height=1, width=2).set_fill(color=YELLOW, opacity=0.2 if color == 1 else 0),
        Text("1024")
    )

def create_pow(color=1, pow=2):
    return VGroup(
        Rectangle(
            height=1, width=2
        ).set_fill(color=YELLOW, opacity=0.2 if color == 1 else 0),
        MathTex(f"1024^{pow}").scale(1.5)
    )

class p3_mult(Scene):
    def construct(self):
        bit = create_bit("0")

        self.play(Create(bit[0]), Write(bit[1]))
        self.wait()

        bit_name = Text("bit (b)").to_edge(UP)
        self.play(Write(bit_name))

        self.wait()
        
        self.play(Transform(bit, create_bit("1")))
        self.wait()

        kb = VGroup(
            [create_bit(str("1" if i % 2 == 0 else "0")) for i in range(4)],
            Text('...').scale(2),
            [create_bit(str("1" if i % 2 == 0 else "0")) for i in range(4)],
        ).arrange(RIGHT, buff=0.5).scale(0.5)

        self.play(
            ReplacementTransform(bit, kb[0]),
        )

        self.wait()

        self.play(Create(kb[1:]))

        brace = Brace(kb, direction=DOWN, buff=0.1)

        kb_text = brace.get_text("1024").scale(1.5)
        self.play(Create(brace), Write(kb_text))

        self.wait()

        kb_name = Text("Kilobit (Kb)").move_to(bit_name)
        self.play(
            TransformFromCopy(kb_text, kb_name[:4]),
            ReplacementTransform(bit_name[:3], kb_name[4:-4]),
            FadeOut(bit_name[3:])
        )

        self.wait()

        self.play(
            TransformFromCopy(kb_name[0], kb_name[-3], path_arc=PI/2),
            TransformFromCopy(kb_name[4], kb_name[-2], path_arc=PI/2),
            Write(kb_name[-4::3])
        )

        self.wait()

        # NOTE: MB
        # self.next_section(skip_animations=False)

        mb = VGroup(
            *[create_kb(i % 2) for i in range(2)],
            Text("...").scale(2),
            *[create_kb(i % 2) for i in range(2)],
        ).arrange(RIGHT, buff=0.5)

        self.play(
            ReplacementTransform(kb, mb[0]),
            FadeOut(kb_text, brace)
        )

        self.wait()
        self.play(Create(mb[1:], run_time=2))
        self.wait()

        brace = Brace(mb, DOWN)
        mb_text = brace.get_text("1024").scale(1.5)

        self.play(Write(brace))
        self.play(Write(mb_text))
        self.wait()

        value = MathTex(r"1024", r"\cdot", "1024").scale(2)
        value.to_edge(DOWN)

        self.play(
            TransformMatchingShapes(mb[0][1].copy(), value[0]),
            TransformMatchingShapes(mb_text.copy(), value[2]),
            Write(value[1])
        )

        self.wait()

        self.play(
            Transform(
                value, MathTex(f"{1024 ** 2}").scale(2).to_edge(DOWN)
            )
        )

        mb_name = Text("Megabit (Mb)").to_edge(UP)

        self.play(
            ReplacementTransform(value, mb_name[:4]),
            ReplacementTransform(kb_name[4:7], mb_name[4:7]),
            FadeOut(kb_name[:4], kb_name[7:])
        )

        self.wait()

        self.play(
            TransformFromCopy(mb_name[0], mb_name[-3], path_arc=PI/2),
            TransformFromCopy(mb_name[4], mb_name[-2], path_arc=PI/2),
            Write(mb_name[-4::3])
        )

        self.wait()

        # NOTE: Gb
        # self.next_section(skip_animations=False)

        gb = VGroup(
            *[create_pow(color=i % 2, pow=2) for i in range(2)],
            Text("...").scale(2),
            *[create_pow(color=i % 2, pow=2) for i in range(2)],
        ).arrange(RIGHT, buff=0.5)

        self.play(
            ReplacementTransform(
                mb, gb[0],
            ),
            FadeOut(mb_text, brace)
        )

        self.wait()

        self.play(Create(gb[1:]), run_time=2)
        self.wait()

        brace = Brace(gb, DOWN)
        gb_text = brace.get_text("1024").scale(1.5)

        self.play(Write(brace))
        self.play(Write(gb_text))
        self.wait()

        value = MathTex(r"1024^2", r"\cdot", "1024").scale(2)
        value.to_edge(DOWN)

        self.play(
            TransformMatchingShapes(gb[0][1].copy(), value[0]),
            TransformMatchingShapes(gb_text.copy(), value[2]),
            Write(value[1])
        )

        self.wait()

        self.play(
            Transform(
                value, MathTex(f"{1024 ** 3}").scale(2).to_edge(DOWN)
            )
        )

        gb_name = Text("Gigabit (Gb)").to_edge(UP)

        self.play(
            ReplacementTransform(value, gb_name[:4]),
            ReplacementTransform(mb_name[4:7], gb_name[4:7]),
            FadeOut(mb_name[:4], mb_name[7:])
        )

        self.wait()

        self.play(
            TransformFromCopy(gb_name[0], gb_name[-3], path_arc=PI/2),
            TransformFromCopy(gb_name[4], gb_name[-2], path_arc=PI/2),
            Write(gb_name[-4::3])
        )

        self.wait()

        #NOTE: Tb
        # self.next_section(skip_animations=False)

        tb = VGroup(
            *[create_pow(color=i % 2, pow=3) for i in range(2)],
            Text("...").scale(2),
            *[create_pow(color=i % 2, pow=3) for i in range(2)],
        ).arrange(RIGHT, buff=0.5)

        self.play(
            ReplacementTransform(
                gb, tb[0],
            ),
            FadeOut(gb_text, brace)
        )

        self.wait()

        self.play(Create(tb[1:]), run_time=2)
        self.wait()

        brace = Brace(tb, DOWN)
        tb_text = brace.get_text("1024").scale(1.5)

        self.play(Write(brace))
        self.play(Write(tb_text))
        self.wait()

        value = MathTex(r"1024^3", r"\cdot", "1024").scale(2)
        value.to_edge(DOWN)

        self.play(
            TransformMatchingShapes(tb[0][1].copy(), value[0]),
            TransformMatchingShapes(tb_text.copy(), value[2]),
            Write(value[1])
        )

        self.wait()

        self.play(
            Transform(
                value, MathTex(f"{1024 ** 4}").scale(2).to_edge(DOWN)
            )
        )

        tb_name = Text("Terabit (Tb)").to_edge(UP)

        self.play(
            ReplacementTransform(value, tb_name[:4]),
            ReplacementTransform(gb_name[4:7], tb_name[4:7]),
            FadeOut(gb_name[:4], gb_name[7:])
        )

        self.wait()

        self.play(
            TransformFromCopy(tb_name[0], tb_name[-3], path_arc=PI/2),
            TransformFromCopy(tb_name[4], tb_name[-2], path_arc=PI/2),
            Write(tb_name[-4::3])
        )

        self.wait()


        # NOTE: BYTES
        # *******************
