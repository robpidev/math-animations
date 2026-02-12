from itertools import pairwise

from manim import (
    BLACK,
    DOWN,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Arrow,
    Create,
    FadeOut,
    MathTex,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Text,
    Transform,
    TransformMatchingShapes,
    VGroup,
    Vector,
    Write,
)

from pixel import FONT, animate_pixel, pixel_hexa, pixel_rgb, rgb, to_hexa


class p9Hexa(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()
        # self.next_section(skip_animations=False)

        pixel_hex, vt_hex = pixel_hexa(255, 23, 128, True)
        pixel_hex = VGroup(*pixel_hex)
        self.play(Create(pixel_hex))
        self.wait()
        self.play(*animate_pixel(vt_hex, 128, 33, 205))
        self.wait(0.5)
        self.play(*animate_pixel(vt_hex, 32, 207, 23))
        self.wait(0.5)
        self.play(*animate_pixel(vt_hex, 187, 28, 187))
        self.wait(0.5)
        self.play(*animate_pixel(vt_hex, 255, 255, 255))
        # self.play(vt[1].animate.set_value(255))
        self.wait()

        # self.next_section(skip_animations=False)

        pix_rgb, vt_rgb = pixel_rgb(255, 255, 255, True)
        pix_rgb = VGroup(*pix_rgb)

        self.play(TransformMatchingShapes(pixel_hex, pix_rgb))
        self.wait()
        self.play(*animate_pixel(vt_rgb, 128, 23, 128))
        self.wait(0.5)
        self.play(*animate_pixel(vt_rgb, 33, 205, 32))
        self.wait(0.5)
        self.play(*animate_pixel(vt_rgb, 205, 23, 187))
        self.wait()

        self.play(FadeOut(pix_rgb))
        self.wait()

        # === Numbers To hexa ===
        # self.next_section(skip_animations=False)
        numbers = [str(i) if i > 9 else "0" + str(i) for i in range(16)]
        vt_hex = VGroup(
            VGroup(
                *[Text(i, font=FONT, t2c={"[:1]": BLACK}) for i in numbers[:8]],
            ).arrange(RIGHT, buff=1),
            VGroup(
                *[Text(i, font=FONT) for i in numbers[8:]],
            ).arrange(RIGHT, buff=1),
        )

        vt_hex[0][0][1].set_color(WHITE)
        vt_hex[1][0][0].set_color(BLACK)
        vt_hex[1][1][0].set_color(BLACK)

        hexa = VGroup(
            *[Arrow(UP, DOWN).next_to(n, DOWN).shift(DOWN) for n in vt_hex[1][2:]]
        ).set_color(YELLOW)

        hexa = VGroup(
            hexa,
            VGroup(
                *[
                    Text(char, font=FONT).next_to(hexa[i], DOWN)
                    for i, char in enumerate("ABCDEF")
                ]
            ).set_color(GREEN),
        )

        # VGroup(vt_hex, hexa).move_to(ORIGIN)

        vt_hex.arrange(DOWN, buff=1)
        self.play(Create(vt_hex))
        self.wait()
        self.play(Create(hexa), run_time=3)
        self.wait()

        hexa = VGroup(vt_hex, hexa)

        # self.next_section(skip_animations=False)
        self.play(hexa.animate.scale(0.4).to_edge(LEFT + UP))
        self.wait()

        # === Hexa To Number ===
        MathTex("F", "B").scale(2)

        eqs = [
            MathTex("F", "B"),
            MathTex("F", r"\cdot", "16", "+", "B"),
            MathTex("15", r"\cdot", "16", "+", "11"),
            MathTex(f"{15 * 16}", "+", "11"),
            MathTex(f"{15 * 16 + 11}"),
        ]

        eqs = VGroup(*eqs).arrange(DOWN, buff=0.5).scale(1.5).move_to(2 * RIGHT)

        self.play(Write(eqs[0]))

        for i, j in pairwise(eqs):
            self.play(ReplacementTransform(i.copy(), j))
            self.wait(0.5)

        result = MathTex(r"FB", "=", f"{15 * 16 + 11}").scale(2)
        self.play(
            TransformMatchingShapes(VGroup(eqs[0], eqs[-1]), result), FadeOut(eqs[1:-1])
        )

        self.play(FadeOut(result))

        eqs = [
            MathTex("FF"),
            MathTex("F", R"\cdot", "16", "+", "F"),
            MathTex("15", R"\cdot", "16", "+", "15"),
            MathTex("240", "+", "15"),
            MathTex("255"),
        ]

        eqs = VGroup(*eqs).arrange(DOWN, buff=0.5).scale(1.5).move_to(2 * RIGHT)

        self.play(Write(eqs[0]))

        for i, j in pairwise(eqs):
            self.play(ReplacementTransform(i.copy(), j))
            self.wait(0.5)

        result = MathTex(r"FF", "=", "255").scale(2)
        self.play(
            TransformMatchingShapes(VGroup(eqs[0], eqs[-1]), result), FadeOut(eqs[1:-1])
        )

        self.play(FadeOut(result))

        # self.next_section(skip_animations=False)
        # ===  Number To Exa ===
        num = 237
        eqs = [
            MathTex(str(num)),
            MathTex(r"\frac{" + str(num) + "}{" + "16" + "}"),
            MathTex(f"{num // 16}", r"\cdot 16+", f"{num % 16}"),
            MathTex(f"{to_hexa(num // 16)}", f"{to_hexa(num % 16)}"),
        ]

        eqs = VGroup(*eqs).arrange(DOWN, buff=0.5).scale(1.5).move_to(2 * RIGHT)

        self.play(Write(eqs[0]))

        self.play(
            ReplacementTransform(eqs[0].copy(), eqs[1][0][:3]), Write(eqs[1][0][3:])
        )

        self.play(ReplacementTransform(eqs[1].copy(), eqs[2]))

        sq = SurroundingRectangle(eqs[2][0], corner_radius=0.1, color=YELLOW)
        self.play(Create(sq))
        self.play(ReplacementTransform(eqs[2][0].copy(), eqs[3][0]))

        self.play(
            Transform(
                sq, SurroundingRectangle(eqs[2][-1], corner_radius=0.1, color=YELLOW)
            )
        )
        self.play(ReplacementTransform(eqs[2][-1].copy(), eqs[3][1]))
        self.play(FadeOut(sq))
        self.wait(0.2)

        result = MathTex(
            f"{num}", "=", f"{to_hexa(num // 16)}{to_hexa(num % 16)}"
        ).scale(2)
        self.play(
            TransformMatchingShapes(VGroup(eqs[0], eqs[-1]), result), FadeOut(eqs[1:-1])
        )

        self.wait()

        # self.next_section(skip_animations=False)
        self.play(FadeOut(*self.mobjects))
        self.wait()


class P9HexaE2Compare(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()

        pixel, vt = pixel_rgb(255, 22, 175, True)
        rt, gt, bt = vt
        subs = pixel[1]
        self.play(
            Create(pixel),
        )

        self.wait()

        arrows = [
            Vector(RIGHT, color=rgb(255, 0, 0)).next_to(subs[0], RIGHT),
            Vector(RIGHT, color=rgb(0, 255, 0)).next_to(subs[1], RIGHT),
            Vector(RIGHT, color=rgb(0, 0, 255)).next_to(subs[2], RIGHT),
        ]

        hexs = [
            Text(f"{to_hexa(int(rt.get_value()))}", font=FONT)
            .next_to(arrows[0], RIGHT)
            .set_z_index(3),
            Text(f"{to_hexa(int(gt.get_value()))}", font=FONT)
            .next_to(arrows[1], RIGHT)
            .set_z_index(3),
            Text(f"{to_hexa(int(bt.get_value()))}", font=FONT)
            .next_to(arrows[2], RIGHT)
            .set_z_index(3),
        ]

        hexs[0].add_updater(
            lambda m: m.become(
                Text(f"{to_hexa(int(rt.get_value()))}", font=FONT).move_to(m)
            )
        )

        hexs[1].add_updater(
            lambda m: m.become(
                Text(f"{to_hexa(int(gt.get_value()))}", font=FONT).move_to(m)
            )
        )

        hexs[2].add_updater(
            lambda m: m.become(
                Text(f"{to_hexa(int(bt.get_value()))}", font=FONT).move_to(m)
            )
        )

        for a, h in zip(arrows, hexs):
            self.play(Create(a), run_time=0.5)
            self.play(Write(h), run_time=0.5)

        self.wait()

        hexs = VGroup(*hexs)

        hex_label = Text(
            f"#{to_hexa(rt.get_value())}{to_hexa(gt.get_value())}{to_hexa(bt.get_value())}",
            font=FONT,
        ).set_z_index(3)

        hex_label.add_updater(
            lambda m: m.become(
                Text(
                    f"#{int(rt.get_value()):02X}{int(gt.get_value()):02X}{int(bt.get_value()):02X}",
                    font=FONT,
                ).move_to(m)
            )
        )

        sqs = [
            SurroundingRectangle(
                hex_label[1:3], corner_radius=0.1, color=rgb(255, 0, 0), buff=0.01
            ).set_opacity(1),
            SurroundingRectangle(
                hex_label[3:5], corner_radius=0.1, color=rgb(0, 255, 0), buff=0.01
            ).set_opacity(1),
            SurroundingRectangle(
                hex_label[5:], corner_radius=0.1, color=rgb(0, 0, 255), buff=0.01
            ).set_opacity(1),
        ]

        hex_label = VGroup(hex_label, *sqs)

        # self.play(pixel[-2].animate.move_to(3 * LEFT))

        # self.next_section(skip_animations=False)

        hex_label.next_to(pixel[-1], RIGHT)

        self.play(TransformMatchingShapes(hexs.copy(), hex_label))
        self.wait()

        self.play(hex_label.animate.move_to(pixel[-1]), FadeOut(pixel[-1]))

        self.wait()

        # self.next_section(skip_animations=False)
        self.play(animate_pixel(vt, 0, 0, 0), run_time=2)
        self.wait(0.5)
        self.play(animate_pixel(vt, 128, 168, 245), run_time=2)
        self.wait(0.5)
        self.play(animate_pixel(vt, 244, 12, 134), run_time=2)
        self.wait(0.5)
        self.play(animate_pixel(vt, 255, 255, 255), run_time=2)
        self.wait(0.5)
        self.play(animate_pixel(vt, 157, 51, 204), run_time=2)
        self.wait()
