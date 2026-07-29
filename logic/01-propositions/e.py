from manim import MathTex, Scene


class E(Scene):
    def construct(self):
        t = MathTex(r"p \leftrightarrow q \equiv", r"(p\to q)\wedge (q \to p)")
        t.scale(2.3)
        self.add(t)
        print(r"\n")
