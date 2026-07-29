import numpy as np
from manim import (
    DOWN,
    RIGHT,
    UP,
    Create,
    FadeOut,
    MathTex,
    ReplacementTransform,
    Scene,
    SurroundingRectangle,
    Text,
    Transform,
    TransformFromCopy,
    TransformMatchingShapes,
    Write,
)

font = "JetBrainsMono Nerd Font"


def factorial(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact *= i
    return fact


def exp_tex(x, m):
    tex = "\\frac{" + str(x) + "^0}{0!}"

    if m <= 6:
        for i in range(1, m + 1):
            tex += " + \\frac{" + str(x) + "^{" + str(i) + "}}{" + str(i) + "!}"
    else:
        tex += "+ \\cdots + "

        for i in range(m - 2, m + 1):
            tex += " + \\frac{" + str(x) + "^{" + str(i) + "}}{" + str(i) + "!}"

    return tex


def exp_value(x, m):
    e = 1
    for i in range(1, m + 1):
        e += x**i / factorial(i)
    return e


class Exp(Scene):
    def construct(self):

        # self.next_section(skip_animations=True)
        self.wait()
        exp = MathTex("e^x").scale(3)
        self.play(Write(exp))

        self.wait()

        exp_taylor = MathTex(
            "e^x",
            "=",
            "1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + \\frac{x^5}{5!}"
            + " + \\cdots",
        ).scale(1.5)

        self.play(TransformMatchingShapes(exp, exp_taylor[0]))
        self.play(Write(exp_taylor[1]))
        self.play(Write(exp_taylor[2]), run_time=5)
        self.wait()

        exp_taylor_alt = MathTex(
            "e^x",
            "=",
            "\\frac{1}{0!} + \\frac{x}{1!} + \\frac{x^2}{2!} + \\frac{x^3}{3!}"
            + " + \\frac{x^4}{4!} + \\frac{x^5}{5!} + \\cdots",
        ).scale(1.5)

        self.play(
            TransformMatchingShapes(
                exp_taylor,
                exp_taylor_alt,
            )
        )

        self.wait()

        exp_taylor_sum = MathTex(
            "e^x",
            "=",
            "\\sum_{n=0}^\\infty \\frac{x^n}{n!}",
        ).scale(2)

        self.wait()

        self.play(TransformMatchingShapes(exp_taylor_alt, exp_taylor_sum))
        self.wait()

        # === Factorial ===
        rect = SurroundingRectangle(exp_taylor_sum[2][-2:])
        self.play(Create(rect))

        factorial = (
            MathTex("n!", "=", "n \\cdot (n-1) \\cdot (n-2) \\cdots 1")
            .scale(2)
            .shift(DOWN * 2)
        )
        self.play(TransformMatchingShapes(exp_taylor_sum[2][-2:].copy(), factorial[0]))
        self.wait()
        self.play(Write(factorial[1]))
        self.wait()
        self.play(TransformFromCopy(factorial[0], factorial[2]), path_arc=np.pi / 2)
        self.wait()

        factorial_example = (
            MathTex(
                "5!",
                "=",
                "5 \\cdot 4 \\cdot 3 \\cdot 2 \\cdot 1",
                "=",
                "120",
            )
            .scale(2)
            .move_to(factorial)
        )

        # self.next_section(skip_animations=False)
        self.play(ReplacementTransform(factorial, factorial_example[:-2]))
        self.wait()
        self.play(Write(factorial_example[-2]))
        self.play(
            ReplacementTransform(
                factorial_example[2:-2].copy(),
                factorial_example[-1],
                path_arc=np.pi / 2,
            )
        )
        self.wait()

        self.play(FadeOut(rect, factorial_example))

        # === Taylor Example ===
        self.wait()

        # self.next_section(skip_animations=False)

        exp_taylor_sup = MathTex(
            "e^x",
            "\\approx",
            "\\sum_{n=0}^m \\frac{x^n}{n!}",
        ).scale(2)

        self.play(TransformMatchingShapes(exp_taylor_sum, exp_taylor_sup))
        self.wait()

        exp_taylor_val = MathTex(
            "e^{1}",
            "=",
            "\\sum_{n=0}^m \\frac{1^n}{n!}",
        ).scale(2)

        self.play(Transform(exp_taylor_sup, exp_taylor_val))
        self.wait()

        exp_taylor_m = (
            MathTex(
                "e^{1}",
                "=",
                "\\sum_{n=0}^1 \\frac{1^n}{n!}",
            )
            .scale(1.5)
            .to_edge(UP)
        )
        # self.next_section(skip_animations=False)

        e_real = Text(str(np.exp(1)), font=font).scale(0.5).to_edge(RIGHT + UP)
        self.play(Write(e_real))

        self.play(Transform(exp_taylor_sup, exp_taylor_m))
        self.wait()

        e_cal = MathTex(
            "e^{1}",
            "=",
            exp_tex(1, 1),
            "=",
            str(exp_value(1, 1)),
        )

        self.play(TransformFromCopy(exp_taylor_sup, e_cal))
        self.wait()

        e_vl = exp_value(1, 1)
        e_vl -= exp_value(1, 0)

        zeros = str(e_vl).count("0")

        e_cal_last = (
            MathTex(str(exp_value(1, 1)), "-", str(exp_value(1, 0)), "=", str(e_vl))
            .to_edge(DOWN)
            .scale(0.7)
        )

        rect = SurroundingRectangle(e_cal_last[-1][:zeros])
        rect_real = SurroundingRectangle(e_real[:zeros])
        # self.next_section(skip_animations=True)

        for i in range(2, 20):
            self.play(
                Transform(
                    exp_taylor_sup,
                    MathTex(
                        "e^{1}",
                        "=",
                        "\\sum_{n=0}^{" + str(i) + "}\\frac{1^n}{n!}",
                    )
                    .scale(1.5)
                    .move_to(exp_taylor_sup),
                )
            )
            self.play(
                Transform(
                    e_cal,
                    MathTex(
                        "e^{1}",
                        "=",
                        exp_tex(1, i),
                        "=",
                        str(exp_value(1, i)),
                    ),
                )
            )

            # === zerores ===
            self.play(
                Transform(
                    e_cal_last,
                    MathTex(
                        str(f"{exp_value(1, i):0.16f}"),
                        "-",
                        str(f"{exp_value(1, i - 1):0.16f}"),
                        "=",
                        str(f"{exp_value(1, i) - exp_value(1, i - 1):0.16f}"),
                    )
                    .scale(0.7)
                    .to_edge(DOWN),
                )
            )

            e_vl = exp_value(1, i)
            e_vl -= exp_value(1, i - 1)

            zeros = str(f"{e_vl:0.16f}").count("0")

            # === rect ===
            self.play(
                Transform(
                    rect,
                    SurroundingRectangle(e_cal_last[-1][: zeros + 1]),
                )
            )

            # === rect_real ===
            self.play(
                Transform(
                    rect_real,
                    SurroundingRectangle(e_real[: zeros + 1]),
                )
            )
            self.wait(0.5)
