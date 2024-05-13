from math import cos, sin, pi


def vec_ab(a: list, b: list) -> list:
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]

def vec_add(u: list, v: list) -> list:
    return [u[0] + v[0], u[1] + v[1], u[2] + v[2]]

def vec_mod_angled(mod: float, angle: float) -> list:
    return [mod * cos(angle * pi/180),
            mod * sin(angle * pi/180),
            0]


