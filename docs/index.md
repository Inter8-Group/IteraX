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
El método de la bisección es una técnica numérica iterativa utilizada para hallar raíces reales de funciones continuas. Se basa en el teorema de Bolzano, que garantiza que si una función continua cambia de signo en un intervalo [a,b], entonces existe al menos una raíz en dicho intervalo.
A diferencia de métodos como Newton-Raphson, que requieren derivadas, el método de la bisección solo necesita que f(a) y f(b) tengan signos opuestos.

####Implementación en IteraX
El método de la bisección ha sido implementado en IteraX de la siguiente manera:

```python
def bisection(f, a, b, tol=1e-5, max_iter=100):
    pasos = []

    # Verificación de signo en los extremos
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    for i in range(max_iter):
        c = (a + b) / 2       # Punto medio
        fc = f(c)             # Evaluación de la función en c
        
        # Registro del paso actual
        pasos.append({
            "iteracion": i+1, 
            "a": a, 
            "b": b, 
            "c": c, 
            "f(c)": fc
        })

        # Criterios de parada
        if abs(fc) < tol or abs(b - a) < tol:
            return c, pasos

        # Ajuste del intervalo
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c, pasos  # Retorna última aproximación si no se cumple tolerancia
```
####Explicacion del algoritmo
1. **Puntos iniciales**
El algoritmo comienza con dos valores iniciales a y b, que deben ser elegidos por el usuario de modo que la función tenga signos opuestos en los extremos del intervalo:

f(a)*f(b)<0
Esto garantiza (según el teorema de Bolzano) que existe al menos una raíz entre a y b.

2. **Cálculo del punto medio**
En cada iteración, se calcula el punto medio del intervalo actual:

c=(a + b )/2
 
Luego se evalúa la función en ese punto f(c). Dependiendo del signo de f(c), se actualiza el intervalo:

Si f(a)*f(c)<0, la raíz está entre a y c, por lo que b = c.

Si no, la raíz está entre c y b, por lo que a = c.

3. **Condición de parada**
El algoritmo se detiene si se cumple alguna de estas condiciones:

∣f(c)∣<tol
∣b−a∣<tol

Ambas aseguran que se ha llegado lo suficientemente cerca de una raíz.

4. **Resultados**
En cada iteración, se almacena un registro con los valores actuales de a, b, c y f(c) en una lista llamada pasos.
Esto permite visualizar cómo el algoritmo reduce el intervalo.
Finalmente, el método retorna:

La raíz aproximada c

La lista de pasos realizados

5. **Manejo de errores**
Si los valores iniciales no cumplen que f(a)⋅f(b)<0, se lanza un error para evitar una ejecución inválida:

    raise ValueError("f(a) y f(b) deben tener signos opuestos")

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

### 3.5 Gauss-Seidel

El **método de Gauss-Seidel** es una técnica numérica iterativa utilizada para resolver sistemas de ecuaciones lineales del tipo:

\[
Ax = b
\]

A diferencia del método de Gauss-Jacobi, este algoritmo utiliza los **valores recién actualizados** dentro de la misma iteración para acelerar la convergencia. Es particularmente eficiente cuando se trabaja con matrices diagonales dominantes o matrices simétricas definidas positivas.

---

#### Implementación en IteraX

El método de Gauss-Seidel ha sido implementado en IteraX de la siguiente manera:

```python
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
```

---

#### Explicación del algoritmo

1. **Valores iniciales**  
   Se inicia con un vector de solución estimada \( x \), comúnmente con todos sus elementos en cero, aunque puede ser definido por el usuario. Este vector se irá actualizando en cada iteración.

2. **Fórmula de actualización**  
   Para cada variable \( x_i \), se calcula su nuevo valor usando la fórmula:

   ![image](https://github.com/user-attachments/assets/db9b1dcd-0171-400a-b2b8-18cc3fd390e1)


   Donde \( x_j^{(*)} \) representa:
   - El nuevo valor \( x_j^{(k+1)} \), si ya fue calculado en la iteración actual.
   - El valor anterior \( x_j^{(k)} \), si aún no se actualizó.

3. **Condición de parada**  
   El método se detiene si el **error máximo absoluto** entre dos iteraciones consecutivas es menor que una tolerancia establecida:

   \[
   \max_i \left|x_i^{(k+1)} - x_i^{(k)}\right| < \text{tol}
   \]

   También finaliza si se alcanza el número máximo de iteraciones (`max_iter`).

4. **Resultados**  
   En cada iteración se almacena:
   - El número de la iteración actual
   - El vector solución calculado en esa iteración
   - El error absoluto máximo respecto a la iteración anterior

   Estos datos se guardan en una lista llamada `pasos`, útil para analizar la convergencia del sistema.  
   Finalmente, se retorna:
   - El vector solución \( x \) aproximado
   - La lista de pasos realizados durante las iteraciones

5. **Manejo de errores**  
   El método no garantiza convergencia si la matriz \( A \) no cumple ciertas propiedades. Para aumentar las chances de convergencia, se recomienda que \( A \) sea **diagonalmente dominante** o **simétrica definida positiva**. En caso de no converger dentro de `max_iter`, se retorna la última aproximación disponible junto con el historial completo.




### 3.6 Gauss-Jacobi
El **método de Gauss-Jacobi** es una técnica iterativa utilizada para resolver sistemas de ecuaciones lineales de la forma:

![image](https://github.com/user-attachments/assets/9eaf552b-0dd6-45b7-886e-bd45cfbdd3cf)

Es especialmente útil cuando el sistema es grande y disperso. A diferencia del método de Gauss-Seidel, el método de Gauss-Jacobi **utiliza únicamente los valores de la iteración anterior** para calcular los nuevos valores, lo cual facilita su implementación en paralelo.

---

#### Implementación en IteraX

El método de Gauss-Jacobi ha sido implementado en IteraX de la siguiente manera:

```python
def gauss_jacobi(A, b, tol=1e-5, max_iter=100):
    n = len(A)
    x = [0.0 for _ in range(n)]
    pasos = []

    for iteracion in range(1, max_iter + 1):
        x_nuevo = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
        
        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))
        pasos.append({"iteracion": iteracion, "valores": x_nuevo.copy(), "error": error})

        if error < tol:
            return x_nuevo, pasos
        x = x_nuevo

    return x, pasos
```

---

#### Explicación del Algoritmo

##### Valores Iniciales

El vector inicial se define generalmente como:

```python
x = [0.0, 0.0, ..., 0.0]
```

o como otro valor elegido por el usuario. Este vector sirve como punto de partida para las iteraciones.

---

##### Fórmula de Actualización

En cada iteración, para cada elemento x_i, el nuevo valor se calcula como:

![image1](https://github.com/user-attachments/assets/edc8f74e-ed7c-4fca-82b4-ee2475705d84)

**Importante:** Todos los valores x_j utilizados en esta ecuación provienen **de la iteración anterior**, a diferencia del método de Gauss-Seidel que usa los valores actualizados en cuanto están disponibles.

---

##### Condición de Parada

La iteración se detiene cuando el error máximo entre los valores de iteraciones consecutivas es menor que la tolerancia especificada (`tol`), o cuando se alcanza el número máximo de iteraciones (`max_iter`):

![image](https://github.com/user-attachments/assets/d2a42b7e-1a5d-4ab4-830d-2fe1afbdffba)


---

#### Resultados

Durante cada iteración, el algoritmo almacena en una lista llamada `pasos`:

- Número de la iteración
- Vector de solución calculado
- Error relativo/absoluto máximo de la iteración

Esto permite rastrear el progreso y visualizar cómo se aproxima la solución a lo largo de las iteraciones.

---

#### Requisitos de Convergencia

Para asegurar que el método de Gauss-Jacobi converge, la matriz \( A \) debe ser preferentemente **diagonalmente dominante**, es decir:

![image](https://github.com/user-attachments/assets/9f2aa7c6-fbc7-4eeb-b53c-dffacde4d28d)

Si esta condición no se cumple, el método podría no converger o hacerlo muy lentamente.

---

#### Manejo de Errores

Si se alcanza el número máximo de iteraciones sin cumplir con la condición de parada, la función retorna el vector con los valores de la última iteración y todos los pasos realizados. Esto es útil para análisis posteriores, incluso si la convergencia total no fue alcanzada.

---

## 4. Interfaz de Usuario (Frontend)

4.1 Tecnologías utilizadas
La interfaz de usuario de IteraX fue desarrollada utilizando tecnologías modernas del ecosistema web:

- **React.js**: Biblioteca principal utilizada para construir la SPA (Single Page Application). Permite una experiencia dinámica, rápida y fluida.

- **Chart.js (a través de react-chartjs-2)**: Utilizado para representar gráficamente los resultados de los métodos numéricos. Permite visualizaciones interactivas con tooltips, escalas y puntos de iteración.

- **CSS puro**: Los estilos fueron personalizados con App.css, utilizando flexbox para el diseño responsivo, y estilos definidos para formularios, tablas, botones y el panel lateral.

- **Fetch API**: Para la comunicación HTTP entre el frontend y el backend.

4.2 Componentes principales
La aplicación se organiza dentro de un único componente principal (App.jsx), que contiene todas las funcionalidades:

a) Sidebar de métodos:

- Muestra botones para seleccionar el método numérico a aplicar: Bisección, Regula Falsi, Newton-Raphson, Secante, Gauss-Seidel y Jacobi.
- Cada botón cambia el estado actual y actualiza dinámicamente la vista principal.
  
b) Formulario dinámico:

- Se renderizan campos específicos según el método seleccionado:
    - Métodos de raíces: función, extremos a, b, valores x₀, x₁, tolerancia e iteraciones.
    - Métodos de sistemas: matriz A y vector b.
- Se valida cada campo y se muestra un botón para calcular.

c) Resultados visuales:

- Se muestra un gráfico f(x) con puntos rojos sobre las iteraciones (cuando aplica).
- Se genera una tabla de iteraciones con los datos clave de cada método (por ejemplo, x, f(x), error).
- 
d) Comportamiento responsivo:

- El diseño se adapta a distintas resoluciones de pantalla.
- El contenido principal está dividido en secciones de ingreso, gráfico y resultados.
  
4.3 Validación de datos

El sistema incorpora validación básica en el frontend antes de enviar los datos al backend:

- Los campos numéricos (a, b, x0, x1, tolerancia, etc.) son validaciones por tipo usando .
- Se controlan valores que no pueden ser vacíos o cero si el método lo requiere (por ejemplo, tolerancia).
- Los errores de cálculo (como divisiones por cero o falta de convergencia) son capturados y mostrados al usuario como alertas.
- Si ocurre un error inesperado, se muestra una notificación con el mensaje proveniente del backend.

## 5. Backend

### 5.1 Tecnologías utilizadas

<!-- Lenguaje, framework, librerías matemáticas -->

### 5.2 Estructura del código

<!-- Organización de carpetas, controladores, servicios, etc. -->

### 5.3 Lógica de cálculo de métodos

<!-- Cómo cada método es llamado y procesado en el backend -->

## 6. Integración Frontend ↔ Backend (API REST)

#### 6.1 ```POST /secant```

El método de la secante está disponible a través de una ruta **POST** en la API de IteraX. La ruta es:



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

La función `secant(...)`, implementada en el backend de **IteraX**, devuelve dos elementos principales:

1. **La raíz aproximada** encontrada, que es la solución estimada de la ecuación \( f(x) = 0 \) dentro del margen de tolerancia definido.
2. **Una lista de pasos** (`pasos`) que describe detalladamente cada iteración realizada durante el proceso.

Cada paso incluye:

- `iteracion`: número de la iteración actual.
- `x0` y `x1`: los valores utilizados en esa iteración.
- `f(x0)`: la evaluación de la función en el punto \( x_0 \).
- `error`: el error absoluto entre \( x_2 \) y \( x_1 \), utilizado como criterio de parada.

#### Ejemplo de respuesta esperada (formato JSON):

```json
{
  "raiz": 1.521,
  "pasos": [
    {
      "iteracion": 1,
      "x0": 1.0,
      "x1": 2.0,
      "f(x0)": -1.0,
      "error": 0.25
    },
    ...
  ]
}
```

Al hacer una solicitud a esta ruta, el servidor ejecutará el método de la secante y devolverá la raíz aproximada junto con los pasos de la iteración.

## 7. Consideraciones finales

<!-- Limitaciones actuales, posibles mejoras, decisiones de diseño técnico -->
