from manim import *

# import random
import random



def rgb(color=[0, 0, 0]):
    color = [int(c % 256) for c in color]
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def create_imgob(pixels=[[0, 0, 0]]):
        return VGroup(
            *[
                VGroup(
                    *[
                        Square().set_fill(
                            color=pixels[i][j],
                            opacity=1,
                        ).set_stroke(width=0) for j in range(len(pixels[0]))
                    ]
                ).arrange(RIGHT) for i in range(len(pixels))
        ]).arrange(DOWN)

def pixel_rgb(red=0, green=0, blue=0):
    r = RoundedRectangle(height=1, width=4, corner_radius=0.1)
    g = RoundedRectangle(height=1, width=4, corner_radius=0.1)
    b = RoundedRectangle(height=1, width=4, corner_radius=0.1)

    r.set_fill(color=rgb([red, 0, 0]), opacity=1)
    g.set_fill(color=rgb([0, green, 0]), opacity=1)
    b.set_fill(color=rgb([0, 0, blue]), opacity=1)

    leds = VGroup(r, g, b).arrange(DOWN, buff=0.5)
    leds.arrange(DOWN, buff=0.5)

    r_value = Text(f"{red}").move_to(r)
    g_value = Text(f"{green}").move_to(g)
    b_value = Text(f"{blue}").move_to(b)

    rgb_values = VGroup(r_value, g_value, b_value)
    
    border = SurroundingRectangle(leds, corner_radius=0.1, buff=0.5)
    border.set_color(WHITE)

    return VGroup(border, leds, rgb_values)


f = "JetBrainsMono Nerd Font"

def rgb_to_hex(color = (0, 0, 0)):
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"



class P7Pixel(Scene):
    def construct(self):
        self.wait()

        # self.next_section(skip_animations=True)
        # self.play(Create(Text("Hola :3")))
        # self.wait()

        sq = RoundedRectangle(
            height=5,
            width=5,
            corner_radius=0.1
        )

        r = RoundedRectangle(height=1, width=4, corner_radius=0.1)
        g = RoundedRectangle(height=1, width=4, corner_radius=0.1)
        b = RoundedRectangle(height=1, width=4, corner_radius=0.1)

        prgb = VGroup(r, g, b).arrange(DOWN, buff=0.5)

        r.set_fill(color=rgb([0, 0, 0]), opacity=1)
        g.set_fill(color=rgb([0, 0, 0]), opacity=1)
        b.set_fill(color=rgb([0, 0, 0]), opacity=1)



        
        rt = Text("0", font=f).move_to(r)
        gt = Text("0", font=f).move_to(g)
        bt = Text("0", font=f).move_to(b)

        rvt = ValueTracker(0)
        gvt = ValueTracker(0)
        bvt = ValueTracker(0)

        r.add_updater(
            lambda m: m.set_fill(
                color=rgb([rvt.get_value(), 0, 0]),
                opacity=1
            )
        )

        g.add_updater(
            lambda m: m.set_fill(
                color=rgb([0, gvt.get_value(), 0]),
                opacity=1
            )
        )

        b.add_updater(
            lambda m: m.set_fill(
                color=rgb([0, 0, bvt.get_value()]),
                opacity=1
            )
        )

        # Text updater
        rt.add_updater(
            lambda m: m.become(
                Text(f"{int(rvt.get_value())}", font=f).move_to(r)
            )
        )

        gt.add_updater(
            lambda m: m.become(
                Text(f"{int(gvt.get_value())}", font=f).move_to(g)
            )
        )

        bt.add_updater(
            lambda m: m.become(
                Text(f"{int(bvt.get_value())}", font=f).move_to(b)
            )
        )


        self.play(Create(sq))
        self.wait()

        # Red
        self.play(Create(r))
        self.wait(0.5)
        self.play(Write(rt))
        self.wait()
        self.play(rvt.animate.set_value(255))
        self.wait()
       
        #Green
        self.play(Create(g))
        self.wait(0.5)
        self.play(Write(gt))
        self.wait()
        self.play(gvt.animate.set_value(255))
        self.wait()

        #Blue
        self.play(Create(b))
        self.wait(0.5)
        self.play(Write(bt))
        self.wait()
        self.play(bvt.animate.set_value(255))
        self.wait()


        # self.next_section(skip_animations=False)

        pixrgb = VGroup(
            r, g, b, rt, gt, bt, sq,
        )

        self.play(pixrgb.animate.to_edge(LEFT))
        self.wait()

        pixel = RoundedRectangle(
            height=4,
            width=4,
            corner_radius=0.1
        ).set_fill(color="#ffffff", opacity=1)
        pixel.to_edge(RIGHT)

        pixel.add_updater(
            lambda m: m.set_fill(
                color=rgb([rvt.get_value(), gvt.get_value(), bvt.get_value()]),
                opacity=1
            )
        )

        self.play(
            TransformFromCopy(
                VGroup(r, g, b),
                pixel
            )
        )

        self.wait()
        self.play(
            rvt.animate.set_value(0),
        )
        self.wait(0.5)
        self.play(gvt.animate.set_value(0))
        self.wait(0.5)
        self.play(bvt.animate.set_value(0))
        self.wait()

        self.play(
            rvt.animate.set_value(100),
            gvt.animate.set_value(150),
            bvt.animate.set_value(33),
        )

        self.wait()

        # cambia los value trackers para que
        # me de el color purpura

        self.play(
            rvt.animate.set_value(149),
            gvt.animate.set_value(117),
            bvt.animate.set_value(205),
        )

        self.wait()

        # self.next_section(skip_animations=False)

        pixels = [
            [rgb([119, 117, 205]) for _ in range(16)]
            for _ in range(9)
        ]
        
        img_ob = create_imgob(pixels).scale(0.3)
        self.play(FadeOut(pixrgb))

        self.play(
            ReplacementTransform(pixel, img_ob[0][0]),
        )

        self.wait()
        self.play(Create(img_ob[0][1:]))
        self.wait()

        brace_w = Brace(img_ob, direction=UP, buff=0.1)
        brace_wt = brace_w.get_text("16").scale(1.2)

        brace_h = Brace(img_ob, direction=LEFT, buff=0.1)
        brace_ht = brace_h.get_text("9").scale(1.2)

        self.play(Write(brace_w))
        self.play(Write(brace_wt))
        self.wait()

        self.play(Create(img_ob[1:]), run_time = 4)
        self.wait()

        self.play(Write(brace_h))
        self.play(Write(brace_ht))
        self.wait()


        res = MathTex(r"16", r"\times", "9").to_edge(DOWN)

        self.play(
            TransformMatchingShapes(brace_wt.copy(), res[0]),
            Write(res[1]),
            TransformMatchingShapes(brace_ht.copy(), res[2]),
        )
        self.wait()

        self.play(FadeOut(brace_w, brace_wt, brace_h, brace_ht))

        img_white = [
            [rgb([255, 255, 255]) for _ in range(16)]
            for _ in range(9)
        ]

        self.play(
            Transform(img_ob, create_imgob(img_white).scale(0.3))
        )

        self.wait()

        img_grad = [
            [rgb([2 * i * j,2 * i * j,2 * i * j]) for i in range(16)]
            for j in range(9)
        ]

        self.play(
            Transform(img_ob, create_imgob(img_grad).scale(0.3))
        )

        self.wait()


        img_rand = [
            [rgb([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) for _ in range(16)]
            for _ in range(9)
        ]

        self.play(
            Transform(img_ob, create_imgob(img_rand).scale(0.3))
        )

        self.wait()

        img_16x16 = [
            [rgb([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]) for _ in range(16)]
            for _ in range(16)
        ]


        self.play(
            Transform(img_ob, create_imgob(img_16x16).scale(0.2)),
            FadeOut(res)
        )


        # self.next_section(skip_animations=False)


        img_heart = [
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF",  "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#000000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF",  "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF",  "#FFFFFF", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF",  "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF"],
            ["#ffffff", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000",  "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF"],
            ["#ffffff", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF"],
            ["#ffffff", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#FF0000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#FF0000", "#FF0000",  "#FF0000", "#FF0000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#FF0000",  "#FF0000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000",  "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF",  "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"],
            ["#ffffff", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF",  "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]

        ]        


        self.play(
            Transform(img_ob, create_imgob(img_heart).scale(0.2))
        )


        self.wait()



