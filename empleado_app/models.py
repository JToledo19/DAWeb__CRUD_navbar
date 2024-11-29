from django.db import models

# Create your models here.

class Empleado (models.Model):
    id_empleado=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    id_ventas=models.IntegerField()
    nombre=models.CharField(max_length=100)
    telefono=models.IntegerField()
    sexo=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    turno=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
