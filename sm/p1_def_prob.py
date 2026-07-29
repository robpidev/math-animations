import random

from manim import (
    DOWN,
    IN,
    LEFT,
    OUT,
    PI,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Create,
    Dot,
    FadeIn,
    FadeOut,
    MathTex,
    Rotate,
    Scene,
    Square,
    SurroundingRectangle,
    TransformFromCopy,
    VGroup,
    Write,
)


def die_face(n):
    """Create a 2D die face centered at origin in the xy-plane"""
    square = Square(side_length=2, stroke_width=4, color=WHITE)
    dot_positions = {
        1: [(0, 0)],
        2: [(0.5, 0.5), (-0.5, -0.5)],
        3: [(0.5, 0.5), (0, 0), (-0.5, -0.5)],
        4: [(-0.5, 0.5), (0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)],
        5: [(-0.5, 0.5), (0.5, 0.5), (0, 0), (-0.5, -0.5), (0.5, -0.5)],
        6: [(-0.5, 0.5), (0.5, 0.5), (-0.5, 0), (0.5, 0), (-0.5, -0.5), (0.5, -0.5)],
    }
    dots = VGroup(*[Dot(point=[x, y, 0], radius=0.15) for x, y in dot_positions[n]])
    return VGroup(square, dots)


def build_3d_die():
    """Build a 3D die from 6 oriented 2D faces (side-length 2 cube)"""
    props = [
        (1, UP, -PI / 2, RIGHT),
        (6, DOWN, PI / 2, RIGHT),
        (2, OUT, 0, RIGHT),
        (5, IN, PI, UP),
        (3, RIGHT, -PI / 2, UP),
        (4, LEFT, PI / 2, UP),
    ]
    faces = VGroup()
    for n, shift, angle, axis in props:
        face = die_face(n)
        if angle != 0:
            face.rotate(angle, axis=axis)
        face.shift(shift)
        faces.add(face)
    return faces


class DefProb(Scene):
    def construct(self):
        die = build_3d_die()
        self.add(die)

        set_tex = MathTex(r"\mathcal{A} = \{1\}", font_size=40)
        set_tex.next_to(die, DOWN, buff=1.5)
        self.play(Write(set_tex))

        for i in range(2, 7):
            self.play(
                Rotate(die, angle=PI / 3, axis=UP + RIGHT, run_time=0.4),
            )

            num_label = MathTex(str(i), font_size=48, color=YELLOW)
            num_label.next_to(die, UP, buff=0.5)
            self.play(FadeIn(num_label, scale=0.5, run_time=0.15))

            content = ", ".join(str(j) for j in range(1, i + 1))
            new_set_tex = MathTex(
                r"\mathcal{A} = \{" + content + r"\}", font_size=40
            )
            new_set_tex.move_to(set_tex)

            self.play(
                TransformFromCopy(num_label, new_set_tex, run_time=0.6),
                FadeOut(set_tex, run_time=0.3),
                FadeOut(num_label, run_time=0.2),
            )
            set_tex = new_set_tex

        final_n = random.randint(1, 6)
        self.play(
            Rotate(die, angle=PI, axis=UP + OUT, run_time=0.5),
        )
        self.wait(0.5)

        self.play(
            die.animate.scale(0.7).to_edge(LEFT, buff=1.5),
            set_tex.animate.scale(0.7).next_to(die, RIGHT, buff=1).shift(UP * 1.5),
        )

        probs = VGroup()
        for i in range(1, 7):
            prob_tex = MathTex(f"P({i}) = \\frac{{1}}{{6}}", font_size=36)
            if i == final_n:
                prob_tex.set_color(YELLOW)
            probs.add(prob_tex)
        probs.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        probs.next_to(set_tex, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(probs))

        highlight = SurroundingRectangle(probs[final_n - 1], color=YELLOW, buff=0.15)
        self.play(Create(highlight))
        self.wait(2)
