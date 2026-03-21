from fastapi import FastAPI, HTTPException, Depends
from app.schemas import TareaBase, TareaResponse
from app.database import engine
from app import models, crud, database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/tarea/", response_model=TareaResponse)
async def crear_tarea (tarea: TareaBase, db: Session = Depends(database.get_db)):
    return crud.create_tarea(db, tarea)

@app.get("/tarea/")
async def consultar_tareas(db: Session = Depends(database.get_db)):
    return crud.get_tareas(db)

@app.get("/tarea/{id}")
async def consultar_tareas_con_id(id: int, db: Session = Depends(database.get_db)):
    tarea = crud.get_tarea(db, id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.put("/tarea/{id}")
async def modificar_tarea (id: int, tarea: TareaBase, db: Session = Depends(database.get_db)):
    tarea_existe = crud.get_tarea(db, id)
    if not tarea_existe:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea = crud.update_tarea(db, id, tarea)
    return tarea
    
@app.delete("/tarea/{id}")
async def eliminar_tarea (id: int, db: Session = Depends(database.get_db)):
    tarea_existe = crud.get_tarea(db, id)
    if not tarea_existe:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tarea_existe = crud.delete_tarea(db, id)
    return {"message": "Tarea eliminada"}
