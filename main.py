from fastapi import FastAPI, HTTPException
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

app = FastAPI()
tareas = []

@app.post("/tarea/", response_model=TareaResponse)
async def crear_tarea (tarea: TareaBase):
    nuevo_id = len(tareas) + 1 
    nueva_tarea = TareaResponse (id=nuevo_id, **tarea.model_dump())
    tareas.append(nueva_tarea)
    return nueva_tarea

@app.get("/tarea/")
async def consultar_tareas():
    return tareas

@app.get("/tarea/{id}")
async def consultar_tareas_con_id(id: int):
    for tarea in tareas: 
        if tarea.id == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tarea/{id}")
async def modificar_tarea (id: int, tarea: TareaBase):
    for i, tarea_actual in enumerate(tareas):
        if tarea_actual.id == id:
            tarea_modificada = TareaResponse(id= id, **tarea.model_dump())
            tareas[i] = tarea_modificada
            return tarea_modificada
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tarea/{id}")
async def eliminar_tarea (id: int):
    for i, tarea_actual in enumerate(tareas):
        if tarea_actual.id == id:
            tareas.pop(i)
            return {"message": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
