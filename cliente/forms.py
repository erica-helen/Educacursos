from .models import Venda
from django import forms
from administrador.forms import CursoForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']