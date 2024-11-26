from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    id_cliente=models.IntegerField()
    fecha_pedido=models.CharField(max_length=100)
    total_pedido=models.IntegerField()
    estado_pedido=models.CharField(max_length=100)
    metodo_pago=models.CharField(max_length=100)
    direccion_envio=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
