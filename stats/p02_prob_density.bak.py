from manim import (
    DOWN,
    GREEN,
    ORIGIN,
    YELLOW,
    Create,
    FadeOut,
    MathTex,
    RoundedRectangle,
    Scene,
    TransformMatchingShapes,
    TransformMatchingTex,
    VGroup,
    Write,
)


class P02ProbDensity(Scene):
    def construct(self):
        self.wait()

        # ============================================================
        # FASE 1  —  PROBLEMA
        # ============================================================

        self.next_section(skip_animations=True)

        desc = MathTex(r"\text{Dada una variable aleatoria continua } x \text{,}")
        desc2 = MathTex(r"\ \text{con densidad de probabilidad}")
        pdf_eq = MathTex(r"P(x) = A e^{-2x}, \quad x > 0")
        question = MathTex(
            r"\text{Hallar el valor de } A \text{ y la probabilidad de que } x > 1"
        )

        problem = VGroup(desc, desc2, pdf_eq, question)
        problem.arrange(DOWN, buff=0.4)
        problem.move_to(ORIGIN)

        self.play(Write(desc))
        self.wait()
        self.play(Write(desc2))
        self.wait()
        self.play(Write(pdf_eq))
        self.wait()
        self.play(Write(question))
        self.wait()
        self.play(FadeOut(problem))
        self.wait()

        self.next_section(skip_animations=False)

        # ============================================================
        # FASE 2  —  NORMALIZACIÓN  (∫ P = 1  →  A = 2)
        # ============================================================

        L1 = MathTex(r"\int_{0}^{\infty}", r"P(x)", r"\,dx = 1")
        L2 = MathTex(r"\implies", r"\int_{0}^{\infty}", r"A", "e^{-2x}", r"\,dx = 1")
        L3 = MathTex(r"\implies", r"A", r"\int_{0}^{\infty}", r"e^{-2x} \, dx = 1")
        L4 = MathTex(
            r"\implies",
            r"A",
            r"\left[ -\frac{1}{2} e^{-2x} \right]_{0}^{\infty}",
            r"= 1",
        )
        L5 = MathTex(r"\implies", r"-\frac{A}{2}", r"(0 - 1)", r"= 1")
        L6 = MathTex(r"\implies", r"\frac{A}{2}", r"= 1")
        L7 = MathTex(r"\implies", r"A", r"= 2")

        L1.move_to(ORIGIN)
        self.play(Write(L1))
        self.wait()

        L2.next_to(L1, DOWN, buff=0.4)
        self.play(TransformMatchingTex(L1.copy(), L2))
        self.wait()

        L3.next_to(L2, DOWN, buff=0.4)
        self.play(TransformMatchingShapes(L2.copy(), L3))
        self.wait()

        #
        L4.next_to(L3, DOWN, buff=0.4)
        # m34 = L3.copy()
        # self.play(TransformMatchingShapes(m34, L4))
        # self.wait()

        for l3, l4 in zip(L3, L4):
            self.play(TransformMatchingShapes(l3, l4))
            self.wait(0.5)

        self.next_section(skip_animations=True)

        L5.next_to(L4, DOWN, buff=0.4)
        self.play(Write(L5))
        self.wait()

        L6.next_to(L5, DOWN, buff=0.4)
        m56 = L5.copy()
        self.play(TransformMatchingShapes(m56, L6))
        self.wait()

        L7.next_to(L6, DOWN, buff=0.4)
        m67 = m56.copy()
        self.play(TransformMatchingShapes(m67, L7))
        self.wait()

        self.play(FadeOut(L1, L3, L5))
        self.wait(0.5)

        # ============================================================
        # FASE 3  —  P(x > 1)
        # ============================================================

        M1 = MathTex(r"P(x > 1)", r" = ", r"\int_{1}^{\infty}", r"2 e^{-2x}", r"\,dx")
        M2 = MathTex(
            r"P(x > 1)",
            r" = ",
            r"2",
            r"\left[ -\frac{1}{2} e^{-2x} \right]_{1}^{\infty}",
        )
        M3 = MathTex(
            r"P(x > 1)",
            r" = ",
            r"-\left( \lim_{x \to \infty} e^{-2x} - e^{-2} \right)",
        )
        M4 = MathTex(r"P(x > 1)", r" = ", r"e^{-2}")
        M5 = MathTex(r"P(x > 1)", r" = ", r"e^{-2}", r"\approx", r"0.1353")

        M1.move_to(ORIGIN)
        self.play(Write(M1))
        self.wait()

        M2.next_to(M1, DOWN, buff=0.4)
        n12 = M1.copy()
        self.play(TransformMatchingShapes(n12, M2))
        self.wait()

        M3.next_to(M2, DOWN, buff=0.4)
        self.play(Write(M3))
        self.wait()

        M4.next_to(M3, DOWN, buff=0.4)
        n34 = M3.copy()
        self.play(TransformMatchingShapes(n34, M4))
        self.wait()

        M5.next_to(M4, DOWN, buff=0.4)
        n45 = n34.copy()
        self.play(TransformMatchingShapes(n45, M5))
        self.wait()

        self.play(FadeOut(M1, n12, M3, n34, M4, n45))
        self.wait()

        # ============================================================
        # FASE 4  —  RESPUESTA FINAL
        # ============================================================

        ans1 = MathTex(r"A = 2", font_size=48)
        ans2 = MathTex(r"P(x > 1) = e^{-2} \approx 0.1353", font_size=48)

        box1 = RoundedRectangle(
            corner_radius=0.2,
            width=ans1.width + 1.0,
            height=ans1.height + 0.6,
            color=YELLOW,
        ).move_to(ans1)

        box2 = RoundedRectangle(
            corner_radius=0.2,
            width=ans2.width + 1.0,
            height=ans2.height + 0.6,
            color=GREEN,
        ).move_to(ans2)

        pair1 = VGroup(ans1, box1)
        pair2 = VGroup(ans2, box2)

        pair2.next_to(pair1, DOWN, buff=0.6)
        final = VGroup(pair1, pair2)
        final.move_to(ORIGIN)

        self.play(Write(ans1), Create(box1))
        self.wait()
        self.play(Write(ans2), Create(box2))
        self.wait()
