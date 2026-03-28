# TaskFlow - Backend (API)

Este es el backend de la aplicación **TaskFlow**, una API RESTful construida con **FastAPI** y **Python**. Proporciona todos los servicios necesarios para la gestión de usuarios (autenticación y autorización) y un CRUD completo para la gestión de tareas, utilizando **PostgreSQL** como base de datos.

## Características principales

- **Autenticación Segura:** Implementación de JSON Web Tokens (JWT) y encriptación de contraseñas mediante hashing.
- **Gestión de Tareas (CRUD):** Endpoints completos para crear, leer, actualizar y eliminar tareas.
- **Base de Datos Relacional:** Configurado para trabajar con PostgreSQL.
- **Documentación Interactiva:** Autogenerada por FastAPI (Swagger UI y ReDoc).
- **Contenedores:** Soporte para despliegue rápido usando Docker y Docker Compose.

## Tecnologías utilizadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/) (Servidor ASGI)
- JWT (JSON Web Tokens)
- Docker & Docker Compose

## Requisitos Previos

- **Python 3.8+** instalado en tu sistema.
- **PostgreSQL** en ejecución (o puedes usar Docker).

## Instalación y Configuración local

1. **Clona el repositorio** en la ruta de tu preferencia y entra al directorio `task-api`.

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto y agrega tus credenciales:
   ```env
   DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_bd
   SECRET_KEY=tu_clave_secreta_super_segura
   ```

## Ejecutar la aplicación

Para iniciar el servidor en modo desarrollo con recarga automática, ejecuta:

```bash
uvicorn main:app --reload
```

El servidor estará corriendo en `http://127.0.0.1:8000`. 
Para acceder a la **documentación interactiva y probar los endpoints**, navega a:
`http://127.0.0.1:8000/docs`

### Ejecutar con Docker (Opcional)
Si prefieres usar los contenedores, simplemente ejecuta:
```bash
docker-compose up --build
```

## Endpoints Principales

La API cuenta con las siguientes rutas (se pueden probar todas desde `/docs`):

### Tareas
- `GET /tarea/` - Consulta todas las tareas del usuario.
- `GET /tarea/{id}` - Consulta una tarea específica por su ID.
- `POST /tarea/` - Crea una nueva tarea.
- `PUT /tarea/{id}` - Modifica una tarea existente.
- `DELETE /tarea/{id}` - Elimina una tarea específica.

### Usuarios (Autenticación)
- `POST /registro/` - Crea (registra) un nuevo usuario.
- `POST /usuario/` - Inicia sesión y devuelve el token JWT.

## Estructura del Proyecto

```text
task-api/
 ├── app/
 │   ├── __init__.py
 │   ├── auth.py      # Lógica de seguridad y JWT
 │   ├── crud.py      # Operaciones de base de datos
 │   ├── database.py  # Conexión y sesión de BD
 │   ├── models.py    # Modelos ORM (SQLAlchemy)
 │   └── schemas.py   # Esquemas Pydantic para validación de datos
 ├── main.py          # Punto de entrada de la aplicación FastAPI
 ├── requirements.txt # Dependencias de Python
 ├── Dockerfile       # Instrucciones para la imagen Docker
 └── docker-compose.yml 
```