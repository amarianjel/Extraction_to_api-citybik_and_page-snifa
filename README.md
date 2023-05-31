# Proyecto Django

<p align="center">
  <img src="https://www.opengis.ch/wp-content/uploads/2020/04/django-python-logo.png" alt="Logo Django">
</p>

# Tarea 1
Dada la siguiente API pública <https://api.citybik.es/v2/networks/bikerio> desarrolle los siguiente requerimientos:

-	Crear una función que obtenga la información presentada en la API pública (librerías a utilizar: requests, urllib3 o aiohttp).
-	Crear un modelo para la información obtenida.
-	Guardar en el modelo la información obtenida desde el API.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

# Tarea 2
Dada la siguiente url <https://snifa.sma.gob.cl/Sancionatorio/Resultado> desarrolle los siguiente requerimientos:

-	Crear un script para obtener la información presentada en la tabla de la url proporcionada (librerías a utilizar: BeautifulSoup o Selenium).
-	El script deberá recorrer todas las páginas y obtener la información de las tablas.
-	El script deberá crear un archivo .json con la información obtenida.
-	Generar modelo para guardar la información obtenida.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.


# Librerias adicionales

`pip install request`

`pip install psycopg2`




# Crear el entorno virtual
- Una vez dento de la carpeta madre, se crea el entorno virtual. Primero se instala.
1. `pip install virtualenv`
- Creo ahora el entorno virtual.
2. `virtualenv venv`
- Ahora se debe ejecutar o activar.
3. _./venv/Scripts/activate_
- Finalmente con F1 puedo seleccionar el python que yo deseo para mi trabajo.

# Instalar DJANGO
1. `pip install django`
2. `django-admin --version`
- Ahora para crear al proyecto inicial debemos utilizar el siguiente comando seguido de la carpeta como se llamara. ***El punto es para decirle que coloque la carpeta en la raiz y no que en la raiz realice una capeta y dentro de ella el proyecto.***
3. `django-admin startproyect nombreDelProyecto .`
- Para correr el archivo
4. `python manage.py runserver 8000`


# Aplicaciones
Django ve asi las aplicaciones, se pueden ir quitando o agregando como funcionalidades

<p align="center">
  <img src="Aplicaciones.png" alt="Forma de que ve DJango">
</p>

`python manage.py startapp nombreAplicacion`


# BDD POSTGRESQL
- Instalar la bdd de datos a ocupar, luego configurarla en DATABASES{} (aplicacionBase/setting.py). Comandos Generales primero
1. `python manage.py makemigrations`
2. `python manage.py migrate`
- Crear la tabla en models.py y agregar en INSTALLED_APPS (setting.py) la aplicacion base.
- Ejecutar las migraciones
1. `python manage.py makemigrations nombreAplicacion`
2. `python manage.py migrate nombreAplicacion`
*Si la bdd se borro desde postgres, realizar pasos para la conexion desde el principio creando una nueva bdd*









# Eliminar venv y restaurar
- Exportar la lista de paquetes mediante `pip freeze > requirements.txt`
- Luego cerrar el entorno y eliminar la carpeta.
- Para restaurar, seguir los mismos pasos para crearlo `python -m venv nombreENV`
- Activarlo y instalar las dependencias `pip install -r requirements.txt`


|Columna 1|Columna 2|
|--------|--------|
|    A    |    B    |
|    C    |    D    |
