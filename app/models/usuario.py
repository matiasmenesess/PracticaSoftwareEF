from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .contacto import Contacto
from .mensaje import Mensaje
from typing import List, Optional


class Usuario(BaseModel):
    alias: str
    nombre: str
    listaContactos: Optional[List[Contacto]] = None
    mensajesEnviados: Optional[List[Mensaje]] = None
    mensajesRecibidos: Optional [List[Mensaje]] = None
