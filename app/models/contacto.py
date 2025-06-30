from datetime import datetime
from pydantic import BaseModel

class Contacto(BaseModel):
    alias: str
    fechaRegistro: datetime
