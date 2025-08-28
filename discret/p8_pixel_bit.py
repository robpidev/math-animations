from manim import *

from bites import create_byte
from p7_pixel import pixel_with_updaters, rgb



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

        # self.next_section(skip_animations=False)
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

        self.play(pixel.animate.to_edge(LEFT))

        self.wait()

        # Color bits 
        # Red
        red_arr = Vector(LEFT, color=rgb(255, 0, 0)).next_to(pixel[1][0], RIGHT)

        self.play(Create(red_arr))

        red_byte = create_byte(f'{255:08b}', rgb(255))
        red_byte.scale(0.6).next_to(red_arr, RIGHT)

        self.play(TransformFromCopy(
            VGroup(pixel[1][0], pixel[2][0]), red_byte
        ))

        # Green
        green_arr = Vector(LEFT, color=rgb(0, 255, 0)).next_to(pixel[1][1], RIGHT)

        self.play(Create(green_arr))

        green_byte = create_byte(f'{255:08b}', rgb(0, 255, 0))
        green_byte.scale(0.6).next_to(green_arr, RIGHT)

        self.play(TransformFromCopy(
            VGroup(pixel[1][1], pixel[2][1]), green_byte
        ))

        # Blue
        blue_arr = Vector(LEFT, color=rgb(0, 0, 255)).next_to(pixel[1][2], RIGHT)

        self.play(Create(blue_arr))

        blue_byte = create_byte(f'{255:08b}', rgb(0, 0, 255))
        blue_byte.scale(0.6).next_to(blue_arr, RIGHT)

        self.play(TransformFromCopy(
            VGroup(pixel[1][2], pixel[2][2]), blue_byte
        ))

        # Updaters bits

        self.wait()
        
        red_byte.add_updater(
            lambda m: m.become(
                create_byte(
                    f'{int(value_trackers[0].get_value()):08b}',
                    rgb(int(value_trackers[0].get_value()), 0, 0)
                ).scale(0.6).move_to(m)
            )
        )

        green_byte.add_updater(
            lambda m: m.become(
                create_byte(
                    f'{int(value_trackers[1].get_value()):08b}',
                    rgb(0, int(value_trackers[1].get_value()), 0)
                ).scale(0.6).move_to(m)
            )
        )

        blue_byte.add_updater(
            lambda m: m.become(
                create_byte(
                    f'{int(value_trackers[2].get_value()):08b}',
                    rgb(0, 0, int(value_trackers[2].get_value()))
                ).scale(0.6).move_to(m)
            )
        )

        # self.next_section(skip_animations=False)

        self.play(
            value_trackers[0].animate.set_value(200),
            value_trackers[1].animate.set_value(150),
            value_trackers[2].animate.set_value(50),
            run_time=2
        )

        self.wait()

        self.play(
            value_trackers[0].animate.set_value(234),
            value_trackers[1].animate.set_value(123),
            value_trackers[2].animate.set_value(183),
            run_time=2
        )

        self.wait()

        self.play(
            value_trackers[0].animate.set_value(20),
            value_trackers[1].animate.set_value(200),
            value_trackers[2].animate.set_value(100),
            run_time=2
        )

        self.wait()


        self.next_section(skip_animations=False)
        
        bc = Brace(red_byte, direction=UP, buff=0.1)
        bc_text = bc.get_tex(r"\text{Byte (B)}").scale(1.5)

        self.play(Create(bc), Write(bc_text))
        self.wait()

        self.play(
            Transform(
                bc_text, bc.get_tex(r"\text{8 bits (b)}").scale(1.5)
            )
        )

        self.wait()

        self.play(
            Transform(
                bc_text, bc.get_tex(r"\text{Byte (B)}").scale(1.5)
            )
        )

        sq = SurroundingRectangle(
            VGroup(red_byte, green_byte, blue_byte),
            buff=0.1,
            corner_radius=0.1,
        )

        sq_label = Text("3").next_to(sq, DOWN)

        self.play(Create(sq))
        self.wait()
        self.play(Write(sq_label))
        self.wait()

        brace_pixel = Brace(pixel, direction=DOWN, buff=0.1)
        brace_text = brace_pixel.get_tex(r"\text{3 Bytes (3 B)}").scale(1.5)

        self.play(Write(brace_pixel))
        self.play(Write(brace_text))
        self.wait()
