from django.db import models

# Create your models here.

class Ventas (models.Model):
    id_empleado=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    id_producto=models.IntegerField()
    id_cliente=models.IntegerField()
    cantidad_producto=models.IntegerField()
    fecha=models.DateField(max_length=100)
    precio_total=models.IntegerField()
    metodo_pago=models.CharField(max_length=100)

    def __str__(self):
        return self.id_producto
