from funcs.vec2D_tex import *
from funcs.vec_algebra import *
from manim import *
from mobj.mobjets import number_plane


class P04_Resultant(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        title = Tex(r"Longitud de la resultante: $\|\mathbf{u + v}\|$")

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        # self.next_section(skip_animations=False)

        plane = number_plane()
        # self.play(Create(plane))
        self.wait(0.5)

        u, t1 = 3, 30
        v, t2 = 2, 120
        t = t2 - t1
        uv, vv = vec_angle(u, t1), vec_angle(v, t2)
        uv, vv = Vector(uv, color=RED), Vector(vv, color=GREEN)
        ul, vl = MathTex("u", color=RED), MathTex("v", color=GREEN)
        uvl, vvl = (
            MathTex(r"\mathbf{u}", color=RED),
            MathTex(r"\mathbf{v}", color=GREEN),
        )

        ul.next_to(uv, LEFT).shift(RIGHT)
        vl.next_to(vv, LEFT)

        uvl.next_to(uv.get_end(), RIGHT)
        vvl.next_to(vv.get_end(), LEFT)

        xL = Line(ORIGIN, xvec(u, t1), color=GREEN)
        yL = Line(ORIGIN, vec_angle(u, t1))
        xLl = MathTex(r"u\cos(\alpha)", color=GREEN).next_to(xL, DOWN)

        t1a = Angle(xL, yL, radius=0.8, color=RED)
        t2a = Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, vec_angle(u, t2)))
        t1t = MathTex(r"\alpha", color=RED).move_to(
            Angle(xL, yL, radius=0.8 + 3 * SMALL_BUFF).point_from_proportion(0.5)
        )

        self.play(Create(uv), Write(ul))
        self.wait(0.5)
        self.play(Create(t1a))
        self.play(Write(t1t))
        self.wait()

        yL = Line(ORIGIN, yvec(u, t1), color=BLUE).shift(xvec(u, t1))
        yLl = MathTex(r"u\sin(\alpha)", color=BLUE).next_to(yL, RIGHT)

        self.play(Create(xL))
        self.wait(0.5)
        self.play(TransformMatchingShapes(Group(ul.copy(), t1t.copy()), xLl))
        self.wait()

        self.play(Create(yL))
        self.wait(0.5)
        self.play(TransformMatchingShapes(Group(ul.copy(), t1t.copy()), yLl))
        self.wait(0.5)

        # self.next_section(skip_animations=False)

        uvtex = MathTex(
            r"\mathbf{u}",
            "=",
            vec_matrix(r"u\cos(\alpha)", r"u\sin(\alpha)"),
            color=RED,
        ).to_edge(UP + LEFT)

        self.play(
            TransformMatchingShapes(Group(xLl, yLl), uvtex),
            FadeOut(ul, xL, yL),
            Write(uvl),
        )

        self.wait()
        self.play(Create(vv), Write(vl))
        self.wait()

        xL = Line(ORIGIN, RIGHT)
        yL = Line(ORIGIN, vec_angle(v, t2))

        t2a = Angle(xL, yL, radius=0.7, color=GREEN)
        t2t = MathTex(r"\beta", color=GREEN).move_to(
            Angle(xL, yL, radius=0.7 + 3 * SMALL_BUFF).point_from_proportion(0.5)
        )

        self.play(Create(t2a))
        self.play(Write(t2t))
        self.wait()

        vvtex = MathTex(
            r"\mathbf{v}",
            "=",
            vec_matrix(r"v\cos(\beta)", r"v\sin(\beta)"),
            color=GREEN,
        ).next_to(uvtex, RIGHT)

        self.play(
            TransformMatchingShapes(Group(vl.copy(), t2t.copy()), vvtex),
            FadeOut(vl),
            Write(vvl),
        )

        self.wait()

        uL = Line(ORIGIN, vec_angle(u, t1))
        vL = Line(ORIGIN, vec_angle(v, t2))
        thetaarc = Angle(uL, vL, radius=1)
        thetal = MathTex(r"\theta").move_to(
            Angle(uL, vL, radius=1 + 3 * SMALL_BUFF).point_from_proportion(0.5)
        )

        rv = vec_add(uv.get_end(), vv.get_end())
        rv = Vector(rv, color=YELLOW)
        rvl = MathTex(r"\mathbf{u + v}", color=YELLOW).next_to(rv.get_end(), RIGHT)

        # self.next_section(skip_animations=False)

        self.play(Create(thetaarc))
        self.wait()
        self.play(Write(thetal))
        self.wait()

        thetatex = MathTex(
            r"\theta",
            "=",
            r"\beta",
            "-",
            r"\alpha",
        ).to_edge(RIGHT + UP)

        self.play(
            TransformMatchingShapes(
                Group(t1t.copy(), t2t.copy(), thetal.copy()), thetatex
            )
        )

        self.wait()

        self.play(Create(rv), Write(rvl))

        self.wait()

        # self.next_section(skip_animations=False)

        rtex = MathTex(
            r"\mathbf{u + v}",
            "=",
            vec_matrix(
                r"u\cos(\alpha) + v\cos(\beta)", r"u\sin(\alpha) + v\sin(\beta)"
            ),
        )

        rtex.move_to(VGroup(uvtex, vvtex).get_center())
        #
        # self.play(
        #     Transform(
        #         Group(uvtex[0].copy(), vvtex[0].copy()), rtex[0]
        #     ),
        #     FadeIn(rtex[1], rtex[2][0], rtex[2][-1]),
        #     TransformMatchingShapes(
        #         Group(uvtex[2][1:8].copy(), vvtex[2][1:8].copy()), rtex[2][1:16]
        #     ),
        #     TransformMatchingShapes(
        #         Group(uvtex[2][8:-1].copy(), vvtex[2][8:-1].copy()), rtex[2][16:-1]
        #     )
        # )
        self.play(
            ReplacementTransform(Group(uvtex[0], vvtex[0]), rtex[0]),
            FadeIn(rtex[1], rtex[2][0], rtex[2][-1]),
            TransformMatchingShapes(Group(uvtex[2][1:8], vvtex[2][1:8]), rtex[2][1:16]),
            TransformMatchingShapes(
                Group(uvtex[2][8:-1], vvtex[2][8:-1]), rtex[2][16:-1]
            ),
            FadeOut(
                uvtex[2][0], uvtex[2][-1], vvtex[2][0], vvtex[2][-1], uvtex[1], vvtex[1]
            ),
        )
        self.wait()

        # self.next_section(skip_animations=False)
        mod_res = (
            MathTex(
                r"\|\mathbf{u + v}\|",
                "=",
                r"\sqrt{[u\cos(\alpha) + v\cos(\beta)]^{2} + [u\sin(\alpha) + v\sin(\beta)]^{2}}",
            )
            .to_edge(LEFT)
            .shift(DOWN)
        )

        mod_resc = (
            MathTex(
                r"\|\mathbf{u + v}\|",
                "=",
                r"\sqrt{u^2\cos^2(\alpha) + 2uv\cos(\alpha)\cos(\beta) + v^2\cos^2(\beta)"
                + r"+u^2\sin^2(\alpha) + 2uv\sin(\alpha)\sin(\beta) + v^2\sin^2(\beta) }",
            )
            .scale(0.6)
            .move_to(mod_res)
        )

        self.play(
            ReplacementTransform(rtex[0].copy(), mod_res[0][1:-1]),
            FadeIn(mod_res[0][0], mod_res[0][-1], mod_res[1]),
            Write(VGroup(mod_res[2][:3], mod_res[2][18:22], mod_res[2][-2:])),
            ReplacementTransform(rtex[2][1:16].copy(), mod_res[2][3:18]),
            ReplacementTransform(rtex[2][16:-1].copy(), mod_res[2][22:-2]),
        )

        self.wait()
        self.play(TransformMatchingShapes(mod_res, mod_resc))

        mod_res = (
            MathTex(
                r"\|\mathbf{u + v}\|",
                "=",
                r"\sqrt{u^2[\cos^2(\alpha) + \sin^2(\alpha)]"
                + r"+v^2[\cos^2(\beta) + \sin^2(\beta)]"
                + r"+2uv[\cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)]}",
            )
            .move_to(mod_res)
            .scale(0.6)
        )
        self.wait()

        self.play(TransformMatchingShapes(mod_resc, mod_res))
        self.wait()

        # self.next_section(skip_animations=False)
        brace1 = Brace(mod_res[2][4:21])
        brace1l = brace1.get_tex("1")
        self.play(Write(brace1), Write(brace1l))
        self.wait()

        brace2 = Brace(mod_res[2][25:41])
        brace2l = brace2.get_tex("1")
        self.play(Write(brace2), Write(brace2l))
        self.wait()

        brace3 = Brace(mod_res[2][46:-1])
        brace3l = brace3.get_tex(r"\cos(\beta-\alpha)=\cos(\theta)")
        self.play(Write(brace3), Write(brace3l))
        self.wait()

        # self.next_section(skip_animations=False)
        mod_resc = MathTex(
            r"\|\mathbf{u + v}\|", "=", r"\sqrt{u^2 + v^2 + 2uv\cos(\theta)}"
        ).move_to(ORIGIN + DOWN)

        self.play(
            FadeOut(
                brace1,
                brace1l,
                brace2,
                brace2l,
                brace3,
                brace3l,
                t1t,
                t1a,
                t2t,
                t2a,
                rtex,
                thetatex,
            ),
            Transform(mod_res, mod_resc),
        )

        self.wait()

        self.next_section(skip_animations=False)
        dtex = MathTex(
            r"\mathbf{u - v}",
            "=",
            vec_matrix(
                r"u\cos(\alpha) - v\cos(\beta)", r"u\sin(\alpha) - v\sin(\beta)"
            ),
        ).to_edge(UP + LEFT)
        dv = Arrow(vv.end, uv.end, color=YELLOW, buff=0)
        dvl = MathTex(r"\mathbf{u - v}", color=YELLOW).next_to(dv, UP)

        mod_dif = MathTex(
            r"\|\mathbf{u - v}\|", "=", r"\sqrt{u^2 + v^2 - 2uv\cos(\theta)}"
        ).move_to(ORIGIN + DOWN)

        self.play(ReplacementTransform(rv, dv), ReplacementTransform(rvl, dvl))

        self.wait()

        self.play(Write(dtex))

        self.wait()
        self.play(ReplacementTransform(mod_res, mod_dif))

        # self.play(FadeIn(rtex))
        self.wait()
