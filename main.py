from fastapi import FastAPI, HTTPException, Depends
from app.schemas import TareaBase, TareaResponse, UsuarioCreate, UsuarioLogin, UsuarioResponse
from app.database import engine
from app import models, crud, database, auth
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/tarea/", response_model=TareaResponse)
async def crear_tarea (tarea: TareaBase, db: Session = Depends(database.get_db), current_user: str = Depends(auth.get_current_user)):
    usuario = crud.get_usuario_by_email(db, current_user)
    return crud.create_tarea(db, tarea, usuario.id)

@app.get("/tarea/")
async def consultar_tareas(db: Session = Depends(database.get_db), current_user: str = Depends(auth.get_current_user)):
    usuario = crud.get_usuario_by_email(db, current_user)
    return crud.get_tareas(db, usuario.id)

@app.get("/tarea/{id}")
async def consultar_tareas_con_id(id: int, db: Session = Depends(database.get_db), current_user: str = Depends(auth.get_current_user)):
    tarea = crud.get_tarea(db, id)
    usuario = crud.get_usuario_by_email(db, current_user)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if tarea.usuario_id != usuario.id:
        raise HTTPException(status_code=403, detail="No tiene permisos")
    return tarea

@app.put("/tarea/{id}")
async def modificar_tarea (id: int, tarea: TareaBase, db: Session = Depends(database.get_db), current_user: str = Depends(auth.get_current_user)):
    tarea_db = crud.get_tarea(db, id)
    usuario = crud.get_usuario_by_email(db, current_user)
    if not tarea_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    if tarea_db.usuario_id != usuario.id:
        raise HTTPException(status_code=403, detail="No tiene permisos")
    tarea_actualizada = crud.update_tarea(db, id, tarea)
    return tarea_actualizada
    
@app.delete("/tarea/{id}")
async def eliminar_tarea (id: int, db: Session = Depends(database.get_db), current_user: str = Depends(auth.get_current_user)):
    tarea_existe = crud.get_tarea(db, id)
    usuario = crud.get_usuario_by_email(db, current_user)
    if not tarea_existe:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    if tarea_existe.usuario_id != usuario.id:
        raise HTTPException(status_code=403, detail="No tiene permisos")
    tarea_existe = crud.delete_tarea(db, id)
    return {"message": "Tarea eliminada"}

@app.post("/registro/", response_model=UsuarioResponse)
async def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(database.get_db)):
    email_existe = crud.get_usuario_by_email(db, usuario.email)
    if email_existe:
        raise HTTPException(status_code=400, detail="El correo ya está registado")
    return crud.create_usuario(db, usuario)
    
@app.post("/usuario/")
async def login_usuario(credenciales: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    usuario_existe = crud.get_usuario_by_email(db, credenciales.username)
    if not usuario_existe:
        raise HTTPException(status_code=401, detail="El usuario no está registrado")
    contraseña_correcta = auth.verify_password(credenciales.password, usuario_existe.hashed_password)
    if contraseña_correcta == False:
        raise HTTPException(status_code=404, detail="Contraseña invalida")
    token = auth.create_access_token(data={"sub": usuario_existe.email})
    return {"access_token": token, "token_type": "bearer"}
    