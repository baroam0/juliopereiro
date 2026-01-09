

from django import forms
from django.contrib.auth.models import User

from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    descripcion = forms.CharField(
        label="Descripcion"
    )

    observacion = forms.CharField(
        label="Observacion", required=False
    )

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Proveedor
        fields = [
            "descripcion", "domicilio", "localidad", "codpostal",
            "cuit", "telefono", "fax", "provincia", "pais", "observacion", 
            "email"
        ]
      
