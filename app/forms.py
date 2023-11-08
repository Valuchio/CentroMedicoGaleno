from django import forms
from .models import Contacto, opciones_consultas, Doctor


class ContactoForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    tipo_consulta = forms.IntegerField(widget=forms.Select(choices=opciones_consultas, attrs={"class":"form-select" }))
    mensaje = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


    class Meta:
        model = Contacto 
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje"]
        fields = '__all__'


class DoctoresForm(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    edad = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Doctor
        fields = '__all__'
