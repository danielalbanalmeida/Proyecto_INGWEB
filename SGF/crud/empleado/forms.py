from django import forms
from django.forms import fields
from empleado.models import Empleado


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "_all_"
