from manim import NumberPlane

def number_plane():
    return NumberPlane(
            background_line_style={
                "stroke_width": 2,
                "stroke_opacity": 0.4,
            },
            axis_config={
                "stroke_width": 1,
                "stroke_opacity": 0.8,
            }
        )
