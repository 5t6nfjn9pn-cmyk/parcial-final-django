from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ["codigo", "nombre", "facultad", "estado"]
        labels = {
            "codigo": "Código",
            "nombre": "Nombre del programa",
            "facultad": "Facultad",
            "estado": "Activo",
        }
