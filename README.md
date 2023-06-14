<div align="center">

# Proyecto [Django](https://www.djangoproject.com/) &middot; [<img src="https://i.postimg.cc/wT4x8tWS/codepenblanco.png" alt="LinkedIn" class="footer-nav__link-image" height="30px" />](https://codepen.io/amarianjel/)   [<img src="https://i.postimg.cc/5NBMxTJX/github.png" alt="GitHub" class="footer-nav__link-image" height="30px" />](https://github.com/amarianjel)   [<img src="https://i.postimg.cc/1Xj3mL3G/github-Pages-blanco.png" alt="GitHub" class="footer-nav__link-image" height="70px" style="margin-bottom: -20px;"/>](https://amarianjel.github.io/Portfolio/)  [<img src="https://i.postimg.cc/J7BLFtdc/linkedin.png" alt="LinkedIn" class="footer-nav__link-image" height="30px" />](https://www.linkedin.com/in/amarianjel/)   [<img src="https://i.postimg.cc/1zqYRTyp/facebook.png" alt="LinkedIn" class="footer-nav__link-image" height="30px" />](https://www.facebook.com/Abraham13071993/)   [<img src="https://i.postimg.cc/sfJtqS4W/instagram.png" alt="Instagram" class="footer-nav__link-image" height="30px" />](https://www.instagram.com/abr_marianjel/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/django/django)
[![Up to Date](https://github.com/ikatyang/emoji-cheat-sheet/workflows/Up%20to%20Date/badge.svg)](https://github.com/ikatyang/emoji-cheat-sheet/actions?query=workflow%3A%22Up+to+Date%22)
[![Last Commit](https://img.shields.io/github/last-commit/amarianjel/Extraction_to_api-citybik_and_page-snifa?color=blue)](https://github.com/amarianjel/Extraction_to_api-citybik_and_page-snifa/commits/main)
[![forthebadge](https://img.shields.io/badge/Made%20with-Django-darkgreen.svg)](https://www.djangoproject.com/)
[![forthebadge](https://img.shields.io/badge/Made%20with-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![forthebadge](https://img.shields.io/badge/Made%20with-Requests-yellowgreen.svg)](https://requests.readthedocs.io/)
[![forthebadge](https://img.shields.io/badge/Made%20with-Selenium-green.svg)](https://www.selenium.dev/)
[![Issues](https://img.shields.io/github/issues/amarianjel/Extraction_to_api-citybik_and_page-snifa?color=0088ff)](https://github.com/amarianjel/Extraction_to_api-citybik_and_page-snifa/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/amarianjel/Extraction_to_api-citybik_and_page-snifa?color=0088ff)](https://github.com/amarianjel/Extraction_to_api-citybik_and_page-snifa/pulls)

</div>


<p align="center">
  <img src="https://www.opengis.ch/wp-content/uploads/2020/04/django-python-logo.png" alt="Logo Django">
</p>

[Leer como usar Django en tu proyecto](https://docs.djangoproject.com/en/4.2/).

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
## 📑 Tarea 1 📑
Dada la siguiente API pública <https://api.citybik.es/v2/networks/bikerio> desarrolle los siguiente requerimientos:

-	Crear una función que obtenga la información presentada en la API pública (librerías a utilizar: requests, urllib3 o aiohttp).
-	Crear un modelo para la información obtenida.
-	Guardar en el modelo la información obtenida desde el API.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/solar.png)

## 📑 Tarea 2 📑
Dada la siguiente url <https://snifa.sma.gob.cl/Sancionatorio/Resultado> desarrolle los siguiente requerimientos:

-	Crear un script para obtener la información presentada en la tabla de la url proporcionada (librerías a utilizar: BeautifulSoup o Selenium).
-	El script deberá recorrer todas las páginas y obtener la información de las tablas.
-	El script deberá crear un archivo .json con la información obtenida.
-	Generar modelo para guardar la información obtenida.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


## 👨‍💻 Tecnologías Usadas 👨‍💻
<table>
  <thead>
    <tr>
      <th>Django</th>
      <th>CSS</th>
      <th>Request</th>
      <th>Selenium</th>
      <th>PostgreSQL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <img src="https://i.postimg.cc/05MYmxp1/django.png" width="150px" />
      </td>
      <td>
        <img src="https://i.postimg.cc/mgSDG9F2/css.png" width="150px" />
      </td>
      <td>
        <img src="https://i.postimg.cc/kXtn2xRM/requests-sidebar.png" width="150px" />
      </td>
      <td>
        <img src="https://i.postimg.cc/3wkR6rrK/selenium.png" width="150px" />
      </td>
      <td>
        <img src="https://i.postimg.cc/YCbGZy1x/postgresql.png" width="150px" />
      </td>
    </tr>
  </tbody>
</table>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

# 🚀 Crear el entorno virtual 🚀
1. Una vez dento de la carpeta madre, se crea el ntorno virtual. Primero se instala.
```js
pip install virtualenv
```

2. Creo ahora el entorno virtual.
```js
virtualenv venv
```
3. Ahora se debe ejecutar o activar.
```js
_./venv/Scripts/activate_
```
4. Finalmente con F1 puedo seleccionar el python que yo deseo para mi trabajo.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🛠 Instalar DJANGO 🛠
```js
pip install django
```
```js
django-admin --version
```
Ahora para crear al proyecto inicial debemos utilizar el siguiente comando seguido de la carpeta como se llamara. ***El punto es para decirle que coloque la carpeta en la raiz y no que en la raiz realice una capeta y dentro de ella el proyecto.***
```js
django-admin startproject nombreDelProyecto 
```
```js
django-admin startproject myapp .
```
Para correr el archivo
```js
python manage.py runserver 8000
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🚩 Aplicaciones 🚩
Django ve asi las aplicaciones, se pueden ir quitando o agregando como funcionalidades

<p align="center">
  <img src="./web/static/img/Aplicaciones-django.png" alt="Forma de que ve DJango">
</p>

```js
python manage.py startapp nombreAplicacion
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🛠 BDD PostgreSQL 🛠
- Instalar la bdd de datos a ocupar, luego configurarla en DATABASES{} (aplicacionBase/setting.py). Comandos Generales primero
```js
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'extraction_request',
      'USER': 'postgres',
      'PASSWORD': 'root',
      'HOST': 'localhost',
      'PORT': '5432',
  }
}
```
```js
python manage.py makemigrations
```
```js
python manage.py migrate
```

- Crear la tabla en models.py y agregar en INSTALLED_APPS (setting.py) la aplicacion base.
- Ejecutar las migraciones
```js
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'web',
]
```
```js
python manage.py makemigrations nombreAplicacion
```
```js
python manage.py migrate nombreAplicacion
```
*Si la bdd se borro desde postgres, realizar pasos para la conexion desde el principio creando una nueva bdd*


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🚀 Eliminar venv y restaurar 🚀
Exportar la lista de paquetes mediante 
```js
pip freeze > requirements.txt
```
Luego cerrar el entorno y eliminar la carpeta.
Para restaurar, seguir los mismos pasos para crearlo: 
```js
python -m venv nombreENV
```
Activarlo y instalar las dependencias 
```js 
pip install -r requirements.txt
```
**Finalmente puedo crear las carpetas nuevamente y copiar los archivos con los comandos para cada aplicacion**.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### Sintaxis
| **NOMBRE** | **SÍMBOLO** |
|--------|--------|
| *Template inheritance* | {% url 'index' %} |
| *Jinja Loops* | {% for station in stations %} |
| *Static Files* | {% load static %} |


## 🏫 Librerias adicionales 🏫
```js
pip install selenium
```
```js
pip install webdriver_manager
```
```js
pip install request

pip install psycopg2
```

***El código se encuentra en la app web, en view hay que descomentar para que el boot realice el web scrapy***

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

### 📑 Estructura del proyecto 📑
Esta estructura contempla las carpetas mas importantes con algunos archivos
```
request_selenium/
├── myapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── web/
|   ├── extraction/
|   |   ├── tarea1_request.py
|   |   ├── tarea2_selenium.py
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
|   |   ├── navbar.html
|   |   ├── selenium.html
│   ├── static/
|   |   ├── css/
|   |   |   ├── main.css
|   |   ├── img/
|   |   |   ├── Aplicaciones.png
|   |   |   ├── Baldr.png
|   |   ├── json/
|   |   |   ├── procedimientos_sanitarios.json
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .gitIgnore
├── manage.py
├── README.md
└── ...
