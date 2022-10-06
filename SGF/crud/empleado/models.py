from django.db import models


# Create your models here.
class Empleado(models.Model):
    ide = models.CharField(max_length=20)
    nombre=models.CharField(max_length=255)
    email=models.EmailField()
    contacto=models.CharField(max_length=15)

    def __str__(self):
        return "%s " % (self.nombre)

    class Meta:
        db_table = "empleado"
