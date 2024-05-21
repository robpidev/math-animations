def vec_matrix(r1, r2) -> str:
    return r"\begin{bmatrix}" + f"{r1}" + r"\\" + f"{r2}" + r"\end{bmatrix}"


def vec(vec: list[int | str] = [0, 0]) -> str:
    return vec_matrix(f"{vec[0]}", f"{vec[1]}")


def vec_float(vec: list = [0, 0]) -> str:
    return vec_matrix(f"{vec[0]:.2f}", f"{vec[1]:.2f}")


def vec_comps(vec_name: str = "u") -> str:
    """
    takes ```u``` and return 
    ⎡u_x⎤
    ⎣u_y⎦
    """

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


def vec_less_int(u: list = [0, 0], v: list = [0, 0]) -> tuple:

    sx = f"{u[0]} - {v[0]}"
    sy = f"{u[1]} - {v[1]}"

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
    """
    return ⎡u_x + v_x⎤
           ⎣u_y _ v_y⎦
    """

    return vec_matrix(f"{u}_x + {v}_x", f"{u}_y + {v}_y")

def vec_sub_comps(u: str = "u", v: str = "v") -> str:
    """
    return ⎡u_x - v_x⎤
           ⎣u_y - v_y⎦
    """
    return vec_matrix(f"{u}_x - {v}_x", f"{u}_y - {v}_y")

def vec_sub_int(u: list = [0, 0], v: list = [0, 0]) -> tuple:
    """
    Takes a vector ```u``` in ```Z``` and a vector ```v``` in ```Z```
    and return  ⎡a - d⎤
                ⎣c - d⎦

    or si c or d < 0
                ⎡a - (-d)⎤
                ⎣c - (-d)⎦

    """
    if v[0] >= 0:
        sx = f"{u[0]} - {v[0]}"
    else:
        sx = f"{u[0]} - ({v[0]})"

    if v[1] >= 0:
        sy = f"{u[1]} - {v[1]}"
    else:
        sy = f"{u[1]} - ({v[1]})"

    return vec_matrix(sx, sy)


def vec_scalar(scale: int | str = 1, vec: list | str = [0, 0]) -> list [int | str]:
    return f"{scale}" + f"{vec(vec)}"


def vec_scalar_comps(scale: int|str, vec: list[int|str]) -> str:
    return vec_matrix(f"{scale} \\cdot {vec[0]}", f"{scale} \\cdot {vec[1]}")

def vec_scalar_var_comps(scalar="c", vec="u") -> str:
    """
    takes a scalar ```c``` and a vector ```u``` and return a latex string of
    ⎡c u_x⎤
    ⎣c u_y⎦
    """
    return vec_matrix(f"{scalar} \\cdot {vec}_x", f"{scalar} \\cdot {vec}_y")

