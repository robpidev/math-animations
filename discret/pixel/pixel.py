from manim import (
    DOWN,
    ORIGIN,
    RoundedRectangle,
    SurroundingRectangle,
    Text,
    ValueTracker,
    VGroup,
)


def rgb(r=0.0, g=0.0, b=0.0):
    color = [r, g, b]
    color = [int(c % 256) for c in color]
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


FONT = "JetBrainsMono Nerd Font"


# === Pixel Hexa ===
def to_hexa(n):
    n = int(n)
    return f"{n:02X}" if n > 128 else f"{n:1X}"


def animate_pixel(
    value_trackers: tuple[ValueTracker, ValueTracker, ValueTracker], r, g, b
):
    rt, gt, bt = value_trackers
    rt = rt.animate.set_value(r)
    gt = gt.animate.set_value(g)
    bt = bt.animate.set_value(b)

    return rt, gt, bt


def pixel_hexa(r=0, g=0, b=0, label=False):
    """
    If ```label = True```  True, this returns
    ```python
    return (Rectangle, VGroup(subpixels), VGroup(subpixels_labels), Text("#rrggbb"),
    (rt, gt, bt)
    ```

    If ```label = True```  True, this returns
    ```python
    return (Rectangle, VGroup(subpixels), VGroup(subpixels_labels)), (rt, gt, bt)
    ```
    """
    bg = RoundedRectangle(height=5, width=5, corner_radius=0.1)
    bg.set_fill(color=rgb(r, g, b), opacity=1)

    rs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(255, 0, 0))
    gs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(0, 255, 0))
    bs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(0, 0, 255))

    rs.set_fill(color=rgb(r, 0, 0), opacity=1)
    gs.set_fill(color=rgb(0, g, 0), opacity=1)
    bs.set_fill(color=rgb(0, 0, b), opacity=1)

    subpixels = VGroup(rs, gs, bs).arrange(DOWN, buff=0.5).move_to(bg)

    rl = Text(f"{to_hexa(r)}", font=FONT).move_to(subpixels[0])
    gl = Text(f"{to_hexa(g)}", font=FONT).move_to(subpixels[1])
    bl = Text(f"{to_hexa(b)}", font=FONT).move_to(subpixels[2])

    subpixels_labels = VGroup(rl, gl, bl)

    pixel = VGroup(bg, subpixels, subpixels_labels)

    # red_updater
    rt = ValueTracker(r)
    gt = ValueTracker(g)
    bt = ValueTracker(b)

    rs.add_updater(
        lambda m: m.set_fill(color=rgb(int(rt.get_value()), 0, 0), opacity=1)
    )

    gs.add_updater(
        lambda m: m.set_fill(color=rgb(0, int(gt.get_value()), 0), opacity=1)
    )

    bs.add_updater(
        lambda m: m.set_fill(color=rgb(0, 0, int(bt.get_value())), opacity=1)
    )

    bg.add_updater(
        lambda m: m.set_fill(
            color=rgb(*(c.get_value() for c in (rt, gt, bt))), opacity=1
        )
    )

    rl.add_updater(
        lambda m: m.become(
            Text(f"{to_hexa(int(rt.get_value()))}", font=FONT).move_to(subpixels[0])
        )
    )

    gl.add_updater(
        lambda m: m.become(
            Text(f"{to_hexa(int(gt.get_value()))}", font=FONT).move_to(subpixels[1])
        )
    )

    bl.add_updater(
        lambda m: m.become(
            Text(f"{to_hexa(int(bt.get_value()))}", font=FONT).move_to(subpixels[2])
        )
    )

    if not (label):
        return (bg, subpixels, subpixels_labels), (rt, gt, bt)

    text = Text(f"#{to_hexa(r)}{to_hexa(g)}{to_hexa(b)}", font=FONT)

    text.add_updater(
        lambda m: m.become(
            Text(
                f"#{to_hexa(int(rt.get_value()))}{to_hexa(int(gt.get_value()))}{to_hexa(int(bt.get_value()))}",
                font=FONT,
            ).move_to(m)
        )
    )

    VGroup(pixel, text).arrange(DOWN, buff=0.5).move_to(ORIGIN)

    return (bg, subpixels, subpixels_labels, text), (rt, gt, bt)


# === Pixel RGB ===
def pixel_rgb(r=0, g=0, b=0, label=False):
    """
    If ```label = True```  True, this returns
    ```python
    return (Rectangle, VGroup(subpixels), VGroup(subpixels_labels), Text("rgb(r, g, b)"),
    (rt, gt, bt)
    ```

    If ```label = True```  True, this returns
    ```python
    return (Rectangle, VGroup(subpixels), VGroup(subpixels_labels)), (rt, gt, bt)
    ```
    """

    bg = RoundedRectangle(height=5, width=5, corner_radius=0.1)
    bg.set_fill(color=rgb(r, g, b), opacity=1)

    rs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(255, 0, 0))
    gs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(0, 255, 0))
    bs = RoundedRectangle(height=1, width=4, corner_radius=0.1, color=rgb(0, 0, 255))

    rs.set_fill(color=rgb(r, 0, 0), opacity=1)
    gs.set_fill(color=rgb(0, g, 0), opacity=1)
    bs.set_fill(color=rgb(0, 0, b), opacity=1)

    subpixels = VGroup(rs, gs, bs).arrange(DOWN, buff=0.5).move_to(bg)

    rl = Text(f"{r}", font=FONT).move_to(subpixels[0])
    gl = Text(f"{g}", font=FONT).move_to(subpixels[1])
    bl = Text(f"{b}", font=FONT).move_to(subpixels[2])

    subpixels_labels = VGroup(rl, gl, bl)

    pixel = VGroup(bg, subpixels, subpixels_labels)

    # red_updater
    rt = ValueTracker(r)
    gt = ValueTracker(g)
    bt = ValueTracker(b)

    rs.add_updater(
        lambda m: m.set_fill(color=rgb(int(rt.get_value()), 0, 0), opacity=1)
    )

    gs.add_updater(
        lambda m: m.set_fill(color=rgb(0, int(gt.get_value()), 0), opacity=1)
    )

    bs.add_updater(
        lambda m: m.set_fill(color=rgb(0, 0, int(bt.get_value())), opacity=1)
    )

    bg.add_updater(
        lambda m: m.set_fill(
            color=rgb(*(c.get_value() for c in (rt, gt, bt))), opacity=1
        )
    )

    rl.add_updater(
        lambda m: m.become(
            Text(f"{int(rt.get_value())}", font=FONT).move_to(subpixels[0])
        )
    )

    gl.add_updater(
        lambda m: m.become(
            Text(f"{int(gt.get_value())}", font=FONT).move_to(subpixels[1])
        )
    )

    bl.add_updater(
        lambda m: m.become(
            Text(f"{int(bt.get_value())}", font=FONT).move_to(subpixels[2])
        )
    )

    if not (label):
        return (bg, subpixels, subpixels_labels), (rt, gt, bt)

    text = rgb_label(r, g, b).next_to(pixel, DOWN)

    text.add_updater(
        lambda m: m.become(
            rgb_label(
                int(rt.get_value()), int(gt.get_value()), int(bt.get_value())
            ).next_to(pixel, DOWN)
        )
    )

    vg = VGroup(bg, subpixels, subpixels_labels, text)
    vg.move_to(ORIGIN)

    return vg, (rt, gt, bt)


def rgb_label(r=0, g=0, b=0):
    text = Text(f"rgb({r},{g},{b})", font=FONT)
    f = 4
    rd = len(str(r))
    s = f + rd + 1
    gd = len(str(g))
    t = s + gd + 1

    sqs = [
        SurroundingRectangle(text[f : s - 1], corner_radius=0.1, color=rgb(255, 0, 0)),
        SurroundingRectangle(text[s : t - 1], corner_radius=0.1, color=rgb(0, 255, 0)),
        SurroundingRectangle(text[t:-1], corner_radius=0.1, color=rgb(0, 0, 255)),
    ]

    return VGroup(text, *sqs)
