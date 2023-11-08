from django.urls import path
from .views import index, contacto, Doctores, agendar, agregar, listar, modificar

urlpatterns = [
    path('', index,name="index"),
    path('contacto/', contacto,name="contacto"),
    path('Doctores/', Doctores,name="Doctores"),
    path('agendar/', agendar,name="agendar"),
    path('agregar/', agregar,name="agregar"),
    path('listar/', listar,name="listar"),
    path('modificar/', modificar,name="modificar"),

]
