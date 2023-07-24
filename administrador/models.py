from datetime import datetime
from django.db import models

# Create your models here.


class Curso(models.Model):
    TIPOS = (
        ("online" , "online"),
        ("presencial", "presencial"),
    )

    titulo = models.CharField(max_length=200)
    ano = models.SmallIntegerField(blank=True, null= True, default=datetime.now().year)
    imagem = models.ImageField(upload_to='cursos/',  blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    valor = models.CharField(max_length=100, blank=True, null=True)
    intrutor = models.CharField(max_length=200, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True, choices=TIPOS, default='online')
    #sold = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.titulo +  " de " + str (self.ano) 
    
    class Meta:
        ordering = ['titulo']


