from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Especialidad, AgendaDoctor
from .forms import ContactoForm, DoctoresForm, CustomUserCreationForm, AgendaDoctorForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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


@login_required
def agendar(request):
    especialidades = Especialidad.objects.all()
    horarios = AgendaDoctor.HORARIOS
    doctores = Doctor.objects.all()

    if request.method == 'POST':
        form = AgendaDoctorForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:  # Asegurarse de que el usuario esté autenticado
                agenda_doctor = form.save(commit=False)
                agenda_doctor.user = request.user  # Asigna el usuario actual
                agenda_doctor.save()
                messages.success(request, "Cita agendada correctamente")
                return redirect('agendar')
            else:
                messages.error(request, "Error al agendar la cita. Usuario no autenticado.")
        else:
            messages.error(request, "Error al agendar la cita. Revise los datos.")
    else:
        form = AgendaDoctorForm()

    context = {
        'form': form,
        'especialidades': especialidades,
        'horarios': horarios,
        'doctores': doctores,
    }

    return render(request, 'app/agendar.html', context)

@permission_required('app.add_docs')
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



@permission_required('app.change_docs')
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


@permission_required('app.view_docs')
def listar (request):
    doctores = Doctor.objects.all()
    data ={
        'doctores' : doctores

    }
    return render(request,'app/docs/listar.html',data)


@permission_required('app.delete_docs')
def eliminar (request,id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)


