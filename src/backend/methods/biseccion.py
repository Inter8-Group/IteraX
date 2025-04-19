
def biseccion(f, a, b, tol=1e-5, max_iter=100):
    pasos = []
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        pasos.append({"iteracion": i+1, "a": a, "b": b, "c": c, "f(c)": fc})

        if abs(fc) < tol or abs(b - a) < tol:
            return c, pasos

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c, pasos
