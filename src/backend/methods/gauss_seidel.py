def gauss_seidel(A, b, tol=1e-5, max_iter=100):
    n = len(A)
    x = [0.0 for _ in range(n)]
    pasos = []

    for iteracion in range(1, max_iter + 1):
        x_new = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x_new[j] if j < i else A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i][i]
        
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        pasos.append({"iteracion": iteracion, "valores": x_new.copy(), "error": error})

        if error < tol:
            return x_new, pasos
        x = x_new

    return x, pasos
