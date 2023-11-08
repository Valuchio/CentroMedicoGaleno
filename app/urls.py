from django.urls import path
from .views import index, contacto, Doctores, agendar

urlpatterns = [
    path('', index,name="index"),
    path('contacto/', contacto,name="contacto"),
    path('Doctores/', Doctores,name="Doctores"),
    path('agendar/', agendar,name="agendar"),
]
