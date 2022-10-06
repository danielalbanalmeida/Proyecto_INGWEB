from django.db import models


# Create your models here.
class Empleado(models.Model):
    id = models.CharField(max_length=20)
    Nombre=models.CharField(max_Length=255)
    Apellido=models.CharField(max_Length=255)
    Email=models.EmailField()
    Contacto=models.CharField(max_Length=15)

    def __str__ (self):
        return "%s" %(self.Nombre)

    class Meta:
        db_table="empleado"
