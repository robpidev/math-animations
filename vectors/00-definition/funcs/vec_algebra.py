from math import cos, pi, sin


def vec_ab(a: list, b: list) -> list:
    return [j - i for i, j in zip(a, b)]


def vec_add(u: list, v: list) -> list:
    return [i + j for i, j in zip(u, v)]


def vec_sub(u: list, v: list) -> list:
    return [i - j for i, j in zip(u, v)]


def vec_mod_angled(mod: float, angle: float) -> list:
    return [mod * cos(angle * pi / 180), mod * sin(angle * pi / 180), 0]


def vec_scale(k: int, u: list) -> list:
    return [k * i for i in u]
