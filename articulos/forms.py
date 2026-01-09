


from django import forms
from django.contrib.auth.models import User

from .models import Articulo


class ArticuloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Articulo
        fields = "__all__"
        exclude = ["pk"]
