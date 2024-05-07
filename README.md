# backGeoCatatumbo

## Descripción

**backGeoCatatumbo** es un proyecto que integra funcionalidades administrativas y APIs para el sitio web. Este proyecto utiliza tecnologías modernas y librerías especializadas para ofrecer soluciones robustas y eficientes.

## Tecnologías Utilizadas

- **Django**: Un framework de Python para el desarrollo de aplicaciones web.
- **Django REST Framework**: Para construir APIs web.
- **GeoPandas**: Una biblioteca de Python para manipular datos geoespaciales.
- **MongoDB**: Un sistema de base de datos NoSQL para almacenamiento de datos.

### Creación del Entorno Virtual

Primero, necesitas crear un entorno virtual para aislar las dependencias de tu proyecto. Abre tu terminal y ejecuta:
- **`.\venv\Scripts\activate`**

### Creación del Proyecto Django


##### Por último para crear el proyecto: #####
- **`django-admin startproject name_project`** Reemplaza `name_project` con el nombre que desees para tu proyecto.

### Cómo arrancar el proyecto ###

-**`pipenv shell`** (Virtualización)

- **`pipenv install`** (Instalación de dependencias)

- **`python manage.py runserver`** (Correr el proyecto)

### ¿Qué hacer siempre que se instale una librería? ###

***`pip freeze > requirements.txt`*** Con este comando por consola actualizamos el archivo requirements con todos los paquetes instalados en el entorno virtual.


## Documentación Adicional

- **Django REST Framework**: [Documentación oficial](https://www.django-rest-framework.org/)
- **GeoPandas**: [Documentación oficial](https://geopandas.org/en/stable/docs.html)
- **MongoDB**: [Documentación oficial](https://www.mongodb.com/docs/)