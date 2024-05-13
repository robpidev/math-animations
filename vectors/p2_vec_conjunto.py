from manim import *

class Anim(Scene):
    def construct(self):

        # self.next_section(skip_animations=True)
        self.wait()
        r = MathTex(r"\vec r", r"=\overrightarrow{OO}", r"=\overrightarrow{AA}")
        r1 = MathTex(r"\vec r", "=[", "A_x - A_x", ",", "A_y - A_y", "]")
        r2 = MathTex(r"\vec r", "=[", "0", ",", "0", "]")

        o = MathTex(r"\vec 0", "=[", "0", ",", "0", "]", )

        vg = VGroup(r, r1, r2, o).arrange(DOWN, aligned_edge=LEFT)

        rec_o = SurroundingRectangle(o, buff=0.1)

        self.play(Write(r[:2]))
        self.wait()
        self.play(Write(r[2]))
        self.wait()

        self.play(Write(r1[1:])) 
        self.wait()
        self.play(Write(r2[1]))
        self.play(Write(r2[3]))
        self.play(Write(r2[5]))
        self.wait()
        
        self.play(TransformFromCopy(r1[2], r2[2]))
        self.play(TransformFromCopy(r1[4], r2[4]))
        self.wait()

        self.play(Write(o[0]))
        self.play(r2[1:].animate.move_to(o[1:].get_center()))
        self.play(Create(rec_o))
        self.wait()

        self.play(FadeOut(r, r1[1:], r2[1:], o[0], rec_o))
        self.wait()

        self.next_section(skip_animations=False)


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

        set_r = MathTex(r"\mathbb{R}^2", r"=\mathbb{R} \times \mathbb{R}", r"=\left\{(x, y):x,y\in\mathbb{R}\right\}")
        self.play(Transform(plane, set_r[0]))
        self.wait()
        self.play(Write(set_r[1]))
        self.wait()
        self.play(Write(set_r[2]), run_time=2)
        self.wait()


        vec_r = MathTex(r"\mathbb{R}", "{}^2", r"=\mathbb{R} \times \mathbb{R}", r"=\left\{[x, y]:x,y\in\mathbb{R}\right\}")
        self.play(Transform(set_r[2], vec_r[3]))
        self.wait()


        self.clear()
        self.add(vec_r)

        field_r =Tex("Grupo", ": ",
                     r"$\left(\mathbb{R},+\right)$",
                     r', $\forall x, y, z \in \mathbb{R}$'
                     )
        
        ad1 = MathTex(r"1.\quad x + y \in \mathbb{R}")
        ad2 = MathTex(r"2.\quad x + y = y + x")
        ad3 = MathTex(r"3.\quad x + (y + z) = (x + y) + z")
        ad4 = MathTex(r"4. \quad \exists 0 \in \mathbb{R}: x + 0 = x")
        ad5 = MathTex(r"5.\quad \forall x, \exists -x \in \mathbb{R}: x + (-x) = 0")
        esc = Tex(r"Se acosumbra escribir\\",
                  "$(x + y) + z = z + y + z$, $x + (-y) = x - y$"
                  )

        vfield = VGroup(field_r, ad1, ad2, ad3, ad4, ad5, esc).arrange(DOWN, aligned_edge=LEFT)

        self.play(TransformMatchingShapes(vec_r[0], field_r[2]),
                  FadeOut(vec_r[1:]))

        self.wait()
        self.play(Write(field_r[3]))
        self.wait()

        for i in range(1, len(vfield)):
            self.play(Write(vfield[i]))
            self.wait()

        self.play(Write(field_r[:2]))
        self.wait()

        field_rc =Tex("Grupo conmutativo", ": ",
                        r"$\left(\mathbb{R},+\right)$",
                        r', $\forall x, y, z \in \mathbb{R}$'
                     ).move_to(field_r.get_center() + RIGHT * 1.4)

        rect = SurroundingRectangle(ad2)
        self.play(Create(rect))
        self.wait()

        self.play(TransformMatchingShapes(field_r[1:], field_rc[1:]))

        self.play(Transform(rect, field_rc[0][5:]))
        self.wait()













