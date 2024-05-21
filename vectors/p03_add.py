from manim import *
from funcs.vec2D_tex import vec_matrix

class Adition(Scene):
    def construct(self):

        # self.next_section(skip_animations=True)

        self.wait()

        plane = NumberPlane(
            background_line_style={
                "stroke_width": 1,
                "stroke_opacity": 0.8
            },
            axis_config={
                "stroke_width": 1,
                "stroke_opacity": 0.8
            },
        )

        self.play(Create(plane))
        self.wait()

        u = Vector([2, 3], color=GREEN)
        v = Vector([4, -2], color=BLUE)
        r = Vector([6, 1], color=RED)

        ul = MathTex(vec_matrix(2, 3)).set_color(GREEN).move_to([0.5, 2, 0])
        vl = MathTex(vec_matrix(4, -2)).set_color(BLUE).move_to([5, 2.5, 0])
        rl = MathTex(vec_matrix(6, 1)).set_color(RED).move_to([3, -0.7, 0])

        vg = VGroup(u, v, r)
        vgt = VGroup(ul, vl, rl)

        self.play(Create(u))
        self.play(Create(v))
        self.wait()

        self.play(v.animate.move_to([4, 2, 0]))
        self.wait()

        self.play(Create(r))
        self.wait()

        for mo in vgt:
            self.play(Write(mo))
            self.wait()


        ux = Vector([2, 0], color=GREEN_A)
        uy = Vector([0, 3], color=GREEN_B)

        vx = Vector([4, 0], color=BLUE_A).move_to([4, 3, 0])
        vy = Vector([0, -2], color=BLUE_B).move_to([2, 2, 0])

        rx = Vector([6, 0], color=RED_A)
        ry = Vector([0, 1], color=RED_B)

        self.play(TransformFromCopy(ul[0][1], ux))
        self.wait()
        self.play(TransformFromCopy(vl[0][1], vx))
        self.wait()

        self.play(vx.animate.move_to([4, 0, 0]))
        self.wait()

        vgx = VGroup(vx, ux)
        self.play(TransformMatchingShapes(vgx, rx))
        self.play(Transform(rx, rl[0][1]))
        self.wait()
        self.remove(rx)

        self.play(TransformFromCopy(ul[0][2], uy))
        self.wait()
        self.play(TransformFromCopy(vl[0][2:4], vy))
        self.wait()

        self.play(vy.animate.move_to([0, 2, 0]))
        self.wait()

        vgy = VGroup(uy, vy)
        self.play(Transform(vgy, ry))
        self.play(vgy.animate.shift(RIGHT*6))
        self.wait(0.5)
        self.play(Transform(vgy, rl[0][-2]))
        self.wait()
        self.remove(vgy)

        self.play(FadeOut(plane))


        # adition of two vectors
        op = MathTex(vec_matrix(2,3), "+", vec_matrix(4, -2), 
                     "=", vec_matrix("2+4", "3+(-2)"),
                     "=", vec_matrix(6, 1),
                     )

        op.move_to([3.5, -2.5, 0])

        self.play(TransformMatchingShapes(ul.copy(), op[0]))
        self.play(Write(op[1]))
        self.play(TransformMatchingShapes(vl.copy(), op[2]))
        self.play(Write(op[3]))
        self.play(Write(op[4][0]), Write(op[4][-1]))
        self.wait()
        self.play(
            TransformMatchingShapes(op[0][1].copy(), op[4][1]),
            TransformMatchingShapes(op[2][1].copy(), op[4][3]),
            TransformFromCopy(op[1], op[4][2]))
        
        self.wait()

        self.play(
            TransformMatchingShapes(op[0][2].copy(), op[4][4]),
            TransformMatchingShapes(op[2][2:4].copy(), op[4][6:10]),
            TransformFromCopy(op[1], op[4][5])
        )
        self.play(Write(op[5]))
        self.play(Write(op[6][0]), Write(op[6][-1]))
        self.play(
            TransformFromCopy(op[4][1:5], op[6][1]),
            TransformFromCopy(op[4][5:10], op[6][2]),
        )
        self.play(op[6].animate.set_color(RED))


        # def de suma
        df = Tex(r"Def. Sea $\mathbf{u}, \mathbf{v} \in \mathbb{R}^2$: ", )
        vecs = MathTex(r"\mathbf{u} =", vec_matrix("u_x", "u_y"),
                       r", \quad \mathbf{v} = ", vec_matrix("v_x", "v_y"))
        text = Tex(r"Se define la adición (+) de $\mathbf{u}$ y $\mathbf{v}$: ")
        add = MathTex(r"\mathbf{u} + \mathbf{v} = ",
                      vec_matrix("u_x", "u_y"), "+",
                      vec_matrix("v_x", "v_y"),"=",
                      vec_matrix("u_x + v_x", "u_y + v_y"))

        defg = VGroup(df, vecs, text, add)
        defg.arrange(DOWN, aligned_edge=LEFT).move_to([-3.5, 0, 0])
        defg.scale(0.8)

        self.play(Write(df))
        self.play(Write(vecs))
        self.play(Write(text))

        self.play(Write(add[0]))
        self.play(TransformMatchingShapes(vecs[1].copy(), add[1]))
        self.play(Write(add[2]))
        self.play(TransformMatchingShapes(vecs[3].copy(), add[3]))
        self.play(Write(add[4]))
        self.play(Write(add[5][0]), Write(add[5][-1]))
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(add[1][1:3].copy(), add[5][1:3]),
            TransformMatchingShapes(add[3][1:3].copy(), add[5][4:6]),
            Transform(add[2].copy(), add[5][3])
        )
        self.wait()
        self.play(
            TransformMatchingShapes(add[1][3:-1].copy(), add[5][6:9]),
            TransformMatchingShapes(add[3][3:-1].copy(), add[5][10:13]),
            Transform(add[2].copy(), add[5][9])
        )

        self.wait()


        self.play(FadeOut(op))

        self.wait()

        ulv = MathTex(r"\mathbf{u}").set_color(GREEN).move_to(ul.get_center())
        vlv = MathTex(r"\mathbf{v}").set_color(BLUE).move_to(vl.get_center()).shift(LEFT*0.5)
        rlv = MathTex(r"\mathbf{u} + \mathbf{v}").set_color(RED).move_to(rl.get_center()).shift(UP*0.5)

        self.play(Transform(ul, ulv), Transform(vl, vlv), Transform(rl, rlv))
        self.wait()


        self.wait()
        self.play(Create(plane))
        self.wait()
        self.play(
            v.animate.move_to([2, -1, 0]),
            vl.animate.move_to([1.5, -1.5,0])
        )
        self.wait()

        # haz una linea punteada

        lv = DashedLine(ORIGIN, [4, -2, 0], color=YELLOW)
        self.play(Create(lv))
        self.play(lv.animate.move_to([4, 2, 0]))
        self.wait()

        lx = DashedLine(ORIGIN, [2, 3, 0], color=YELLOW)
        self.play(Create(lx))
        self.play(lx.animate.move_to([5, -0.5, 0]))
        self.wait()

        # self.next_section(skip_animations=False)

        
