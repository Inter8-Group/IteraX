import numpy as np  # Importamos la librería numpy para trabajar con matrices 

def gauss_jordan(matriz_coeficientes, vector_resultados):
    """
    Esta función aplica el método de Gauss-Jordan para resolver sistemas de ecuaciones lineales.
    Parámetros:
        matriz_coeficientes: la matriz A del sistema (n x n)
        vector_resultados: el vector b del sistema (n)
    Retorna:
        Una tupla con:
        - el vector solución
        - la matriz extendida reducida final
    """

    # Paso 1: Convertimos la matriz A y el vector b en una sola matriz extendida [A | b]
    cantidad_ecuaciones = len(matriz_coeficientes)
    matriz_extendida = np.hstack((matriz_coeficientes.astype(float), vector_resultados.reshape(-1, 1)))

    # Paso 2: Aplicamos el proceso de eliminación Gauss-Jordan
    for fila_actual in range(cantidad_ecuaciones):
        # Paso 2.1: Asegurarse de que el elemento de la diagonal no sea cero
        if matriz_extendida[fila_actual][fila_actual] == 0:
            for fila_siguiente in range(fila_actual + 1, cantidad_ecuaciones):
                if matriz_extendida[fila_siguiente][fila_actual] != 0:
                    # Intercambiamos las filas si encontramos una con valor distinto de cero
                    matriz_extendida[[fila_actual, fila_siguiente]] = matriz_extendida[[fila_siguiente, fila_actual]]
                    break

        # Paso 2.2: Hacemos que el elemento de la diagonal sea 1 (dividiendo toda la fila)
        pivote = matriz_extendida[fila_actual][fila_actual]
        matriz_extendida[fila_actual] = matriz_extendida[fila_actual] / pivote

        # Paso 2.3: Hacemos cero el resto de la columna
        for otra_fila in range(cantidad_ecuaciones):
            if otra_fila != fila_actual:
                factor = matriz_extendida[otra_fila][fila_actual]
                matriz_extendida[otra_fila] = matriz_extendida[otra_fila] - factor * matriz_extendida[fila_actual]

    # Paso 3: Extraemos la solución desde la última columna
    solucion = matriz_extendida[:, -1]

    # Retornamos la solución y la matriz reducida final (por si se quiere ver el proceso)
    return solucion, matriz_extendida

def main():
    print("Método de Gauss-Jordan para resolver sistemas de ecuaciones lineales")

    # Pedimos al usuario cuántas ecuaciones tendrá el sistema
    cantidad = int(input("Ingrese el número de ecuaciones (n variables): "))

    # Creamos la matriz A y el vector b
    matriz_A = np.zeros((cantidad, cantidad))
    vector_b = np.zeros(cantidad)

    print("\nIngrese los coeficientes de la matriz A fila por fila:")
    for i in range(cantidad):
        while True:
            fila = input(f"Ingrese los {cantidad} coeficientes de la fila {i+1}, separados por espacios: ").split()
            if len(fila) == cantidad:
                try:
                    matriz_A[i] = [float(x) for x in fila]
                    break
                except ValueError:
                    print("Por favor, ingrese solo números.")
            else:
                print(f"Debe ingresar exactamente {cantidad} números.")

    print("\nIngrese los términos independientes del vector b:")
    for i in range(cantidad):
        while True:
            try:
                vector_b[i] = float(input(f"b[{i+1}]: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

    # Llamamos a la función que resuelve el sistema
    solucion, matriz_reducida = gauss_jordan(matriz_A, vector_b)

    print("\nMatriz extendida reducida final:")
    print(matriz_reducida)

    print("\nSolución del sistema:")
    for i in range(cantidad):
        print(f"x{i+1} = {solucion[i]:.6f}")

if __name__ == "__main__":
    main()