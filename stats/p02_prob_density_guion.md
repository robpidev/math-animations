# P02 — Densidad de Probabilidad (Normalización + Probabilidad)

**Escena:** `P02ProbDensity` — `stats/p02_prob_density.py`
**Duración estimada:** ~45 seg

---

## Fase 1 — Problema

Aparece el enunciado completo en 4 líneas apiladas. Luego se desvanece.

| # | Animación | Objeto | Texto en pantalla |
|---|-----------|--------|-------------------|
| 1 | `Write` | `title` | "Problema 5.1 — Densidades de probabilidad" |
| 2 | `Write` | `desc` | "Dada una variable aleatoria continua x, con densidad de probabilidad" |
| 3 | `Write` | `pdf_eq` | \( P(x) = A e^{-2x}, \quad x > 0 \) |
| 4 | `Write` | `question` | "Hallar el valor de A y la probabilidad de que x > 1" |
| 5 | `FadeOut` | `problem` | (se limpia todo) |

---

## Fase 2 — Normalización (\( \int P = 1 \to A = 2 \))

Cada ecuación aparece apilada debajo de la anterior. Las transiciones similares usan `TransformMatchingShapes` (solo morphs la parte que cambia); los cambios estructurales usan `Write`.

| # | Animación | Texto en pantalla | Tipo |
|---|-----------|-------------------|------|
| 1 | `Write(L1)` | \( \int_{0}^{\infty} P(x) \, dx = 1 \) | Write |
| 2 | `TMS(L1.copy → L2)` | \( \int_{0}^{\infty} A e^{-2x} \, dx = 1 \) | Morph (solo parte [1]) |
| 3 | `Write(L3)` | \( A \int_{0}^{\infty} e^{-2x} \, dx = 1 \) | Write (cambio estructural) |
| 4 | `TMS(L3.copy → L4)` | \( A \left[ -\frac{1}{2} e^{-2x} \right]_{0}^{\infty} = 1 \) | Morph |
| 5 | `Write(L5)` | \( -\frac{A}{2} (0 - 1) = 1 \) | Write (cambio estructural) |
| 6 | `TMS(L5.copy → L6)` | \( \frac{A}{2} = 1 \) | Morph (simplifica) |
| 7 | `TMS(m56 → L7)` | \( A = 2 \) | Morph (resultado) |
| 8 | `FadeOut` | toda la pila | (se limpia) |

---

## Fase 3 — \( P(x > 1) \)

Mismo patrón: apilado acumulativo con morphing en cambios pequeños.

| # | Animación | Texto en pantalla | Tipo |
|---|-----------|-------------------|------|
| 1 | `Write(M1)` | \( P(x > 1) = \int_{1}^{\infty} 2 e^{-2x} \, dx \) | Write |
| 2 | `TMS(M1.copy → M2)` | \( P(x > 1) = 2 \left[ -\frac{1}{2} e^{-2x} \right]_{1}^{\infty} \) | Morph |
| 3 | `Write(M3)` | \( P(x > 1) = -\left( \lim_{x \to \infty} e^{-2x} - e^{-2} \right) \) | Write (cambio estructural) |
| 4 | `TMS(M3.copy → M4)` | \( P(x > 1) = e^{-2} \) | Morph (simplifica) |
| 5 | `TMS(n34 → M5)` | \( P(x > 1) = e^{-2} \approx 0.1353 \) | Morph (agrega ≈) |
| 6 | `FadeOut` | toda la pila | (se limpia) |

---

## Fase 4 — Respuesta final

Dos recuadros de esquinas redondeadas, apilados verticalmente, centrados.

| # | Animación | Texto en pantalla | Color |
|---|-----------|-------------------|-------|
| 1 | `Write` + `Create(box)` | \( A = 2 \) | Amarillo |
| 2 | `Write` + `Create(box)` | \( P(x > 1) = e^{-2} \approx 0.1353 \) | Verde |
| 3 | `wait(3)` | (pausa final) | — |

---

## Comandos

```bash
# Horizontal (landscape, 854×480 preview)
uv run manim -pql stats/p02_prob_density.py P02ProbDensity

# Vertical (portrait, 1080×1920 preview)
uv run manim -pql -r 1080,1920 stats/p02_prob_density.py P02ProbDensity

# Alta calidad
uv run manim -pqh stats/p02_prob_density.py P02ProbDensity
uv run manim -pqh -r 1080,1920 stats/p02_prob_density.py P02ProbDensity

# Lint
uv run ruff check stats/p02_prob_density.py
```
