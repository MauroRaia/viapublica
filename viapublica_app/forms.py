from django import forms

from .models import *

class ReclamoForm(forms.ModelForm):

    class Meta:
        model = Reclamo
        fields = ('nombre', 'apellido','dni', 'correo', 'telefono', 'descripcion')
