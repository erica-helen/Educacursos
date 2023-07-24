from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

# Create your views here.
def home(request):
    cursos = Curso.objects.all()  # Recupera todos os cursos do banco de dados
    return render(request, "administrador/home.html", {'cursos': cursos})
    #return render(request, "administrador/home.html")

def add(request):
    formulario = CursoForm
    if request.method=="POST":
        formulario = CursoForm(request.POST , request.FILES)
        formulario.save()
        return redirect ("administrador:home")
    return render(request, "administrador/add.html", {'formulario':formulario} )


def delete(request, id):
    #eliminar o livro com primary key igual ao parametro url id
    curso1 = Curso.objects.filter(pk=id)
    curso1.delete()
    return redirect("administrador:home")

def edit(request, id):
    #obter a informação antiga do livro
    curso1 = Curso.objects.get(pk=id)
    formulario = CursoForm(instance = curso1)
    if request.method=="POST":
        formulario = CursoForm(request.POST, request.FILES, instance=curso1)
        formulario.save()
        return redirect("administrador:home")
    return render(request, "administrador/edit.html", {'formulario':formulario})



