# P01 — Variable Aleatoria vs Número Aleatorio

**Escena:** `P01RandomVar` — `stats/p01_random_var.py`
**Total animaciones:** ~82 | **Duración estimada:** ~50 seg

---

## Sección 1 — Pelotas (eventos NO numéricos)

Aparecen 7 bolas (3 rojas, 2 blancas, 2 azules). Se agrupan por color y se
muestra la probabilidad de cada color en una fila. Se verifica que suman 1 y
se concluye que los eventos **no son números** (son palabras).

| # | Animación | Objeto | Texto en pantalla |
|---|-----------|--------|-------------------|
| 1–2 | `Write` | `label1` | "V. Aleatoria" (esquina sup. izq., amarillo) |
| 3–9 | `Create(ball) + Write(label)` ×7 | 7 círculos + etiquetas | roja, roja, roja, blanca, blanca, azul, azul |
| 10–11 | `Write` + `FadeOut` | `S = \{roja, blanca, azul\}` | — |
| 12–14 | `Create(rect)` ×3 | rectángulo rojo, blanco, azul rodeando cada grupo | — |
| 15–17 | `Write` ×3 | `P(roja) = 3/7`, `P(blanca) = 2/7`, `P(azul) = 2/7` (coloreados) | — |
| 18–20 | `FadeOut(rect)` ×3 | limpia rectángulos | — |
| 21–22 | `Write` + wait | `3/7 + 2/7 + 2/7 = 7/7 = 1` | — |
| 23–24 | `Write` + wait | **"Los eventos NO son números"** (verde) | — |
| 25 | `FadeOut(Group)` | limpia sección | — |

---

## Sección 2 — Dado (eventos SÍ numéricos)

Seis cuadrados numerados del 1 al 6 en grid 2×3. Se muestra el conjunto
\( A = \{1,2,3,4,5,6\} \), se igualan las probabilidades a \( \frac{1}{6} \),
suman 1, y se concluye que los eventos **sí son números**.

| # | Animación | Objeto | Texto en pantalla |
|---|-----------|--------|-------------------|
| 1 | `Write` | `label2` | "Número Aleatorio" (esquina sup. izq., amarillo) |
| 2–7 | `Create(square) + Write(num)` ×6 | 6 cuadrados con número dentro | 1, 2, 3, 4, 5, 6 |
| 8–9 | `Write` + wait | \( A = \{1, 2, 3, 4, 5, 6\} \) | — |
| 10–11 | `Write` + wait | \( P(1) = P(2) = \cdots = P(6) = \frac{1}{6} \) | — |
| 12–13 | `Write` + wait | \( 6 \times \frac{1}{6} = 1 \) | — |
| 14–15 | `Write` + wait | **"Los eventos SÍ son números"** (verde) | — |
| 16 | `FadeOut(Group)` | limpia sección | — |

---

## Sección 3 — Definición formal + cajas comparativas

Se construye la definición axiomática paso a paso: conjunto de eventos \( A \),
probabilidades acotadas entre 0 y 1, evento imposible vs. cierto, suma total
unitaria. Se introduce el concepto de **variable aleatoria discreta** (NA
finito/numerable) y de **número aleatorio** (eventos = números). Se cierra con
dos cajas enfrentadas que resumen el contraste.

| # | Animación | Objeto | Texto en pantalla |
|---|-----------|--------|-------------------|
| 1 | `Write` | `A = {a_j \mid j = 1, \dots, N_A}` | — |
| 2 | `Write` | \( 0 \leq P(a_j) \leq 1 \) | — |
| 3 | `Write` (2 simultáneos) | \( P(\emptyset) = 0 \) (evento imposible) + \( P(S) = 1 \) (evento cierto) | — |
| 4 | `Write` | \( \sum_{j=1}^{N_A} P(a_j) = 1 \) | — |
| 5 | `Write` ×3 | texto: «To simplify notation…» + \( \sum_a P(a) = 1 \) + «suppressing explicit mention…» (notación compacta futura) | — |
| 6 | `Write` (2 simultáneos) | «Si \( N_A \) es finito o numerable ⇒» + **variable aleatoria discreta** (amarillo) | — |
| 7 | `Write` (2 simultáneos) | «Si los eventos son números ⇒» + **número aleatorio** (amarillo) | — |
| 8 | `FadeOut(Group)` | limpia definición | — |
| 9 | `Write(box + content)` | **Caja izquierda:** Pelotas → {roja, blanca, azul} → NO son números → **Variable Aleatoria** | — |
| 10 | `Write(box + content)` | **Caja derecha:** Dado → {1,…,6} → SÍ son números → **Número Aleatorio** | — |
| 11 | `FadeOut(Group)` | cierre | — |

---

## Comandos

```bash
uv run manim -pql stats/p01_random_var.py P01RandomVar   # render pre vista baja
uv run manim -pqh stats/p01_random_var.py P01RandomVar   # render alta calidad
uv run ruff check stats/p01_random_var.py                 # lint
```

---

## Notación (para referencia futura)

> To simplify notation we will often write this equation as
>
> \[ \sum_a P(a) = 1 \]
>
> suppressing explicit mention of the number of elementary events.
```
