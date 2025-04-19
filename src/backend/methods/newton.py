def newton_raphson(f, df, x0, tol, max_iter):
    pasos = []
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("La derivada es cero en x = {:.4f}".format(x0))
        x1 = x0 - fx / dfx
        error = abs(x1 - x0)
        pasos.append({"iteracion": i, "x": x0, "f(x)": fx, "error": error})
        if error < tol:
            return x1, pasos
        x0 = x1
    return x1, pasos
