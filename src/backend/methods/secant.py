def secant(f, x0, x1, tol, max_iter):
    """
    Secant Method to find the root of a function.
    :param f: Function to be analyzed
    :param x0: Initial value 1
    :param x1: Initial value 2
    :param tol: Tolerance for precision
    :param max_iter: Maximum number of iterations
    :return: The root found and the steps taken
    """
    pasos = []
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Secant formula
        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero in secant method at iteration {}".format(i))
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x2 - x1)
        
        pasos.append({
            "iteracion": i, 
            "x0": x0, 
            "x1": x1, 
            "f(x0)": f_x0, 
            "error": error
        })
        
        if error < tol:
            return x2, pasos
        
        # Update values for the next iteration
        x0, x1 = x1, x2

    raise ValueError("Maximum number of iterations reached without convergence.")
