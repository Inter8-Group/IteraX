
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from methods.bisection import bisection
from methods.gauss_seidel import gauss_seidel
from methods.newton import newton_raphson
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sympy import symbols, diff, sympify
from methods.secant import secant
from methods.regula_falsi import regula_falsi
import math

app = FastAPI()

# Permitir frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés limitarlo a http://localhost:3000 si querés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para método de bisección
class BiseccionInput(BaseModel):
    funcion: str
    a: float
    b: float
    tol: float
    max_iter: int

# Modelo para método de Newton-Raphson
class NewtonInput(BaseModel):
    funcion: str
    x0: float
    tol: float
    max_iter: int

# Modelo para resolver sistemas
class SistemaInput(BaseModel):
    A: List[List[float]]
    b: List[float]
    tol: float
    max_iter: int

# Modelo para el método secante
class SecantInput(BaseModel):
    funcion: str
    x0: float
    x1: float
    tol: float
    max_iter: int

# Modelo para método de Regula Falsi
class RegulaFalsiInput(BaseModel):
    funcion: str
    a: float
    b: float
    tol: float
    max_iter: int


@app.post("/biseccion")
def calcular_biseccion(data: BiseccionInput):
    try:
        f = lambda x: eval(data.funcion, {"x": x, "math": math})
        raiz, pasos = bisection(f, data.a, data.b, data.tol, data.max_iter)
        return {"raiz": raiz, "pasos": pasos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/gauss-seidel")
def resolver_sistema(data: SistemaInput):
    try:
        solucion, iteraciones = gauss_seidel(data.A, data.b, data.tol, data.max_iter)
        return {"solucion": solucion, "pasos": iteraciones}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/newton")
def calcular_newton(data: NewtonInput):
    try:
        # Derivar automáticamente la función
        x = symbols('x')
        f_expr = sympify(data.funcion)
        df_expr = diff(f_expr, x)
        f_str = str(f_expr)
        df_str = str(df_expr)

        # Crear funciones evaluables
        f = lambda x_val: eval(f_str, {"x": x_val, "math": math})
        df = lambda x_val: eval(df_str, {"x": x_val, "math": math})

        # Calcular raíz e iteraciones
        raiz, pasos = newton_raphson(f, df, data.x0, data.tol, data.max_iter)
        return {"raiz": raiz, "pasos": pasos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/secant")
def secant_controller(data: SecantInput):
    try:
        f = lambda x: eval(data.funcion, {"x": x, "math": math})
        raiz, pasos = secant(f, data.x0, data.x1, data.tol, data.max_iter)
        return {"raiz": raiz, "pasos": pasos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/regula-falsi")
def calcular_regula_falsi(data: RegulaFalsiInput):
    try:
        raiz, pasos = regula_falsi(data.funcion, data.a, data.b, data.max_iter, data.tol)
        return {"raiz": raiz, "pasos": pasos}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
