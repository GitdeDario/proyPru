from django.urls import path
from . import views

urlpatterns=[
    path("", views.indice, name="elIndice"),
    path("<str:nombre>", views.saludos, name="saludos"),
    path("hola/app01", views.index, name="index"),
]