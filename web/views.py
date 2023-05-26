from django.http import HttpResponse
from django.shortcuts import render
from .extraction import tarea1_request as lib_request

# Create your views here.
def index(request):
    cont = 0
    info = lib_request.obtener_informacion_api(cont)
    return render( request, 'index.html', { 'info': info } )

def hello(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")