from fastapi import FastAPI, HTTPException, Depends
from app.schemas import TareaBase, TareaResponse, UsuarioCreate, UsuarioLogin, UsuarioResponse
from app.database import engine
from app import models, crud, database, auth
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

@app.post("/registro/", response_model=UsuarioResponse)
async def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(database.get_db)):
    email_existe = crud.get_usuario_by_email(db, usuario.email)
    if email_existe:
        raise HTTPException(status_code=400, detail="El correo ya está registado")
    return crud.create_usuario(db, usuario)
    
@app.post("/Usuario/")
async def login_usuario(credenciales: UsuarioLogin, db: Session = Depends(database.get_db)):
    usuario_existe = crud.get_usuario_by_email(db, credenciales.email)
    if not usuario_existe:
        raise HTTPException(status_code=401, detail="El usuario no está registrado")
    contraseña_correcta = auth.verify_password(credenciales.contraseña, usuario_existe.hashed_password)
    if contraseña_correcta == False:
        raise HTTPException(status_code=404, detail="Contraseña invalida")
    token = auth.create_access_token(data={"sub": usuario_existe.email})
    return {"access_token": token, "token_type": "bearer"}
    