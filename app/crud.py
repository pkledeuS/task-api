from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password

def get_tareas(db: Session):
    return db.query(models.Tarea).all()

def get_tarea(db:Session, id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == id).first()

def create_tarea(db:Session, tarea: models.Tarea):
    nueva_tarea = models.Tarea(**tarea.model_dump())
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea 

def update_tarea(db:Session, id: int, tarea: models.Tarea):
    tarea_a_modificar = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    for key, value in tarea.model_dump().items():
        setattr(tarea_a_modificar, key, value)
    db.commit()
    return tarea_a_modificar 

def delete_tarea(db: Session, id: int):
    tarea_a_eliminar = db.query(models.Tarea).filter(models.Tarea.id == id).first()
    db.delete(tarea_a_eliminar)
    db.commit()
    return tarea_a_eliminar

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    pass_hasheada = hash_password(usuario.contraseña)
    nuevo_usuario = models.Usuario(email=usuario.email, hashed_password=pass_hasheada)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def get_usuario_by_email (db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()