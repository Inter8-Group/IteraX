import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def __crear_funcion(func_str):
    """
    Convierte una cadena que representa una función matemática
    en una función evaluable en Python.
    """
    def f(x):
        return eval(func_str, {"x": x, "np": np, "numpy": np, "__builtins__": {}})
    return f

def regula_falsi(func_str, a, b, itermax=10, error_maximo=1e-6):
    F = __crear_funcion(func_str)
    tabla_resultado = []

    if F(a) * F(b) > 0:
        raise ValueError("Intervalo inválido: f(a) * f(b) > 0")

    iteracion = 0
    error = 1
    x_anterior = a
    fa = F(a)
    fb = F(b)
    puntos_x = []

    while iteracion < itermax and error > error_maximo:
        iteracion += 1
        x = (a * fb - b * fa) / (fb - fa)
        fx = F(x)
        puntos_x.append(x)

        paso = {
            "iteracion": iteracion,
            "a": round(a, 6),
            "b": round(b, 6),
            "c": round(x, 6),
            "f(c)": f"{fx:.4e}",
            "error": f"{error:.4e}" if iteracion > 1 else "---"
        }
        tabla_resultado.append(paso)

        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        error = abs(x - x_anterior)
        x_anterior = x

    # Graficar f(x)
    x_vals = np.linspace(a - 1, b + 1, 200)
    y_vals = [F(xi) for xi in x_vals]

    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, y_vals, label="f(x)", color='blue')
    plt.axhline(0, color='black', linestyle='--')
    plt.scatter(puntos_x, [F(xi) for xi in puntos_x], color='red', label='Puntos de iteración')
    plt.title("Método de Regula-Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    return x, tabla_resultado, imagen_base64


