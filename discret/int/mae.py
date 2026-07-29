from manim import (
    BLUE,
    PINK,
    PURPLE,
    YELLOW,
    FadeOut,
    Scene,
    Text,
    Transform,
    VGroup,
    Write,
    UP,
)


class MAE(Scene):
    def construct(self):
        self.wait()
        mae = Text("Hello, Mae :3").scale(2)
        self.play(Write(mae))
        self.wait()
        self.play(mae.animate.to_edge(UP))

        text = Text("You").scale(2)

        self.play(Write(text))
        self.wait(0.5)
        self.play(Transform(text, Text("are", color=PURPLE).scale(2)))
        self.wait(0.5)
        self.play(Transform(text, Text("in", color=BLUE).scale(2)))
        self.wait(0.5)
        self.play(Transform(text, Text("My", color=YELLOW).scale(2)))
        self.wait(0.5)
        self.play(
            Transform(VGroup(text, mae[6:-2]), Text("❤", color=PINK).scale(10)),
            FadeOut(mae[:6], mae[-2:]),
        )
        self.wait()
