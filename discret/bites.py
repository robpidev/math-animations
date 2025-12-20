from manim import RIGHT, YELLOW, Square, Text, VGroup


def create_byte(byte_text="0000 0000", color=YELLOW):
    """
    ```python
    return byte
    ```
    """
    byte_text = byte_text.replace(" ", "")
    byte = VGroup()
    for b in byte_text:
        sq = Square().scale(0.5).set_fill(color, 1 if b == "1" else 0)
        text = Text(b).scale(1.5).move_to(sq)
        bit = VGroup(sq, text)
        byte.add(bit)
    byte.arrange(RIGHT, buff=0.5)
    return byte


def byte_updater(byte_text="0000 0000", color=YELLOW):
    """
    ```python
    return byte, updater
    ```
    """
    byte = create_byte(byte_text, color)
    byte.add_updater(lambda m: m.become(create_byte(byte_text)))
    return byte


def int_to_bin(n: int) -> str:
    return f"{n:08b}"


print(int_to_bin(25))
