from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    formulario_reclamo = ReclamoForm()
    return render(request, 'views/index.html', {'formulario_reclamo': formulario_reclamo})

def reclamo_alta(request):
    # PROCESAR EL FORMULARIO
    if request.method == "POST":
        formulario = ReclamoForm(request.POST)
        if formulario.is_valid():
            form = formulario.save(commit=False)
            form.save()
            return render( request,'views/partials/ .html',{})
