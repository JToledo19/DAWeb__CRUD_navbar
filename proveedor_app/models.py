from django.db import models

# Create your models here.

class Proveedor (models.Model):
    id_proveedor=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    nombre_empresa=models.CharField(max_length=100)
    contacto=models.CharField(max_length=100)
    telefono=models.IntegerField()
    correo_electronico=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    productos=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empresa
