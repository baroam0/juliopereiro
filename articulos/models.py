
from datetime import datetime

from django.db import models
from marcas.models import Marca
from proveedores.models import Proveedor


class Articulo(models.Model):
    codigoaccess = models.CharField(max_length=50, null=True, blank=True) 
    descripcion = models.CharField(max_length=250, null=False, blank=False)
    minimo = models.IntegerField(null=True, blank=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.IntegerField(null=True, blank=True)
    pventa1 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    pventa2 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    pventa3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    pventa4 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    comib = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    comiu = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    codigobarra = models.CharField(max_length=250, null=True, blank=True)
    pmoneda = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cotizacion = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    pcompra = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ocultar = models.BooleanField(default=False, null=True, blank=True)
    margen1 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    margen2 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    margen3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    margen4 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    d1 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    d2 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    d3 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    flete = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    fechaprecio = models.DateTimeField(null=True, blank=True)
    codigoproducto = models.CharField(max_length=250, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    selecciones = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.descripcion.upper()
    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.upper()
        ahora = datetime.now()
        self.fechaprecio=ahora
        super(Articulo, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Articulos"




# Create your models here.

