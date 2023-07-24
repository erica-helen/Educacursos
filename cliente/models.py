from django.db import models
from django.contrib.auth.models import AbstractUser, Group
#novo
from administrador.models import Curso
#novo

# Create your models here.

class Venda(models.Model):
 
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    #novo
    comprado = models.BooleanField(default=False)
    curso = models.ForeignKey(Curso,on_delete=models.PROTECT, blank=True, null=True)


    def __str__(self)-> str:
        return self.nome

