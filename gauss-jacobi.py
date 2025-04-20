import numpy as np  # Importamos numpy para manejar matrices y operaciones numéricas

def gauss_jacobi(matriz_coeficientes, vector_resultados, tolerancia=1e-6, maximo_iteraciones=100):
    """
    Esta función resuelve un sistema de ecuaciones lineales usando el método iterativo de Gauss-Jacobi.
    Parámetros:
        matriz_coeficientes: matriz cuadrada A del sistema
        vector_resultados: vector b del sistema
        tolerancia: error relativo mínimo para detenerse
        maximo_iteraciones: cantidad máxima de iteraciones a realizar
    Retorna:
        vector_solucion: solución aproximada
        iteraciones_realizadas: cantidad de iteraciones ejecutadas
        errores: error relativo de cada variable en la última iteración
    """
    cantidad_variables = len(matriz_coeficientes)
    
    # Inicializamos la solución actual como vector de ceros
    solucion_actual = np.zeros(cantidad_variables)

    for iteracion in range(maximo_iteraciones):
        nueva_solucion = np.zeros(cantidad_variables)

        # Para cada variable, calculamos su nuevo valor
        for i in range(cantidad_variables):
            suma = 0
            for j in range(cantidad_variables):
                if j != i:
                    suma += matriz_coeficientes[i][j] * solucion_actual[j]

            nueva_solucion[i] = (vector_resultados[i] - suma) / matriz_coeficientes[i][i]

        # Calculamos los errores relativos
        errores = np.zeros(cantidad_variables)
        for i in range(cantidad_variables):
            if nueva_solucion[i] != 0:
                errores[i] = abs((nueva_solucion[i] - solucion_actual[i]) / nueva_solucion[i]) * 100
            else:
                errores[i] = abs(nueva_solucion[i] - solucion_actual[i]) * 100  # evita dividir por 0

        # Si todos los errores están dentro de la tolerancia, terminamos
        if np.all(errores < tolerancia):
            return nueva_solucion, iteracion + 1, errores

        # Actualizamos la solución para la próxima iteración
        solucion_actual = nueva_solucion

    # Si no converge, devolvemos la última solución obtenida
    return solucion_actual, maximo_iteraciones, errores

def main():
    print("Método de Gauss-Jacobi para resolver sistemas de ecuaciones lineales")

    # Pedimos al usuario la cantidad de ecuaciones y variables
    cantidad = int(input("Ingrese el número de ecuaciones (y variables): "))

    # Creamos una matriz de ceros para los coeficientes y el vector b
    matriz_coeficientes = np.zeros((cantidad, cantidad))
    vector_independientes = np.zeros(cantidad)

    print("\nIngrese los coeficientes de la matriz A, fila por fila:")
    for i in range(cantidad):
        while True:
            fila = input(f"Ingrese los {cantidad} coeficientes de la fila {i+1}, separados por espacios: ").split()
            if len(fila) == cantidad:
                try:
                    matriz_coeficientes[i] = [float(x) for x in fila]
                    break
                except ValueError:
                    print("Por favor, ingrese solo números.")
            else:
                print(f"Debe ingresar exactamente {cantidad} números.")

    print("\nIngrese los términos independientes del vector b:")
    for i in range(cantidad):
        while True:
            try:
                vector_independientes[i] = float(input(f"b[{i+1}]: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

    # Parámetros del método
    tolerancia = float(input("\nIngrese la tolerancia (por ejemplo, 1e-6): "))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

    # Llamamos a la función principal que resuelve el sistema
    solucion, iteraciones, errores = gauss_jacobi(
        matriz_coeficientes,
        vector_independientes,
        tolerancia,
        max_iteraciones
    )

    # Mostramos los resultados
    print(f"\nSolución aproximada encontrada en {iteraciones} iteraciones:")
    for i in range(cantidad):
        print(f"x{i+1} = {solucion[i]:.6f} (error: {errores[i]:.6f}%)")

if __name__ == "__main__":
    main() 