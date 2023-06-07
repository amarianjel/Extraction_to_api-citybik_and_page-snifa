
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def iniciarChrome():
    ruta = ChromeDriverManager().install()
    driver = webdriver.Chrome(ruta)
    return driver

def esperar_carga_completa(driver, tiempo_espera=10):
    wait = WebDriverWait(driver, tiempo_espera)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

def obtener_detalles(driver, enlace, datos):
    driver.get(enlace)
    esperar_carga_completa(driver)

    inicio = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[1]/div/div/h4[1]/i[2]').text

    t = driver.find_element(By.XPATH, '/html/body').text

    print(type(t), " => ", t)

    verDetalles = {
        "F_Inicio": inicio,
    }
    datos["Ver_Detalles"] = verDetalles

    # Encontrar la tabla de documentos
    tabla_documentos = driver.find_elements(By.XPATH, '//*[@id="documentos"]/table/tbody/tr')
    #abla_hechos = driver.find_elements(By.XPATH, '//*[@id="instrumentos-considerados"]')   # Esta tabla no funciona, por eso esta segmentado, tiene una carga dinamica.
    for fila in tabla_documentos:
        contador = fila.find_element(By.XPATH, './td[1]').text
        nombre = fila.find_element(By.XPATH, './td[2]').text
        tipo = fila.find_element(By.XPATH, './td[3]').text
        fecha = fila.find_element(By.XPATH, './td[4]').text

        documento = {
            "dCont": contador,
            "dNombre": nombre,
            "dTipo": tipo,
            "dFecha": fecha,
        }
        verDetalles["Documentos"] = documento

    driver.back()

def paginaProcedimientosSancionatorios():

    driver = iniciarChrome()
    driver.get("https://snifa.sma.gob.cl/Sancionatorio/Resultado")  # Cargar la página
    driver.implicitly_wait(10)  # Esperar hasta 10 segundos para que los resultados se carguen

    PAGINACION_MAX = 2
    PAGINACION_ACTUAL = 1
    diccionario_json = []   # Lista para almacenar los datos de los resultados

    while PAGINACION_MAX > PAGINACION_ACTUAL:
        # Encontrar los elementos que contienen los datos que deseas extraer
        tablas = driver.find_elements(By.XPATH, '//tr[@class="odd"] | //tr[@class="even"]') 

        for tabla in tablas:

            try:
                contador = tabla.find_element(By.XPATH, './td[1]').text
                expediente = tabla.find_element(By.XPATH, './td[2]').text
                unidadFiscalizadora = tabla.find_element(By.XPATH, './td[3]').text
                nombre = tabla.find_element(By.XPATH, './td[4]').text
                categoria = tabla.find_element(By.XPATH, './td[5]').text
                region = tabla.find_element(By.XPATH, './td[6]').text
                estado = tabla.find_element(By.XPATH, './td[7]').text

                print(contador, expediente)

                # Crear un diccionario con los datos del resultado actual
                datos = {
                    "Contador": contador,
                    "Expediente": expediente,
                    "Unidad_Fiscalizadora": unidadFiscalizadora,
                    "Nombre": nombre,
                    "Categoria": categoria,
                    "Region": region,
                    "Estado": estado
                }

                # Obtener el enlace de detalle
                enlace_detalle = tabla.find_element(By.XPATH, './td[8]/a').get_attribute('href')

                obtener_detalles(driver, enlace_detalle, datos)

                diccionario_json.append(datos)

            except Exception as e:
                print(e)
                # Si sucede algún error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
                driver.back()

        # Lógica de detección de fin de paginación
        try:
            # Intento obtener el botón de SIGUIENTE y le intento dar click
            puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[@id="myTable_next"]')
            puedo_seguir_horizontal.click()
        except Exception as e:
            print(e)
            break

        PAGINACION_ACTUAL += 1

    with open("web/static/json/procedimientos_sancionatorios.json", "w") as archivo_json:
        json.dump(diccionario_json, archivo_json, indent=4)

    driver.quit()