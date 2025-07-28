from manim import *

from p7_pixel import pixel_rgb, pixel_with_updaters, rgb




class P8PixelBit(Scene):
    def construct(self):
        self.wait()
        self.next_section(skip_animations=True)

        color = [220, 123, 222]

        pixel, value_trackers = pixel_with_updaters(*color)



        self.play(Create(pixel[0]))

        for l, v in zip(pixel[1], pixel[2]):
            self.play(Create(l), Write(v), run_time=0.5)
        
        self.wait()

        self.next_section(skip_animations=False)
        self.play(pixel[0].animate.set_fill(color=rgb(*color), opacity=1))
        self.wait()

        self.play(
            *[
                value_trackers[i].animate.set_value(0)
                for i in range(3)
            ]
        )

        self.wait()

        self.play(
            *[
                value_trackers[i].animate.set_value(255)
                for i in range(3)
            ]
        )

        self.wait()

        
