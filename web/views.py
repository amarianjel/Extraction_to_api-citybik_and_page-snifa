from django.http import HttpResponse
from django.shortcuts import render
from .extraction import tarea1_request as lib_request
from .models import Station

# Create your views here.
def index(request):
    cont = 1    # Aqui me doy cuenta si la libreria se puede editar o no
    #lib_request.obtener_informacion_api(cont)

    # TODO: Recupero la tabla que tengo en la BDD y la retorno por parametro
    stations = Station.objects.order_by('contador')
    return render(request, 'index.html', {'stations': stations})

def selenium(request):
    return render(request, 'selenium.html')

def about(request):
    return HttpResponse("<h1>About</h1>")
