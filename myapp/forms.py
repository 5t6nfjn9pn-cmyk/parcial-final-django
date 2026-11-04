from django import forms
from myapp.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "last_name", "age", "status"]
        labels = {
            "name": "Nombre",
            "last_name": "Apellido",
            "age": "Edad",
            "status": "Activo",
        }