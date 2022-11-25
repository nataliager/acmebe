from django.db import models

class Sede(models.Model):

    id = models.BigAutoField(primary_key=True,unique=False,null=False)
    ciudad = models.CharField(max_length=20, null=False)
    direccion = models.CharField( max_length=30, null=False)
    telefono = models.CharField(max_length=15, unique=False, null=False)
    