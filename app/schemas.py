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
    usuario_id: int

class UsuarioCreate(BaseModel):
    email: str
    contraseña: str

class UsuarioResponse(BaseModel):
    id: int
    email: str
    activo: bool

class UsuarioLogin(BaseModel):
    email: str
    contraseña: str