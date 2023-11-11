from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import ContactoForm, DoctoresForm
from django.contrib import messages

# Create your views here.

def index (request):
    return render(request,'app/index.html')

def contacto (request):
    data = {
        'form': ContactoForm()
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



def agregar (request):

    data = {
        'form' : DoctoresForm()

    }

    if request.method == 'POST':
        formulario = DoctoresForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            messages.success(request,"Agregado correctamente")
            return redirect('listar')
        else:
            data["form"] = formulario

    return render(request,'app/docs/agregar.html',data)




def modificar (request,id):
    doctor = get_object_or_404(Doctor, id=id)

    data = {
        'form' : DoctoresForm(instance=doctor)

    }

    if request.method == 'POST':
        formulario = DoctoresForm(data=request.POST, instance=doctor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar")
        data["form"] = formulario
        



    return render(request,'app/docs/modificar.html',data)



def listar (request):
    doctores = Doctor.objects.all()
    data ={
        'doctores' : doctores

    }
    return render(request,'app/docs/listar.html',data)



def eliminar (request,id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar")



