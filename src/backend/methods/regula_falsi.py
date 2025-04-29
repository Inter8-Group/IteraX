import numpy as np

def __crear_funcion(func_str):
    """
    Convierte una cadena que representa una función matemática
    en una función evaluable en Python.

    Parámetro:
    - func_str: str, función matemática (ejemplo: "x**2 - 4")

    Retorna:
    - función evaluable f(x)
    """
    def f(x):
        return eval(func_str, {"x": x, "np": np, "numpy": np, "__builtins__": {}})
    return f

def regula_falsi(func_str, a, b, itermax=10, error_maximo=1e-6):
    """
    Implementa el método de Regula Falsi para encontrar una raíz de la función
    dentro del intervalo [a, b], usando una cantidad máxima de iteraciones y
    una tolerancia de error.

    Parámetros:
    - func_str: str, función matemática como cadena (ejemplo: "x**2 - 4")
    - a: float, extremo izquierdo del intervalo
    - b: float, extremo derecho del intervalo
    - itermax: int, número máximo de iteraciones (default=10)
    - error_maximo: float, tolerancia del error (default=1e-6)

    Retorna:
    - tabla_resultado: list[dict], lista con los datos de cada iteración
    """
    F = __crear_funcion(func_str)
    tabla_resultado = []

    # Verifica que f(a) y f(b) tengan signos opuestos
    if F(a) * F(b) > 0:
        raise ValueError("Intervalo inválido: f(a) * f(b) > 0")

    iteracion = 0
    error = 1
    x_anterior = a
    fa = F(a)
    fb = F(b)

    # Itera hasta alcanzar el máximo de iteraciones o que el error sea aceptable
    while iteracion < itermax and error > error_maximo:
        iteracion += 1
        # Punto medio calculado por la fórmula de regula falsi
        x = (a * fb - b * fa) / (fb - fa)
        fx = F(x)

        # Guarda datos de la iteración
        paso = {
            "iteración": iteracion,
            "a": a,
            "b": b,
            "x": x,
            "f(x)": fx
        }
        tabla_resultado.append(paso)

        # Actualiza el intervalo dependiendo del signo
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        # Calcula el error relativo
        error = abs(x - x_anterior)
        x_anterior = x

    return tabla_resultado

