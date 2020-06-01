# Login simple con Flask

Este proyecto es un ejemplo simple de un control de acceso en Python utilizando las siguientes paquetes:
* flask (https://flask.palletsprojects.com/en/1.1.x/)
* flask-sqlalchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* flask-bcrypt (https://flask-bcrypt.readthedocs.io/en/latest/)

Para la instalación de paquetes en este proyecto se utilizó **pipenv** (https://pipenv.pypa.io/en/latest/).

## Instalación pipenv

Se debe instalar *pipenv* de manera global en el sistema con el siguiente comando:

> $ pip install pipenv

Posterior a la instacíon de *pipenv* y para inicializar el entorno virtual e instalar todas las dependencias (*Pipfile*) se debe ejecutar el siguiente comando desde la raiz del proyecto:

> $ pipenv install

## Ejecución del proyecto

Para ejecutar el proyecto se debe ingresar el entorno virtual con el comando:

> $ pipenv shell

y ya dentro del entorno virtual se ejecuta:

> $ python app.py

El proyecto se encarga de crear la base de datos (SQLlite), tablas y un usuario de prueba:

* **username:** admin
* **password:** admin

## Rutas del proyecto

#### Página principal:
> localhost:3000/

#### Login:
> localhost:3000/login

#### Ruta de prueba para el API:
> localhost:3000/api/test