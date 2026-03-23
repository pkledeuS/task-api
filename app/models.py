import datetime
from app.database import Base
from sqlalchemy import Integer, String, Date, Time, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Tarea(Base):
    __tablename__ = "tareas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre_tarea: Mapped [str] = mapped_column(String(100))
    description: Mapped [str] = mapped_column(String(255))
    fecha: Mapped [datetime.date] = mapped_column(Date)
    hora: Mapped [datetime.time] = mapped_column(Time)
    termino: Mapped [bool] = mapped_column(Boolean, default=False)
    usuario_id: Mapped [int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)