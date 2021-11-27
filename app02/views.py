from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indiceApp2(request):
    return HttpResponse("Hola amigos! <br> Esto es app02.")