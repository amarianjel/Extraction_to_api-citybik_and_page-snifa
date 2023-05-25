from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render( request, 'index.html' )

def hello(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")