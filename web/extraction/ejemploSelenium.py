from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #* instala automaticamente 
from selenium.webdriver.chrome.service import Service as ChromeService
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciarChrome():
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    ruta = ChromeDriverManager( path='./chromedriver' ).install() #+ Instala el driver si no lo esta, el log es para que no aparezca nada en el terminal

    # TODO: Definimos el User Agent en Selenium utilizando la clase Options
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
    opts.add_argument("--window-size=500, 500") #+ Para configurar el ancho --start-maximized
    opts.add_argument("--disable-web-security")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--ignore-certificate-errors") #+ para ignaorar el aviso "Su conexion no es privada"
    opts.add_argument("--no-sandbox")
    opts.add_argument("--no-default-browser-check") #+ Aviso que no es navegador por defecto
    opts.add_argument("--no-first-run") #+ Evita la realizacion de ciertas tareas al principio
    opts.add_argument("--no-proxy-server")
    opts.add_argument("--disable-blink-features=AutomationControlled") #+  Evita que selenium sea detectado

    # TODO: PARÁMETROS A OMITIR EN EL INICIO DE CHROMEDRIVER
    exp_opt = [
        'enable-automation', #+ para que no muestre "software automatizado de pruebas"
        'ignore-certificate-errors', #+ para ignorar errores de certificados caducados
        'eneble-logging' #+ para que nos se muestre en la terminal "DevTools listening on..."
        ]
    opts.add_experimental_option( "excludeSwitches", exp_opt )

    # TODO: PARÁMETROS QUE DEFINEN LAS PREFERENCIAS EN CHROMEDRIVER
    prefs = {
        "profile.default_content_setting_values.automatic_downloads": 2, #+ notificaciones: 0=preguntar | 1=permitir | 2=no permitir
        "intl.accept_languages": [ "es-ES", "es" ], 
        "credentials_eneble_service": False #+ evita que Chrome nos pregunte si queremos guarar la info
        }
    opts.add_experimental_option( "prefs", prefs )

    # TODO: Instanciamos el driver
    service = ChromeService(ruta)
    driver = webdriver.Chrome( service=service, options=opts ) #+ Instanciamos web driver de Selenium con Chrome
    return driver


driver = iniciarChrome()
# Cargar la página
driver.get("https://snifa.sma.gob.cl/Sancionatorio/Resultado")

driver.implicitly_wait(10)  # Esperar hasta 10 segundos para que los resultados se carguen

PAGINACION_MAX = 5
PAGINACION_ACTUAL = 1

# Lista para almacenar los datos de los resultados
diccionario_json = []

while PAGINACION_MAX > PAGINACION_ACTUAL:

    # Encontrar los elementos que contienen los datos que deseas extraer
    tablas = driver.find_elements(By.XPATH, '//tr[@class="odd"] | //tr[@class="even"]') 

    for tabla in tablas:

        try:
            numero = tabla.find_element(By.XPATH, './td[1]').text
            expediente = tabla.find_element(By.XPATH, './td[2]').text
            unidadFiscalizadora = tabla.find_element(By.XPATH, './td[3]').text
            nombre = tabla.find_element(By.XPATH, './td[4]').text
            categoria = tabla.find_element(By.XPATH, './td[5]').text
            region = tabla.find_element(By.XPATH, './td[6]').text
            estado = tabla.find_element(By.XPATH, './td[7]').text

            print(numero , expediente)


            #+ Crear un diccionario con los datos del resultado actual
            datos = {
                "#": numero,
                "Expediente": expediente,
                "Unidad Fiscalizadora": unidadFiscalizadora,
                "Nombre": nombre,
                "Categoria": categoria,
                "Region": region,
                "Estado": estado
            }

            # Agregar el diccionario a la lista de datos de resultados
            diccionario_json.append(datos)

        except Exception as e:
            print (e)
            # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
            driver.back()
        
    # Logica de deteccion de fin de paginacion
    try:
        # Intento obtener el boton de SIGUIENTE y le intento dar click
        puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[@id="myTable_next"]')
        puedo_seguir_horizontal.click()
    except Exception as e:
        print (e)
        # Si obtengo un error al intentar darle click al boton, quiere decir que no existe
        # Lo cual me indica que ya no puedo seguir paginando, por ende rompo el While
        break

    PAGINACION_ACTUAL += 1
        
#+ Guardar los datos en un archivo JSON
with open("procedimientos_sancionatorios.json", "w") as archivo_json:
    json.dump(diccionario_json, archivo_json, indent=4)
    
driver.quit()