Este es un proyecto el cual tiene como propósito crear un CRUD funcional a través de endpoints de FastAPI y actualmente funcionando con un almacenamiento a través de un arreglo.

- Para poder iniciiarlo debes tener Python instalado en tu sistema
- Debes crear tu ambiente virtual 'python -m venv venv'
- Posteriormmente debes entrar en el '.\venv\Scripts\activate'
- Y finalmente ejecutar el archvio de "requirementes.txt" con 'pip install -r requirements.txt'
- Para iniciar el servidor debes ir a la raiz del proyecto y ejecutar 'uvicorn main:app --reload'
- Dentro de la terminal, aparecera una url local la cual servirá para probar cada endpoint, solo que al final de la URL debes agregar '/docs'

- Los endpoints que podemos encontrar son los siguientes:
    * Post(/tarea/): Para poder crear tareas.
    * Get(/tarea/): Para consultar todas las tareas.
    * Get{id}(/tarea/{id}): Para consultar tareas especificas.
    * Put{id}(/tarea/{id}): Para modificar tareas especificas.
    * Delete{id}(/tarea/{id}): Para eliminar tareas especificas.
