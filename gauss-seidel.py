import numpy as np  # Librería para operaciones con matrices  

def es_matriz_diagonalmente_dominante(matriz_coeficientes):
    """
    Verifica si una matriz es diagonalmente dominante por filas.
    Esto ayuda a asegurar la convergencia del método de Gauss-Seidel.
    """
    cantidad_filas = len(matriz_coeficientes)
    for fila in range(cantidad_filas):
        suma_fuera_diagonal = 0
        for columna in range(cantidad_filas):
            if columna != fila:
                suma_fuera_diagonal += abs(matriz_coeficientes[fila][columna])
        if abs(matriz_coeficientes[fila][fila]) <= suma_fuera_diagonal:
            return False
    return True

def metodo_gauss_seidel(matriz_coeficientes, vector_independientes, vector_inicial=None, tolerancia=1e-6, iteraciones_maximas=100):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Seidel.
    Parámetros:
        matriz_coeficientes: matriz cuadrada con los coeficientes del sistema
        vector_independientes: vector con los términos independientes
        vector_inicial: estimación inicial de la solución
        tolerancia: tolerancia para el criterio de parada
        iteraciones_maximas: límite de iteraciones a ejecutar
    """
    cantidad_variables = len(matriz_coeficientes)

    # Si no se proporciona una solución inicial, se usa un vector de ceros
    if vector_inicial is None:
        solucion_actual = np.zeros(cantidad_variables)
    else:
        solucion_actual = np.array(vector_inicial, dtype=float)

    for numero_iteracion in range(iteraciones_maximas):
        nueva_solucion = np.copy(solucion_actual)

        for indice_variable in range(cantidad_variables):
            suma_parcial_izquierda = 0
            suma_parcial_derecha = 0

            # Usamos valores recién actualizados
            for j in range(indice_variable):
                suma_parcial_izquierda += matriz_coeficientes[indice_variable][j] * nueva_solucion[j]

            # Usamos valores aún no actualizados
            for j in range(indice_variable + 1, cantidad_variables):
                suma_parcial_derecha += matriz_coeficientes[indice_variable][j] * solucion_actual[j]

            # Calculamos el nuevo valor para la variable
            nueva_solucion[indice_variable] = (
                vector_independientes[indice_variable] - suma_parcial_izquierda - suma_parcial_derecha
            ) / matriz_coeficientes[indice_variable][indice_variable]

        # Calculamos el error relativo porcentual de cada variable
        errores_relativos = np.zeros(cantidad_variables)
        for i in range(cantidad_variables):
            if nueva_solucion[i] != 0:
                errores_relativos[i] = abs((nueva_solucion[i] - solucion_actual[i]) / nueva_solucion[i]) * 100
            else:
                errores_relativos[i] = abs(nueva_solucion[i] - solucion_actual[i]) * 100  # evita división por cero

        # Si todos los errores están dentro del margen de tolerancia, terminamos
        if np.all(errores_relativos < tolerancia):
            return nueva_solucion, numero_iteracion + 1, errores_relativos

        # Actualizamos la solución para la siguiente iteración
        solucion_actual = nueva_solucion

    # Si no converge en el número máximo de iteraciones, lanzamos error
    raise Exception("No se alcanzó la convergencia en el número máximo de iteraciones.")

def main():
    print("Método de Gauss-Seidel")

    cantidad_ecuaciones = int(input("Ingrese el tamaño del sistema (ej: 2, 3, 4, 5, 10, etc.): "))

    if cantidad_ecuaciones < 2:
        print("El sistema debe tener al menos tamaño 2x2.")
        return

    # Ingreso de la matriz A
    print("Ingrese la matriz de coeficientes A:")
    matriz_A = np.zeros((cantidad_ecuaciones, cantidad_ecuaciones))

    for i in range(cantidad_ecuaciones):
        while True:
            fila = input(f"Fila {i+1} (separada por espacios): ").split()
            if len(fila) == cantidad_ecuaciones:
                try:
                    matriz_A[i] = [float(valor) for valor in fila]
                    break
                except ValueError:
                    print("Por favor ingrese solo números.")
            else:
                print(f"Debe ingresar exactamente {cantidad_ecuaciones} valores.")

    # Ingreso del vector b
    print("Ingrese el vector de términos independientes b:")
    vector_b = np.zeros(cantidad_ecuaciones)

    for i in range(cantidad_ecuaciones):
        while True:
            try:
                vector_b[i] = float(input(f"b[{i+1}]: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

    # Verificamos si la matriz es diagonalmente dominante
    if not es_matriz_diagonalmente_dominante(matriz_A):
        print("Advertencia: La matriz no es diagonalmente dominante. El método podría no converger.")

    # Configuraciones adicionales
    solucion_inicial = [0.0] * cantidad_ecuaciones
    tolerancia_usuario = float(input("Ingrese la tolerancia (por ejemplo, 1e-6): "))
    iteraciones_limite = int(input("Ingrese el número máximo de iteraciones: "))

    try:
        solucion_final, cantidad_iteraciones, errores_finales = metodo_gauss_seidel(
            matriz_A, vector_b, solucion_inicial, tolerancia_usuario, iteraciones_limite
        )
        print("\nSolución aproximada encontrada en", cantidad_iteraciones, "iteraciones:")
        for i in range(cantidad_ecuaciones):
            print(f"x{i+1} = {solucion_final[i]:.6f} (error: {errores_finales[i]:.6f}%)")
    except Exception as mensaje_error:
        print("Error:", mensaje_error)

if __name__ == "__main__":
    main()