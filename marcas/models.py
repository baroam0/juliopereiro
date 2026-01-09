
from django.db import models


class Marca(models.Model):
    fecha = models.DateField(auto_now=True)
    descripcion = models.CharField(max_length=50, unique=True)
    codigoaccess = models.IntegerField()

    def __str__(self):
        return self.descripcion.upper()
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Marcas"


# Create your models here.
