from manim import (
    BLUE,
    GREEN,
    RED,
    YELLOW,
    Circle,
    Create,
    Scene,
    Square,
    Star,
    Text,
    Triangle,
    Write,
)
from utils.panels import PanelLayout


class DemoScene(Scene):
    def construct(self):
        layout = PanelLayout(n_panels=4)  # "auto": detecta landscape/portrait solo
        borders = layout.show_borders()

        shapes = [
            Circle(color=BLUE),
            Square(color=RED),
            Triangle(color=GREEN),
            Star(color=YELLOW),
        ]
        for i, shape in enumerate(shapes):
            layout.fit(shape, i)

        self.play(Create(borders))
        self.play(*[Create(s) for s in shapes])
        self.wait()


class DemoHeaderScene(Scene):
    """3 paneles: título arriba (o arriba-izq) + p1 + p2.
    panel0 = titulo, panel1 = p1, panel2 = p2."""

    def construct(self):
        layout = PanelLayout(n_panels=3, variant="header")
        borders = layout.show_borders()

        titulo = Text("Ejercicios, problemas y otros", weight="BOLD")
        p1_content = Square(color=RED)
        p2_content = Circle(color=BLUE)

        layout.fit(titulo, 0)
        layout.fit(p1_content, 1)
        layout.fit(p2_content, 2)

        self.play(Create(borders))
        self.play(Write(titulo), Create(p1_content), Create(p2_content))
        self.wait()
