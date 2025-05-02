import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def __crear_funcion(func_str):
    """
    Convierte una cadena que representa una función matemática
    en una función evaluable en Python.
    
    Parámetros:
    func_str (str): Una cadena que representa la función matemática en términos de 'x'.
    
    Retorna:
    func (function): Una función de Python que puede ser evaluada con un valor para 'x'.
    
    Ejemplo:
    Si func_str es "np.sin(x)", la función retornada será una función que calcule 
    el seno de 'x' usando la librería NumPy.
    """
    def f(x):
        # Evaluar la expresión matemática usando eval()
        return eval(func_str, {"x": x, "np": np, "numpy": np, "__builtins__": {}})
    return f

def regula_falsi(func_str, a, b, itermax=10, error_maximo=1e-6):
    """
    Aplica el método de Regula-Falsi para encontrar la raíz de una función dentro de un intervalo dado.
    
    Parámetros:
    func_str (str): Cadena que representa la función matemática que queremos analizar.
    a (float): Extremo izquierdo del intervalo en el que se busca la raíz.
    b (float): Extremo derecho del intervalo en el que se busca la raíz.
    itermax (int): Número máximo de iteraciones para el método. Por defecto es 10.
    error_maximo (float): Error máximo permitido para la convergencia. Por defecto es 1e-6.
    
    Retorna:
    x (float): La raíz estimada de la función.
    tabla_resultado (list): Una lista de diccionarios con los pasos de la iteración, mostrando la evolución de los valores.
    imagen_base64 (str): La representación en base64 de la gráfica generada.
    
    Excepciones:
    Si f(a) * f(b) > 0, el método lanzará un ValueError indicando que el intervalo es inválido.
    
    Ejemplo:
    Si func_str es "x**3 - 2*x - 5", a=2, b=3, itermax=20, el método intentará encontrar la raíz de esta función en el intervalo [2, 3].
    """
    # Crear la función a partir de la cadena proporcionada
    F = __crear_funcion(func_str)
    
    # Lista que almacenará los pasos de la iteración para mostrar en la tabla
    tabla_resultado = []

    # Comprobar que el intervalo es válido (f(a) * f(b) debe ser negativo)
    if F(a) * F(b) > 0:
        raise ValueError("Intervalo inválido: f(a) * f(b) > 0")

    # Inicialización de variables
    iteracion = 0
    error = 1
    x_anterior = a
    fa = F(a)
    fb = F(b)
    puntos_x = []  # Lista para almacenar los puntos de intersección (raíces estimadas)

    # Iteración del método de Regula-Falsi
    while iteracion < itermax and error > error_maximo:
        iteracion += 1
        # Fórmula de Regula-Falsi
        x = (a * fb - b * fa) / (fb - fa)
        fx = F(x)
        puntos_x.append(x)  # Guardamos los puntos de intersección

        # Crear un diccionario con los resultados de la iteración actual
        paso = {
            "iteracion": iteracion,
            "a": round(a, 6),
            "b": round(b, 6),
            "c": round(x, 6),
            "f(c)": f"{fx:.4e}",
            "error": f"{error:.4e}" if iteracion > 1 else "---"
        }
        tabla_resultado.append(paso)

        # Actualizar el intervalo dependiendo de si el signo de f(a) y f(c) son opuestos
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        # Calcular el error como la diferencia entre la nueva y la anterior estimación
        error = abs(x - x_anterior)
        x_anterior = x

    # Generación de la gráfica de la función
    x_vals = np.linspace(a - 1, b + 1, 200)
    y_vals = [F(xi) for xi in x_vals]

    # Crear la gráfica
    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, y_vals, label="f(x)", color='blue')
    plt.axhline(0, color='black', linestyle='--')
    plt.scatter(puntos_x, [F(xi) for xi in puntos_x], color='red', label='Puntos de iteración')
    plt.title("Método de Regula-Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)

    # Guardar la imagen en un buffer para convertirla a base64
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    # Codificar la imagen en base64
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Retornar la raíz, la tabla de resultados y la imagen en base64
    return x, tabla_resultado, imagen_base64



