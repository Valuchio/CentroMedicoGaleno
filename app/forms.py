from django import forms
from .models import Contacto, opciones_consultas, Doctor, AgendaDoctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto 
        fields = '__all__'


class DoctoresForm(forms.ModelForm):

    
    class Meta:
        model = Doctor
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1", "password2"]


class AgendaDoctorForm(forms.ModelForm):
    horario = forms.ChoiceField(choices=AgendaDoctor.HORARIOS)

    class Meta:
        model = AgendaDoctor
        fields = ['doctor', 'rut', 'dia', 'horario']