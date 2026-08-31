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
from typing import Union

import numpy as np
from manim import GREY, ORIGIN, Mobject, Rectangle, Transform, VGroup, config

ORIENTATIONS = ("landscape", "portrait")
DEFAULT_MARGIN = 0.4

MarginSpec = Union[
    float, tuple[float, float], tuple[float, float, float, float], dict[str, float]
]


def _normalize_margin(margin: MarginSpec) -> tuple[float, float, float, float]:
    """
    Normaliza distintos formatos de margen a (top, right, bottom, left):
    - número (ej. 0.4): mismo margen en los 4 lados
    - (vertical, horizontal): top=bottom=vertical, left=right=horizontal
    - (top, right, bottom, left): estilo CSS, los 4 lados independientes
    - dict con llaves parciales 'top'/'right'/'bottom'/'left' (el resto usa DEFAULT_MARGIN)
    """
    if isinstance(margin, dict):
        return (
            margin.get("top", DEFAULT_MARGIN),
            margin.get("right", DEFAULT_MARGIN),
            margin.get("bottom", DEFAULT_MARGIN),
            margin.get("left", DEFAULT_MARGIN),
        )
    if isinstance(margin, (tuple, list)):
        if len(margin) == 2:
            v, h = margin
            return (v, h, v, h)
        if len(margin) == 4:
            return tuple(margin)  # type: ignore[return-value]
        raise ValueError(
            "margin como tupla/lista debe tener 2 valores (vertical, horizontal) o 4 (top, right, bottom, left)."
        )
    return (margin, margin, margin, margin)


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
    margin : float | tuple | dict
        Espacio entre el borde del frame y la grilla de paneles. Acepta:
        - un número: mismo margen en los 4 lados (default 0.4)
        - (vertical, horizontal): top=bottom=vertical, left=right=horizontal
        - (top, right, bottom, left): estilo CSS, los 4 lados independientes
        - dict parcial: {"top": 0.6, "left": 1.0} (lo no especificado usa DEFAULT_MARGIN)
    gap : float
        Separación entre paneles contiguos (aplica a filas y columnas si no
        se pasan `row_gap`/`col_gap`).
    row_gap : float, opcional
        Separación vertical entre filas de paneles (sobreescribe `gap` solo
        en esa dirección).
    col_gap : float, opcional
        Separación horizontal entre columnas de paneles (sobreescribe `gap`
        solo en esa dirección).
    spec : PanelSpec, opcional
        Layout explícito, para casos que no cubren los defaults (ignora
        `variant` si se pasa).
    """

    def __init__(
        self,
        n_panels: int,
        orientation: str = "auto",
        variant: str = "default",
        margin: MarginSpec = DEFAULT_MARGIN,
        gap: float = 0.3,
        row_gap: float | None = None,
        col_gap: float | None = None,
        spec: PanelSpec | None = None,
        frame_width: float | None = None,
        frame_height: float | None = None,
    ):
        self.n_panels = n_panels
        self.variant = variant
        self.margin_top, self.margin_right, self.margin_bottom, self.margin_left = (
            _normalize_margin(margin)
        )
        self.gap = gap
        self.row_gap = row_gap if row_gap is not None else gap
        self.col_gap = col_gap if col_gap is not None else gap
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

        usable_w = (
            self.frame_width
            - self.margin_left
            - self.margin_right
            - (cols - 1) * self.col_gap
        )
        usable_h = (
            self.frame_height
            - self.margin_top
            - self.margin_bottom
            - (rows - 1) * self.row_gap
        )
        cell_w = usable_w / cols
        cell_h = usable_h / rows

        # esquina superior-izquierda de la grilla completa
        origin_x = -self.frame_width / 2 + self.margin_left
        origin_y = self.frame_height / 2 - self.margin_top

        rects = []
        for cell in self.spec.cells:
            w = cell_w * cell.col_span + self.col_gap * (cell.col_span - 1)
            h = cell_h * cell.row_span + self.row_gap * (cell.row_span - 1)
            x = origin_x + cell.col * (cell_w + self.col_gap) + w / 2
            y = origin_y - cell.row * (cell_h + self.row_gap) - h / 2
            rect = Rectangle(width=w, height=h)
            rect.move_to([x, y, 0])
            rects.append(rect)
        return rects

    def get(self, index: int) -> Rectangle:
        """Rectangle del panel `index` (0-based)."""
        return self.rects()[index]

    # -- helpers de contenido -------------------------------------------

    def scale_factor(self, index: int, reference_frame_height: float = 8.0) -> float:
        """
        Factor de escala del panel `index` comparado con un frame de
        referencia de altura `reference_frame_height` (8 = default de Manim).

        Un panel de la mitad de esa altura da factor 0.5. Es la base para
        escalar de forma *consistente* texto y objetos entre paneles de
        distinto tamaño (en vez de que cada uno se estire al máximo de su
        propio panel, lo cual distorsiona el tamaño relativo entre ellos).
        """
        panel = self.get(index)
        return panel.height / reference_frame_height

    def font_size(
        self, index: int, base: float = 48, reference_frame_height: float = 8.0
    ) -> float:
        """Sugiere un font_size (en puntos) proporcional al tamaño real del panel."""
        return base * self.scale_factor(index, reference_frame_height)

    def scale_to_panel(
        self,
        mobject: Mobject,
        index: int,
        factor: float = 1.0,
        reference_frame_height: float = 8.0,
    ) -> Mobject:
        """
        Escala `mobject` a su tamaño "natural" multiplicado por el factor de
        escala del panel (proporcional a su altura respecto al frame de
        referencia) y lo centra en el panel.

        A diferencia de `fit()`, NO fuerza que el mobject llene el panel:
        conserva el tamaño relativo entre mobjects de distintos paneles.
        Útil para diagramas/vectores/figuras donde quieres que se vean
        proporcionalmente iguales sin importar cuán chico sea cada panel
        (ej. landscape 4 paneles vs. portrait 1 panel por fila).

        `factor` es un multiplicador extra tuyo (por si el objeto es
        naturalmente muy grande o chico y quieres ajustarlo a mano).
        """
        s = self.scale_factor(index, reference_frame_height) * factor
        mobject.scale(s)
        mobject.move_to(self.get(index).get_center())
        return mobject

    def animate_fit(self, mobject: Mobject, index: int, buff: float = 0.15):
        """
        Como `fit()`, pero NO muta `mobject` de inmediato: calcula el
        escalado/posición objetivo y devuelve un `.animate` listo para
        `self.play()`. Así puedes animar el desplazamiento en vez de que
        el objeto salte de golpe a su lugar.

        Uso:
            self.play(layout.animate_fit(mi_objeto, index=1))

        Útil también para mover un mismo objeto entre paneles de layouts
        distintos (ej. de un layout de 2 paneles a uno de 4):
            self.play(layout_4.animate_fit(mi_objeto, index=2))
        """
        panel = self.get(index)
        avail_w = panel.width - 2 * buff
        avail_h = panel.height - 2 * buff
        scale = avail_w / mobject.width
        if mobject.height * scale > avail_h:
            scale = avail_h / mobject.height
        return mobject.animate.move_to(panel.get_center())

    def morph_to(self, borders: VGroup, other: "PanelLayout") -> list[Transform]:
        """
        Devuelve una lista de `Transform` que morfean cada rectángulo de
        `borders` (creado antes con `self.show_borders()`) hacia la
        posición/tamaño de los paneles de `other`. Sirve para animar el
        cambio de un layout a otro (2 paneles -> 4 paneles, landscape ->
        portrait, distinta variante, etc.).

        El orden de `borders` debe corresponder al índice de panel (0, 1, 2...),
        igual que devuelve `show_borders()`/`rects()`.

        Uso:
            layout_a = PanelLayout(n_panels=2)
            layout_b = PanelLayout(n_panels=4)
            borders = layout_a.show_borders()
            self.play(Create(borders))
            ...
            self.play(*layout_a.morph_to(borders, layout_b))
        """
        if len(borders) != other.n_panels:
            raise ValueError(
                f"El número de bordes ({len(borders)}) no coincide con los "
                f"paneles del layout destino ({other.n_panels})."
            )
        target_rects = other.rects()
        return [Transform(borders[i], target_rects[i]) for i in range(len(borders))]

    def anchor(self, index: int, direction=ORIGIN, buff: float = 0.15):
        """
        Punto de anclaje dentro del panel `index`, en una dirección dada.

        `direction` usa las constantes de Manim: ORIGIN (centro), UP, DOWN,
        LEFT, RIGHT, y las esquinas UL, UR, DL, DR (o combinaciones tipo
        `UP + RIGHT`). `buff` es cuánto se "achica" hacia adentro del panel
        desde ese borde/esquina (0 = justo en el borde). El buff se aplica
        por eje de forma independiente (igual que `to_corner` en Manim), no
        en diagonal, para que quede simétrico en las esquinas.
        """
        panel = self.get(index)
        point = panel.get_critical_point(direction)
        dx, dy = direction[0], direction[1]
        shift = np.array(
            [
                -buff if dx > 0 else (buff if dx < 0 else 0.0),
                -buff if dy > 0 else (buff if dy < 0 else 0.0),
                0.0,
            ]
        )
        return point + shift

    def place(
        self, mobject: Mobject, index: int, direction=ORIGIN, buff: float = 0.15
    ) -> Mobject:
        """
        Ubica `mobject` en un borde/esquina del panel `index`, alineando el
        punto correspondiente del propio `mobject` (no solo su centro) con
        el anclaje del panel — igual que `to_edge()`/`to_corner()` de Manim,
        pero relativo al panel en vez de al frame completo.

        Ejemplos:
            layout.place(texto, index=0, direction=UP)       # arriba, centrado horiz.
            layout.place(texto, index=0, direction=DOWN)     # abajo, centrado horiz.
            layout.place(texto, index=0, direction=LEFT)     # pegado a la izquierda
            layout.place(texto, index=0, direction=UR)       # esquina superior-derecha
            layout.place(texto, index=0)                     # centro (equivale a fit sin escalar)
        """
        target = self.anchor(index, direction, buff)
        mobject.shift(target - mobject.get_critical_point(direction))
        return mobject

    def animate_place(
        self, mobject: Mobject, index: int, direction=ORIGIN, buff: float = 0.15
    ):
        """Versión animada de `place()`: devuelve un `.animate` para usar con `self.play()`."""
        target = self.anchor(index, direction, buff)
        return mobject.animate.shift(target - mobject.get_critical_point(direction))

    def center_direction(self, index: int) -> np.ndarray:
        """
        Dirección hacia el "gap" central de la composición que le corresponde
        al panel `index`, según su posición en la grilla:
        - paneles de la fila de arriba -> empujan su contenido hacia abajo
        - paneles de la fila de abajo -> empujan su contenido hacia arriba
        - paneles de la columna izquierda -> empujan su contenido a la derecha
        - paneles de la columna derecha -> empujan su contenido a la izquierda
        - si el panel está en el medio de una grilla impar (sin "lado" hacia
          el que converger en ese eje), ese eje queda en 0 (sin empuje).

        Pensado para usar con `place()`/`animate_place()` y lograr que el
        contenido de paneles contiguos se vea más "junto" hacia el centro de
        la composición, en vez de quedar centrado en cada panel por separado
        (ej. 2 paneles apilados en modo vertical).
        """
        cell = self.spec.cells[index]
        cols, rows = self.spec.cols, self.spec.rows
        mid_col = (cols - 1) / 2
        mid_row = (rows - 1) / 2
        cell_col_center = cell.col + (cell.col_span - 1) / 2
        cell_row_center = cell.row + (cell.row_span - 1) / 2

        dx = (
            1.0
            if cell_col_center < mid_col
            else (-1.0 if cell_col_center > mid_col else 0.0)
        )
        dy = (
            -1.0
            if cell_row_center < mid_row
            else (1.0 if cell_row_center > mid_row else 0.0)
        )
        return np.array([dx, dy, 0.0])

    def place_toward_center(
        self, mobject: Mobject, index: int, buff: float = 0.15
    ) -> Mobject:
        """Como `place()`, pero calcula la dirección automáticamente con
        `center_direction()` para que el contenido converja hacia el centro
        de la composición en vez de quedar centrado en su panel."""
        return self.place(
            mobject, index, direction=self.center_direction(index), buff=buff
        )

    def animate_place_toward_center(
        self, mobject: Mobject, index: int, buff: float = 0.15
    ):
        """Versión animada de `place_toward_center()`."""
        return self.animate_place(
            mobject, index, direction=self.center_direction(index), buff=buff
        )

    def fit(
        self,
        mobject: Mobject,
        index: int,
        buff: float = 0.15,
        auto_font_size: bool = False,
        base_font_size: float = 48,
    ) -> Mobject:
        """Escala y centra `mobject` para que quepa dentro del panel `index`.

        Si `auto_font_size=True` y `mobject` es Text/Tex/MathTex (tiene
        atributo `font_size`), primero se le asigna el font_size sugerido
        por `self.font_size(index, base=base_font_size)` antes de encajarlo;
        así el texto no depende de `set_max_width` para verse chico, que
        puede distorsionar el grosor visual en textos muy largos.
        """
        if auto_font_size and hasattr(mobject, "font_size"):
            mobject.font_size = base_font_size * self.scale_factor(index)

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
        DOWN,
        GREEN,
        LEFT,
        RED,
        RIGHT,
        UP,
        UR,
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

    class DemoPlaceScene(Scene):
        """Coloca objetos en distintos bordes/esquinas de un mismo panel."""

        def construct(self):
            layout = PanelLayout(n_panels=1)
            borders = layout.show_borders()
            self.add(borders)

            arriba = Text("arriba", font_size=24)
            abajo = Text("abajo", font_size=24)
            izq = Text("izq", font_size=24)
            der = Text("der", font_size=24)
            esquina = Text("UR", font_size=24)
            centro = Text("centro", font_size=24)

            layout.place(arriba, index=0, direction=UP)
            layout.place(abajo, index=0, direction=DOWN)
            layout.place(izq, index=0, direction=LEFT)
            layout.place(der, index=0, direction=RIGHT)
            layout.place(esquina, index=0, direction=UR)
            layout.place(centro, index=0)  # direction=ORIGIN por defecto

            self.play(*[Write(t) for t in (arriba, abajo, izq, der, esquina, centro)])
            self.wait()

    class DemoAnimatedScene(Scene):
        """Muestra: 1) animar un objeto encajando en su panel con animate_fit,
        y 2) animar la transición de un layout de 2 paneles a uno de 4."""

        def construct(self):
            layout2 = PanelLayout(n_panels=2)
            borders = layout2.show_borders()
            self.play(Create(borders))

            circ = Circle(color=BLUE, radius=1)
            self.add(circ)
            # se desplaza y escala animado hacia el panel 0, en vez de saltar
            self.play(layout2.animate_fit(circ, index=0))
            self.wait()

            # transición animada: de 2 paneles a 4 paneles
            layout4 = PanelLayout(n_panels=4)
            self.play(*layout2.morph_to(borders, layout4))
            self.play(layout4.animate_fit(circ, index=2))
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
