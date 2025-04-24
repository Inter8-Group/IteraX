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

El **método de Newton-Raphson** es una técnica numérica iterativa utilizada para encontrar raíces de funciones reales de la forma:

\[
f(x) = 0
\]

Es uno de los métodos más utilizados por su velocidad de convergencia, siempre que la función sea diferenciable y la derivada no se anule cerca del punto inicial.

---

#### Implementación en IteraX

El método de Newton-Raphson ha sido implementado en IteraX de la siguiente manera:

```python
def newton_raphson(f, df, x0, tol, max_iter):
    pasos = []
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("La derivada es cero en x = {:.4f}".format(x0))
        x1 = x0 - fx / dfx
        error = abs(x1 - x0)
        pasos.append({"iteracion": i, "x": x0, "f(x)": fx, "error": error})
        if error < tol:
            return x1, pasos
        x0 = x1
    return x1, pasos
```

---

#### Explicación del algoritmo

1. **Valor inicial**
   Se comienza con un valor inicial \( x0 \), elegido por el usuario. Es importante que esté cerca de la raíz buscada.

2. **Fórmula de actualización**
   En cada iteración, se calcula un nuevo valor \( x1 \) a partir de:

   ![image](https://github.com/user-attachments/assets/a2b56962-8bd8-4087-a79b-1e5136b4ac2f)

   Este valor se obtiene restando al punto actual el cociente entre la función evaluada y su derivada en ese punto.

3. **Condición de parada**
   El algoritmo se detiene si:

   - El **error absoluto** ![image](https://github.com/user-attachments/assets/655f0400-5d40-466e-bd71-a03b71701489)
   - O si se alcanza el número máximo de iteraciones `max_iter`

4. **Resultados**
   En cada paso se guarda:
   - La iteración actual
   - El valor de \( xn \)
   - La evaluación de la función \( f(xn) \)
   - El error absoluto con respecto a la iteración anterior

   Estos valores se almacenan en una lista llamada `pasos`. Al finalizar, el método retorna:
   - La raíz aproximada \( x \)
   - La lista de pasos realizados

5. **Manejo de errores**
   Si la derivada \( f'(x) \) se anula en algún punto del proceso, se lanza un error para evitar una división por cero. Esto indica que el método no puede continuar desde ese punto.

---

#### Recomendaciones

- Elegir un valor inicial \( x0 \) cercano a la raíz.
- Verificar que \( f'(x0) \) distinto a 0 para evitar errores.
- Ideal para funciones suaves y con derivadas conocidas.

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


   Donde ![image](https://github.com/user-attachments/assets/dd7a4da0-377b-4d42-a6fc-905eb2ef920b) representa:
   - El nuevo valor ![image](https://github.com/user-attachments/assets/63a22e8c-2036-4935-880f-12b672511b9a), si ya fue calculado en la iteración actual.
   - El valor anterior ![image](https://github.com/user-attachments/assets/ac4ffca1-90e1-4611-8015-8044ed97d512), si aún no se actualizó.

3. **Condición de parada**  
   El método se detiene si el **error máximo absoluto** entre dos iteraciones consecutivas es menor que una tolerancia establecida:

   ![image](https://github.com/user-attachments/assets/65f121e1-cf7e-4f4c-8243-2ba4a3dc86db)

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

### 4.1 Tecnologías utilizadas
La interfaz de usuario de IteraX fue desarrollada utilizando tecnologías modernas del ecosistema web:

- **React.js**: Biblioteca principal utilizada para construir la SPA (Single Page Application). Permite una experiencia dinámica, rápida y fluida.

- **Chart.js (a través de react-chartjs-2)**: Utilizado para representar gráficamente los resultados de los métodos numéricos. Permite visualizaciones interactivas con tooltips, escalas y puntos de iteración.

- **CSS puro**: Los estilos fueron personalizados con App.css, utilizando flexbox para el diseño responsivo, y estilos definidos para formularios, tablas, botones y el panel lateral.

- **Fetch API**: Para la comunicación HTTP entre el frontend y el backend.

### 4.2 Componentes principales
La aplicación se organiza dentro de un único componente principal (App.jsx), que contiene todas las funcionalidades:

a) **Sidebar de métodos**:

- Muestra botones para seleccionar el método numérico a aplicar: Bisección, Regula Falsi, Newton-Raphson, Secante, Gauss-Seidel y Jacobi.
- Cada botón cambia el estado actual y actualiza dinámicamente la vista principal.
  
b) **Formulario dinámico**:

- Se renderizan campos específicos según el método seleccionado:
    - Métodos de raíces: función, extremos a, b, valores x₀, x₁, tolerancia e iteraciones.
    - Métodos de sistemas: matriz A y vector b.
- Se valida cada campo y se muestra un botón para calcular.

c) **Resultados visuales**:

- Se muestra un gráfico f(x) con puntos rojos sobre las iteraciones (cuando aplica).
- Se genera una tabla de iteraciones con los datos clave de cada método (por ejemplo, x, f(x), error).

d) **Comportamiento responsivo**:

- El diseño se adapta a distintas resoluciones de pantalla.
- El contenido principal está dividido en secciones de ingreso, gráfico y resultados.
  
### 4.3 Validación de datos
El sistema incorpora validación básica en el frontend antes de enviar los datos al backend:

- Los campos numéricos (a, b, x0, x1, tolerancia, etc.) son validaciones por tipo usando .
- Se controlan valores que no pueden ser vacíos o cero si el método lo requiere (por ejemplo, tolerancia).
- Los errores de cálculo (como divisiones por cero o falta de convergencia) son capturados y mostrados al usuario como alertas.
- Si ocurre un error inesperado, se muestra una notificación con el mensaje proveniente del backend.

## 5. Backend

### 5.1 Tecnologías utilizadas

**Lenguaje:** Python 3.10+

**Framework principal:** FastAPI – lo utilizamos para definir endpoints de la API REST que calculan métodos numéricos.

**Librerías complementarias:**

- pydantic – para validar la estructura de entrada de datos con modelos.

- sympy – para derivación simbólica automática.

- math – para funciones matemáticas estándar.

- typing.List – para definir entradas tipo listas.

- fastapi.middleware.cors.CORSMiddleware – para permitir la comunicación con el frontend en React desde otro dominio.

### 5.2 Estructura del código

**Archivos principales:**
main.py - Punto de entrada del backend. Define todos los endpoints de la API para cada método numérico. Implementa modelos de entrada con pydantic y configura CORS.
  
Carpeta methods/ - Contiene los módulos Python con las implementaciones específicas de cada método numérico:
- bisection.py
- newton.py
- secant.py
- regula_falsi.py
- gauss_seidel.py
- gauss_jacobi.py

### 5.3 Lógica de cálculo de métodos

Cada método numérico es expuesto como un endpoint tipo POST. El backend recibe los datos desde el frontend, realiza el cálculo correspondiente y retorna un JSON con los resultados. A continuación, se resumen los endpoints:

/biseccion
- Entrada: función f(x), intervalo [a, b], tolerancia y cantidad máxima de iteraciones.

- Proceso: Evalúa f en cada iteración hasta cumplir la tolerancia.

- Salida: raíz aproximada y pasos intermedios.

/newton
- Entrada: función f(x), valor inicial x0, tolerancia, iteraciones máximas.

- Proceso: Usa sympy para derivar simbólicamente la función, luego aplica Newton-Raphson.

- Salida: raíz aproximada y lista de iteraciones con errores.

/secant
- Entrada: función f(x), dos valores iniciales x0 y x1, tolerancia, iteraciones.

- Proceso: Aplica el método de la secante para encontrar la raíz.

- Salida: raíz y detalle paso a paso.

/regula-falsi
- Entrada: función f(x), extremos a, b, tolerancia, iteraciones máximas.

- Proceso: Implementa el método de la falsa posición para converger a la raíz.

- Salida: raíz y pasos intermedios.

/gauss-seidel y /jacobi
- Entrada: matriz A, vector b, tolerancia, iteraciones máximas.

- Proceso: Iteran hasta encontrar la solución del sistema lineal 
𝐴
𝑥
=
𝑏
Ax=b.

- Salida: solución aproximada y vector de errores en cada iteración.

Aqui está a seção **"Consideraciones finales"** revisada e com os pontos que você pediu:

---

## 6. Consideraciones finales

**IteraX** ha sido una solución efectiva y funcional para la resolución de problemas numéricos, implementando seis métodos matemáticos fundamentales. Sin embargo, como cualquier software, siempre existe espacio para mejoras y optimizaciones en diversas áreas. A continuación, se detallan algunas consideraciones importantes sobre el proyecto:

### Mejoras Potenciales

1. **Modularidad**:
   - Actualmente, el sistema está estructurado de manera que cada método numérico está encapsulado en su propia función dentro del backend. Sin embargo, se podría mejorar aún más la modularidad separando los componentes del backend en microservicios.
   - Además, se podría implementar un sistema de **plugin** que permita agregar fácilmente nuevos métodos numéricos sin tener que modificar el núcleo de la aplicación.

2. **Arquitectura más limpia y escalable**:
   - Aunque la estructura actual es efectiva, se podría mejorar la modularidad del código al adoptar patrones como **MVC** (Modelo-Vista-Controlador), lo que aseguraría una separación clara de responsabilidades y facilitaría la extensión del software a futuro.
   - Se recomienda también refactorizar el backend para adoptar una arquitectura más robusta, como microservicios para que cada algoritmo numérico funcione de manera independiente, lo que haría más fácil el mantenimiento y la escalabilidad.

3. **Despliegue y Escalabilidad**:
   - Además, se podría utilizar un servicio **cloud hosting** como AWS, Azure o GCP para asegurar que la aplicación sea accesible para usuarios y sin problemas de rendimiento.

4. **Interfaz de Usuario**:
   - La interfaz de usuario podría mejorar en cuanto a diseño y experiencia de usuario. Aunque funciona bien, sería interesante agregar **visualizaciones interactivas** para mostrar cómo convergen los métodos en tiempo real, lo cual podría ser muy útil en un contexto educativo. Esto podría incluir animaciones o gráficos más dinámicos.

5. **Documentación y Soporte**:
   - Se podría ampliar la documentación técnica, añadiendo más ejemplos prácticos y tutoriales paso a paso para ayudar a los usuarios a entender mejor cómo usar la aplicación.
   - Agregar **soporte multi-idioma** también sería una excelente mejora, permitiendo que el proyecto sea utilizado por usuarios de diferentes países.

### Conclusión

**IteraX** fue desarrollado como parte de un proyecto académico en **UCASAL**, y cumple con su objetivo principal: ofrecer una herramienta simple y eficiente para resolver problemas numéricos. Las consideraciones mencionadas representan áreas donde el software podría crecer, adaptarse y mejorar para satisfacer necesidades más complejas o integrarse mejor en entornos profesionales. No obstante, el sistema actual ya proporciona una base sólida y eficaz para resolver ecuaciones y sistemas de ecuaciones de manera rápida.