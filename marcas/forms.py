

from django import forms
from django.contrib.auth.models import User

from .models import Marca


class MarcaForm(forms.ModelForm):
    descripcion = forms.CharField(
        label="Descripcion"
    )

    def __init__(self, *args, **kwargs):
        super(MarcaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Marca
        fields = ["descripcion"]
