"""
panels.py — Sistema de paneles coherente para Manim (landscape / portrait)
============================================================================

Idea central
------------
Manim deriva `config.frame_width` / `config.frame_height` a partir de la
resolución en píxeles que le pases (`-r ancho,alto` en la CLI). Este módulo
lee esos valores en tiempo de construcción y decide automáticamente si el
canvas es "landscape" (ancho >= alto) o "portrait" (alto > ancho), y arma
la grilla de paneles correspondiente. Así el MISMO código de escena sirve
para ambas orientaciones; solo cambias el flag de resolución al renderizar.

Uso rápido
----------
    manim -pql panels.py DemoScene -r 1920,1080   # horizontal
    manim -pql panels.py DemoScene -r 1080,1920   # vertical

Layouts incluidos por defecto
------------------------------
2 paneles:
    landscape:  [p1][p2]
    portrait:   [p1]
                [p2]

4 paneles:
    landscape:  [p1][p3]
                [p2][p4]
    portrait:   [p1]
                [p2]
                [p3]
                [p4]

Puedes definir tus propios layouts pasando un `PanelSpec` explícito.
"""

from dataclasses import dataclass, field

from manim import GREY, Mobject, Rectangle, VGroup, config

ORIENTATIONS = ("landscape", "portrait")


# ---------------------------------------------------------------------------
# Definición de celdas / especificación de grilla
# ---------------------------------------------------------------------------


@dataclass
class Cell:
    """Posición (col, row) de un panel dentro de la grilla, 0-indexado.
    col crece hacia la derecha, row crece hacia abajo.
    col_span / row_span permiten que un panel ocupe varias celdas."""

    col: int
    row: int
    col_span: int = 1
    row_span: int = 1


@dataclass
class PanelSpec:
    """Grilla completa: dimensiones (cols x rows) y la celda de cada panel,
    en el orden del índice de panel (0-based == panel1, panel2, ...)."""

    cols: int
    rows: int
    cells: list[Cell] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Layouts por defecto: {n_paneles: {variante: {orientación: PanelSpec}}}
#
# Cada combinación (n_paneles, variante) trae su propia versión landscape
# y portrait, para que el mismo `variant=` funcione en ambas orientaciones.
# ---------------------------------------------------------------------------

DEFAULT_LAYOUTS: dict[int, dict[str, dict[str, PanelSpec]]] = {
    1: {
        "default": {
            "landscape": PanelSpec(cols=1, rows=1, cells=[Cell(0, 0)]),
            "portrait": PanelSpec(cols=1, rows=1, cells=[Cell(0, 0)]),
        },
    },
    2: {
        "default": {
            # [p1][p2]
            "landscape": PanelSpec(cols=2, rows=1, cells=[Cell(0, 0), Cell(1, 0)]),
            # [p1]
            # [p2]
            "portrait": PanelSpec(cols=1, rows=2, cells=[Cell(0, 0), Cell(0, 1)]),
        },
    },
    3: {
        "default": {
            # [p1][p2][p3]
            "landscape": PanelSpec(
                cols=3, rows=1, cells=[Cell(0, 0), Cell(1, 0), Cell(2, 0)]
            ),
            # [p1]
            # [p2]
            # [p3]
            "portrait": PanelSpec(
                cols=1, rows=3, cells=[Cell(0, 0), Cell(0, 1), Cell(0, 2)]
            ),
        },
        "header": {
            # [titulo][  p2  ]
            # [ p1   ][  p2  ]   -> panel0=titulo (arriba-izq), panel1=p1 (abajo-izq),
            #                       panel2=p2 (columna derecha completa, las dos filas)
            "landscape": PanelSpec(
                cols=2,
                rows=2,
                cells=[
                    Cell(0, 0),  # titulo
                    Cell(0, 1),  # p1
                    Cell(1, 0, row_span=2),  # p2 (ocupa toda la col. derecha)
                ],
            ),
            # [   titulo    ]
            # [ p1  ][  p2  ]   -> título como banner arriba, p1/p2 lado a lado abajo
            "portrait": PanelSpec(
                cols=2,
                rows=2,
                cells=[
                    Cell(0, 0, col_span=2),  # titulo (ancho completo, fila superior)
                    Cell(0, 1),  # p1
                    Cell(1, 1),  # p2
                ],
            ),
        },
    },
    4: {
        "default": {
            # [p1][p3]
            # [p2][p4]   -> numeración "por columnas": p1,p2 en la col. izq (arriba/abajo),
            #               p3,p4 en la col. derecha (arriba/abajo)
            "landscape": PanelSpec(
                cols=2,
                rows=2,
                cells=[Cell(0, 0), Cell(0, 1), Cell(1, 0), Cell(1, 1)],
            ),
            # [p1]
            # [p2]
            # [p3]
            # [p4]
            "portrait": PanelSpec(
                cols=1,
                rows=4,
                cells=[Cell(0, 0), Cell(0, 1), Cell(0, 2), Cell(0, 3)],
            ),
        },
    },
}


# ---------------------------------------------------------------------------
# PanelLayout: calcula posiciones/tamaños reales dentro del frame de Manim
# ---------------------------------------------------------------------------


class PanelLayout:
    """
    Gestiona un conjunto de paneles dentro del frame de Manim, adaptándose
    automáticamente a orientación landscape/portrait.

    Parámetros
    ----------
    n_panels : int
        Número de paneles (debe existir en DEFAULT_LAYOUTS o pasar `spec`).
    orientation : "auto" | "landscape" | "portrait"
        "auto" (default) infiere la orientación comparando frame_width vs
        frame_height en el momento de instanciar el layout.
    variant : str
        Nombre de la variante de layout para ese `n_panels` (ej. "default",
        "header"). Usa `PanelLayout.available_variants(n_panels)` para ver
        cuáles existen.
    margin : float
        Margen entre el borde del frame y la grilla de paneles.
    gap : float
        Separación entre paneles contiguos.
    spec : PanelSpec, opcional
        Layout explícito, para casos que no cubren los defaults (ignora
        `variant` si se pasa).
    """

    def __init__(
        self,
        n_panels: int,
        orientation: str = "auto",
        variant: str = "default",
        margin: float = 0.4,
        gap: float = 0.3,
        spec: PanelSpec | None = None,
        frame_width: float | None = None,
        frame_height: float | None = None,
    ):
        self.n_panels = n_panels
        self.variant = variant
        self.margin = margin
        self.gap = gap
        self.frame_width = (
            frame_width if frame_width is not None else config.frame_width
        )
        self.frame_height = (
            frame_height if frame_height is not None else config.frame_height
        )

        if orientation == "auto":
            orientation = (
                "landscape" if self.frame_width >= self.frame_height else "portrait"
            )
        elif orientation not in ORIENTATIONS:
            raise ValueError(
                f"orientation debe ser 'auto', 'landscape' o 'portrait', no {orientation!r}"
            )

        self.orientation = orientation

        if spec is not None:
            self.spec = spec
        else:
            variants = DEFAULT_LAYOUTS.get(n_panels)
            if variants is None:
                raise ValueError(
                    f"No hay layouts por defecto para {n_panels} paneles. "
                    f"Pasa un PanelSpec explícito via el argumento `spec`."
                )
            by_orientation = variants.get(variant)
            if by_orientation is None:
                raise ValueError(
                    f"No existe la variante '{variant}' para {n_panels} paneles. "
                    f"Variantes disponibles: {list(variants.keys())}"
                )
            try:
                self.spec = by_orientation[orientation]
            except KeyError:
                raise ValueError(
                    f"La variante '{variant}' de {n_panels} paneles no define '{orientation}'."
                )
            if len(self.spec.cells) != n_panels:
                raise ValueError(
                    f"El PanelSpec tiene {len(self.spec.cells)} celdas pero se pidieron {n_panels} paneles."
                )

    @staticmethod
    def available_variants(n_panels: int) -> list[str]:
        """Lista las variantes de layout registradas para `n_panels`."""
        return list(DEFAULT_LAYOUTS.get(n_panels, {}).keys())

    # -- geometría -----------------------------------------------------

    def rects(self) -> list[Rectangle]:
        """Rectangle (sin estilo aplicado) por cada panel, en orden de índice."""
        cols, rows = self.spec.cols, self.spec.rows

        usable_w = self.frame_width - 2 * self.margin - (cols - 1) * self.gap
        usable_h = self.frame_height - 2 * self.margin - (rows - 1) * self.gap
        cell_w = usable_w / cols
        cell_h = usable_h / rows

        # esquina superior-izquierda de la grilla completa
        origin_x = -self.frame_width / 2 + self.margin
        origin_y = self.frame_height / 2 - self.margin

        rects = []
        for cell in self.spec.cells:
            w = cell_w * cell.col_span + self.gap * (cell.col_span - 1)
            h = cell_h * cell.row_span + self.gap * (cell.row_span - 1)
            x = origin_x + cell.col * (cell_w + self.gap) + w / 2
            y = origin_y - cell.row * (cell_h + self.gap) - h / 2
            rect = Rectangle(width=w, height=h)
            rect.move_to([x, y, 0])
            rects.append(rect)
        return rects

    def get(self, index: int) -> Rectangle:
        """Rectangle del panel `index` (0-based)."""
        return self.rects()[index]

    # -- helpers de contenido -------------------------------------------

    def fit(self, mobject: Mobject, index: int, buff: float = 0.15) -> Mobject:
        """Escala y centra `mobject` para que quepa dentro del panel `index`."""
        panel = self.get(index)
        mobject.set_max_width(panel.width - 2 * buff)
        if mobject.height > panel.height - 2 * buff:
            mobject.set_max_height(panel.height - 2 * buff)
        mobject.move_to(panel.get_center())
        return mobject

    def show_borders(self, **style) -> VGroup:
        """VGroup con los bordes de todos los paneles (útil para depurar el layout)."""
        style.setdefault("stroke_color", GREY)
        style.setdefault("stroke_width", 2)
        style.setdefault("fill_opacity", 0)
        return VGroup(*[r.set_style(**style) for r in self.rects()])


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from manim import (
        BLUE,
        GREEN,
        RED,
        YELLOW,
        Circle,
        Create,
        Scene,
        Square,
        Star,
        Text,
        Triangle,
        Write,
    )

    class DemoScene(Scene):
        def construct(self):
            layout = PanelLayout(n_panels=4)  # "auto": detecta landscape/portrait solo
            borders = layout.show_borders()

            shapes = [
                Circle(color=BLUE),
                Square(color=RED),
                Triangle(color=GREEN),
                Star(color=YELLOW),
            ]
            for i, shape in enumerate(shapes):
                layout.fit(shape, i)

            self.play(Create(borders))
            self.play(*[Create(s) for s in shapes])
            self.wait()

    class DemoHeaderScene(Scene):
        """3 paneles: título arriba (o arriba-izq) + p1 + p2.
        panel0 = titulo, panel1 = p1, panel2 = p2."""

        def construct(self):
            layout = PanelLayout(n_panels=3, variant="header")
            borders = layout.show_borders()

            titulo = Text("Ejercicios, problemas y otros", weight="BOLD")
            p1_content = Square(color=RED)
            p2_content = Circle(color=BLUE)

            layout.fit(titulo, 0)
            layout.fit(p1_content, 1)
            layout.fit(p2_content, 2)

            self.play(Create(borders))
            self.play(Write(titulo), Create(p1_content), Create(p2_content))
            self.wait()
