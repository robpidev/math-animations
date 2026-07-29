from manim import Circle, Create, Scene


class P00Intro(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=False)
        n1 = Circle(radius=1)
        self.play(Create(n1))
        self.wait()
