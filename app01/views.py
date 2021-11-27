from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indice(request):
    return HttpResponse("hola amigos!")

def saludos(request, nombre):
    return render(request,"app01/holas.html",{
        "nombre":nombre.capitalize()
    })    


def index(request):
    return render (request, "app01/index.html")