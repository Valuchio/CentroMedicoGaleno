from django.db import models
from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.especialidad 

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="docs", null=True)

    def __str__(self):
        return self.nombre

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No se puede elegir una fecha pasada.')
    if weekday in [5, 6]:  # Sábado o domingo
        raise ValidationError('Elija un día laborable de la semana.')

class AgendaDoctor(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Introduzca una fecha para el calendario", validators=[validar_dia])
    rut = models.CharField(max_length=12, help_text="Ingrese su rut")

    HORARIOS = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.doctor}'

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "otros"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre