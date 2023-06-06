import json
from django.http import HttpResponse
from django.shortcuts import render
from .extraction import tarea1_request as lib_request
from .extraction import tarea2_selenium as lib_selenium
from .models import Station
from .models import Keypay

# Create your views here.
def index(request):
    cont = 1
    # lib_request.obtener_informacion_api(cont)     #+Carga Dinamica

    # TODO: Recupero la tabla que tengo en la BDD y la retorno por parametro
    stations = Station.objects.order_by('contador')
    keypays = Keypay.objects.all()

    return render(request, 'index.html', { 'stations': stations, 'keypays': keypays })

def selenium(request):
    lib_selenium.paginaProcedimientosSancionatorios()

    # Cargar los datos del archivo JSON
    with open("web\static\json\procedimientos_sancionatorios.json") as archivo_json:
        selenium_json = json.load(archivo_json)

    return render(request, 'selenium.html', { 'selenium_json': selenium_json })
