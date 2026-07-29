# math-anims

Manim animations for math topics (discrete math, linear algebra, logic, physics, neural networks).

## Verification

After writing a scene file, run `uv run ruff check <file>`. **Do not run `manim` commands** — no typecheck or render test needed.

## Commands

```bash
uv sync                        # install dependencies (uv, not pip)
uv run ruff check .            # lint config: line-length=88, select E,F,W,I,UP
```

## Code style

- **Imports:** Most scene files import Manim symbols explicitly (one per line), but `from manim import *` is accepted for simple scripts (`logic/01-propositions/portada.py`, `calc/dirac-delta/anim.py`, `physics/anim.py`).
- **Animations:** Prefer `Create`/`Write` to introduce elements, `Transform`/`ReplacementTransform`/`TransformMatchingShapes` for morphing, and `FadeOut(Group(...))` for cleanup. `self.next_section(skip_animations=True)` marks skip points during development.
- **Multi-part MathTex:** For step-by-step derivations use `MathTex("part1", "part2", ...)` so each brace group is a submobject addressable by index. `TransformMatchingShapes` morphs only the parts that change while leaving others static.
- **Accumulative derivations:** Stack each equation step **below** the previous one (`.next_to(prev, DOWN, aligned_edge=LEFT)`) so the full derivation remains visible on screen.
- **Dynamic values:** Use `ValueTracker` + `add_updater(lambda m: m.become(...))` for animated/interactive elements.
- **Grouping:** Use `VGroup` (not `Group`) almost exclusively for collections of mobjects. Arrange via `.arrange(DOWN)` / `.move_to()` / `.next_to()`.
- **Naming:** Scene classes are `PascalCase`, typically `P<Número><Descripción>` (e.g. `P1Def`, `P2Math`, `P6BinDec`). Files are `pXX_descripcion.py`.
- **No type hints** in most scene files — only utility modules (`funcs/`) occasionally use them.

## Architecture

- **Not a package** — each file is a standalone Manim `Scene` class. No unified entrypoint (`main.py` is a trivial placeholder).
- Independent scene files grouped by topic directory. Render directly with `manim`.
- **Directories:** `discret/` `vectors/` `FFNN/` `logic/` `physics/` `calc/` `stats/`
- **Shared utilities:** `vectors/00-definition/funcs/` and `vectors/01-length/funcs/` contain `vec2D_tex.py` (LaTeX helpers) and `vec_algebra.py` (vector operations), imported via relative imports from sibling scenes.
- Scene files follow pattern `pXX_descripcion.py` (numbered lesson order).

## Quirks

- `discret/pixel/p8_pixel_bit.py` imports `from bites` (not `from ..bites`). Run from `discret/pixel/` or adjust `PYTHONPATH` to resolve.
- `vectors/01-length/p00-intro.py` is an empty placeholder.
- Some files use `from manim import *` — acceptable convention for Manim scripts.
- Video output saved to `media/` (gitignored).
- Requires Python >= 3.13 (see `.python-version`).
