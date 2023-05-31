from django.http import HttpResponse
from django.shortcuts import render
# from .extraction import tarea1_request as lib_request
# from .models import Station

# Create your views here.
# def index(request):
#     cont = 0
#     lib_request.obtener_informacion_api(cont)
#     # TODO: Recupero la tabla que tengo en la BDD y la retorno por parametro
#     #stations = Station.objects.all()
#     stations = Station.objects.order_by('contador') # Ordenados por el contador
#     return render(request, 'index.html', {'stations': stations})

def hello(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")