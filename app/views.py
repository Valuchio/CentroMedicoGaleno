from django.shortcuts import render
from .models import Doctor
from .forms import ContactoForm

# Create your views here.

def index (request):
    return render(request,'app/index.html')

def contacto (request):
    data = {
        'form': ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request,'app/contacto.html',data)

def Doctores (request):
    doctores = Doctor.objects.all()
    data = {
        'doctores' :doctores
    }
    
    return render(request,'app/Doctores.html',data)

def agendar (request):
    return render(request,'app/agendar.html')