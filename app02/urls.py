from django.urls import path
from . import views

urlpatterns=[
    path("", views.indiceApp2, name="elIndiceDeApp2")
]