from manim import *


def create_byte(byte_text = "1000 1101"):
    byte_text = byte_text.replace(" ", "")
    byte = VGroup()
    for b in byte_text:
        sq = Square().scale(0.5).set_fill(YELLOW, 1 if b == '1' else 0)
        text = Text(b).scale(1.5).next_to(sq, DOWN)
        bit = VGroup(sq, text).arrange(DOWN)
        byte.add(bit)
    byte.arrange(RIGHT, buff=0.5)
    return byte


def create_pow(color=1, pow=0):
    return VGroup(
        Rectangle(
            height=1, width=2
        ).set_fill(color=YELLOW, opacity=0.2 if color == 1 else 0),
        MathTex(f"1000" + (f"^{pow}" if pow != 1 else "")).scale(1.2) if pow != 0 else Text("Byte")
    )

def create_table(number: int, name: str) -> VGroup:
    return VGroup(
        Text(f"Sistema {name}"),
        Line(LEFT, 4 * RIGHT),
        *[
            VGroup(
                Text(f"{mult}B", t2c={"[:1]": YELLOW}, font="JetBrainsMono Nerd Font"),
                Vector(RIGHT),
                MathTex(f"{number}^{i}", color=YELLOW).scale(1.5)
            ).arrange(RIGHT, buff=0.5)
            for i, mult in enumerate("1KMGT")
        ]
    ).arrange(DOWN, buff=0.5)


class P6BinDec(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        byte = create_byte("1000 1101")
        byte_name = Text("Byte (B)").to_edge(UP)
        self.play(Create(byte), Write(byte_name), run_time=3)
        self.wait()

        vg, vg_name = self.pow(byte, byte_name, "Kilo")

        for i, name in enumerate(["Mega", "Giga", "Tera"]):
            vg, vg_name = self.pow(vg, vg_name, name, i + 1)

        self.wait()

        # self.next_section(skip_animations=False)

        bytes_dec = create_table(1000, "Decimal") 
        bytes_bin = create_table(1024, "Binario") 

        tables = VGroup(
            bytes_dec,
            bytes_bin
        ).arrange(RIGHT, buff=2)

        self.play(
            ReplacementTransform(
                vg, VGroup(
                        *([o[0] for o in bytes_dec[2:]]),
                    bytes_dec[0],
                    bytes_dec[1],
                )
            ),
            FadeOut(vg_name)
        )

        self.wait()

        for o in bytes_dec[2:]:
            self.play(Create(o[1]), run_time = 0.3)
            self.play(
                TransformFromCopy(
                    o[0][0], o[2], path_arc=-PI/2
                )
            )
            self.wait(0.5)
        
        self.wait()

        # self.next_section(skip_animations=False)

        self.play(Write(bytes_bin[0]), Create(bytes_bin[1]))
        self.wait()

        self.play(
            TransformFromCopy(
                bytes_dec[2:], bytes_bin[2:]
            )
        )

        self.wait()
        # self.next_section(skip_animations=False)

        self.play(
            FadeOut(
                bytes_dec[2:],
                bytes_bin[2:],
            ),
            bytes_dec[5].animate.next_to(bytes_dec[1], DOWN),
            bytes_bin[5].animate.next_to(bytes_bin[1], DOWN),
        )

        self.add(bytes_dec[5], bytes_bin[5])

        eq = MathTex(
            r"\frac{1000^3}{1024^3}", "=", f"{1000**3/1024**3:.2f}"
        ).scale(2).to_edge(DOWN)


        # self.next_section(skip_animations=False)
        self.play(ReplacementTransform(bytes_dec[5][2].copy(), eq[0][0:5]))
        self.play(Write(eq[0][5]))
        self.play(ReplacementTransform(bytes_bin[5][2].copy(), eq[0][6:]))

        self.wait()
        self.play(Write(eq[1]))
        self.play(
            TransformFromCopy(
                eq[0], eq[-1], path_arc=-PI/2
            )
        )

        self.wait()
        eqc = MathTex("0.93").scale(2).to_edge(DOWN)
        self.play(
            # FadeOut(eq[:-1]),
            TransformMatchingTex(
            eq,
            eqc
        ))

        # self.next_section(skip_animations=False)

        examp = MathTex(
            r"16 \text{ GB}",
            r"\implies",
            r"0.93 \times 16 \text{ GB}",
            "=",
            f"{0.93 * 16:.2f}" + r"\text{ GB}"
        ).scale(1.5).shift(DOWN)

        self.play(Write(examp[0]))
        self.wait()
        self.play(Write(examp[1]))
        self.play(
            ReplacementTransform(
                eqc, examp[2][:4]
            )
        )
        self.wait()
        self.play(
            Write(examp[2][4]),
            TransformFromCopy(
                examp[0], examp[2][5:], path_arc=-PI/2
            )
        )

        self.wait()

        self.play(Write(examp[3]))
        self.play(TransformFromCopy(
            examp[2], examp[4], path_arc=-PI/2
        ))


        # self.next_section(skip_animations=False)

        self.wait()

        examp2 = MathTex(
            r"500 \text{ GB}",
            r"\implies",
            r"0.93 \times 500 \text{ GB}",
            "=",
            f"{0.93 * 500:.2f}" + r"\text{ GB}"
        ).scale(1.5).shift(DOWN)

        self.play(Transform(examp, examp2))

        self.wait()
        examp2 = MathTex(
            r"1 \text{ TB}", "=", r"1000 \text{ GB}"
        ).scale(3).shift(DOWN)

        self.play(Transform(examp, examp2)) 
        self.wait()



    def pow(self, unity: VGroup, u_title: Text, u_name: str, pow=0):
        vg = VGroup(
            *[create_pow(color=i % 2, pow=pow) for i in range(2)],
            Text('...').scale(2),
            *[create_pow(color=i % 2, pow=pow) for i in range(2)],
        ).arrange(RIGHT, buff=0.5)

        self.play(ReplacementTransform(unity, vg[0],))
        self.wait()
        self.play(Create(vg[1:]), run_time = 2)
        self.wait()

        brace = Brace(vg, direction=DOWN, buff=0.1)
        brace_text = MathTex(
            f"1000" 
        ).scale(1.5).next_to(brace, DOWN)
        
        self.play(Write(brace))
        self.play(Write(brace_text))
        self.wait()

        value = MathTex(
            ("1000" + f"^{pow}") if pow > 0 else "1", r"\cdot", "1000"
        ).scale(2).to_edge(DOWN)

        self.play(
            ReplacementTransform(vg[0][1].copy(), value[0]),
            Write(value[1]),
            TransformMatchingShapes(brace_text.copy(), value[2])
        )

        self.wait()

        self.play(
            Transform(
                value,
                MathTex(f"{1000 ** (pow + 1)}").scale(2).to_edge(DOWN)
            )
        )

        self.wait()

        unity_name = Text(f"{u_name}Byte ({u_name[0].capitalize()}B)")
        unity_name.to_edge(UP)
        start = u_title.text.find("B")
        self.play(
            ReplacementTransform(
                value, unity_name[:4],
            ),
            ReplacementTransform(
                u_title[start : start + 4], unity_name[4:8]
            ),
            FadeOut(u_title[start + 4:], u_title[: start])
        )

        self.wait()

        self.play(
            TransformFromCopy(unity_name[0], unity_name[-3], path_arc=PI/2),
            TransformFromCopy(unity_name[4], unity_name[-2], path_arc=PI/2),
            Write(unity_name[-4::3])
        )

        self.wait()

        return VGroup(vg, brace, brace_text), unity_name


