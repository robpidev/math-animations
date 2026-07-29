from manim import (
    BLUE_D,
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    FadeOut,
    MathTex,
    Scene,
    Square,
    SurroundingRectangle,
    Text,
    VGroup,
    Write,
)


def create_ball(color, label, size=0.35):
    c = Circle(radius=size)
    c.set_fill(color, opacity=1)
    c.set_stroke(WHITE, width=1.5)
    lbl = Text(label, font_size=18).next_to(c, DOWN, buff=0.15)
    return VGroup(c, lbl)


class P01RandomVar(Scene):
    def construct(self):
        self.wait()

        # ========================================================
        # SECTION 1  —  BALLS  (random variable, events are words)
        # ========================================================
        # self.next_section(skip_animations=True)

        label1 = Text("V. Aleatoria", font_size=22, color=YELLOW).to_edge(UP + LEFT)
        self.play(Write(label1))
        self.wait()

        balls = VGroup(
            create_ball(RED, "roja"),
            create_ball(RED, "roja"),
            create_ball(RED, "roja"),
            create_ball(WHITE, "blanca"),
            create_ball(WHITE, "blanca"),
            create_ball(BLUE_D, "azul"),
            create_ball(BLUE_D, "azul"),
        )
        balls.arrange(RIGHT, buff=0.5).shift(UP * 0.5)

        for b in balls:
            self.play(Create(b[0]), run_time=0.2)
        self.wait(0.3)
        for b in balls:
            self.play(Write(b[1]), run_time=0.15)
        self.wait()

        space_set = MathTex(
            r"S = \{\text{roja}, \text{blanca}, \text{azul}\}", font_size=28
        )
        space_set.next_to(balls, DOWN, buff=0.6)
        self.play(Write(space_set))
        self.wait()
        self.play(FadeOut(space_set))
        self.wait()

        # --- Show each color group and its probability in a row ---
        red_group = VGroup(balls[0][0], balls[1][0], balls[2][0])
        white_group = VGroup(balls[3][0], balls[4][0])
        blue_group = VGroup(balls[5][0], balls[6][0])

        prob_red = MathTex(r"P(\text{roja}) = \frac{3}{7}", font_size=30, color=RED)
        prob_white = MathTex(
            r"P(\text{blanca}) = \frac{2}{7}", font_size=30, color=WHITE
        )
        prob_blue = MathTex(r"P(\text{azul}) = \frac{2}{7}", font_size=30, color=BLUE_D)

        prob_row = VGroup(prob_red, prob_white, prob_blue).arrange(RIGHT, buff=0.8)
        prob_row.next_to(balls, DOWN, buff=0.6)

        for group, prob, color in [
            (red_group, prob_red, RED),
            (white_group, prob_white, WHITE),
            (blue_group, prob_blue, BLUE_D),
        ]:
            rect = SurroundingRectangle(group, buff=0.15, color=color)
            self.play(Create(rect))
            self.wait(0.3)
            self.play(Write(prob))
            self.wait(0.5)
            self.play(FadeOut(rect))

        sum_tex = MathTex(
            r"\frac{3}{7} + \frac{2}{7} + \frac{2}{7} = \frac{7}{7} = 1",
            font_size=28,
        )
        sum_tex.next_to(prob_row, DOWN, buff=0.4)
        self.play(Write(sum_tex))
        self.wait()

        not_num = Text("Los eventos NO son n\u00fameros", font_size=26, color=GREEN)
        not_num.next_to(sum_tex, DOWN, buff=0.4)
        self.play(Write(not_num))
        self.wait()

        self.play(FadeOut(label1, balls, prob_row, sum_tex, not_num))
        self.wait()

        # ========================================================
        # SECTION 2  —  DICE  (random number, events are numbers)
        # ========================================================
        # self.next_section(skip_animations=True)

        label2 = Text("N\u00famero Aleatorio", font_size=22, color=YELLOW).to_edge(
            UP + LEFT
        )
        self.play(Write(label2))
        self.wait()

        faces = VGroup()
        for n in range(1, 7):
            sq = Square(side_length=0.8)
            sq.set_fill(WHITE, opacity=0.15)
            sq.set_stroke(WHITE, width=1.5)
            num = MathTex(str(n), font_size=36).move_to(sq)
            faces.add(VGroup(sq, num))

        faces.arrange_in_grid(2, 3, buff=0.4).shift(UP * 0.5)
        for f in faces:
            self.play(Create(f[0]), Write(f[1]), run_time=0.25)
        self.wait()

        a_set = MathTex(r"A = \{1, 2, 3, 4, 5, 6\}", font_size=30)
        a_set.next_to(faces, DOWN, buff=0.6)
        self.play(Write(a_set))
        self.wait()

        dice_probs = MathTex(
            r"P(1) = P(2) = \cdots = P(6) = \frac{1}{6}", font_size=30
        )
        dice_probs.next_to(a_set, DOWN, buff=0.4)
        self.play(Write(dice_probs))
        self.wait()

        dice_sum = MathTex(r"6 \times \frac{1}{6} = 1", font_size=28)
        dice_sum.next_to(dice_probs, DOWN, buff=0.4)
        self.play(Write(dice_sum))
        self.wait()

        yes_num = Text(
            "Los eventos S\u00cd son n\u00fameros", font_size=26, color=GREEN
        )
        yes_num.next_to(dice_sum, DOWN, buff=0.4)
        self.play(Write(yes_num))
        self.wait()

        self.play(FadeOut(label2, faces, a_set, dice_probs, dice_sum, yes_num))
        self.wait()

        # ========================================================
        # SECTION 3  —  FORMAL DEFINITION
        # ========================================================
        # self.next_section(skip_animations=True)

        # --- A = {aj | j = 1..NA} ---
        line1 = MathTex(
            r"A = \{a_j \mid j = 1, \ldots, N_A\}", font_size=36
        )
        line1.shift(UP * 2)
        self.play(Write(line1))
        self.wait()

        # --- 0 <= P(aj) <= 1 ---
        line2 = MathTex(r"0 \leq P(a_j) \leq 1", font_size=36)
        line2.next_to(line1, DOWN, buff=0.5)
        self.play(Write(line2))
        self.wait()

        # --- impossible = 0, certain = 1 ---
        imp = MathTex(
            r"P(\emptyset) = 0", r"\quad\text{(evento imposible)}", font_size=30
        )
        cert = MathTex(r"P(S) = 1", r"\quad\text{(evento cierto)}", font_size=30)
        imp.next_to(line2, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.5)
        cert.next_to(imp, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(imp), Write(cert))
        self.wait()

        # --- sum of all = 1 ---
        sum_all = MathTex(
            r"\sum_{j=1}^{N_A} P(a_j) = 1", font_size=36
        )
        sum_all.next_to(cert, DOWN, buff=0.4)
        self.play(Write(sum_all))
        self.wait()

        # --- Simplified notation ---
        simplify_text = MathTex(
            r"\text{To simplify notation we will often write this equation as}",
            font_size=26,
        )
        simplify_sum = MathTex(r"\sum_a P(a) = 1", font_size=36, color=YELLOW)
        suppress_text = MathTex(
            r"\text{suppressing explicit mention of the number}"
            r"\ \text{of elementary events}",
            font_size=22,
        )
        simplify_text.next_to(sum_all, DOWN, buff=0.4)
        simplify_sum.next_to(simplify_text, DOWN, buff=0.15)
        suppress_text.next_to(simplify_sum, DOWN, buff=0.15)
        self.play(Write(simplify_text))
        self.wait(0.3)
        self.play(Write(simplify_sum))
        self.wait(0.3)
        self.play(Write(suppress_text))
        self.wait()

        # --- Discrete random variable ---
        dv_line = MathTex(
            r"\text{Si } N_A \text{ es finito o numerable} \implies",
            font_size=28,
        )
        dv_label = MathTex(
            r"\text{variable aleatoria } \mathbf{discreta}",
            font_size=32,
            color=YELLOW,
        )
        dv_line.next_to(sum_all, DOWN, buff=0.4)
        dv_label.next_to(dv_line, DOWN, buff=0.2)
        self.play(Write(dv_line), Write(dv_label))
        self.wait()

        # --- Random number ---
        rn_line = MathTex(
            r"\text{Si los eventos son n\u00fameros} \implies",
            font_size=28,
        )
        rn_label = MathTex(
            r"\text{se llama n\u00famero aleatorio}",
            font_size=32,
            color=YELLOW,
        )
        rn_line.next_to(dv_label, DOWN, buff=0.4)
        rn_label.next_to(rn_line, DOWN, buff=0.2)
        self.play(Write(rn_line), Write(rn_label))
        self.wait()

        # --- Final comparison boxes ---
        self.play(FadeOut(
            line1, line2, imp, cert, sum_all,
            simplify_text, simplify_sum, suppress_text,
            dv_line, dv_label, rn_line, rn_label
        ))
        self.wait()

        left = VGroup(
            Text("Pelotas", font_size=24, color=RED),
            Text("{roja, blanca, azul}", font_size=20),
            Text("NO son n\u00fameros", font_size=20, color=GREEN),
            Text("\u2192 Variable Aleatoria", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.25).shift(LEFT * 3 + UP * 0.5)

        left_box = SurroundingRectangle(left, buff=0.25, color=WHITE)

        right = VGroup(
            Text("Dado", font_size=24, color=BLUE_D),
            Text("{1, 2, 3, 4, 5, 6}", font_size=20),
            Text("S\u00cd son n\u00fameros", font_size=20, color=GREEN),
            Text("\u2192 N\u00famero Aleatorio", font_size=22, color=YELLOW),
        ).arrange(DOWN, buff=0.25).shift(RIGHT * 3 + UP * 0.5)

        right_box = SurroundingRectangle(right, buff=0.25, color=WHITE)

        self.play(Write(left_box), Write(left))
        self.play(Write(right_box), Write(right))
        self.wait(2)

        self.play(FadeOut(left_box, left, right_box, right))
        self.wait()
