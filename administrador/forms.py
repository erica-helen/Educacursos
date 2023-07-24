from .models import Curso
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
