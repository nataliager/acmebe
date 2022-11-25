from django.db import models

class Proveedor(models.Model):

    id = models.CharField( max_length=11,primary_key= True, unique=True, null=False)
    nombre = models.CharField(max_length=30, unique=False, null=False)
    telefono = models.CharField(max_length=15, unique=False, null=True)
    correo = models.EmailField( max_length=50, null=False)