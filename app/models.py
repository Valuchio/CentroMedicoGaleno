from django.db import models

# Create your models here.

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
    fechas = models.DateField()
    imagen = models.ImageField(upload_to="docs",null=True)

    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0,"Reclamo"],
    [1,"Sugerencia"],
    [2,"Toma de Hora"],
    [3,"Otros"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices = opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
