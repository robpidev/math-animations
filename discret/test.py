# num = 3
# print("par" if num % 2 == 0 else "impar")
# print(f"{ord(' '):8b}")

from manim import RED, Circle, Scene, Text, Transform, Write

color = [255, 0, 2]


class Test(Scene):
    def construct(self):
        t = Text("Hello")

        self.play(Write(t))
        c = Circle().set_fill(RED, 1)
        self.play(Transform(t, c))
        self.wait()
