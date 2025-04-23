# Documentación Técnica del Proyecto

## 1. Introducción

**IteraX** es una aplicación diseñada para la resolución de problemas numéricos mediante la implementación de seis métodos matemáticos fundamentales. Esta herramienta fue desarrollada como parte de un proyecto para una evaluación de la **UCASAL**, con el objetivo de proporcionar una solución eficiente y accesible para estudiantes y profesionales que necesitan resolver ecuaciones y sistemas de ecuaciones de manera rápida y precisa.

El proyecto consta de dos partes principales: el **frontend** y el **backend**. El **frontend** está diseñado para interactuar con el usuario de manera intuitiva, permitiendo ingresar las funciones y parámetros requeridos para ejecutar los métodos numéricos. El **backend**, por su parte, está compuesto por varios algoritmos que procesan las entradas y devuelven los resultados solicitados. Entre los métodos implementados se incluyen **Bisección**, **Regula Falsi**, **Newton-Raphson**, **Secante**, **Gauss-Seidel** y **Jacobi**.

Esta aplicación tiene como objetivo no solo resolver ecuaciones, sino también proporcionar una interfaz visual para ayudar a comprender y verificar los pasos intermedios de cada algoritmo, brindando una experiencia de aprendizaje más completa.

## 2. Arquitectura General del Sistema

**IteraX** se basa en una arquitectura de software moderna y modular, dividida en dos capas principales: **Frontend** y **Backend**. A continuación, se presenta la descripción detallada de la arquitectura de cada componente, así como la estructura de las carpetas del proyecto.

### 2.1 Estructura General

```
src/
│
├── frontend/               # Proyecto Frontend (React.js)
│   ├── public/             # Archivos estáticos (index.html, favicon.ico)
│   ├── src/                # Código fuente de React
│   │   ├── App.jsx         # Componente principal de la app
│   │   ├── App.css         # Estilos
│   │   └── index.js        # Punto de entrada de la aplicación
│   └── package.json        # Dependencias y scripts de Frontend
│
└── backend/                # Proyecto Backend (Python con FastAPI)
    ├── methods/            # Algoritmos de métodos numéricos (Bisección, Newton, etc.)
    │   ├── bisection.py    # Implementación del método de Bisección
    │   ├── regula_falsi.py # Implementación de Regula Falsi
    │   ├── newton.py       # Implementación de Newton-Raphson
    │   ├── secant.py       # Implementación de la Secante
    │   ├── gauss_seidel.py # Implementación de Gauss-Seidel
    │   └── jacobi.py       # Implementación de Jacobi
    ├── main.py             # Punto de entrada de FastAPI y definición de controllers
    ├── requirements.txt    # Dependencias de Backend (FastAPI, Uvicorn, etc.)
```

### 2.2 Descripción de Componentes

#### **Frontend (Cliente Web)**

El frontend está basado en **React.js**, un framework ligero y eficiente para desarrollar interfaces de usuario interactivas. Su arquitectura se organiza en varios componentes reutilizables, como formularios, botones y vistas para cada uno de los métodos numéricos. Además, se integra con el backend mediante peticiones HTTP a los endpoints de la API.

- **Servicios:** Gestiona las peticiones al backend con Fetch para obtener resultados de los métodos numéricos.
- **Vistas:** Todo ocurre en una página, que se renderiza automáticamente mostrando los campos de entrada y los resultados de las iteraciones según el método seleccionado.

#### **Backend (API REST con FastAPI)**

El backend está desarrollado con **FastAPI**, un framework web de alto rendimiento para Python. El backend expone seis rutas principales, una por cada método numérico. Cada ruta procesa las entradas y llama a una función que ejecuta el cálculo y devuelve los resultados de la iteración.

- **Métodos Numéricos:** Cada algoritmo (Bisección, Regula Falsi, Newton-Raphson, Secante, Gauss-Seidel, Jacobi) está implementado en su propio archivo dentro de la carpeta `methods/`.
- **Controladores:** Los controladores gestionan las peticiones entrantes y las validaciones de datos. Cada uno está separado por el método numérico que gestiona.

#### **Comunicación Frontend ↔ Backend**

El frontend se comunica con el backend a través de una API REST. El flujo de trabajo es el siguiente:

1. El usuario ingresa una función matemática y parámetros en el frontend.
2. El frontend valida estos datos y hace una petición `POST` al endpoint correspondiente del backend.
3. El backend recibe los datos, ejecuta el algoritmo numérico y devuelve los resultados.
4. El frontend muestra los resultados al usuario en forma de gráficos y/o tablas, mostrando los pasos de las iteraciones y la raíz aproximada obtenida en cada uno de los métodos.

Con esta arquitectura modular y clara, **IteraX** garantiza una separación eficiente de responsabilidades, permitiendo un fácil mantenimiento y futuras ampliaciones tanto en el frontend como en el backend.

## 3. Métodos Numéricos Implementados

### 3.1 Bisección

### 3.2 Regula Falsi

### 3.3 Newton-Raphson

### 3.4 Secante

El **método de la Secante** es una técnica iterativa que permite aproximar las raíces de una función \(f(x) = 0\). A diferencia del método de Newton-Raphson, que requiere el cálculo de la derivada de la función, el método de la secante utiliza dos puntos iniciales para aproximar la pendiente de la función en cada iteración.

#### Implementación en IteraX

El método de la secante ha sido implementado en IteraX de la siguiente manera:

```python
def secant(f, x0, x1, tol, max_iter):
    pasos = []
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            raise ValueError("División por cero en el método de la secante en la iteración {}".format(i))
        
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
        
        x0, x1 = x1, x2

    raise ValueError("Se alcanzó el número máximo de iteraciones sin converger.")
```

#### Explicación del algoritmo

1. **Puntos iniciales**  
   El algoritmo comienza con dos valores iniciales \(x_0\) y \(x_1\), que son elegidos por el usuario y deben estar cerca de la raíz de la función.

2. **Fórmula de la Secante**  
   En cada iteración, el siguiente valor \(x_2\) se calcula utilizando la fórmula de la secante:

   \[
   x_2 = x_1 - \frac{f(x_1) \cdot (x_1 - x_0)}{f(x_1) - f(x_0)}
   \]

   Donde \(f(x_1)\) y \(f(x_0)\) son las evaluaciones de la función en los puntos \(x_1\) y \(x_0\), respectivamente.

3. **Condición de parada**  
   El algoritmo continúa iterando hasta que el **error absoluto** entre dos iteraciones sucesivas sea menor que la tolerancia especificada \(tol\), o hasta que se alcance el número máximo de iteraciones \(max_iter\).

4. **Resultados**  
   Durante cada iteración, se almacenan los valores de \(x_0\), \(x_1\), \(f(x_0)\), y el error relativo en una lista `pasos`. Este registro permite visualizar cómo el método avanza y se aproxima a la raíz. Finalmente, el algoritmo devuelve la raíz encontrada junto con todos los pasos realizados.

5. **Manejo de errores**  
   En caso de que la diferencia entre las evaluaciones de la función \(f(x_1) - f(x_0)\) sea cero, se lanza un error indicando que hubo una división por cero, lo que puede ocurrir si los dos puntos iniciales son iguales o si la función tiene un comportamiento inesperado.

#### Ruta POST para el Método de la Secante

El método de la secante está disponible a través de una ruta **POST** en la API de IteraX. La ruta es:

```
POST /secant
```

El cuerpo de la solicitud debe contener los siguientes parámetros:

```json
{
  "funcion": "x**2 - 2",  // La función matemática a analizar
  "x0": 1.0,              // Primer valor inicial
  "x1": 2.0,              // Segundo valor inicial
  "tol": 0.001,            // Tolerancia para la precisión
  "max_iter": 100         // Número máximo de iteraciones
}
```

- **funcion**: La función matemática a analizar, expresada como una cadena (por ejemplo, "x**2 - 2").
- **x0**: El primer valor inicial para la iteración.
- **x1**: El segundo valor inicial para la iteración.
- **tol**: La tolerancia que define el error máximo aceptable.
- **max_iter**: El número máximo de iteraciones permitidas antes de detenerse.

Al hacer una solicitud a esta ruta, el servidor ejecutará el método de la secante y devolverá la raíz aproximada junto con los pasos de la iteración.

### 3.6 Jacobi

## 4. Interfaz de Usuario (Frontend)

### 4.1 Tecnologías utilizadas

<!-- Frameworks, librerías y estilos visuales aplicados -->

### 4.2 Componentes principales

<!-- Qué vistas existen, qué acciones puede hacer el usuario -->

### 4.3 Validación de datos

<!-- Cómo se validan las entradas del usuario -->

## 5. Backend

### 5.1 Tecnologías utilizadas

<!-- Lenguaje, framework, librerías matemáticas -->

### 5.2 Estructura del código

<!-- Organización de carpetas, controladores, servicios, etc. -->

### 5.3 Lógica de cálculo de métodos

<!-- Cómo cada método es llamado y procesado en el backend -->

## 6. Integración Frontend ↔ Backend

### 6.1 API REST

<!-- Rutas disponibles, método HTTP, estructura de los cuerpos (body) -->

### 6.2 Flujo de datos

<!-- Cómo viaja la información desde el frontend al backend y viceversa -->

## 7. Consideraciones finales

<!-- Limitaciones actuales, posibles mejoras, decisiones de diseño técnico -->

## 8. Anexos

<!-- Ejemplos de entrada/salida, capturas de pantalla, enlaces útiles -->
