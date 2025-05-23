# IteraX

**IteraX** is a web application designed to solve numerical methods interactively.  

It is composed of two parts: **Frontend** (React) and **Backend** (Python - FastAPI).

---

## 🎯 Motivation

**IteraX** was developed as part of an academic project for an evaluation at **UCASAL (Universidad Católica de Salta)**. The objective was to demonstrate the practical application of numerical methods through a full-stack solution, reinforcing concepts of algorithmic logic, software architecture, and user interface design.

**Team Members:**
- **[Agustín](https://github.com/Juarex9)**
- **[Alejo](https://github.com/aaalejo8)**
- **[Cate Daruich](https://github.com/catedaruich)**
- **[Cristiane](https://github.com/andrdcris)**
- **[Guada](https://github.com/Guada2-dot)**
- **[Joselito Júnior](https://github.com/joselitojunior)**
- **[Luciano Lazarte](https://github.com/Jehp23)**
- **[Máximo Cordoba](https://github.com/maxicordoba22)**
- **[Máximo Echazú](https://github.com/zMax98)**

---

## 🧠 About the Methods

The backend provides six numerical methods for finding the roots of a function:

- **Bisection Method**
- **False Position Method (Regula-Falsi)**
- **Newton-Raphson Method**
- **Secant Method**
- **Fixed Point Iteration**
- **Multiple Roots Method**

Each method iteratively finds approximations for the roots of mathematical functions based on user inputs.

---

## 🚀 Running the Application Remotely

### Backend Setup (Python - FastAPI)

1. **Clone the repository** and navigate to the backend directory.
   
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server:**

   ```bash
   uvicorn main:app --reload
   ```

The backend will be running at [http://localhost:8000](http://localhost:8000).

---

### Frontend Setup (React)

1. **Navigate to the frontend directory.**

2. **Install the required libraries:**

   ```bash
   npm install
   ```

3. **Start the frontend server:**

   ```bash
   npm start
   ```

The frontend will be running at [http://localhost:3000](http://localhost:3000).

---

## 📄 Project Documentation
This project includes a full Technical Documentation written in Spanish, covering all relevant aspects of the system and provides a comprehensive technical overview for developers and collaborators alike.

---

## 📚 Summary

- **Frontend:** React app to interact with numerical methods.
- **Backend:** Python FastAPI server with six implemented numerical methods.
- **Usage:** Input your function and interval/data, and visualize iterations and convergence through the UI.
