from django.db import models
from .producto import Producto
from .sede import Sede

class Productoxsede(models.Model):

    id = models.BigAutoField(primary_key=True,unique=False,null=False)
    cantDisponible = models.IntegerField(null=False)
    cantReservada = models.IntegerField(null=False)
    refProducto = models.ForeignKey(Producto, on_delete=models.CASCADE,null=False)
    refSede = models.ForeignKey(Sede, on_delete=models.CASCADE,null=False)
    talla = models.CharField(max_length=5,null=False)