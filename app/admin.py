from django.contrib import admin
from .models import Especialidad, Doctor, AgendaDoctor, Contacto  

admin.site.register(Especialidad)
admin.site.register(Doctor)
admin.site.register(AgendaDoctor)
admin.site.register(Contacto) 