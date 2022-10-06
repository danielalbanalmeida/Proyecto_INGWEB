from django import forms
from empleado.models import Empleado
from django.forms import fields


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
