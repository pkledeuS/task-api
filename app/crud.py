from sqlalchemy.orm import Session
from app import models

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