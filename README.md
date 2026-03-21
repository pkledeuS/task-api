Este es un proyecto el cual tiene como propósito crear un CRUD funcional a través de endpoints de FastAPI y junto con una base de datos en PostgreSQL.

- Para poder iniciarlo debes tener Python instalado en tu sistema
- Clona el repositoio en algúna ruta de preferencia
- Debes crear tu ambiente virtual con 'python -m venv venv' abriendo la terminal en la raiz del directorio
- Posteriormente debes entrar en el ambiente virtual con '.\venv\Scripts\activate'
- Y finalmente ejecutar el archvio de "requirementes.txt" con 'pip install -r requirements.txt'
- Debes crear un archivo '.env' en la raiz del directorio y agregar la URL con la conexión a la base de datos junto con tu contraseña
- Para iniciar el servidor debes ir a la raiz del proyecto y ejecutar 'uvicorn main:app --reload'
- Dentro de la terminal, aparecera una URL local la cual servirá para probar cada endpoint, al final de la URL debes agregar '/docs' para ver cada metodo

- Los endpoints que podemos encontrar son los siguientes:
    * Get (/tarea/): Para consultar todas las tareas.
    * Get especifico (/tarea/{id}): Para consultar tareas especificas a través de id.
    * Post (/tarea/): Para poder crear tareas.
    * Put (/tarea/{id}): Para modificar tareas especificas a través de id.
    * Delete (/tarea/{id}): Para eliminar tareas especificas a través de id.
