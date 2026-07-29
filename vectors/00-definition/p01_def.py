from funcs.vec2D_tex import vec_matrix
from manim import *
from mobj.mobjets import number_plane


class Def(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)

        self.wait()
        # title = Text("1. Definición de un Vector")
        # self.play(Write(title))
        # self.wait()
        # self.play(FadeOut(title))

        plane = number_plane()

        self.play(Create(plane))
        self.wait()

        a = Dot([4, 3, 0])
        al = MathTex("A=(4,3)").next_to(a, RIGHT)
        lx = Line(ORIGIN, 4 * RIGHT, stroke_width=2).set_color(RED)
        ly = Line(ORIGIN, 3 * UP, stroke_width=2).set_color(YELLOW)

        self.play(Create(a))
        self.wait()
        self.play(Write(al[0][0:3]))
        self.play(Create(lx))
        self.wait()
        self.play(Transform(lx, al[0][3]))
        self.play(Write(al[0][4]))
        self.play(Create(ly))
        self.play(Transform(ly, al[0][5]))
        self.play(Write(al[0][6:]))
        self.wait()

        o = Dot(ORIGIN)
        ot = MathTex("O=(0, 0)").next_to(o, DOWN)

        self.play(Create(o))
        self.wait()
        self.play(Write(ot))
        self.wait()

        r = Vector([4, 3], color=ORANGE)
        rt = (
            MathTex(r"\vec r", r"=\overrightarrow{OA}", "=[4,3]")
            .next_to(r, 0.5 * LEFT)
            .set_color(ORANGE)
        )
        self.play(Create(r))
        self.wait()
        self.play(Write(rt[0]))
        self.wait()
        self.play(Write(rt[1]))
        self.wait()
        self.play(Write(rt[2][:2]))
        self.play(TransformMatchingShapes(al[0][3].copy(), rt[2][2]))
        self.play(Write(rt[2][3]))
        self.play(TransformMatchingShapes(al[0][5].copy(), rt[2][4]))
        self.play(Write(rt[2][5]))
        self.wait()

        rtm = (
            MathTex("=", vec_matrix(4, 3)).move_to(rt[2].get_center()).set_color(ORANGE)
        )
        self.play(TransformMatchingShapes(rt[2], rtm))
        self.wait()
        self.play(FadeOut(rtm, rt[:2]))

        d1 = Dot([-3, 1, 0])
        d1t = MathTex("B=(-3,1)").next_to(d1, UP)
        r1 = Vector([-3, 1], color=GREEN)
        r1t = MathTex(r"\vec b=", vec_matrix(-3, 1)).next_to(d1, UP).set_color(GREEN)

        d2 = Dot([-4, -2, 0])
        d2t = MathTex("C=(-4,-2)").next_to(d2, DOWN)
        r2 = Vector([-4, -2], color=BLUE)
        r2t = MathTex(r"\vec c=", vec_matrix(-4, -2)).next_to(d2, DOWN).set_color(BLUE)

        d3 = Dot([2, -3, 0])
        d3t = MathTex("D=(2,-3)").next_to(d3, RIGHT)
        r3 = Vector([2, -3], color=PURPLE)
        r3t = (
            MathTex(r"\vec d=", vec_matrix(2, -3)).next_to(d3, RIGHT).set_color(PURPLE)
        )

        self.play(Create(d1))
        self.play(Write(d1t))
        self.play(Create(r1))
        self.play(TransformMatchingShapes(d1t, r1t))
        self.wait()

        self.play(Create(d2))
        self.play(Write(d2t))
        self.play(Create(r2))
        self.play(TransformMatchingShapes(d2t, r2t))
        self.wait()

        self.play(Create(d3))
        self.play(Write(d3t))
        self.play(Create(r3))
        self.play(TransformMatchingShapes(d3t, r3t))
        self.wait()

        self.play(FadeOut(r1, r2, r3, r1t, r2t, r3t, d1, d2, d3))
        self.wait()

        r1 = r.copy()
        r1t = MathTex(r"\vec r=[", "4,3]").move_to([-4, 1, 0]).set_color(ORANGE)

        rt = MathTex(r"\vec r=[", "4,3]").move_to([4, 1, 0]).set_color(ORANGE)

        self.play(r1.animate.move_to([-3, 0.5, 0]))
        self.wait()

        c = Dot([-5, -1, 0])
        ct = MathTex("C=(-5,-1)").next_to(c, DOWN)

        d = Dot([-1, 2, 0])
        dt = MathTex("D=(-1,2)").next_to(d, UP)

        self.play(Create(c))
        self.play(Write(ct))
        self.wait()
        self.play(Create(d))
        self.play(Write(dt))
        self.wait()

        lx1 = Line([-5, -1, 0], [-1, -1, 0]).set_color(RED)
        ly1 = Line([-1, -1, 0], [-1, 2, 0]).set_color(GREEN)

        self.play(Write(r1t[0]))
        self.play(Create(lx1))
        self.play(TransformFromCopy(lx1.copy(), r1t[1][0]))
        self.play(Write(r1t[1][1]))
        self.play(Write(rt[0]))
        self.play(lx1.animate.move_to([2, 0, 0]))
        self.wait()
        self.play(Transform(lx1, rt[1][0]))
        self.play(Write(rt[1][1]))
        self.wait()

        self.play(Create(ly1))
        self.play(TransformFromCopy(ly1.copy(), r1t[1][2]))
        self.play(Write(r1t[1][3]))
        self.play(ly1.animate.move_to([4, 1.5, 0]))
        self.wait()
        self.play(Transform(ly1, rt[1][2]))
        self.play(Write(rt[1][3]))
        self.wait()

        self.play(FadeOut(c, ct, d, dt, rt, lx1, ly1))
        self.wait()

        vg = VGroup(r1, r1t)

        self.play(vg.animate.move_to([1, 1, 0]))
        self.wait()

        self.play(vg.animate.move_to([3, -2, 0]))
        self.wait()

        self.play(vg.animate.move_to([2, 1.5, 0]))
        self.wait()

        vecs = MathTex(
            r"\vec u =[", "u_x", ",", "u_y", r"],\quad\vec v=[", "v_x", ",", "v_y", "]"
        )

        igales = MathTex(
            r"\vec u = \vec v \iff", "u_x", "=", "v_x", r"\wedge", "u_y", "=", "v_y"
        )

        vg = VGroup(vecs, igales).arrange(DOWN).move_to([-3, 2, 0])

        self.play(Write(vecs))
        self.play(Write(igales[0]))
        self.play(TransformMatchingShapes(vecs[1].copy(), igales[1]))
        self.play(Write(igales[2]))
        self.play(TransformMatchingShapes(vecs[-4].copy(), igales[3]))
        self.play(Write(igales[4]))
        self.play(TransformMatchingShapes(vecs[3].copy(), igales[-3]))
        self.play(Write(igales[-2]))
        self.play(TransformMatchingShapes(vecs[-2].copy(), igales[-1]))
        self.wait()

        self.play(FadeOut(vg))

        name = Text("Vector en posición normal").move_to([0, -2, 0])
        self.wait()
        self.play(Write(name))
        self.wait()
        self.play(FadeOut(name))
        self.wait()

        self.play(FadeOut(r1, r1t, o, ot, a, al, r, lx, ly))
        self.wait()

        a = Dot([-3, 2, 0])
        al = MathTex("A=(", "-3", ",", "2", ")").next_to(a, UP)
        b = Dot([2, 1, 0])
        bl = MathTex("B=(", "2", ",", "1", ")").next_to(b, UP + RIGHT)

        r = Arrow(a, b, buff=0)

        self.play(Create(a))
        self.play(Write(al))
        self.play(Create(b))
        self.play(Write(bl))
        self.wait()

        self.play(Transform(plane, r))
        self.wait()

        # Animacion que me olvide

        line = NumberLine(
            include_numbers=True,
            include_tip=True,
        )

        self.play(Transform(plane, line), FadeOut(a, al, b, bl))
        self.wait()

        p2 = Dot([3, 0, 0]).set_color(ORANGE)
        p1 = Dot([-2, 0, 0]).set_color(ORANGE)

        self.play(Create(p1))
        self.play(Create(p2))
        self.wait()

        l = Line(p1, p2).set_color(YELLOW)
        lt = MathTex(r"3 - (-2)", "=", "5").next_to(l, UP)
        rx = Arrow(p1, p2, buff=0).set_color(BLUE)

        self.play(Create(l))
        self.play(Write(lt[0]))
        self.wait()
        self.play(Write(lt[1]))
        self.play(TransformFromCopy(lt[0], lt[2]))
        self.wait()
        self.play(Create(rx))

        lt2 = MathTex(r"(-2) - 3", "=", "-5").next_to(l, UP)
        self.play(TransformMatchingShapes(lt, lt2))
        self.wait()
        self.play(FadeOut(rx))
        rx = Arrow(p2, p1, buff=0).set_color(BLUE)
        self.play(Create(rx))
        self.wait()

        self.play(FadeOut(lt2, l, p1, p2, rx))

        ly = NumberLine(
            include_numbers=True,
            include_tip=True,
            label_direction=RIGHT,
            rotation=90 * DEGREES,
        )

        self.play(Transform(plane, ly))

        p1 = Dot([0, -2, 0]).set_color(ORANGE)
        p2 = Dot([0, 1, 0]).set_color(ORANGE)

        ry = Arrow(p1, p2, buff=0).set_color(BLUE)
        rt = MathTex("1 - (-2)", "=", "3").next_to(ry, 1.5 * RIGHT)
        rt1 = MathTex("-2 - 1", "=", "-3").next_to(ry, 1.5 * RIGHT)

        self.play(Create(p1))
        self.play(Create(p2))
        self.play(Write(rt[0]))
        self.play(Write(rt[1]))
        self.play(TransformFromCopy(rt[0].copy(), rt[2]))
        self.play(Create(ry))
        self.wait()

        self.play(TransformMatchingShapes(rt, rt1))
        self.play(FadeOut(ry))

        ry = Arrow(p2, p1, buff=0).set_color(BLUE)
        self.play(Create(ry))
        self.wait()

        r = Arrow(a, b, buff=0)

        self.play(FadeOut(rt1, p1, p2, ry), Transform(plane, r), FadeIn(a, al, b, bl))

        self.wait()
        # sigue con las animaciones

        rt = MathTex(r"\vec r = \overrightarrow{AB}").next_to(r, DOWN)
        self.play(Write(rt))

        rt1 = MathTex(
            r"\vec r = \overrightarrow{AB}",
            "=[",
            "2",
            "-",
            "(-3)",
            ",",
            "1",
            "-",
            "2",
            "]",
        ).next_to(r, DOWN)

        resp = MathTex(r"\implies \vec r=[", "5", ",", "-1", "]").next_to(rt1, DOWN)

        self.play(rt.animate.move_to(rt1[0].get_center()))
        self.play(Write(rt1[1]))
        self.play(Write(rt1[5]))
        self.play(Write(rt1[-1]))
        self.wait()

        self.play(TransformMatchingShapes(bl[1].copy(), rt1[2]))
        self.play(Write(rt1[3]))
        self.play(TransformMatchingShapes(al[1].copy(), rt1[4]))
        self.wait()
        self.play(TransformMatchingShapes(bl[3].copy(), rt1[6]))
        self.play(Write(rt1[7]))
        self.play(TransformMatchingShapes(al[3].copy(), rt1[8]))
        self.wait()

        self.play(Write(resp[0]))
        self.play(Transform(rt1[2:5].copy(), resp[1]))
        self.play(Write(resp[2]))
        self.play(Transform(rt1[6:9].copy(), resp[3]))
        self.play(Write(resp[4]))
        self.wait()

        plane = number_plane()
        self.play(Transform(r.copy(), plane))
        self.wait()

        lx = Line([-3, 1, 0], [2, 1, 0]).set_color(RED)
        ly = Line([-3, 2, 0], [-3, 1, 0]).set_color(GREEN)

        self.play(TransformFromCopy(resp[1], lx))
        self.wait()
        self.play(TransformFromCopy(resp[-2], ly))
        self.wait()

        ry = Arrow([-3, 2, 0], [-3, 1, 0], buff=0).set_color(YELLOW)
        self.play(Create(ry))
        self.wait()

        rx = Arrow([-3, 1, 0], [2, 1, 0], buff=0).set_color(BLUE)
        self.play(Create(rx))

        self.wait()

        self.remove(lx, ly)

        # self.next_section(skip_animations=False)
        self.play(rx.animate.shift(UP))
        self.wait()
        self.play(ry.animate.shift(RIGHT * 5))
