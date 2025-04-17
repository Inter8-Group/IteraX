import math

# esto transforma el texto en una funcion evaluable
def crearFuncion(funcion_str):
    def f(x):
        return eval(funcion_str, {"x": x, "math": math})
    return f

# aca va el metodo
def biseccion(a, b, tol, max_iter, funcion_str):
    f = crearFuncion(funcion_str)

    if f(a) * f(b) >= 0:
        return "El método de bisección no es aplicable. f(a) y f(b) deben tener signos opuestos."

    iteracion = 0
    c_ant = a

    while iteracion < max_iter:
        c = (a + b) / 2.0
        error_rel = abs((c - c_ant) / c) * 100 if iteracion > 0 else None

        print(f"Iter {iteracion+1}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={f(c):.6f}", end="")
        if error_rel is not None:
            print(f", error_rel={error_rel:.6f}%")
        else:
            print("")

        if abs(f(c)) < tol:
            print("\nCriterio de f(c) suficientemente cercano a 0 alcanzado.")
            return round(c, 6)
        if error_rel is not None and error_rel < tol:
            print("\nCriterio de error relativo alcanzado.")
            return round(c, 6)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_ant = c
        iteracion += 1

    print("\nNúmero máximo de iteraciones alcanzado.")
    return round(c, 6)

# parte del usuario
try:
    funcion_str = input("Ingresa la función f(x): ")
    a = float(input("Ingresa el extremo izquierdo a: "))
    b = float(input("Ingresa el extremo derecho b: "))
    tol = float(input("Ingresa la tolerancia (ej: 0.001): "))
    max_iter = int(input("Máx. número de iteraciones: "))

    raiz = biseccion(a, b, tol, max_iter, funcion_str)

    print(f"\nRaíz aproximada: {raiz}")

except Exception as e:
    print(f" Ocurrió un error: {e}")