from django.db import models

class Proveedor(models.Model):
    codigoaccess = models.IntegerField()
    descripcion = models.CharField(max_length=50, unique=True)
    domicilio = models.CharField(max_length=150, null=True, blank=True)
    localidad = models.CharField(max_length=150, null=True, blank=True)
    codpostal = models.CharField(max_length=50, null=True, blank=True)
    cuit = models.CharField(max_length=15, unique=False, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    provincia = models.CharField(max_length=150, null=True, blank=True)
    pais = models.CharField(max_length=150,null=True, blank=True )
    observacion = models.CharField(max_length=150, unique=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.descripcion.upper()
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Proveedores"


# Create your models here.
