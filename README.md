# Django-app

Trabajo de practica de fullstack con Django

## Comandos
#### Mostrar listas.
- `ls -la` Mostrar ficheros ocultos 
- `pip list`muestra los paquetes.
- `pip freeze`Lista los paquetes que tine el entorno virtual.
---
### Para colocar venv
- `py -m venv venv` se coloca el modulo y el segundo venv es el nombre que se le quiere dar.
- `django-admin startproject app .` instalar la carpeta en el mismo Sitio por el punto.

- `source` venv/script/ `activate` Se usa el "Source" como comando principal depende de como estas en la terminal y activate .
- `pip install django` instala "django".

- `rm -rf app/`Para borrar  elementos 

- `pip freeze > requirements.txt` para crear un txt en la carpeta  a través de paquetes.
- `pip install -r requirements.txt` actualizacion de los requirements.txt
---
### Activar el DJANGO para entrar.

- `source` venv/script/ `activate`
- `py manage.py runserver` para correr Django en el puerto //8000.
- `python manage.py runserver` para correr Django en el puerto //8000.
- ` crtl + c` para apagar el Puerto 

---
## Staging
- `git status` mira el estado actual
- `git add .` agrega los comabios al estado actual
- `git commit -m "//comentario"` colocar un comentario.
- `git push` subir el add y el comentario.

---
#### Realizar y visualizar la migracion
- Despues de aplica la base de datos de `models.py`
- `$py manage.py makemigrations` Crear migraciones o crear modelos.
- `$py manage.py migrate` Sube las migraciones a la base de datos.
- `$py manage.py showmigrations ` Visualizar migraciones. realizadas o pendientes


- #### Crear el super usuario  con el siguiente comando:
- `py manage.py createsuperuser` Crear el super usuario
- 
- `pip install psycopg2` para instalar controlador de python.

-  #### Cuando se clona el repositorio Cuanto ya l habia clonado anteriormente en el mismo sitio:
- `git pull`
- `pip install -r requirements.txt` Recuperar todos los paquetes que se descargaron en el repositorio

- ### Base de Datos `settings.py`
```python

'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app',
        "USER": 'postgres',
        'PASSWORD': 'unicesmag',
        'PORT': '5432',
    }
```
- `py manage.py migrate` para actualizar en postgres la data base
---
### Crear una nueva app a través de comandos de git

- `py manage.py startapp `(nombre que se le quiere dar) // para actualizar en postgres la data base

``` c++
INSTALLED_APPS = [
    `'academics.apps.AcademicsConfig',`
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


```
- `py manage.py makemigrations` Crea un nueva migración 
- `py manage.py showmigrations academics` visualizar la migración
- `py manage.py sqlmigrate academics 0001` Visualizar la migración 
- `py manage.py migrate` pasar la migración a pgAdmin

Visualizar el SQl de la base de datos
- `py manage.py sqlmigrate academics 0001`para visualizar el modelo 1
- `py manage.py sqlmigrate academics 0002`para visualizar el modelo 2 una vez actualizada la tabla

---

Agregar valores en la base de datos
- `Py manage.py shell`
- `from academics.models import User`
- `user = User(email = "carlos@gmail.com", password = "1234")`
- `user.save()`
- `User.objects.all()`
- `exit()`
---
# Intanciar variables de entorno en Django
- `.env` creamos en el proyecto principal
```python

DB_NAME=app
DB_USER=postgres
DB_PASSWORD=unicesmag
DB_HOST=localhost
DB_PORT=5432

```
- `export $(cat .env | grep -v '^#' | xargs)` Cuando se actualiza el puerto de `.env`




<!-- 
```python

def a:
    return 1
``` -->

---
<!-- 
1. a
2. b -->

