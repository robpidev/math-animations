from manim import *
from funcs.vec2D_tex import *
from funcs.vec_algebra import *

class Add3(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait()

        a3 = Tex(r"(A3). $(x + y) + z = x + (y + z)$, $\forall x, y, z \in \mathbb{R}$")
        self.play(Write(a3))
        self.wait()

        self.play(a3.animate.scale(0.8).to_edge(UP + LEFT))


        plane = NumberPlane(
            background_line_style={
                "stroke_width": 1,
                "stroke_opacity": 0.8
            },
            axis_config={
                "stroke_width": 1,
                "stroke_opacity": 0.8
            }
        )

        self.play(Create(plane))
        self.wait()

        pp = [-4, -2, 0]
        pq = [-2, 2, 0]
        pr = [1, 2, 0]
        ps = [4, -1, 0]


        u = Arrow(pp, pq, buff=0, color=GREEN)
        v = Arrow(pq, pr, buff=0, color=BLUE)
        w = Arrow(pr, ps, buff=0, color=PURPLE)
        uv = Arrow(pp, pr, buff=0, color=YELLOW)
        vw = Arrow(pq, ps, buff=0, color=ORANGE)
        ruv = Arrow(pp, ps, buff=0, color=RED)
        rvw = Arrow(pp, ps, buff=0, color=RED)

        ul = MathTex(r"\mathbf{u}", color=GREEN).move_to([-3.5, 0, 0])
        vl = MathTex(r"\mathbf{v}", color=BLUE).move_to([-0.5, 2.5, 0])
        wl = MathTex(r"\mathbf{w}", color=PURPLE).move_to([3, 1, 0])
        uvl = MathTex(r"\mathbf{u}", "+", r"\mathbf{v}",
                      color=YELLOW).move_to([-0.5, 0, 0])
        vwl = MathTex(r"\mathbf{v}", "+", r"\mathbf{w}",
                      color=ORANGE).move_to([0, 0.5, 0])
        ruvl = MathTex(r"(\mathbf{u} + \mathbf{v})", "+", "\mathbf{w}",
                       color=RED).move_to([0, -1, 0])
        rvwl = MathTex(r"\mathbf{u}", "+", "(\mathbf{v} + \mathbf{w})",
                       color=RED).move_to([0, -1, 0])

        vecs = VGroup(u, v, w, ul, vl, wl)

        self.play(Create(u), Write(ul))
        self.play(Create(v), Write(vl))
        self.play(Create(w), Write(wl))
        self.wait()

        uvg = VGroup(u, v, ul, vl)
        self.play(Create(uv), Write(uvl), uvg.animate.set_opacity(0.4))
        self.wait()

        self.play(
            Create(ruv)
        )
        self.wait()

        self.play(TransformMatchingShapes(uvl.copy(), ruvl[0]))
        self.play(Write(ruvl[1]))
        self.play(TransformFromCopy(wl, ruvl[2]))
        
        eq1 = MathTex(
            "\left(", vec(vec_ab(pp, pq)), "+", vec(vec_ab(pq, pr)), r"\right)",
            "+", vec(vec_ab(pr, ps)),
            "=", vec(vec_add(vec_ab(pp, pq), vec_ab(pq, pr))), "+", vec(vec_ab(pr, ps)),
            "=", vec(vec_add(vec_ab(pp, pr), vec_ab(pr, ps))),
        ).move_to([0, -3, 0])

        eq1[0].set_color(YELLOW)
        eq1[4].set_color(YELLOW)
        eq1[1].set_color(GREEN)
        eq1[3].set_color(BLUE)
        eq1[6].set_color(PURPLE)
        eq1[8].set_color(YELLOW)
        eq1[10].set_color(PURPLE)
        eq1[12].set_color(RED)


        self.play(TransformFromCopy(u, eq1[1]))
        self.play(Write(eq1[2]))
        self.play(TransformFromCopy(v, eq1[3]))
        self.wait()

        pg = VGroup(eq1[0], eq1[4])
        self.play(TransformFromCopy(uv, pg))
        self.play(Write(eq1[5]))
        self.play(TransformFromCopy(w, eq1[6]))
        self.play(Write(eq1[7]))
        
        self.play(TransformFromCopy(eq1[:6], eq1[8]))
        self.play(Write(eq1[9]))
        self.play(TransformMatchingShapes(eq1[6].copy(), eq1[10]))
        self.play(Write(eq1[11]))
        self.play(TransformFromCopy(eq1[8:-2], eq1[12]))
        self.wait()
        eq12 = eq1[12].copy()
        self.play(Transform(eq12, ruv))
        self.wait()

        vecs1 = VGroup(u.copy(), v.copy(), ruv, w.copy(), uv,
                       ul.copy(), vl.copy(), wl.copy(), uvl, ruvl, eq12)

        self.play(vecs1.animate.scale(0.5).move_to([5, 1.7, 0]),
                  eq1[-1].animate.scale(0.7).move_to([5, 0.1, 0]),
                  uvg.animate.set_opacity(1),
                  FadeOut(eq1[8:-1])
                  )

        self.wait()

        vwg = VGroup(v, w, vl, wl)
        self.play(Create(vw), vwg.animate.set_opacity(0.4))
        self.wait()
        self.play(Write(vwl))

        self.play(Create(rvw))

        self.play(TransformMatchingShapes(ul.copy(), rvwl[0]))
        self.play(Write(rvwl[1]))
        self.play(TransformMatchingShapes(vwl.copy(), rvwl[2]))
        self.wait()


        eq2 = MathTex(
            vec(vec_ab(pp, pq)), "+", r"\left(", vec(vec_ab(pq, pr)), "+", vec(vec_ab(pr, ps)), r"\right)",
            "=", vec(vec_ab(pp, pq)), "+", vec(vec_add(vec_ab(pq, pr), vec_ab(pr, ps))),
            "=", vec(vec_ab(pp, ps))
        ).move_to([0, -3, 0])

        eq2[0].set_color(GREEN)
        eq2[2].set_color(ORANGE)
        eq2[3].set_color(BLUE)
        eq2[5].set_color(PURPLE)
        eq2[6].set_color(ORANGE)
        eq2[8].set_color(GREEN)
        eq2[10].set_color(ORANGE)
        eq2[12].set_color(RED)


        self.play(TransformMatchingShapes(eq1[0:8], eq2[0:8]))
        self.wait()
        
        self.play(TransformFromCopy(eq2[0], eq2[8]))
        self.play(Write(eq2[9]))
        self.play(TransformFromCopy(eq2[2:7], eq2[10]))
        self.wait()
        self.play(Write(eq2[11]))
        self.play(TransformFromCopy(eq2[8:11], eq2[12]))
        self.wait()


        rvwc = rvw.copy()
        self.play(TransformFromCopy(eq2[12], rvwc))
        self.wait()
        self.play(Transform(rvwc, eq1[12]))
        self.wait()
        
        vecs2 = VGroup(u.copy(), v.copy(), rvw, w.copy(), rvwl, ul.copy(),
                       vl.copy(), wl.copy(), vw, vwl)

        self.remove(eq1[12])
        # self.add(vecs, vecs1, vecs2, plane, a3, rvwc)
        self.play(vecs2.animate.scale(0.5).move_to([5, -2.2, 0]),
                  FadeOut(eq2, rvwc), vwg.animate.set_opacity(1),)

        self.wait()
        r = Arrow(pp, ps, color=RED, buff=0)
        rl = MathTex(r"\mathbf{u} + \mathbf{v} + \mathbf{w}",
                     color=RED).move_to([0, -2.2, 0])


        self.play(Create(r))
        self.wait()
        self.play(Write(rl))
        self.wait()

        self.play(FadeOut(vecs, r, rl, plane))

        self.wait()

        # proof.
        l1 = MathTex(
            r"(\mathbf{u} + \mathbf{v})", "+", "\mathbf{w}",
            "=", r"\left(", vec_comps("u"), " + ", vec_comps("v"), r"\right)",
            "+", vec_comps("w")
            )

        l2 = MathTex(
            r"(\mathbf{u} + \mathbf{v})", "+", "\mathbf{w}",
            "=", vec_add_comps("u", "v"), "+", vec_comps("w"),
            "=", vec_matrix(r"\left(u_x + v_x\right) + w_x", r"\left(u_y + v_y\right) + w_y")
        )

        l3 = MathTex(
            r"(\mathbf{u} + \mathbf{v})", "+", "\mathbf{w}",
            "=", vec_matrix(r"u_x + \left(v_x + w_x\right)", r"u_y + \left(v_y + w_y\right)"),
            "=", vec_comps("u"), "+", vec_add_comps("v", "w")
        )

        l4 = MathTex(
            r"(\mathbf{u} + \mathbf{v})", "+", "\mathbf{w}",
            "=", vec_comps("u"), "+", "\left(", vec_comps("v"), "+", vec_comps("w"), r"\right)",
            "=", r"\mathbf{u}", "+", "(", r"\mathbf{v}", "+", r"\mathbf{w}", ")",
        )


        proof = VGroup(l1, l2, l3,l4)
        proof.arrange(DOWN, aligned_edge=LEFT)
        proof.scale(0.82).move_to([-2, 0, 0])

        self.play(Write(l1[0:3]))
        self.wait()
        self.play(Write(l1[3:]))
        self.wait()
        self.play(Write(l2[3]))
        self.play(TransformMatchingShapes(l1[4:-2].copy(), l2[4]))
        self.play(TransformFromCopy(l1[-2].copy(), l2[5]))
        self.play(TransformFromCopy(l1[-1], l2[6]))
        self.wait()
        self.play(Write(l2[7]))
        self.play(TransformMatchingShapes(l2[4:7].copy(), l2[-1]))
        self.wait()

        self.play(Write(l3[3]))
        self.wait()
        rect = SurroundingRectangle(a3, buff=0.1)
        self.play(Create(rect))
        self.wait()
        self.play(TransformMatchingShapes(l2[-1].copy(), l3[4])) 
        self.play(FadeOut(rect))
        self.wait()

        self.play(Write(l3[5]))
        self.play(TransformMatchingShapes(l3[4].copy(), l3[6:]))
        self.wait()

        self.play(Write(l4[3]))
        self.play(TransformFromCopy(l3[-3], l4[4]))
        self.play(TransformFromCopy(l3[-2], l4[5]))
        self.play(TransformMatchingShapes(l3[-1].copy(), l4[6:11]))
        self.wait()
        self.play(Write(l4[11]))
        self.play(TransformFromCopy(l4[4], l4[12]))
        self.play(TransformFromCopy(l4[5], l4[13]))
        self.play(TransformFromCopy(l4[6], l4[14]),
                  TransformFromCopy(l4[10], l4[18]))
        self.play(TransformFromCopy(l4[7], l4[15]))
        self.play(TransformFromCopy(l4[8], l4[16]))
        self.play(TransformFromCopy(l4[9], l4[17]))
        self.wait()


        result = MathTex(
            r"\text{(A3). }",
            r"(\mathbf{u} + \mathbf{v}) + \mathbf{w}", "=",
            r"\mathbf{u} + (\mathbf{v} + \mathbf{w})",
            r",\quad \forall \mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^2"
        ).scale(0.8).shift(2 * LEFT)

        res_g = VGroup(
            result,
            Tex("Suele escribirse: "),
            MathTex(
                r"\mathbf{u} + \mathbf{v} + \mathbf{w}",
                "=", 
                vec_comps("u") + "+" + vec_comps("v") + "+" + vec_comps("w"),
            ),
            MathTex(
                r"\mathbf{u} + \mathbf{v} + \mathbf{w}",
                "=",
                vec_matrix("u_x + v_x + w_x", "u_y + v_y + w_y")
            )
        )

        res_g.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        res_g.move_to(2 * LEFT)

        self.play(l1[0:4].animate.move_to(result[1:3].get_center()).scale(1),
                  l4[-7:].animate.move_to(result[3].get_center()).scale(1),
                  FadeOut(l1[4:], l2[3:], l3[3:], l4[3:-7])
                  )
        self.wait()
        self.play(Write(result[4:]))
        self.wait()
        self.play(Write(result[0]))
        self.wait()

        self.play(Write(res_g[1]))
        self.play(Write(res_g[2]))
        self.play(TransformMatchingShapes(res_g[2][1:].copy(), res_g[3][1:]))
        # self.play(Write(res_g[3][1:]))
        self.wait()
        self.clear()

        self.add(result, vecs1, vecs2, a3)

        self.play(FadeOut(res_g[:-1], res_g[-1][1:], vecs1, vecs2, a3),)

        self.play(Create(plane))

        a = Vector([3, 2], color=GREEN)
        b = Vector([-3, 1], color=BLUE)
        c = Vector([-2, -2], color=PURPLE)
        d = Vector([1, -3], color=ORANGE)
        e = Vector([4, -1], color=YELLOW)
        r = Vector([3, -3], color=RED)

        vecs = VGroup(a, b, c, d, e)

        for v in vecs:
            self.play(Create(v))

        self.wait()

        eq = MathTex(
            vec([3, 2]), "+",
            vec([-3, 1]), "+",
            vec([-2, -2]), "+",
            vec([1, -3]), "+",
            vec([4, -1]), "=",
            vec_matrix("3 - 3 - 2 + 1 + 4", "2 + 1 - 2 - 3 - 1"),
            "=",
            vec([3, -3])
        ).move_to([0, -3, 0]).scale(0.8)

        eq[0].set_color(GREEN)
        eq[2].set_color(BLUE)
        eq[4].set_color(PURPLE)
        eq[6].set_color(ORANGE)
        eq[8].set_color(YELLOW)
        eq[-1].set_color(RED)

        for i in range(0, 9, 2):
            self.play(TransformFromCopy(vecs[i // 2], eq[i]))
            self.play(Write(eq[i + 1]))


        self.play(b.animate.move_to([1.5, 2.5, 0]))
        self.play(c.animate.move_to([-1, 2, 0]))
        self.play(d.animate.move_to([-1.5, -0.5, 0]))
        self.play(e.animate.move_to([1, -2.5, 0]))
        self.wait()
        self.play(Create(r), vecs.animate.set_opacity(0.5))
        self.wait()

        self.play(TransformMatchingShapes(eq[:-4].copy(), eq[-3]))
        self.play(Write(eq[-2]))
        self.play(TransformFromCopy(eq[-3], eq[-1]))
        self.wait()
        self.play(TransformFromCopy(eq[-1], r))

        self.play(FadeOut(eq))

        # self.next_section(skip_animations=False)

        self.play(b.animate.move_to([-3.5, 1.5, 0]))
        self.play(e.animate.move_to([-3, 1.5, 0]))
        self.play(a.animate.move_to([0.5, 2, 0]))
        self.play(d.animate.move_to([2.5, 1.5, 0]))
        self.wait()
        self.play(r.animate.move_to([1.5, 1.5, 0]))




