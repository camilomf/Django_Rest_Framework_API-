from django.db import models

# Create your models here.

class Heroe(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    poder = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre