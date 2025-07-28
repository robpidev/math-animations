from manim import *

from p7_pixel import pixel_rgb



class P8PixelBit(Scene):
    def construct(self):
        self.wait()
        # self.next_section(skip_animations=True)

        pixel = pixel_rgb(220, 123, 222)

        self.play(Create(pixel), run_time = 3)
        self.wait()
        self.next_section()



