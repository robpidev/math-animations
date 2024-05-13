def vec_matrix(r1, r2) -> str:
    return r"\begin{bmatrix}" + f"{r1}" + r"\\" + f"{r2}" + r"\end{bmatrix}"


def vec(vec: list[int | str] = [0, 0]) -> str:
    return vec_matrix(f"{vec[0]}", f"{vec[1]}")


def vec_float(vec: list = [0, 0]) -> str:
    return vec_matrix(f"{vec[0]:.2f}", f"{vec[1]:.2f}")


def vec_comps(vec_name: str = "u") -> str:
    return vec_matrix(f"{vec_name}_x", f"{vec_name}_y")


def vec_add_int(u: list = [0, 0], v: list = [0, 0]) -> tuple:
    if v[0] >= 0:
        sx = f"{u[0]} + {v[0]}"
    else:
        sx = f"{u[0]} + ({v[0]})"

    if v[1] >= 0:
        sy = f"{u[1]} + {v[1]}"
    else:
        sy = f"{u[1]} + ({v[1]})"

    return vec_matrix(sx, sy)

def vec_add_float(u: list = [0, 0], v: list = [0, 0]) -> tuple:
    if v[0] > 0:
        sx = f"{u[0]:.2f} + {v[0]:.2f}"
    else:
        sx = f"{u[0]:.2f} - {-1 * v[0]:.2f}"

    if v[1] > 0:
        sy = f"{u[1]:.2f} + {v[1]:.2f}"
    else:
        sy = f"{u[1]:.2f} - {-1 * v[1]:.2f}"

    return vec_matrix(sx, sy)


def vec_add_comps(u: str = "u", v: str = "v") -> str:
    return vec_matrix(f"{u}_x + {v}_x", f"{u}_y + {v}_y")
