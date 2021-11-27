from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.
tasks=["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

def index(request):
    return render(request, "tasks/index.html",{
        "tasks":tasks
    })

# Add a new task:
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) # Guarda en la variable form, lo que el usuario escribió en el form (sea válido o no)
        if form.is_valid():   # Check if form data is valid (server-side). Revisa que la fecha tenga el formato, que si es un número que tenga que estar en un rango lo esté, etc
            task = form.cleaned_data["task"]  # Guarda en la variable task, lo que haya en el campo "task" del form. Este task hace referencia al task de la class NewTaskForm
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index")) # Redirecciona a index. HttpResponseRedirect es "lo mismo" que render, salvo que render puede recibir contexto y esto no.
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
# si es un GET:
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })