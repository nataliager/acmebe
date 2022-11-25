from django.db import models

class Producto(models.Model):

    id = models.BigAutoField(primary_key=True,unique=False,null=False)
    tipo = models.CharField(max_length=20, null=False)
    marca = models.CharField(max_length=30, null=False)
    color = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=80, null=True)