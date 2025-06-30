from fastapi import FastAPI
from pydantic import BaseModel
from app.controllers import usuario_controller, mensaje_controller  # importa tus routers
from typing import List

app = FastAPI()

app.include_router(usuario_controller.router)
app.include_router(mensaje_controller.router)
