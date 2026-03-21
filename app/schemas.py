from pydantic import BaseModel
from datetime import date, time

class TareaBase(BaseModel):
    nombre_tarea: str
    description: str
    fecha: date
    hora: time
    termino: bool

class TareaResponse(TareaBase):
    id: int