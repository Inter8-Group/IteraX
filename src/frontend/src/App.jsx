import React, { useState } from 'react';
import './App.css';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
} from 'chart.js';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend, CategoryScale);

function App() {
  const [metodo, setMetodo] = useState("Bisección");
  const [funcion, setFuncion] = useState("x**3 - 6*x + 2");
  const [a, setA] = useState(1);
  const [b, setB] = useState(4);
  const [tol, setTol] = useState(0.001);
  const [maxIter, setMaxIter] = useState(50);
  const [resultado, setResultado] = useState(null);
  const [x0, setX0] = useState(1.5);
  const [x1, setX1] = useState(1);

  const [matriz, setMatriz] = useState([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 3],
  ]);
  const [vectorB, setVectorB] = useState([15, 10, 10]);

  const actualizarMatriz = (i, j, valor) => {
    const nueva = [...matriz];
    nueva[i][j] = parseFloat(valor);
    setMatriz(nueva);
  };

  const actualizarVectorB = (i, valor) => {
    const nuevo = [...vectorB];
    nuevo[i] = parseFloat(valor);
    setVectorB(nuevo);
  };

  const calcular = async () => {
    try {
      let res;
      if (metodo === "Bisección") {
        res = await fetch("http://localhost:8000/biseccion", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ funcion, a, b, tol, max_iter: maxIter })
        });
      } else if (metodo === "Regula-Falsi") {
        res = await fetch("http://localhost:8000/regula_falsi", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ funcion, a, b, tol, max_iter: maxIter })
        });
      } else if (metodo === "Secante") {
        res = await fetch("http://localhost:8000/secant", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ funcion, x0, x1, tol, max_iter: maxIter })
        });
      } else if (metodo === "Newton-Raphson") {
        res = await fetch("http://localhost:8000/newton", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ funcion, x0, tol, max_iter: maxIter })
        });
      } else if (metodo === "Gauss-Seidel") {
        res = await fetch("http://localhost:8000/gauss_seidel", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ A: matriz, b: vectorB, tol, max_iter: maxIter })
        });
      } else if (metodo === "Jacobi") {
        res = await fetch("http://localhost:8000/jacobi", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ A: matriz, b: vectorB, tol, max_iter: maxIter })
        });
      }
      if (!res.ok) throw new Error("Error en la solicitud");
      const data = await res.json();
      setResultado(data);
    } catch (error) {
      console.error("Error en el cálculo:", error);
    }
  };

  return (
    <div className="container">
      <div className="sidebar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="MATLAB" width="100" />
        <h2>Métodos Numéricos</h2>
        <p><strong>Proyecto Análisis</strong></p>

        <h3>Búsqueda de raíces</h3>
        <button className={metodo === "Bisección" ? "active" : ""} onClick={() => setMetodo("Bisección")}>Bisección</button>
        <button className={metodo === "Newton-Raphson" ? "active" : ""} onClick={() => setMetodo("Newton-Raphson")}>Newton-Raphson</button>
        <button className={metodo === "Regula-Falsi" ? "active" : ""} onClick={() => setMetodo("Regula-Falsi")}>Regula-Falsi</button>
        <button className={metodo === "Secante" ? "active" : ""} onClick={() => setMetodo("Secante")}>Secante</button>

        <h3>Solución de sistemas</h3>
        <button className={metodo === "Gauss-Seidel" ? "active" : ""} onClick={() => setMetodo("Gauss-Seidel")}>Gauss-Seidel</button>
        <button className={metodo === "Jacobi" ? "active" : ""} onClick={() => setMetodo("Jacobi")}>Jacobi</button>
      </div>

      <div className="main">
        <h1>{metodo}</h1>

        <div className="contenido">
          <div className="formulario">
            <p><strong>Ingrese los datos:</strong></p>



            {metodo === "Newton-Raphson" && (
              <>
                <label>Función f(x):</label>
                <input value={funcion} onChange={e => setFuncion(e.target.value)} />
                <label>Valor inicial x₀:</label>
                <input type="number" value={x0} onChange={e => setX0(e.target.value)} />
              </>
            )}

            {metodo === "Bisección" && (
              <>
                <label>Función f(x):</label>
                <input value={funcion} onChange={e => setFuncion(e.target.value)} />

                <label>Extremo izquierdo a:</label>
                <input type="number" value={a} onChange={e => setA(e.target.value)} />

                <label>Extremo derecho b:</label>
                <input type="number" value={b} onChange={e => setB(e.target.value)} />
              </>
            )}
            {metodo === "Secante" && (
              <>
                <label>Función f(x):</label>
                <input value={funcion} onChange={e => setFuncion(e.target.value)} />

                <label>Valor inicial x₀:</label>
                <input type="number" value={x0} onChange={e => setX0(e.target.value)} />

                <label>Valor inicial x₁:</label>
                <input type="number" value={x1} onChange={e => setX1(e.target.value)} />
              </>
            )}
            {metodo === "Regula-Falsi" && (
              <>
                <label>Función f(x):</label>
                <input value={funcion} onChange={e => setFuncion(e.target.value)} />

                <label>Extremo izquierdo a:</label>
                <input type="number" value={a} onChange={e => setA(e.target.value)} />

                <label>Extremo derecho b:</label>
                <input type="number" value={b} onChange={e => setB(e.target.value)} />

                <label>Tolerancia:</label>
                <input type="number" step="any" value={tol} onChange={e => setTolerancia(e.target.value)} />

                <label>Iteraciones máximas:</label>
                <input type="number" value={maxIter} onChange={e => setMaxIter(e.target.value)} />
              </>
            )}
            {metodo === "Gauss-Seidel" && (
              <>
                <label>Matriz A:</label>
                {matriz.map((fila, i) => (
                  <div key={i} style={{ display: "flex", gap: "10px", marginBottom: "5px" }}>
                    {fila.map((valor, j) => (
                      <input
                        key={j}
                        type="number"
                        value={valor}
                        onChange={(e) => actualizarMatriz(i, j, e.target.value)}
                        style={{ width: "60px" }}
                      />
                    ))}
                  </div>
                ))}

                <label>Vector b:</label>
                <div style={{ display: "flex", gap: "10px", marginBottom: "10px" }}>
                  {vectorB.map((valor, i) => (
                    <input
                      key={i}
                      type="number"
                      value={valor}
                      onChange={(e) => actualizarVectorB(i, e.target.value)}
                      style={{ width: "60px" }}
                    />
                  ))}
                </div>
              </>
            )}
            {metodo === "Jacobi" && (
              <>
                <label>Matriz A:</label>
                {matriz.map((fila, i) => (
                  <div key={i} style={{ display: "flex", gap: "10px" }}>
                    {fila.map((valor, j) => (
                      <input
                        key={j}
                        type="number"
                        value={valor}
                        onChange={e => actualizarMatriz(i, j, e.target.value)}
                        style={{ width: "60px" }}
                      />
                    ))}
                  </div>
                ))}

                <label>Vector b:</label>
                {vectorB.map((valor, i) => (
                  <input
                    key={i}
                    type="number"
                    value={valor}
                    onChange={e => actualizarVectorB(i, e.target.value)}
                  />
                ))}

                <label>Tolerancia:</label>
                <input type="number" step="any" value={tol} onChange={e => setTolerancia(e.target.value)} />

                <label>Iteraciones máximas:</label>
                <input type="number" value={maxIter} onChange={e => setMaxIter(e.target.value)} />
              </>
            )}


            <label>Tolerancia:</label>
            <input type="number" value={tol} onChange={e => setTol(e.target.value)} />

            <label>Iteraciones máximas:</label>
            <input type="number" value={maxIter} onChange={e => setMaxIter(e.target.value)} />

            <button className="calcular" onClick={calcular}>Calcular</button>
          </div>

          {resultado?.raiz !== undefined && (metodo === "Bisección" || metodo === "Newton-Raphson") && (
            <div className="grafico">
              <h3>Gráfico de f(x):</h3>
              <Line
                data={{
                  datasets: [
                    {
                      label: 'f(x)',
                      data: Array.from({ length: 100 }, (_, i) => {
                        let left, right;
                        if (metodo === "Bisección") {
                          left = a;
                          right = b;
                        } else if (metodo === "Newton-Raphson") {
                          const xs = resultado.pasos.map(p => p.x);
                          const minX = Math.min(...xs);
                          const maxX = Math.max(...xs);
                          const margin = (maxX - minX) * 0.2 || 1; // si da 0, usar margen 1
                          left = minX - margin;
                          right = maxX + margin;
                        }
                        const xVal = left + (right - left) * (i / 99);
                        try {
                          return { x: xVal, y: eval(funcion.replace(/x/g, `(${xVal})`)) };
                        } catch {
                          return { x: xVal, y: null };
                        }
                      }),
                      borderColor: 'blue',
                      tension: 0.3,
                      fill: false,
                    },
                    {
                      label: 'Puntos de iteración',
                      data: metodo === "Bisección"
                        ? resultado.pasos.map(p => ({ x: p.c, y: p["f(c)"] }))
                        : metodo === "Newton-Raphson"
                          ? resultado.pasos.map(p => ({ x: p.x, y: p["f(x)"] }))
                          : [],
                      pointBackgroundColor: 'red',
                      pointBorderColor: 'red',
                      showLine: false,
                      borderColor: 'red',
                    },
                  ]
                }}
                options={{
                  responsive: true,
                  maintainAspectRatio: false,
                  interaction: {
                    mode: 'nearest',
                    intersect: false
                  },
                  plugins: {
                    tooltip: {
                      enabled: true,
                      mode: 'nearest',
                      intersect: false,
                      callbacks: {
                        label: (ctx) => `x: ${ctx.parsed.x.toFixed(4)}, f(x): ${ctx.parsed.y.toFixed(4)}`
                      }
                    },
                    legend: {
                      display: true
                    }
                  },
                  scales: {
                    x: { type: 'linear', title: { display: true, text: 'x' } },
                    y: { title: { display: true, text: 'f(x)' } }
                  }
                }}
              />
            </div>
          )}
        </div>

        {resultado?.raiz !== undefined && metodo === "Bisección" && (
          <div className="resultado">
            <h2>Raíz aproximada: {Number(resultado.raiz).toFixed(4)}</h2>
            <h3>Iteraciones:</h3>
            <table className="resultado-table">
              <thead>
                <tr>
                  <th>Iteración</th>
                  <th>a</th>
                  <th>b</th>
                  <th>c</th>
                  <th>f(c)</th>
                </tr>
              </thead>
              <tbody>
                {resultado.pasos.map((fila, i) => (
                  <tr key={i}>
                    <td>{fila.iteracion}</td>
                    <td>{Number(fila.a).toFixed(4)}</td>
                    <td>{Number(fila.b).toFixed(4)}</td>
                    <td>{Number(fila.c).toFixed(4)}</td>
                    <td>{Number(fila["f(c)"]).toExponential(3)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {resultado?.raiz !== undefined &&
          metodo === "Newton-Raphson" &&
          resultado.pasos?.[0]?.x !== undefined && (
            <div className="resultado">
              <h2>Raíz aproximada: {Number(resultado.raiz).toFixed(4)}</h2>
              <h3>Iteraciones:</h3>
              <table className="resultado-table">
                <thead>
                  <tr>
                    <th>Iteración</th>
                    <th>x</th>
                    <th>f(x)</th>
                    <th>Error</th>
                  </tr>
                </thead>
                <tbody>
                  {resultado.pasos.map((fila, i) => (
                    <tr key={i}>
                      <td>{fila.iteracion}</td>
                      <td>{fila.x.toFixed(6)}</td>
                      <td>{fila["f(x)"].toExponential(3)}</td>
                      <td>{fila.error.toExponential(3)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

        {resultado?.raiz !== undefined && metodo === "Regula-Falsi" && (
          <div className="resultado">
            <h2>Raíz aproximada: {Number(resultado.raiz).toFixed(4)}</h2>
            <h3>Iteraciones:</h3>
            <table className="resultado-table">
              <thead>
                <tr>
                  <th>Iteración</th>
                  <th>a</th>
                  <th>b</th>
                  <th>c</th>
                  <th>f(c)</th>
                </tr>
              </thead>
              <tbody>
                {resultado.pasos.map((fila, i) => (
                  <tr key={i}>
                    <td>{fila.iteracion}</td>
                    <td>{Number(fila.a).toFixed(4)}</td>
                    <td>{Number(fila.b).toFixed(4)}</td>
                    <td>{Number(fila.c).toFixed(4)}</td>
                    <td>{Number(fila["f(c)"]).toExponential(3)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {resultado?.raiz !== undefined && metodo === "Secante" && (
          <div className="resultado">
            <h2>Raíz aproximada: {Number(resultado.raiz).toFixed(4)}</h2>
            <h3>Iteraciones:</h3>
            <table className="resultado-table">
              <thead>
                <tr>
                  <th>Iteración</th>
                  <th>x0</th>
                  <th>x1</th>
                  <th>f(x0)</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {resultado.pasos.map((fila, i) => (
                  <tr key={i}>
                    <td>{fila.iteracion}</td>
                    <td>{Number(fila.x0).toFixed(4)}</td>
                    <td>{Number(fila.x1).toFixed(4)}</td>
                    <td>{Number(fila["f(x0)"]).toExponential(3)}</td>
                    <td>{Number(fila.error).toExponential(3)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}


        {resultado?.solucion && metodo === "Gauss-Seidel" && (
          <div className="resultado">
            <h2>Solución del sistema:</h2>
            <p>{resultado.solucion.map((v, i) => `x${i + 1} = ${v.toFixed(5)}`).join(" | ")}</p>
            <h3>Iteraciones:</h3>
            <table className="resultado-table">
              <thead>
                <tr>
                  <th>Iteración</th>
                  <th>Valores</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {resultado.pasos.map((fila, i) => (
                  <tr key={i}>
                    <td>{fila.iteracion}</td>
                    <td>{fila.valores.map(v => v.toFixed(4)).join(", ")}</td>
                    <td>{fila.error.toExponential(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {resultado?.solucion && metodo === "Jacobi" && (
          <div className="resultado">
            <h2>Solucion del sistema:</h2>
            <p>{resultado.solucion.map((v, i) => `x${i + 1} = ${v.toFixed(5)}`).join(" | ")}</p>
            <h3>Iteraciones:</h3>
            <table className="resultado-table">
              <thead>
                <tr>
                  <th>Iteración</th>
                  <th>Valores</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {resultado.pasos.map((fila, i) => (
                  <tr key={i}>
                    <td>{fila.iteracion}</td>
                    <td>{fila.valores.map(v => v.toFixed(4)).join(", ")}</td>
                    <td>{fila.error.toExponential(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
