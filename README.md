# math-anims

Manim animations for math topics: discrete math, linear algebra (vectors), logic, probability & statistics, calculus, physics, and neural networks.

## Topics

| Directory | Topic |
|-----------|-------|
| `discret/` | Bits, bytes, powers of two, binary ↔ decimal conversion, kilobyte vs kibibyte units, pixels & hex (`int/`, `pixel/` subfolders) |
| `vectors/00-definition/` | Definition of a vector, vector sets, addition & scalar multiplication axioms, field properties |
| `vectors/01-length/` | Vector norm/length, unit vectors, resultant, basis |
| `vectors/02-dot/` | Dot product and the cosine between two vectors |
| `FFNN/` | Feed-forward neural networks: neuron anatomy, weights/bias example, step activation |
| `logic/01-propositions/` | Propositional logic: definitions, simple/compound propositions, conditionals, biconditionals, notation |
| `stats/` | Random variables, probability density of a continuous variable |
| `sm/` | Probability: sample space of a die roll |
| `calc/dirac-delta/` | Dirac delta function visualization |
| `physics/` | Pendulum ODE, plank-and-boy torque problem |
| `shorts/` | Short-form videos: e^x Taylor series expansion |

## Requirements

- Python >= 3.13 (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) as the package manager

## Setup

```bash
uv sync
```

## Rendering a scene

Each file is a standalone Manim `Scene`. Render any scene with the `manim` CLI:

```bash
manim -pql discret/p1_def.py P1Def
```

Videos are written to `media/` (gitignored).

> Note: scenes with relative imports (e.g. `vectors/00-definition/p01_def.py`) should be rendered from their own directory, and `discret/pixel/p8_pixel_bit.py` uses a plain `from bites` import, so run it from `discret/pixel/`.

## Linting

```bash
uv run ruff check .
```

## Project structure

- Not a package: there is no unified entrypoint (`main.py` is a placeholder).
- Scene files follow `pXX_descripcion.py` naming and define `PascalCase` scene classes.
- Shared utilities live next to the scenes: `vectors/00-definition/funcs/` and `vectors/01-length/funcs/` provide LaTeX helpers and vector algebra helpers.

See `AGENTS.md` for code style and contribution conventions.
