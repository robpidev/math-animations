from manim import *


class Conclution(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        de = MathTex(
            r"\mathbb{R}^2",
            r".\quad \text{Def. } \mathbf{u + v}",
            r",\text{ } c\mathbf{u}.",
            r" \quad c\in \mathbb{R}",
            r"\wedge \mathbf{u, v}\in \mathbb{R}^2",
        )

        de_alt = MathTex(
            r"\mathbb{R}^3",
            r".\quad \text{Def. } \mathbf{u + v}",
            r",\text{ } c\mathbf{u}.",
            r" \quad c\in \mathbb{R}",
            r"\wedge \mathbf{u, v}\in \mathbb{R}^3",
        )

        de_gen = MathTex(
            r"V",
            r".\quad \text{Def. } \mathbf{u + v}",
            r",\text{ } c\mathbf{u}.",
            r" \quad c\in \mathbb{F}",
            r"\wedge \mathbf{u, v}\in V",
        )

        p1 = MathTex(
            r"\text{1. }",
            r"\mathbf{u + v} \in \mathbb{R}^2",
        )
        p2 = MathTex(
            r"\text{2. }",
            r"\mathbf{u + v = v + u}",
        )

        p3 = MathTex(
            r"\text{3. }",
            r"\mathbf{(u + v) + w = u + (v + w)}",
        )

        p4 = MathTex(
            r"\text{4. }",
            r"\exists \mathbf{0} \in \mathbb{R} : \mathbf{u + 0 = u}",
        )

        p5 = MathTex(
            r"\text{5. }",
            r"\forall \mathbf{u}, \exists -\mathbf{u} \in \mathbb{R}^2",
            r": \mathbf{u + (-u) = 0}",
        )

        p6 = MathTex(
            r"\text{6. }",
            r"c\mathbf{u} \in \mathbb{R}^2",
        )

        p7 = MathTex(
            r"\text{7. }",
            r"c(\mathbf{u + v}) = c\mathbf{u} + c \mathbf{v}",
        )
        p8 = MathTex(
            r"\text{8. }",
            r"(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}",
        )
        p9 = MathTex(
            r"\text{9. }",
            r"c(d\mathbf{u}) = (cd)\mathbf{u}",
        )
        p10 = MathTex(r"\text{10. }", r"1\mathbf{u} = \mathbf{u}")

        el = MathTex(
            r"\forall c, d \in \mathbb{R}",
            r"\wedge\forall \mathbf{u, v, w} \in \mathbb{R}^2",
        )

        props = (
            VGroup(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
        )

        space = VGroup(de, props, el).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        de_alt.move_to(de.get_center())
        de_gen.move_to(de.get_center())

        props.shift(RIGHT * 0.5)
        space.move_to(ORIGIN)

        for mo in de:
            self.play(Write(mo))
            self.wait()

        for prop in props:
            self.play(Write(prop))

        self.wait()

        self.play(Write(el))
        self.wait()

        # self.next_section(skip_animations=False)
        self.wait()

        esp = Tex(r"$\mathbb{R}^2$", ": Espacio vectorial")
        esp_alt = Tex(r"$\mathbb{R}^3$", ": Espacio vectorial")

        vecs = Tex(r"$\mathbf{u, v} \in \mathbb{R}^2$", ": Vectores")
        vecs_alt = Tex(r"$\mathbf{u, v} \in \mathbb{R}^3$", ": Vectores")

        esp_gen = Tex(r"$V$", ": Espacio vectorial")
        vecs_gen = Tex(r"$\mathbf{u, v} \in V$", ": Vectores")

        VGroup(esp, vecs).arrange(DOWN, aligned_edge=LEFT)
        esp_alt.move_to(esp.get_center())
        esp_gen.move_to(esp.get_center())

        vecs_gen.move_to(vecs.get_center())
        vecs_alt.move_to(vecs.get_center())

        self.play(ReplacementTransform(space[1:], esp[0]))
        self.wait()
        self.play(Write(esp[1]))
        self.wait()
        self.play(Write(vecs[0]))
        self.wait()
        self.play(Write(vecs[1]))
        self.wait()

        self.play(
            ReplacementTransform(esp, esp_alt),
            ReplacementTransform(vecs, vecs_alt),
            ReplacementTransform(de, de_alt),
        )
        self.wait()

        self.play(
            ReplacementTransform(esp_alt, esp_gen),
            ReplacementTransform(vecs_alt, vecs_gen),
            ReplacementTransform(de_alt, de_gen),
        )
