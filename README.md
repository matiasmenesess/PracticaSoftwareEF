# PracticaSoftwareEF

python -m venv venv
.\venv\Scripts\activate

Paso 1:
pip install fastapi uvicorn

Explicaciones:

fastapi: el framework para crear APIs.

uvicorn: un servidor que ejecuta FastAPI.

Paso 2:

el main debe verse como:

# main.py
from fastapi import FastAPI

# Creamos la app
app = FastAPI()

# Ruta de prueba (endpoint)
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola mundo desde FastAPI!"}

# Otra ruta con parámetro
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}

Para ejecutar:

uvicorn main:app --reload
