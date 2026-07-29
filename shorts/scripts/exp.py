def abs(n: float) -> float:
    if n < 0:
        return -1 * n

    return n

assert abs(1.5) == 1.5
assert abs(-2.123) == 2.123

def factorial(n: int) -> int:
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1


def exp(x, m) -> float:
    """
    La variable ```x```: exponente; ```m``` cifras de precisas
    """

    e, e_ant = 1, 0

    i = 1
    while abs(e - e_ant) >= 10 ** (-m):
        e_ant = e
        e += x ** i / factorial(i)

        if i >= 1000: break
        
        i += 1

    return e


print(exp(5, 15))
print("2.718281828459045")
