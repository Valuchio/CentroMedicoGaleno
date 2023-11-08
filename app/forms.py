from django import forms
from .models import Contacto, Doctor

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto 
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje"]
        fields = '__all__'


class DoctoresForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'
