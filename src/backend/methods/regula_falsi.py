import numpy as np

def __crear_funcion(func_str):
    def f(x):
        return eval(func_str, {"x": x, "np": np, "__builtins__": {}})
    return f

def regula_falsi(func_str, a, b, itemax=10, errormax=1e-6):
    f = __crear_funcion(func_str)
    tablaresultado = []

    if f(a) * f(b) > 0:
        raise ValueError("Intervalo inválido: f(a) * f(b) > 0")

    ite = 0
    error = 1
    c_old = a
    fa, fb = f(a), f(b)

    while ite < itemax and error > errormax:
        ite += 1
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        paso = {
            "iteracion": ite,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc
        }
        tablaresultado.append(paso)

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

        error = abs((c - c_old) / c)
        c_old = c

    return c, tablaresultado
