# Tutorial Flask 
[tutorial](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/)

## Asi debera quedar el proyecto
/home/user/Projects/flask-tutorial  
├── flask_todolist/  
│   ├── __init__.py  
│   ├── db.py  
│   ├── schema.sql  
│   ├── auth.py  
│   ├── blog.py  
│   ├── templates/  
│   │   ├── base.html  
│   │   ├── auth/  
│   │   │   ├── login.html  
│   │   │   └── register.html  
│   │   └── blog/  
│   │       ├── create.html  
│   │       ├── index.html  
│   │       └── update.html  
│   └── static/  
│       └── style.css  
├── tests/  
│   ├── conftest.py  
│   ├── data.sql  
│   ├── test_factory.py  
│   ├── test_db.py  
│   ├── test_auth.py  
│   └── test_blog.py  
├── .venv/  
├── pyproject.toml  
└── MANIFEST.in  

## creando el entorno virtual
mkdir flask_todolist

cd flask_todolist

python3 -m venv .venv 

. .venv/bin/activate ó source .venv/bin/activate

## Instalando el framework y modulo de conexion
pip install flask

## Ejecutando el proyecto
cd ~/scripts_py/Introduccion_FLASK/flask-tutorial

flask --app flask_todolist init-db

flask --app flask_todolist run --debug

Open http://127.0.0.1:5000 in a browser.


## Inicializar el archivo de base de datos
Si todavía está ejecutando el servidor desde la página anterior, puede detener el servidor o ejecutar este comando en una nueva terminal. Si usa una terminal nueva, recuerde cambiar al directorio de su proyecto y activar el env como se describe en Instalación.

flask --app flask_todolist init-db
Initialized the database.

## Instalable
pip install yourproject.whl

## Comando para ejecutar las pruebas
pip install pytest coverage

pytest ó coverage run -m pytest
