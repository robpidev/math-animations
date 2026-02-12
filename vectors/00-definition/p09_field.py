from manim import *


class Field(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        group = MathTex(r"(\mathbb{R},+", ")")
        field = MathTex(r"(\mathbb{R},+", ",\cdot", ")")

        self.play(Write(group))
        self.wait()
        self.play(TransformMatchingTex(group, field))
        self.wait()

        a = MathTex(r"\text{(A). } (\mathbb{R}, +) \text{ es un grupo Abeliano}.")
        m = Tex("(M). Propiedades de la multiplicación: ")
        m1 = MathTex(
            r"\quad 1. \quad",
            r"x, y \in \mathbb{R} \implies x \cdot y \in \mathbb{R}",
        )

        m2 = MathTex(
            r"2. \quad",
            r"x \cdot y = y \cdot x,\quad \forall x, y \in \mathbb{R}",
        )

        m3 = MathTex(
            r"3. \quad",
            r"(x \cdot y) \cdot z = x \cdot (y \cdot z),"
            + r"\quad \forall x, y, z \in\mathbb{R}",
        )

        m4 = MathTex(
            r"4. \quad",
            r"\exists 1 \neq 0 \in \mathbb{R} : 1 \cdot x = x",
        )

        m5 = MathTex(
            r"5. \quad",
            r"\forall x \neq 0 \in \mathbb{R},\quad \exists 1/x \in \mathbb{R}:"
            + r"(1/x) \cdot x = 1",
        )

        d = MathTex(
            r"\text{(D). Ley Distributiva: }",
        )

        d1 = MathTex(
            r"x \cdot (y + z) = x \cdot y + x \cdot z,",
            r"\quad \forall x, y, z \in \mathbb{R}",
        )

        line = Line([-5, 0, 0], [5, 0, 0], stroke_width=2)
        line.set_color(YELLOW)

        field_c = field.copy()

        fieldg = VGroup(field, line, a, m, m1, m2, m3, m4, m5, d, d1)

        fieldg.arrange(DOWN, aligned_edge=LEFT)

        fieldg[4:9].shift(RIGHT * 0.5)
        fieldg[-1].shift(RIGHT * 0.5)

        fieldg[:3].shift(UP * 0.3)
        fieldg[-2:].shift(DOWN * 0.3)

        self.clear()

        self.play(Transform(field_c, field))
        self.wait()

        for prop in fieldg[1:]:
            self.play(Write(prop))
            self.wait()

        field_name = MathTex(
            r"\text{Campo (Cuerpo): }", r"(\mathbb{R},+", ",\cdot", ")"
        )

        field_name.move_to(fieldg[0].get_center() + RIGHT * 2)

        self.play(TransformMatchingTex(field_c, field_name))
        self.wait()

        self.play(FadeOut(fieldg[1:], field_name))

        write = MathTex(
            "x\cdot y",
            ",",
            r"\quad x \cdot \left(\frac{1}{y}\right)",
            ",",
            r"\quad (x\cdot y) \cdot z",
            ",",
            r"\quad xx",
            ",",
            r"\quad x + x",
            ",",
            "\quad\dots",
        )

        write_alt = MathTex(
            r"xy",
            ",",
            r"\quad \frac{x}{y}",
            ",",
            r"\quad xyz",
            ",",
            r"\quad x^2",
            ",",
            r"\quad 2x",
            ",",
            "\quad\dots",
        )

        VGroup(write, write_alt).arrange(DOWN, buff=1)
        # write_alt =

        # self.next_section(skip_animations=False)

        for i in range(0, len(write) - 2, 2):
            self.play(Write(write[i]))
            self.play(TransformMatchingShapes(write[i].copy(), write_alt[i]))
            self.play(Write(write[i + 1]), Write(write_alt[i + 1]))

        self.play(Write(write[-1]), Write(write_alt[-1]))
