from manim import RIGHT, WHITE, YELLOW, Square, Text, VGroup
from manim.mobject.svg.svg_mobject import RoundedRectangle

font = "JetBrainsMono Nerd Font"


def create_byte(byte_text="0000 0000", color=YELLOW):
    """
    ```python
    return byte
    ```
    """
    byte_text = byte_text.replace(" ", "")
    byte = VGroup()
    for b in byte_text:
        sq = RoundedRectangle(0.1, height=1.2, width=1.2).set_color(
            color if b == "1" else WHITE
        )
        text = (
            Text(b, font=font, color=color if b == "1" else WHITE)
            .scale(1.5)
            .move_to(sq)
        )
        bit = VGroup(sq, text)
        byte.add(bit)
    byte.arrange(RIGHT, buff=0.5)
    return byte


def create_byte_updater(byte_text="0000 0000", color=YELLOW):
    """
    ```python
    return byte, updater
    ```
    """
    byte = create_byte(byte_text, color)
    byte.add_updater(lambda m: m.become(create_byte(byte_text)))
    return byte


def int_to_bin(n: int | float) -> str:
    n = int(n)
    return f"{n:08b}"


print(int_to_bin(25))
