from datetime import datetime
from pydantic import BaseModel, Field

class Mensaje(BaseModel):
    # para una clase que se define luego
    remitente: 'Usuario'
    destinatario: 'Usuario'
    contenido: str
    fechaEnvio: datetime
