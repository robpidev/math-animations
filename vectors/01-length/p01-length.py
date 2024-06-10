from manim import *
from mobj.mobjets import number_plane
from funcs.vec2D_tex import *
from funcs.vec_algebra import *



class P01_Length(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)
        plane = number_plane()
        self.play(Create(plane))
        self.wait()

        r = Vector([4, 3], color=YELLOW)
        rl = MathTex(r"\mathbf{r}", color=YELLOW).move_to([1.5, 2, 0])

        lx = DashedLine(ORIGIN, [4, 0, 0], color=RED)
        ly = DashedLine([4, 0, 0], [4, 3, 0], color=GREEN)

        eq = MathTex(r"\mathbf{r} = ", vec([4, 3]))
        eq.move_to([2.5, -2.5, 0])

        self.play(Create(r), Write(rl))
        self.wait()

        self.play(Create(lx), Create(ly))

        self.play(
            TransformMatchingShapes(rl.copy(), eq[0]),
            Write(eq[1][0]), Write(eq[1][-1]),
        )

        self.wait()
        self.play(TransformFromCopy(lx, eq[1][1]))
        self.play(TransformFromCopy(ly, eq[1][2]))
        self.wait()

        rx = Vector([4, 0], color=RED)
        ry = Vector([0, 3], color=GREEN).shift(4*RIGHT)
        rxl = MathTex("4", color=RED).next_to(rx, DOWN)
        ryl = MathTex("3", color=GREEN).next_to(ry, RIGHT)

        self.play(Create(rx))
        self.wait()
        self.play(TransformFromCopy(eq[1][1], rxl))
        self.wait()

        self.play(Create(ry))
        self.wait()
        self.play(TransformFromCopy(eq[1][2], ryl))
        self.wait()

        
        l4 = Arrow(ORIGIN, [4/7 * 4, 4/7 * 3, 0], buff=0, color=YELLOW)
        l3 = Arrow([4/7 * 4, 4/7 * 3, 0], [4, 3, 0], buff=0, color=YELLOW)

        self.play(
            Transform(rx, l4),
            Transform(ry, l3)
        )

        self.play(FadeOut(rx, ry))
        self.wait()
        square = Square(0.5, stroke_width=1).move_to([3.75, 0.25, 0])
        # square = DashedVMobject(square)
        self.play(Create(square))
        self.wait()

        pitagoras = MathTex(
            "r^2", "=", "4^2", "+", "3^2",
            "=", "25",
        )

        result = MathTex(r"\implies", "r", "=", r"\sqrt{25}", "=", "5" )

        VGroup(pitagoras, result).arrange(DOWN).move_to([-3, 2, 0])

        self.play(TransformFromCopy(rl, pitagoras[0]))
        self.wait()
        self.play(Write(pitagoras[1]))
        self.play(
            TransformMatchingShapes(rxl.copy(), pitagoras[2]),
            Write(pitagoras[3]),
            TransformMatchingShapes(ryl.copy(), pitagoras[4]),
        )

        self.wait()
        self.play(Write(pitagoras[5]))
        self.play(TransformFromCopy(pitagoras[2:5], pitagoras[-1]))
        self.wait()
        
        self.play(Write(result[0]))
        self.play(
            TransformFromCopy(pitagoras[0][0], result[1]),
            TransformFromCopy(pitagoras[1], result[2]),
            TransformMatchingShapes(
                pitagoras[-1].copy(),
                result[3][2:],
                fade_transform_mismatches=True
            ),
            TransformFromCopy(pitagoras[0][1], result[3][0:2])
        )
        self.play(Write(result[4]))
        self.play(TransformFromCopy(result[3], result[-1]))
        self.wait()

        

        brace = Brace(r, direction=r.copy().rotate(90 * DEGREES).get_unit_vector())
        bracel = brace.get_tex("5")
        self.wait()
        
        self.play(
            FadeOut(result[:-1], pitagoras),
            ReplacementTransform(result[-1], brace),
            ReplacementTransform(rl, bracel)
        )

        self.wait()

        rl_alt = MathTex(r"\mathbf{r}=" + vec(["x", "y"]), color=YELLOW).move_to(rl.get_center())
        rxl_alt = MathTex("x", color=RED).next_to(lx, DOWN)
        ryl_alt = MathTex("y", color=GREEN).next_to(ly, RIGHT)

        self.play(
            ReplacementTransform(Group(brace, bracel), rl_alt),
            Transform(rxl, rxl_alt),
            Transform(ryl, ryl_alt),
            FadeOut(eq)
        )
        self.wait()

        fig = VGroup(rxl, ryl, rl_alt, r, lx, ly, square)
        self.play(FadeOut(plane), fig.animate.move_to([4, 0, 0]))
        self.wait()


        #NOTE:  ================ def longitud =============

        l1 = MathTex(
            r"\text{Def. La \textit{\textbf{longitud}} (o \textit{\textbf{norma}})}",
        )

        l2 = MathTex(
            r"\text{de un vector } ",
            r"\mathbf{r} =" + vec(["x", "y"]) + "\in \mathbb{R}^2",
        )

        l3 = MathTex(
            r"\text{es un escalar } \|\mathbf{r}\| \text{ definido por }"
        )

        eq = MathTex(r"\|\mathbf{r}\|", "=", r"\sqrt{x^2 + y^2}")

        enun = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT)
        df = VGroup(enun, eq).arrange(DOWN, buff=1).shift(LEFT * 2.5)

        self.play(Write(l1))
        self.wait()
        self.play(Write(l2))
        self.wait()
        self.play(Write(l3))
        self.wait()
        self.play(Write(eq))
        self.wait()
        
        #NOTE: ===================== ||cR|| =====================
        self.play(
            Create(plane),
            FadeOut(df, square, lx, ly, rxl, ryl),
            r.animate.move_to([2, 1.5, 0])
        )
        self.wait()

        dp = [-2, 1]
        r1 = Vector(dp, color=YELLOW)
        r1l = MathTex(r"\mathbf{r} = ", vec(dp),
                      color=YELLOW).move_to([-1, 2, 0])
        
        self.play(
            ReplacementTransform(r, r1),
            TransformMatchingShapes(rl_alt, r1l,
                                    transform_mismatches=True)
        ) 
        self.wait()

        mod_r1 = MathTex(
            r"\implies \|\mathbf{r}\| =", "\sqrt{(-2)^2 + 1^2}",
            "=", "\sqrt{5}"
        ).next_to(r1l, RIGHT)
        self.play(Write(mod_r1[0][0:2]))
        self.play(TransformMatchingShapes(
            r1l[0].copy(), mod_r1[0][2:],
            fade_transform_mismatches=True
        ))

        self.play(TransformMatchingShapes(
            r1l[1].copy(), mod_r1[1],
            fade_transform_mismatches=True,
            path_arc=PI/2
        ))

        self.play(Write(mod_r1[2]))
        self.play(TransformMatchingShapes(
            mod_r1[1].copy(), mod_r1[-1],
            transform_mismatches=True,
            path_arc=PI/2
        ))

        self.wait()

        dq = vec_scale(-3, dp)

        r1_3 = Vector(dq, color=GREEN)
        r1_3l = MathTex(
            r"-3\mathbf{r}", "=",
            vec_scalar_comps("-3", ["(-2)", 1]),
            color=GREEN
        ).move_to([4, -0.5, 0])

        self.play(
            TransformMatchingShapes(r1l.copy(), r1_3l,
                                    fade_transform_mismatches=True)
        )

        

        self.wait()
        self.play(Create(r1_3))
        self.wait()

        fig = VGroup(plane, r1, r1_3, r1l, r1_3l, mod_r1)
        self.play(
            fig.animate.scale(0.5).move_to([3, -2, 0])
        )
        self.wait()


        mtex = r"\|-3\mathbf{r}\|"

        l1 = MathTex(mtex, "=", r"\sqrt{(-3\cdot(-2))^2 + (-3\cdot1)^2}")
        l2 = MathTex(mtex, "=", r"\sqrt{(-3)^2 \cdot (-2)^2 + (-3)^2\cdot1^2}")
        l3 = MathTex(mtex, "=", r"\sqrt{(-3)^2\cdot \left(4 + 1\right)}")
        l4 = MathTex(mtex, "=", r"\sqrt{(-3)^2}\sqrt{5}")
        l5 = MathTex(mtex, "=", r"|-3|\sqrt{5}")


        mod = VGroup(l1, l2, l3, l4, l5)
        mod.arrange(DOWN, aligned_edge=LEFT).move_to([-1, 1, 0])
        self.wait()

        self.play(Write(l1[0]))
        self.play(Write(l1[1]))
        self.play(TransformMatchingShapes(
            r1_3l[-1].copy(), l1[-1],
            fade_transform_mismatches=True
        ))
        self.wait()

        for i in range(1, len(mod)):
            self.play(Write(mod[i][-2]))
            self.play(TransformMatchingShapes(
                mod[i-1][-1].copy(), mod[i][-1],
                transform_mismatches=True
            ))
            self.wait()
        # self.play(Write(l2[-2]))
        # self.play(TransformMatchingShapes(
        #     l1[-1].copy(), l2[-1],
        #     transform_mismatches=True
        # ))
        # self.wait()
        # self.play(Write(l3[-2]))
        # self.play(TransformMatchingShapes(
        #     l1[-2]
        # ))

        result = MathTex(
            r"\implies",
            r"\|-3\mathbf{r}\|", "=",
            r"|-3|\|\mathbf{r}\|", "=|-3|\sqrt{5}"
        ).move_to([0, -2.5, 0])

        self.play(
            fig.animate.scale(2).move_to(ORIGIN),
            ReplacementTransform(l1[0:2], result[1]),
            ReplacementTransform(l5[-1], result[-1]),
            Write(result[0]),
            Write(result[2:-1]),
            FadeOut(l1[2:], l2, l3, l4, l5[:-1])
        )

        self.play(FadeOut(fig[1:], result))

        #NOTE: =========== generalizando for all vector =============
        dp = [1.5, 1]
        r = Vector(dp, color=RED).set_z_index(2)
        rl = MathTex(
            r"\mathbf{r} &= " + vec(["x", "y"]), r"\\\implies",
            "\|\mathbf{r}\| &= \sqrt{x^2 + y^2}",
            color=RED
        ).move_to([-2, 0, 0])

        dpe = vec_scale(2.7, dp)
        re = Vector(dpe, color=GREEN).set_z_index(1)
        rel = MathTex(
            r"c\mathbf{r}&=" + vec_scalar("c", ["x", "y"]), r"\\\implies",
            r"\|c\mathbf{r}\|", r"&=", r"|c|\|\mathbf{r}\| \\", 
            r"&=",  "|c|\sqrt{x^2 + y^2}",
            color=GREEN
        ) .move_to([4, 0, 0])


        self.play(Create(r), Write(rl[0]))
        self.wait()
        self.play(Write(rl[1]), TransformMatchingShapes(
            rl[0].copy(), rl[-1], transform_mismatches=True
        ))
        self.wait()

        self.play(
            Create(re),
            TransformMatchingShapes(
                rl[0].copy(), rel[0],
                fade_transform_mismatches=True
            )
        )
        self.wait()
        self.play(
            Write(rel[1]),
            TransformMatchingShapes(
                rel[0][0:2].copy(), rel[2],
                fade_transform_mismatches=True
            )
        )
        self.play(Write(rel[3]))
        self.play(TransformMatchingShapes(
            rel[2].copy(), rel[4],
            fade_transform_mismatches=True
        ))
        self.play(Write(rel[5]))
        self.play(TransformMatchingShapes(
            rel[4].copy(), rel[6],
            transform_mismatches=True
        ))

        self.wait()
        self.play(FadeOut(rl, rel))

        br = Brace(r, direction=r.copy().rotate(PI/2).get_unit_vector())
        brl = br.get_tex(r"\|\mathbf{r}\|")


        bre = Brace(re, direction=re.copy().rotate(-PI/2).get_unit_vector())
        brel = bre.get_tex(r"|c|\|\mathbf{r}\|")
        self.play(Write(brl), Write(br), Write(brel), Write(bre))
        self.wait()

        fig = VGroup(r, re, br, brl, bre, brel)
        self.play(
            FadeOut(plane),
            fig.animate.scale(0.7).move_to([5, 0, 0])
        )

        self.wait()

        l1 = MathTex(
            r"c\in\mathbb{R}",
            r"\wedge \mathbf{r}=" + vec(["x", "y"]) + r"\in\mathbb{R}^2,"
        )

        l2 = MathTex(
            r"\implies", r"\|c\mathbf{r}\|",
            "=", r"\left\|" + vec(["cx", "cy"]) + r"\right\|",
            "=", r"\sqrt{(cx)^2 + (cy)^2}",
        )

        l3 = MathTex(
            r"\implies", r"\|c\mathbf{r}\|",
            "=", r"\sqrt{c^2x^2 + c^2y^2}",
            "=", r"\sqrt{c^2(x^2 + y^2)}"
        )

        l4 = MathTex(
            r"\implies", r"\|c\mathbf{r}\|",
            "=", r"\sqrt{c^2}", "\sqrt{x^2 + y^2}",
            "=", r"|c|", r"\|\mathbf{r}\|"
        )

        proof = VGroup(l1, l2, l3, l4)
        proof.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        proof.move_to([-2, 0,0])

        self.play(Write(l1[0]))
        self.wait()
        self.play(Write(l1[1]))
        self.wait()


        self.play(
            Write(l2[0]),
            TransformMatchingShapes(
                VGroup(l1[0][0], l1[1][1]).copy(), l2[1],
                fade_transform_mismatches=True
            )
        )
        self.play(Write(l2[2]))

        self.play(
            TransformMatchingShapes(
                VGroup(l2[1][1], l1[1][3:7]).copy(), l2[3][4:-4],
                transform_mismatches=True
            )
            # TransformFromCopy(l2[0][2:-2], l2[3][2:-2])
        )
        self.wait()
        self.play(
            TransformMatchingShapes(
                l2[1][0].copy(), l2[3][:4],
                fade_transform_mismatches=True
            ),
            TransformMatchingShapes(
                l2[1][-1].copy(), l2[3][-4:],
                fade_transform_mismatches=True
            )
        )

        self.play(Write(l2[4]))
        self.play(TransformMatchingShapes(
            l2[3].copy(), l2[5],
            fade_transform_mismatches=True
        ))
        self.wait()

        self.play(Write(l3[2]))

        self.play(
            TransformMatchingShapes(
                l2[-1][2:].copy(), l3[3][2:],
            ),
            ReplacementTransform(
                l2[-1][:2].copy(), l3[3][:2]
            )
        )
        self.wait()
        self.play(Write(l3[4]))
        self.play(
            TransformMatchingShapes(
                l3[3][2:].copy(), l3[5][2:],
                path_arc = PI/2
            ),
            ReplacementTransform(l3[3][:2].copy(), l3[5][:2])
        )
        self.wait()

        self.play(Write(l4[2]))
        self.play(
            TransformMatchingShapes(
                l3[-1].copy(), l4[3:5],
            )
        )

        self.wait()
        self.play(Write(l4[5]))
        self.play(TransformMatchingShapes(
            l4[3].copy(), l4[6],
            fade_transform_mismatches=True,
            path_arc = PI/2
        ))
        self.wait()
        self.play(ReplacementTransform(
            l4[4].copy(), l4[7],
            path_arc = PI/2
        ))

        self.wait()

        self.next_section(skip_animations=False)
        result = MathTex(
            r"\|c\mathbf{r}\|=",
            r"|c|\|\mathbf{r}\|"
        )

        l1c = l1.copy()
        VGroup(l1c, result).arrange(DOWN, buff=0.2).move_to(ORIGIN)


        self.play(
            FadeOut(proof),
            ReplacementTransform(l2[1:3], result[0]),
            ReplacementTransform(l5[-1], result[1]),
            ReplacementTransform(l1,l1c)
        )



