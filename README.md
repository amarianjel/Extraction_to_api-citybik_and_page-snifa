# Proyecto Django

## Tarea 1
Dada la siguiente API pública https://api.citybik.es/v2/networks/bikerio desarrolle los siguiente requerimientos:

-	Crear una función que obtenga la información presentada en la API pública (librerías a utilizar: requests, urllib3 o aiohttp).
-	Crear un modelo para la información obtenida.
-	Guardar en el modelo la información obtenida desde el API.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

## Tarea 2
Dada la siguiente url https://snifa.sma.gob.cl/Sancionatorio/Resultado desarrolle los siguiente requerimientos:

-	Crear un script para obtener la información presentada en la tabla de la url proporcionada (librerías a utilizar: BeautifulSoup o Selenium).
-	El script deberá recorrer todas las páginas y obtener la información de las tablas.
-	El script deberá crear un archivo .json con la información obtenida.
-	Generar modelo para guardar la información obtenida.
-	Opcional. Generar vista en el administrador para visualizar la información obtenida.
-	Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.



# Librerias

pip install request

pip install psycopg2

## Para usar bdd
- Instalar la bdd de datos a ocupar, luego configurarla en DATABASES{} (aplicacionBase/setting.py).
- *Comandos*
> 1-. _python manage.py makemigrations_
> 2-. _python manage.py migrate_
- Crear la tabla en models.py y agregar en INSTALLED_APPS (setting.py) la aplicacion base.
- Ejecutar las migraciones *Comandos*
> 1-. _python manage.py makemigrations web_
> 2-. _python manage.py migrate web_
_Si la bdd se borro desde postgres, realizar pasos para la conexion desde el princio creando una nueva bdd_









## Eliminar venv y restaurar
- Exportar la lista de paquetes mediante _pip freeze > requirements.txt_
- Luego cerrar el entorno y eliminar la carpeta.
- Para restaurar, seguir los mismos pasos para crearlo _python -m venv nombreENV_
- Activarlo y instalar las dependencias _pip install -r requirements.txt_

