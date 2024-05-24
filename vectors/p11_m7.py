from manim import *
from funcs.vec_algebra import *
from funcs.vec2D_tex import *
from mobj import number_plane


class Prop7(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        d = MathTex(
            r"\text{(D). }",
            "x(y + z) = xy + xz",
            r",\quad\forall x, y, z \in \mathbb{R}"
        )

        self.play(Write(d))
        self.wait()
        self.play(d.animate.scale(0.8).to_edge(UP + LEFT))

        plane = number_plane() 
        self.play(Create(plane))
        self.wait()

        a = [-2, -1, 0]
        b = [-3, 1, 0]
        
        u = Vector(a, color=GREEN)
        v = Arrow(a, b, buff=0, color=BLUE)
        r = Vector(b, color=ORANGE)
        ul = MathTex(r"\mathbf{u}", color=GREEN).move_to(u, DOWN)
        vl = MathTex(r"\mathbf{v}", color=BLUE).move_to(v, LEFT)
        rl = MathTex(r"\mathbf{u} + \mathbf{v}", color=ORANGE).move_to(r, UP)

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))
        self.wait()
        self.play(Create(r), Write(rl))

        r2 = Vector(vec_scale(2, b), color=RED).set_opacity(0.8)
        rl2 = MathTex(
            r"2", r"(\mathbf{u} + \mathbf{v})",
            color=RED
        ).move_to(r2, UP)


        self.play(
            Create(r2),
            TransformMatchingShapes(rl.copy(), rl2),
        )

        self.wait()

        u2 = Vector(vec_scale(2, a), color=GREEN_B).set_opacity(0.8)
        ul2 = MathTex(
            r"2", r"\mathbf{u}",
            color=GREEN_B
        ).move_to(u2, DOWN)
        self.play(
            Create(u2),
            TransformMatchingShapes(ul.copy(), ul2),
        )

        self.wait()

        v2 = Arrow(vec_scale(2, a), vec_scale(2, b), buff=0, color=BLUE_B).set_opacity(0.8)
        vl2 = MathTex(
            r"2", r"\mathbf{v}",
            color=BLUE_B
        ).move_to(v2, LEFT)
        self.play(
            TransformMatchingShapes(v.copy(), v2),
            TransformMatchingShapes(vl.copy(), vl2),
        )

        self.wait()

        vecs_org = VGroup(u, v, r, ul, vl, rl)
        self.play(vecs_org.animate.set_opacity(0.4))

        rl2_add = MathTex("=", r"2\mathbf{u}", "+",  r"2\mathbf{v}")
        rl2_add.next_to(rl2, RIGHT).set_color(RED)

        self.play(TransformMatchingShapes(
            Group(ul2.copy(), vl2.copy()),
            rl2_add
        ))

        self.wait()
        graf = Group(vecs_org, u2, v2, ul2, vl2, r2, rl2, rl2_add)

        self.play(
            graf.animate.scale(0.7).move_to([4.5, -2.5, 0]),
            FadeOut(plane)
        )
    
        self.wait()

        #NOTE: ##################### PROOF ########################

        l1 = MathTex(
            r"c\in\mathbb{R}", r"\wedge"
                + "\mathbf{u}, \mathbf{v}\in \mathbb{R}^2", ",",
        )

        l2 = MathTex(
            r"c", r"(\mathbf{u} + \mathbf{v})=",
            "c", vec_add_comps("u", "v"),
            "=", vec_matrix("c(u_x + v_x)", "c(u_y + v_y)"),
        )

        l3 = MathTex(
            r"c", r"(\mathbf{u} + \mathbf{v})",
            "=", vec_add_comps("cu", "cv"),
            "=", vec_comps("cu"), "+", vec_comps("cv")
        )

        l4 = MathTex(
            r"c", r"(\mathbf{u} + \mathbf{v})",
            "=", "c" + vec_comps("u"), "+", "c" + vec_comps("v")
        )

        l5 = MathTex(
            r"c", r"(\mathbf{u} + \mathbf{v})",
            "=", r"c\mathbf{u}", "+", r"c\mathbf{v}"
        )

        result = MathTex(
            r"c", r"(\mathbf{u} + \mathbf{v})=",
            r"c\mathbf{u}", "+", r"c\mathbf{v}",
            r",\quad \forall c \in \mathbb{R}" + 
            r"\wedge \forall \mathbf{u}, \mathbf{v}\in \mathbb{R}^2",
        )
        proof = VGroup(l1, l2, l3, l4, l5)
        proof.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        proof.move_to([-1, 0, 0])

        for mo in l1:
            self.play(Write(mo))
            self.wait()

        
        self.play(Write(l2[:2]))
        self.play(TransformFromCopy(l2[0], l2[2]))
        self.play(TransformFromCopy(l2[1][:-1], l2[3]))
        self.wait()
        self.play(Write(l2[4]))
        self.play(TransformMatchingShapes(l2[2:4].copy(), l2[5]))
        self.wait()

        rec = SurroundingRectangle(d)
        self.play(Create(rec))
        self.wait()

        self.play(Write(l3[2]))
        self.play(TransformMatchingShapes(l2[-1].copy(), l3[3]))
        self.wait()

        self.play(FadeOut(rec))

        self.play(Write(l3[4]))
        self.play(
            TransformMatchingShapes(
                Group(l3[3][1:4], l3[3][8:11]).copy(),l3[5]
            ),
            TransformFromCopy(Group(l3[3][4], l3[3][11]),l3[6]),
            TransformMatchingShapes(
                VGroup(l3[3][5:8], l3[3][12:15]).copy(),l3[7]
            ),
        )
        self.wait()

        self.play(Write(l4[2]))
        self.play(TransformMatchingShapes(l3[5].copy(), l4[3]))
        self.play(TransformMatchingShapes(l3[6].copy(), l4[4]))
        self.play(TransformMatchingShapes(l3[7].copy(), l4[5]))
        self.wait()

        self.play(Write(l5[2]))
        self.play(TransformFromCopy(l4[3], l5[3]))
        self.play(TransformFromCopy(l4[4], l5[4]))
        self.play(TransformFromCopy(l4[5], l5[5]))
        self.wait()

        name = Tex("7. ").next_to(result, LEFT)

        Group(name, result).move_to(ORIGIN)

        # self.next_section(skip_animations=False)
        self.play(
            Transform(l2[0:2], result[0:2]),
            Transform(l5[3:], result[2:-1]),
            FadeOut(l2[2:], l3[2:], l4[2:], l5[2]),
            TransformMatchingShapes(l1, result[-1])
        )
        self.wait()
        self.play(Write(name))
        self.wait()

        self.clear()
        self.add(name, result, graf, d)

        self.play(FadeOut(name, result, graf))
        self.wait()
