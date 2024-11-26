from django.db import models

# Create your models here.

class Reseña (models.Model):
    id_reseña=models.PositiveSmallIntegerField(primary_key=True,max_length=6)
    id_producto=models.IntegerField()
    id_cliente=models.IntegerField()
    calificacion=models.IntegerField()
    comentario=models.CharField(max_length=100)
    fecha_reseña=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)

    def __str__(self):
        return self.comentario
